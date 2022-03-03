import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Decision Making With Matrices

# This is a pretty simple assignment.  You will do something you do everyday, but today it will be with matrix manipulations. 

# The problem is: you and your work friends are trying to decide where to go for lunch. You have to pick a restaurant that’s best for everyone.  Then you should decided if you should split into two groups so everyone is happier.  

# Despite the simplicity of the process you will need to make decisions regarding how to process the data.
  
# This process was thoroughly investigated in the operation research community.  This approach can prove helpful on any number of decision making problems that are currently not leveraging machine learning.  

people = {'Jane': {'willingness to travel':1,
                  'desire for new experience':1,
                  'cost':3,
                  'indian food':4,
                  #'mexican food':1,
                  'hipster points':2,
                  'vegetarian':3 },
        "John": {'willingness to travel': 5,
                  'desire for new experience':2,
                  'cost':5,
                  'indian food':3,
                  #'mexican food':4,
                  'hipster points':1,
                  'vegetarian':2, },
        "Jack": {'willingness to travel':5,
                  'desire for new experience':2,
                  'cost':3,
                  'indian food':3,
                  #'mexican food':4,
                  'hipster points':1,
                  'vegetarian':2,},
        "Greg": {'willingness to travel':5,
                  'desire for new experience':5,
                  'cost':5,
                  'indian food':3,
                  #'mexican food':4,
                  'hipster points':1,
                  'vegetarian':2, },
        "Kenny": {'willingness to travel':4,
                  'desire for new experience':4,
                  'cost':2,
                  'indian food':3,
                  #'mexican food':4,
                  'hipster points':1,
                  'vegetarian':2,},
        "Mike": {'willingness to travel':3,
                  'desire for new experience':3,
                  'cost':2,
                  'indian food':3,
                  #'mexican food':4,
                  'hipster points':1,
                  'vegetarian':2,},
        "Zhang": {'willingness to travel':3,
                  'desire for new experience':3,
                  'cost':2,
                  'indian food':3,
                  #'mexican food':4,
                  'hipster points':1,
                  'vegetarian':2,},      
        "Zion": {'willingness to travel':5,
                  'desire for new experience':5,
                  'cost':2,
                  'indian food':3,
                  #'mexican food':4,
                  'hipster points':1,
                  'vegetarian':2,},  
        "Ava": {'willingness to travel':4,
                  'desire for new experience':3,
                  'cost':2,
                  'indian food':3,
                  #'mexican food':4,
                  'hipster points':1,
                  'vegetarian':2,},      
        "Jose": {'willingness to travel':4,
                  'desire for new experience':4,
                  'cost':2,
                  'indian food':3,
                  #'mexican food':4,
                  'hipster points':1,
                  'vegetarian':2,},             
                }         

# print (people)    

# Transform the user data into a matrix(M_people). Keep track of column and row ids.   
dictlist =[]
for key in people:
    print("Name: ", key)
    print(key, "'s choices:", people[key].values())
    temp = list(people[key].values())
    dictlist.append(temp)
    
M_people = np.array(dictlist)    
print("Here is the people matrix \n", M_people)


# Next you collected data from an internet website. You got the following information.

