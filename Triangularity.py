stack = []
stack2 = []

def run(code):
    global stack
    global stack2
    lines = code.split('\n')
    length = len(code.split('\n'))
    if not all(len(elem) == length * 2 - 1 for elem in lines):
        print("I smell no triangularity. YOU SHALL NOT PASS!")
        return
    for i in range(length - 1):
        if lines[i][:length - i - 1] == lines[i][- (length - i - 1):] == (length - i - 1) * ".":
            continue
        else:
            print("I smell no triangularity. YOU SHALL NOT PASS!")
            break
            return
    for index, command in enumerate(code):
        if code[:index].count('"') % 2 == 0:
            if command == "@":
                stack.append(stack.pop() + 1)
            elif command == "!":
                stack.append(0 if stack.pop() else 1)
            elif command == ")":
                stack.append(0)
            elif command == "E":
                stack.append(eval(stack.pop()))
            elif command == "I":
                stack.append(__import__('sys').stdin.read().split("\n")[stack.pop()])
            elif command == "S":
                stack, stack2 = stack2, stack
            elif command == "=":
                a = stack[-1]
                b = stack[-2]
                stack = stack[:-2]
                stack.append(1 if a == b else 0)
            elif command == ">":
                a = stack[-1]
                b = stack[-2]
                stack = stack[:-2]
                stack.append(1 if a > b else 0)
            elif command == "<":
                a = stack[-1]
                b = stack[-2]
                stack = stack[:-2]
                stack.append(1 if a < b else 0)
            elif command == "+":
                a = stack[-1]
                b = stack[-2]
                stack = stack[:-2]
                stack.append(a + b)
            elif command == "_":
                stack.append(- stack.pop())
            elif command == "/":
                a = stack[-1]
                b = stack[-2]
                stack = stack[:-2]
                stack.append(a / b)
            elif command == "i":
                stack.append(int(stack.pop()))
            elif command == "`":
                stack.append(str(stack.pop()))
            elif command == "L":
                stack.append(len(stack.pop()))
            elif command == "W":
                stack.append([stack])
            elif command == "a":
                stack2.append(stack.pop())
            elif command == "s":
                a = stack[-1]
                b = stack[-2]
                stack = stack[:-2]
                stack.append(a, b)
            elif command == "R":
                stack = stack[::-1]
            elif command == "^":
                a = stack[-1]
                b = stack[-2]
                stack = stack[:-2]
                stack.append(a ** b)
            elif command == '"':
                stack.append("")
            elif command == "h":
                a = stack[-1]
                b = stack[-2]
                stack = stack[:-2]
                stack.append(a[:b])
            elif command == "t":
                a = stack[-1]
                b = stack[-2]
                stack = stack[:-2]
                stack.append(a[b:])
            elif command in "0123456789":
                stack.append(stack.pop() * 10 + int(command))
            elif command == "u":
                stack.append(sum(stack.pop()))
            elif command == "w":
                stack.append(sorted(stack.pop()))
            elif command == "i":
                a = stack[-1]
                b = stack[-2]
                stack = stack[:-2]
                stack.append(a[b])
            elif command == "l":
                a = stack[-1]
                b = stack[-2]
                stack = stack[:-2]
                stack.append([i for i, v in enumerate(a) if v == b])
            elif command == "D":
                a = stack.pop()
                stack.append(a)
                stack.append(a)
            elif command == "d":
                a = stack.pop()
                stack.append([k for k in range(1, a + 1) if a % k == 0])
            elif command == "p":
                a = stack.pop()
                stack.append(1 if all(a % k for k in range(2, a)) else 0)
            elif command == "J":
                a = stack[-1]
                b = stack[-2]
                stack = stack[:-2]
                stack.append(a.join(b))
            elif command == "C":
                a = stack[-1]
                b = stack[-2]
                stack = stack[:-2]
                stack.append(a.count(b))
            elif command == "c":
                stack.append(chr(stack.pop()))
            elif command == "o":
                stack.append(ord(stack.pop()))
        else:
            if command != '"':
                stack.append(stack.pop() + command)
    if stack:
        print(stack[-1])

if __name__ == '__main__':
    program = open(__import__('sys').argv[1], 'r').read()
    run(program)
