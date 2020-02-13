import sys

def check(password):
    s = str(password)
    cl = None
    check1 = True
    check2 = False
    check2str = ""
    check2strs = []
    for c in s:
        if (cl != None):
            if (cl == c):
                if (not check2):
                    check2str = cl + c;
                    check2 = True
                else:
                    check2str = check2str + c
            else:
                if (check2):
                    if (len(check2str) == 2):
                        check2strs.append(check2str)
                check2 = False
                check2str = ""

            if (cl > c):
                check1 = False
                break
        cl = c
    if (len(check2str) == 2):
        check2strs.append(check2str)
    result = (check1 and len(check2strs) > 0)
    if (result):
        print "check1 =", check1, "check2strs =", check2strs
    return result

matched = 0
for password in range(138307, 654504 + 1):
    result = check(password)
    print "password =", password, "result =", result
    if result:
        matched = matched + 1

print "matched =", matched
