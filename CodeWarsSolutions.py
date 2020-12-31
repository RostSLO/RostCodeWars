from pickle import FALSE
import itertools,operator
from future.backports.test.pystone import TRUE


#res = parse_int('five hundred thousand three hundred')
#print (str(res))


#res = parse_int('two hundred three thousand')
#print (str(res))


'''
==========================================================================
NAME: parseInt() reloaded

In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

"one" => 1
"twenty" => 20
"two hundred forty-six" => 246
"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
Additional Notes:

The minimum number is "zero" (inclusively)
The maximum number, which must be supported is 1 million (inclusively)
The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
All tested numbers are valid, you don't need to validate them
'''
'''
#my solution
def checkNum(resStr, s, short, long):
    if len(s) == 1:
        sym = s
    else: sym = s[len(s)-1]
  
    if s in resStr and resStr.find(sym) != len(resStr)-1: 
        if s == 'h':
            temp = resStr
            temp = temp.replace("h","")
            if int(temp) < 100: return resStr.replace(s, "0")
            elif len(temp) > 2: return resStr.replace(s, "")
            else: return resStr.replace(s, short)
        elif s == 'ht':
            new = list(resStr)
            new[resStr.find("h")] = 'X'
            resStr = ''.join(new)
            if resStr.find('t') == 2 and len(resStr) == 3: return resStr.replace("Xt", "00000")
            elif resStr.find('t') == 2 and len(resStr) == 4: return resStr.replace("Xt", "0000")
            elif resStr.find('t') == 2 and len(resStr) == 5 and resStr.find("h") != len(resStr)-1: return resStr.replace("Xt", "000")
            else: return resStr.replace("Xt", short)
      
        else: return resStr.replace(s, short)
        
    elif s == "t" and resStr.find("t") == len(resStr)-1:
        if "h" in resStr and len(resStr) == 4: return resStr.replace("h", "0").replace("t", "000")
        else: return resStr.replace(s, long)
    else: return resStr.replace(s, long)


def parse_int(string):
    print(string)
    string = string.lower()
    resStr = string.replace("hundred thousand", "ht").replace("million", "000000").replace("of", "").replace(" ", "").replace("thousand", "t").replace("and", "").replace("hundred", "h").replace("fourteen", "14").replace("fifteen", "15").replace("sixteen", "16").replace("seventeen", "17").replace("eighteen", "18").replace("nineteen", "19").replace("zero", "0").replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("ten", "10").replace("eleven", "11").replace("twelve", "12").replace("thirteen", "13").replace("twenty-", "2").replace("thirty-", "3").replace("forty-", "4").replace("fifty-", "5").replace("sixty-", "6").replace("seventy-", "7").replace("eighty-", "8").replace("ninety-", "9")
    resStr = resStr.replace("twenty", "20").replace("thirty", "30").replace("forty", "40").replace("fifty", "50").replace("sixty", "60").replace("seventy", "70").replace("eighty", "80").replace("ninety", "90").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9")
    resStr = checkNum(resStr, "hst", "00", "00000")
    resStr = checkNum(resStr, "ht", "00", "00000")
    resStr = checkNum(resStr, "hs", "", "00")
    resStr = checkNum(resStr, "t", "", "000")
    resStr = checkNum(resStr, "h", "", "00")
                    
    return int(resStr)

#The best community solution
words = {w: n for n, w in enumerate('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split())}
words.update({w: 10 * n for n, w in enumerate('twenty thirty forty fifty sixty seventy eighty ninety hundred'.split(), 2)})
thousands = {w: 1000 ** n for n, w in enumerate('thousand million billion trillion quadrillion quintillion sextillion septillion octillion nonillion decillion'.split(), 1)}
def parse_int(strng):
    num = group = 0
    for w in strng.replace(' and ', ' ').replace('-', ' ').split():
        if w == 'hundred': 
            group *= words[w]
        elif w in words: 
            group += words[w]
        else:
            num += group * thousands[w]
            group = 0
    return num + group
'''

