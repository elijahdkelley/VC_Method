def calc_cost_of_capital(
        factor_type="",
        alpha=0,
        risk_free_rate=0,
        return_market_portfolio=0,
        market_beta_hat=0,
        market_beta_hat_size=0,
        market_beta_hat_value=0,
        market_beta_hat_liquidity=0,
        size_t=0,
        value_t=0,
        liquidity_t=0):

        #Conversions
    alpha = float(alpha)
    risk_free_rate = float(risk_free_rate)
    return_market_portfolio = float(return_market_portfolio)
    market_beta_hat = float(market_beta_hat)
    market_beta_hat_size = float(market_beta_hat_size)
    market_beta_hat_value = float(market_beta_hat_value)
    market_beta_hat_liquidity = float(market_beta_hat_liquidity)
    size_t = float(size_t)
    value_t = float(value_t)
    liquidity_t =float(liquidity_t)

    factor_loading_market, factor_loading_other = calc_factor_loading(risk_free_rate, return_market_portfolio, market_beta_hat_size,
            market_beta_hat_value, market_beta_hat_liquidity, size_t, value_t, liquidity_t)

    factor_loading_market = float(factor_loading_market)
    factor_loading_other = float(factor_loading_other)

    cost_of_capital = calc_cost_of_capital_type(factor_type, alpha, risk_free_rate, market_beta_hat, factor_loading_market,
            factor_loading_other)

    return cost_of_capital

def calc_factor_loading(
        risk_free_rate,
        return_market_portfolio,
        market_beta_hat_size,
        market_beta_hat_value,
        market_beta_hat_liquidity,
        size_t,
        value_t,
        liquidity_t):

    factor_loading_market = return_market_portfolio - risk_free_rate
    factor_loading_other = market_beta_hat_size * size_t + market_beta_hat_value * value_t + market_beta_hat_liquidity * liquidity_t

    return factor_loading_market, factor_loading_other

def calc_cost_of_capital_type(
        factor_type,
        alpha,
        risk_free_rate,
        market_beta_hat,
        factor_loading_market,
        factor_loading_other):

    factor_type_list = ["CAPM", "FFM", "PSM"]

    if factor_type in factor_type_list:
        cost_of_capital = alpha + risk_free_rate + market_beta_hat * factor_loading_market + factor_loading_other
    else:
        cost_of_capital = .15

    return cost_of_capital
