import random

balance = 0

def bet():
    while balance <= 0:
        print(f"You cannot bet because your balance is: ${balance}")
        deposit()

    l = input("Number of lines to bet on (1-3): ")
    # Hard coding this to a game of 3
    try:
        lines = int(l)
        while lines < 1 or lines > 3:
            print(f"Please bet on 1 to 3 lines")
            lines = int(input("Number of lines to bet on (1-3): "))

        a=input("How much are you willing to bet: $")

        try:
            amount = int(a)
            while amount < 0:
                print(f"Enter a positive number!")
                amount=int(input("How much are you willing to bet: $"))
            while amount > balance:
                print(f"You cannot bet more than your balance!")
                amount=int(input("How much are you willing to bet: $"))
        except ValueError:
            print(f"Plese type in a number")

        total = lines * amount

        print(f"You just bet ${amount} on {lines} lines. Total bet is: ${total}")
        subtractFromBalance(amount)
        slots(lines, amount)
    except ValueError:
        print(f"Plese type in a number")
        bet()

def slots(lines, amount):
    faces = ["A", "B", "C", "D"]
    wins = [0]
    for l in range(lines):
        line = [random.choice(faces), random.choice(faces), random.choice(faces)]
        print(f"{line[0]} | {line[1]} | {line[2]}")
        if line[0] == line[1] and line[1] == line[2]:
            wins.append(amount * 2)

    print(f"Congratulations? You have won: ${sum(wins)}")
    addToBalance(sum(wins))

def addToBalance(amount):
    global balance
    balance += amount
    print(f"Your current balance is: ${balance}")

def subtractFromBalance(amount):
    global balance
    balance -= amount
    if balance >= 0:
        print(f"Your current balance is: ${balance}")
    else:
        print(f"You are in debt. Your balance is ${balance}")

def deposit():
    d = input("How much would you like to deposit? $")
    try:
        deposit = int(d)
        if deposit >= 0:
            print(f"You deposited: ${deposit}")
            addToBalance(deposit)
        else:
            print(f"Nice try! You need to deposit money.")
    except:
        print(f"You must type in a number")

def gap():
    print("")

def main():
    while True:
        deposit()
        gap()
        answer = input("Press enter to play (q to quit): ")
        if answer == "q" or balance < 0:
            break
        else:
            gap()
            bet()
            gap()

    print("Thank you for playing!")

if __name__ == "__main__":
    main()
