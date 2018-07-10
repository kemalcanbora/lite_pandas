from sklearn.model_selection import train_test_split
import operator

class MinimalistDataframe:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def get_spesific_rows(self, column_name, value, logic="eq"):
        '''
          lt "Same as a < b."
          le "Same as a <= b."
          eq "Same as a == b."
          ne "Same as a != b."
          ge "Same as a >= b."
          gt "Same as a > b."
          You can change this part for your data problem
        '''

        if logic == "lt":
            logic = operator.lt
        elif logic == "le":
            logic = operator.le
        elif logic == "eq":
            logic = operator.eq
        elif logic == "ne":
            logic = operator.ne
        elif logic == "ge":
            logic = operator.ge
        elif logic == "gt":
            logic = operator.gt

        operation = logic(self.dataframe[column_name], value)
        return self.dataframe.loc[operation]

    def get_column_values(self, column_name):
        return self.dataframe[column_name]

    def dropna(self, column_name):
        return self.dataframe.dropna(subset=[column_name], how='all')

    def split_dataframe(self, test_size):
        ''' Train_test_split make a shuffle don't worry '''

        train_set, test_set = train_test_split(df, test_size=test_size)
        return train_set, test_set

    def dataframe_shuffle(self):
        ''' Shuffle '''

        dataframe = self.dataframe.sample(frac=1).reset_index(drop=True)
        return dataframe

    def select_some_row(self, select_index_column, selected_column_sought):
        '''Select_index_column is necessary for can be designated '''
        '''selected_column_sought should be list type.The values in the selected column sought'''

        df = self.dataframe.set_index(select_index_column)
        return df.loc[selected_column_sought, :]
