def minion_game(string):
    # your code goes here
    vowel = ['A','E','I','O','U']
    sum1 = 0
    sum2 = 0
    for i in range(len(string)):
        if string[i] in vowel:
            sum2 = sum2 + len(string) - i
        else:
            sum1 = sum1 + len(string) - i
    for k in stuart.values():
        sum1 = sum1 + k
    if sum1>sum2:
        print "Stuart " + str(sum1)
    elif sum2>sum1:
        print "Kevin " + str(sum2)
    else:
        print "Draw"
