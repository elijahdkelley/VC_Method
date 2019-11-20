
def calc_fee_structure(committed_capital, investment_capital):
    investment_capital = float(investment_capital)
    committed_capital = float(committed_capital)

    fee_structure = committed_capital/investment_capital
    return fee_structure

def calc_gp_percent(committed_capital, carry = ".20", fee_percent = ".02", fund_life = "10"):
    carry = float(carry)
    fee_percent = float(fee_percent)
    committed_capital = int(committed_capital)
    fund_life = int(fund_life)
    fees = (committed_capital*fee_percent*fund_life)
    investment_capital = committed_capital - fees
    GVM = 2.5

    gp_percent = carry * (GVM * investment_capital-committed_capital)/(GVM * investment_capital)
    return gp_percent

#Debug
#test = calc_fee_structure(100,80)
#print(test)

#test2 = calc_gp_percent(100)
#print(test2)

#input("")
