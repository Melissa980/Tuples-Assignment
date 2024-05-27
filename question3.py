# Question 3 Task 1 

def average_closing_price(stock_data, stock_symbol):
    total_price = 0
    count = 0
    
    for data in stock_data:
        symbol, date, closing_price = data
        if symbol == stock_symbol:
            total_price += closing_price
            count += 1
    
    if count == 0:
        return f"No data available for stock symbol: {stock_symbol}"
    
    average_price = total_price / count
    return f"Average closing price for {stock_symbol}: {average_price:.2f}"

# Sample Data
stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    ("AAPL", "2021-01-03", 135.0),
    ("MSFT", "2021-01-02", 225.0),
    ("AAPL", "2021-01-04", 133.0)
]

# Example usage
average_aapl = average_closing_price(stock_data, "AAPL")
average_msft = average_closing_price(stock_data, "MSFT")
average_goog = average_closing_price(stock_data, "GOOG")

print(average_aapl)
print(average_msft)
print(average_goog)
