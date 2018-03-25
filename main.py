from spy_details import spy_name,spy_salutation,spy_age,spy_ratings # for importing variables from another file named spy_detais
print "Hello !!"   #To print a string
print "Let's get started."

def start_chat(spy_name,spy_age,spy_ratings):  #function is defined
    print "Here are your options " + spy_name
    show_menu = True
    while show_menu: #menu added so that spy can choose options
        choice=input("What do you want to do? \n 1.Add a status \n 2.Add a friend \n 0.Exit ")
        if choice==1:
            print "Will add a status."
        elif choice==2:
            print "Will add a friend."
        elif choice==0:
            show_menu = False
        else:
            print "Invalid option."


spy_exist=raw_input("Are you a new user?(Y/N) ") #to check if spy is already registered or not
if spy_exist.upper()=="N":
    print "Welcome back "+ spy_salutation + spy_name
    start_chat(spy_name,spy_age,spy_ratings)

elif spy_exist.upper()=="Y": #if spy is new then the registration starts
    spy_name = raw_input("What is your spy name?")
    if spy_name.isspace(): #to ensure that input is not space
        print "Enter a valid name."

    elif len(spy_name)>2: #to check the length of the input
        print "Welcome " + spy_name +". Glad to have you with us."
        spy_salutation=raw_input("What should we call you (Mr. or Ms.)?")
        if spy_salutation=="Mr." or spy_salutation=="Ms.":
            spy_name=spy_salutation + spy_name  #concatenation
            print "Alright " + spy_name + ". I would like to know a little bit more about you."
            spy_age = input("What is your age?")
            if 60>spy_age>14:
                print "Your age is correct."
                spy_ratings = input("What is your ratings?")
                if spy_ratings>8.0:
                    print "Great spy" #commenting under nested ifs
                elif 5.5<spy_ratings<=8.0:
                    print "Average spy"
                elif 3.0<spy_ratings<=5.5:
                    print "Bad spy"
                else:
                    print "Are you really a spy?"
                spy_is_online=True
                print "Authentication is completed. Welcome %s of age: %d having ratings %f " % (spy_name,spy_age,spy_ratings)
                start_chat(spy_name,spy_age,spy_ratings) # to provide options to the spy
            else:
                print "Sorry.Your age is not eligible to be a spy."
        else:
            print"Invalid salutation"
    else:
        print "Invalid name. Please enter a valid name"
else:
    print"Invalid entry"