driving = input('請問你有開過車嗎?')
if driving != '有' and driving != '沒有':
    print('只能輸入 有/沒有')
    raise SystemExit  #錯誤，讓系統停止
age = input('請問你的年齡?')
age = float(age)
if driving == '有':
    if age >=18:
        print('通過測驗')
    else:
    	print('無照駕駛')
elif driving == '沒有':
    if age >=18:
    	print('快去考')
    else:
    	print('很好，沒無照')
