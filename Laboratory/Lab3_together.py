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

    elif speed <= 9:
        return 1,516


def driving_time(miles,speed):
    """
    Finds the amount of time (hours) it takes to drive a given number of miles at a given speed (mph)
    Inputs: miles (int), speed (int)
    Returns: time (int in hours)
    """
    t=miles/speed
    return t

def race(a_miles,a_speed,b_miles,b_speed):
    """
    Finds the who will reach their destination first (a or b)
    Inputs: a_miles (miles), a_speed (mph), b_miles (miles), b_speed (mph)
    Returns: 0 if player A arrives first, 1 if player B arrives first, -1 if equal
    """
    if driving_time(a_miles, a_speed) < driving_time(b_miles, b_speed):
        return 0
    elif driving_time(a_miles, a_speed) > driving_time(b_miles, b_speed):
        return 1
    else:
        return -1


def countLetters(letters, theLetter):
    """
    Given a string of letters and the letter you are looking for, return the number of times that happens.
    """
    result = 0
    for singleLetter in letters:
        if theLetter == singleLetter:
            result += 1
    return result

def countLetters2(letters, theLetter):
    """
    Given a string of letters and the letter you are looking for, return the number of times that happens.
    """
    result = 0
    for index in range(len(letters)):
        singleLetter = letters[index]
        if theLetter == singleLetter:
            result += 1
    return result


def myTestString(func, params):
    return func.__name__ + "" + str(params) + " produces " + str(func(*params))

# For more information about the line below, refer to the link: https://docs.python.org/3/library/__main__.html
#   You can read more about it but it is to help when handling multiple files
#   Will be dicussed at a later point
if __name__ == "__main__":
    print("Final Test Code\n")
    print("Testing warping()")
    for x in [(0,), (41.0,),(10.2,), (1111,)]:
        print(myTestString(warping, x))
    
    print()
    print("Testing race()")
    for x in [(5,50,6,60,),(5,25,4,60,)]:
        print(myTestString(race, x))
    
    print()
    print("testing countLetters()")
    testing = [("aaabbbaaacccdddifkf;lkajsdf;lkjA", "b"), ("The quick brown fox jumped very lazily over the green short worm", "i")]
    for x in testing:
        print(myTestString(countLetters, x))
    
    print()
    print("testing countLetters2()")
    testing = [("aaabbbaaacccdddifkf;lkajsdf;lkjA", "b"), ("The quick brown fox jumped very lazily over the green short worm", "i")]
    for x in testing:
        print(myTestString(countLetters2, x))