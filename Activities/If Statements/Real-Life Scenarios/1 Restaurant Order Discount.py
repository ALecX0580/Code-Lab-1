total_bill = float(input("Put your bill: "))
discount10 = 0.10 # 10%

if total_bill > 50:
    discount10_result = (50 * discount10)
    print("Discount applied, your final bill is £", total_bill - discount10_result)
else:
    print("No discount applied, youe final bill is £", total_bill)
    