print("*"*30)
TITLE = "TICKET DETAILS"
print(TITLE)
print("*"*30)

import datetime
from datetime import timedelta
x=datetime.datetime.now()
y=timedelta(hours=3)
Ticket=("A01",("Nairobi", ("37E","3S")),
        ("Kigali",("34E","1S")),x ,x +y)
# print(f"Flight number:",Ticket [0],
#       "\nDeparting from:", Ticket[1],"at", Ticket[3],
#       "\nArriving at:", Ticket[2], "at", Ticket[4])
Ticket_Number, Departure_city, Destination, Departure_time, Arrival_time=Ticket
# print("Passenger's ticket number:", Ticket_Number)
# print("Passenger's City of origin and coordinates:", Departure_city)
# print("Passenger's time and date of departure:", Departure_time)
# print("Passenger's destination and coordinates:", Destination)
# print("Passenger's time and date of arrival:", Arrival_time)

while True:
    print("1.Ticket Number")
    print("2.City of Origin")
    print("3.Time and Date of Departure")
    print("4.Destination")
    print("5.Time and Date of Arrival")
    print("6.Ticket Details")
    print("7.Exit Ticket Details")

    option = input("Please enter your choice (1-7):")
    # option = int(option)

    if option == "1":
        print(f"Ticket Number: {Ticket_Number}")
    elif option == "2":
        print(f"City of Origin: {Departure_city}")
    elif option == "3":
        print(f"Time and Date of Departure: {Departure_time}")
    elif option == "4":
        print(f"Destination: {Destination}")
    elif option == "5":
        print(f"Time and Date of Arrival: {Arrival_time}")
    elif option == "6":
        print("!!Complete Ticket Details!!")
        print("#"* 30)
        print(f"Ticket Number: {Ticket_Number}")
        print(f"City of Origin: {Departure_city}")
        print(f"Time and Date of Departure: {Departure_time}")
        print(f"Destination: {Destination}")
        print(f"Time and Date of Arrival: {Arrival_time}")
        print("#"*30)
    elif option == "7":  
        print("Exiting Ticket Details") 
        break
    else:
        print("Enter a Valid Number!!!")
    print("/"*40)    