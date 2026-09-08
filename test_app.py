import pytest
from app import calculate_risk_score, portfolio_risk_score

def test_calculate_risk_score():
    assert calculate_risk_score(0.2, 0.5) == pytest.approx(0.1)

def test_portfolio_risk_score():
    holdings = [(0.25, 0.4), (0.15, 0.35), (0.30, 0.25)]
    assert portfolio_risk_score(holdings) == pytest.approx(0.22)
