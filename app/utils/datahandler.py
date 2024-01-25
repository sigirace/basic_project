import pandas as pd
import os
import pickle
import json

PATH_DATA_STORAGE = ""

class DF():
    def __init__(self, path=PATH_DATA_STORAGE):
        self.path = path

    def df_to_pickle(self, df, filename):
        '''
            PARAMETER
            df      : dataframe for saving in pickle format
            filename: filename
        '''
        df.to_pickle("{}.pkl".format(os.path.join(self.storage, filename)))
        print("file saved at {}".format(os.path.join(self.storage, filename)))


    def pickle_to_df(self, filename):
        '''
            PARAMETER
            filename: filename
            RETURN
            df      : dataframe from pickle
        '''
        df = pd.read_pickle("{}.pkl".format(os.path.join(self.storage, filename)))
        return df

class DataTool():

    def __init__(self):
        pass

    def list_to_jsonline(self, DATA_PATH, data):
        # JSON Lines 형식의 파일로 저장
        with open(DATA_PATH, "w") as jsonl_file:
            for item in data:
                json.dump(item, jsonl_file)
                jsonl_file.write("\n")