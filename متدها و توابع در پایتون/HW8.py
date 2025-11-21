#تمرین زوج هارا بردار

def pick_evens(*args):
    my_evens=[]
    for i in args:
        if i%2==0:
            my_evens.append(i)
    return my_evens


my_inputs=[]

while True:
    temp=input()
    if not temp.lstrip("-").isdigit():
        break
    my_inputs.append(int(temp))


print(pick_evens(*my_inputs))