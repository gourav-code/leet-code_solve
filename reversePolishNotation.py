
def evalRPN(tokens):
    stack=[]
    sign=["+","-","/","*"]
    a=b=0
    for tmp in tokens:
        if tmp in sign:
            a=stack.pop()
            print(f"here a: {int(a)}")
            b=stack.pop()
            print(f"here b: {int(b)}")
            if(tmp=="+"):
                a+=b
            elif(tmp=="-"):
                a-=b
            elif(tmp=="/"):
                a=b/a
            else:
                a*=b
            print(f"a: {int(a)}")
            stack.append(int(a))
        else:
            stack.append(int(tmp))

    print(stack.pop())

tokens=["4","13","5","/","+"]
evalRPN(tokens)