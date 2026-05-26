
#List [] - lists are mutable array we can add or modify them //int string boolean 

Dogs = ["roger","tommy","jenny"]

print("roger" in Dogs)

Dogs[2] = 'brew'

print(Dogs)

print(Dogs[1:3])

Dogs.append('jessy')
print(Dogs)

Dogs.extend(["ferry",5]) #to add list in a list like append 
print(Dogs)

Dogs.remove('brew')
print(Dogs)

print(Dogs.pop())

Dogs.insert(2,"test") #insert inbetween with specific index 
print(Dogs)

Dogs.sort()
print(Dogs)

DogsCopy = Dogs[:] # to copy the list 
print(DogsCopy)


#Tuple () - are immutable array we cannot modify them 

names = ("john","doe")

print(len(names))

print(sorted(names)) #just printed not modified 

#Dictionaries {} - are like objects  stores the data in key value pairs 

data = {"name": "John", "Age": 19 }

data['name'] = 'roger'
print(data['name'])

print(data.get("color","brown")) # if not found retrun default - brown

print(data.popitem())

print(data.keys())
print(data.values())

print(list(data.items()))

data['fav'] = 'lemon' # add the key value pair
print(data)

del data['fav'] #delete the pair
print(data)

dataCopy = data.copy()
print(dataCopy)


#Sets () - are the set of unique items 

dataset1 = {"lemon","jamun"}
print(dataset1)

dataset2 = {"lemon"}

intersect = dataset1 & dataset2
print(intersect)

mod = dataset1 | dataset2
print(mod)

superset = dataset1 > dataset2
subset = dataset1 < dataset2

