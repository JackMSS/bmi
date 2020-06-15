weight = input('請輸入你的體重(kg)')
height = input('請輸入你的身高(m)')
weight = float(weight)
height = float(height)
bmi = weight / (height*height)
bmi = float(bmi)
print('你的BMI為', bmi)
if bmi < 18.5 :
    print('體重過輕！')
elif bmi >= 18.5 and bmi < 24 :
	print('正常體重喔！')
elif bmi >=27 and bmi < 30 :
	print('輕度肥肥')
elif bmi >=30 and bmi < 35 :
	print('中度肥肥')
else:
	print('肥豬喔該減肥了')