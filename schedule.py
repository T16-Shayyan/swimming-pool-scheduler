

def save_bookings(book_lst, file_name):
    count = 0
    f = open(file_name, 'w')            #opening file for writing
    for items in book_lst:
        temp_str = ''
        for i in range(len(items)):
            temp_str += (str(items[i]) + ':')
            count += 1
        temp_str += '\n'        #adding a next line
        f.write(temp_str)

    return count

def load_lines(file_name):
    try:
        f = open(file_name,'r')
        return f.readlines()            #reading the whole file
    except FileNotFoundError:           #if file does not exist
        return f'The file {file_name} could not be found'


def split_lines(booking_lines):
    output_list = []
    int_things_index = [1,2,4,5]
    for item in booking_lines:
        temp_list = item.split(':')             #splitting string by ':'
        temp_list = temp_list[:-1]              #removing \n
        for i in range(len(temp_list)):
            if i in int_things_index or i >= 7:
                try:
                    temp_list[i] = int(temp_list[i])        #trying if converts to int
                except:
                    return f'An int was expected instead of {temp_list[i]}'     #if cannot then return this
        output_list.append(temp_list)
    return output_list

def check_schedule(booking_items, num_lanes):
    hour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    minute = [0, 15, 30, 45]
    time = ['AM', 'PM']

    for item in booking_items:
        if len(item[0]) < 3:        #checking fo F1
            raise ValueError
        if item[1] not in hour or item[4] not in hour:          #checking fo F2
            raise ValueError
        if item[2] not in minute or item[5] not in minute:      #checking fo F3
            raise ValueError
        if item[3] not in time or item[6] not in time:          #checking fo F4
            raise ValueError
        for i in range(7,len(item)):
            if not(item[i] > 0 and item[i] < num_lanes):        #checking fo F5
                raise ValueError



def make_schedule(booking_items, num_lanes):
    schedule = [['~~~' for l in range(num_lanes)] for m in range(10 * 4)]    #making a 2d list for lanes
    if num_lanes == 0:
        string_schedule = "LANES    " + "   ".join(str(i) for i in range(1, num_lanes + 1)) + "\n"
    else:
        string_schedule = "LANES     " + "   ".join(str(i) for i in range(1, num_lanes + 1)) + "  \n"   #making a string for later use

    add_index = []
    for i in range(len(booking_items)):    #looping around the list to add names on booked lanes
        mini_list = []
        start_hr = 7
        start_min = 0
        add = False
        for j in range(40):
            if booking_items[i][1] == start_hr:
                if booking_items[i][2] == start_min:
                    add = True

            if booking_items[i][4] == start_hr:
                if booking_items[i][5] == start_min:
                    add = False

            if start_hr == 12 and start_min == 45:
                start_hr = 1
                start_min = 0
            else:
                start_min += 15
                if start_min == 60:
                    start_min = 0
                    start_hr += 1

            if add is True:
                for x in range(7,len(booking_items[i])):
                    schedule[j][booking_items[i][x]-1] = booking_items[i][0][:3]
                mini_list.append(j)
        add_index.append(mini_list)

    start_hr = 7
    start_min = 0
    add_min = ''
    add_hour = ''
    time = ' AM '
    for g in range(40):         #making a multi line string using the list
        if start_min == 0:
            add_min = '00'
        else:
            add_min = str(start_min)

        if start_hr < 10:
            add_hour = '0' + str(start_hr)
        else:
            add_hour = str(start_hr)

        if num_lanes == 0:
            string_schedule += add_hour + ':' + add_min + time + ' '.join(schedule[g]) + '\n'
        else:
            string_schedule += add_hour + ':' + add_min + time + ' '.join(schedule[g]) + ' \n'

        if start_hr == 12 and start_min == 45:          #increment of min hour or changing am to pm
            start_hr = 1
            start_min = 0
        else:
            start_min += 15
            if start_min == 60:
                start_min = 0
                start_hr += 1

        if start_hr == 12 and start_min == 0:
            time = " PM "

    return string_schedule



'''
    total =[]

    start_hr = 7
    start_min = 0
    time = ' AM '
    add = False

    while start_hr <= 4 or start_min <= 45 or time == 'AM':
        temp_list = []
        if start_hr < 10:
            temp = '0'+str(start_hr)
            temp_list.append(temp)
        else:
            temp_list.append(start_hr)

        temp_list.append(':')
        if start_min == 0:
            temp_list.append('00')
        else:
            temp_list.append(start_min)

        if start_hr == 12 :
            time = ' PM '
        temp_list.append(time)

        if booking_items[0][2] >= start_min:
            if booking_items[0][1] >= start_hr:
                add = True

        if booking_items[0][5] < start_min:
            if booking_items[0][4] <= start_hr:
                add = False

        list_of_lanes = []
        for i in range(7,len(booking_items)):
            list_of_lanes.append(booking_items[i])

        for i in range(num_lanes):
            temp_list.append('~~~')

        if add == True:
            for index in list_of_lanes:
                temp_list[index+3] = booking_items[0][:3].upper

        temp_list[-1] += '\n'


        if start_hr == 12 and start_min == 45:
            start_hr = 1
            start_min = 0
        else:
            start_min += 15
            if start_min == 60:
                start_min = 0
                start_hr += 1

        total.append(temp_list)
'''



'''
print(save_bookings( [['CS 112 Lab', 9, 15, 'AM', 10, 45, 'AM', 2, 3],
['MECH Class', 11, 0, 'AM', 12, 0, 'PM', 2, 3],
['STAT Swimmers', 7, 0, 'AM', 4, 45, 'PM', 1]],
'another_bookings_file.txt' ))

print(split_lines( ['CS 112 Lab:9:15:AM:10:45:AM:2:3:',
'MECH Class:11:0:AM:12:0:PM:2:3:',
'STAT Swimmers:7:0:AM:4:45:PM:1:'] ))

print(check_schedule( [['CS 112 Lab', 9, 15, 'AM', 10, 45, 'AM', 2, 3],
['MECH Class', 11, 0, 'AM', 12, 0, 'PM', 2, 3],
['STAT Swimmers', 7, 0, 'AM', 4, 45, 'PM', 1]] , 5 ))

check_schedule( [['abc', 9, 15, 'AM', 10, 45, 'AM', 2, 3],
['def', 11, 0, 'AM', 12, 0, 'PM', 2, 3],
['gh', 7, 0, 'AM', 4, 45, 'PM', 1]] , 5 )

check_schedule( [['abc', 9, 15, 'AM', 10, 45, 'AM', 2, 3],
['def', 11, 60, 'AM', 12, 0, 'PM', 2, 3]] , 5 )

'''

thing = make_schedule( [['CS 112 Lab', 9, 15, 'AM', 10, 45, 'AM', 2, 3],
['MECH Class', 11, 0, 'AM', 12, 0, 'PM', 2, 3],
['STAT Swimmers', 7, 0, 'AM', 4, 45, 'PM', 1]], 3)

print( make_schedule([['Hii',7,0,'AM',3,0,'PM',2,3]],4))
print(thing)

print(make_schedule([['CSHawks', 7, 30, 'AM', 8, 30, 'AM', 1, 5, 6]], 9))

print(make_schedule([], 0))

