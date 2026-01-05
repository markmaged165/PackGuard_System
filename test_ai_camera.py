import cv2
import time
from inspection_functions import inspect_product

cap = cv2.VideoCapture(0)

print("Camera Ready.")
print("Press 's' to SCAN (5 samples).")
print("Press 'q' to QUIT.")

while True:
    ret, frame = cap.read()
    if not ret: 
        break

    cv2.imshow('Quality Control Camera', frame)
    key = cv2.waitKey(1) & 0xFF

    # --- THE VOTING LOOP ---
    if key == ord('s'):
        print("\n--- Starting Scan ---")
        scan_results = [] # List to hold [0, 1, 0, 1, 0]

        # Take 5 samples
        for i in range(5):
            # 1. Capture a fresh frame
            ret, current_frame = cap.read()
            if not ret: break

            # 2. Check the product using your logic
            is_good = inspect_product(current_frame)

            # 3. Add result to list (1 for Good, 0 for Bad)
            if is_good:
                scan_results.append(1)
                print(f"  Sample {i+1}: ✅ Good")
            else:
                scan_results.append(0)
                print(f"  Sample {i+1}: ❌ Defect")
            
            # Wait a tiny bit between shots
            time.sleep(0.1)

        # --- CALCULATE FINAL RESULT ---
        print(f"DEBUG Votes List: {scan_results}")
        
        # Calculate average (Total '1's / 5)
        good_votes = scan_results.count(1)
        
        if good_votes >= 3: # If 3 or more are Good
            print(">>> FINAL DECISION: ✅ PRODUCT OK")
        else:
            print(">>> FINAL DECISION: ❌ DEFECT DETECTED")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()