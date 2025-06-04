from agents.data_collector import DataCollectorAgent

def main():
    print("🚀 SmartRetail.AI – Multi-Agent System Starting...")
    
    # Initialize and run the Data Collector Agent
    collector = DataCollectorAgent()
    sales_data = collector.collect_data()

    # Simple confirmation
    print(f"✅ Collected {len(sales_data)} records from source.")
    print("📊 Sample data:", sales_data[:2])  # Preview first 2 rows

if __name__ == "__main__":
    main()
