import numpy as np

def montecarlo_option_price(S, K, T, r, sigma, n=100000, option_type='call', conf_level=0.95):
    """
    Estimate the price of a European option (call or put) using Monte Carlo simulation under Black-Scholes model.

    Parameters:
    - S : float, initial stock price
    - K : float, strike price
    - T : float, time to maturity (in years)
    - r : float, risk-free interest rate (annual)
    - sigma : float, volatility of the underlying asset (annual)
    - n : int, number of Monte Carlo simulations (default=100000)
    - option_type : str, 'call' or 'put' (default='call')
    - conf_level : float, confidence level for the interval (default=0.95)

    Returns:
    - price : float, estimated option price
    - conf_interval : tuple, lower and upper bounds of the confidence interval
    """

    # Generate n samples from standard normal distribution
    Z = np.random.normal(0, 1, n)

    # Simulate asset price at maturity using Black-Scholes formula
    St = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

    # Calculate payoffs depending on option type
    if option_type == 'call':
        payoffs = np.maximum(St - K, 0)
    elif option_type == 'put':
        payoffs = np.maximum(K - St, 0)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    # Discount payoffs back to present value
    discounted_payoffs = np.exp(-r * T) * payoffs

    # Estimate option price as the mean of discounted payoffs
    price = np.mean(discounted_payoffs)

    # Calculate standard error
    std_error = np.std(discounted_payoffs) / np.sqrt(n)

    # Calculate confidence interval using normal approximation
    from scipy.stats import norm
    z = norm.ppf(0.5 + conf_level / 2)
    conf_interval = (price - z * std_error, price + z * std_error)

    return price, conf_interval

price, ci = montecarlo_option_price(S=100, K=100, T=1, r=0.05, sigma=0.2, n=100000, option_type='call')
print(f"Estimated call option price: {price:.4f}")
print(f"{95}% confidence interval: [{ci[0]:.4f}, {ci[1]:.4f}]")
