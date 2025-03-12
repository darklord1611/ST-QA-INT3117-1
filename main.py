

def check_password(x, n, s):
    result = "weak"
    if x < 8 or x > 64:
        result = "invalid"
    elif x >= 16 and n == True and s == True:
        result = "strong"
    elif x >= 16 and (n == True or s == True):
        result = "medium"
    return result

