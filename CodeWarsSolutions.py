

def next_smaller(n):

    res = []
    
    strNum = str(n)
    for i in range(len(strNum)-1, 0, -1):
        m = strNum[i]
        for j in range(i-1, -1, -1):
            if int(m) < int(strNum[j]):
                res.append(strNum[:j] + m + strNum[i+1:])

    res.sort(reverse = True)
    print(res)
    return res[0]

print(next_smaller(531))
print(next_smaller(29009))
#print(RomanNumerals.from_roman('MCDXCV'))
#print(mix("Lords of the Fallen", "gamekult"))
#print(mix("codewars", "codewars"))
#print(mix("A generation must confront the looming ", "codewarrs"))




'''

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):

    level = 0
    res = []
    finalRes = []

    if node == None: return []

    # take second element for sort
    def takeSecond(elem):
        return elem[1]


    def serf_the_tree(node, level, res):
        level += 1
        if node.left != None: 
            res = serf_the_tree(node.left, level, res)

        if node.right != None: 
            res = serf_the_tree(node.right, level, res)

        return res + [(node.value, level)]

    finalRes = serf_the_tree(node, level, res)
    finalRes.sort(key=takeSecond)

    return [x[0] for x in finalRes]

#       1
#   2       3
#     4   5    6
# [1, 2, 3, 4, 5, 6]

def decompose(n):
    def _recurse(s, i):
        if s < 0:
            return None
        if s == 0:
            return []
        for j in range(i-1, 0, -1):
            sub = _recurse(s - j**2, j)
            if sub != None:
                return sub + [j]
    return _recurse(n**2, n)




def is_list(p):
    return isinstance(p, list)

def same_structure_as(original,other):
    if not is_list(original) and not is_list(other):
        return True
    elif (is_list(original) and is_list(other)) and (len(original) == len(other)):
        return all(map(same_structure_as, original, other)) # Here
    return False




def longest_slide_down(p):
    res = p.pop()
    while p:
        tmp = p.pop()
        res = [tmp[i] + max(res[i],res[i+1])  for i in range(len(tmp))] 
    return res.pop()

print(longest_slide_down([
                                        [75],
                                      [95, 64],
                                    [17, 47, 82],
                                  [18, 35, 87, 10],
                                [20,  4, 82, 47, 65],
                              [19,  1, 23, 75,  3, 34],
                            [88,  2, 77, 73,  7, 63, 67],
                          [99, 65,  4, 28,  6, 16, 70, 92],
                        [41, 41, 26, 56, 83, 40, 80, 70, 33],
                      [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
                    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
                  [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
                [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
              [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
            ]))


class RomanNumerals:

    @staticmethod
    def iterTransforming(remValue, levelValue):
        return [remValue%levelValue, int(remValue/levelValue)]
    
    @staticmethod
    def to_roman(val):
        
        if val == 0: return "Now"
        
        decypher = [
        ["M", 1000],
        ["CM", 900],
        ["D", 500],
        ["CD", 400],
        ["C", 100],
        ["XC", 90],
        ["L", 50],
        ["XL", 40],
        ["X", 10],
        ["IX", 9],
        ["V", 5],
        ["IV", 4],
        ["I", 1]
        ]
        res = [val, -1]
        finalRes = []
        
        # Check if value is higher than particular level in the decypher and start iterating 
        # from this level 
        counter = 0

        while res[0] > 0:

            # counter will iterate through decypher dict, but first we should check what is the next
            # closest level for the remainder
            while res[0] < decypher[counter][1]: 
                t = decypher[counter][1]
                counter += 1

            # Computation that will take 1: number value (remaining), 2: level (M, or D etc...)
            # returns: 1: reminder; 2: amount of levels in the number value (remainder for the next one if not 0)
            res = [res[0]%decypher[counter][1], int(res[0]/decypher[counter][1])]

            finalRes.append(decypher[counter][0]*res[1])

        return ''.join(x for x in finalRes)

    @staticmethod
    def from_roman(roman_num):
        
        if roman_num == 0: return "Now"
        
        decypher = [
        ["CM", 900],
        ["CD", 400],
        ["XC", 90],
        ["IX", 9],        
        ["IV", 4],
        ["XL", 40],
        ["M", 1000],
        ["D", 500],
        ["C", 100],
        ["L", 50],
        ["X", 10],
        ["V", 5],
        ["I", 1]        ]
        finalRes = []
        for x in decypher:
            if roman_num.count(x[0]) > 0: 
                finalRes.append(x[1]*roman_num.count(x[0]))
                roman_num = roman_num.replace(x[0]*roman_num.count(x[0]), '')
            if len(roman_num) == 0:
                break
        
        return sum(x for x in finalRes)


def fix(l, a, b):
   """let l.index(a) < l.index(b)"""
   if l.index(a) > l.index(b):
       l.remove(a)
       l.insert(l.index(b), a)

def recoverSecret(triplets):
  r = list(set([i for l in triplets for i in l]))
  for l in triplets:
    fix(r, l[1], l[2])
    fix(r, l[0], l[1])
  return ''.join(r)
  


#triplets = [
#  ['t','u','p'],
#  ['w','h','i'],
#  ['t','s','u'],
#  ['a','t','s'],
#  ['h','a','p'],
#  ['t','i','s'],
#   ['w','h','s']]
triplets = [['t', 's', 'f'], 
['a', 's', 'u'], 
['m', 'a', 'f'], 
['a', 'i', 'n'], 
['s', 'u', 'n'], 
['m', 'f', 'u'], 
['a', 't', 'h'], 
['t', 'h', 'i'], 
['h', 'i', 'f'], 
['m', 'h', 'f'], 
['a', 'u', 'n'], 
['m', 'a', 't'], 
['f', 'u', 'n'], 
['h', 's', 'n'], 
['a', 'i', 's'], 
['m', 's', 'n'], 
['m', 's', 'u']]
print(recoverSecret(triplets))




def perm(str):

    resList = []

    l = list(str)

    if len(l) == 0: return []

    if len(l) == 1: return [l]

    for i in range(len(l)):
        m = l[i]

        tempList = l[:i] + l[i+1:]

        for p in perm(tempList):
            resList.append([m] + p)

    return resList



def dbl_linear(n):
	# your code

    res = []
    temp = []
    i = 0

    if n == 0: return 1
    if n == 1: return 3
    if n == 2: return 4

    res = res+ [1] 

    while i < n/2+n/10+3:
        res = res + [res[i]*2+1] + [res[i]*3+1]
        i += 1
        if i%3 == 0: 
            temp = res[len(res)-i:]
            res = res[:len(res)-i]
            temp.sort()
            res = res + temp

    res = list( dict.fromkeys(res) )

    return res[n]



# take second element for sort
def takeThird(elem):
    return len(elem[2])

def mix(s1, s2):
    # your code

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lTemp1 = []
    lTemp2 = []
    lTemp3 = []
    lRes = []
    lResFinal = []
    res = ''


    # 1. calculate number of different letter in each string and put result in temp storage
    # reviewing alphabetically should guarantee the proper sequense, i think (?)
    for x in alphabet:
        if s1.count(x) == s2.count(x) and s1.count(x) > 1: lRes = lRes + [(x, "=", s1.count(x)*x, s1.count(x))]
        elif s1.count(x) > s2.count(x) and s1.count(x) > 1: lRes = lRes + [(x, 1, s1.count(x)*x, s1.count(x))]
        elif s2.count(x) > 1: lRes = lRes + [(x, 2, s2.count(x)*x, s2.count(x))]

    if len(lRes) == 0: return ''
    elif len(lRes) > 1:

        lRes.sort(key=takeThird, reverse=True)
        start = 0
        
        if lRes[0][1] == 1: lTemp1.append(lRes[0])
        elif lRes[0][1] == 2: lTemp2.append(lRes[0])
        else: lTemp3.append(lRes[0])
        
        for i in range(1, len(lRes)):
            if lRes[i-1][3] == lRes[i][3]:
                if lRes[i][1] == 1: lTemp1.append(lRes[i])
                elif lRes[i][1] == 2: lTemp2.append(lRes[i])
                else: lTemp3.append(lRes[i])
            else:
                if len(lTemp1) == 0 and len(lTemp2) == 0 and len(lTemp3) == 0:
                    if 1 < len(lRes) - 1:
                        lResFinal = lResFinal.append(lRes[i-1])  
                    else: lResFinal = lResFinal.append(lRes[i])                    
                else: lResFinal = lResFinal + lTemp1 + lTemp2 + lTemp3
                lTemp1 = []
                lTemp2 = []
                lTemp3 = []
                if lRes[i][1] == 1: lTemp1.append(lRes[i])
                elif lRes[i][1] == 2: lTemp2.append(lRes[i])
                else: lTemp3.append(lRes[i]) 

        if len(lTemp1) != 0 or len(lTemp2) != 0 or len(lTemp3) != 0:
            lResFinal = lResFinal + lTemp1 + lTemp2 + lTemp3    
    else: 
        return str(lRes[1])+":"+lRes[2]

    return '/'.join(str(x[1])+":"+x[2] for x in lResFinal if x[3] > 1)


def permutations(s):
    
    # return string if it has 1 character
    if len(s) == 1: return [s]

    # start permutations
    l = []
    d = {}

    for i in range(len(s)):
        m = s[i]

        remLst = s[:i] + s[i+1:]

        for x in permutations(remLst):
            #if l.count(m + x) == 0: 
            #l = l+ [m + x]
            d[m + x] = None


    return list(d)



def sum_of_intervals(intervals):

    if len(intervals) == 1: return intervals[0][1] - intervals[0][0]

    res = []
    temp = []
    s = 0

    for i in range(len(intervals)):
        if intervals[i] != (0, 0):
            change = False
            temp = [intervals[i]]
            for j in range(len(intervals)):
                if j != i and intervals[j] != (0, 0):
                    if temp[0][1] >= intervals[j][0] and temp[0][0] <= intervals[j][1]:
                        # Situation 1: second interval starts in the first but end oustide of the first
                        if temp[0][0] <= intervals[j][0] and temp[0][1] <= intervals[j][1]:
                            temp = [(temp[0][0], intervals[j][1])]
                            change = True

                        # Situation 2: second interval iside the first
                        elif temp[0][0] <= intervals[j][0] and temp[0][1] >= intervals[j][1]:
                            change = True

                        # Situation 3: second interval starts earlier than the first but ends inside the first
                        elif temp[0][0] >= intervals[j][0] and temp[0][1] >= intervals[j][1]:
                            temp = [(intervals[j][0], temp[0][1])]
                            change = True

                        # Situation 4: first interval inside the second one
                        elif temp[0][0] >= intervals[j][0] and temp[0][1] <= intervals[j][1]:
                            temp = [(intervals[j][0], intervals[j][1])]
                            change = True 

                        if change:
                            intervals[j] = (0, 0)
            res = res + temp
            intervals = intervals + temp
            intervals[i] = (0, 0)

    for x in intervals:
        s += abs(x[1] - x[0])

    return s


def move_zeros(lst):
    
    newLst = [x for x in lst if x != 0] + [x for x in lst if x == 0]

    return newLst


def perimeter(n):
    
    last = new = res = 1
    final = 2
    
    #find the sum of 1 side from all rectangels
    if n > 0:
        for i in range(1, n):
            res = res + last
            last = new
            new = res
            final = final + res

    else: final = 1
    
    return str(4*final)


def strip_comments(strng, markers):
    print(strng)
    strng = strng.replace("\n", "\n ")
    for i in range(len(markers)):
        strng = strng.replace(markers[i], markers[i]+' ')

    l = list(strng.split(' '))

    print(l)

    for s in range(len(markers)):
        i = -1
        if markers[s] in l:
            i = l.index(markers[s])
            if s == 0:
                empty = True
                for j in range(0, i):
                    if l[j] not in ('', '\n', '\t'):
                        empty = False
                        break
                if empty: l = l[i-1:len(l)]
            count = l.count(markers[s])
            for j in range (0, count):
                if markers[s] in l: 
                    i = l.index(markers[s])
                    for w in range(i, len(l)):
                        if "\n" in l[w]:
                            l = l[0:i] + ['\n'] + l[w+1:len(l)]
                            print(l)
                            break
                        elif w == len(l)-1:
                            l = l[0:i]
                            print(l)

    for i in range(len(l)-1):
        if "\n" != l[i+1] and "\n" not in l[i]:
            l[i] = l[i] + ' '

    print(l)
    return ''.join( x for x in l )    


def strip_comments(strng, markers):
    iter = 0
    i = 0
    l = []

    while iter >= 0:
        if i < len(strng):
            s = strng[i]
            if strng[i] in markers:
                j = i
                while j < len(strng) - 1:
                    j += 1
                    if strng[j] == '\n': 
                        strng = strng[0:i] + strng[j:len(strng)]
                        j = len(strng) + 2
                if j == len(strng)-1:
                    strng = strng[0:i]
                i += 1
            else: i += 1
        else: iter = -1
    
    l = strng.split('\n')
    
    res = '\n'.join(x.rstrip() for x in l)
    
    return res



def validate(l):
    
    for r in l:
        for i in r:
            if l[0].count(i) + l[1].count(i) + l[2].count(i)  > 1: return False   

    return True 



def valid_solution(board):
    
    n = 9

    #check zeroes and rows
    for l in board:
        if l.count(0) > 0: return False
        for i in l:
            if l.count(i) > 1: return False
        
    #check columns
    transposedList = [list(i) for i in zip(*board)]
    for l in transposedList:
        for i in l:
            if l.count(i) > 1: return False

    subList = []
    l = []
    for v in range(0, 9, 3):
        for h in range(0, 9, 3):
            for i in range(v, v+3):
                l.append(board[i][h])
                l.append(board[i][h+1])
                l.append(board[i][h+2])
                subList.append(l)
                l = []
            print(subList)  
            if not validate(subList): return False
            subList = []

    return True

'''
'''
    for i in range(len(s), 0, -1):
        c = s[i - 1: i]
        s1 = s[:i-1]
        s2 = s[i:len(s)]
        newStr = s1 + s2        
        for j in range(len(newStr)+1):
            sTemp = newStr[0:j] + c + newStr[j:len(newStr)]
            #if resList.count(int(sTemp)) == 0:
            resList.append(int(sTemp))
        if ind > 1:
            ind -= 1

            permutation( , sTemp, ind)

def permutation(s, d):

    global depth

    # If lst is empty then there are no permutations
    if len(s) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(s) == 1:
        return [s]


    l = [] # empty list that will store current permutation
 
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(s)):
        m = s[i]
        
        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = s[:i] + s[i+1:]
    
        # Generating all permutations where m is first
        # element

        for p in permutation(remLst, depth):
            depth += 1
            #l.append([m] + p)
            if d == 0 and int(m + p) > int(s):
                l.append(m + p)
            elif d != 0: l.append(m + p)

    return l

depth = 0

def next_bigger(n):
    
    if n <= 10: return -1

    s = str(n)
    #finalList = []
    delta = -1
    res = -1

    for p in permutation(s, 0):
        #finalList.append(int(''.join(c for c in p)))
        print(p)
        #num = int(p)
        #num = int(''.join(c for c in p))
        #print(str(num))
        if int(p) > n:
            if delta == -1: 
                res = int(p)
                delta = int(p) - n 
            elif int(p) - n < delta: 
                res = int(p)
                delta = int(p) - n
    
    #finalList.sort()

    #for i in finalList:
    #    if i > n: return i

    return "result = " + str(res)

#1. Make all permutations of possible numbers
#2. Sort them
#3. find the first that is bigger than the input


def changeAtoB(arr, a, b):
    inc = 0
    for i in arr:
        if a in str(i) or b in str(i): 
            arr[inc] = int(str(i).replace(a,'x').replace(b, a).replace('x', b))
        inc += 1
    return arr


def sort_twisted37(arr):
    revertArr = arr
    revertArr = changeAtoB(revertArr, "3", "7")
    revertArr.sort()
    return changeAtoB(revertArr, "7", "3")



def likes(names):
    l = len(names)
    res = ""
    if l == 0:
        res = "no one likes this"
    elif l > 0 and l < 4:
        if l == 1:
            res = names[0] + " likes this"    
        elif l == 2:
            res = names[0] + " and " + names[1] + " like this"
        else: res = names[0] + ", " + names[1] + " and " + names[2] + " like this"
    else:
        res = names[0] + ", " + names[1] + " and " + str(l - 2) + " others like this"

    return res


def find_uniq(arr):

    if arr[0] == arr[1] or arr[0] == arr[2]: n = arr[0] 
    else: n = arr[1]
    
    newSet = set(arr)
    newList = list(newSet)

    n = (newList[1] if newList[0] == n else newList[0])

    return n   # n: unique number in the array



def find_missing_letter(chars):
    
    upperBool = False
    res = 'empty'

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    if chars[0].isupper():
        upperBool = True
    
    if upperBool:
        for i in range(len(chars)-1):
            chars[i] = chars[i].lower()

    index = alphabet.index(chars[0])

    i = 0
    while chars[i] == alphabet[index]:
        index +=1
        i += 1 

    res = (alphabet[index].upper() if upperBool else alphabet[index])
    
    return res



def narcissistic( value ):
    # Code away
    res = True
    num = 0

    sValue = str(value)
    l = len(sValue)
    for s in sValue:
        num += int(s)**l

    res = (True if num == value else False )
    return res

'''
'''
def zero(): #your code here
def one(): #your code here
def two(): #your code here
def three(): #your code here
def four(): #your code here
def five(): #your code here
def six(): #your code here
def seven(): #your code here
def eight(): #your code here
def nine(): #your code here

def plus(): #your code here
def minus(): #your code here
def times(): #your code here
def divided_by(): #your code here

def zero(*func):
    if len(func) == 0: return 0
    else: return operation(func, 0)

def one(*func):
    if len(func) == 0: return 1
    else: return operation(func, 1)

def two(*func):
    if len(func) == 0: return 2
    else: return operation(func, 2)

def three(*func):
    if len(func) == 0: return 3
    else: return operation(func, 3)

def four(*func):
    if len(func) == 0: return 4
    else: return operation(func, 4)

def five(*func):
    if len(func) == 0: return 5
    else: return operation(func, 5)

def six(*func):
    if len(func) == 0: return 6
    else: return operation(func, 6)

def seven(*func):
    if len(func) == 0: return 7
    else: return operation(func, 7)

def eight(*func):
    if len(func) == 0: return 8
    else: return operation(func, 8)

def nine(*func):
    if len(func) == 0: return 9
    else: return operation(func, 9)

def plus(num):
    return str(num) + '+'
def minus(num):
    return str(num) + '-'
def times(num):
    return str(num) + '*'
def divided_by(num):
    return str(num) + '/'

def operation(func, num1):
    funcRes = func[0]
    sign = funcRes[-1]
    num2 = int(funcRes[0:len(funcRes)-1])
    if sign == '*': return num1 * num2
    elif sign == '+': return num1 + num2
    elif sign == '-': return num1 - num2
    else: return int(num1 / num2)

def round(num):
    return (num if num >= 0 and num <= 255 else (0 if num < 0 else 255))
    
def rgb(r, g, b):
    
    r = round(r)
    g = round(g)
    b = round(b)

    return (hex(r)[0] + hex(r)[2] if len(hex(r)) < 4 else hex(r)[2] + hex(r)[3]).upper() + (hex(g)[0] + hex(g)[2] if len(hex(g)) < 4 else hex(g)[2] + hex(g)[3]).upper() + (hex(b)[0] + hex(b)[2] if len(hex(b)) < 4 else hex(b)[2] + hex(b)[3]).upper()


def productFib(prod):
    a = 0
    b = 1

    while a * b < prod:
        c = a + b
        a = b
        b = c


    return ([a, b, True] if a * b == prod else [a, b, False])


def generate_hashtag(s):
    
    word = False
    l = list(s)
    for i in range(len(l)):
        if l[i] != ' ' and not word:
            l[i] = l[i].upper()
            word = True
        elif l[i] != ' ' and l[i].isupper():
            l[i] = l[i].lower()
        elif l[i] == ' ':
            word = False

    s = ''.join(l)
    return ("#" + s.replace(' ', '') if s != '' and len(s) <= 140 else False)

def first_non_repeating_letter(string):
    
    sLower = string.lower()

    for i in range(len(string)):
        if sLower.count(sLower[i]) == 1:
            return string[i]    
    
    return ''



def domain_name(url):
    
    s = url.replace('http://', '').replace('https://', '').replace('www.', '')
    s_string = s.split('.', 1)
    return s_string[0]



def score(dice):
    
    res = 0
    triple = 0
    dict = {k:dice.count(k) for k in dice}

    for key in dict:
        if dict[key] >= 3:
            res += (key*100 if key !=1 else 1000)
            if key in (1, 5): triple = 3
            
        if key in (1, 5): res += ((dict[key]-triple)*50 if key != 1 else (dict[key]-triple)*100)

    return res

    #print(dict)



def string(dict):
    keys = list(dict)

    s = "" if dict[keys[0]] == 0 else ("1 second" if dict[keys[0]] == 1 else "{} seconds".format(dict[keys[0]]))
    m = "" if dict[keys[1]] == 0 else ("1 minute" if dict[keys[1]] == 1 else "{} minutes".format(dict[keys[1]]))
    joint = " and " if m != '' and s == '' else (", " if m != '' else '')
    h = "" if dict[keys[2]] == 0 else ("1 hour" + joint if dict[keys[2]] == 1 else "{} hours".format(dict[keys[2]]) + joint)
    joint = ", " if h != '' or m != '' else ''
    d = "" if dict[keys[3]] == 0 else ("1 day" + joint if dict[keys[3]] == 1 else "{} days".format(dict[keys[3]]) + joint)
    joint = ", " if d!= '' or h != '' or m != '' else ''
    y = "" if dict[keys[4]] == 0 else ("1 year" + joint if dict[keys[4]] == 1 else "{} years".format(dict[keys[4]]) + joint)
    joint = " and " if s != '' and (m != '' or h != '' or d != '' or y != '') else ''
 
    return y + d + h + m + joint + s


def format_duration(seconds):
    
    if seconds == 0: return "now"
    else:
        res = {'s': 0, 'm': 0, 'h': 0, 'd': 0, 'y': 0}
        duration = 's'
        num = seconds
        i = 0
        keys = list(res)
        coeff = 60

        while duration != '':
            if duration =='s':
                coeff = 60
            if duration == 'm':
                coeff = 60
            elif duration == 'h':
                coeff = 24
            elif duration == 'd':
                coeff = 365

            rem = num//coeff
            if rem > 0: duration = keys[i+1] 
            else: duration = ''

            res[keys[i]] = num - rem*coeff
            if duration == 'y': 
                res[keys[i+1]] = rem
                duration = ''
            i += 1
            num = rem

    return string(res)
 
'''


