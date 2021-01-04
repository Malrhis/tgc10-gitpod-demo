amount_loan = float(input("How much did you borrow?"))
interest_rate = float(input("Monthly interest rate?"))
repayment_per_month = float(input("Monthly repayment?"))

months_needed_to_repay = 0
while amount_loan > 0:
    interest_for_this_month = interest_rate/100 * amount_loan
    amount_loan += interest_for_this_month
    print("Amount left to pay = ", amount_loan)
    amount_loan -= repayment_per_month
    months_needed_to_repay += 1

print("months_needed_to_repay", months_needed_to_repay)
