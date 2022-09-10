import pandas as pd
import yfinance as yf
import numpy as np

month_code_list = ["F", "G", "H", "J", "K", "M", "N", "Q", "U", "V", "X", "Z"]
test_symbol = "NG=F"
ticker = yf.Ticker("GC=F")
df = ticker.history(period="1mo")

ticker2 = yf.Ticker("CL=F")
df2 = ticker2.history(period="1mo")
if df["Volume"].mean() > df2["Volume"].mean():
    print("df has more volume")
else:
    print("df2 has more volume")


def get_max_vol_df(_input_df1, _input_df2):

    if _input_df1["Volume"].mean() > _input_df2["Volume"].mean():
        return _input_df1
    else:
        return _input_df2