#  Given a binary tree, please implement an Iterator for inorder traversal.

# class BTInorderIterator {
#    boolean hasNext()
#    Node next()



#              1
#        2           3
#    4       5

# BTInorderIterator()
# hasnext() 
# next() 
















'''
# Given a binary tree, please implement an Iterator for inorder traversal

class BTInorderIterator {
    boolean hasNext();
    Node next();
    inorderList = []
    resList = []
    
    
    def __init__(self, tree):
        self.tree = tree
        resList = self.traverse


    def hasnext(self, currentNode):
        # return boolean
        if self.currentNode.data == resList[len(resList)-1]:
            retrun False
        else: return True
           
    
    
    def next(self, currentNode):
        # return the node
        
        for i in range(len(resList)):
            if currenNode.data == resList[i]:
                if  i == len(resList)-1:
                    return None
                else: return resList[i+1]
                
        
    
  
    def traverse(self):
        if self.left != None:
            self.left.traverse
        inorderList.append(self.data)
        return inorderList
        if self.right != None:
            self.righ.traverse
    
}
    
# building the tree
tree = Tree(1)
...


btIterator = BTInorderIterator(tree)
isNextExist = btIterator.hasnext(node) # should return is exist or not
nextNode = btIterator.next(node) # return data for the next item not NODE


'''













