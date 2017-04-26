# _*_ coding: cp949 _*_

print '직각삼각형 그리기굈'
d = float(raw_input("변의 길이 : "))

for i in range(int(d)+1) :
    print ('*' * i)

area = float((d ** 2) / 2)
print ('넓이 : %s' %area)

raw_input()