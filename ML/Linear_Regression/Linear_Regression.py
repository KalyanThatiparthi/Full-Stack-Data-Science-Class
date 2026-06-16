
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.impute import SimpleImputer
dataset = pd.read_csv(r'C:\Users\Jagatjyoti\Jagat_Code\04-05-2026\Salary_Data.csv')

# dataset2 = pd.read_csv('C:\\Users\\Jagatjyoti\\Jagat_Code\\02-05-2026\\Data.csv')
x = dataset.iloc[:, :-1].values
# DEPENDENT VARIABLE
y = dataset.iloc[:, -1].values

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8, test_size= 0.2, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)
print(y_pred)

comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(comparison)


plt.scatter(x_test,y_test,color='red')
plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(x_train,y_train,color='red')
plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()  

model_coeff = regressor.coef_
print("Coefficient:", model_coeff)

model_intercept = regressor.intercept_
print("Intercept:", model_intercept)

y_12 = model_coeff * 12 + model_intercept
print("Predicted salary for 12 years of experience:", y_12)

y_20 = model_coeff * 20 + model_intercept
print("Predicted salary for 20 years of experience:", y_20)

y_30 = model_coeff * 30 + model_intercept
print("Predicted salary for 30 years of experience:", y_30)
