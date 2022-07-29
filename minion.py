#
# The Minion Game
#
# Game Rules
#
# Both players are given the same string, S .
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.
# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
#
# Your task is to determine the winner of the game and their score.
#
# Function Description
# Complete the minion_game in the editor below.
# minion_game has the following parameters:
# string string: the string to analyze
#
# Prints
# string: the winner's name and score, separated by a space on one line, 
# or Draw if there is no winner Input Format
#
# A single line of input containing the string S.
# Note: The string S will contain only uppercase letters: A - Z.
#

def minion_game(string):
    VOWELS = {'A','E','I','O','U'}
    
    def vcount(string, chars):
        cnt = 0
        for i in range(len(string)):
            if i + len(chars) > len(string):
                break
            if string.startswith(chars, i):
                cnt += 1
        return cnt
    # end vcount()
       
    def sum_count(string, loop=1):
        
        if loop > len(string):
            return 0, 0
        
        checked = set()
        K, S = 0, 0
        
        for i in range(len(string)):
            if loop+i > len(string):
                break
            C = string[i:loop+i]
            if C in checked:
                continue
            score = vcount(string, C)
            if C[0] in VOWELS:
                K += score
            else:
                S += score
        
            checked.add(C)
            
            print(C, ' ', score)
        return K, S
    # end sum_count()
    
    Kevin, Stuart = 0, 0
    
    for i in range(len(string)):
        K, S = sum_count(string, i+1)
        Kevin += K
        Stuart += S
        print(Kevin, Stuart)
        print(K, S)
    
    if Kevin > Stuart:
        print('Kevin ', Kevin)
    elif Stuart > Kevin:
        print('Stuart ', Stuart)
    else:
        print('Draw')
# end minion_game()

if __name__ == '__main__':
    s = input()
    minion_game(s)