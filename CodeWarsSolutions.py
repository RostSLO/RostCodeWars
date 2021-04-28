


res = order_weight("103  123 4444   99 2000")
print(res)
res = order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")
print(res)
res = order_weight("")
print(res)
   



'''
==========================================================================
Weight for weight

def order_weight(strng):

    if strng == "" or strng is None:
        return ""

    resList = []
    num = 0

    strList = strng.split(" ")

    for n in strList:
        if n != '':
            num = 0
            for i in n:
                num += int(i)
            resList.append((num,  n))
    resList.sort()

    return ' '.join(str(i[1]) for i in resList)


the best answer
def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))


'''


'''
==========================================================================
Human Readable Time

def make_readable(seconds):
    
    hours = int(seconds / 3600)
    minutes = int((seconds-hours*3600) / 60)
    sec = seconds - minutes*60 - hours*3600
    
    return f'{hours:02d}:{minutes:02d}:{sec:02d}'

'''


'''
==========================================================================
Sum of pairs

def sum_pairs(ints, s):
    
    distance = len(ints)
    badNumbers = []
    i = first = second =  0
    secondNumExists = False
    
    for i in range(len(ints)-1):
        if ints[i] not in badNumbers:
            secondNumber = s - ints[i]
            if secondNumber in ints[i+1:i+distance]:
                if secondNumber == ints[i+1]: return [ints[i], secondNumber]
                elif distance > ints[i+1:i+distance].index(secondNumber):
                    first = ints[i]
                    second = secondNumber
                    distance = ints[i+1:i+distance].index(secondNumber)
            else: badNumbers.append(ints[i])

    return ([first, second] if distance != len(ints) else None)
'''


'''
==========================================================================
Valid Parentheses

def valid_parentheses(string):
    
    if string == '': return True
    
    open = 0
    
    for char in string[::-1]:
        if char == ')':
            open -= 1
        elif char == '(' and open < 0:
            open += 1
        elif char == '(':
            return False
            
    return (True if open == 0 else False)        
'''


'''
==========================================================================
Highest Scoring Word

def high(x):

    resList = x.split(" ")
    result = ''
    resNum = winner = 0

    for word in resList:
        resNum = 0
        for ch in word:
            resNum += ord(ch) - 96
            
        if resNum > winner:
            result = word
            winner = resNum
     
    return result 

    #return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

'''



'''
==========================================================================
English beggars

def beggars(values, n):
    
    return [sum(values[i::n]) for i in range(n)]

'''



'''
==========================================================================
Unique In Order


def unique_in_order(iterable):

    return [iterable[i] for i in range(len(iterable)) if i == 0 or iterable[i] != iterable[i-1]]
        

'''


'''
==========================================================================
Vasya - Clerk

def tickets(people):
    
    bill25 = bill50 = bill100 = 0
    
    for bill in people:
        if bill == 25:
            bill25 += 1
        if bill == 50:
            bill50 += 1
            if bill25 == 0: return "NO"
            bill25 -= 1
        if bill == 100:
            bill100 += 1
            if bill25 == 0 or (bill25 < 3 and bill50 == 0): return "NO"
            if bill50 > 0:
                bill50 -= 1
                bill25 -= 1
            else: bill25 -= 3

    return "YES"
'''

'''
==========================================================================
IQ Test

def iq_test(numbers):
    
    if numbers is None or len(numbers) == 0:
        return 0
    
    resList = numbers.split(" ")
    
    counter = even = odd = evenPosition = oddPosition = 0
    
    for i in range(len(resList)):
        counter += 1
        if int(resList[i])%2 == 0:
            if even > 1 and odd == 1: return oddPosition
            even += 1
            evenPosition = i+1
        else:
            if odd > 1 and even == 1: return evenPosition
            odd += 1
            oddPosition = i+1
        
    return (evenPosition if even == 1 else oddPosition)

'''


'''
==========================================================================
Equal Sides Of An Array

def find_even_index(arr):
    
    for i in range(0, len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    
    return -1
'''