restaurants  = {'flacos':{'distance' : 1,
                        'novelty' :2,
                        'cost': 3,
                        'average rating': 4,
                        'cuisine':5,
                        'vegetarians':1},
                'Nobu':{'distance' : 5,
                        'novelty' :2,
                        'cost': 5,
                        'average rating': 4,
                        'cuisine':1,
                        'vegetarians':3},
                'Cheescake Factory':{'distance' : 1,
                        'novelty' :5,
                        'cost': 4,
                        'average rating': 4,
                        'cuisine':4,
                        'vegetarians':2},
                'Chipotle':{'distance' : 4,
                        'novelty' :3,
                        'cost': 3,
                        'average rating': 4,
                        'cuisine':5,
                        'vegetarians':5},
                'Subway':{'distance' : 3,
                        'novelty' :2,
                        'cost': 1,
                        'average rating': 4,
                        'cuisine':5,
                        'vegetarians':5},
                'McDonalds':{'distance' : 1,
                        'novelty' :2,
                        'cost': 1,
                        'average rating': 4,
                        'cuisine':5,
                        'vegetarians':2},
                'Dominos':{'distance' : 2,
                        'novelty' :2,
                        'cost': 1,
                        'average rating': 4,
                        'cuisine':5,
                        'vegetarians':4},
                'Ritas':{'distance' : 4,
                        'novelty' :2,
                        'cost': 3,
                        'average rating': 4,
                        'cuisine':5,
                        'vegetarians':5},
                'Pizza Hut':{'distance' : 2,
                        'novelty' :2,
                        'cost': 1,
                        'average rating': 4,
                        'cuisine':5,
                        'vegetarians':4},
                'dunkin':{'distance' : 2,
                        'novelty' :2,
                        'cost': 1,
                        'average rating': 4,
                        'cuisine':5,
                        'vegetarians':3}}
print('\n \n  Restaurant Details: \n \n')
dictlist =[]
for key in restaurants:
    print("Restaurant:", key)
    print("Restaurant rankings: ", restaurants[key].values())
    temp = list(restaurants[key].values())
    dictlist.append(temp)

M_resturants = np.array(dictlist)    
print("Here is the restaurant matrix \n", M_resturants)
# The most important idea in this project is the idea of a linear combination.  
# Informally describe what a linear combination is  and how it will relate to our restaurant matrix.

print ("A linear combination is defined as numbers in a matrices that have been multiplied by a factor  and added together. ");
print ("This can  be seen in every day life as everyone has different preferences and that this can play a factor in choosing what restaurants   to go to can");
print ("change the rankings about what restaurant is the best. ");

# Choose a person and compute(using a linear combination) the top restaurant for them.  What does each entry in the resulting vector represent? 
Gregs_choice = np.dot(M_resturants, M_people[3].transpose())
firstwinner = np.argmax(Gregs_choice)

bestchoice = np.argwhere(Gregs_choice == np.amax(Gregs_choice))
print(bestchoice)


print(M_resturants[firstwinner])
print("Each entry in the vector represents a value of strength that is making the  person more likely to pick a restaurants ")


# Next, compute a new matrix (M_usr_x_rest  i.e. an user by restaurant) from all people.  What does the a_ij matrix represent? 
M_usr_x_rest = np.dot(M_resturants, M_people.transpose())
print(M_usr_x_rest)

print ("The matrix  above values would represent the amount of like a person had for a restaurant. This is for all the people")
print("This A_ij matrix represents  the ability to  utilize for Skew symmetric matrices and reciprocal matrices to be able to possibly use for transitivity ")

# Sum all columns in M_usr_x_rest to get the optimal restaurant for all users.  What do the entries represent?

col_sum = np.sum(M_usr_x_rest, axis=1)

print(col_sum)
print ("This shows that there are  favored winner of what restaurant would  be  the fourth restaurant which would be Cheesecake Factory")


# Now convert each row in the M_usr_x_rest into a ranking for each user and call it M_usr_x_rest_rank.   Do the same as above to generate the optimal restaurant choice.  
M_usr_x_rest_rank = M_usr_x_rest.argsort(axis=0).argsort(axis=0) + 1
print(M_usr_x_rest_rank)

# Why is there a difference between the two?  What problem arrives?  What does it represent in the real world?
print("There are differences for the output for both groups because there is  the score  ranking  would be more skewed by other than rank based ranking")

# How should you preprocess your data to remove this problem. 
print("The data can be normalized so that the scores can be less impactful how they skew other people in the group. Here we have normalized it from 1-5")

# Find  user profiles that are problematic, explain why?
print ("The users John and Jack could pose some problems as there have the same weights and they could skew the results in their favor.")
print ("Since the users are all normalized on a scale 1  to 5 that is  good other wise there could be problems with the score ranking system ")

# Think of two metrics to compute the dissatisfaction with the group.  
print("I think that it would be important to see  people individual  rankings with the group rankings and see how it compares with what the whole group ranking choose")
print("The other  method I would look at would possibly be clustering as there might be some benefit in splitting the groups to where they end up going")

