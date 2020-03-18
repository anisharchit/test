x=input()
n=int(x)
arr_f = [n]
arr_r = []

arr = [int(i) for i in input().split()]

print(arr)
  
arr_r=arr[::-1]

print(arr_r)

for i in range(n):
    print(i)
    arr_f[i]=int(arr[i])+int(arr_r[i])
  
print(arr_f)