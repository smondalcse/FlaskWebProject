import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

class Predictor:

    def linear_prediction(dataset, yearid):
        X = dataset.iloc[:, 0:1].values
        y = dataset.iloc[:, 1].values
        lin_reg = LinearRegression()
        lin_reg.fit(X, y)

        # Visualising the Linear Regression results
        plt.scatter(X, y, color='red')
        plt.plot(X, lin_reg.predict(X), color='blue')
        plt.title('Truth or Bluff (Linear Regression)')
        plt.xlabel('Position level')
        plt.ylabel('Salary')
        plt.show()
        lin_predict = lin_reg.predict([[yearid]])
        return lin_predict

    def polynomial_prediction(dataset, yearid):
        X = dataset.iloc[:, 0:1].values
        y = dataset.iloc[:, 1].values
        from sklearn.preprocessing import PolynomialFeatures
        poly_reg = PolynomialFeatures(degree=4)
        X_poly = poly_reg.fit_transform(X)
        lin_reg_2 = LinearRegression()
        lin_reg_2.fit(X_poly, y)

        # Visualising the Polynomial Regression results
        plt.scatter(X, y, color='red')
        plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color='blue')
        plt.title('Truth or Bluff (Polynomial Regression)')
        plt.xlabel('Position level')
        plt.ylabel('Salary')
        plt.show()

        # Visualising the Polynomial Regression results (for higher resolution and smoother curve)
        X_grid = np.arange(min(X), max(X), 0.1)
        X_grid = X_grid.reshape((len(X_grid), 1))
        plt.scatter(X, y, color='red')
        plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color='blue')
        plt.title('Truth or Bluff (Polynomial Regression)')
        plt.xlabel('Position level')
        plt.ylabel('Salary')
        plt.show()
        poly_predict = lin_reg_2.predict(poly_reg.fit_transform([[yearid]]))
        return poly_predict
