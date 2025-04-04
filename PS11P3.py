# Function to compute commission and next year's target
def compute_commission_and_target(sales):
    if sales > 100000:
        commission = sales * 0.10  # 10% commission for sales over $100,000
    else:
        commission = sales * 0.05  # 5% commission for sales at or under $100,000
    
    next_year_target = sales * 0.05  # 5% of sales as next year's target
    return commission, next_year_target

# Main program
def main():
    # Get input from the user
    last_name = input("Enter salesperson's last name: ")
    sales = float(input("Enter sales amount: "))

    # Compute commission and next year's target
    commission, next_year_target = compute_commission_and_target(sales)

    # Display results
    print("\nSales Report")
    print("-------------")
    print(f"Salesperson: {last_name}")
    print(f"Commission: ${commission:.2f}")
    print(f"Next Year's Target: ${next_year_target:.2f}")

# Run the main function
main()
