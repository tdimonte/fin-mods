#The Sharpe ratio was developed by Nobel laureate William F. Sharpe and is used to help investors understand the return of an investment compared to its risk. The ratio is the average return earned in excess of the risk-free rate per unit of volatility or total risk. Volatility is a measure of the price fluctuations of an asset or portfolio.

#Rp = return of portfolio
#Rf = risk-free rate
#σp = standard deviation of the portfolio's excess return

Rp = float(input("Enter Rp: "))
Rf = float(input("Enter Rf: "))
σp = float(input("Enter σp: "))

def sharpe_ratio(Rp, Rf, σp):
    ratio = (Rp - Rf) / σp
    return(ratio)

print(sharpe_ratio(Rp, Rf, σp))
