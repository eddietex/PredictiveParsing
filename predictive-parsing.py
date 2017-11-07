import sys

# lookahead index will be used to iterate as a subscript in the user-input string
lookahead = 0

# used to store the user input in infix notation
usr = 'nil'

# will keep the result
res = ''

# will be true whenever the program finish processing the user input with the lookahead
finish = False

# will keep the user input expression's length
input_size = -1

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def digit():
    global res
    if lookahead_in_digits():
        t = usr[lookahead]
        match(t)
        res += t
    else:
        present_syntax_error()


def factor():
    if lookahead_in_digits():
        digit()
    elif lookahead_equals('('):
        match('(')
        expr()
        match(')')
    else:
        present_syntax_error()


def rest3():
    global res
    if lookahead_equals('%'):
        match('%')
        factor()
        res += '%'
    else:
        pass


def operand():
    factor()
    rest3()


def rest2():
    global res
    if lookahead_equals('*'):
        match('*')
        operand()
        res += '*'
        rest2()
    elif lookahead_equals('/'):
        match('/')
        operand()
        res += '/'
        rest2()
    else:
        pass


def operation():
    operand()
    rest2()


def rest():
    global res
    if lookahead_equals('+'):
        match('+')
        operation()
        res += '+'
        rest()
    elif lookahead_equals('-'):
        match('-')
        operation()
        res += '-'
        rest()
    else:
        pass


def expr():
    operation()
    rest()


def match(t):
    if lookahead_equals(t):
        move_lookahead()
    else:
        present_syntax_error()


# check if the position lookahead is pointing is equal to t
def lookahead_equals(t):
    if lookahead >= input_size:
        return False
    elif usr[lookahead] == t:
        return True
    else:
        return False


# increment lookahead by 1
def move_lookahead():
    global lookahead
    lookahead += 1

    # if this is the last input character, finish = true
    if lookahead == input_size:
        global finish
        finish = True


# check if the position lookahead points is a digit
def lookahead_in_digits():
    # presents syntax error whenever the program tries to put lookahead in a index higher than the last position of the
    # user input
    if lookahead >= input_size or finish:
        present_syntax_error()
    else:
        if usr[lookahead] in digits:
            return True
        else:
            return False


def present_syntax_error():
    print("Syntax Error")
    input("Press Enter to continue...")
    sys.exit()


# main function
def main():
    global usr
    global input_size
    usr = input("Enter de infix expression to be converted to "
                "postfix expression:\n")
    input_size = len(usr)

    # calling starting symbol
    expr()

    # presents syntax error if the program execution ends but not all the user input was processed
    if not finish:
        present_syntax_error()
    else:
        print('Postfix:', res)

    input("Press Enter to continue...")


# main execution
main()
