import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# المسارات
BASE_DIR = r'C:\Users\markm_pxjw4kd\OneDrive\Desktop\ras_beryy' 
TRAIN_DIR = f'{BASE_DIR}/train'
IMG_SIZE = (150, 150)
BATCH_SIZE = 32

# --- تعديل مولد البيانات (Data Augmentation) ---
# الموديل سيتدرب على نسخ معدلة من الصور (دوران، إضاءة، زووم) ليكون أقوى
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,      # دوران الصورة حتى 20 درجة
    width_shift_range=0.1,  # تحريك بسيط لليمين واليسار
    height_shift_range=0.1, # تحريك للأعلى والأسفل
    brightness_range=[0.8, 1.2], # تغيير شدة الإضاءة
    zoom_range=0.1,         # تكبير وتصغير بسيط
    horizontal_flip=True,   # قلب الصورة أفقياً
    validation_split=0.2    # تقسيم البيانات للتحقق
)

train_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='validation'
)

# --- بناء الموديل مع إضافة Dropout لمنع Overfitting ---
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(512, activation='relu'),
    Dropout(0.5), # حذف عشوائي لـ 50% من الخلايا لمنع الحفظ وتنشيط الفهم
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# التدريب
model.fit(train_generator, epochs=15, validation_data=validation_generator)

# حفظ الموديل الجديد
model.save(f'{BASE_DIR}/final_product_model.h5')
print("Model Updated and Saved!")