# Monte Carlo
A method that allows estimating, with reasonable accuracy, the expectation of a random variable or its transformation, the probability of an event, or the cumulative distribution function of a distribution.

This method is based on the law of large numbers. By simulating random variables a very large number of times and then calculating the average of these realizations, one can approximate the expectation.

#  Estimation of a Call Option Price Using Monte Carlo (Black-Scholes)
This project uses the Monte Carlo method to estimate the price of a European call option based on the Black-Scholes model.

## Description
The Black-Scholes model allows modeling the price evolution of a financial asset.
The Monte Carlo method simulates multiple price trajectories at maturity and calculates the discounted average of the payoffs to estimate the option price.

The code simulates the Gaussian random variable Z, calculates the asset price at maturity, and then evaluates the value of the European call option.

## Function 

def montecarlo(S, K, T, r, sigma, n):
    
    """ Estimates the price of a European call option using Monte Carlo.
    Arguments:
    - S: initial price of the underlying asset
    - K: strike price
    - T: maturity (in years)
    - r: annual risk-free interest rate
    - sigma: annual volatility
    - n: number of simulations

    Returns:
    - estimated price of the call option
    """
