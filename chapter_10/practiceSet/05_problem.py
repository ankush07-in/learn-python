from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, frm, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {frm} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running successfully..")

    def getFare(self, frm, to):
        print(f"Ticket fare in train no: {self.trainNo} from {frm} to {to} is {randint(222, 5555)}/-")

t = Train(12399)

t.book("Kolkata", "Bengaluru")
t.getStatus()
t.getFare("Kolkata", "Bengaluru")