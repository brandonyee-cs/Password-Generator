import string
import random

class passgen():
    def __init__(self, passreq):
        #Determines Flags for Password Requirements Set By User
        self.includeUpper = passreq[0]
        self.includeLower = passreq[1]
        self.includeNums = passreq[2]
        self.includeSymbol = passreq[3]
        self.numberofChar = passreq[4]
    
    def generate_password(self):
        choiceArray = [1,2,3,4]
        symbolchoice = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "{", "}", "[", "]", ",", ".", "?"]
        password = ""
        randomLetter = random.choice(string.ascii_letters)
        while len(password) < self.numberofChar:
            if random.choice(choiceArray) == 1 and self.includeUpper == True:
                password = password + (random.choice(string.ascii_letters)).upper()
            elif random.choice(choiceArray) == 2 and self.includeLower == True:
                password = password + random.choice(string.ascii_letters)
            elif random.choice(choiceArray) == 3 and self.includeNums == True:
                password = password + str(random.randint(1,10))
            elif random.choice(choiceArray) == 4 and self.includeSymbol == True:
                password = password + random.choice(symbolchoice)
        self.password = password
    
    def get_password(self):
        return self.password

    def test_pass():
        test = passgen([True,True,True,False, 10])
        passgen.generate_password(test)
        print(passgen.get_password(test))