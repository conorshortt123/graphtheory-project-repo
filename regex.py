# Conor Shortt
# Classes used in Thompson's Construction.

class State:
    """A state with one or two edges, all edges labelled by label."""
    # Constructor for the class.
    def __init__(self, label=None, edges=[]):
        # Every state has 0, 1, or 2 edges(arrows) from it
        self.edges = edges
        # Label for the arrows. None means epsilon(e)
        self.label = label

class Fragment:
    """An NFA fragment with a start state and an accept state."""
    # Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

def shunt(infix):
    """Return the infix regular expression in postfix."""
    infix = list(infix)[::-1]

    # Operator stack.
    opers, postfix = [], []

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

def compile(infix):
    """Return an NFA fragment representing the infix regular expression"""
    # Convert infix to postfix.
    postfix = shunt(infix)
    # Make postfix a stack of characters.
    postfix = list(postfix)[::-1]
    
    # A stack of NFA fragments.
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

            start = frag2.start
            accept = frag1.accept
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
        elif c == '*':
            # Pop a single fragment off the stack
            frag = nfa_stack.pop()
            # Create new start and accept states
            accept = State()
            start = State(edges=[frag.start, accept])
            # Point the arrows.
            frag.accept.edges = ([frag.start, accept])
        else:
            accept = State()
            start = State(label=c, edges=[accept])
         
        # Create new instance of Fragment to represent the new NFA
        newfrag = Fragment(start, accept)  
        # Push new NFA to stack.
        nfa_stack.append(newfrag) 

    return nfa_stack.pop()

# Add a state to a set and follow all of the e arrows.
def followes(state, current):
    """Function that follows all epsilon arrows recursively."""
    # Only do something when we haven't already seen the state.
    if state not in current:
        # Put the state into current
        current.add(state)
        if state.label is None:
            # Loop through the states pointed to by this one.
            for x in state.edges:
                # Follow all of their e(psilon)s too.
                followes(x, current)

def match(regex, s):
    """Returns true if the regular expression matches the input string."""
    # Returns true if regex (fully) matches the string s. It returns false otherwise.

    # Compile the regular expression into an NFA.
    nfa = compile(regex)

    # Try to match the regular expression to the string s

    # Current set of states
    current = set()
    # Add the first state, and follow all e arrows.
    followes(nfa.start, current)
    # Current set of states
    previous = set()

    # Loop through characters in s.
    for c in s:
        # Keep track of where we were.
        previous = current
        # Create a new empty set for states we're about to be in.
        current = set()
        # Loop through the previous state
        for state in previous:
            # Only follow arrows not labelled by e(psilon).
            if state.label is not None:
                # If the label of the state is equal to the character we've read.
                if state.label == c:
                    # Add the state at the end of the arrow to current.
                    followes(state.edges[0], current)


    # Ask the NFA if it matches the string s.
    return nfa.accept in current

if __name__ == "__main__":

    tests = [
        ["a.b|b*", "bbbbb", True],
        ["a.b|b*", "bbx", False],
        ["a.b", "ab", True],
        ["b**", "b", True],
        ["b*", "", True]
    ]

    for test in tests:
        assert match(test[0], test[1]) == test[2], test[0] + \
        (" should match " if test[2] else " should not match") + test[1]
