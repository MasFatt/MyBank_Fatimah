import random
class newAccount:
    def __init__(self, name, initialDeposit, accountNumber):
        self.name = name
        self.initialDeposit = initialDeposit
        self.accountNumber = accountNumber

    def DisplayAccountDetails(self):
        print("Account Name:", self.name)
        print("Account Number:", self.accountNumber)
        print("Your current balance is £", self.initialDeposit)

class existingAccount:
    def __init__(self):
        self.name = 'Fatimah'
        self.accountNumber = 12345
        self.balance = 1000

    def makeWithdrawal(self, amount):
        if self.balance - amount < 0:
            print("Saldo Anda tidak cukup")
        else:
             self.balance = self.balance - amount

    def makeDeposit(self, amount):
        self.balance = self.balance + amount

    def DisplayAccountDetails(self):
        print("Account Name:", self.name)
        print("Account Number:", self.accountNumber)
        print("Your current balance is £", self.balance)

while True:
    print("Selamat datang di BANK .... - ada yang bisa saya bantu?")
    print("Tekan 1 untuk membuat akun")
    print("Tekan 2 untuk melihat akun")
    print("Tekan 3 untuk keluar")

    userChoice = int(input())
    if userChoice == 1:
        print("Masukkan nama anda: ")
        name = input()
        print("Masukkan deposit anda: ")
        initialDeposit = input()
        accountNumber = ''.join(random.sample('0123456789', 5))
        account = newAccount(name, initialDeposit, accountNumber)
        print("Terimakasih telah membuat akun, berikut adalah data anda")
        account.DisplayAccountDetails()
    elif userChoice == 2:
        print("Silakan konfirmasi nama anda: ")
        name = input()
        print("Silakan konfirmasi nomor id anda: ")
        accountNumber = input()
        account = existingAccount()
        while True:
            print("Terimakasih, ada yang bisa dibantu?")
            print("Tekan a melihat saldo")
            print("Tekan b menambah deposit")
            print("Tekan c penarikan saldo")
            print("Tekan d keluar")
            secondChoice = input()
            if secondChoice == "a":
                account.DisplayAccountDetails()
            elif secondChoice == "b":
                print("Anda ingin deposit berapa?")
                deposit = int(input())
                account.makeDeposit(deposit)
            elif secondChoice == "c":
                print("Anda ingin menarik saldo berapa?")
                withdrawal = int(input())
                account.makeWithdrawal(withdrawal)
            elif secondChoice == "d":
                break
    elif userChoice == 3:
        quit();
