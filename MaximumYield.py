#   MaximumYield.py
#   
#   SOLUTION for problem #6 - Maximum yield
#               by Eugene Berenshteyn
#   Python 3.4.3
#
############################################################################
#   
#  #6 - Maximum yield
#
#You are a Science Engineer on the Federation mining freighter Daedalus. 
#Your team mines strips for a special type of dilithium that is rare 
#and particularly volatile. This has certain implications.
#When your team mines a square in the strip, the trace amounts of 
#dilithium that remain become charged for years. Your team simply cannot 
#mine two squares that are side by side or this would result in an 
#explosion and destroy the planet.
#The ship’s sensors can detect the quantity of dilithium 
#in each square in advance. Your team needs to know the optimal 
#squares it should mine, as well as the total yield from a strip of 
#any size so they can bring it before the captain for final approval.
#Two strip examples:
#[ 206, 140, 300, 52, 107 ] should return 613 units, as mining the first, 
#                           third, and fifth squares is optimal 
#                           [ 206, x, 300, x, 107 ]
#[ 147, 206, 52, 240, 300 ] should return 506 units, as mining the second 
#                           and fifth squares is optimal 
#                           [ x, 206, x, x, 300 ]
############################################################################
#
# Test cases are located next to the bottom of the file
#
############################################################################
#
#   greaterlist: 
#                   input:  two lists of positive integers
#                   output: the list with greater sum of elements
#
def greaterlist(list1, list2):
    """greaterlist: out of 2 input lists, returns the one with greater sum of elements"""
    s1 = sum(list1)
    s2 = sum(list2)
    if s1 > s2:
        return  list1
    else:
        return  list2

#
#   sensor:
#               input: list representing the mine strip (positive integers)
#               output: list of non-adjacent squares to be mined in order to get
#               maximal yield
#
def sensor(land):
    """sensor: return the list of "squares" delivering optimal yield"""
    lenland = len(land)

    if lenland == 1:
        return [land[0]]
    if lenland == 2:
        if (land[0] > land[1]):
            land[1] = 0
        else:
            land[0] = 0

        return land

    alterland1 = []                         # "value - zero - everything else" 
    alterland2 = []                         # "zero - value - zero - everything else"
    
    alterland1.append(land[0])              # - value
    alterland1.append(0)                    # - zero

    firstcallresult = sensor(land[2:])      # there must be at least one 
                                            # element with index greater than 1
    for el in firstcallresult:              
        alterland1.append(el)               # - everything else

    alterland2.append(0)                    # - zero
    alterland2.append(land[1])              # - value
    alterland2.append(0)                    # - zero
    if (len (land[3:]) > 0):                # there may or may not be elements
        secondcallresult = sensor(land[3:]) # with index greater than 2  
        for el in secondcallresult:        
            alterland2.append(el)           # - everything else

    return greaterlist(alterland1,alterland2)


### Two test cases: use one at a time.
#   Uncomment the desired "strip"
#   Comment out another one

## Test case 1
#strip = [ 206, 140, 300, 52, 107 ]

## Test case 2
strip = [ 147, 206, 52, 240, 300 ] 

print ("The strip to evaluate",strip)
optimalsquares = sensor(strip)
profit = sum(optimalsquares)
print ("Profit: ", profit, ", Optimal Squares (zero means \"no digging here\"):\n",14*' ', optimalsquares)


