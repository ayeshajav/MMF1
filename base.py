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


#''''''''''''Main Routine'''''''''''

#Set up dictionaries / lists need to hold data 

#Ask user if they have used the program before & show instruction if necessary 

#Loop to get ticket details 

  #Get name (can't be blank)
  name = not_blank("Name: ")

  #Get age (betweem 12 and 130)

  #calculate ticket price 

  #Loop to ask for snacks

  #Calculate snack price 

  #Ask for payment method (and apply surcharge if necessary)


#Calculate Total sales and profit 

#Output data to text file 
