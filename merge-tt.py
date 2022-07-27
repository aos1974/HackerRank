#
# Merge th Tools!
#
# Given a string "string"
# Given a "k" - integer
# Split the "string" in to substring k-times
# and deduplicate results substrings
#
# Example
# string = 'AAABCADDE'
# k = 3
# substrings = ['AAA', 'BCA', 'DDE'] 
# deduplicated substrings = ['A', 'BCA', 'DE'] 
#


def merge_the_tools(string, k):
    parts = len(string)//k
    lst = [string[p*k:k+p*k] for p in range(parts)]
    lst = map(lambda l: ''.join(sorted(set(l), key=l.index)), lst)
    for l in list(lst):
        print(l)
# end merge_the_tools()

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    