def calc_vc_structure(
        committed_capital=100,
        carry=20,
        fee_percent=.02,
        fund_life=10):

    committed_capital = int(committed_capital)
    carry = float(carry)
    if carry >1:
        carry=carry/100
        pass
    fee_percent = float(fee_percent)
    fund_life = int(fund_life)

    fees = calc_total_fees(committed_capital, fee_percent, fund_life)
    investment_capital = calc_investment_capital(committed_capital, fees)
    fee_structure = calc_fee_structure(committed_capital, investment_capital)
    gp_percent = calc_gp_percent(committed_capital, investment_capital, carry)

    return [investment_capital, fee_structure, gp_percent, fees]

def calc_total_fees(
        committed_capital,
        fee_percent,
        fund_life):

    fees = (committed_capital*fee_percent*fund_life)
    return fees

def calc_investment_capital (
        committed_capital,
        fees):

    investment_capital = committed_capital - fees
    return investment_capital

def calc_fee_structure(
        committed_capital,
        investment_capital):

    investment_capital = float(investment_capital)
    committed_capital = float(committed_capital)

    fee_structure = committed_capital/investment_capital
    return fee_structure

def calc_gp_percent(
        committed_capital,
        investment_capital,
        carry):

    GVM = 2.5

    gp_percent = carry * (GVM * investment_capital-committed_capital)/(GVM * investment_capital)
    return gp_percent