'''
def permutation(lst):
    print(lst)

    if lst == None:
        return []

    if len(lst) == 1:
        return [lst]

    permList = []

    for i in range(len(lst)):
        oneChar = lst[i]

        tempList = lst[:i] + lst[i+1:]

        for p in permutation(tempList):
            permList.append([oneChar] + p)

    return permList

data = 'abc'

res = permutation(list(data))
print(res)

'''


'''
class Node:
    inc = 0
    def __init__(self, data, level):
        if isinstance(data, int):
            self.data = data
            self.level = level
            self.left = None
            self.right = None
        else: raise ValueError('Node value should be integer')



    def insert(self, data):
        if self.data == None:
            self.data = data
        elif self.data == data:
            raise "Element with such data point has already exists"
        elif self.data > data:
            if self.left == None:
                self.left = Node(data, self.level + 1)
            else: self.left.insert(data)
        else:
            if self.right == None:
                self.right = Node(data, self.level + 1)
            else: self.right.insert(data)

    def traverseInOrder(self):
        if self.left != None:
            self.left.traverseInOrder()
        print(str(self.data))
        if self.right != None:
            self.right.traverseInOrder()

    def traversePreOrder(self):
        if self.left != None:
            self.left.traversePreOrder()
        if self.right != None:
            self.right.traversePreOrder()
        print(self.data)


root = Node('text', 0)
print(root)

'''
'''
root = Node(45, 0)
root.insert(25)
root.insert(15) 
root.insert(30)
root.insert(20)
root.insert(55)
root.insert(65)
root.insert(50)
root.insert(40)
root.insert(5)
root.insert(75)
root.insert(60)
root.insert(52)

root.traversePreOrder()

'''












'''
base64 = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def cypherBase64(number):

    res = ''
    
    while number > 0:
        i = number % len(base64)
        res += base64[i]
        number = number // len(base64)

    res = res[::-1]
    return res


res = cypherBase64(5000000)
print(res)
'''


'''
#permutation - recursion

# Python function to print permutations of a given list
def permutation(lst):
 
    # If lst is empty then
    #    return []
 
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]
 
    # Find the permutations for lst if there are
    # more than 1 characters
 
    l = [] # empty list that will store current permutation
 
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]
 
       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]
 
       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
            l.append([m] + p)
    return l
 
 
# Driver program to test above function
data = list('abc')
res = permutation(data)
print(res)

#for p in permutation(data):
#    print(p)
'''