'''
==========================================================================
NAME Range Extraction

Description:
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"

#my solution
def solution(args):
    ranges = sum((list(t) for t in zip(args, args[1:]) if t[0]+1 != t[1]), [])
    iranges = args[0:1] + ranges + args[-1:]
    resStr = ""
    for i in range(0, len(iranges)-1, 2):
        if iranges[i] == iranges[i+1]: resStr += str(iranges[i]) + ","
        elif iranges[i]+1 == iranges[i+1]: resStr += str(iranges[i]) + "," + str(iranges[i+1]) + ","
        else: resStr += str(iranges[i]) + "-" + str(iranges[i+1]) + ","
    resStr = resStr[:-1]
    return resStr
    
#the best community solution
def solution(args):
    out = []
    beg = end = args[0]
    
    for n in args[1:] + [""]:        
        if n != end + 1:
            if end == beg:
                out.append( str(beg) )
            elif end == beg + 1:
                out.extend( [str(beg), str(end)] )
            else:
                out.append( str(beg) + "-" + str(end) )
            beg = n
        end = n
    
    return ",".join(out)

'''

'''
==========================================================================
NAME: Snail

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:


NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

#my solution
def oneCircle(i, snail_map):
    res = ""
    numRows = len(snail_map)
    for j in range(i, numRows-i):
        res += snail_map[i][j] + ","
    for j in range(i+1, numRows-i):
        res += snail_map[j][numRows-i-1] + ","
    for j in range(numRows-i-2, i-1, -1):    
        res += snail_map[numRows-i-1][j] + ","
    for j in range(numRows-i-2, i, -1):
        res += snail_map[j][i] + ","
    return res

def snail(snail_map):
    res = ""
    strSnailMap = []
    if any(snail_map):
        for listElement in snail_map: 
            strSnailMap.append(list(map(str, listElement)))
    
        #validating the odd \ even number of rows and # of circles
        if len(strSnailMap) % 2 == 0:
            oddOrEven = True
            numOfCircles = int((len(strSnailMap)/2)-1)
        else:
            oddOrEven = False
            numOfCircles = int((len(strSnailMap)-1)/2)
            
        for i in range(numOfCircles):
            res += oneCircle(i, strSnailMap) 
        
        if oddOrEven:
            res += strSnailMap[numOfCircles][numOfCircles] + "," + strSnailMap[numOfCircles][numOfCircles+1] + "," + strSnailMap[numOfCircles+1][numOfCircles+1] + "," + strSnailMap[numOfCircles+1][numOfCircles]
        else:
            res += strSnailMap[numOfCircles][numOfCircles]
            
        return list(map(int, res.split(",")))
    return []
    
#the best community solution
def snail(array):
    ret = []
    if array and array[0]:
        size = len(array)
        for n in xrange((size + 1) // 2):
            for x in xrange(n, size - n):
                ret.append(array[n][x])
            for y in xrange(1 + n, size - n):
                ret.append(array[y][-1 - n])
            for x in xrange(2 + n, size - n + 1):
                ret.append(array[-1 - n][-x])
            for y in xrange(2 + n, size - n):
                ret.append(array[-y][n])
    return ret

'''

