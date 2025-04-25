'''9. Bank Transaction Analyzer (Representation & Clarity)
Write a Python program that allows users to input a series of transactions (credits and debits). Your
program should:
• Record each transaction clearly.
• Calculate and print the balance after each transaction.
• Provide a final summary at the end.'''

class Transaction:
    def __init__(self):
        self.trans = []
        self.balance = 0.0
    
    def add_trans(self, amt):
        # Add a transaction and update balance
        self.trans.append(amt)
        self.balance += amt
        return self.balance
    
    def count_trans(self):
        # Return number of transactions"
        return len(self.trans)
    
    def get_balance(self):
        # Return current balance
        return self.balance
    
    def trans_type(self, amt):
        #Return transaction type
        return "credit" if amt >= 0 else "debit"
    
    def check_summary(self):
        #summary
        summary = []
        summary.append("Transaction Summary")
        summary.append("Total Transactions: " + str(len(self.trans)))
        summary.append("Final Balance: ₹" + format(self.balance))
        
        if self.trans:
            summary.append("\nTransaction Details:")
            for i, amount in enumerate(self.trans,1):
                Type=self.trans_type(amount)
                summary.append(f"{i}. {Type}: ₹{abs(amount)}")
                
        return "\n".join(summary)
    
    def display(self):
        print("Bank Transaction Analyzer")
        while True:
            user_input = input("Transaction amount: ").strip()
            if user_input=='done':
                break
            try:
                amount = float(user_input)
                self.add_trans(amount)
                
                count = self.count_trans()
                trans_type = self.trans_type(amount)
                
                print(f"\nTransaction {count}: {trans_type} of ₹{abs(amount)}")
                print(f"Current Balance: ₹{self.balance}\n")
                
            except ValueError:
                print("Please enter a valid number or 'done'")
        print(self.check_summary())
        
if __name__ == "__main__":
    analyzer = Transaction()
    analyzer.display()
    analyzer.check_summary()