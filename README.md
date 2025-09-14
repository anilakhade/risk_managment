# Risk Management System  
A PySide6 + pandas + Broker APIs tool to view, filter, and analyze trading positions in real-time.  

This project is part of my journey to build financial tools and systems.  
It helps traders analyze and track positions in Indian markets without relying on manual Excel workflows.  

## Why I need to build this  

**Current situation in our organisation**  
- We are 30+ traders, across different broker IDs (Zerodha, IIFL, etc.).  
- After market close, we compile all positions from all brokers into Excel.  
- Managers and owners then use these sheets for risk management and hedging decisions.  
- This requires 20+ back-office staff, often working until **10 PM or even midnight**.  
- Mistakes are frequent because of **manual data entry**.  

 **In short: we are stuck in Excel, and we need automation.**  

**In short: we are stuck in Excel, and we need automation.**  

## What I am doing to solve this problem  
- **Step 1:** Collect all positions from all traders (downloaded directly from broker as Excel files).  
- **Step 2:** Separate them into intraday squared-off positions and carry-forward positions to merge with previous day’s net.  
- **Step 3:** Split squared-off and outstanding positions; generate new net positions for the next day.  
- **Step 4:** Create payoffs for all FUTURE and OPTION strategies, and calculate margins for each (via API).  
- **Step 5:** Fetch real-time rates for all positions through a single WebSocket connection.  

**This software automates all tasks — reducing the time from ~6 hours to just 5–10 minutes.**  
**It also cuts costs drastically, as the organization no longer needs a 20-person back-office team.**  





Licensed under the [Apache License 2.0](./LICENSE)
