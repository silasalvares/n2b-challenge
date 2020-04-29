import pandas as pd
from decimal import Decimal

class DatasetHandler():
    
    def __init__(self, dataset='', page_size=10):
        self.df = self._preprocessing(pd.read_csv(dataset))
        self.df_size = self.df.shape[0]
        self.page_size = page_size

    def _preprocessing(self, df):
        for col in df:
            dt = df[col].dtype
            if dt == int or dt == float:
                df[col] = df[col].fillna(0)
            else:
                df[col] = df[col].fillna("")

        return df

    def filter(self, filter_info):
        filters = self._get_filters(filter_info.get('filter_data', []), self.df)
        page = filter_info.get('page', 1) * self.page_size
        
        if len(filters) > 0:
            return (self.df[ eval(' & '.join(filters))].head(page)
                    .tail(self.page_size).to_dict(orient='records'))
        else:
            return self.df.head(page).tail(self.page_size).to_dict(orient='records')
    
    def _get_filters(self, filter_data, df):
        filters = []

        if filter_data.get('country', False):
            filters.append("(self.df['country'] == '%s')" % filter_data.get('country'))
        if filter_data.get('description', False):
            filters.append("(self.df['description'].str.contains('%s'))" % filter_data.get('description'))
        if filter_data.get('points', False):
            filters.append("(self.df['points'] == int('%s'))" % str(filter_data.get('points')))
        if filter_data.get('price', False):
            filters.append("(self.df['price'] == Decimal('%s'))" % str(filter_data.get('price')))
        if filter_data.get('variety', False):
            filters.append("(self.df['variety'] == '%s')" % filter_data.get('variety'))

        return filters


    
