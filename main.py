import random #Slot machine

MAX_LINES=3 #Global variable defined in capital
MAX_BET=1000
MIN_BET=1

#rows and columns of the slot machine
ROWS=3
COLS=3

#Symbols in the slot machine
symbol_count={
    'A':4,
    'B':5,
    'C':4,
    'D':5
}

def get_slot_machine_spin(rows,cols,symbols):
    #adding all symbols in a list for random choosing
    all_symbols=[]
    for symbols,su





"""
Function to record player deposit
"""
def deposit():
    while True: #running while till valid input received
        amount=input('What would you like to deposit? ')
        if amount.isdigit(): #checking if the input is a number
            amount=int(amount) #converting str to int
            if amount>0:
                break
            else:
                print("Amount should be greater than 0")
        else: #if input isn't number
            print('Enter a valid number')
    return amount 

def get_number_lines():
    """getting number of lines to bet on from the player"""
    while True: #running while till valid input received
        #str(MAX_LINES) concatinating int and str isn't possible
        lines=input('Enter number of lines to bet on (1 -' + str(MAX_LINES)+')? ')
        if lines.isdigit(): #checking if the input is a number
            lines=int(lines) #converting str to int
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Lines should be greater than 0")
        else: #if input isn't number
            print('Enter a valid number')
    return lines 

def get_bet():
    """getting bets from the player"""
    while True: #running while till valid input received
        bet=input('What would you like to bet on each line ? $')
        if bet.isdigit(): #checking if the input is a number
            bet=int(bet) #converting str to int
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet should be between {MIN_BET} - {MAX_BET}")
        else: #if input isn't number
            print('Enter a valid number')
    return bet

def main():
    balance = deposit()
    lines=get_number_lines()
    
    """ Checking if bet amount is within their deposit"""
    while True:

        bet=get_bet()
        total_bet=lines*bet

        if total_bet>balance:
            print(f"You do not have enough amount to bet. Your current balance {balance}")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to {total_bet}")

main()