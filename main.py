import random #Slot machine

MAX_LINES=3 #Global variable defined in capital
MAX_BET=1000
MIN_BET=1

#rows and columns of the slot machine
ROWS=3
COLS=3

#Symbols in the slot machine
symbols={
    'A':4,
    'B':5,
    'C':4,
    'D':5
}

symbols_values={
    'A':4,
    'B':5,
    'C':4,
    'D':5
}

def check_winnings(columns,lines,bet,symbol_values):
    winnings=0
    winnings_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol != symbol_to_check:
                break
        else: #for-else..runs when break doesn't come into play
            winnings+= symbol_values[symbol]*bet
            winnings_lines.append(line+1)
    return winnings,winnings_lines


def get_slot_machine_spin(rows,cols,symbols):
    #adding all symbols in a list for random choosing
    all_symbols=[]
    for symbols,symbols_count in symbols.items(): #in dict .items gets keys & values
        for _ in range(symbols_count):
            """
            The loop will run based on symbols counts and 
            Append the symbol as many times the loop runs in the list 
            """
            all_symbols.append(symbols)
    columns=[] #Slot machine output 
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:] #[:] way to copy a list ,changes to either of the list doesn't affect the other
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns #format [['B', 'C', 'D'], ['B', 'B', 'A'], ['D', 'B', 'C']]

def print_slot_machine(columns): #transpose the columns
    for row in range(len(columns[0])): #if there are no columns then this code breaks
        for i,column in enumerate(columns): #enumerate gets the index of the list
            if i != len(column) - 1: #to not print | at the end
                print(column[row],end=" | ")
            else:
                print(column[row],end="\n")
        #print() #fter every loop,print occurs in the next line
 
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

def spin(balance):
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

    slots=get_slot_machine_spin(ROWS,COLS,symbols)
    print_slot_machine(slots)
    winnings,winnings_lines=check_winnings(slots,lines,bet,symbols_values)
    print(f"You won ${winnings}")
    print(f'You won on the lines',*winnings_lines) #*slack operator
    return winnings-total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is {balance}")
        if balance==0:
            print(f'You cant play anymore.See you next time')
            break
        else:
            answer=input('Press enter to continue( q to quit)')
            if answer=='q':
                break
            balance+=spin(balance)
    print(f"You have {balance}")
    
main()
