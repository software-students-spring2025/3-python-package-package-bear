import time
happiness = 0
hunger = 0
cleanliness = 0
budget = 100
name = "Bear"
initialized = False
food = 0

# need variables for timer/ clock


# - We might need to create a quit function 
#   that saves the data to a local DB to save progress
# - Restart/ die funtion
# ^^^^ OPTIONAL IMPLEMENTATION

# ******** Alex
# This function sets up the inital pet
# and starts the clock/ timing for
# hunger, cleanliness, and happiness to go down
# Also show initial startup diaglogue & instructions
# Something like : Hi! I'm Bear! Nice to meet you!
# Feed me to keep me happy! Work a job to earn money!... etc
# MOST IMPORTANT DIRECTION:
# TELL USER TO USE check_status after using play to check on pet
# play is only the initializer!!!!
# !!!! SET INITIALIZED TO TRUE AFTER!!!
# !!!!! MIGHT NEED TO CHANGE THIS LATER IN MAIN WHEN RUN/ PACKAGE AND NOT AS A FUNCTION!!!!!
def play():
    global happiness, hunger, cleanliness, initialized
    initialized = True
    happiness = 100
    hunger = 100
    cleanliness = 100
    print("Hi! I'm Bear! Nice to meet you!")
    print("Feed me to keep me happy! Work a job to earn money!")
    print("Use check_status to check my current happiness, hunger, and cleanliness!")
    while initialized:
        time.sleep(100)
        update_happiness()
        update_cleanliness()
        update_hunger()



# ******** Jasmine
# This function prints out the current status of the pet
# along with the correct emoticons
# THIS FUNCTION CAN ONLY RUN IF PLAY() IS CALLED
# (INITIALIZED == TRUE)
# IF NOT INIT, PRINT DIRECTION TO CALL PLAY()
def check_status():
    pass

# ******** Jasmine
# This function uses the clock/ timer to update the 
# hunger, happiness, and cleanliness over time
# THIS FUNCTION CAN ONLY RUN IF PLAY() IS CALLED
# (INITIALIZED == TRUE)
# IF NOT INIT, PRINT DIRECTION TO CALL PLAY()
def update_status():
    pass

# ******** Sophia
# This function allows the user to change the name of the pet
# THIS FUNCTION CAN ONLY RUN IF PLAY() IS CALLED
# (INITIALIZED == TRUE)
# IF NOT INIT, PRINT DIRECTION TO CALL PLAY()
def change_name():
   if initialized:
        name = input("Enter a new name for your pet!")
   else:
        print("Make sure to use play() to set up the bear!")
        return

    

# ******** Alex
# This function uses the timer/ clock to periodically update the happiness
# THIS FUNCTION CAN ONLY RUN IF PLAY() IS CALLED
# (INITIALIZED == TRUE)
# IF NOT INIT, PRINT DIRECTION TO CALL PLAY()
def update_happiness():
    global initialized, happiness
    if not initialized:
        print("Make sure to use play() to set up the bear!")
        return
    while initialized and happiness > 0:
        time.sleep(100)
        happiness -= 1

# ******** Tadelin
# This function uses the timer/ clock to periodically update the cleanliness
# THIS FUNCTION CAN ONLY RUN IF PLAY() IS CALLED
# (INITIALIZED == TRUE)
# IF NOT INIT, PRINT DIRECTION TO CALL PLAY()
def update_cleanliness():
    pass

# ******** Tadelin
# This function uses the timer/ clock to periodically update the hunger
# THIS FUNCTION CAN ONLY RUN IF PLAY() IS CALLED
# (INITIALIZED == TRUE)
# IF NOT INIT, PRINT DIRECTION TO CALL PLAY()
def update_hunger():
    pass

# ******** Sophia
# This function takes a certain int of hours to work
# $16/ hour (or how many you want)
# Updates budget!!
# THIS FUNCTION CAN ONLY RUN IF PLAY() IS CALLED
# (INITIALIZED == TRUE)
# IF NOT INIT, PRINT DIRECTION TO CALL PLAY()
def work(hours: int):
    if initialized:
        budget = budget + (hours*16)
    else:
        print("Make sure to use play() to set up the bear!")
        return
    

# ******** Sophia
# This function allows the user to buy food for a set int amount
# THIS FUNCTION CAN ONLY RUN IF PLAY() IS CALLED
# (INITIALIZED == TRUE)
# IF NOT INIT, PRINT DIRECTION TO CALL PLAY()
def buy_food(amount: int):
    if initialized:
        #for now, food costs $1
        cost = 1
        food = food+amount
        budget = budget - (amount*cost)
    else:
        print("Make sure to use play() to set up the bear!")
        return