'''
==========================================================================
Create Phone Number

def create_phone_number(n):
    
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)
    
    #return '({}) '.format(''.join(str(n[i]) for i in range(0, 3))) + '{}-'.format(''.join(str(n[i]) for i in range(3, 6))) + '{}'.format(''.join(str(n[i]) for i in range(6, 10)))
    
'''

'''
==========================================================================
Dubstep
    
def song_decoder(song):
    
    if song is None or len(song) == 0:
        return ""
    
    #return ' '.join([value for value in song.split('WUB') if value != ''])
    
    return " ".join(song.replace('WUB', ' ').split())

'''

'''
==========================================================================
Tribonacci Sequence

def tribonacci(signature, n):
    
    if n == 0 or signature is None or len(signature) == 0:
        return []
    
    resList = signature[:n]
    
    for i in range(n-3): resList.append(sum(resList[i:i+3]))
                       
    return resList
        
'''


'''
==========================================================================
Bit Counting

def count_bits(n):
    
    
    return str(bin(n)).count('1')

'''


'''
==========================================================================
Duplicate encode


def duplicate_encode(word):
    
    if word is None or word =='':
        return ''

    return ''.join('(' if word.count(ch) == 1 else ')' for ch in word.lower())
'''



'''
==========================================================================
Find the odd int


def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
'''


'''
==========================================================================

Multiples of 3 or 5

def solution(number):
    
    if number < 0: return 0
    
    resList = []
    
    resList = [i for i in range(0, number, 3)]
    resList += [i for i in range(0, number, 5)]

    return sum(set(resList))
'''

'''
def epidemic(tm, n, s, i, b, a):
    def f(s, i, r):  
        dt = tm / n
        for t in range(n):
            s, i, r = s-dt*b*s*i, i+dt*(b*s*i-a*i), r+dt*i*a
            yield i
    return int(max(f(s, i, 0)))


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def epidemic(tm, n, s0, i0, b, a):
    # your code
    dt = tm/n
    S = []
    I = []
    R = []
    S.append(s0)
    I.append(i0)
    R.append(0)
    for k in range(n-1):
        S.append(S[k] - dt * b * S[k] * I[k])
        I.append(I[k] + dt * (b * S[k] * I[k] - a * I[k]))
        R.append(R[k] + dt * I[k] *a)
    
    df = pd.DataFrame({'Susceptible': S,
                     'Infected': I,
                     'Recovered': R})
    
    df.plot()
    
    plt.show()
    
    return int(max(I))

'''

'''
==========================================================================
def run(tricks):
   
    resDict = {}
   
    for i in range(len(tricks)):
        currentVal = nextVal = previousPoints = counter = 0
        while currentVal <= nextVal:
            counter += 1
            currentVal = nextVal

            nextVal = (tricks[i]['probability']**(counter))*(previousPoints + tricks[i]['points']*tricks[i]['mult_base']**(counter-1))
            previousPoints += (tricks[i]['points']*tricks[i]['mult_base']**(counter-1))
        
        #print(str(currentVal))    
        resDict[tricks[i]['name']] = counter-1

    return resDict

res = run([{ 'name': 'kickflip', 'points': 100, 'mult_base': .8, 'probability': .95 },
           { 'name': 'heelflip', 'points': 101, 'mult_base': .25, 'probability': .95 },])
print(res)

res = run([{ 'name': 'kickflip', 'points': 100, 'mult_base': .8, 'probability': .95 },
           { 'name': 'pop shove it', 'points': 50, 'mult_base': .75, 'probability': .99 },])
print(res)

res = run([{ 'name': 'kickflip', 'points': 100, 'mult_base': .8, 'probability': .95 },
                        { 'name': 'pop shove it', 'points': 50, 'mult_base': .75, 'probability': .995 },
                        { 'name': '360 flip', 'points': 250, 'mult_base': .825, 'probability': .9 },])
print(res)

res = run([{ 'name': 'kickflip', 'points': 100, 'mult_base': .8, 'probability': .95 },
                        { 'name': 'pop shove it', 'points': 50, 'mult_base': .75, 'probability': .995 },
                        { 'name': '360 flip', 'points': 250, 'mult_base': .825, 'probability': .9 },
                        { 'name': '50-50 grind', 'points': 150, 'mult_base': .9, 'probability': .925 },
                        { 'name': 'noseslide', 'points': 100, 'mult_base': .8, 'probability': .95 },
                        { 'name': 'manual', 'points': 50, 'mult_base': .99, 'probability': .975 },])
print(res)
'''

