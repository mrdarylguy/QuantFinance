import pandas as pd
import yfinance as yf
import statsmodels.api as sm

#Specify asset + time horzion
risky_asset = "AMZN"
market_benchmark = "^GSPC"
start_date = "2014-01-01"
end_date = "2018-12-31"

#import data from yfinance
df = yf.download([risky_asset, market_benchmark],
                  start=start_date,
                  end=end_date,
                  adjusted=True,
                  progress=False)

#Resample to monthly data and get simple returns
X = df["Adj Close"].rename(columns={risky_asset: "asset",
                                    market_benchmark: "market"}) \
                    .resample("M") \
                    .last() \
                    .pct_change() \
                    .dropna()

#Calculate beta
covariance = X.cov().iloc[0, 1]
benchmark_variance = X.market.var()
beta = covariance/benchmark_variance

#estimate CAPM as linear regression
y = X.pop('asset')
X = sm.add_constant(X)

capm_model = sm.OLS(y, X).fit()
print(capm_model.summary())