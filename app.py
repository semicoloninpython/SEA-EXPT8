def calculate_risk_score(volatility, weight):
    """Simple weighted risk contribution for a stock in a portfolio."""
    return round(volatility * weight, 2)

def portfolio_risk_score(holdings):
    """holdings: list of (volatility, weight) tuples"""
    return round(sum(calculate_risk_score(v, w) for v, w in holdings), 2)

if __name__ == "__main__":
    print("Stock Portfolio Risk Scorer - CI/CD Demo")
    sample_portfolio = [(0.25, 0.4), (0.15, 0.35), (0.30, 0.25)]
    print("Portfolio Risk Score:", portfolio_risk_score(sample_portfolio))