'''
==========================================================================
NAME: Who likes it?

def persistence(n):
    
def likes(names):
   
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
    
    
'''


'''
==========================================================================
NAME: Find The Parity Outlier

def persistence(n):
    
    counter = 1
    strNum = str(n)
    resNum = 1
    resBool = False
    
    if n < 9:
        return 0
    
    while not resBool:
        for chr in strNum:
            resNum *= int(chr)

        if resNum >= 10: 
            counter += 1
            strNum = str(resNum)
            resNum = 1
        else: 
            resBool = not resBool    
        
    
    return counter
    
    
'''

'''
==========================================================================
NAME: Find The Parity Outlier

def find_outlier(integers):

    resNum = 0
    oddEven = -1
    
    if len(integers) == 0:
        return None
    elif len(integers) == 1:
        return integers[0]
    else:
        if (integers[0]%2 == 0 and integers[1]%2 == 0) or (integers[1]%2 == 0 and integers[2]%2 == 0) or (integers[0]%2 == 0 and integers[2]%2 == 0): oddEven = 1
        else: oddEven = 0
    
    for item in integers:
        if oddEven == 0 and item%2 == 0:
                return item
        if oddEven == 1 and item%2 != 0:
                return item
            
    
    return resNum
    
    
'''


'''
==========================================================================
NAME: Statistics for an Athletic Association

def secToTimeFormat(sec):
    #transfer seconds to time format
    
    resStr = ""
    #calculating hours
    h = sec / 3600
    if h < 0:
        resStr += "00|"
    elif int(h) < 10 :
        resStr += "0" + str(int(h)) + "|"
    else:
        resStr += str(int(h)) + "|"
    
    sec = sec - int(h)*3600
    
    m = sec / 60    
    if m < 0:
        resStr += "00|" + str(sec)
    elif m < 10: 
        resStr += "0" + str(int(m)) + "|" 
    else:
        resStr += str(int(m)) + "|" 
     
    sec = int(sec - int(m)*60)
     
    if sec < 10:
        resStr += "0" + str(sec)
    else:
        resStr += str(sec)
        
    return resStr    
    

def stat(strg):

    if strg is None or strg == "":
        return ""
    
    inputList = strg.split(", ")
    
    tempList = []
    
    #transfer time to seconds
    for item in inputList:
        tempList.clear()
        tempList = item.split("|")
        inputList[inputList.index(item)] = 3600*int(tempList[0]) + 60*int(tempList[1]) + int(tempList[2])  
    
    #find Range
    resStr = "Range: " + secToTimeFormat(max(inputList) - min(inputList))
    
    #find Mean or Average
    resStr += " Average: " + secToTimeFormat(int(sum(inputList)/len(inputList)))

    inputList.sort()

    #find Median
    if not len(inputList)%2:
        resStr += " Median: " + secToTimeFormat(int(inputList[int(len(inputList)/2)-1] + inputList[int(len(inputList)/2)])/2)
    else:
        resStr += " Median: " + secToTimeFormat(inputList[int(len(inputList)/2)])
    
    return resStr
    
'''



'''
==========================================================================
NAME: Playing with passphrases

def play_pass(s, n):
    resStr = ""
    counter = 1
    s = s.lower()
    for c in s:
        index = 0
        if c.isdigit(): resStr += str(9-int(c))
        elif not c.isdigit() and not c.isalpha(): resStr += c
        else: 
            if (ord(c) + n) > ord("z"): index = 96 + (ord(c) + n) - ord("z")
            else: index = (ord(c) + n)
     
            if not counter%2:
                resStr += chr(index).lower()
            else: resStr += chr(index).upper()
        counter += 1
        
    return resStr[::-1]
'''
'''
==========================================================================
NAME: Playing with digits

def dig_pow(n, p):

    resStr = str(n)
    sum = counter = 0
    
    for i in resStr:
        sum += int(i)**(p+counter)
        counter += 1
    
    return (int(sum/n) if not sum%n else -1)
'''

