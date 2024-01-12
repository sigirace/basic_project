import pandas as pd
import os
import pickle

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
    
class DT():
    def __init__(self):
        pass
