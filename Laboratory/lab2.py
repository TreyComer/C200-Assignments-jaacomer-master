import math


def warping(speed):
    """
    Problem Description
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    In the wonderful world of Star Trek, they have a way to travel faster than light. Below is a table of the speed representation. 
    The table is from "The Star Trek Encyclopedia: A Reference Guide to the Future. Updated and Expanded Edition" by Michael Okuda 
    and Denise Okuda.
    Speed                   |    Number of times speed of light (Number represents lower bound)
    Sublight(Warp Factor 0) |    0
    Warp Factor 1           |    1
    Warp Factor 2           |    10
    Warp Factor 3           |    39
    Warp Factor 4           |    102
    Warp Factor 5           |    214
    Warp Factor 6           |    392
    Warp Factor 7           |    656
    Warp Factor 8           |    1,024
    Warp Factor 9           |    1,516
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Input: A float or number
    Returns: A number representing the warp factor
    """
    if speed < 1:
        return 0

    elif speed < 2:
        return 1
    
    elif speed < 3:
        return 10
    
    elif speed < 4:
        return 39
    
    elif speed < 5:
        return 102

    elif speed < 6:
        return 214
    
    elif speed < 7:
        return 392
    
    elif speed < 8:
        return 1024

    elif speed <= 9
        return 1,516
    pass

def driving_time(miles,speed):
    """
    Finds the amount of time (hours) it takes to drive a given number of miles at a given speed (mph)

    Inputs: miles (int), speed (int)
    Returns: time (int in hours)
    """

    return miles/speed
    



    

def driving_speed(miles,time):
    """
    Finds the speed (mph) it takes to drive a given number of miles in a given time (hours)


    Inputs: miles (int), time (int)
    Returns: speed (int in mph)
    """
    return miles*time



def driving_distance(speed,time):
    """
    Finds the distance (miles) driven in a given time (hours) at a given speed (mph)


    Inputs: speed (int), time (int)
    Returns: miles (int)
    """

   return speed/time



def race(a_miles,a_speed,b_miles,b_speed):
    """
    Finds the who will reach their destination first (a or b)


    Inputs: a_miles (miles), a_speed (mph), b_miles (miles), b_speed (mph)
    Returns: 0 if player A arrives first, 1 if player B arrives first, -1 if equal
    """

    if a_miles*a_speed > b_miles*b_speed:
        return 0

    if a_miles*a_speed < b_miles*b_speed:
        return 1

    if a_miles*a_speed = b_miles*b_speed:
        return -1

    

def most_distance(a_time,a_speed,b_time,b_speed):
    """
    Finds the who will drive the farthest (a or b)


    Inputs: a_time (hours), a_speed (mph), b_miles (hours), b_speed (mph)
    Returns: 0 if player A drives the farthest, 1 if player B drives the farthest, -1 if equal
    """
    if a_speed/a_time > b_speed/b_time:
        return 0

    if a_speed/a_time < b_speed/b_time:
        return 1
    
    if a_speed/a_time = b_speed/b_time:
        return -1

    

def most_speed(a_miles,a_time,b_miles,b_time):
    """
    Finds the who will drive the fastest (a or b)


    Inputs: a_miles (miles), a_time (hours), b_miles (miles), b_time (hours)
    Returns: 0 if player A drives the fastest, 1 if player B drives the fastest, -1 if equal
    """

    if a_miles*a_time > b_miles*b_time:
        return 0

    if a_miles*a_time < b_miles*b_time:
        return 1

    if a_miles*a_times = b_miles*b_time:
        return -1
    

def whichAssingmentToWorkOn(assingment1,assingment2,assingment3):
    """
    I'm an unmotivated student and need help determining which homework assingment
    I should do next. The function is given a list of THREE classes and how many days
    until the next assingment is due. I want to work on the class which has the assingment due
    next. Write a function which tells me what class I should work on next


    """
    

    pass

def didIMakeHonorRoll(gpa,creditHours,lowestGrade):
    """
    To make the honor roll at Greendale Community College you have to fufill 3 criteria
    - A gpa greater than 3.7
    - A minimum of 12 credit hours
    - The lowest grade you can get is a B-
    given a list with the students gpa, the number of credit hours they took and the lowest grade they got
    return wether or not the are on the honor roll"""
    
    if gpa >= 3.7
        return print("You did not make Honor role")
    else:
        print("You made Honor role")
    if creditHours <= 12
        return print("You did not make Honor role")
    else: 
        print("You made Honor role")
    
    if lowest Grade >= A+,A,A-,B+,B,B-
        return print("You did not make Honor role")
    else:
        print("you made Honor role")
    pass

