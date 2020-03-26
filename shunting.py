# Conor Shortt
# The Shunting Yard algorithm for regular expressions.

def shunt(infix):
    """Return the infix regular expression in postfix."""
    print("Infix = " + infix)
    infix = list(infix)[::-1]
    print(infix)
    # Operator stack.
    opers, postfix = [], []

    # Operator precedence.
    prec = {'*': 100, '?': 95, '+':90, '.': 80, '|': 60, ')': 40, '(': 20}

    # Loop through the input one character at a time.
    while infix:
        # Pop a character from the input.
        c = infix.pop()

        # Decide what to do based on the character.
        if c == '(':
            # Push an open bracket to the opers stack.
            opers.append(c)
        elif c == ')':
            # Pop the operators stack until you find an (.
            if(opers):
                while opers[-1] != '(':
                    postfix.append(opers.pop())
	        # Get rid of the '('.
                opers.pop()
                print("Brackets popped off postfix:")
                print(postfix)
        elif c in prec:
            print("Found character in precedence: " + c)
            # Push any operators on the opers stack with higher prec to the output.
            print(opers)
            print(prec[c])
            print(prec[opers[-1]])
            while opers and prec[c] > prec[opers[-1]]:
                print("In opers while")
                postfix.append(opers.pop())
                # Push c to the operator stack.
                opers.append(c)
        else:
            # Typically, we just push the character to the output.
            postfix.append(c)

    # Pop all the operators to the output.
    while opers:
        postfix.append(opers.pop())

    # Convert output list to string.
    return ''.join(postfix)
