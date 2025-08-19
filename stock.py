# Hardcoded stock prices dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 135,
    "MSFT": 300
}

# Portfolio dictionary to store user stocks
portfolio = {}

# Taking input from user
while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").strip().upper()
    if stock == "DONE":
        break
    
    # If stock not in dictionary, ask user to add it
    if stock not in stock_prices:
        try:
            price = float(input(f"Stock {stock} not found. Enter current price for {stock}: "))
            stock_prices[stock] = price
            print(f"✅ Added {stock} with price ${price}")
        except ValueError:
            print("⚠ Invalid price. Try again.")
            continue
    
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("⚠ Please enter a valid number.")

# Calculate total investment value
total_value = 0
print("\n📊 Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\n💰 Total Investment Value = ${total_value}")
  
  # LETS RUN OUR CODE