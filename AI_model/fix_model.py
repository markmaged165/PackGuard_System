import h5py
import json

FILENAME = "final_product_model.h5"

print(f"--- STARTING NUCLEAR FIX FOR: {FILENAME} ---")

try:
    # Open file in Read/Write mode
    f = h5py.File(FILENAME, mode="r+")
    
    # 1. Read the old configuration
    if "model_config" not in f.attrs:
        print("Error: No model config found.")
        exit()
        
    raw_data = f.attrs["model_config"]
    
    # Handle different data types (bytes vs string vs numpy)
    if hasattr(raw_data, 'decode'):
        config_str = raw_data.decode('utf-8')
    else:
        config_str = str(raw_data)

    config_dict = json.loads(config_str)
    
    # 2. Define the cleaning function
    changes_made = False
    
    def clean_config(item):
        global changes_made
        if isinstance(item, dict):
            if 'class_name' in item and item['class_name'] == 'Conv2D':
                if 'config' in item and 'groups' in item['config']:
                    print("Found 'groups' setting... Removing it.")
                    del item['config']['groups']
                    changes_made = True
            for value in item.values():
                clean_config(value)
        elif isinstance(item, list):
            for i in item:
                clean_config(i)

    # 3. Apply the cleaning
    clean_config(config_dict)
    
    if changes_made:
        # 4. DELETE the old config entirely (Solves the U4215 error)
        del f.attrs["model_config"]
        
        # 5. WRITE the new config as fresh bytes
        new_json = json.dumps(config_dict)
        f.attrs.create("model_config", new_json.encode('utf-8'))
        print("✅ SUCCESS: Config updated and saved.")
    else:
        print("NOTE: No 'groups' setting found. The model might already be fixed.")
        
    f.close()
    print("---------------------------------------------")
    print("NOW: Run your inspection_functions.py script.")

except Exception as e:
    print(f"❌ CRITICAL ERROR: {e}")