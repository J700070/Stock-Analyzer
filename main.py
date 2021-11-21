import streamlit as st
import pandas as pd
import numpy as np
from style import *
import json
import datetime
import matplotlib.pyplot as plt
import yfinance as yf


# Streamlit config
st.set_page_config(
    layout="wide",
    initial_sidebar_state="auto",
    page_title="Portfolio Tracker",
    page_icon=None,
)
# Pandas config
pd.options.display.float_format = "{:,.2f}".format

# Import Data
with open("config.json") as json_data_file:
    data = json.load(json_data_file)


# ==========================================================================

st.title('Stock Analyzer')
cols = st.columns(4)
ticker = cols[0].text_input('Stock Ticker', 'AAPL')
stock = yf.Ticker(ticker)

# Process Data
# ==========================================================================
# Col 0
info = stock.info
long_name = info["longName"]
asset_type = info["quoteType"]
sector = info["sector"]
industry = info["industry"]
summary = info["longBusinessSummary"]
currency = info["currency"]
shares = info["sharesOutstanding"]
country = info["country"]
employees = info["fullTimeEmployees"]
enterprise_value = info["enterpriseValue"]

last_price = float(info["regularMarketPrice"])
open_price = float(info["open"])
daily_price_change = round(last_price - open_price, 2)
daily_price_change_percentage = daily_price_change / last_price * 100

market_cap = last_price * shares

# Col 1

# Margins
gross_margin = info["grossMargins"]
operating_margin = info["operatingMargins"]
ebitda_margin = info["ebitdaMargins"]
net_margin = info["profitMargins"]


# Earnings
revenue = info["totalRevenue"]
gross_profit = info["grossProfits"]
operating_profit = revenue * operating_margin
ebitda = info["ebitda"]
net_income = revenue * net_margin
operating_cashflow = info["operatingCashflow"]
free_cash_flow = info["freeCashflow"]


# RETURN
return_on_assets = info["returnOnAssets"]
return_on_equity = info["returnOnEquity"]

# Col 2
# GROWTH
revenue_growth = info["revenueGrowth"]
earnings_growth = info["earningsGrowth"]
revenue_qq_growth = info["revenueQuarterlyGrowth"]
earnings_qq_growth = info["earningsQuarterlyGrowth"]

# HEALTH
current_ratio = info["currentRatio"]
debt_to_equity = info["debtToEquity"]
total_cash = info["totalCash"]
total_debt = info["totalDebt"]
quick_ratio = info["quickRatio"]
total_assets = info["totalAssets"]
book_value = info["bookValue"]

# PER SHARE
cash_per_share = info["totalCashPerShare"]
revenue_per_share = info["revenuePerShare"]
earnings_per_share = info["trailingEps"]
forward_earnings_per_share = info["forwardEps"]


# Col 3

# OWNER
held_percent_institutions = info["heldPercentInstitutions"]
held_percent_insiders = info["heldPercentInsiders"]

# VALUATION
price_to_sales = info["priceToSalesTrailing12Months"]
peg = info["pegRatio"]
per = info["trailingPE"]
forward_per = info["forwardPE"]

# OTHER
number_of_analyst = info["numberOfAnalystOpinions"]

# Draw Charts
# ==========================================================================

# Show Data
# ==========================================================================

# Col 0
cols[0].metric(ticker, long_name, currency + " " +
               str(daily_price_change) + " (" + str(round(daily_price_change_percentage, 2)) + "%)")
cols[0].markdown("<p style='font-size: 18px'>Price: " + str(round(last_price, 2)) +
                 "<br> Asset Type: " + asset_type +
                 "<br> Sector: " + sector +
                 "<br> Industry: " + industry +
                 "<br> Country: " + country +
                 "<br> Employees: " + str(employees) +
                 "<br> Shares: " + number_format(int(shares/1000000)) + " million" +
                 "<br> Market Cap: " +
                 number_format(int(market_cap/1000000000)) + " billion" +
                 "<br> Enterprise Value: " +
                 number_format(int(enterprise_value/1000000000)) + " billion </p>", unsafe_allow_html=True)


cols[0].markdown("<hr> <b>Summary:</b> <br>" +
                 summary, unsafe_allow_html=True)


