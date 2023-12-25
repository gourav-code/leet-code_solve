
def carFleet(target: int, position: [int], speed: [int]) -> int:
    carsList=[[p,s] for p,s in zip(position, speed)]

    stack=[]
    for p,s in sorted(carsList)[::-1]: #sorted in reverse order
        stack.append((target-p)/s)
        if len(stack)>=2 and stack[-1]<=stack[-2]:
            stack.pop()
        
    return len(stack)


target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

print(carFleet(target, position, speed))