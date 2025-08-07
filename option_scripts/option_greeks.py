try:
    import QuantLib as ql
except ImportError:
    print('QuantLib is required for this script. Please install it with `pip install QuantLib-Python`.')
    exit(1)


# User-editable parameters
option_type = 'CALL'  # 'CALL' or 'PUT'
underlying = 150.0
strike = 150.0
risk_free_rate = 0.01
dividend_rate = 0.0
volatility = 0.2
settlement = '2025-07-11'
expiration = '2025-07-18'
european = True

settlement_date = ql.DateParser.parseFormatted(settlement, '%Y-%m-%d')
expiration_date = ql.DateParser.parseFormatted(expiration, '%Y-%m-%d')
ql.Settings.instance().evaluationDate = settlement_date

if option_type.upper() in ('C', 'CALL'):
    ql_option_type = ql.Option.Call
elif option_type.upper() in ('P', 'PUT'):
    ql_option_type = ql.Option.Put
else:
    raise ValueError('Wrong option type')

if european:
    exercise = ql.EuropeanExercise(expiration_date)
else:
    exercise = ql.AmericanExercise(settlement_date, expiration_date)

payoff = ql.PlainVanillaPayoff(ql_option_type, strike)
option = ql.VanillaOption(payoff, exercise)

spot_handle = ql.QuoteHandle(ql.SimpleQuote(underlying))
risk_free_rate_handle = ql.YieldTermStructureHandle(ql.FlatForward(settlement_date, risk_free_rate, ql.Actual365Fixed()))
dividend_handle = ql.YieldTermStructureHandle(ql.FlatForward(settlement_date, dividend_rate, ql.Actual365Fixed()))
vol_handle = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(settlement_date, ql.NullCalendar(), volatility, ql.Actual365Fixed()))

bsm_process = ql.BlackScholesMertonProcess(spot_handle, dividend_handle, risk_free_rate_handle, vol_handle)
engine = ql.AnalyticEuropeanEngine(bsm_process) if european else ql.BaroneAdesiWhaleyEngine(bsm_process)
option.setPricingEngine(engine)

print(f'NPV: {option.NPV()}')
print(f'Delta: {option.delta()}')
print(f'Gamma: {option.gamma()}')
print(f'Theta: {option.theta()}')
print(f'Vega: {option.vega()}')
print(f'Rho: {option.rho()}') 