def add_friend():
    new_friend = User('',0,0,'')
    new_friend = User('',0,0,'')
# Asking details of new friend
print_friend = 0
# Printing the list of friends
for friend in friends:
    print ('%d. %s %s aged %d with rating %.2f is online' % (print_friend +1, friend.salutation, friend.name,friend.age,friend.rating)
    print_friend=print_friend +1
# Choosing a friend from friend list
choose_friend = int(input("Choose from your friends"))
choosefriendpos = int(choose_friend) - 1
# If selection valid, return index of friend selected.
if choosefriendpos < len(friends):
return choosefriendpos
else:
print ('Invalid')
exit()






    def add_friend():
        new_friend = User('',0,0,'')
        new_friend = User('',0,0,'')
# Printing the list of friends
for friend in friends:
    print_friend = 0
    print ('%d. %s %s aged %d with rating %.2f is online' % (print_friend +1, friend.salutation, friend.name,friend.age,friend.rating)
# Choosing a friend from friend list
choose_friend = int(input())
x == int(choose_friend) - 1
# If selection valid, return index of friend selected.
if choose_friend < len(friends):
    return choose_friend
else:
print ('Invalid')
exit()
    '''
