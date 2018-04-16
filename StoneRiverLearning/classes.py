##Classes

class calc:

    def add(x,y):
        answer = x + y
        print(answer)
    
    def sub(x,y):
        answer = x - y
        print(answer)

    def mul(x,y):
        answer = x * y
        print(answer)

#calc.add(2,3)

import statistics

exList = [1,4,5,6,7,6,5,9,8,1]

x = statistics.median(exList)
print(x)

