#input variables
probability_success=input("Probability of Successful Exit: ")
expected_retention=input("Expected Retention of Investment: ")
investment_amount=input("Amount to Invest ($mm): ")
ownership=input("% Ownership: ")
exit_value=input("Expected Exit Value ($mm): ")
exit_years=input("Years Until Exit: ")

#type conversion and data check
probability_success = float(probability_success)
if probability_success >1:
    probability_success=probability_success/100
    pass

expected_retention = float(expected_retention)
if expected_retention >1:
    expected_retention=expected_retention/100
    pass

investment_amount = float(investment_amount)

ownership = float(ownership)
if ownership >1:
    ownership=ownership/100
    pass

exit_value=int(exit_value)

exit_years=int(exit_years)

#static variables
vc_cost_of_capital=.15
fee_structure=1.25
gp_percent=.1

#calculated variables
target_multiple=(1+vc_cost_of_capital)**exit_years/probability_success
present_total_valutation=exit_value*expected_retention/target_multiple
present_partial_valuation = present_total_valutation*ownership
lp_cost=investment_amount*fee_structure
lp_valuation=present_partial_valuation*(1-gp_percent)
expected_return = lp_valuation-lp_cost


#debug
#print(f"{probability_success}, {expected_retention}, {investment_amount}, {ownership}, {exit_value} {exit_years}")
#print(f"{target_multiple}, {present_total_valutation}, {present_partial_valuation}, {lp_cost}, {lp_valuation}, {expected_return}")

#logic

expected_return = round(expected_return, 2)

if lp_valuation>=lp_cost:
    print(f"You should invest. Expected LP return is, {expected_return}$mm")
else:
    print(f"You should not invest. Expected LP return is, {expected_return}$mm")

input("")
