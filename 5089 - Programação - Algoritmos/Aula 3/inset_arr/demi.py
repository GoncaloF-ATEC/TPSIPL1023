
import time

arr = [1,2,3,4,5,6,22,423,423,423,423,423,42,423,423,423,42,423,432]


start = time.perf_counter()
for i in range(10000):
    arr.insert(0, 99)

end = time.perf_counter()
t = (end - start)
print(f"{i}\t\t{t:0.10f}")

# 9999		0.0005088210
# 9999		0.0088538830