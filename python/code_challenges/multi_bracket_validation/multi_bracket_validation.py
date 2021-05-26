from Data_Structures.stacks_and_queues.stacks_and_queues import Stack


def multi_bracket_validation(str):
    s = Stack()

    values = [ch for ch in str]
    for i in values:
        if i == '{' or i == '[' or i == '(':
            s.push(i)
        else:
            if i == '}' or i == ']' or i == ')':
                x=0
                if i == '}':
                    x = '{'
                if i == ']':
                    x = '['
                if i == ')':
                    x = '('

                if x == s.peek():
                    s.pop()
                else:
                    return False

    if s.top != None:
        return False
    else:
        return True
