# While1
A = int(input("A: "))
B = int(input("B: "))
while A >= B:
    A -= B
print(A)

# While2
A = int(input("A: "))
B = int(input("B: "))
count = 0
while A >= B:
    A -= B
    count += 1
print(count)

# While3
N = int(input("N: "))
K = int(input("K: "))
while N >= K:
    N -= K
print(N)

# While4
n = int(input("n: "))
x = 1
while x < n:
    x *= 3
if x == n:
    print("3 - ning darajasi")
else:
    print("3 - ning darajasi emas")

# While5
n = int(input("n: "))
x = 1
while x < n:
    x *= 2
if x == n:
    print("2 - ning darajasi")
else:
    print("2 - ning darajasi emas")

# While6
n = int(input("n: "))
result = 1
i = n
while i > 1:
    result *= i
    i -= 2
print(result)

# While7
n = int(input("n: "))
k = 1
while k * k <= n:
    k += 1
print(k - 1)

# While8
n = int(input("n: "))
k = 1
while k * k < n:
    k += 1
print(k)

# While9
n = int(input("n: "))
k = 0
while 3 ** k <= n:
    k += 1
print(k)

# While10
n = int(input("n: "))
k = 0
while 3 ** k < n:
    k += 1
print(k)

# While11
n = int(input("n: "))
k = 0
sum_ = 0
while sum_ < n:
    k += 1
    sum_ += k
print(k, sum_)

# While12
n = int(input("n: "))
k = 0
sum_ = 0
while sum_ + k + 1 <= n:
    k += 1
    sum_ += k
print(k, sum_)

# While13
a = float(input("a: "))
sum_ = 0.0
k = 0
while sum_ < a:
    k += 1
    sum_ += 1 / k
print(k, sum_)

# While14
a = float(input("a: "))
sum_ = 0.0
k = 0
while sum_ + 1 / (k + 1) <= a:
    k += 1
    sum_ += 1 / k
print(k, sum_)
