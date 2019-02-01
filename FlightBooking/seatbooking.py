import re

class SeatBooking(object):
    def __init__(self, ColumnCount, row_count, seats_per_row):
        self.row_count = row_count
        self.seats_per_row = seats_per_row
        self.seat_count = row_count * seats_per_row
        self.window_seats = row_count * 2
        self.alias_seats = ((ColumnCount*2)-2) * row_count

    Flag = True


    def TicketBooking(self, bookingclass, preferance):
        print bookingclass
        print preferance
        if re.search('business',bookingclass,re.IGNORECASE):
            if re.search('window',preferance,re.IGNORECASE):
                #print self.window_seats
                if self.window_seats > 0:
                    self.window_seats -= 1
                    print self.window_seats
                    return self.Flag
                else:
                    self.Flag = False
                    print "sorry window tickets are not available"
            elif re.search('aisle',preferance,re.IGNORECASE):
                if self.alias_seats > 0:
                    self.alias_seats -= 1
                    return self.Flag
                else:
                    self.Flag = False
                    print "Sorry Alias seats are not availble"
        elif re.search('economy',bookingclass,re.IGNORECASE):
            if re.search('window',preferance,re.IGNORECASE):
                if self.window_seats > 0:
                    self.window_seats -= 1
                    return self.Flag
                else:
                    self.Flag = False
                    print "sorry window tickets are not available"
            elif re.search('aisle',preferance,re.IGNORECASE):
                if self.alias_seats > 0:
                    self.alias_seats -= 1
                    return self.Flag
                else:
                    self.Flag = False
                    print "Sorry Alias seats are not availble"