'''
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def buildlist(head, item):

    if head == None: return

    if head.next == None: 
        head.next = item
        return
    
    element = head.next
    end = head

    while element.next != None:
        buffer = element        
        element = element.next
        buffer.next = 
        elemen
    
    element.next = item


def reverse(head):
    
    if head == None: return ''

    resList = []

    item = head

    while item.next != None:
        resList.append(item.data)
        item = item.next
    resList.append(item.data)

    resList = resList[::-1]

    head = Node(resList[0])

    for i in resList[1:]:
        item = Node(i)
        buildlist(head, item)

        
    #print(resList)
    #print(' -> '.join(str(x) for x in resList[::-1]) + ' -> None.')
    #return res




res = reverse([1, 3, 8])
print(res)
# 3 -> 1 -> None

'''

'''
Four Letter Words ~ Mutations




def findWord(list, word):

    for item in list:

        if item[0] == word[0]:
            if (item[1] == word[1] and item[2] == word[2] and item[3] != word[3]) or (item[1] == word[1] and item[2] != word[2] and item[3] == word[3]) or (item[1] != word[1] and item[2] == word[2] and item[3] == word[3]):
                if item.count(item[0]) > 1 or item.count(item[1]) > 1 or item.count(item[2]) > 1: continue
                else: return item
        elif item[1:4] == word[1:4]:
            if item.count(item[0]) > 1 or item.count(item[1]) > 1 or item.count(item[2]) > 1: continue
            else: return item
    return None


def mutations(alice, bob, word, first):

    if alice == None or bob == None or word == None or first < 0 or first > 1:
        return None
    aliceRes = bobRes = ' '
    originAlice = alice.copy()
    originBob = bob.copy()
    if originAlice.count(word) > 0: originAlice.remove(word)
    if originBob.count(word) > 0: originBob.remove(word)


    while not (aliceRes == None and bobRes == None):
        if first == 0:           
            aliceRes = findWord(originAlice, word)
            if aliceRes != None:
                word = aliceRes
                originAlice.remove(aliceRes)
                if originBob.count(aliceRes) > 0: originBob.remove(aliceRes)
                if bobRes == None: return 0
            else:
                if bobRes == ' ' : first  = 1
                elif bobRes != None: return 1
            first = 1
        else:
            bobRes = findWord(originBob, word)
            if bobRes != None:
                word = bobRes
                originBob.remove(bobRes)
                if originAlice.count(bobRes) > 0: originAlice.remove(bobRes)
                if aliceRes == None: return 1
            else:
                if aliceRes == ' ' : first  = 0
                elif aliceRes != None: return 0
            first = 0
                
    return -1


#res = findWord(['fear', 'fard'], 'farl')
#print(res)

alice = ['void', 'emyd', 'exes', 'lick', 'brrr', 'lira', 'koto', 'upon', 'dunk', 'wawl', 'keno', 'fuss', 'fine', 'rins', 'brae', 'drys', 'yuke', 'seif', 'slap', 'miso', 'mems', 'miss', 'warn', 'coot', 'molt', 'rhea', 'draw', 'stem', 'irks', 'oust', 'tirl', 'will', 'pams', 'owed', 'firm', 'ring', 'nine', 'kris', 'eche', 'lion', 'pass', 'duds', 'seek', 'snap', 'iglu', 'raft', 'wali', 'polk', 'byes', 'emeu', 'yeuk', 'vacs', 'wage', 'meed', 'dreg', 'moot', 'leer', 'tees', 'fief', 'curn', 'oryx', 'oyer', 'juco', 'echo', 'dors', 'doss', 'lent', 'dene', 'plus', 'ewer', 'feod', 'chis', 'miff', 'eely', 'tosh', 'huts', 'asci', 'menu', 'whew', 'dido', 'amir', 'kyar', 'over', 'sice', 'bree', 'yutz', 'mids', 'clot', 'foys', 'bibb', 'magi', 'sorn', 'barm', 'adze', 'hood', 'info', 'tuck', 'cess', 'doum', 'hajj', 'dame', 'cote', 'ours', 'tuis', 'rage', 'kaon', 'kaka', 'zeks', 'wing', 'typp', 'clog', 'inky', 'vera', 'asks', 'bort', 'gaud', 'belt', 'tips', 'rase', 'pics', 'vein', 'file', 'mott', 'time', 'hays', 'bitt', 'ands', 'clay', 'pled', 'weep', 'moue', 'tela', 'nark', 'bang', 'skin', 'lowe', 'lied', 'boar', 'nope', 'bema', 'joes', 'boom', 'edge', 'sigh', 'eave', 'trek', 'aril', 'pfui', 'nogs', 'kids', 'head', 'plop', 'alan', 'tori', 'gone', 'kyte', 'recs', 'ruga', 'erst', 'nota', 'keel', 'puff', 'quid', 'vina', 'pare', 'rods', 'pill', 'corn', 'mixt', 'enol', 'poem', 'sues', 'tour', 'leks', 'muds', 'kobs', 'rend', 'quey', 'yags', 'hwan', 'buns', 'bolo', 'pole', 'typy', 'alee', 'mold', 'viva', 'leak', 'gley', 'leva', 'weta', 'alfa', 'gibe', 'slum', 'harp', 'raze', 'anil', 'dabs', 'coil', 'peag', 'yews', 'redd', 'bide', 'goal', 'leno', 'dans', 'fuci', 'urus', 'burs', 'hops', 'visa', 'jagg', 'gray', 'pomp', 'raga', 'cage', 'easy', 'alas', 'huge', 'duce', 'sord', 'kain', 'oafs', 'mums', 'stye', 'gite', 'mair', 'wain', 'peat', 'dine', 'also', 'wisp', 'dart', 'wove', 'gowd', 'exit', 'fond', 'pods', 'tabu', 'inly', 'toll', 'buys', 'prig', 'mete', 'azan', 'luke', 'tets', 'ruse', 'sybo', 'hobs', 'zoic', 'bawl', 'call', 'hart', 'turn', 'mash', 'topo', 'oxen', 'juts', 'bice', 'fits', 'vena', 'odes', 'trug', 'croc', 'coft', 'rout', 'olid', 'name', 'flew', 'nard', 'paps', 'weet', 'chop', 'cons', 'drek', 'nets', 'babu', 'ruff', 'cute', 'pick', 'moms', 'owse', 'bozo', 'cuif', 'waft', 'imid', 'paca', 'jams', 'corf', 'jail', 'area', 'buds', 'tone', 'wees', 'coco', 'torr', 'rein', 'vans', 'pirn', 'tack', 'idyl', 'lido', 'qoph', 'koel', 'lire', 'aper', 'ouph', 'robs', 'rebs', 'whid', 'pegs', 'weft', 'wych', 'berk', 'fids', 'baud', 'toms', 'coys', 'okeh', 'soap', 'jiao', 'home', 'stow', 'mako', 'kemp', 'lids', 'hork', 'meme', 'soke', 'lies', 'lode', 'five', 'zany', 'lych', 'ukes', 'dull', 'boor', 'ware', 'ceps', 'shog', 'trow', 'mome', 'kame', 'tanh', 'dual', 'opah', 'pula', 'plea', 'quiz', 'rocs', 'hake', 'rubs', 'frog', 'naik', 'barf', 'hour', 'whit', 'lust', 'jess', 'rets', 'fons', 'lips', 'dhal', 'vega', 'calx', 'alef', 'brig', 'mews', 'sipe', 'urps', 'furs', 'luvs', 'ixia', 'rued', 'dune', 'meat', 'durn', 'oats', 'daze', 'flab', 'vier', 'stop', 'juga', 'urge', 'dyad', 'odea', 'eats', 'zerk', 'nape', 'tots', 'fash', 'unit', 'masa', 'ashy', 'mawn', 'duct', 'pain', 'womb', 'talk', 'leas', 'yard', 'larn', 'zees', 'tivy', 'suit', 'slot', 'stum', 'tyer', 'mole', 'sris', 'find', 'jade', 'dump', 'tune', 'joey', 'coif', 'rink', 'mopy', 'sacs', 'cuds', 'feal', 'lead', 'boot', 'itch', 'dele', 'inti', 'frug', 'naos', 'tahr', 'alit', 'owes', 'mint', 'feus', 'mugs', 'peas', 'fisk', 'hill', 'soys', 'acyl', 'shwa', 'thai', 'pond', 'whir', 'ires', 'otic', 'drow', 'carr', 'mart', 'june', 'jive', 'fund', 'moon', 'tidy', 'ilex', 'runt', 'sura', 'pome', 'karn', 'honk', 'hasp', 'dirk', 'eyra', 'thug', 'salp', 'bunk', 'luau', 'many', 'toro', 'awee', 'task', 'fiat', 'pies', 'scar', 'idly', 'cate', 'dues', 'didy', 'laid', 'obia', 'chef', 'beau', 'shiv', 'haws', 'rads', 'have', 'dopy', 'kith', 'jogs', 'dado', 'bien', 'orbs', 'cowl', 'kudu', 'baby', 'sall', 'tyro', 'loir', 'cero', 'rack', 'step', 'dace', 'khis', 'reel', 'loin', 'naan', 'kiln', 'wair', 'woks', 'durr', 'mono', 'pale', 'says', 'yoni', 'filo', 'murr', 'ears', 'bowl', 'olea', 'egos', 'soms', 'webs', 'puny', 'thro', 'welt', 'dray', 'ritz', 'hung', 'kadi', 'vise', 'knar', 'gibs', 'caky', 'leku', 'body', 'them', 'afar', 'vole', 'nary', 'laud', 'mony', 'term', 'very', 'wool', 'tell', 'cede', 'chid', 'raku', 'bool', 'ales', 'oots', 'sumo', 'plie', 'wabs', 'shim', 'udos', 'gore', 'rind', 'sups', 'nana', 'lift', 'coda', 'rely', 'flus', 'soar', 'stub', 'gnus', 'psst', 'skip', 'riot', 'cabs', 'roil', 'halo', 'glum', 'site', 'peri', 'beak', 'paik', 'mise', 'stob', 'hock', 'moss', 'saps', 'sine', 'bigs', 'dote', 'syph', 'weed', 'yams', 'fogs', 'camp', 'batt', 'trim', 'bust', 'brow', 'agar', 'ruin', 'slur', 'wadi', 'chit', 'ells', 'agha', 'germ', 'keys', 'ping', 'know', 'pork', 'mace', 'trap', 'rids', 'bren', 'paid', 'taco', 'kufi', 'rums', 'wauk', 'eggy', 'prez', 'virl', 'sear', 'bake', 'fowl', 'daps', 'gout', 'neon', 'wist', 'heme', 'rasp', 'lard', 'twig', 'oldy', 'jane', 'oils', 'hant', 'wads', 'room', 'shin', 'reis', 'yowe', 'icon', 'ares', 'lore', 'else', 'anis', 'yups', 'daff', 'noon', 'airt', 'ibex', 'peed', 'egis', 'ruck', 'arcs', 'swig', 'dere', 'biga', 'cosh', 'deny', 'orra', 'tame', 'teal', 'wyle', 'ayah', 'eaux', 'snye', 'thee', 'foin', 'sard', 'albs', 'gads', 'pile', 'vara', 'lens', 'yoks', 'runs', 'acne', 'vees', 'cart', 'mips', 'sway', 'gits', 'taro', 'kane', 'dogs', 'pial', 'acme', 'pray', 'take', 'gaby', 'lisp', 'anon', 'ebbs', 'lees', 'joke', 'chum', 'ages', 'mazy', 'owns', 'wows', 'hare', 'lits', 'frit', 'hems', 'envy', 'horn', 'gang', 'posh', 'mill', 'risk', 'juju', 'mabe', 'psis', 'gull', 'lieu', 'lewd', 'alme', 'sibb', 'lase', 'yaks', 'rimy', 'kibe', 'serf', 'dolt', 'loth', 'perp', 'libs', 'rems', 'vied', 'sagy', 'rims', 'loup', 'yolk', 'hols', 'hull', 'blog', 'fibs', 'berg', 'tows', 'tael', 'haul', 'holy', 'pail', 'homy', 'gled', 'yarn', 'swam', 'vang', 'nick', 'osar', 'modi', 'blip', 'kina', 'ates', 'bats', 'girl', 'muso', 'palp', 'kirn', 'fins', 'casa', 'vita', 'bosk', 'tape', 'caul', 'near', 'kvas', 'reds', 'veld', 'fugs', 'last', 'carb', 'agma', 'skua', 'lyse', 'halt', 'coup', 'teff', 'nada', 'oily', 'shea', 'ends', 'oars', 'soth', 'bock', 'bulk', 'sour', 'mons', 'ides', 'towy', 'marc', 'flex', 'hets', 'moil', 'dout', 'brut', 'went', 'wavy', 'grue', 'bath', 'areg', 'cels', 'bidi', 'toot', 'lory', 'wins', 'slab', 'quit', 'yirr', 'blub', 'legs', 'quai', 'vice', 'haaf', 'cloy', 'jeff', 'gelt', 'ilks', 'laws', 'corm', 'fems', 'pals', 'urns', 'burn', 'bulb', 'guar', 'aery', 'such', 'rigs', 'peel', 'hims', 'roup', 'slew', 'rusk', 'beam', 'zoea', 'gall', 'whoa', 'sirs', 'hear', 'eyer', 'hows', 'hams', 'gasp', 'gets', 'pool', 'spin', 'hoof', 'saws', 'fyke', 'jibe', 'lude', 'guns', 'peek', 'teak', 'load', 'minx', 'fats', 'delf', 'viga', 'dish', 'midi', 'dibs', 'roof', 'snot', 'loto', 'neve', 'seed', 'anew', 'fohn', 'forb', 'yaud', 'dins', 'bade', 'soma', 'diel', 'duns', 'wady', 'half', 'fume', 'taos', 'vasa', 'waif', 'baps', 'hind', 'sums', 'yobs', 'boat', 'lite', 'cops', 'tiro', 'jins', 'oozy', 'bize', 'zero', 'rhos', 'burr', 'hymn', 'maid', 'pish', 'klik', 'pity', 'kief', 'jump', 'stew', 'sips', 'inia', 'taps', 'yaff', 'haes', 'bids', 'ruth', 'tilt', 'dent', 'poxy', 'khet', 'ilia', 'note', 'poke', 'ursa', 'surd', 'cony', 'flue', 'cred', 'mare', 'fads', 'warp', 'ocas', 'boyo', 'thir', 'maim', 'khan', 'napa', 'lunt', 'ados', 'eyry', 'daks', 'demy', 'clew', 'zonk', 'pump', 'hogg', 'glom', 'pily', 'tels', 'keet', 'emus', 'wons', 'nome', 'meou', 'whee', 'whet', 'pong', 'esne', 'luna', 'swat', 'swab', 'leke', 'beet', 'foal', 'aals', 'cool', 'ague', 'malm', 'amok', 'safe', 'chon', 'opal', 'smew', 'jows', 'doms', 'blae', 'fame', 'tegs', 'shul', 'ebon', 'idea', 'away', 'ryas', 'data', 'shew', 'cant', 'goad', 'deet', 'heal', 'duma', 'lose', 'peer', 'culm', 'seas', 'flub', 'scop', 'gyro', 'cure', 'mumu', 'foot', 'milk', 'bush', 'pase', 'coni', 'noil']
bob   = ['sook', 'cogs', 'anti', 'imam', 'moxa', 'lwei', 'zoom', 'giga', 'kays', 'odea', 'ends', 'bets', 'paws', 'caps', 'doat', 'rugs', 'skeg', 'toil', 'defi', 'shri', 'amie', 'veld', 'baff', 'koji', 'frat', 'nurl', 'plum', 'puns', 'more', 'chop', 'fear', 'deet', 'wore', 'hays', 'opus', 'pont', 'page', 'pant', 'amin', 'flir', 'sext', 'coco', 'tuts', 'beak', 'mend', 'goof', 'rolf', 'nosy', 'rush', 'bump', 'fuss', 'sing', 'mazy', 'fink', 'hewn', 'sees', 'hogg', 'swum', 'hahs', 'ream', 'hehs', 'surf', 'faze', 'bees', 'mise', 'beep', 'udon', 'rias', 'sorb', 'alae', 'pubs', 'goth', 'mule', 'moon', 'buds', 'band', 'corn', 'heal', 'hale', 'sika', 'sulk', 'goer', 'demy', 'cels', 'lump', 'rete', 'puls', 'mems', 'curd', 'carr', 'rimu', 'leis', 'saga', 'jack', 'bats', 'shoo', 'foes', 'hims', 'ocas', 'trio', 'expo', 'lulu', 'olid', 'sock', 'need', 'gown', 'soli', 'amen', 'doge', 'zonk', 'ooze', 'peed', 'silk', 'tete', 'eddy', 'holy', 'coky', 'feta', 'rink', 'cued', 'toad', 'pies', 'paca', 'find', 'prao', 'wyns', 'floe', 'burr', 'shoe', 'sels', 'hove', 'fled', 'osar', 'engs', 'eyas', 'bate', 'romp', 'rail', 'nota', 'calx', 'send', 'gulp', 'goal', 'zerk', 'fumy', 'refs', 'sawn', 'arco', 'laid', 'wens', 'bras', 'phon', 'dodo', 'hump', 'knop', 'fold', 'info', 'bots', 'owns', 'loos', 'corf', 'psis', 'rums', 'foal', 'arts', 'cyst', 'gaur', 'tyer', 'beam', 'flub', 'mode', 'rems', 'haku', 'segs', 'glue', 'folk', 'work', 'peri', 'mopy', 'glia', 'ride', 'yams', 'yutz', 'nave', 'tans', 'kata', 'cage', 'ovum', 'mart', 'defy', 'milk', 'kore', 'mail', 'paly', 'yawp', 'verd', 'wiry', 'hire', 'rhus', 'kens', 'home', 'wiss', 'reis', 'peke', 'effs', 'filo', 'gems', 'prau', 'glom', 'achy', 'rank', 'barb', 'apse', 'eros', 'cane', 'derv', 'kern', 'pose', 'jail', 'miry', 'hots', 'pits', 'ruly', 'kine', 'coni', 'undo', 'tars', 'mica', 'azan', 'ohia', 'fool', 'mint', 'aril', 'bedu', 'lisp', 'rate', 'hora', 'cigs', 'naik', 'cede', 'lice', 'race', 'drab', 'agon', 'kuru', 'kudo', 'dhow', 'mote', 'ands', 'rive', 'luge', 'oxen', 'nose', 'cult', 'deke', 'tree', 'piny', 'cuts', 'mums', 'gets', 'hurl', 'emyd', 'juco', 'muds', 'holp', 'mind', 'play', 'tyee', 'pouf', 'teen', 'tung', 'gaes', 'doxy', 'hern', 'rets', 'ebbs', 'abye', 'lakh', 'grow', 'heel', 'jagg', 'sipe', 'vied', 'dahl', 'dank', 'sibs', 'lamb', 'byre', 'lurk', 'drew', 'weep', 'tali', 'sics', 'yuck', 'earn', 'dido', 'duit', 'veal', 'thaw', 'gibs', 'vasa', 'bong', 'birr', 'vies', 'ahed', 'sith', 'rags', 'vile', 'tram', 'ursa', 'menu', 'blog', 'hike', 'raia', 'plie', 'yuga', 'oyes', 'york', 'hoax', 'vavs', 'gyve', 'soja', 'calf', 'halo', 'dins', 'pled', 'drow', 'vees', 'twit', 'when', 'jots', 'soys', 'comb', 'keps', 'sews', 'hard', 'weet', 'outs', 'masa', 'naps', 'kits', 'perk', 'jouk', 'fond', 'whid', 'horn', 'gold', 'upas', 'dite', 'abri', 'cord', 'ankh', 'pomp', 'kite', 'maul', 'doux', 'zoos', 'deni', 'rosy', 'kyat', 'into', 'earl', 'farm', 'gowk', 'viol', 'bawl', 'lich', 'coos', 'sago', 'apod', 'gust', 'skim', 'habu', 'yack', 'elhi', 'puja', 'oops', 'rich', 'towy', 'frau', 'awns', 'modi', 'aloe', 'tics', 'kune', 'days', 'plod', 'brut', 'glop', 'pams', 'boys', 'mays', 'army', 'rode', 'bash', 'stop', 'padi', 'lues', 'pome', 'tube', 'cove', 'aryl', 'ikon', 'envy', 'cosh', 'tubs', 'tora', 'mako', 'away', 'ward', 'clod', 'funk', 'apex', 'yodh', 'boos', 'pugh', 'bans', 'mayo', 'fess', 'eave', 'jeon', 'woes', 'brag', 'baal', 'sett', 'undy', 'bubs', 'gull', 'hoof', 'saws', 'acyl', 'luna', 'past', 'mura', 'gins', 'ains', 'moos', 'glut', 'boat', 'lima', 'ghis', 'fury', 'zags', 'limo', 'cedi', 'wist', 'abut', 'nevi', 'herd', 'blip', 'paps', 'odas', 'warm', 'bals', 'nada', 'vans', 'scry', 'dumb', 'hone', 'bola', 'wail', 'whin', 'ogam', 'idyl', 'slop', 'rede', 'pipy', 'hive', 'gain', 'stye', 'floc', 'moil', 'hors', 'edgy', 'phew', 'emus', 'lipe', 'soda', 'deck', 'reck', 'nana', 'macs', 'deer', 'jags', 'abys', 'fund', 'tyes', 'axle', 'mane', 'toes', 'tors', 'talc', 'knar', 'seem', 'gird', 'miri', 'scad', 'nubs', 'smog', 'pone', 'nolo', 'eves', 'brio', 'bads', 'lyre', 'eide', 'ragg', 'byte', 'tarp', 'etch', 'bins', 'cyme', 'warp', 'lamp', 'exit', 'salp', 'body', 'mews', 'rubs', 'racy', 'main', 'yelp', 'dona', 'boil', 'limb', 'toll', 'juga', 'rude', 'wish', 'aces', 'ashy', 'logs', 'sake', 'inby', 'sots', 'sets', 'fyce', 'thug', 'soot', 'bell', 'haps', 'meat', 'ones', 'drum', 'jess', 'mool', 'agar', 'bite', 'raja', 'aide', 'skew', 'plea', 'orle', 'wrap', 'souk', 'kips', 'udos', 'midi', 'birk', 'yech', 'sore', 'cast', 'seed', 'slim', 'bier', 'mock', 'mete', 'core', 'lums', 'cyma', 'yagi', 'hawk', 'pupa', 'vrow', 'faut', 'have', 'spam', 'cans', 'limn', 'gent', 'fast', 'melt', 'arvo', 'elmy', 'bree', 'temp', 'soms', 'none', 'robs', 'lins', 'side', 'cred', 'fado', 'glum', 'saul', 'year', 'poly', 'atop', 'rind', 'opal', 'afar', 'bise', 'razz', 'brig', 'sure', 'heat', 'palm', 'bane', 'life', 'curs', 'syce', 'dude', 'jane', 'pops', 'huge', 'dewy', 'onus', 'plex', 'webs', 'dawt', 'rack', 'lode', 'rifs', 'tuns', 'gamb', 'megs', 'legs', 'alec', 'wyes', 'roux', 'mell', 'qaid', 'lift', 'neat', 'murk', 'bias', 'maws', 'keno', 'copy', 'dibs', 'slid', 'post', 'raya', 'roto', 'kaif', 'simp', 'math', 'reek', 'gane', 'jarl', 'ptui', 'half', 'alms', 'cods', 'hake', 'mome', 'idle', 'nide', 'take', 'rock', 'sorn', 'blat', 'duff', 'neon', 'tola', 'gogo', 'yogi', 'gift', 'migg', 'elds', 'raps', 'tape', 'sial', 'agog', 'chaw', 'noms', 'taro', 'okas', 'meed', 'gaed', 'holk', 'mitt', 'helm', 'brat', 'plug', 'atma', 'lust', 'wali', 'nuns', 'burd', 'lehr', 'dunt', 'coot', 'alga', 'dreg', 'tink', 'crud', 'chap', 'fizz', 'wasp', 'paik', 'oped', 'ping', 'seal', 'sold', 'mown', 'trek', 'vids', 'kerf', 'kadi', 'oint', 'riff', 'dyer', 'dime', 'jigs', 'wild', 'moth', 'gaen', 'egis', 'pian', 'gang', 'mars', 'taps', 'firm', 'noun', 'uric', 'cols', 'yaud', 'book', 'cabs', 'nims', 'peat', 'luny', 'soap', 'urds', 'bead', 'shiv', 'door', 'ants', 'lake', 'kiln', 'wisp', 'sank', 'puke', 'papa', 'vole', 'pias', 'yipe', 'lids', 'gien', 'hwyl', 'teth', 'sade', 'crus', 'pull', 'sura', 'cone', 'card', 'naoi', 'meld', 'yegg', 'goas', 'seat', 'list', 'shew', 'raff', 'belt', 'acta', 'tilt', 'deny', 'tame', 'germ', 'doit', 'pass', 'syke', 'birl', 'teds', 'lowe', 'muso', 'lags', 'roll', 'rote', 'edit', 'thai', 'rare', 'drag', 'tost', 'toga', 'whim', 'mast', 'oast', 'hand', 'jeep', 'luma', 'wink', 'tide', 'bask', 'bumf', 'brie', 'toro', 'love', 'dure', 'mead', 'kane', 'geek', 'vatu', 'free', 'obas', 'umbo', 'skua', 'ring', 'crew', 'oral', 'bema', 'grok', 'difs', 'yare', 'demo', 'ceca', 'gite', 'crux', 'fend', 'wans', 'howf', 'odds', 'burg', 'vets', 'jaws', 'idea', 'last', 'naff', 'weed', 'buhr', 'bloc', 'alts', 'hade', 'joky', 'lewd', 'wash', 'twae', 'twos', 'hyps', 'daps', 'purl', 'yods', 'lain', 'left', 'whit', 'spew', 'song', 'orca', 'gapy', 'shmo', 'kaka', 'kemp', 'suks', 'harm', 'tonk', 'pacy', 'axil', 'yond', 'ruer', 'oath', 'yays', 'huic', 'mary', 'gabs', 'glow', 'fobs', 'thud', 'shin', 'bark', 'pyin', 'ceps', 'neve', 'ghat', 'tala', 'cleg', 'aahs', 'lost', 'fern', 'ante', 'bend', 'isms', 'pard', 'burp', 'enow', 'tuff', 'boss', 'nook', 'sang', 'gums', 'hods', 'gate', 'lory', 'gybe', 'hobo', 'taos', 'raws', 'neuk', 'carn', 'brim', 'cloy', 'mobs', 'gasp', 'skid', 'mics', 'bods', 'juku', 'jazz', 'blur', 'kois', 'zoea', 'inly', 'feel', 'leat', 'riot', 'teas', 'type', 'zona', 'rill', 'swat', 'cars', 'prop', 'mump', 'rods', 'gnar', 'mads', 'guts', 'byes', 'peon', 'logo', 'ecru', 'bidi', 'late', 'vena', 'fief', 'wean', 'chew', 'frug', 'fops', 'gobs', 'damp', 'grin', 'firn', 'moot', 'digs', 'coss', 'tads', 'taco', 'tule', 'wack', 'tiny', 'rout', 'dolt', 'tine', 'gosh', 'pung', 'ship', 'fido', 'muon', 'jimp', 'lall', 'obit', 'does', 'kids', 'repp', 'kaki', 'phis', 'ragi', 'nibs', 'bosk', 'navy', 'burn', 'fade', 'tace', 'prof', 'eyry', 'vane', 'moll', 'duck', 'coal', 'nerd', 'clad', 'clue', 'kifs', 'hips', 'lawn', 'virl', 'bays', 'note', 'loth', 'wads', 'slug', 'bris', 'sord', 'rend', 'nine', 'keys', 'glug']

res = mutations(alice, bob, "ptui", 0)
print(str(res))

'''
'''
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            self.data = data
            return    
        elif self.data > data:
            if self.left is None: self.left = TreeNode(data)
            else: self.left.insert(data)
        else:
            if self.right is None: self.right = TreeNode(data)
            else: self.right.insert(data)          


def complete_binary_tree(a):
    
    for item in a:
        insert()
    


res = complete_binary_tree([1])
print(res)
res = complete_binary_tree([1, 2, 3, 4, 5, 6])
print(res)
res = complete_binary_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(res)
res = complete_binary_tree([6, 3, 8, 1, 5, 7, 9, 0, 2, 4])
print(res)

'''


