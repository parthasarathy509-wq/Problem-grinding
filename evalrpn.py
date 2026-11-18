def evalRPN(tokens):
    s = []
    op = ["+", "-", "*", "/"]
    for i in tokens:
        if i in op:
            top = s.pop()
            top1 = s.pop()
            if i == "+":
                top += top1
                s.append(top)
            elif i == "-":
                top1 -= top
                s.append(top1)
            elif i == "*":
                top = top * top1
                s.append(top)
            elif i == "/":
                top1 /= top
                s.append(int(top1))
        else:
            s.append(int(i))
    return s[-1]


print(evalRPN(["1", "2", "+", "3", "*", "4", "-"]))  # Expected: 5
print(evalRPN(["-42"]))  # Expected: -42
print(evalRPN(["6", "-132", "/"]))  # Expected: 0
print(evalRPN(["-7", "3", "/"]))  # Expected: -2
print(evalRPN(["3", "10", "-"]))  # Expected: -7
print(evalRPN(["5", "-5", "+"]))  # Expected: 0
print(evalRPN(["1", "2", "3", "4", "5", "+", "+", "+", "+"]))  # Expected: 15
print(
    evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
)  # Expected: 22
