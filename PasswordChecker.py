def pswd_check(user_pswd):
    # Character length greater than 8
    if len(user_pswd) < 8:
        return False

#    # At least 1 uppercase character
#    seen_upper = False
#    for char in user_pswd:
#        if char.isupper():
#            seen_upper = True
#            break
#    if seen_upper == False:
#        return False
#    # At least 1 lowercase character
#    seen_lower = False
#    for char in user_pswd:
#        if char.islower():
#            seen_lower = True
#            break
#    if seen_lower == False:
#        return False
#    # At least 1 number
#    seen_number = False
#    for num in user_pswd:
#        if num.isdigit():
#            seen_number = True
#            break
#    if seen_number == False:
#        return False
#    return True
#    # At least 1 underscore
#    seen_underscore = False
#    for char in user_pswd:
#        if char == '_':
#            seen_underscore = True
#            break
#    if seen_underscore == False:
#        return False
#    return True

    # All in one
    seen_upper = False
    seen_lower = False
    seen_number = False
    seen_underscore = False
    for i in user_pswd:
        if i.isupper():
            seen_upper = True
            continue
        if i.islower():
            seen_lower = True
            continue
        if i.isdigit():
            seen_number = True
            continue
        if i == '_':
            seen_underscore = True
    if seen_upper == False or seen_lower == False or seen_number == False or seen_underscore == False:
        return False
    return True
