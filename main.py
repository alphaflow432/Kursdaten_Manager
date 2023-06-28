import dataStore
import pandas as pd
import os
import matplotlib

import finding_future_front_months

'''df = pd.read_csv("data/indicie_symbol_list .csv")
df2 = pd.read_csv("data/us_equity_symbol_list.csv")
df3 = pd.read_csv("data/etf_symbol_list.csv")'''


# print(dataStore.listen_herunterladen("data", df))

# Future Front Months
symbol_list = ["NG", "ZC", "ZS", "HG"]
symbol_list2 = ["SI", "LE", "LC"]
month_code_list = ["F", "G", "H", "J", "K", "M", "N", "Q", "U", "V", "X", "Z"]



# Downloading run


def run_download(input_path, type_name):
    df1 = pd.read_csv(input_path)

    wkd = "/home/artbart/PycharmProjects/pythonProject/data"
    if not os.path.exists(wkd + "/" + type_name):
        os.mkdir(wkd + "/" + type_name)

    result = dataStore.listen_herunterladen(wkd + "/" + type_name, input_symbol_df=df1, type_name=type_name)
    return result



path_etf = "/home/artbart/PycharmProjects/scientificProject1/data/etf_symbol_list.csv"
path_us_stocks = "/home/artbart/PycharmProjects/scientificProject1/data/us_equity_symbol_list.csv"

#run_download(path_etf, type_name="etfs")
#run_download(path_us_stocks, type_name="us_stocks")


# corr test v0

data = dataStore.ordner_buendeln("/home/artbart/PycharmProjects/scientificProject1/data/indicie", "dl_log.csv")
#data.plot()
#data.to_csv("bundled_data.csv")
data
