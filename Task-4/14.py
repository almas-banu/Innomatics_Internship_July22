# Merge the Tools

def merge_the_tools(string, k):
    lst = []
    m = 0
    for i in range(len(string)//k):
        lst.append(string[m:m+k])
        m+=k
    for i in lst:
        print(''.join(list(dict.fromkeys(list(i)).keys())))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)