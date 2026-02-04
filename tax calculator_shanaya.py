print("--- GST Calculator Tool ---")


def add_gst(amount):
    tax = amount * 0.18

    total = amount + tax
    print(f"Original: {amount} | Tax: {tax} | Final Total: {total}")

print("Calculating bill for Laptop...")
add_gst(50000)

print("\nCalculating bill for Phone...")
add_gst(15000)

