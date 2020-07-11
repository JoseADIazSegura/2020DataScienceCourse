import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("../dataSrc/3.2 cost_revenue_clean.csv")

print(data.describe())

productionBudget = DataFrame(data, columns=['production_budget_usd'])
revenue = DataFrame(data, columns=['worldwide_gross_usd'])

plt.figure(figsize=(10,6))
plt.scatter(productionBudget,revenue,alpha=0.3)
plt.title('Film Cost vs Global Revenue')
plt.xlabel('Production Budget ')
plt.ylabel('Worldwide Gross $')
plt.ylim(0,3000000000)
plt.xlim(0,450000000)
plt.xlim()
plt.show()

#Linear Regression
regression = LinearRegression()
regression.fit(productionBudget,revenue)

# Slope Coefficiente
regression.coef_ # theta_1

#Intercept
regression.intercept_

# Goodness of fit ( r² or R²)
regression.score(productionBudget,revenue)
print(regression.score(productionBudget,revenue))

plt.figure(figsize=(10,6))
plt.scatter(productionBudget,revenue,alpha=0.3)
plt.plot(productionBudget,regression.predict(productionBudget),color='red', linewidth=4)
plt.title('Film Cost vs Global Revenue')
plt.xlabel('Production Budget ')
plt.ylabel('Worldwide Gross $')
plt.ylim(0,3000000000)
plt.xlim(0,450000000)
plt.xlim()
plt.show()
