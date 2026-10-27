import numpy as np

a = np.array([[10, 100, 200],
              [50, 150, 250]], dtype=np.uint8)

print("a.dtype: ", a.dtype)
print("a.shape: ", a.shape)
print("a.ndim: ", a.ndim)
print("a.size: ", a.size)
print("a.nbytes: ", a.nbytes)
print("a[1, 2]: ", a[1, 2])
print("a[0, 1]: ", a[0, 1])
print("a+10: ", a + 10)
print("a-20: ", a - 20)
print("a*2: ", a * 2)
print("a.max(): ", a.max())
print("a.max(axis=0): ", a.max(axis=0))
print("a.max(axis=1): ", a.max(axis=1))
