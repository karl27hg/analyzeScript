class CodelineUnit:
    def __init__(self, lineNum, code):
        self.lineNum = lineNum
        self.code = code

    def Print(self):
        print( '│{0:5d}│'.format(self.lineNum), self.code, sep='', end='')


if __name__ == "__main__":
    tmp = CodelineUnit(1, "hello")
    tmp.Print()