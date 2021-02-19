
# User-Defined Function with one parameter
def fahrenheitToCelsius(t):
    return (5/9)*(t - 32)

# User-Defined Function with several parameters
def futureValue(p, r, m, t):
    ## Find the future value of a savings account deposit
    # p - principal, the amount deposited
    # r - annual rate of interest in decimal form
    # m - number of times interest is compounded per year
    # t - number of years
    i = r / m    # interest rate per period
    n = m * t  # total numbers of times interest is compounded
    amount = p * ((1 + i) ** n)
    return amount