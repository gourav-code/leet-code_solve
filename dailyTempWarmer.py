
def dailyTemperatures(temperatures):
    stack=[]
    output=[0]*len(temperatures)
    for i,temp in enumerate(temperatures):
        while(stack and stack[-1][0]<temp):
            tmp=stack.pop()
            output[tmp[1]]=i-tmp[1]
        stack.append((temp,i))

    return output

print(dailyTemperatures([73,74,75,71,69,72,76,73]))

# monotonic decreasing stack