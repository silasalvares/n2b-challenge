import pandas as pd
from decimal import Decimal

class DatasetHandler():
    
    def __init__(self, dataset=''):
        self.df = self._preprocessing(pd.read_csv(dataset))
        self.df_size = self.df.shape[0]

    def _preprocessing(self, df):
        for col in df:
            dt = df[col].dtype
            if dt == int or dt == float:
                df[col] = df[col].fillna(0)
            else:
                df[col] = df[col].fillna("")

        return df

    def filter(self, filter_info):
        filters = self._get_filters(filter_info.get('filter_data', {}), self.df)
        page_size = filter_info.get('page_size', 10)
        page = filter_info.get('page', 1) * page_size
        
        if len(filters) > 0:
            reviews = self.df[ eval(' & '.join(filters))]
            reviews_page = reviews.head(page).tail(page_size).to_dict(orient='records')
            return {'page': page, 'total_records': len(reviews), 'reviews': reviews_page }
        else:
            reviews = self.df.head(page).tail(page_size).to_dict(orient='records')
            return {'page': page, 'total_records': self.df_size, 'reviews': reviews }
    
    def _get_filters(self, filter_data, df):
        filters = []

        if filter_data.get('country', False):
            filters.append("(self.df['country'].str.lower() == '%s')" % filter_data.get('country').lower())
        if filter_data.get('description', False):
            filters.append("(self.df['description'].str.lower().str.contains('%s'))" % filter_data.get('description').lower())
        if filter_data.get('points', False):
            filters.append("(self.df['points'] == int('%s'))" % str(filter_data.get('points')))
        if filter_data.get('price', False):
            filters.append("(self.df['price'] == Decimal('%s'))" % str(filter_data.get('price')))
        if filter_data.get('variety', False):
            filters.append("(self.df['variety'].str.lower() == '%s')" % filter_data.get('variety').lower())

        return filters


    
