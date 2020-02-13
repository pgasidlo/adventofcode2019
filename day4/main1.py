def check(password):
    s = str(password)
    cl = None
    check1 = True
    check2 = False
    for c in s:
        if (cl != None):
            if (cl == c):
                check2 = True
            if (cl > c):
                check1 = False
                break
        cl = c
    return (check1 and check2)

matched = 0
for password in range(138307, 654504 + 1):
    result = check(password)
    # print "password =", password, "result =", result
    if result:
        matched = matched + 1

print "matched =", matched
