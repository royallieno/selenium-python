from Oops import Calculator


class ChildImpl(Calculator):
    num3 = 300

    # def __init__(self):
    #     Calculator.__init__(self, 10, 20)

    def getCompleteDta(self):
        return self.num1 + self.num3 + self.Summition()


obj = ChildImpl(10, 20)
print(obj.getCompleteDta())
