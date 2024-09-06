import pandas as pd
from flask import Flask, request, jsonify, render_template

# Load the datasets
yoY_data = pd.read_csv('final_financial_data.csv')
avg_growth_data = pd.read_csv('average_growth.csv')

# Convert DataFrames to dictionaries for easier querying
yoY_data = yoY_data.set_index('Company').T.to_dict()
avg_growth_data = avg_growth_data.set_index('Company').T.to_dict()

# Initialize Flask app
app = Flask(__name__)

def simple_chatbot(company, query):
    company = company.title()

    # Total Revenue
    if "total revenue" in query.lower():
        return f"The total revenue for {company} is {yoY_data[company]['Total Revenue']}."

    # Net Income
    elif "net income" in query.lower():
        return f"The net income for {company} is {yoY_data[company]['Net Income']}."

    # Total Assets
    elif "total assets" in query.lower():
        return f"The total assets for {company} are {yoY_data[company]['Total Assets']}."

    # Total Liabilities
    elif "total liabilities" in query.lower():
        return f"The total liabilities for {company} are {yoY_data[company]['Total Liabilities']}."

    # Cash Flow from Operating Activities
    elif "cash flow from operating activities" in query.lower():
        return f"The cash flow from operating activities for {company} is {yoY_data[company]['Cash Flow from Operating Activities']}."

    # Revenue Growth (%)
    elif "revenue growth" in query.lower():
        return f"The revenue growth for {company} is {avg_growth_data[company]['Revenue Growth (%)']}%."

    # Net Income Growth (%)
    elif "net income growth" in query.lower():
        return f"The net income growth for {company} is {avg_growth_data[company]['Net Income Growth (%)']}%."

    # Assets Growth (%)
    elif "assets growth" in query.lower():
        return f"The assets growth for {company} is {avg_growth_data[company]['Assets Growth (%)']}%."

    # Liabilities Growth (%)
    elif "liabilities growth" in query.lower():
        return f"The liabilities growth for {company} is {avg_growth_data[company]['Liabilities Growth (%)']}%."

    # Cash Flow from Operations Growth (%)
    elif "cash flow from operations growth" in query.lower():
        return f"The cash flow from operations growth for {company} is {avg_growth_data[company]['Cash Flow from Operations Growth (%)']}%."

    # Year by Year Average Revenue Growth Rate (%)
    elif "year by year average revenue growth rate" in query.lower():
        return f"The year-by-year average revenue growth rate for {company} is {avg_growth_data[company]['Average Revenue Growth (%)']}%."

    # Year by Year Average Net Income Growth Rate (%)
    elif "year by year average net income growth rate" in query.lower():
        return f"The year-by-year average net income growth rate for {company} is {avg_growth_data[company]['Average Net Income Growth (%)']}%."

    # Year by Year Average Assets Growth Rate (%)
    elif "year by year average assets growth rate" in query.lower():
        return f"The year-by-year average assets growth rate for {company} is {avg_growth_data[company]['Average Assets Growth (%)']}%."

    # Year by Year Average Liabilities Growth Rate (%)
    elif "year by year average liabilities growth rate" in query.lower():
        return f"The year-by-year average liabilities growth rate for {company} is {avg_growth_data[company]['Average Liabilities Growth (%)']}%."

    # Year by Year Average Cash Flow from Operations Growth Rate (%)
    elif "year by year average cash flow from operations growth rate" in query.lower():
        return f"The year-by-year average cash flow from operations growth rate for {company} is {avg_growth_data[company]['Average Cash Flow from Operations Growth (%)']}%."

    # If query doesn't match any predefined patterns
    else:
        return "Sorry, I can only provide information on predefined queries related to total financial data and growth rates."

# Define routes for Flask app
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.form['query']
    company = request.form['company']
    response = simple_chatbot(company, user_query)
    return jsonify({'response': response})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
