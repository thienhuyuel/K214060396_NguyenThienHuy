flag=0
while True:
#nhập ngày tháng năm
    day=int(input('Nhập ngày:'))
    month=int(input('Nhập tháng:'))
    year=int(input('Nhập năm:'))
#kiểm tra
    if year%4==0:
        print(year,'là năm nhuận')
        if month==2 and day<=29:
            print('Tháng',month,'năm',year,'có 29 ngày')
            break
        elif (month==1 or month==3 or month==5 or month==6 or month==8 or month==10 or month==12) and (day>0 and day<=31):
            print('Tháng',month,'năm',year,'có 31 ngày')
            break
        elif (month==4 or month==7 or month==9 or month==11) and (day>0 and day<=30):
            print('Tháng',month,'năm',year,'có 30 ngày')
            break
        else:
            print('Bạn đã nhập sai!\nVui lòng nhập lại')
    else:
        if month==2 and day <= 28:
            print('Tháng', month,'năm',year, 'có 28 ngày')
            break
        elif (month==1 or month==3 or month==5 or month==6 or month==8 or month==10 or month==12) and (day>0 and day<=31):
            print('Tháng', month,'năm',year, 'có 31 ngày')
            break
        elif (month==4 or month==7 or month==9 or month== 11) and (day>0 and day<=30):
            print('Tháng', month,'năm',year, 'có 30 ngày')
            break
        else:
            print('Bạn đã nhập sai!\nVui lòng nhập lại')