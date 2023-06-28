import pandas as pd
import yfinance
# Standardatentyp !



def listen_einlesen_zusammenfuehren(dateipfade_listen):
    return


# Standardatentyp für symbol list !
# dataFrame mit "symbol"  als Spaltename


def update_results_to_csv(file_name, new_data_frame):
    # Check if file exists
    if os.path_etf.exists(file_name):
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
        temptransdf = pd.DataFrame(data=new_data_frame)
        temptransdf.to_csv(file_name)

    return "seems to worked"


def listen_herunterladen(operating_dir,
                         input_symbol_df,
                         type_name,
                         _period = "max",
                         _interval = "1d",
                         _logfile_name = "dl_log",
                         _download_delay = 2.0):

    """
    usage of yfinance
    checking if symbol history data misses
    then downloading symbol max 1y history in to the operating_dir

    logs the successful downloads in dl_log.csv
    :param type_name: name of equity type, usally sub-directiory name
    :param _period:
    :param _interval:
    :param _logfile_name:
    :param _download_delay:
    :param operating_dir: working directory
    :param input_symbol_df: pd.DataFrame containing symbols , column name must be "symbol"

    :return: requests + failed downloads
    """



    import yfinance
    import os
    import time

    status_str: str = ""

    if not os.path.exists(operating_dir):
        status_str = "Path of the file is Invalid"
        return status_str

    requests = 0
    success_dl_log = []

    for symbol in input_symbol_df["symbol"]:
        # Checking if file already exits
        if not os.path.exists(str(operating_dir + "/" + symbol + ".csv")):
            temp_df = pd.DataFrame()
            try:
                temp_ticker = yfinance.Ticker(symbol)
                temp_df = temp_ticker.history(interval=_interval, period=_period)

                # Check if DF is empty
                # and only then save downloaded table
                if not temp_df.empty:
                    success_dl_log.append(symbol)
                    temp_df.to_csv(str(operating_dir + "/" + symbol + ".csv"))
                    print(f" {symbol} download complete " + "/n" + f"requests   :  {requests}")

                    # log successful download


            except:
                status_str += (symbol + "download failed" + "/n")
                pass
            finally:
                # count request
                requests += 1
                time.sleep(_download_delay)

    temp_dict = {"symbol": success_dl_log}
    temp_df2 = pd.DataFrame(temp_dict)
    _logfile_name = str(type_name + _logfile_name)
    if temp_df2.empty:
        pass
    else:
        if os.path.exists(str(operating_dir + "/" + _logfile_name + ".csv")):
            existing_dl = pd.read_csv(str(operating_dir+"/"+_logfile_name+".csv"))
            existing_dl = existing_dl["symbol"]
            temp_df2.append(existing_dl["symbol"])
            temp_df2.drop_duplicates(inplace=True)
            temp_df2.reindex(inplace=True)
            temp_df2.to_csv(str(operating_dir + "/" + _logfile_name + ".csv"))
        else:
            temp_df2.to_csv(str(operating_dir + "/" + _logfile_name + ".csv"))

    status_str = "used requests : " + str(requests) + "/n" + status_str
    return status_str




def ordner_buendeln(wk_directory, log_file_name):
    import os
    """

    :param wk_directory:   collecting dir, here should be the csv files
    :param log_file_name: logfile_name to skip this one in reading process
    :return: dataFrame with only Close price and the symbol name in timeseries
    """
    sammel_df = pd.DataFrame(columns=['Date'])
    sammel_df.set_index('Date')
    dirlist = os.listdir(wk_directory)
    for item in dirlist:
        if not (item == log_file_name):
            print(item)
            temp = pd.read_csv(str(wk_directory + "/" + item), index_col="Date")
            temp[item] = temp["Close"]
            sammel_df = sammel_df.append(temp[item])
            sammel_df.reset_index()
            sammel_df.reindex(['date'])

    return sammel_df



def bestehende_symbole_updaten(operating_dir, log_txt, status_txt):
    # Nach Upadate letztes Datum in status_txt schreiben
    return


# Keymap erzeugen um Laufzeiten bei Verarbeitung zu reduzieren
# @param : euqity history files (usually csv)
# @return
def keymap_erzeugen():
    return



# Hashmap erzeugen um Laufzeiten bei Verarbeitung zu reduzieren
# @param : euqity history files (usually csv)
def hashmap_erzeugen():
    return


dct = {'symbol': ["^JKSE", "^VIX", "^RUT" ]}
df = pd.DataFrame(dct)



