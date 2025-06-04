                              ┌──────────────────────────────┐
                              │     User / Retail Manager    │
                              └─────────────┬────────────────┘
                                            │
                           ┌────────────────▼────────────────┐
                           │        Frontend Interface        │
                           │ (optional: Streamlit / React)    │
                           └────────────────┬────────────────┘
                                            │
                                            ▼
              ┌─────────────────────────────────────────────────────┐
              │                  Backend (main.py)                  │
              │   Orchestrates agent execution using ADK (Python)  │
              └────────────────┬────────────────┬──────────────────┘
                               │                │
           ┌───────────────────▼───┐      ┌─────▼────────────────────┐
           │ DataCollectorAgent   │      │ TrendAnalyzerAgent        │
           │ - Fetch CSV / Sheet  │      │ - Query BigQuery          │
           │ - Local or GCS       │      │ - Analyze sales trends    │
           └──────────┬───────────┘      └──────────────┬────────────┘
                      │                                 │
         ┌────────────▼───────────┐        ┌────────────▼─────────────┐
         │ Google Cloud Storage   │        │     Google BigQuery      │
         └────────────────────────┘        └──────────────────────────┘

           ┌─────────────────────────────────────────────────────────┐
           │ RestockAdvisorAgent                                     │
           │ - Uses data from TrendAnalyzer                          │
           │ - Suggests what to restock, when, and how much          │
           └─────────────────────────────────────────────────────────┘

           ┌─────────────────────────────────────────────────────────┐
           │ ReportWriterAgent                                       │
           │ - Generates daily summary reports                       │
           │ - Uses Jinja2 + Plotly/Matplotlib                       │
           │ - Output: HTML or PDF                                   │
           └─────────────────────────────────────────────────────────┘

           ┌─────────────────────────────────────────────────────────┐
           │ CustomerSupportAgent                                    │
           │ - Handles FAQs using Dialogflow or Twilio               │
           │ - Could be integrated into WhatsApp or web widget       │
           └─────────────────────────────────────────────────────────┘
