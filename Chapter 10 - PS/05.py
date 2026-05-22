from random import randint
class train:
    def __init__ (self, trainno):
        self.trainno = trainno
    
    def book(self, fro, to):
        print(f"ticket is booked in train no. {self.trainno} moving from {fro} to {to}")

    def getstatus(self):
        print (f"train no : {self.trainno} is running on time")

    def fare(self, fro, to):
        print (f"ticket fare in train no. : {self.trainno} moving from {fro} to {to} is {randint((200), (800))}")

t = train(234565)
t.book ("vskp", "ndls")
t.getstatus()
t.fare ("vskp", "ndls")