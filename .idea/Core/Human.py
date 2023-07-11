class Human:

    arms = 2 #class variable kinda like static for Java

    def __init__ (self, Race, Height, Weight, isRich):
        self.Race = str(Race) #instance variable
        self.Height = float(Height)
        self.Weight = float(Weight)
        self.isRich = bool(isRich)

    def Walk(self):
        print("The " + Race + " person is going to the store")

    def weighing(self):
        print("Thier weight is " + Weight + " pounds")



