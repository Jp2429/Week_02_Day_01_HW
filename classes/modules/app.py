# import bank_account as ba #alt syntax, would have to call from 'ba' whenever functions used
from bank_account import *


sams_bank_account = BankAccount("Sam", 50, "personal") #will create an instance of a BankAccount class assigned to the variable sams_bank...
example_student_account = BankAccount("Brian", 50, "student")
example_business_account = BankAccount("Jeremy", 100, "business")

# account = {
#     "holder_name" : "John",
#     "balance": 500,
#     "type": "business"
# }

print(sams_bank_account.holder_name)
print(sams_bank_account.motto)

sams_bank_account.withdraw_money(10)
sams_bank_account.pay_monthly_fee(20)
print(f"sams account after monthly fee: {sams_bank_account.balance}")

example_student_account.withdraw_money(10)
example_student_account.pay_monthly_fee(20)
print(f"student account after paymonthly: {example_student_account.balance}")

example_business_account.withdraw_money(10)
example_business_account.pay_monthly_fee(20)
print(f"example business account after pay monthly: {example_business_account.balance}")

