from VCStructure import calc_vc_structure
from ExpectedReturns import calc_lp_valuation
from CostofCapital import calc_cost_of_capital

#input variables
investment_amount=input("Amount to Invest ($mm): ")
ownership=input("% Ownership: ")
exit_value=input("Expected Exit Value ($mm): ")
exit_years=input("Years Until Exit: ")
probability_success=input("Probability of Successful Exit: ")
expected_retention=input("Expected Retention of Investment: ")

investment_amount = int(investment_amount)

#calculate cost of capital based on portfolio view
#calc_cost_of_capital(factor_type="",alpha=0,risk_free_rate=0,return_market_portfolio=0,market_beta_hat=0,market_beta_hat_size=0,market_beta_hat_value=0,market_beta_hat_liquidity=0,size_t=0,value_t=0,liquidity_t=0)
#TODO create inputs for factor types
cost_of_capital = calc_cost_of_capital()

#calc_vc_structure(committed_capital, carry, fee_percent, fund_life) default values are committed_capital = 100, carry = 20%, fee_percent = 2%, fund_life = 10 years
vc_structure = calc_vc_structure()
fee_structure = vc_structure[1]
gp_percent = vc_structure[2]

lp_valuation = calc_lp_valuation (cost_of_capital, exit_years, probability_success, expected_retention, exit_value, ownership, gp_percent)
lp_cost = investment_amount*fee_structure

expected_return = lp_valuation-lp_cost
expected_return = round(expected_return, 2)
#logic

if expected_return>=0:
    print(f"You should invest. Expected LP return is, ${expected_return}mm")
else:
    print(f"You should not invest. Expected LP return is, ${expected_return}mm")

input("")
