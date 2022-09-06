import sys
input = lambda: sys.stdin.readline().rstrip()
def binary(arr, num, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == num:
            return True
        if arr[mid] > num:
            end = mid-1
        else:
            start = mid + 1           
    return False
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
c_arr = list(map(int, input().split()))
for c in c_arr:
    if binary(arr, c, 0, n-1):
        print(1)
    else:
        print(0)