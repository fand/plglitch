import random

CODE_FRAME = "00dc"


class Frame:

    def __init__(self, binary, _type):
        self.binary = binary
        self.type = self.frameType(_type)

    def frameType(self, s):
        if s == "\x01\xB0":
            return "I"
        if s == "\x01\xB6":
            return "P"
        else:
            return "O"

        
class AVI:
    
    def __init__(self, path):
        with open(path, 'rb') as f:
            self.binary = f.read()
        self._initFrame()


    def _initFrame(self):
        last = self.binary.find(CODE_FRAME)
        self.header = self.binary[:last]
        self.frames = []
        while True:
            i = self.binary[(last + 1):].find(CODE_FRAME)
            if i == -1:
                break
            f = Frame(self.binary[last : (last + 1) + i], self.binary[last + 10 : last + 12])
            self.frames.append(f)
            last = (last + 1) + i 

        self.footer = self.binary[last:]

        
    def mosh(self):
        first = True
        for i in range(len(self.frames)):
            if self.frames[i].type == "I":
                if first:
                    first = False
                    continue
                self.frames[i].binary = ""

                
    def slide(self, duration):
        slides = filter(lambda f: f.type == "P", self.frames)
        sliding = False
        i = 0
        while i < len(self.frames):
            if sliding:
#            if sliding and f_slide != None:                
                print ",",
                sliding = False
                
                f_slide = slides[random.randint(0, len(slides))]
                for j in range(duration):

                    self.frames.insert(i, f_slide)
                i += duration
                
            else:
                if self.frames[i].type == "I":
                    sliding = True
                    self.frames[i].binary = ""
                i += 1
                    
                
    def write(self, path):
        s = "".join([f.binary for f in self.frames])
        self.binary = self.header + s + self.footer
        with open(path, 'wb') as f:
            f.write(self.binary)
        



if __name__=='__main__':
    import sys

    if len(sys.argv) != 3:
        print "args error"
        exit()
    
    avi = AVI(sys.argv[1])
    avi.mosh()
    avi.slide(70)
    # for f in filter(lambda f:f.type == "I", avi.frames)[1:]:
    #     if f.type == "I":
    #         s = chr(random.randint(10, 230)) * len(f.binary)
    #         f.binary = s
    
    avi.write(sys.argv[2])
