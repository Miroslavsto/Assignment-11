# Global variables for total and tax
total = 0
tax = 0

# Function to compute total and tax
def compute_total_and_tax(quantity, unit_price):
    global total, tax  # Declare total and tax as global variables
    total = quantity * unit_price  # Calculate total cost
    tax = total * 0.07  # Calculate tax (7% of total)

# Main program
def main():
    # Get input from the user
    quantity = int(input("Enter quantity of the item: "))
    unit_price = float(input("Enter unit price: "))

    # Compute total and tax
    compute_total_and_tax(quantity, unit_price)

    # Display results
    print("\nPurchase Summary")
    print("----------------")
    print(f"Total Cost: ${total:.2f}")
    print(f"Tax (7%): ${tax:.2f}")

# Run the main function
main()
