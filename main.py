print "Hello spy!!"
print "Let's get started."
spy_name = raw_input("What is your spy name?")
if len(spy_name)>2:
    print "Welcome " + spy_name +". Glad to have you back with us."
    spy_salutation=raw_input("What should we call you (Mr. or Ms.)?")
    if spy_salutation=="Mr." or spy_salutation=="Ms.":
        spy_name=spy_salutation + spy_name
        print "Alright " + spy_name + ". I would like to know a little bit more about you."
        spy_age = input("What is your age?")
        if 60>spy_age>14:
            print "Your age is correct."
            spy_ratings = input("What is your ratings?")
            if spy_ratings>8.0:
                print"Great spy"
            elif 5.5<spy_ratings<=8.0:
                print "Average spy"
            elif 3.0<spy_ratings<=5.5:
                print"Bad spy"
            else:
                print "Are you really a spy?"
            spy_is_online=True
            print "Authentication is completed. Welcome " + spy_name + "age: " + str(spy_age) + " and ratings: " + str(spy_ratings)
        else:
            print "Your age is not eligible to be a spy"

    else:
        print"Invalid salutation"
else:
    print "Oooppppss"