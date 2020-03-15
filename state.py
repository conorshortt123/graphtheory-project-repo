# Conor Shortt
# Classes used in Thompson's Construction.

class State:
    # Every state has 0, 1, or 2 edges(arrows) from it
    edges = []

    # Label for the arrows. None means epsilon(e)
    label = None
   
    # Constructor for the class.
    def __init__(self, edges=[], label=None):
        self.edges = edges
        self.label = label

class Frag:
    # Start state of NFA fragment.
    start = None
    # Accept state of NFA fragment.
    accept = None

    # Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept

edge1 = State(label='a')
edge2 = State(label='b')
myState = State(edges =[edge1, edge2])
myFrag = Frag(edge1, myState)
print(edge1.label)
print(edge2.label)
print(myState.edges)
print(myFrag)
