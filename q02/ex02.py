import numpy as np
# 1. תמונה שחורה בגווני אפור (גובה 100, רוחב 200) - כולה אפסים (0 = שחור)
black_img = np.zeros((100,200), dtype=np.uint8)

# 2. תמונה לבנה באותו גודל - כולה 255 (255 = לבן)
white_img = np.full((100,200), 255, dtype=np.uint8)

# 3. תמונה צבעונית (RGB) - גובה 100, רוחב 200, 3 ערוצי צבע
# ה-shape חייב להיות (100, 200, 3)
#  הצבע הנבחר אדום: [255, 0, 0] (Red=255, Green=0, Blue=0)
color_img = np.full((100,200,3), [255, 0, 0], dtype=np.uint8)

#4. הדפסה
print("--- תמונה שחורה ---")
print(f"shape: {black_img.shape}, ndim: {black_img.ndim}, size: {black_img.size}, nbytes: {black_img.nbytes}")

print("--- תמונה לבנה ---")
print(f"shape: {white_img.shape}, ndim: {white_img.ndim}, size: {white_img.size}, nbytes: {white_img.nbytes}")

print("--- תמונה צבעונית ---")
print(f"shape: {color_img.shape}, ndim: {color_img.ndim}, size: {color_img.size}, nbytes: {color_img.nbytes}")


#  בדיקה בקוד עבור נפח זיכרון:
img_1080p_bytes = np.zeros((1080, 1920, 3), dtype=np.uint8).nbytes
print("\nזיכרון לתמונת 1080p צבעונית בבתים:", img_1080p_bytes)
 

# לחישוב 12 מגה פיקסל ניתן ליצור מערך בגודל 12,000,000 איברים ב-3 ערוצים:
img_12mp_bytes = np.zeros((12000000, 3), dtype=np.uint8).nbytes
print("זיכרון לתמונת 12MP צבעונית בבתים:", img_12mp_bytes)


# 6. בדיקת המערך b ופעולות סכום
b = np.arange(12).reshape(3, 4)
print("\nהמערך b:")
print(b)
print("b.sum():", b.sum())
print("b.sum(axis=0):", b.sum(axis=0))
print("b.sum(axis=1):", b.sum(axis=1))
print("איברים בפינה:", b[2, 3], b[-1, -1])
