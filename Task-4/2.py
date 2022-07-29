# String Split and Join

def split_and_join(line):
    # write your code here
    line = line.split(" ")
    x = "-".join(line)
    return x
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)