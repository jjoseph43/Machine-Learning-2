print ("hello world");
print ("hello world2");

from heapq import merge
import numpy as np;

# Jobin Joseph HW1 Submission 

#----------------LISTS--------------------------------------------------
# append() 
list1 = ['Green',"Red","Red",'Blue'] # creating a mock list
list1.append("Yellow") # append = added to the list
print(list1)  #we can see that append added the nine to the list1

#extend()
list2 = ['Pink',"Gray"]
list1.extend(list2) #extend added this list to another list
print(list1) 

#index()
print(list1[2])  #prints the value at that index
print(list1.index("Pink")) #tells you what index that value is at

#index(value, integer)

print(list1.index("Blue",1) )# allows for you to search for a value from a begining point

#insert(position)
list1.insert(1,"teal") #inserts  a value at a position in this case teal at that index
print(list1)

#remove()
list1.remove("Pink") #removes this value from the list
print(list1)

#pop() 
list1.pop() # takes the last item out of the list
print(list1)

#count()
print(list1.count("Red") )# counts how often this value occurs in the list

#reverse()
list1.reverse() # reverses the list
print(list1)
#sort()
list1.sort() # sorts the list in this case is is alphabetical
print(list1)

#[1]+[1] #you can add lists together
list1double = ['Green',"Red","Red",'Blue'] +['Green',"Red","Red",'Blue']
print(list1double)

#[2]*2 # you can multiply the values of lists
List2new = ['Pink',"Gray"] * 2
print(List2new)
#[1,2][1:]# the output starts at the value of list 
print(['Green',"Red","Red",'Blue','Pink',"Gray"] [1:])

#[x for x in [2,3]]
print([x for x in ['Pink',"Gray"]]) # this function loops in list
 
#[x for x in [1,2] if x ==1] # loops through a list until it  finds a true match
print([x for x in ['Pink',"Gray"]if x =="Pink"])#returns a value
print([x for x in ['Pink',"Gray"]if x =="Red"]) #does not return a value

#[y*2 for x in [[1,2],[3,4]] for y in x]
list3 = [y*2 for x in [['Pink',"Gray"],["Red",'Blue']] for y in x]
print(list3) # here we can see that the are both multiplied by two  by the for loop 
#A = [1]
A = [1]
print(A) # here we assigned a list to a variable name

#---------------Tuples-------------------------------------------------------------
# tuples are different lists because they cannot contain modified
tupletry = (10,9,8,7,6,5,5)

#count() #tells how many times that value comes up in the tuple 
print(tupletry.count(5))

#index() # gives you what position the value is in the tuple 
print(tupletry.index(9))

#build a dictionary from tuples
Tupledef = dict([("Pepsi",1),("Coke",2),("Sprite",3)]) #adds a dictionary to the tuple
print (Tupledef)

#unpacking tuples #you can find the parts of the tuple
for n, v in Tupledef.items():
    print ()
    print (n, v)

#-----------------dictionary--------------------------------

a_dict = {'I hate':'you', 'You should':'leave'}

#keys()
print(a_dict.keys()) #shows you the just the keys of the dictionary

#items()
print(a_dict.items())#shows you both keys and definitions 
#hasvalues()
#print(a_dict.hasvalues())  could not find this function values() is a function
#_key() I could not find this function of dictionary
#print(a_dict.keys())
#‘never’ in a_dict # comes back as false as there is no never
print('never' in a_dict)
#del a_dict['me']
#del a_dict['me'] this throws an error since there is no me to delete
#print(a_dict)
#a_dict.clear() # this clears the dictionary
a_dict.clear()
print(a_dict)

#-----------------SETS--------------------------------

# sets  allow multiple items to store into a single variable
#Sets use curly brackets
#Sets do not have any order, duplicates are not allowed

Exampleset = {"Pen","Pencil", "Marker"}
#.add
Exampleset.add("Hilighter") #added  Hilighter to the set
#clear()
Exampleset.clear() #clears the set
#copy()
Exampleset = {"Pen","Pencil", "Marker"}
Copyset = Exampleset.copy() #copies the first set to the second variable name
print(Copyset)
#difference() #compares two sets
setdifferences = Exampleset.difference(Copyset)
print(setdifferences)
print(Exampleset)
#discard() #removes one item from the set
Exampleset.discard("Pen")
print(Exampleset)
 
#intersection() #this shows the same items in the two sets
Setinter = Exampleset.intersection(Copyset)
print(Setinter)

