MAX_LINES = 3 #intentional constants
MAX_BET = 100
MIN_BET = 1

#Start wit collecting user input
def deposit():
    while True: #continually ask the user until they enter the amount (integer)
        amount = input('What would you like to deposit? E ')
        if amount.isdigit(): #To check if value is degit
            amount = int(amount) #convert it into int (from input is string)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0.')
        else :
            print('Please enter a number')
    return amount

#collect the bet from the user
def get_number_of_lines():
    while True:
        lines = input(f'Enter number of lines to bet on 1 - {MAX_LINES} ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES: #if lines are less than or equal to 1 and less than or equal to maxlines
                break
            else:
                print('Enter a valid number of lines')
        else:
            print('Please enter a number.')
    return lines

def get_bet():
    while True:
        amount = input('What would you like to bet on each line? E')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between {MIN_BET} - {MAX_BET}.')
        else:
            print('Please enter a number.')
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print('Insufficient funds! Please add deposit')    
        else:
            break

    print(f'Your are betting E{bet} each on {lines} lines. Total bet is {total_bet} and your balance is {balance}')

main()