# Col 1
cols[1].markdown("<p style='font-size: 18px; margin-left:50px'>" +
                 "<span style='font-size: 22px;'> <b>Margins </b></span>" +
                 "<br> Gross Margin: " + str(gross_margin) +
                 "<br> Operating Margin: " + str(operating_margin) +
                 "<br> EBITDA Margin: " + str(ebitda_margin) +
                 "<br> Net Margin: " + str(net_margin) +
                 "<br></p>", unsafe_allow_html=True)


cols[1].markdown("<p style='font-size: 18px; margin-left:50px'>" +
                 "<span style='font-size: 22px;'> <b>Earnings </b></span>" +
                 "<br> Revenue: " + str(revenue) +
                 "<br> Gross Profit: " + str(gross_profit) +
                 "<br> EBITDA: " + str(ebitda) +
                 "<br> Net Income: " + str(net_income) +
                 "<br></p>", unsafe_allow_html=True)

cols[1].markdown("<p style='font-size: 18px; margin-left:50px'>" +
                 "<span style='font-size: 22px;'> <b>Cash Flow </b></span>" +
                 "<br> Operating Cash Flow: " + str(operating_cashflow) +
                 "<br> Free Cash Flow: " + str(free_cash_flow) +
                 "<br></p>", unsafe_allow_html=True)

cols[1].markdown("<p style='font-size: 18px; margin-left:50px'>" +
                 "<span style='font-size: 22px;'> <b>Ratios </b></span>" +
                 "<br> Return on Assets: " + str(return_on_assets) +
                 "<br> Return on Equity: " + str(return_on_equity) +
                 "<br></p>", unsafe_allow_html=True)


# Col 2
cols[2].markdown("<p style='font-size: 18px'>" +
                 "<span style='font-size: 22px;'> <b>Growth </b></span>" +
                 "<br> Revenue Growth: " + str(revenue_growth) +
                 "<br> Revenue Quarterly Growth: " + str(revenue_qq_growth) +
                 "<br> Earnings Growth: " + str(earnings_growth) +
                 "<br> Earnings Quarterly Growth: " + str(earnings_qq_growth) +
                 "<br></p>", unsafe_allow_html=True)


cols[2].markdown("<p style='font-size: 18px'>" +
                 "<span style='font-size: 22px;'> <b>Health </b></span>" +
                 "<br> Current Ratio: " + str(current_ratio) +
                 "<br> Quick Ratio: " + str(quick_ratio) +
                 "<br> Debt to Equity: " + str(debt_to_equity) +
                 "<br> Book Value: " + str(book_value) +
                 "<br> Total Assets: " + str(total_assets) +
                 "<br> Total Cash: " + str(total_cash) +
                 "<br> Total Debt: " + str(total_debt) +
                 "<br></p>", unsafe_allow_html=True)

cols[2].markdown("<p style='font-size: 18px'>" +
                 "<span style='font-size: 22px;'> <b>Per Share </b></span>" +
                 "<br> Revenue per Share: " + str(revenue_per_share) +
                 "<br> Earnings per Share: " + str(earnings_per_share) +
                 "<br> Forward Earnings per Share: " + str(forward_earnings_per_share) +
                 "<br> Cash per Share: " + str(cash_per_share) +
                 "<br></p>", unsafe_allow_html=True)


# Col 3

cols[3].markdown("<p style='font-size: 18px'>" +
                 "<span style='font-size: 22px;'> <b>Ownership </b></span>" +
                 "<br> Held % by institutions: " + str(held_percent_institutions) +
                 "<br> Held % by insiders: " + str(held_percent_insiders) +
                 "<br></p>", unsafe_allow_html=True)

cols[3].markdown("<p style='font-size: 18px'>" +
                 "<span style='font-size: 22px;'> <b>Valuation </b></span>" +
                 "<br> Price to Sales: " + str(price_to_sales) +
                 "<br> Forward PER: " + str(forward_per) +
                 "<br> PER: " + str(per) +
                 "<br> PEG Ratio: " + str(peg) +
                 "<br></p>", unsafe_allow_html=True)

cols[3].markdown("<p style='font-size: 18px'>" +
                 "<span style='font-size: 22px;'> <b>Other </b></span>" +
                 "<br> Number of Analyst: " + str(number_of_analyst) +
                 "<br></p>", unsafe_allow_html=True)

# Styling


# Aux functions
# ==========================================================================
