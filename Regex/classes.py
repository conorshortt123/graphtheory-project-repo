class State:
    """A state with one or two edges, all edges labelled by label."""
    # Constructor for the class.
    def __init__(self, label=None, edges=None):
        # Every state has 0, 1, or 2 edges(arrows) from it
        self.edges = edges if edges else []
        # Label for the arrows. None means epsilon(e)
        self.label = label

class Fragment:
    """An NFA fragment with a start state and an accept state."""
    # Constructor
    def __init__(self, start, accept):
        self.start = start
        self.accept = accept
