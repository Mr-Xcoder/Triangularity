import sys

stack = []
visited_indices = []
additive_index = 0
mapFlag = False
filterFlag = False
STDIN = sys.stdin.read().split("\n")


def format_triangularity_code(code):
    formatted = []
    dot_length = (lambda n: int(n) + (n != int(n)))(len(code) ** .5) - 1
    for num in range(dot_length, -1, -1):
        line = num * "." + code[(dot_length - num) ** 2:][:(dot_length - num) * 2 + 1] + num * "."
        line = line + (dot_length * 2 + 1 - len(line)) * "."
        formatted.append(line)
    return "\n".join(formatted)


def run(code):
    register = []
    if "--format" in sys.argv[1:] or "-f" in sys.argv[1:]:
        print(format_triangularity_code(code))
        return
    global stack
    global mapFlag
    global filterFlag
    global visited_indices
    global additive_index
    lines = code.split('\n')
    length = len(code.split('\n'))
    if not mapFlag and not filterFlag:
        if not all(len(elem) == length * 2 - 1 for elem in lines):
            print("I smell no triangularity. YOU SHALL NOT PASS!")
            return
        for i in range(length - 1):
            if lines[i][:length + ~i] == lines[i][- (length + ~i):] == (length + ~i) * ".":
                continue
            else:
                print("I smell no triangularity. YOU SHALL NOT PASS!")
                return
    for index, command in enumerate(code):
        if index + additive_index not in visited_indices:
            visited_indices.append(index + additive_index)
        else:
            if not mapFlag and not filterFlag:
                continue
        if code[:index].count('"') % 2 == 0:
            if command == "M":
                additive_index_copy = additive_index
                stack_copy = stack
                mapped_list = []
                mapped = stack.pop()
                additive_index = index + 1
                mapFlag = True
                for ind, element in enumerate(mapped):
                    stack = [element]
                    run(code[index + 1: index + code[index:].find("}")])
                    mapped_list.append(stack[-1])
                stack = stack_copy + [mapped_list]
                mapFlag = False
                additive_index = additive_index_copy
            elif command == "F":
                additive_index_copy = additive_index
                stack_copy = stack
                filtered_list = []
                filtered = stack.pop()
                additive_index = index + 1
                filterFlag = True
                for ind, element in enumerate(filtered):
                    stack = [element]
                    run(code[index + 1: index + code[index:].find("{")])
                    if stack[-1]:
                        filtered_list.append(element)
                stack = stack_copy + [filtered_list]
                filterFlag = False
                additive_index = additive_index_copy
            elif command == "@":
                stack.append(stack.pop() + 1)
            elif command == "f":
                stack.append(int(stack.pop()))
            elif command == "P":
                stack.pop()
            elif command == "!":
                stack.append(int(not stack.pop()))
            elif command == ")":
                stack.append(0)
            elif command == "r":
                a = stack[-1]
                b = stack[-2]
                stack = stack[:-2]
                stack.append(list(range(a, b)))
            elif command == "E":
                stack.append(eval(stack.pop()))
            elif command == "e":
                stack.extend(stack.pop())
            elif command == "I":
                stack.append(STDIN[stack.pop() % len(STDIN)])
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
            elif command == "i":
                stack.append(STDIN)
            elif command == "`":
                stack.append(str(stack.pop()))
            elif command == "L":
                stack.append(len(stack.pop()))
            elif command == "W":
                stack = [stack]
            elif command == "w":
                stack.append([stack.pop()])
            elif command == "s":
                a = stack[-1]
                b = stack[-2]
                stack = stack[:-2]
                stack.append(a)
                stack.append(b)
            elif command == "S":
                a = stack[-1]
                b = stack[-2]
                stack = stack[:-2]
                try:
                    stack.append(a.index(b))
                except ValueError:
                    stack.append(-1)
            elif command == "R":
                stack.append(stack.pop()[::-1])
            elif command == "^":
                a = stack[-1]
                b = stack[-2]
                stack = stack[:-2]
                stack.append(a ** b)
            elif command == '"':
                stack.append("")
            elif command == "#":
                register.append(stack.pop())
            elif command == "$":
                stack.append(register[-1])
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
            elif command == "O":
                stack.append(sorted(stack.pop()))
            elif command == "m":
                a = stack[-1]
                b = stack[-2]
                stack = stack[:-2]
                stack.append(a[b % len(a)])
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
                stack.append(a.join(map(str, b)))
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
    if stack and not mapFlag and not filterFlag:
        print(stack[-1])


if __name__ == "__main__":
    program = open(__import__("sys").argv[1], "r").read()
    run(program)