# Should you split in two groups today? 
# For this we would should use a clustering algorithm to find out. A good place to look at would be kmean clustering
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
kmeans = KMeans(n_clusters=2, random_state=0).fit(M_people)
y_pred = KMeans(n_clusters=2, random_state=0).fit_predict(M_people)
n_samples = 10
random_state = 170
X, y = make_blobs(n_samples=n_samples, random_state=random_state)

plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.title("The different clusters of people ")
print(" In this example we could see where there could be 3 groups")
plt.show()

# Ok. Now you just found out the boss is paying for the meal. How should you adjust? Now what is the best restaurant?
print( "Since the boss is paying  for lunch we could set the  users cost preference to high as they might not have the restriction of a high cost meal. This would greatly impact the  order  of the rankings ")
# setting dictionary  to new preferences
peoplewithboss = {'Jane': {'willingness to travel':1,
                  'desire for new experience':1,
                  'cost':5,
                  'indian food':4,
                  #'mexican food':1,
                  'hipster points':2,
                  'vegetarian':3 },
        "John": {'willingness to travel': 5,
                  'desire for new experience':2,
                  'cost':5,
                  'indian food':3,
                  #'mexican food':4,
                  'hipster points':1,
                  'vegetarian':2, },
        "Jack": {'willingness to travel':5,
                  'desire for new experience':2,
                  'cost':5,
                  'indian food':3,
                  #'mexican food':4,
                  'hipster points':1,
                  'vegetarian':2,},
        "Greg": {'willingness to travel':5,
                  'desire for new experience':5,
                  'cost':5,
                  'indian food':3,
                  #'mexican food':4,
                  'hipster points':1,
                  'vegetarian':2, },
        "Kenny": {'willingness to travel':4,
                  'desire for new experience':4,
                  'cost':5,
                  'indian food':3,
                  #'mexican food':4,
                  'hipster points':1,
                  'vegetarian':2,},
        "Mike": {'willingness to travel':3,
                  'desire for new experience':3,
                  'cost':5,
                  'indian food':3,
                  #'mexican food':4,
                  'hipster points':1,
                  'vegetarian':2,},
        "Zhang": {'willingness to travel':3,
                  'desire for new experience':3,
                  'cost':5,
                  'indian food':3,
                  #'mexican food':4,
                  'hipster points':1,
                  'vegetarian':2,},      
        "Zion": {'willingness to travel':5,
                  'desire for new experience':5,
                  'cost':5,
                  'indian food':3,
                  #'mexican food':4,
                  'hipster points':1,
                  'vegetarian':2,},  
        "Ava": {'willingness to travel':4,
                  'desire for new experience':3,
                  'cost':5,
                  'indian food':3,
                  #'mexican food':4,
                  'hipster points':1,
                  'vegetarian':2,},      
        "Jose": {'willingness to travel':4,
                  'desire for new experience':4,
                  'cost':5,
                  'indian food':3,
                  #'mexican food':4,
                  'hipster points':1,
                  'vegetarian':2,},             
                }         
dictlist =[]
for key in peoplewithboss:
    print("Name: ", key)
    print(key, "'s choices:", peoplewithboss[key].values())
    temp = list(peoplewithboss[key].values())
    dictlist.append(temp)
    
M_peopleboss = np.array(dictlist)  
#use the dot product to find the scores
M_usr_x_rest = np.dot(M_resturants, M_peopleboss.transpose())
#Use the addtion to show ranking of resturants
col_sum = np.sum(M_usr_x_rest, axis=1)

print(col_sum)
print("So when cost can be higher for all the coworkers now the the most costly restaurant Nobu wins ")

# Tomorrow you visit another team. You have the same restaurants and they told you their optimal ordering for restaurants.  Can you find their weight matrix? 
print("Once the ranking of the matrix is done then there can not be any back calculations that can definitively tell you the weight that each person gave. There are different weights that can be multiplied added so that it produces the same value ")
