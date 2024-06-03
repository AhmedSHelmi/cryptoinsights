class DataProcessor:
    def calculate_moving_average(self, df, window):
        df[f'ma_{window}'] = df['close'].rolling(window=window).mean()
        return df

    def filter_by_date(self, df, start_date, end_date):
        return df[(df['open_time'] >= start_date) & (df['open_time'] <= end_date)]
