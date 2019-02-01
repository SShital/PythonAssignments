import re,time
from seatbooking import SeatBooking
# Business Class
BusinessSeatDetails = SeatBooking(2, 1, 4)

# Economy Class
EconomyClassDetails = SeatBooking(3, 10, 4)
print '** Welcome to Flight booking system **'
while True:
    response = raw_input("Do you want ticket now ? ")
    if re.search('yes|y', response, re.I):
        class_response = raw_input("Select Business/Economy ? ")
        if re.search('business|economy', class_response, re.I):
            preference_response = raw_input("Select Window/Aisle? ")
            if preference_response.lower() == 'window' or preference_response.lower() == 'aisle':
                Passenger_Name = raw_input("Enter your Name: ")
                pAge = input("Enter your Age: ")
                if BusinessSeatDetails.TicketBooking(class_response, preference_response):
                    print "{}, your {}({}) ticket has booked.".format(Passenger_Name, class_response, preference_response)
                else:
                    print "Sorry, No Ticket Available"
                    break
        else:
            print "Please enter valid class.."
            continue
    elif response.lower() == 'n' or response.lower() == 'no':
        print "Thank you for visiting..."
        break
    else:
        continue
