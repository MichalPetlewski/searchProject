def all_valid(CVV, numbers):
    if len(CVV) == 3 and CVV.isdigit() == True and len(numbers) == 16 and numbers.isdigit() == True:
        return True

    else:
        return False

def comment_not_null(comment : str):
    if comment != None:
        return True
    else:
        return False 
