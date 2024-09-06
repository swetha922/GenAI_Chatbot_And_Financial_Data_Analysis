# Financial Data Analysis & AI-Powered Financial Chatbot 💬📊
This repository contains two key projects: financial data analysis from 10-K filings and the development of an AI-powered chatbot built using Python and Flask. The chatbot allows users to interact with financial data dynamically and retrieve meaningful insights.
# Project Overview
# 1. Task 1: Financial Data Extraction & Analysis
In this project, I manually extracted and analyzed financial data from the 10-K filings of Microsoft, Tesla, and Apple for the last three fiscal years. The extracted data includes:

Total Revenue
Net Income
Total Assets
Total Liabilities
Cash Flow from Operating Activities
# Key Steps:
Extracted financial data from the SEC EDGAR database.
Cleaned and structured the data using pandas for further analysis.
Performed year-over-year growth calculations and trend analysis.
Visualized the financial data using matplotlib for clear insights.

# 2. Task 2: AI-Powered Financial Chatbot
This task involves building a financial chatbot using Flask to provide users with financial insights based on the analysis from Task 1. The chatbot can answer predefined queries such as:

"What is the total revenue?"
"What is the revenue growth (%)?"
"What is the net income growth (%)?"
# Key Features:
Flask-based Web Interface: Users can interact with the chatbot through a simple web UI.
Predefined Queries: The chatbot responds to predefined queries by fetching financial data from Task 1.
Dynamic Response Generation: The chatbot uses logic to compute and present year-over-year growth rates and other financial metrics.

# Tech Stack
Python 
Pandas
Flask
Jupyter Notebook
HTML/CSS (for Flask-based UI)
matplotlib (for data visualization)

# Future Improvements
Incorporating machine learning models to allow more flexible, conversational user queries.
Enhancing the chatbot’s ability to handle more complex financial queries beyond predefined ones.
Adding more dynamic data visualizations based on user queries.
