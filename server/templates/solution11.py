#La plus rapide a coder, mais elle utilise la function 'min' de Python.

def minimum(arr):
    return min(arr)

# Solution 2

def minimum(arr):
    ans = float('-inf')
    for val in arr:
        ans = min(ans, val)
    return ans

# Solution 3

#Cette solution utilize moins les astuces de Python

def minimum(arr): 
    ans = arr[0]
    n = len(arr)
    for i in range(1, n):
        if ans > arr[i]:
            ans = arr[i]
    return ans

