# Solution 1
def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

# Solution 2

def factorial(n):
    if n == 1:
        return 1
    return n* factorial(n - 1)
        
