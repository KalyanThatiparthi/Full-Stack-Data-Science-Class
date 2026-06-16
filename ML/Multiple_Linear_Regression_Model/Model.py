import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r'C:\Users\Jagatjyoti\Jagat_Code\11-05-2026\Investment.csv')
x = dataset.iloc[:, :-1]
y = dataset.iloc[:,4]
    
x = pd.get_dummies(x, dtype=int)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train)

y_pred = regression.predict(X_test)

print(y_pred)   


print(regression.coef_)

print(regression.intercept_)

x=np.append(arr=np.full((50,1),42467).astype(int), values=x, axis=1)

import statsmodels.api as sm
# import statsmodels.formula.api as smf
x_opt = x[:, [0,1,2,3,4,5]]
#OridanaryLeastSquares
regressor_OLS = sm.OLS(endog=y, exog=x_opt).fit()
regressor_OLS.summary()


# import statsmodels.formula.api as smf
x_opt = x[:, [0,1,2,3,5]]
#OridanaryLeastSquares
regressor_OLS = sm.OLS(endog=y, exog=x_opt).fit()
regressor_OLS.summary()

import statsmodels.api as sm
# import statsmodels.formula.api as smf
x_opt = x[:, [0,1,2,3]]
#OridanaryLeastSquares
regressor_OLS = sm.OLS(endog=y, exog=x_opt).fit()
regressor_OLS.summary()

# import statsmodels.formula.api as smf

x_opt = x[:, [0,1,3]]
#OridanaryLeastSquares
regressor_OLS = sm.OLS(endog=y, exog=x_opt).fit()
regressor_OLS.summary()



import statsmodels.api as sm

x = sm.add_constant(x)
model = sm.OLS(y, x).fit()
print(model.summary())