import time

def factorial_memoized (n):
    mem = []
    for i in range(0,n+1):
        mem.append(None)
    return helper_factorial(n, mem)

def helper_factorial (n, mem):
    if n == 0:
        return 1
    if mem[n] == None:
        x = helper_factorial(n-1, mem)
        mem[n] = x
    else:
        x = mem[n]
    return n * x

def factorial_brute (n):
    if n == 0:
        return 1
    return n * factorial_brute(n-1)



start1 = time.time()
num1 = factorial_memoized(100)
end1 = time.time()

start2 = time.time()
num2 = factorial_brute(100)
end2 = time.time()

print("Brute Forced = ", (end1 - start1))
print("factorial_brute = ", num2)
print("Memoized = ", (end2 - start2))
print("factorial_memoized = ", num1)