print("--- GST Calculator Tool ---")


def add_gst(amount):
    tax = amount * 0.18

    total = amount + tax
    print(f"Original: {amount} | Tax: {tax} | Final Total: {total}")

bill=int(input("please enter your bill amount:"))
print("your bill with GST is as follows")
add_gst(bill)