#issubset() #tells you if the sets contains the other set
subsetoutput = Exampleset.issubset(Copyset)
print(subsetoutput)
#pop() #takes the last item from the set
print(Exampleset.pop())
#remove() #removes the item from the set (Threw an error sincethere is any
# pens left in the set)
#Exampleset.remove("Pen")
print(Exampleset)
#union() #makes a new set combining both sets takes out duplicates
newset = Exampleset.union(Copyset)
print(newset)
#update() # added the new set to the existing
Exampleset = {"Pen","Pencil", "Marker"}
newset = {"Hilighter"}
Exampleset.update(newset)
print(Exampleset)


#-----------------Strings--------------------------------
TestStrings = "On Wednesday we have class."
#capitalize() #capitalizs the first letter of the string
print(TestStrings.capitalize()) 
#casefold() #lowercase the first letter of the string
print(TestStrings.casefold())
#center() #centers the string
print(TestStrings.center(30))
#count() #how many of that word is in the string
print(TestStrings.count("we"))
#encode() #gives an encoded string
print(TestStrings.encode())
#find() #finds where the that word starts
print(TestStrings.find("we"))
#partition() #creates breaks around the word 
print(TestStrings.partition("we"))
#replace() #swaps out the word with the second word
TestStrings = "On Wednesday we have class."
print(TestStrings.replace("we","you"))
#split() Breaks the  string two differt parts
TestStrings = "On Wednesday we have class."
print(TestStrings.split("we"))
#title()# Each word has a capital letter
print(TestStrings.title())
#zfill() #adds zeros to the begining of a numerical string not too applicable here
print(TestStrings.zfill(11))
#------------------Flowers ----------------------------------------------------
from collections import Counter
import matplotlib.pyplot as plt;
import numpy as np;
from itertools import *
print ("hello world");

flower_orders=['W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B',
               'W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B',
               'W/R/B','W/R/B','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R',
               'R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','W/R/V','W/R/V','W/R/V','W/R/V',
               'W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V',
               'W/N/R/V','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','B/Y','B/Y','B/Y','B/Y','B/Y','R/B/Y','R/B/Y',
               'R/B/Y','R/B/Y','R/B/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/G','W/G','W/G','W/G',
               'R/Y','R/Y','R/Y','R/Y','N/R/V/Y','N/R/V/Y','N/R/V/Y','N/R/V/Y','W/R/B/V','W/R/B/V','W/R/B/V','W/R/B/V','W/N/R/V/Y',
               'W/N/R/V/Y','W/N/R/V/Y','W/N/R/V/Y','N/R/Y','N/R/Y','N/R/Y','W/V/O','W/V/O','W/V/O','W/N/R/Y','W/N/R/Y','W/N/R/Y','R/B/V/Y',
               'R/B/V/Y','R/B/V/Y','W/R/V/Y','W/R/V/Y','W/R/V/Y','W/R/B/V/Y','W/R/B/V/Y','W/R/B/V/Y','W/N/R/B/Y','W/N/R/B/Y','W/N/R/B/Y','R/G',
               'R/G','B/V/Y','B/V/Y','N/B/Y','N/B/Y','W/B/Y','W/B/Y','W/N/B','W/N/B','W/N/R','W/N/R','W/N/B/Y','W/N/B/Y','W/B/V/Y','W/B/V/Y',
               'W/N/R/B/V/Y/G/M','W/N/R/B/V/Y/G/M','B/R','N/R','V/Y','V','N/R/V','N/V/Y','R/B/O','W/B/V','W/V/Y','W/N/R/B','W/N/R/O','W/N/R/G',
               'W/N/V/Y','W/N/Y/M','N/R/B/Y','N/B/V/Y','R/V/Y/O','W/B/V/M','W/B/V/O','N/R/B/Y/M','N/R/V/O/M','W/N/R/Y/G','N/R/B/V/Y','W/R/B/V/Y/P',
               'W/N/R/B/Y/G','W/N/R/B/V/O/M','W/N/R/B/V/Y/M','W/N/B/V/Y/G/M','W/N/B/V/V/Y/P']

#1. Build a counter object and use the counter and confirm they have the same values.
Flowercounts = Counter(flower_orders)
settingflower = set(flower_orders)
print (Flowercounts)

#2 Count how many objects have color W in them.
Wflowers = 0
#using a for loop and elements function
for type in Counter(flower_orders).elements():
    if "W" in type:
     Wflowers += 1
print ("Numbers of objects with W in them" , Wflowers)

#3 Make histogram of colors
colors = [y for x in flower_orders for y in x.split('/')]
colorscount = Counter(colors)
plt.bar(colorscount.keys(),colorscount.values())
plt.show()
#4. Rank the pairs of colors in each order regardless of how many colors are in an order.

