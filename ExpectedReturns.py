def calc_lp_valuation (
        cost_of_capital,
        exit_years,
        probability_success,
        expected_retention,
        exit_value,
        ownership,
        gp_percent):

    #format and convert
    cost_of_capital = float(cost_of_capital)
    probability_success = float(probability_success)
    if probability_success >1:
        probability_success=probability_success/100
        pass
    exit_years=int(exit_years)
    expected_retention = float(expected_retention)
    if expected_retention >1:
        expected_retention=expected_retention/100
        pass
    ownership = float(ownership)
    if ownership >1:
        ownership=ownership/100
        pass
    exit_value = int(exit_value)
    gp_percent = float(gp_percent)

    target_multiple = calc_target_multiple(cost_of_capital, exit_years, probability_success)
    target_multiple = float(target_multiple)

    present_total_valutation = calc_present_total_valuation(exit_value, expected_retention, target_multiple)
    present_partial_valuation = present_total_valutation * ownership

    lp_valuation = present_partial_valuation * (1-gp_percent)

    return lp_valuation

def calc_target_multiple (
        cost_of_capital,
        exit_years,
        probability_success):

    target_multiple=(1 + cost_of_capital)**exit_years/probability_success
    return target_multiple

def calc_present_total_valuation(
        exit_value,
        expected_retention,
        target_multiple):

    present_total_valutation = exit_value*expected_retention/target_multiple
    return present_total_valutation
