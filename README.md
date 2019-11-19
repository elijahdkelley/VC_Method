# VC_Method
 
Takes six inputs and returns an investment recommendation. 

Inputs:
1. Investment amount.
     How much is being invested today? In millions, e.g. 15.5
2. Ownership percentage.
     What percentage of the firm's equity is being purchased with the investment amount?
3. Exit value.
     On exit of the investment, what is the expected value of the investment? In millions, e.g. 100
4. Years until exit.
     How many years until the expected exit?
5. Probability of success.
     What is the estimated probability that the exit value will be achieved?
6. Expected retention.
     Of the ownership percentage, what is the expected dilution on exit? e.g. if 20% dilution is expected then the expected retention is 1-.2=.8
     

Output:

The program uses industry standard fee structure (2/20/10 year life) and historical cost of capital to calculate portfolio multiples and risk adjusted valuation of equity. Next, it modifies the valuation according to the carry hurdles for the portfolio to set a valuation by which a general partner meets limited partner expected returns and begins to generate carry. The output is a recommendation of whether an investment meets this hurdle and provides an expected return for LPs.
