# sWAP cASE

def swap_case(s):
    s1 = ""
    for c in s:
        if c.isupper():
            c = c.lower()
        else:
            c = c.upper()
        s1+="".join(c)
    return s1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
