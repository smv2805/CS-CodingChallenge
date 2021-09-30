n,m,maxSum=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
count=0
while(maxSum!=0):
    if(a==[] and b==[]):
        break
    elif(a==[]):
        if(maxSum-b[0]>=0):
            count+=1
            maxSum=maxSum-b[0]
            b.pop(0)
        else:
            break
    elif(b==[]):
        if(maxSum-a[0]>=0):
            count+=1
            maxSum=maxSum-a[0]
            a.pop(0)
        else:
            break
    
        
    elif(a[0]<b[0]):
        if(maxSum-a[0]>=0):
            count+=1
            maxSum=maxSum-a[0]
            a.pop(0)
        else:
            break
    else:
        if(maxSum-b[0]>=0):
            count+=1
            maxSum=maxSum-b[0]
            b.pop(0)
        else:
            break
        
print(count)            