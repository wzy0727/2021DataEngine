import pandas as pd

car_complain = pd.read_csv('car_complain.csv')

car_complain = car_complain.drop(columns='problem').join(car_complain.problem.str.get_dummies(','))

print(car_complain)

brand_group = car_complain.groupby(['brand'])['id'].agg(['count']).sort_values('count', ascending=False)

car_model_group = car_complain.groupby(['car_model'])['id'].agg(['count']).sort_values('count', ascending=False)

mean_brand_group = car_complain.groupby(['brand','car_model'])['id'].agg(['count']).groupby(['brand']).mean().sort_values('count',ascending=False)

