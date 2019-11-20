#Generic Inputs

risk_free_rate = input ("Risk free rate for holding period: ")
return_market_portfolio = input("Historical market yield: ")
market_beta_hat = input("Beta estimate: ")

#Conversions

risk_free_rate = float(risk_free_rate)
return_market_portfolio = float(return_market_portfolio)
market_beta_hat = float(market_beta_hat)



#Settings
factor_loading_market = return_market_portfolio - risk_free_rate
factor_loading_size = market_beta_hat_size * size_t
factor_loading_value = market_beta_hat_value * value_t
factor_loading_liquidity = market_beta_hat_liquidity * liquidity_t



#Capital Asset Pricing Model

cost_of_capital = alpha + risk_free_rate + market_beta_hat * factor_loading_market

#Fama-French Model

cost_of_capital = alpha + risk_free_rate + market_beta_hat * factor_loading_market + factor_loading_size + factor_loading_value

#Pastor-Stambaugh

cost_of_capital = alpha + risk_free_rate + market_beta_hat * factor_loading_market + factor_loading_size + factor_loading_value + factor_loading_liquidity
