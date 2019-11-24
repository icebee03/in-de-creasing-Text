prompt= input("Write a message: ")
output=[]
output2=[]

def add(a):
    for i in range(len(a)):
        output.append(a[i])
        output2.insert(0,a[i])
        fr= f"{''.join(output2)} | {''.join(output)}"
        hi= len(output)-len(a)
        print(" "*-hi + fr)

def remove(a):
    for i in range(len(a)):
        output.pop(-1)
        output2.pop(0)
        fr = f"{''.join(output2)} | {''.join(output)}"
        hi = len(output) - len(a)
        print(" " * -hi + fr)

add(prompt)
remove(prompt)
input("\n\n\nPress any key to close script...")