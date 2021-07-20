# Solution 1
def reverse_list(a):
    def swap(a, i, j):
        a[i], a[j] = a[j], a[i]
    for i in range(len(a) // 2):
        swap(a, i, -1 - i)

# Solution 2

def reverse_list(a):
    for i in range(len(a) // 2):
        ind1 = i
        ind2 = len(a) - 1 - i
        # swap a[ind1] and a[ind2]
        temp = a[ind1]
        a[ind1]= a[ind2]
        a[ind2] = temp 
