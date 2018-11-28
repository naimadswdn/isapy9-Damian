def repeat_y_or_n(t, msg):
    """Function to ask user, whether to repeat program or not.
    It is taking 'y' reply as yes and 'n' reply as no.
    :param t: name of the program/function - without brackets!
    :param msg: message that you would like user - it is string and need to be provided with "" or ''.
    :return: It is repeating or executing the program, depending of user decision(input).
    """
    print(msg)
    while True:
        user_choice = input('Please type "y" if yes, or "n" if no.')
        if user_choice == 'y':
            t()
            print(msg)
            continue
        elif user_choice == 'n':
            break
        else:
            print('Wrong answer. Please type "y" or "n".')
            continue


