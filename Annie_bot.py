print("Hi! I'm Annie")
name = input("What's your name? ")
print("Hello " + name + "! Nice to meet you.")

#1st convo
feelings = input("How are you doing today? ")
responces = ("I am fine", "I'm Okay", "I'm doing great", "good")
if feelings in responces:
    print("I am glad to hear that!")
else:
    print("oh my!")
    print("Why do you feel this way?")
    reason = input("Please tell me: ")
    print("I understand, life no balance.")

#2nd convo
userage = int(input("How old are you? "))
if userage >= 17 and userage <= 24:
    print("beter pikin")
elif userage >= 25 and userage <= 44:
    print("You don old oo mama")
elif userage > 45:
    print("twale! mama")
else:
    print("Sweet sixteen")

#end convo
print("I enjoyed this class")
print("Reminded me of things I had forgotten.")