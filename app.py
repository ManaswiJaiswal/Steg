from PIL import Image
class User:
    friend_dict = {}
    def __init__(self, name, age, rating,status):
      self.name = name
      self.age = age
      self.rating = rating
      self.status = status
      def displayUser(self):
       print("name : ", self.name, ", age: ", self.age, ", rating ", self.rating, ", status: ", self.status)
emp1 = User('Anna', 28, 3, 'Active')
emp2 = User('Dan', 26, 3, 'Active')
emp3 = User('Sarah', 37, 4, 'Active')
emp4 = User('Becky', 33, 5, 'Active')
emp5 = User('Will', 30, 4, 'Inactive')

sarah_messages=[]
anna_messages=[]
becky_messages=[]
dan_messages=[]
#friends
friends = [emp1,emp2,emp3,emp4]
print('Hello Will')
choice = ['1. Add Friend', '2. Status', '3. Chat', '4. Rating']
print(*choice, sep = "\n")
#choosing options
print('Enter Option')
wchoice=int(input())
if wchoice==1:
    print('Add Friend')
    will_friend=[]
    name = ['1.Anna', '2. Dan', '3. Sarah', '4. Becky']
    print(*name, sep = "\n")
    print('Sending friend request to(enter number):')
    wfriend=int(input())
    if wfriend== 1:
        will_friend.append( 'Anna' )
        print(will_friend)
    elif wfriend== 2:
        will_friend.append( 'Dan' )
        print(will_friend)
    elif wfriend== 3:
        will_friend.append( 'Sarah' )
        print(will_friend)
    elif wfriend== 4:
         print('Request not sent.')
         exit()
elif wchoice==2:
    print('Status')
    wstatus=['1. See', '2. Change']
    print(*wstatus, sep = "\n")
    print('Enter Option')
    wstatuschoice=int(input())
    if wstatuschoice==1:
        print(emp5.status)
    elif wstatuschoice==2:
        emp5.status='Active'
        print(emp5.status)
elif wchoice==4:
    print('Rating')
    wrating=['1. See', '2. Change']
    print(*wrating, sep = "\n")
    print('Enter Option')
    wratingchoice=int(input())
    if wratingchoice==1:
        print(emp5.rating)
    elif wratingchoice==2:
        print('enter new rating')
        wredit=int(input())
        emp1.rating=wredit
        print(wredit)
        exit()
elif wchoice==3:
    print('Chat')
    #sending a message
    print('Choose position of a friend ')
    name = ['1.Anna', '2. Dan', '3. Sarah', '4. Becky']
    print(*name, sep = "\n")
    chosen_friend=int(input())
    chosen_friend_position = int(chosen_friend) - 1
    if chosen_friend_position < len(friends):
        if chosen_friend==1:
            print('Anna')
        elif chosen_friend==2:
            print('Dan')
        elif chosen_friend==3:
            print('Sarah')
        elif chosen_friend==4:
            print('Becky')
        else:
            print('Invalid choice')
            exit()
    else:
        print ('Invalid Choice')
        exit()
    def message():
        print('Enter your message')
# Choosing a friend
        chosen_friend = choose_friend()
    from PIL import Image
    def encode_image(img, msg):
        length = len(msg)
    # limit length of message to 255
        if length > 255:
            print("text too long! (don't exeed 255 characters)")
            return False
        if img.mode != 'RGB':
            print("image mode needs to be RGB")
            return False
    # use a copy of image to hide the text in
        encoded = img.copy()
        width, height = img.size
        index = 0
        for row in range(height):
            for col in range(width):
                r, g, b = img.getpixel((col, row))
            # first value is length of msg
                if row == 0 and col == 0 and index < length:
                    asc = length
                elif index <= length:
                    c = msg[index -1]
                    asc = ord(c)
                else:
                    asc = r
                encoded.putpixel((col, row), (asc, g , b))
                index += 1
        return encoded
    def decode_image(img):
        """
         check the red portion of an image (r, g, b) tuple for
        hidden message characters (ASCII values)
        """
        width, height = img.size
        msg = ""
        index = 0
        for row in range(height):
            for col in range(width):
                try:
                    r, g, b = img.getpixel((col, row))
                except ValueError:
                # need to add transparency a for some .png files
                    r, g, b, a = img.getpixel((col, row))
            # first pixel r value is length of message
                if row == 0 and col == 0:
                    length = r
                elif index <= length:
                    msg += chr(r)
                index += 1
        return msg
# pick a .png or .bmp file you have in the working directory
# or give full path name
    original_image_file = "picture.png"
