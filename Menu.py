# This class' job is to have a menu that allows users to easyily add items
# to the list of tickets, load files etc..

# Import over Ticket class
from Ticket import Ticket
from TicketManager import TicketManager

class Menu:

    # Ticket manager object
    tManager = None
    
    # Used to tell if changes need to be written
    # to a file
    hasChanged = None


    # Contructor
    def __init__(this):
        tManager = TicketManager()
        hasChanged = False

    def printOptions(this):
        '''
        Prints out all available menu options
        '''
        print("\nPlease select one of the options:")
        print("1. Add raffle ticket")
        print("2. List raffle tickets")
        print("3. Modify raffle ticket")
        print("4. Delete raffle ticket")
        print("5. Load from file")
        print("6. Safe to file")
        print("7. Quit")

    def addTicket(this):
        '''
        Asks the user questions, then fills out a ticket
        '''
        ID = input("\nTicket ID: ")
        name = input("Ticker holder's name: ")
        eMail = input("Ticket holder's eMail: ")

        tManager.addTicket(Ticket(ID, name, eMail))
        hasChanged = True

    def printTickets(this):
        '''
        Goes through and prints all tickets
        '''
        print("\nTickets: ")
        for i in tManager.getTickets():
            print("%s - %s - %s" % (i.getID(), i.getName(), i.getEMail()))

    def modifyTicket(this):
        '''
        Used to allow users to edit a particular ticket
        '''
        ID = input("Please enter ticket ID: ")
        
        # Make sure the ticket exists
        index = tManager.doesExist(ID)

        if (index == None):
            print("The ID you entered isn't in the database!")
            return

        ID = input("Ticket ID: ")
        name = input("Ticket holder's name: ")
        eMail = input("Ticket holder's eMail: ")

        tManager.editTicket(index, ID, name, eMail)
        print("Entry has been edited!")
        hasChanged = True

    def deleteTicket(this):
        '''
        Used to allow users to delete a particular ticket
        '''
        ID = input("Please enter a ticket ID: ")

        if (index == None):
            print("The ID you entered doesn't exist in the databse!")
            return
        


    def handleInput(this, option):
        '''
        Used to handle whatever input the user gives
        '''
        # Make sure option is/can-be a number
        try:
            option = int(option)
        except:
            print("Incorrect input")
            return

        # Now start checking what input is what
        if (option == 1):
            this.addTicket()
        elif (option == 2):
            this.printTickets()
        elif (option == 3):
            this.modifyTicket()
        elif (option == 4):

    def start(this):
        '''
        Simply starts the menu loop
        '''
        # Nice loop for the menu
        while (True):
            # Print out all available options
            this.printOptions()
