#تمرین بلندترین ساختمان تهران

def skyline(*args):
    highest=0
    for element in args:
        if element>highest:
            highest=element
    return highest


my_inputs=[]
while True:
    temp=input()
    if not temp.isdigit():
        break
    my_inputs.append(int(temp))

print(skyline(*my_inputs))
