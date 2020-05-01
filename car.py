class Car(*args):

    """ defines the class Car """
    
    # constructor of Car
    def __init__(self, model):
        self.model = model
    
    # methods of Car
    
    # display feature
    def display(self):
        print("model:", self.model)