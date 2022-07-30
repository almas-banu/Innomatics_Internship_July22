# The Minion Game

def minion_game(string):
    s = string
    st = 0
    kv = 0
    vow = 'AEIOU'
    for i in range(len(s)):
        if s[i] not in vow:
            st = st+(len(s)-i)
        else:
            kv = kv+(len(s)-i)
    if st>kv:
        print("Stuart",st)
    elif kv>st:
        print("Kevin",kv)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)