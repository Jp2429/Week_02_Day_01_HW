class BankAccount: 
    def __init__(self, input_holder_name, input_balance, input_account_type):
        #self allows for a specific instance data. Defining a property without 'self.' syntax will declare a universal proprty
        self.holder_name = input_holder_name
        self.balance = input_balance
        self.account_type = input_account_type
        self.motto = "Trust the process"
        self._rates = {
            "personal" : 10,
            "business" : 50,
            "student" : 5
        }
    
    #methods:
    def withdraw_money(self, amount_to_withdraw):
        self.balance -= amount_to_withdraw

    def pay_monthly_fee(self, fee):
        fee_after_discount = self._rates[self.account_type]
        self.withdraw_money(fee_after_discount)

