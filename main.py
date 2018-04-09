from spy_details import spy,Spy,ChatMessage  # for importing variables from another file named spy_details
import csv # importing csv files
from colorama import Fore #for importing foreground colour format
from steganography.steganography import Steganography #importing Steganography module from steganography class of steganography library
from datetime import datetime #importing date and time module from datetime class
f=datetime.now()      #calling function now from datetime library
print f.strftime("%b %d %Y %H:%M:%S") #stringtimeformat
print "Hello !!"   #To print a string
print "Let's get started."
Status_message = ["Winners never quit, qitters never win.","If opportunity does not knock,build a door.","Life begins at the end of your comfort zone."] #menu of old statuses
friend1=Spy('Anshu','Ms.',22,4) #details of friend1 using Spy class
friend2=Spy('Priyesh','Mr.',24,5.6) #details of friend2 using Spy classs
friends=[friend1,friend2] #list of friends
messages=[]

def chat_history():
    selected_frnd=select_a_friend()
    choice=friends[selected_frnd].name
    for i in messages:
        if choice==i.receiver:
            print Fore.BLUE + "At time" + i.time
            print Fore.RED + "Received by" +i.receiver
            print Fore.BLACK + "Message sent: " + i.message




def load_frnds():
    with open('friends.csv', 'rb') as friends_data:
        reader = list(csv.reader(friends_data))

        for row in reader[1:]:
            spy = Spy(name=row[0],salutation=row[1],age=row[3],ratings=row[2])
            friends.append(spy)

load_frnds()


def add_status(c_status):
    if c_status != None: #if the spy does not choose from old statuses
        print "Your current status is : " + c_status
    else:
        print "You don't have any status currently."
    existing_status = raw_input("Do you want to select from your old status? Y/N ")
    if existing_status.upper()=="N":
        new_status= raw_input("Enter your status: ")
        if len(new_status)>0:
            updated_status=new_status
            Status_message.append(updated_status) #adding new status in the list of already stored statuses
        else:
            print "Enter a valid status."
    elif existing_status.upper()=="Y":
        serial_number=1
        for old_status in Status_message:
            print str(serial_number) + ". " + old_status
            serial_number=serial_number + 1
        user_choice = input("Enter your choice: ") #asking user for choosing a choice
        updated_status = Status_message[user_choice-1]

    return updated_status

def add_friend():
    frnd=Spy('','',0,0.0)  #to add a new friend
    frnd.name = raw_input('What is your friend \'s name? ')
    frnd.sal = raw_input("What should we call your friend?")
    frnd.age = input('What is your friend\'s age ? ')
    frnd.ratings = input('What is your friend\'s rating ?')
    frnd.is_online= True
    if len(frnd.name)>2 and 14<frnd.age<60 and frnd.ratings>spy.ratings:  # conditons for adding new friend
        friends.append(frnd) #adding this new friend in the list of already existing friends
        with open('friends.csv','a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([frnd.name, frnd.sal, frnd.ratings, frnd.age, frnd.is_online])
    else:
        print "Friend cannot be added."
    return len(friends)  # will return to add_friend()


def select_a_friend():  # defining a function
    serial_no = 1
    for frnd in friends:
        print str(serial_no) + ".  " + frnd.name
        serial_no = serial_no + 1
    user_selected_frnd = input("Enter your choice: ")  # asking user choice to which friend to select
    user_selected_frnd_index = user_selected_frnd - 1
    return user_selected_frnd_index  # returning data to select_a_friend()


def send_a_message():  # definig function
    selected_frnd = select_a_friend()
    original_image = raw_input("What is the name of your image? ")  # asking user about the name of image
    secret_text = raw_input("What is your secret text? ")  # asking about what secret text you need to save in image
    output_path = "output.png"  # giving the output_path or we can say name where the  merged image and secret text will be stored an donly the image will be displayed.
    Steganography.encode(original_image,output_path,secret_text)  # encoding the image with secret text.
    print "Your secret text has been successfully encoded"
    new_chat = ChatMessage(secret_text,True)
    friends[selected_frnd].chats.append(new_chat)  # appending in friends list the new_chat dictionary
    print "Your secret message is ready. "



def read_a_message():
    selected_frnd = select_a_friend()
    output_path = raw_input("Which image you want to decode? ")  # asking about which image user need to decode
    secret_text = Steganography.decode(output_path)  # decoding the text from image
    print "Secret text is " + secret_text
    new_chat = ChatMessage(secret_text,False)
    friends[selected_frnd].chats.append(new_chat)  # appending
    print "Your secret message has been saved. "

def spy_chat(spy_name,spy_age,spy_ratings):  #function is defined
    print "Here are your options " + spy.name
    current_status=None
    show_menu = True
    while show_menu: #menu added so that spy can choose options
        choice=input("What do you want to do? \n 1.Add a status \n 2.Add a friend \n 3.Send a secret message \n 4.Read a secret message \n 5.Chat history \n 0.Exit ")
        if choice==1:
            current_status=add_status(current_status)
            print "Updated status is: " + current_status
        elif choice==2:
            friend_no=1
            no_of_friends=add_friend()
            print "You have " + str(no_of_friends) + " friends."
            for i in friends:
                print(str)(friend_no)+". "+i.name
                friend_no=friend_no+1
        elif choice==3:
            send_a_message()
        elif choice==4:
            read_a_message()
        elif choice==5:
            print chat_history()
        elif choice==0:
            show_menu = False
        else:
            print "Invalid option."


spy_exist=raw_input("Are you a new user?(Y/N) ") #to check if spy is already registered or not
if spy_exist.upper()=="N":
    print "Welcome back "+ spy.name
    spy_chat(spy.name,spy.age,spy.ratings)

elif spy_exist.upper()=="Y": #if spy is new then the registration starts
    spy = Spy(" "," ",0,0.0)
    spy.name = raw_input("What is your spy name?")
    if spy.name.isspace(): #to ensure that input is not space
        print "Enter a valid name."

    elif len(spy.name)>2: #to check the length of the input
        print "Welcome " + spy.name +". Glad to have you with us."
        spy.salutation=raw_input("What should we call you (Mr. or Ms.)?")
        if spy.salutation=="Mr." or spy.salutation=="Ms.":
            spy.name=spy.salutation + spy.name  #concatenation
            print "Alright " + spy.name + ". I would like to know a little bit more about you."
            spy.age = input("What is your age?")
            if 60>spy.age>14:
                print "Your age is correct."
                spy.ratings = input("What is your ratings?")
                if spy.ratings>8.0:
                    print "Great spy" #commenting under nested ifs
                elif 5.5<spy.ratings<=8.0:
                    print "Average spy"
                elif 3.0<spy.ratings<=5.5:
                    print "Bad spy"
                else:
                    print "Are you really a spy?"
                spy_is_online=True
                print "Authentication is completed. Welcome %s of age: %d having ratings %f " % (spy.name,spy.age,spy.ratings)
                spy_chat(spy.name,spy.age,spy.ratings) # to provide options to the spy
            else:
                print "Sorry.Your age is not eligible to be a spy."
        else:
            print"Invalid salutation"
    else:
        print "Invalid name. Please enter a valid name"
else:
    print"Invalid entry"