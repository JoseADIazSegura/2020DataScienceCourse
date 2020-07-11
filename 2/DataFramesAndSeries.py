import pandas as pd

data = pd.read_csv("../dataSrc/9.1 lsd_math_score_data.csv.csv")
OnlyLSD = data['LSD_ppm']
print(OnlyLSD)

data['Test_Subject'] = 'Jennifer Lopez'

data['High_Score'] = 100
# Challenge: Overwrite values in rows for High_Score to equal average score + 100
data['High_Score'] =  data['Avg_Math_Test_Score'] + data['High_Score']
print(data)

# Challenge: Sqyuare the values sotred inside High_Score
data['High_Score'] = data['High_Score'] ** 2
print(data)

# Challenge: Create a list called columnList. Put 'LSD_ppm' and 'Avg_Math_Test_Score' inside.
#columnList = ['LSD_ppm','Avg_Math_Test_Score']
cleanData = data[['LSD_ppm','Avg_Math_Test_Score']]
print(cleanData)

del data['Test_Subject']
print(data)
del data['High_Score']
print(data)