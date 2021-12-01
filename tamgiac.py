import math
while True:
    canh1 = float(input('Do dai canh 1:'))
    canh2 = float(input('Do dai canh 2:'))
    canh3 = float(input('Do dai canh 3:'))
    if abs(canh1 - canh2) < canh3 < canh1 + canh2:
        print('Tam giac hop le')
        break
    else:
        print('Tam giac khong hop le, moi ban nhap lai')
chuvi=canh1+canh2+canh3
p=chuvi//2
dientich=math.sqrt(p*(p-canh1)*(p-canh2)*(p-canh3)) #hê-rông
print(f'Chu vi tam giac: {chuvi:.0f}')
print(f'Dien tich tam giac: {dientich:.3f}')