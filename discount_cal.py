total_amount = float(input("Enter the total amount: "))
discount_percentage = float(input("Enter the discount percentage: "))

discount_amount = (discount_percentage / 100) * total_amount
final_amount = total_amount - discount_amount

print("=-="*20)
print("subtotal: $", total_amount)
print(discount_percentage,"percent discount: $", discount_amount)
print("total amount after discount: $", final_amount)
print("=-="*20)