from fille import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from datetime import datetime
# Function to add friend
def add_friend():

    new_friend = Spy('', '', 0, 0.0)

    # Asking details of new friend
    print("Please add your friend's name: ")
    new_friend.name = input()

    if(new_friend.name > 0):
        print("Are they Mr. or Ms.?: ")
        new_friend.salutation = input()

        if(new_friend.salutation > 0):
            new_friend.name = new_friend.salutation + " " + new_friend.name
        else:
            print ('Provide proper salutation')
            print("Age?")
        new_friend.age = int(input())
        print("Spy rating?")

        new_friend.rating = float(input())

        if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
            friends.append(new_friend)
            print ('\n Friend Added!')
        else:
            print ('\n Sorry! Invalid entry. We can\'t add spy with the details you provided')
    else:
        print ('\n Provide proper name!!')

    # Returning length of friends list i.e  number of friends
    return len(friends)

# Function for selection of friend
def select_a_friend():
    item_number = 0

    # Printing the list of friends
    for friend in friends:
        print ('%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating))

        item_number = item_number + 1

    # Choosing a friend from friend list
    print("Choose from your friends")
    friend_choice = input()


    friend_choice_position = int(friend_choice) - 1
    # If selection valid, return index of friend selected.

    if friend_choice_position < len(friends):

        return friend_choice_position
    else:

        print ('Choose from the people given above')
        exit()
def send_message():

    # Selcting a friend
    friend_choice = select_a_friend()
    # Entering name of image
    original_image = raw_input("What is the name of the image?")
    # Defining output encoded image name
    output_path = "output.jpg"
    # Inputting the message to be sent
    text = raw_input("What do you want to say? ")
    # Checking if a valid message
    if len(text) >0:
        # Encoding the message
        Steganography.encode(original_image, output_path, text)

        new_chat = ChatMessage(text,True)
        # Appending the new message into chats list
        friends[friend_choice].chats.append(new_chat)

        print ("Your secret message image is ready!")
    else:
        print ('Enter a valid message ')

# Defining a function to read a message
def read_message():

    # Selecting a friend
    sender = select_a_friend()
    # Inputting name of file
    output_path = input()
    # Decoding the secret message
    secret_text = Steganography.decode(output_path)
    number_of_words = len(secret_text.split())

    # Checking the number of words in incoming message
    if number_of_words > 100:
        # If number of words in message is greater than 100 , we delete the friend who sent it.
        print ('This friend talks too much, Unfriending!! ')
        del friends[sender]
    else:
        # Check for empty secret message
        if len(secret_text) > 0:
            # Checking for special cases of emergency
            if secret_text == "SOS" or secret_text == "SAVE ME" or secret_text == "HELP":
                print ('Immediate help required.')

            new_chat = ChatMessage(secret_text,False)
            friends[sender].chats.append(new_chat)

            print ("Your secret message has been saved!")
        else:
            print ('Empty message')


# Defining function to read chat history
def read_chat_history():
# Selecting a friend

    read_for = select_a_friend()

    print ('\n')

    # Displaying chat history
    for chat in friends[read_for].chats:

        # Using various colors for printing chat history
        if chat.sent_by_me:
            print ('[%s]' % (colored([chat.time.strftime("%d %B %Y")] ,'blue')))
            print ('%s:' % (colored('You said:','red')))
            print ('%s:' % (colored(chat.message,'yellow')))
        else:
            print ('[%s] ' % (colored([chat.time.strftime("%d %B %Y")],'blue')))
            print ('%s said:' %(colored((friends[read_for].name),'red')))
            print (' %s ' % (colored((chat.message),'yellow')))


# Function to display message corresponding to different spy ratings
def display_msg_acc_spy_rating(spy):

    if spy.rating > 4.5:

        print ('Great ace!')

    elif spy.rating > 3.5 and spy.rating <= 4.5:

        print ('You are one of the good ones.')
    else:

        print ('You can always do better')


# Function to start chat
def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name

    # Checking for age verification of spy
    if spy.age > 12 and spy.age < 50:

        # Printing spy details after authentication
        print ("Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard")

        show_menu = True

        # Display menu of options for a spy
        while show_menu:

            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n " \
                           "3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n" \
                           " 6. Close Application \n"
            print(menu_choices)
            menu_choice = input()

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print ('You have %d friends' % (number_of_friends))
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print ('Sorry you are not of the correct age to be a spy')
