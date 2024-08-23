from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def bookTrain(slf, frm, to):
        print(f"The ticket is booked in train no: {slf.trainNo} from {frm} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(slf, frm, to):
        print(f"The ticket fare is {randint(799, 1299)}/- for {slf.trainNo} no. train which is going from {frm} to {to}")

newTrain = Train(13478)

newTrain.bookTrain("Ranchi", "Kerala")
newTrain.getStatus()
newTrain.getFare("Mumbai", "Kerala")