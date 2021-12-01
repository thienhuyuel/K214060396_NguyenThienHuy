def tong(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s
n=int(input('nhập vào số N:'))
print("Tổng N là:",tong(n))