fpairs = [y for x in flower_orders for y in combinations(x.split('/'), 2)] #using the combinations function
pair_counter = Counter(fpairs)

for i in pair_counter:
    print(f'{i} : {pair_counter[i]}')
#5. Rank the triplets of colors in each order regardless of how many colors are in an order.
ftriplets = [y for x in flower_orders for y in combinations(x.split('/'), 3)]#using the combinations function changing to 3 letter combos
Triplet_counter = Counter(ftriplets)

for i in Triplet_counter:
    print(f'{i} : {Triplet_counter[i]}')
    
#6. Make dictionary color for keys and values are what other colors it is ordered with.
Flowercolordict = dict(Flowercounts) #used the dict function  to make a dictionary 
print(Flowercolordict)

#7.Make a graph showing the probability of having an edge between two colors based 
# on how often they co-occur.  (a numpy square matrix)
fpairs = [y for x in flower_orders for y in combinations(x.split('/'), 2)] #using the combinations function
pair_counter = Counter(fpairs)


flowerDict = {}# this dictionary should hold the values for each
#total number of pairs of colors
ftotal = sum([y for x, y in pair_counter.items()])

for key, value in pair_counter.items():# adding the probabilities as keys for each of the pairs
    flowerDict[key] = value/ftotal

print(flowerDict)
#plt.bar(flowerDict.keys(),flowerDict.values()) Didn't work
#lt.show()

#8.Make 10 business questions related to the questions we asked above

#1 What is our best selling flower?
#2 What are  the most common combinations to sell a bouquet ?
#3 How often do we sell our least common bouquets?
#4 Can this data be presented in a different graph?
#5 How many combinations can I sell from a color group?
#6 Is it  better to have more red in stack than blue flowers?
#7 What could the most common combination  for next season?
#8 What plants should be consistently growing and which just need to be grown some time?
#9 What are the flower colors that we need to change  to produce more variety?
#10 How often do we get this data ?




#--------------------------Dead men tell tales-------------------------
dead_men_tell_tales =['Four score and seven years ago our fathers brought forth on this',
'continent a new nation, conceived in liberty and dedicated to the',
'proposition that all men are created equal. Now we are engaged in',
'a great civil war, testing whether that nation or any nation so',
'conceived and so dedicated can long endure. We are met on a great',
'battlefield of that war. We have come to dedicate a portion of',
'that field as a final resting-place for those who here gave their',
'lives that that nation might live. It is altogether fitting and',
'proper that we should do this. But in a larger sense, we cannot',
'dedicate, we cannot consecrate, we cannot hallow this ground.',
'The brave men, living and dead who struggled here have consecrated',
'it far above our poor power to add or detract. The world will',
'little note nor long remember what we say here, but it can never',
'forget what they did here. It is for us the living rather to be',
'dedicated here to the unfinished work which they who fought here',
'have thus far so nobly advanced. It is rather for us to be here',
'dedicated to the great task remaining before us--that from these',
'honored dead we take increased devotion to that cause for which',
'they gave the last full measure of devotion--that we here highly',
'resolve that these dead shall not have died in vain, that this',
'nation under God shall have a new birth of freedom, and that',
'government of the people, by the people, for the people shall',
'not perish from the earth.']

# 1. Join everything
deadmanjoined = "".join(dead_men_tell_tales)
#2. Remove spaces
deadmanspaceremoved = deadmanjoined.strip() #.strip removes the spaces
#3. Occurrence probabilities for letters
DeadOccurance = [y for x in deadmanspaceremoved for y in x.split() if x.isalpha()] #Identified unique letters
prob = {}
for k, v in Counter(DeadOccurance).items():# takes the letter from the counter
    prob[k] = round(v/len(DeadOccurance),2)# adds the probability 
#4. Tell me transition probabilities for every letter pairs
Deadpairs = [(DeadOccurance[x],DeadOccurance[x+1]) for x in range(len(DeadOccurance)-1)] 
transitionprob = {}
for k, v in Counter(Deadpairs).items():# takes the letter from the counter
    transitionprob[k] = round(v/len(Deadpairs),2)# adds the probability 
#5. Make a 26x26 graph of 4.  in numpy
print(Deadpairs)
#6. plot graph of transition probabilities from letter to letter
#kmeans clustering here?

#Unrelated:
#7. Flatten a nested list
import itertools

list2d = [[1,2,3], [4,5,6], [7], [8,9]]
merged = list(itertools.chain(*list2d)) #using itertools.chain
print(merged)
#Cool intro python resources:
#https://thomas-cokelaer.info/tutorials/python/index.html
