#
# Task: Lists
#
# Consider a list (list = []). 
#
# You can perform the following commands:
#   insert i e: Insert integer e at position i.
#   print: Print the list.
#   remove e: Delete the first occurrence of integer .
#   append e: Insert integer  at the end of the list.
#   sort: Sort the list.
#   pop: Pop the last element from the list.
#   reverse: Reverse the list.
#
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. 
# Iterate through each command in order and perform the corresponding operation on your list.

if __name__ == '__main__':
    
    cnt = int(input())
    
    ilist = list()
    command = list()

    for c in range(cnt):
        
        command = list(input().split())
        
        if command[0] == 'insert':
            ilist.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(ilist)
        elif command[0] == 'remove':
            ilist.remove(int(command[1]))
        elif command[0] == 'append':
            ilist.append(int(command[1]))
        elif command[0] == 'sort':
            ilist.sort()
        elif command[0] == 'pop':
            ilist.pop(-1)
        elif command[0] == 'reverse':
            ilist.reverse()
    