def gradeToGetAnA(currentGrade,weightOfFinal):
    """
    Everybody wants to know what grade they need on a final to get an A in the course
    To calculate this you will need to use the weighted sum of how you did so far plus
    the minimum score needed to get a 93% in the class. Given what your grade currently is
    and what percentage of your grade the final is worth, find the minimum score needed for an A
    (It should be in probability terms so 100% would be 1. 50% would be .5, 25% would be .25 etc"""
    
    if currentGrade*weightOfFinal >= 93%
        return 
    
    pass


def squarea(l,w):
    """
    Implement a function to find the area of a square

    Input: 2 numbers
    Returns: Number
    """

    sum squarea(1,w):
        return sum

    pass

def midlist(list1):
    """
    Implement a function that finds the middle of the list and outputs it
    An example is: for [1,2,3,4,5,6,7] it would output 4
                   for [1,2,3,4,5,6] it would output 4 

    DO NOT use a for loop

    Helper Function:
    - https://docs.python.org/3/library/functions.html#len 
    """
    pass

def twenty_four_twelve(hour,am_pm):
    """
    Implement a function to convert from 24-hour time to 12-hour time
    Example: twenty_four_twelve(8,'pm') -> 16
             twenty_four_twelve(10,'am') -> 10
    Input: hour (int), am_pm (str, "am" or "pm")
    Returns: hour in 24-hour time (int)
    """
    pass


def speed(d, t):
    """
    Calculates speed from distance and time
    INPUT distance d, time t
    OUTPUT speed 
    """
    # TODO: Implement function
    pass

def distance (s, t):
    """
    Finds distance using speed and time
    INPUT speed s, time t
    OUTPUT distance
    """
    # TODO: Implement function
    pass


def time (s, d):
    """
    Finds time using speed and distance
    INPUT speed s, distance d
    OUTPUT time
    """
    # TODO: Implement function
    pass

def hours_to_min(hours):
    """
    Converts hours to minutes
    INPUT hours hours
    OUTPUT minutes
    """
    # TODO: Implement function
    pass

def min_to_sec(min):
    """
    Converts minutes to seconds
    INPUT minutes min
    OUTPUT seconds
    """
    # TODO: Implement function
    pass


def feet_to_mile(feet):
    """
    Converts feet to miles
    INPUT feet feet
    OUTPUT miles
    """
    # TODO: Implement function
    pass

def miles_to_kilometers(miles):
    """
    Converts miles to kilometers
    INPUT miles miles
    OUTPUT kilometers
    """
    # TODO: Implement function
    pass

def k_to_m(k):
    """
    Converts kilometers to miles
    INPUT kilometers k
    OUTPUT miles 
    """
    # TODO: Implement function
    pass

def miles_to_feet(miles):
    """
    Converts miles to feet
    INPUT miles miles
    OUTPUT feet
    """
    # TODO: Implement function
    pass

def degrees_to_radians(degrees):
    """
    Converts degrees to radians
    INPUT degrees degrees
    OUTPUT radians
    """
    # TODO: Implement function
    pass

def loc_c(a,b,gamma):
    """
    Finds the length of side c of a triangle (Law of Cosines)
    where gamma is degrees and is converted to radians
    INPUT side length a, side length b, degree angle gamma
    """
    # TODO: Implement function
    pass

def c_to_f(celcius):
    """
    Convert celcius to fahrenheit 
    INPUT celcius c
    OUTPUT fahrenheit
    """
    # TODO: Implement function
    pass

def f_to_c(fahrenheit):
    """
    Converts fahrenheit to celcius
    INPUT farhenheit fahrenheit
    """
    # TODO: Implement function
    pass

def k_to_f(kelvin):
    """
    Converts fahrenheit to kelvin
    INPUT kelvin kelvin
    OUTPUT fahrenheit
    """
    # TODO: Implement function
    pass


def pc(p,d):
    """
    Given a stock price p and amount change +/- d, 
    calculate the percentage difference
    INPUT stock price p, dollar amount change v
    OUTPUT percent change
    """
    # TODO: Implement function
    pass

def p_to_k(parsecs):
    """
    Convert parsecs to kilometers
    INPUT parsecs p
    OUTPUT kilometers
    """
    # TODO: Implement function
    pass

def ly_to_p(lightyear):
    """
    Convert light years to parsecs
    INPUT light years ly
    OUTPUT parsecs
    """
    # TODO: Implement function
    pass

