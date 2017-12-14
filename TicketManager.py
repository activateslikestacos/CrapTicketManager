# This file holds a class that holds all our tickets in memory
# for easy access.

# Import ticket class
from Ticket import Ticket

class TicketManager:
    
    # Our list of tickets
    tickets = None

    # Constructor
    def __init__(this):
        this.tickets = []

    # Accessors and modifers
    def addTicket(this, ticket):
        this.tickets.append(ticket)

    def getTicket(this, i):
        return this.tickets[i]

    def getTickets(this):
        return this.tickets

    def doesExist(this, ID):
        for i in tickets:
            if (i.getID() == ID):
                return i
        return None

    def editTicket(this, i, ID, name, eMail):
        if (i >= len(tickets)):
            return

        tickets[i] = Ticket(ID, name, eMail)

    def deleteTicket(this, i):
        # TODO
