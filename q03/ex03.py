import numpy as np
#1.
x = np.array([100, 200, 250], dtype=np.uint8)

#[110,210,4]
print(x + 10)
#[200,44,94]
print(x + 100)
#[206,50,100]
print(x - 150)
#[200,144,244]
print(x * 2)
#[200,300,350]
print(x.astype(np.int16) + 100)
#[150,300,375]
print(x * 1.5)
#float64
print((x * 1.5).dtype)

#2. 
#[400,500,550]
try:
    print(x + 300)
except OverflowError as e:
    print("נתפסה שגיאת גלישה:", e)
#3.
def add_safe(x,b):
  x_wide = x.astype(np.int16) + b
  x_clipped = np.clip(x_wide, 0, 255)
  return x_clipped.astype(np.uint8)

x = np.array([100, 200, 250], dtype=np.uint8)

print("b=100:", add_safe(x, 100))
print("b=150:" , add_safe(x, -150))

#5.
# 1. יצירת סקלר/מערך עם הערך המקסימלי של int8 (127)
val = np.int8(127)

print("הערך המקורי:", val)
print("טיפוס הנתונים:", val.dtype)

# 2. הוספת 1 לגרימת גלישה (Overflow)
result = val + np.int8(1)

print("תוצאת 127 + 1:", result)
print("טיפוס התוצאה:", result.dtype)