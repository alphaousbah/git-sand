class Boat(*args):

    """ defines the class Boat """
    
    # constructor of Boat
    def __init__(self, model):
        self.model = model
    
    # methods of Boat
    
    # display feature
    def display(self):
        print("model:", self.model)