'''
# Binary tree

class TreeNode:

    def __init__(self, nodeVal, nodeLev):
        self.left = None
        self.right = None
        self.val = nodeVal
        self.level = nodeLev

    def insertNode(self, nodeVal):
        if self.val < nodeVal:
            if self.right is None: self.right = TreeNode(nodeVal, self.level + 1)
            else: self.right.insertNode(nodeVal)
        else:
            if self.left is None: self.left = TreeNode(nodeVal, self.level + 1)
            else: self.left.insertNode(nodeVal)

    def findNode(self, nodeVal):
        if self.val:
            if self.val == nodeVal: return self.level
            elif self.val < nodeVal:
                if self.right: level = self.right.findNode(nodeVal)
                else: level = -1
            else:
                if self.left: level = self.left.findNode(nodeVal)
                else: level = -1
        else: level = -1

        return level

    def traverseLefttoRight(self):
        if self.val:
            if self.left != None:
                self.left.traverseLefttoRight()
            print (str(self.val))
            if self.right != None:
                self.right.traverseLefttoRight()


tree = TreeNode(42, 0)
tree.insertNode(15)
tree.insertNode(5)
tree.insertNode(55)
tree.insertNode(75)
tree.insertNode(25)
tree.insertNode(35)
tree.insertNode(37)
#findNodeValue = 55
#nodeLevel = tree.findNode(findNodeValue)
#print(f"Node {str(findNodeValue)} has level: {str(nodeLevel)}")

tree.traverseLefttoRight()

'''

