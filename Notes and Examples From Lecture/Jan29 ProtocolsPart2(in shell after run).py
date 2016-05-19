def always_accept(filename, description):
    return True
#Or we could pass it this function if we wanted never to accept a file:

def never_accept(filename, description):
    return False
#Or we could pass it this function if we wanted a user to decide at the console:

def user_decision(filename, description):
    print('A file is being offered')
    print('Filename: ' + filename)
    print('Description: ' + description)
    
    return input('Accept it?  [Y]es or [N]o? ').strip().upper() == 'Y'
