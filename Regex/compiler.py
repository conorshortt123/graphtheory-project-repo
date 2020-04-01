from shunting import shunt
from classes import Fragment, State

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
			frag.accept.edges = (frag.start, accept)
		elif c == '?':
			# Pop a single fragment off the stack
			frag = nfa_stack.pop()
			# Create new start and accept states
			accept = State()
			start = State(edges=[frag.start, accept])
			# Point the old accept states at the new one
			frag.accept.edges.append(accept)
		elif c == '+':
			# Pop a single fragment off the stack
			frag = nfa_stack.pop()
			# Create new start and accept states
			accept = State()
			start = State(edges=[frag.start])
			# Point the old accept states at the new one
			frag.accept.edges = (frag.start, accept)
		else:
			accept = State()
			start = State(label=c, edges=[accept])

		# Create new instance of Fragment to represent the new NFA
		newfrag = Fragment(start, accept)
		# Push new NFA to stack.
		nfa_stack.append(newfrag)

	return nfa_stack.pop()
