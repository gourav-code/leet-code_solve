#heap has n! time complexity and permutation has n*n! time complexity
def swap(arr, a, b):
    arr = list(arr)
    arr[a], arr[b] = arr[b], arr[a]
    arr = ''.join(arr)
    return arr

def heap(n, arr):
    if n == 1:
        print(arr)
    else:
        heap(n-1, arr)

        for i in range(n-1):
            if n%2 == 0:
                arr = swap(arr, i, n-1)
            else:
                arr = swap(arr, 0, n-1)
            
            heap(n-1, arr)
            

def permutation(arr, l, r):
    if l == r:
        print(f"arr:{arr}")
    else:
        for i in range(l, r+1):
            arr = swap(arr, l, i)
            permutation(arr, l+1, r)
            arr = swap(arr, l, i)


arr = 'abd'
#permutation(arr, 0, len(arr)-1)
heap(len(arr),arr)

