import pandas as pd
import yfinance as yf
import time
import os




def get_max_vol_df(_input_df1, _input_df2):
    if _input_df1["Volume"].mean() > _input_df2["Volume"].mean():
        return _input_df1
    else:
        return _input_df2


def find_fmonth(raw_future_symbol_list, future_months, sleeper, start_reqsts = 0):
    """

    :param raw_future_symbol_list: "symbol only, list of strings"
    :param future_months: "month code only , list of strings"
    :param sleeper: "sleeptimer in s"
    :return: "used requests(2 ticker + download) in index0 + list of strings with working fmonths"

    """

    result_file = "possible_future_month_ combinations.csv"
    path = "/home/artbart/PycharmProjects/scientificProject1/data/"
    working_symbol_strings = ["0"]
    working_symbol_strings[0] = str(int(working_symbol_strings[0]) + int(start_reqsts))

    # Max Reqeusts die Stunde
    max_req_per_h = 1800
    # Sleeptimer berechnen
    sleeper_time_calculated = 3600/max_req_per_h
    request_counter = 0 + start_reqsts
    # Sleeper setzen
    time.sleep(start_reqsts*sleeper_time_calculated)


    for future_symbol in raw_future_symbol_list:

        for item in future_months:
            symbol_str = str(future_symbol + "=" + str(item))

            tmp2_ticker = yf.Ticker(symbol_str)

            try:
                data = tmp2_ticker.history(period="1d", auto_adjust=True, interval="5d")
                request_counter += 1
                # Checking if data is inside
                if not data.empty:
                    # Log possible fmonth
                    working_symbol_strings.append(symbol_str)


            finally:

                symbol_str = ""
                time.sleep(sleeper_time_calculated)
        tempdict = {"symbol": working_symbol_strings[1:]}
        tempdf = pd.DataFrame(tempdict)
        #update_results_to_csv(result_file, tempdf)
        update_results_to_csv(path + result_file, tempdf)


    working_symbol_strings[0] = request_counter
    return working_symbol_strings


def update_results_to_csv(file_name, new_data_frame):
    # Check if file exists
    if os.path.exists(file_name):
        try:
            data = pd.read_csv(file_name)
            data = pd.DataFrame(data["symbol"])

            data = data.append(new_data_frame)
            data.drop_duplicates(inplace=True)
            data.reindex()
            data.to_csv(file_name)
            return "worked"
        except:
            print("something went wrong , updating the results")
            return "something went wrong , updating the results"
    else:
        temptransdf = pd.DataFrame(data=new_data_frame, )
        temptransdf.to_csv(file_name)

    return "seems to worked"

