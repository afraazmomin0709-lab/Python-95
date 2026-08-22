base_price = float(input("Enter the original price of the product: ")) 
total_GST_rate = float(input("Enter the total GST rate (e.g., 5, 12, 18, 28): "))

cgst_rate = total_GST_rate / 2 
sgst_rate = total_GST_rate / 2 

cgst_amount = (base_price * cgst_rate) / 100
sgst_amount = (base_price * sgst_rate) / 100 

total_tax = cgst_amount + sgst_amount 
total_price = base_price + total_tax 

print("\nGST Invoice Details") 
print(f"Original Price: Rs. {base_price:.2f}") 
print(f"Total GST Rate: {total_GST_rate}% ({cgst_rate}% CGST + {sgst_rate}% SGST)") 
print(f"CGST Amount: Rs. {cgst_amount:.2f}") 
print(f"SGST Amount: Rs. {sgst_amount:.2f}") 
print(f"Total Tax: Rs. {total_tax:.2f}") 
print(f"Final Bill: Rs. {total_price:.2f}")