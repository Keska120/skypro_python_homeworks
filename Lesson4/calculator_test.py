from calculator import Calculator

calculator = Calculator()

res=calculator.sum(4,5)

assert res==9

res=calculator.sum(-1,-1)
assert res==-2
print("finish")