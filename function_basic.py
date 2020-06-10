def multiply(x, y):
    return x * y

value = multiply(4, 6) + multiply(22, 300)
print(value)

def calculate(max):
    sum = 0
    for n in range(1, max + 1):
        sum = sum + n
    print(sum)

calculate(10)
calculate(100)

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != k) and (i != j) and (j != k):
                print(i, j, k)

import practice_counts