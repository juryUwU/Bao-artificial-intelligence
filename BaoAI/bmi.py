

print('\033[0;34mKIỂM TRA CHỈ SỐ BMI:')
def BMI(cannang,chieucao):
    return cannang/(chieucao**2)

def PhanLoai(BMI):
    print('\033[0;32mMức độ béo/gầy:')
    if BMI < 18.5:
        return '\033[0;37mBạn quá gầy'
    elif BMI <= 24.9:
        return  '\033[0;37mBạn bình thường'
    elif BMI <= 29.9:
        return '\033[0;37mBạn hơi béo'
    elif BMI <= 34.9:
        return '\033[0;37mBạn béo phì cấp độ 1'
    elif BMI <= 39.9: 
        return '\033[0;37mBạn béo phì cấp độ 2'
    else:
        return '\033[0;37mBạn béo phì cấp độ 3'

def NguyCoBenh(BMI):
    print('\033[0;32mNguy cơ bệnh:')
    if BMI < 18.5:
        return '\033[0;37mthấp'
    elif BMI <= 24.9:
        return  '\033[0;37mtrung bình'
    elif BMI <= 29.9:
        return '\033[0;37mcao'
    elif BMI <= 34.9:
        return '\033[0;37mcao'
    elif BMI <= 39.9:
        return '\033[0;37mrất cao'
    else:
        return '\033[0;37mNguy hiểm'

x = float(input('\033[0;33mNhập vào cân nặng của bạn:'))
y = float(input('\033[0;33mNhập vào chiều cao của bạn:'))
bmi = BMI(x, y)
print('BMI của bạn = ', bmi)
print(PhanLoai(bmi))
print(NguyCoBenh(bmi))

