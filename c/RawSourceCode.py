import CodelineUnit as CU

class RawSourceCode:
    def __init__(self, pathFile):
        self.sourcePathFile = pathFile
        self.ReadSource()

    def ReadSource(self):
        self.lastLineNum = 0
        self.codelines = []
        f = open(self.sourcePathFile)
        while True:
            line = f.readline()
            if not line:
                break
            self.lastLineNum += 1
            self.codelines.append(CU.CodelineUnit(self.lastLineNum, line))
        f.close()

    def Print(self):
        for it in self.codelines:
            it.Print()
        print("\n* Last Line Number : %d\n" % self.lastLineNum)
        

if __name__ == "__main__":
    src = RawSourceCode("./sample01.c")
    src.Print()
