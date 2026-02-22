                            OLS Regression Results                            
==============================================================================
Dep. Variable:            Total_Sales   R-squared:                       0.884
Model:                            OLS   Adj. R-squared:                  0.882
Method:                 Least Squares   F-statistic:                     369.3
Date:                Sun, 22 Feb 2026   Prob (F-statistic):           4.40e-46
Time:                        20:08:09   Log-Likelihood:                -1185.2
No. Observations:                 100   AIC:                             2376.
Df Residuals:                      97   BIC:                             2384.
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const      -1.217e+05   9668.294    -12.586      0.000   -1.41e+05   -1.02e+05
Price          4.6106      0.249     18.518      0.000       4.116       5.105
Quantity    2.643e+04   1338.869     19.741      0.000    2.38e+04    2.91e+04
==============================================================================
Omnibus:                        1.152   Durbin-Watson:                   2.057
Prob(Omnibus):                  0.562   Jarque-Bera (JB):                1.077
Skew:                           0.086   Prob(JB):                        0.584
Kurtosis:                       2.522   Cond. No.                     8.25e+04
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 8.25e+04. This might indicate that there are
strong multicollinearity or other numerical problems.