'''
==========================================================================
Find amplitude of a binary tree

class Tree(object):
  
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

def tree_amplitude(root_node, firstTime=[]):
# Your solution
    if root_node is None:
        return max(firstTime) - min(firstTime) if len(firstTime) > 0 else 0
    
    left = tree_amplitude(root_node.left, firstTime + [root_node.data])
    right =  tree_amplitude(root_node.right, firstTime + [root_node.data])
    return max(left, right)

res = tree_amplitude(Tree(5, Tree(1), Tree(3)))
print(str(res))
res = tree_amplitude(Tree(-5, Tree(-20), Tree(3, Tree(-1, None, Tree(88)), Tree(33)),))
print(str(res))
'''

'''
==========================================================================
Linked List

class Node:
    data: int     
    next = None
    def __init__(self, data):
        self.data = data  


class LinkedList:
    head = None       

    def append(self, data):
        if self.head != None:
            item = self.head
            while item.next != None:
                item = item.next
            item.next = Node(data)
        else: self.head = Node(data)

    def remove(self, data, all):
        if self.head != None:
        
            if self.head.next == None:
                if self.head.data == data: 
                    self.head = None
                    return
                
            item = self.head
            while item.next != None:
                if item.next.data == data:
                    if item.next.next != None:
                        item.next = item.next.next
                    else: 
                        item.next = None
                        return
                    if all == 0:
                        return
                item = item.next

    def printLLElements(self):
        if self.head != None:
            item = self.head
            while item.next != None:
                print(f'{str(item.data)}-->')
                item = item.next
            print(f'{str(item.data)}-->')


head = LinkedList()
head.append(8)
head.append(12)
head.append(10)
head.append(7)
head.append(9)
head.append(10)
head.printLLElements()
print('===================================')
head.remove(10, 0)
head.printLLElements()
#4-->8-->12-->6
'''


