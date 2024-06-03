class Application:
    def __init__(self, api_client, data_processor, gpt_service):
        self.api_client = api_client
        self.data_processor = data_processor
        self.gpt_service = gpt_service

    def run(self, symbol, interval, start_str, end_str, ma_window, gpt_prompt):
        df = self.api_client.get_klines(symbol, interval, start_str, end_str)
        df = self.data_processor.calculate_moving_average(df, ma_window)
        filtered_df = self.data_processor.filter_by_date(df, start_str, end_str)
        
        # Prepare the data summary for GPT
        summary = filtered_df[['open_time', 'open', 'high', 'low', 'close', f'ma_{ma_window}']].tail(10).to_string()
        prompt = f"{gpt_prompt}\n\n{summary}"
        
        recommendation = self.gpt_service.get_recommendations(prompt)
        return recommendation
