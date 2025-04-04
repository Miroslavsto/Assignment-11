def compute_discount(quantity, price, discount_rate):
    total_price = quantity * price  # Calculate total price before discount
    discount_amount = total_price * (discount_rate / 100)  # Calculate discount amount
    discounted_price = total_price - discount_amount  # Calculate discounted price
    return discount_amount, discounted_price


def main():
    # Get input from the user
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))
    discount_rate = float(input("Enter discount rate (in %): "))

   
    discount_amount, discounted_price = compute_discount(quantity, price, discount_rate)

   
    print("\nPurchase Summary")
    print("----------------")
    print(f"Quantity: {quantity}")
    print(f"Price per item: ${price:.2f}")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Discounted Price: ${discounted_price:.2f}")


main()
