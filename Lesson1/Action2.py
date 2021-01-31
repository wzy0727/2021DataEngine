import pandas as pd

Data = {'Chinese':[68,95,98,90,80],'Math':[65,76,86,88,90],'English':[30,98,88,77,90]}
Score = pd.DataFrame(Data,index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'], \
     columns=['Chinese', 'Math', 'English'])

df1=pd.DataFrame(Score.mean(),columns=['mean'])
df2=pd.DataFrame(Score.min(),columns=['min'])
df3=pd.DataFrame(Score.max(),columns=['max'])
df4=pd.DataFrame(Score.var(),columns=['var'])
df5=pd.DataFrame(Score.std(),columns=['std'])

df=pd.concat((df1,df2,df3,df4,df5), axis = 1,ignore_index = False, join = 'outer')
print(df)

Score['Sum'] = Score.apply(lambda x: x.sum(), axis=1)
ranking = Score.sort_values('Sum')
print(ranking)
