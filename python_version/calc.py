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
    for i in check_float(user_input):
        if i == check_float(user_input)[0]:
            output_text = i
        elif i == check_float(user_input)[1]:
            user_input = i
    print "out > " + output_text

# UTILITIES
def check_float(user_input):
    '''
    Checks if input is float
    '''
    try:
        return [user_input, float(user_input)]
    except ValueError:
        return ['Please enter a valid input (0-9, +, -, *, /)']



calc()
