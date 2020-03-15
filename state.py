# Conor Shortt
# Classes used in Thompson's Construction.

class State:
    # Every state has 0, 1, or 2 edges(arrows) from it
    edges = []

    # Label for the arrows. None means epsilon(e)
    label = None
   
    # Constructor for the class.
    def __init__(self, label=None, edges=[]):
        self.edges = edges
        self.label = label

class Fragment:
    # Start state of NFA fragment.
    start = None
    # Accept state of NFA fragment.
    accept = None

    # Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

def shunt(infix):
    infix = list(infix)[::-1]

    # Operator stack.
    opers = []

    # Output list.
    postfix = []

    # Operator precedence.
    prec = {'*': 100, '.': 80, '|': 60, ')': 40, '(': 20}

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
            while opers[-1] != '(':
                postfix.append(opers.pop())
            # Get rid of the '('.
            opers.pop()
        elif c in prec:
            # Push any operators on the opers stack with higher prec to the output.
            while opers and prec[c] < prec[opers[-1]]:
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

def regex_compile(infix):
    postfix = shunt(infix)
    postfix = list(postfix)[::-1]

    nfa_stack = []

    while postfix:
        # Pop a character from postfix
        c = postfix.pop()
        if c == '.':
            # Pop two fragments(NFA'S) off the stack.
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            # Point frag 2's accept state at frag 1's start state.
            frag2.accept.edges.append(frag1.start)
            # Create new instance of Fragment to represent the new NFA
            newfrag = Fragment(frag2.start, frag1.accept)
        elif c == '|':
            # Pop two frags off stack
            frag1 = nfa_stack.pop()
            frag2 = nfa_stack.pop()
            # Create new start and accept states
            accept = State()
            start = State(edges=[frag2.start, frag1.start])
            # Point the old accept states at the new one
            frag2.accept.edges.append(accept)
            frag1.accept.edges.append(accept)
            # Create new instance of Fragment to represent the new NFA
            newfrag = Fragment(start, accept)
        elif c == '*':
            # Pop a single fragment off the stack
            frag = nfa_stack.pop()
            # Create new start and accept states
            accept = State()
            start = State(edges=[frag.start, accept])
            # Point the arrows.
            frag.accept.edges = ([frag.start, accept])
            # Create new instance of Fragment to represent the new NFA
            newfrag = Fragment(start, accept)
        else:
            accept = State()
            start = State(label=c, edges=[accept])
            # Create new instance of Fragment to represent the new NFA
            newfrag = Fragment(start, accept)
           
        # Push new NFA to stack.
        nfa_stack.append(newfrag) 

    return nfa_stack.pop()

def match(regex, s):
    # This function will return true if and only if the regular expression regular expression.
    # Regex (fully) matches the string s. It returns false otherwise.

    # Compile the regular expression into an NFA.
    nfa = regex_compile(regex)
    # Ask the NFA if it matches the string s.
    return nfa

print(match("a.b|b*", "bbbbbbbbb"))
