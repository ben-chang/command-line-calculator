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
        if len(check_valid_input(i)) == 2:
            split_input[split_input.index(i)] = check_valid_input(i)[1]
        else:
            split_input[split_input.index(i)] = check_valid_input(i)[0]

    if len(split_input) >= 3:
        x_int = split_input[0]
        y_int = split_input[2]

        if split_input[1] == '+':
            evaluated = x_int + y_int
        elif split_input[1] == '-':
            evaluated = x_int - y_int
        elif split_input[1] == '*':
            evaluated = x_int * y_int
        elif split_input[1] == '/':
            evaluated = x_int / y_int
        else:
            output_text += 'Invalid operator'
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
        return [input_data, float(input_data)]
    except ValueError:
        output = check_if_operator(input_data)
        if output is False:
            return ['Please enter a valid input (0-9, +, -, *, /)']
        else:
            return output



calc()
