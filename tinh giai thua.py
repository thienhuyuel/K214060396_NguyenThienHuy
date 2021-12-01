def tinhgiaithua(a):
    gt=1
    if a==0 or a==1:
        return gt
    else:
        for i in range(1,a+1):
            gt*=i
        return gt
a=int(input('Nhập vào số cần tính giai thừa: '))
print("{}! = {}".format(a,tinhgiaithua(a)))