'''
==========================================================================
NAME: Stop gninnipS My sdroW

def spin_words(sentence):

    return " ".join(word[::-1] if len(word) >= 5 else word for word in sentence.split(" ")) 

'''

'''
==========================================================================
NAME: count '9's from 1 to n

def count_nines(n):
#    return "".join(str(i) for i in range(n+1)).count("9")
    
    strN = str(n)
    resInt = 0
    lenOfStr = len(strN)
    counter = 0
    if n >= 9:
        for i in strN:
            currentI = int(i)
            if counter < lenOfStr - 1:
                if currentI == 9:
                    resInt +=  9*(lenOfStr-counter-1)*10**(lenOfStr-counter-2) + 1 + int(strN[counter+1:])
                    counter += 1
                else: 
                    resInt += currentI*((lenOfStr-counter-1)*10**(lenOfStr-counter-2))
                    counter += 1
            else:
                if currentI == 9: resInt += 1
    else: return resInt
    
    return resInt

'''


'''
==========================================================================
NAME: Is my friend cheating?

def remov_nb(n):
    resList = []
    x = n*(n+1)/2  
    for a in range(n):
        if (x-a)%(a+1) == 0:
            b = (x - a) / (a + 1)
            if b < n and a!= b:
                resList.append((a, int(b)))
    return resList

'''


'''
==========================================================================
NAME: Pete, the baker


def cakes(recipe, available):
    return min([int(available.get(item, 0)/recipe[item]) if item in available  else 0 for item in recipe])

'''


'''
==========================================================================
NAME: Roman Numerals Encoder

def solution(roman):
    romValues = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    num = ''
    numBefore = ''
    res = 0
    for num in list(roman)[::-1]:
        if res == 0:
            res = romValues[num]
        elif romValues[num] >= romValues[numBefore]:
            res += romValues[num]
        else:
            res -= romValues[num]
            
        numBefore = num    
    
    return res
''' 


'''
==========================================================================
NAME: Directions Reduction
Description:
Once upon a time, on a way through the old wild mountainous west, a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.
Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadfull weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed a mountainous desert the smart way.
The directions given to the man are, for example, the following (depending on the language):

["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
or
{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
or
[North, South, South, East, West, North, West]
You can immediatly see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place! So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:

["WEST"]
or
{ "WEST" }
or
[West]
Other examples:
In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and coming back right away.

The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore, the final result is [] (nil in Clojure).

In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly opposite but they become directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].

Task
Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

The Haskell version takes a list of directions with data Direction = North | East | West | South.
The Clojure version returns nil when the path is reduced to nothing.
The Rust version takes a slice of enum Direction {NORTH, SOUTH, EAST, WEST}.
See more examples in "Sample Tests:"
Notes
Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such. Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
if you want to translate, please ask before translating.

#my solution
def dirReduc(arr):
    for i in range(1, len(arr)):
        if i <= len(arr)-1:
            if (arr[i-1] in ("NORTH") and arr[i] in ("SOUTH")) or (arr[i-1] in ("SOUTH") and arr[i] in ("NORTH")) or (arr[i-1] in ("EAST") and arr[i] in ("WEST")) or (arr[i-1] in ("WEST") and arr[i] in ("EAST")):
                arr.pop(i-1)
                arr.pop(i-1)
                arr = dirReduc(arr)
    
    return arr
    
#The best community solution    
opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan

'''
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
"Dot" is 1 time unit long. "Dash" is 3 tie units long. 
Pause between dots and dashes in a character is 1 time unit long.
Pause between characters inside a word  is 3 time units long.
Pause between words is 7 time units long.
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