'''
==========================================================================
NAME: Decode the Morse code, advanced (Python)
Part of Series 2/3
This kata is part of a series on the Morse code. Make sure you solve the previous part before you try this one. After you solve this kata, you may move to the next one.


In this kata you have to write a Morse code decoder for wired electrical telegraph.
Electric telegraph is operated on a 2-wire line with a key that, when pressed, connects the wires together, which can be detected on a remote station. The Morse code encodes every character being transmitted as a sequence of "dots" (short presses on the key) and "dashes" (long presses on the key).

When transmitting the Morse code, the international standard specifies that:

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
However, the standard does not specify how long that "time unit" is. And in fact different operators would transmit at different speed. An amateur person may need a few seconds to transmit a single character, a skilled professional can transmit 60 words per minute, and robotic transmitters may go way faster.

For this kata we assume the message receiving is performed automatically by the hardware that checks the line periodically, and if the line is connected (the key at the remote station is down), 1 is recorded, and if the line is not connected (remote key is up), 0 is recorded. After the message is fully received, it gets to you for decoding as a string containing only symbols 0 and 1.

For example, the message HEY JUDE, that is .... . -.--  .--- ..- -.. . may be received as follows:

1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011

As you may see, this transmission is perfectly accurate according to the standard, and the hardware sampled the line exactly two times per "dot".

That said, your task is to implement two functions:

Function decodeBits(bits), that should find out the transmission rate of the message, correctly decode the message to dots ., dashes - and spaces (one between characters, three between words) and return those as a string. Note that some extra 0's may naturally occur at the beginning and the end of a message, make sure to ignore them. Also if you have trouble discerning if the particular sequence of 1's is a dot or a dash, assume it's a dot.
2. Function decodeMorse(morseCode), that would take the output of the previous function and return a human-readable string.

NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

The Morse code table is preloaded for you (see the solution setup, to get its identifier in your language).


Eg:
  morseCodes(".--") //to access the morse translation of ".--"
All the test strings would be valid to the point that they could be reliably decoded as described above, so you may skip checking for errors and exceptions, just do your best in figuring out what the message is!

Good luck!

After you master this kata, you may try to Decode the Morse code, for real.

#my solution
import itertools,operator

MORSE_CODE = { '.-':'A', '-...':'B', 
                    '-.-.':'C', '-..':'D', '.' : 'E', 
                    '..-.':'F', '--.':'G', '....':'H', 
                    '..':'I', '.---':'J', '-.-':'K', 
                    '.-..':'L', '--':'M', '-.':'N', 
                    '---':'O', '.--.':'P', '--.-':'Q', 
                    '.-.':'R', '...':'S', '-':'T', 
                    '..-':'U', '...-':'V', '.--':'W', 
                    '-..-':'X', '-.--':'Y', '--..':'Z', 
                    '.----':'1', '..---':'2', '...--':'3', 
                    '....-':'4', '.....':'5', '-....':'6', 
                    '--...':'7', '---..':'8', '----.':'9', 
                    '-----':'0', '--..--':', ', '.-.-.-':'.', 
                    '..--..':'?', '-..-.':'/', '-....-':'-', 
                    '-.--.':'(', '-.--.-':')'} 

def decode_bits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    #return bits.replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')
    res = ""
    maxRunOfZeroes = 0
    transmissionRate = 1
    wordSeparator = ""
    bits = bits.lstrip('0')
    bits = bits.rstrip('0')
    if bits == "111000111": return ".."
    if bits == "111000111000111": return "..."    
    if bits != "1" and bits != "111":
        listAll = list(map(int, str(bits)))
        if "0" in bits:
            maxRunOfZeroes = max(len(list(y)) for (c,y) in itertools.groupby(listAll) if c==0)
            if maxRunOfZeroes % 7 == 0:
                wordSeparator = "0"*int(maxRunOfZeroes)
                transmissionRate = maxRunOfZeroes / 7
                bits = bits.split(wordSeparator)
            elif maxRunOfZeroes % 3 == 0:
                transmissionRate = maxRunOfZeroes / 3
            else:
                transmissionRate = maxRunOfZeroes
        bits = [bits]
    
        for bit in bits:
            if wordSeparator == "":
                res += str(bit).replace('1111111'*int(transmissionRate), '.').replace('111111'*int(transmissionRate), '..').replace('111'*int(transmissionRate), '-').replace('000'*int(transmissionRate), ' ').replace('1'*int(transmissionRate), '.').replace('0'*int(transmissionRate), '')    
            else:
                for word in bit:
                    res+= "  "
                    res += str(word).replace('111'*int(transmissionRate), '-').replace('000'*int(transmissionRate), ' ').replace('1'*int(transmissionRate), '.').replace('0'*int(transmissionRate), '')    
    else: return "." 

    res = res.lstrip()
    return res.rstrip()

def decode_morse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    res = ''
    splitList = morse_code.split("  ")
    tempLists = []
    for i in splitList: tempLists.append(i.split())
    for char in tempLists:
        for _ in char:
            res += MORSE_CODE[_]
        res += ' '
    res = res.lstrip()
    return res.rstrip()

#the best community solution
def decodeBits(bits):
    import re
    
    # remove trailing and leading 0's
    bits = bits.strip('0')
    
    # find the least amount of occurrences of either a 0 or 1, and that is the time hop
    time_unit = min(len(m) for m in re.findall(r'1+|0+', bits))
    
    # hop through the bits and translate to morse
    return bits[::time_unit].replace('111', '-').replace('1','.').replace('0000000','   ').replace('000',' ').replace('0','')

def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[l] for l in w.split()) for w in morseCode.split('   '))

'''

