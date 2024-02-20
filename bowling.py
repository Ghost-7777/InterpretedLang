import sys

fileName = "reversestring.txt"
lines = []

try:
    file = open(fileName)
    lines = file.read().split("\n")
    file.close()
except Exception as e:
    print(f"Error while opening file:\n{e}")
    sys.exit(0)

stack = []
pc = 0

def err(message):
    print("\n" + message + f" at line {pc}")
    sys.exit(0)

def pop(index=-1):
    if len(stack) < 1:
        err("Error: Stack underflow")
    return stack.pop(index)

while pc >= 0 and pc < len(lines):
    parts = lines[pc].split(" ")
    instr = parts[0].lower()
    if instr == "pull":
        try:
            stack.append(ord(input("")[0]))
        except IndexError:
            stack.append(0)
    elif instr == "tournament":
        a = pop()
        stack.append(a)
        stack.append(a)
    elif instr == "check":
        a = pop()
        if len(parts) < 3 or parts[1].lower() != "feet":
            err("Error: Expected instruction argument for checking feet")
        try:
            line = int(parts[2]) - 1
            if a == 0:
                pc = line - 1
        except:
            err("Error")
    elif instr == "bowl":
        stack.append(0)
    elif instr == "pin":
        a = pop()
        stack.append(a + 1)
    elif instr == "spare":
        print(chr(pop()), end="", flush=True)
    elif instr == "strike":
        print(int(pop()), end="", flush=True)
    elif instr == "foul":
        a = pop()
        b = pop()
        stack.append(b - a)
    elif instr == "points":
        if len(parts) < 2:
            err("Error: Expected to specify the points")
        if parts[1].lower() == 'travel':
            a = pop(0)
            stack.append(a)
        elif parts[1].lower() == 'home':
            a = pop()
            stack.insert(0, a)
    elif instr == 'fry':
        break
    pc += 1

print('')
