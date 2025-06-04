import pandas as pd

class DataCollectorAgent:
    def __init__(self):
        self.data_source = "data/sales_data.csv"  # Local CSV or can be from GCS bucket

    def collect_data(self):
        try:
            df = pd.read_csv(self.data_source)
            print("📥 Data successfully read from CSV.")
            return df.to_dict(orient="records")  # Convert to list of dicts
        except Exception as e:
            print("❌ Error reading data:", e)
            return []
