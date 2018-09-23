class CodeCmtUnit:
    def __init__(self, firstLineNum, comment):
        self.SetComment(firstLineNum, comment)

    def SetComment(self, firstLineNum, comment):
        if int == type(firstLineNum) and str == type(comment):
            self.firstLineNum = firstLineNum
            self.comment = comment
    
    def Print(self):
        tmpComment = self.comment.replace('\n', '\n│     │')
        print("│%5d│" % self.firstLineNum, tmpComment, sep='', end='')


if "__main__" == __name__:
    tmpCCU = CodeCmtUnit(3, 'Hello\nMan~!\nOk?')
    tmpCCU.Print()