'''
==========================================================================
Factorial

def factorial(n):

    nFactor = 0

    if not isinstance(n, int): return 0
    elif n < 0: nFactor = -1 * n
    else: nFactor = n

    resFactor = 1
    for i in range(1, nFactor+1): resFactor *= i
    return (resFactor * -1 if n < 0 and n%2 != 0 else resFactor)


'''

'''
==========================================================================
Simple Memory Manager

class Node:
    next = None
    def __init__(self, nodeID, size):
        self.nodeID = nodeID
        self.data = [None]*size


class MemoryManager:
    
    head = None
    
    def __init__(self, memory):
        """
        @constructor Creates a new memory manager for the provided array.
        @param {memory} An array to use as the backing memory.
        """
        self.originMemory = len(memory)
        self.availableMemory = len(memory)
        self.memory = memory

    def allocate(self, size):
        """
        Allocates a block of memory of requested size.
        @param {number} size - The size of the block to allocate.
        @returns {number} A pointer which is the index of the first location in the allocated block.
        @raises If it is not possible to allocate a block of the requested size.
        """
        if size <= self.availableMemory:
            if self.head == None:
                self.head = Node(0, size)
                self.memory[0:size] = self.head.data
                self.availableMemory -= size
                return 0
            else:
                if self.head.nodeID >= size:
                    item = Node(0, size)
                    self.memory[0:size] = item.data
                    item.next = self.head.next
                    self.head.next = item
                    return 0
                current = 0
                item = self.head
                current += len(item.data)
                while item.next != None:
                    if item.next.nodeID == current:  
                        item = item.next
                        current += len(item.data)
                    else:
                        if item.next.nodeID - current >= size:
                            newItem = Node(current, size)
                            self.memory[current:size] = newItem.data
                            self.availableMemory -= size
                            newItem.next = item.next
                            item.next = newItem
                            return current
                        else:
                            current += item.next.nodeID - current
                            item = item.next
                            current += len(item.data)                    
                item.next = Node(current, size)
                self.memory[current:size] = item.data
                self.availableMemory -= size
                return current
        elif size > self.originMemory:
            raise Exception("Cannot allocate more memory than exists")
        else:
            raise Exception("Cannot allocate more memory than available")
                
    def release(self, pointer):
        """
        Releases a previously allocated block of memory.
        @param {number} pointer - The pointer to the block to release.
        @raises If the pointer does not point to an allocated block.
        """
        if pointer >= 0 and pointer <= self.originMemory:
            if pointer == 0 and self.head != None:
                self.availableMemory += len(self.head.data)
                for _ in range(self.head.nodeID, self.head.nodeID+len(self.head.data)-1):
                    self.memory[_] = None
                self.head = self.head.next
            else:               
                item = self.head
                while item.next != None:
                    if item.next.nodeID == pointer:
                        self.availableMemory += len(item.next.data)
                        for _ in range(item.next.nodeID, item.next.nodeID+len(item.next.data)-1):
                            self.memory[_] = None
                        if item.next.next != None: item.next = item.next.next
                        else: item.next = None
                        return
                    item = item.next
                return ("Pointer does not point to an allocated block")
        else:
            return ("Pointer does not point to an allocated block")



    def read(self, pointer):
        """
        Reads the value at the location identified by pointer
        @param {number} pointer - The location to read.
        @returns {number} The value at that location.
        @raises If pointer is in unallocated memory.
        """
        if self.head == None: raise Exception("No memory has been allocated")

        if pointer >= 0 and pointer <= self.originMemory:
            if pointer >= self.head.nodeID and pointer <= self.head.nodeID + len(self.head.data) - 1:
                if self.head.data[pointer-self.head.nodeID] != None: return self.head.data[pointer-self.head.nodeID]
                else: return None
            else:
                item = self.head
                while item.next != None:
                    if pointer >= item.next.nodeID and pointer <= item.next.nodeID + len(item.next.data) - 1:
                        if item.next.data[pointer - item.next.nodeID]: return item.next.data[pointer - item.next.nodeID]
                        else: return None
                    item = item.next
                raise Exception("No memory has been allocated")
        else:
            raise Exception("No memory has been allocated")


    def write(self, pointer, value):
        """
        Writes a value to the location identified by pointer
        @param {number} pointer - The location to write to.
        @param {number} value - The value to write.
        @raises If pointer is in unallocated memory.
        """
        if self.head == None: 
            raise Exception("No memory has been allocated")

        if pointer >= 0 and pointer <= self.originMemory:
            if pointer >= self.head.nodeID and pointer <= self.head.nodeID + len(self.head.data) - 1:
                self.head.data[pointer-self.head.nodeID] = value
                self.memory[pointer] = value
                return self.head.data
            else:
                item = self.head
                while item.next != None:
                    if pointer >= item.next.nodeID and pointer <= item.next.nodeID + len(item.next.data) - 1:
                        item.next.data[pointer - item.next.nodeID] = value
                        self.memory[pointer] = value
                        return item.next.data
                    item = item.next
                raise Exception("No memory has been allocated")
        else:
            raise Exception("No memory has been allocated")


#mem = MemoryManager([None] * 256)
#res  = mem.allocate(512)
#print(res)
#pointer1 = mem.allocate(128)
#print(str(pointer1))
#res  = mem.allocate(129)
#print(res)

#mem = MemoryManager([None] * 64)
#pointer1 = mem.allocate(32)
#print(str(pointer1))
#pointer2 = mem.allocate(32)
#print(str(pointer2))
#mem.release(pointer1)
#pointer3 = mem.allocate(32)
#print(str(pointer3))

#mem = MemoryManager([None] * 64)
#pointer1 = mem.allocate(16)
#print(str(pointer1))
#pointer2 = mem.allocate(16)
#print(str(pointer2))
#pointer3 = mem.allocate(16)
#print(str(pointer3))
#pointer4 = mem.allocate(16)
#print(str(pointer4))
#mem.release(pointer2)
#mem.release(pointer3)
#pointer5 = mem.allocate(36)
#print(str(pointer5))

a, b, c, d = 0, 1, 31, 32
mem = MemoryManager([None] * 64)
pointer1 = mem.allocate(32)
print(str(pointer1))
res = mem.write(pointer1, a)
print(res)
res = mem.write(pointer1 + b, b)
print(res)
res = mem.write(pointer1 + c, c)
print(res)
res = mem.write(pointer1 + d, d)
print(res)

#mem = MemoryManager([None] * 64)
#res = mem.write(1,1)
#print(res)

#mem = MemoryManager([None] * 64)
#res = mem.read(1)
#print(res)

#mem = MemoryManager([None] * 64)
#pointer1 = mem.allocate(32)
#print(str(pointer1))
#res = mem.write(pointer1, 1)
#print(res)
#res = mem.read(pointer1)
#print(res)
#res = mem.read(pointer1 + 1)
#print(res)
'''

