print('enter a string')
s=input()
if ''.join(reversed(s))== s:
    print('palindrome')
else:
    print('not a palindrome')
