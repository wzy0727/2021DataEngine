import numpy as np

persontype = np.dtype({
     'names':['name','chinese','math','english'],
     'formats':['S32','i','i','i']
})

peoples = np.array([
     ("Zhangfei",68,65,30),("Guanyu",95,76,98),("Liubei",98,86,88),
     ("Dianwei",90,88,77),("Xuchu",80,90,90)],dtype=persontype)

chinese_score = peoples['chinese']
math_score = peoples['math']
english_score = peoples['english']

print("       |平局成绩" + "|最小成绩" + "|最大成绩" + "|  方差  " + "|标准差")
print("chinese|  %5.2f |   %d   |   %d   | %5.2f | %5.2f "
          %(np.mean(chinese_score), min(chinese_score), max(chinese_score), np.var(chinese_score), np.std(chinese_score)))
print("math   |  %5.2f |   %d   |   %d   | %5.2f  | %5.2f "
          %(np.mean(math_score), min(math_score), max(math_score), np.var(math_score), np.std(math_score)))
print("english|  %5.2f |   %d   |   %d   | %5.2f | %5.2f "
          %(np.mean(english_score), min(english_score), max(english_score), np.var(english_score), np.std(english_score)))

ranking = sorted(peoples,key=lambda x:x[1]+x[2]+x[3], reverse=True)
print(ranking)
