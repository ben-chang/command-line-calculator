'''
Calculator Test
TEST FOR CLI CALCULATOR IN PYTHON
'''
# MAIN FUNCTIONS
def calc():
    '''
    Initialise calculator
    '''
    calc_running = True
    print "Ctrl-C or type 'calc_exit' to exit"
    print "Functionality: Only two nums and an operator e.g. 1 + 2"
    while calc_running:
        user_input = raw_input("in > ")
        if user_input == 'calc_exit':
            print 'Exiting calculator'
            calc_running = False
        else:
            evaluate(user_input)

def evaluate(user_input):
    '''
    Evaluate user input
    '''
    output_text = ''
    split_input = user_input.split()
    for i in split_input:
        split_input[split_input.index(i)] = check_valid_input(i)

    if len(split_input) >= 3:
        x_num = split_input[0]
        y_num = split_input[2]

        if split_input[1] == '+':
            evaluated = x_num + y_num
        elif split_input[1] == '-':
            evaluated = x_num - y_num
        elif split_input[1] == '*':
            evaluated = x_num * y_num
        elif split_input[1] == '/':
            evaluated = x_num / y_num
        else:
            evaluated = 'Invalid operator'
        output_text += str(evaluated)
    else:
        output_text += 'Invalid expression: {0}'.format(str(user_input))

    print "out > " + output_text

# UTILITIES
def check_if_operator(input_data):
    '''
    Checks if input is operator
    '''
    if input_data == '+':
        return '+'
    elif input_data == '-':
        return '-'
    elif input_data == '*':
        return '*'
    elif input_data == '/':
        return '/'
    else:
        return False

def check_valid_input(input_data):
    '''
    Checks if input is float
    '''
    try:
        return float(input_data)
    except ValueError:
        output = check_if_operator(input_data)
        if output is False:
            return 'Please enter a valid input (0-9, +, -, *, /)'
        else:
            return output



calc()
