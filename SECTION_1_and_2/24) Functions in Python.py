def hello(): #creating a callable variable
    print("Hello!")

hello() #calls the variable


#--------------

def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 *24 *60 * 60
    print(f"Your age in seconds is {age_seconds}.")

user_age_in_seconds()

#-----------

#beware
friends = ["Rolf", "Bob"]
# def add_friend():
#     friend_name = input("enter your friends' name")
#     friends = friends + [friend_name] 
#doing this would create a new "friends" variable inside the scope of the function without editing the global variable
friends.append("George")
print(friends)