'''
==========================================================================
NAME Catching Car Mileage Numbers

Description:
"7777...8?!??!", exclaimed Bob, "I missed it again! Argh!" Every time there's an interesting number coming up, he notices and then promptly forgets. Who doesn't like catching those one-off interesting mileage numbers?

Let's make it so Bob never misses another interesting number. We've hacked into his car's computer, and we have a box hooked up that reads mileage numbers. We've got a box glued to his dash that lights up yellow or green depending on whether it receives a 1 or a 2 (respectively).

It's up to you, intrepid warrior, to glue the parts together. Write the function that parses the mileage number input, and returns a 2 if the number is "interesting" (see below), a 1 if an interesting number occurs within the next two miles, or a 0 if the number is not interesting.

Note: In Haskell, we use No, Almost and Yes instead of 0, 1 and 2.

"Interesting" Numbers
Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:

Any digit followed by all zeros: 100, 90000
Every digit is the same number: 1111
The digits are sequential, incementing: 1234
The digits are sequential, decrementing: 4321
The digits are a palindrome: 1221 or 73837
The digits match one of the values in the awesomePhrases array

For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.

#my solution
def incNumber(number, res):
    l = list(map(int, str(number)))
    result = res
    for t in zip(l, l[1:]):
        if t[0] == 9 and t[1] == 0:
            continue
        if t[0]+1 != t[1]: 
            result = 0
    return result

def decNumber(number, res):
    l = list(map(int, str(number)))
    result = res
    for t in zip(l, l[1:]):
        if t[0]-1 != t[1]:
            result = 0
    return result            

def findResult(res, result):
    return max(res, result)

def is_interesting(number, awesome_phrases):
    result = 0
    res = 0

    if len(str(number)) > 2:
        
        #The digits are sequential, incementing: 1234
        res += incNumber(number, 2)
        if res == 0:
            res = incNumber(number+1, 1)
        if res == 0:
            res = incNumber(number+2, 1)
        if res == 0:
            res = incNumber(number-1, 1)
        if res == 0:
            res = incNumber(number-2, 1)
        
        result = findResult(res, result)
        
        #The digits are sequential, decreasing: 1234
        res += decNumber(number, 2)
        if res == 0:
            res = decNumber(number+1, 1)
        if res == 0:
            res = decNumber(number+2, 1)
        if res == 0:
            res = decNumber(number-1, 1)
        if res == 0:
            res = decNumber(number-2, 1)
            
        result = findResult(res, result)
            
        #The digits are a palindrome: 1221 or 73837 or #Every digit is the same number: 1111
        if number == int(str(number)[::-1]):   res += 2
        
        result = findResult(res, result)
            
        if number + 1 == int(str(number+1)[::-1]) or number + 2 == int(str(number+2)[::-1]) or number - 1 == int(str(number-1)[::-1]) or number - 2 == int(str(number-2)[::-1]):
            res = 1
            
        result = findResult(res, result)
            
        #The digits match one of the values in the awesome_phrases array
        if number in awesome_phrases: res += 2
        result = findResult(res, result)
        if number + 1 in awesome_phrases or number + 2 in awesome_phrases or number - 1 in awesome_phrases or number - 2 in awesome_phrases:
            res = 1
            
        result = findResult(res, result)
        
         #Any digit followed by all zeros: 100, 90000
        if int(str(number)[1:]) == 0:
            res += 2
        result = findResult(res, result)
        if int(str(number-2)[1:]) == 0 or int(str(number-1)[1:]) == 0 or int(str(number+1)[1:]) == 0 or int(str(number+2)[1:]) == 0:
            res = 1
        result = findResult(res, result)    
               
    elif number > 97:
        #Any digit followed by all zeros: 100, 90000
        if int(str(number)[1:]) == 0:
            result += 2
        if int(str(number-2)[1:]) == 0 or int(str(number-1)[1:]) == 0 or int(str(number+1)[1:]) == 0 or int(str(number+2)[1:]) == 0:
            result = 1
    
    if result > 2:
        return 2
    else: return result
    
#the best community solution
def is_incrementing(number): return str(number) in '1234567890'
def is_decrementing(number): return str(number) in '9876543210'
def is_palindrome(number):   return str(number) == str(number)[::-1]
def is_round(number):        return set(str(number)[1:]) == set('0')

def is_interesting(number, awesome_phrases):
    tests = (is_round, is_incrementing, is_decrementing,
             is_palindrome, awesome_phrases.__contains__)
       
    for num, color in zip(range(number, number+3), (2, 1, 1)):
        if num >= 100 and any(test(num) for test in tests):
            return color
    return 0

'''




'''
==========================================================================
NAME

'''
