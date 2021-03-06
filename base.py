#import statments 


#functions go here 

#checks that ticket name is not blank 
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        #If name is no blank, program continues
        if response != "": 
            return response 

        #If name is blank, show error (& repeat loop)
        else:
            print ("Sorry - this can't be blank, "
                  "please enter your name")


#checks for an integer more than 0 
def int_check(question):

    error = "Please enter a whole number between {} " \
            "and {}". format(low_num, high_num)

    valid = False 
    while not valid:

        #ask user for number and check it is valid  
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
              return response 
              
#main rountine goes here           
#''''''''''''Main Routine'''''''''''

#Set up dictionaries / lists need to hold data 

#Ask user if they have used the program before & show instruction if necessary 

#Loop to get ticket details 

#start of loop 

#initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5 

while name != "xxx" and count < MAX_TICKETS:  

    #tells user how many seats are left
    if count < 4: 
        print("You have {} seats "
              "left".format(MAX_TICKETS - count))

    #warns user that only one seat is left!
    else: 
        print("*** There is ONE seat left!! ***")
    #Get details...

    #Get name (can't be blank)
    name = not_blank("Name: ")

    #end the loop if the exit code is entered 
    if name == "xxx":
        break    

    #Get age (betweem 12 and 130)
    age = int_check("Age: ")


    #check that age is valid...
    if age < 12:
        print("Sorry you are too young for this movie")
        continue
    elif age > 130:
        print("That is very old - it looks like a mistake")
        continue

    
  count += 1 
      
#end of ticket loop

#calculate profit etc...
if count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets.  \n"
          "There are {} places still available"
          .format(count, MAX_TICKETS - count))
          
  
  #Get age (betweem 12 and 130)

  #calculate ticket price 

  #Loop to ask for snacks

  #Calculate snack price 

  #Ask for payment method (and apply surcharge if necessary)


#Calculate Total sales and profit 

#Output data to text file 