#original_image_file = "picture.png"
    img = Image.open(original_image_file)
# image mode needs to be 'RGB'
    print(img, img.mode)  # test
# create a new filename for the modified/encoded image
    encoded_image_file = "enc_" + original_image_file
# don't exceed 255 characters in the message
    secret_msg = input()
    img_encoded = encode_image(img, secret_msg)
    if img_encoded:
    # save the image with the hidden text
        img_encoded.save(encoded_image_file)
    # view the saved file, works with Windows only
    # behaves like double-clicking on the saved file
    if chosen_friend==1:
        anna_messages.append(secret_msg)
    elif chosen_friend==2:
        dan_messages.append(secret_msg)
    elif chosen_friend==3:
        sarah_messages.append(secret_msg)
    elif chosen_friend==4:
        becky_messages.append(secret_msg)
    else:
        print('Message not sent')
        exit()
    '''
    # or activate the default viewer associated with the image
    # works on more platforms like Windows and Linux
    import webbrowser
    webbrowser.open(encoded_image_file)
    '''
    #switching user so that other user can read the message
    print('Switch User?(enter yes or no)')
    switched_user_choice=input()
    if switched_user_choice=='yes':
        print('Enter username:')
    elif switched_user_choice=='no':
        exit()
    suname=input()
    if str(suname)=='Sarah' or 'Dan' or 'Becky' or 'Anna':
        print('Enter password')
    else:
        print('Incorrect username')
        exit()
    passa=input()
    if passa=='sarahpas':
        choice = ['1. Add Friend', '2. Status', '3. Chat', '4. Rating']
        print(*choice, sep = "\n")
        print('Enter Option')
        schoice=int(input())
        if schoice==1:
            sarah_friend=[]
            name = ['1.Anna', '2. Dan', '3. Will', '4. Becky']
            print(*name, sep = "\n")
            print('Sending friend request to(enter number):')
            sfriend=int(input())
            if sfriend== 1:
                print('Request not sent.')
            elif sfriend== 2:
                print('Request not sent.')
            elif sfriend== 3:
                sarah_friend.append( 'Will' )
                print(sarah_friend)
            elif sfriend== 4:
                sarah_friend.append( 'Becky' )
                print(sarah_friend)
                exit()
        elif schoice==2:
            ss=['1. See', '2. Change']
            print(*ss, sep = "\n")
            print('Enter Option')
            ssedit=int(input())
            if ssedit==1:
                print(emp3.status)
            elif ssedit==2:
                emp1.status='Inactive'
                print(emp3.status)
                exit()
        elif schoice==4:
            sr=['1. See', '2. Change']
            print(*sr, sep = "\n")
            print('Enter Option')
            sratingchoice=int(input())
            if sratingchoice==1:
                print(emp3.rating)
                exit()
            elif sratingchoice==2:
                print('enter new rating')
                sredit=int(input())
                emp3.rating=sredit
        elif schoice==3:
             # view the saved file, works with Windows only
            # behaves like double-clicking on the saved file
             # get the hidden text back ...
            if chosen_friend==3:
                img2 = Image.open(encoded_image_file)
                hidden_text = decode_image(img2)
                print("Hidden text:\n{}".format(hidden_text))
                print('See Image?(yes/no)')
                see_image=input()
                if see_image== 'yes':
                    import os
                    os.startfile(encoded_image_file)
                elif see_image=='no':
                    exit()
            else:
                print('No messages')
                exit()
    elif passa=='annapas':
        print('Hello Anna')
        a = ['1. Add Friend', '2. Status', '3. Chat', '4. Rating']
        print(*a, sep = "\n")

        print('Enter Option')
        ach=int(input())
        if ach==1:
            anna_friend=[]
            name = ['1.Sarah', '2. Dan', '3. Will', '4. Becky']
            print(*name, sep = "\n")
            print('Sending friend request to(enter number):')
            af=int(input())
            if af== 1:
                print('Request not sent.')
            elif af== 2:
                anna_friend.append( 'Dan' )
                print(anna_friend)
            elif af== 3:
                print('Request not sent.')
            elif af== 4:
                print('Request not sent.')
                exit()
        elif ach==2:
            ans=['1. See', '2. Change']
            print(*ans, sep = "\n")
            print('Enter Option')
            asedit=int(input())
            if asedit==1:
                print(emp1.status)
            elif asedit==2:
                emp1.status='Inactive'
                print(emp1.status)
                exit()
        elif ach==4:
            ar=['1. See', '2. Change']
            print(*ar, sep = "\n")
            print('Enter Option')
            arch=int(input())
            if arch==1:
                print(emp1.rating)
                exit()
            elif arch==2:
                print('enter new rating')
                aredit=int(input())
                emp1.rating=aredit
        elif ach==3:
            if chosen_friend==1:
                 # view the saved file, works with Windows only
                # behaves like double-clicking on the saved file
                 # get the hidden text back ...
                img2 = Image.open(encoded_image_file)
                hidden_text = decode_image(img2)
                print("Hidden text:\n{}".format(hidden_text))
                print('See Image?(yes/no)')
                see_image=input()
                if see_image== 'yes':
                    import os
                    os.startfile(encoded_image_file)
                elif see_image=='no':
                    exit()
            else:
                print('No messages')
                exit()
    elif passa=='beckypas':
        print('Hello Becky')
        a = ['1. Add Friend', '2. Status', '3. Chat', '4. Rating']
        print(*a, sep = "\n")

        print('Enter Option')
        bch=int(input())
        if bch==1:
            becky_friend=[]
            name = ['1.Anna', '2. Sarah', '3. Will', '4. Dan']
            print(*name, sep = "\n")
            print('Sending friend request to(enter number):')
            bf=int(input())
            if bf== 1:
                becky_friend.append( 'Anna' )
                print(becky_friend)
            elif bf== 2:
                becky_friend.append( 'Sarah' )
                print(becky_friend)
            elif bf== 3:
                becky_friend.append( 'Will' )
                print(becky_friend)
            elif bf== 4:
                becky_friend.append( 'Dan' )
                print(becky_friend)
                exit()
        elif bch==2:
            bs = ['1. See', '2. Change']
            print(*bs, sep = "\n")
            print('Enter Option')
            bsedit=int(input())
            if bsedit==1:
                print(emp4.status)
            elif bsedit==2:
                emp4.status='Inactive'
                print(emp4.status)
                exit()
        elif bch==4:
            br=['1. See', '2. Change']
            print(*br, sep = "\n")
            print('Enter Option')
            brch=int(input())
            if brch==1:
                print(emp4.rating)
                exit()
            elif brch==2:
                print('enter new rating')
                bredit=int(input())
                emp4.rating=bredit
        elif bch==3:
            if chosen_friend==4:
                 # view the saved file, works with Windows only
                # behaves like double-clicking on the saved file
                 # get the hidden text back ...
                img2 = Image.open(encoded_image_file)
                hidden_text = decode_image(img2)
                print("Hidden text:\n{}".format(hidden_text))
                print('See Image?(yes/no)')
                see_image=input()
                if see_image== 'yes':
                    import os
                    os.startfile(encoded_image_file)
                elif see_image=='no':
                    exit()
            else:
                print('No messages')
                exit()
    elif passa=='danpas':
        print('Hello Dan')
        a = ['1. Add Friend', '2. Status', '3. Chat', '4. Rating']
        print(*a, sep = "\n")

        print('Enter Option')
        dch=int(input())
        if dch==1:
            dan_friend=[]
            name = ['1.Sarah', '2. Anna', '3. Will', '4. Becky']
            print(*name, sep = "\n")
            print('Sending friend request to(enter number):')
            df=int(input())
            if df== 1:
                print('Request not sent.')
            elif df== 2:
                dan_friend.append( 'Anna' )
                print(dan_friend)
            elif df== 3:
                print('Request not sent.')
            elif df== 4:
                print('Request not sent.')
                exit()
        elif dch==2:
            ds = ['1. See', '2. Change']
            print(*ds, sep = "\n")
            print('Enter Option')
            dsedit=int(input())
            if dsedit==1:
                print(emp2.status)
            elif dsedit==2:
                emp2.status='Inactive'
                print(emp2.status)
                exit()
        elif dch==4:
            dr=['1. See', '2. Change']
            print(*dr, sep = "\n")
            print('Enter Option')
            drch=int(input())
            if drch==1:
                print(emp2.rating)
                exit()
            elif drch==2:
                print('enter new rating')
                aredit=int(input())
                emp2.rating=aredit
        elif dch==3:
            if chosen_friend==2:
                 # view the saved file, works with Windows only
                # behaves like double-clicking on the saved file
                 # get the hidden text back ...
                img2 = Image.open(encoded_image_file)
                hidden_text = decode_image(img2)
                print("Hidden text:\n{}".format(hidden_text))
                print('See Image?(yes/no)')
                see_image=input()
                if see_image== 'yes':
                    import os
                    os.startfile(encoded_image_file)
                elif see_image=='no':
                    exit()
            else:
                print('No messages')
                exit()
    else:
        print('Incorrect Password')
        exit()
