class VectorClock:
    def __init__(self, n, id):
        self.clockList = [0] * n
        self.id = id

    def send(self, listOfDest):
        for dest in listOfDest:
            self.clockList[self.id] += 1
            print('Sent a message from', self.id, 'to', dest.id)
            dest.receive(self.id, self.clockList)

    def receive(self, senderId, listt):
        for i in range(len(listt)):
            self.clockList[i] = max(self.clockList[i], listt[i])
        print(self.id, "received a message from", senderId)
        self.clockList[self.id] += 1

    def displayClocks(self):
        print("Process", self.id, "  ", self.clockList)


def displayAll():
    print("")
    p1.displayClocks()
    p2.displayClocks()
    p3.displayClocks()


p1 = VectorClock(3, 0)
p2 = VectorClock(3, 1)
p3 = VectorClock(3, 2)

displayAll()
print("")
p1.send([p2])
displayAll()
print("")
p3.send([p1, p2])
displayAll()
print("")