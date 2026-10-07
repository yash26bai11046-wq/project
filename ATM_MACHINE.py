#!/usr/bin/env python
# coding: utf-8

# ![SBI%20logo.png](attachment:SBI%20logo.png)

# In[1]:


import getpass as get  # To hide pin


class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.wrong_pin_count = 0
        self.blocked = False
        self.display()
        self.menu()

    def display(self):
        print("****************************************************************************")
        print("*                                                                          *")
        print("*                         WELCOME to SBI ATM                               *")
        print("*                                                                          *")
        print("****************************************************************************")

    def menu(self):
        if self.blocked:
            print("\nYOU HAVE ENTERED WRONG PIN 3 TIMES. THIS ATM CARD HAS BEEN BLOCKED.\nPLEASE CONTACT CUSTOMER CARE SERVICE.")
            raise SystemExit

        try:
            user_input = input("""
                HELLO, PLEASE ENTER YOUR TRANSACTION CHOICE?
                *******************************************
                    1. ENTER 1 TO CREATE PIN
                    2. ENTER 2 TO DEPOSIT
                    3. ENTER 3 TO WITHDRAW
                    4. ENTER 4 TO CHECK BALANCE
                    5. ENTER 5 to EXIT
                *******************************************\n
                          """).strip()

            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                self.exit_message()
                raise SystemExit
            else:
                raise ValueError("\n************INVALID INPUT************")
        except ValueError as e:
            print(str(e))
            self.menu()

    def exit_message(self):
        print("****************************************************************************")
        print("*                                                                          *")
        print("*                         THANKYOU FOR USING ATM                           *")
        print("*                                                                          *")
        print("****************************************************************************")

    def create_pin(self):
        if self.pin != "":
            print("\n************PIN ALREADY EXISTS************")
            self.continue_or_exit()
            return

        try:
            pin = get.getpass("CREATE YOUR PIN: ")
            if not pin.isdigit() or len(pin) != 4:
                raise ValueError("\n************PIN MUST BE 4 DIGITS AND INTEGER************")
            self.pin = pin
            print("\n************PIN SET SUCCESSFULLY************")
            self.continue_or_exit()
        except ValueError as e:
            print(str(e))
            self.create_pin()

    def verify_pin(self):
        if self.blocked:
            raise SystemExit

        pin_input = get.getpass("ENTER YOUR PIN: ")
        if pin_input.isdigit() and pin_input == self.pin:
            self.wrong_pin_count = 0
            return True

        self.wrong_pin_count += 1
        if self.wrong_pin_count >= 3:
            self.blocked = True
            print("\nYOU HAVE ENTERED WRONG PIN 3 TIMES. THIS ATM CARD HAS BEEN BLOCKED.\nPLEASE CONTACT CUSTOMER CARE SERVICE.")
            raise SystemExit

        print(f"\n************YOU HAVE {3 - self.wrong_pin_count} ATTEMPTS REMAINING************")
        return False

    def deposit(self):
        if self.pin == "":
            print("\n************YOU MUST CREATE A PIN BEFORE MAKING A DEPOSIT************")
            self.menu()
            return

        try:
            if not self.verify_pin():
                return

            amount = int(input("ENTER AMOUNT TO DEPOSIT: "))
            if amount < 100:
                raise ValueError("\n************AMOUNT SHOULD BE GREATER THAN OR EQUAL TO 100************")
            elif amount > 50000:
                raise ValueError("\n************AMOUNT SHOULD BE LESS THAN OR EQUAL TO 50000************")

            self.balance += amount
            print("\n************DEPOSIT SUCCESSFUL************")
            self.continue_or_exit()
        except ValueError as e:
            print(str(e))
            self.deposit()

    def withdraw(self):
        if self.pin == "":
            print("\n************YOU MUST CREATE A PIN BEFORE MAKING A WITHDRAWAL************ ")
            self.menu()
            return

        try:
            if not self.verify_pin():
                return

            amount = int(input("ENTER AMOUNT TO WITHDRAW: "))
            if amount < 100:
                raise ValueError("\n************AMOUNT SHOULD BE GREATER THAN OR EQUAL TO 100************")
            elif amount > 25000:
                raise ValueError("\n************AMOUNT SHOULD BE LESS THAN OR EQUAL TO 25000************")
            elif amount <= self.balance:
                self.balance -= amount
                print("\n************WITHDRAWAL SUCCESSFUL************")
                self.continue_or_exit()
            else:
                print("\n************INSUFFICIENT BALANCE AND YOUR CURRENT BALANCE IS", self.balance, "************")
                self.continue_or_exit()
        except ValueError as e:
            print(str(e))
            self.withdraw()

    def check_balance(self):
        if self.pin == "":
            print("\n************YOU MUST CREATE A PIN BEFORE CHECKING YOUR BALANCE************")
            self.menu()
            return

        try:
            if not self.verify_pin():
                return

            print(f"\n************YOUR BALANCE IS {self.balance}************")
            self.continue_or_exit()
        except ValueError as e:
            print(str(e))
            self.check_balance()

    def continue_or_exit(self):
        try:
            user_input1 = input("\nENTER 1 TO CONTINUE, or 2 TO EXIT: ").strip()
            if user_input1 == "1":
                self.menu()
            elif user_input1 == "2":
                self.exit_message()
                raise SystemExit
            else:
                raise ValueError("\n************INVALID INPUT************")
        except ValueError as e:
            print(str(e))
            self.continue_or_exit()


# In[2]:


if __name__ == "__main__":
    sbi = Atm()