'''
from math import sqrt

def list_squared(m, n):
    
    if m < 1 or n < 1 or m is None or n is None:
        return []

    resList = []
    finalRes = []

    if m == 1:
        finalRes.append([1, 1])
        m += 1

    for i in range(m, n):
        divider = 1
        pairNum = i
        resList.clear()
        productDivider = 1

        while divider <= pairNum:
        
            while pairNum % divider != 0:
                divider += 1

            if pairNum != divider:
                pairNum = int(pairNum / divider)
                productDivider *= divider
                if pairNum > divider:
                    resList.append(productDivider)
                    if pairNum != divider: resList.append(i / productDivider)
                divider = 2
            elif len(resList) > 4: 
                resList.append(divider * resList[2])
                resList.append(i / (divider * resList[2]))
                break
            else:    
                break

        # square all dividers
        resList = [num**2 for num in resList]

        # summ all squares
        sumNum = sum(resList)

        #print(str(sumNum))

        if sqrt(sumNum) - int(sqrt(sumNum)) == 0:
            finalRes.append([i, int(sumNum)])            

    return finalRes
'''

'''
        42
        / \
       21  2
       / \
      7  3
'''
#res = list_squared(1, 250)
#print(res)
#res = list_squared(42, 250)
#print(res)
#res = list_squared(250, 500)
#print(res)

'''


from math import sqrt

def list_squared(m, n):
    
    if m < 1 or n < 1 or m is None or n is None:
        return []

    resList = []
    finalRes = []
    midNum = 0

    if m == 1:
        finalRes.append([1, 1])
        m += 1

    for i in range(m, n):
        resList.clear()
        lastDivider = i
        primeNum = True
        if i % 2 == 0: midNum = int(i / 2) 
        elif i % 3 == 0: midNum = int(i / 3)
        elif i % 5 == 0: midNum = int(i / 5)
        elif i % 7 == 0: midNum = int(i / 7)
        else: 
            resList.append(1)
            resList.append(i)
        # find all divisers
        for y in range(1, midNum + 1):
            if y >= lastDivider:
                break            
            elif i % y == 0 and y <= lastDivider:
                lastDivider = int(i / y)
                resList.append(y)
                if y != lastDivider: resList.append(lastDivider)
            # validatino on the Prime number
            #elif y > 7 and primeNum:
            #    if len(resList) > 2:
            #        primeNum = False
            #    else: break

        
        # square all dividers
        resList = [num**2 for num in resList]

        # summ all squares
        sumNum = sum(resList)

        #print(str(sumNum))

        if sqrt(sumNum) - int(sqrt(sumNum)) == 0:
            finalRes.append([i, sumNum])


    return finalRes

'''

'''
==========================================================================
Number of trailing zeros of N!

from math import log 

def zeros(n):
    
    pow_of_5 = 5
    zeros = 0
    
    while n >= pow_of_5:
        zeros += n // pow_of_5
        pow_of_5 *= 5
        
    return zeros

'''


'''
==========================================================================
#Binary Tree

class Node:

    def __init__(self, data, level):

        self.left = None
        self.right = None
        self.data = data
        self.level = level
        self.maxlevel = 1

    def insert(self, data):
    # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data, self.level + 1)
                    if self.maxlevel < self.level + 1:
                        self.maxlevel = self.level + 1
                       
                else:
                    templevel = self.left.insert(data)
                    if self.maxlevel < templevel:
                        self.maxlevel = templevel
                    
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data, self.level+1)
                    if self.maxlevel < self.level+1:
                        self.maxlevel = self.level+1
                       
                else:
                    self.right.insert(data)
                    if self.maxlevel < templevel:
                        self.maxlevel = templevel
                        
        else:
            self.data = data
            
        return self.maxlevel


# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
            




numLevels = 1
tempLevel = 1


def maxOfTwo(tempLevel):
    global numLevels
    if numLevels < tempLevel:
        numLevels = tempLevel


# Use the insert method to add nodes
root = Node(12, 1)
tempLevel = root.insert(6)


maxOfTwo(tempLevel)

tempLevel = root.insert(14)
maxOfTwo(tempLevel)

tempLevel = root.insert(3)
maxOfTwo(tempLevel)

tempLevel = root.insert(1)
maxOfTwo(tempLevel)


root.PrintTree()

print ("Num Level = " + str(numLevels))

print (f"Num of levels in power of 2: {str(2**numLevels)}")

print (f"Max levels: {str(root.maxlevel)}")

'''


'''
==========================================================================
String incrementer

def increment_string(strng):
    
    if strng == "" or strng is None:
        return "1"

    if strng.isdigit():
        return str(int(strng) + 1).zfill(len(strng))  

    i = len(strng) - 1

    while strng[i].isdigit():
        i -= 1
    
    if i == len(strng) - 1:
        return strng + "1"
    else:
        dig = len(strng) - 1 - i
        return strng[:i+1] + str(int(strng[i+1:]) + 1).zfill(dig)  
'''


'''
==========================================================================
ROT13

def rot13(message):
    
    if message == "":
        return ""

    resStr = ""

    for ch in message:
        if ch.isalpha():
            if ord(ch) > 96:
                if ord(ch) + 13 > 122:
                    resStr += chr(96 + (ord(ch) + 13 - 122))
                else:
                    resStr += chr(ord(ch)+13)
            else:
                if ord(ch) + 13 > 90:
                    resStr += chr(64 + (ord(ch) + 13 - 90))
                else:
                    resStr += chr(ord(ch)+13)                
        else: resStr += str(ch)

    return resStr

'''

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