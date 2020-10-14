def message(msg):
    """ Prints a message for the user
     :param msg: the message to print"""
    print(msg)


def get_non_empty_string(question):
    """accepts only alpha characers for an answer """
    answer = input(question)
    while True:
        if answer.isalpha() == False:
            message("Please use alpha characters only!") 
            answer = input(question)
        else:
            return answer


def get_id():
    """ Ask for ID, validate to ensure is positive integer
    :returns: the ID value """
    while True:
        try:
            id = int(input('Enter art work ID: '))
            if id > 0:
                return id
            else:
                message('Please enter a positive number.')

        except ValueError:
            message('Please enter a number.')


