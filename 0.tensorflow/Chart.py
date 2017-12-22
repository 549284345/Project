import matplotlib.pyplot  as plt
'''

'b' (blue)
'g' (green)
'r' (red)
'c' (cyan)
'm' (magenta)
'y' (yellow)
'k' (black)
'w' (white)
'''

class line:
    def __init__(self, name, color, linestyle, size):
        self.name = name
        self.color = color
        self.size = size
        self.linestyle = linestyle


# Chart
class chartClass:

    def __init__(self, name, xName, yName, rows = None, cols = None):
        self.__plt = plt  # private

        if rows != None and cols != None:
            self.__plt.figure(figsize=(rows, cols))
        else:
            self.__plt.xlabel(xName)
            self.__plt.ylabel(yName)

        self.__plt.title(name)

        self.title = name
        self.xName = xName
        self.yName = yName
        self.height = cols
        self.width = rows
        self.figureHandle = None
        self.Lines = []
        self.lineHandles = []
    def addDataInLine(self, xVal, yVal, name):
        if isinstance(xVal, int) != isinstance(yVal, int):
            raise "the length of xVal is not match with yVal"
        for itr in self.Lines:
            for line,value in itr.items():
                if line.name != name:
                    continue
                value[0].append(xVal)
                value[1].append(yVal)

    def addLine(self, *args, **kwargs):
        name = kwargs.get('name')
        color = kwargs.get('color')
        linestyle = kwargs.get('linestyle')
        size = kwargs.get('size')

        self.Lines.append({line(name, color, linestyle, size):[[],[]]})

    def annotate(self, line, text, pointA, pointB):
        for lineItr in self.lineHandles:
            if lineItr[0]._label == line:
                self.__plt.annotate(text, xy = pointA, xytext = pointB, arrowprops=dict(facecolor='red', shrink=0.05))


    def addLegend(self):
        for line in self.Lines:
            pass

    def update(self):
        # draw the line
        lineHandles = []
        lineName = []
        for itr in self.Lines:
            for line,value in itr.items():
                #lineName.append(line.name)  elf.lineHandles.append(
                self.__plt.plot(value[0], value[1], label = line.name, color = line.color, linestyle = line.linestyle)
                #self.annotate(line.name, 'here is max', (1,1), (2,5))
        self.__plt.legend()

    def show(self):
        self.figureHandle = self.__plt.gcf()
        self.__plt.show()

    def save(self, name):
        self.figureHandle.savefig(name)




a = chartClass('test', 'x', 'b', 8, 4)
a.addLine(name = 'testLine1', color = 'r')
a.addLine(name = 'testLine2', color = 'b')
for i in range(0, 5):
    a.addDataInLine(i, i + 1, 'testLine1')
    a.addDataInLine(i, i + 2, 'testLine2')
a.update()
a.show()
a.save('test.png')
