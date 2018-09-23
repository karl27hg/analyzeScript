import CodelineUnit as CU
import RawSourceCode as RSC


class MetaSourceCode:
    def __init__(self, rsc):
        self.SetSrcCode(rsc)

    def SetSrcCode(self, rsc):
        self.mainSrcCode = []
        if RSC.RawSourceCode == type(rsc):
            for it in rsc.codelines:
                if it.code == '\n':
                    continue
                self.mainSrcCode.append(CU.CodelineUnit(it.lineNum, it.code))
    
    def Print(self):
        for it in self.mainSrcCode:
            it.Print()
        print('\nLine Count :', len(self.mainSrcCode))
    
if '__main__' == __name__:
    rsc = RSC.RawSourceCode('./sample01.c')
    rsc.Print()
    msc = MetaSourceCode(rsc)
    msc.Print()