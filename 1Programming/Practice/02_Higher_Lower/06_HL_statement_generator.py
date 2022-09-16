# HL Component 6 - Statement Generator

def hl_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print() 

# Main routine

too_low = hl_statement("^^ Too low, try a higher number.  |  Guesses Left: 3 ^^", "^")
print()
too_high = hl_statement("vv Too high, try a lower number.  |  Guesses Left: 2 vv", "v")
print()
duplicate = hl_statement("!! You already guessed that number. Please try again.  |  Guesses Left: 2 !!", "!")
print()
start_round = hl_statement("### Round 1 of 3 ###", "#") 