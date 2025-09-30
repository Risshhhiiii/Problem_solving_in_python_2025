arr = [6,7,2,1,1,3,5,6,7,2,1,2]
k = 9
l,r=0,0
summ , max_sum = 0 , 0
while r < len(arr):
    summ+=arr[r]
    while summ > k :
        summ-=arr[l]
        l+=1
    max_sum = max(max_sum,r-l+1)
    r+=1
print(max_sum)