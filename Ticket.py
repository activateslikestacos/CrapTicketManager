# Simply put, this class will hold each "raffle" ticket and the information
# tied to it. It will help keep track of who won what ticket

class Ticket:

    # ID/Number of the ticket
    ID = None
    # Name of the ticket holder
    name = None
    # E-Mail of the ticket holder
    eMail = None

    # Constructor
    def __init__(this, ID, name, eMail):
        this.ID = ID
        this.name = name
        this.eMail = eMail
    
    # Accessors and modifiers
    def getID(this):
        return this.ID

    def getName(this):
        return this.name

    def getEMail(this):
        return this.eMail
    
    def setID(this, ID):
        this.ID = ID

    def setName(this, name):
        this.name = name

    def seteMail(this, eMail):
        this.eMail = eMail

    # End of Ticket class
