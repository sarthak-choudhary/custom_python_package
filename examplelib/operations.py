class Expression:
    def __init__(self) -> None:
        self.exp = ""

    def __init__(self, s) -> None:
        if isinstance(s, Expression):
            self.exp = str(s.exp)
        else:
            self.exp = str(s)

    def getURL(self):
        return "http://127.0.0.1:8000/compute/" + self.exp
        
    def add(self, s) -> None:

        if (type(s) is int):
            s = str(s)
        
        if isinstance(s, Expression):
            self.exp = '(' + self.exp + '+' + s.exp + ')'
        elif (s.isnumeric()):
            self.exp = '(' + self.exp + '+' + str(s) + ')'
        else:
            if (s[0] != '('):
                s = '(' + s
                s = s + ')'
            self.exp = '(' + self.exp + '+' + s + ')'

    def subtract(self, s) -> None:

        if (type(s) is int):
            s = str(s)

        if isinstance(s, Expression):
            self.exp = '(' + self.exp + '-' + s.exp + ')'        
        elif (s.isdigit()):
            self.exp = '(' + self.exp + '-' + str(s) + ')'
        else:
            if (s[0] != '('):
                s = '(' + s
                s = s + ')'
            self.exp = '(' + self.exp + '-' + s + ')'

    def multiply(self, s) -> None:

        if (type(s) is int):
            s = str(s)

        if isinstance(s, Expression):
            self.exp = '(' + self.exp + '*' + s.exp + ')'    
        elif (s.isdigit()):
            self.exp = '(' + self.exp + '*' + str(s) + ')'
        else:
            if (s[0] != '('):
                s = '(' + s
                s = s + ')'
            self.exp = '(' + self.exp + '*' + s + ')'

    def divide(self, s) -> None:

        if (type(s) is int):
            s = str(s)

        if isinstance(s, Expression):
            self.exp = '(' + self.exp + '^' + s.exp + ')'
        elif (s.isdigit()):
            self.exp = '(' + self.exp + '^' + str(s) + ')'
        else:
            if (s[0] != '('):
                s = '(' + s
                s = s + ')'
            self.exp = '(' + self.exp + '^' + s + ')'

        
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise Exception("Divide by zero error.")
    
    return a / b

def rgbaExpansion(red, blue, green):
    if (red > 8 or red < 1) or (blue > 8 or blue < 1) or (green > 8 or green < 1):
        raise Exception("Bands out of range error.")
    return "http://127.0.0.1:8000/?" + "red="+ str(red - 1) + "&" + "blue=" + str(blue - 1) +"&" + "green=" + str(green - 1)

def convolute(band):
    if (band > 8 or band < 1):
        raise Exception("Bands out of range error.")
    return "http://127.0.0.1:8000/convolute/?" + "band=" + str(band - 1)