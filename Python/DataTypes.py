# Lists - is a mutable array 

courses = ['History','Math','sci','compsci']

print(courses)
print(courses[0])
print(courses[-1])

# Add values
courses.insert(0,'phy')
print(courses)

#Add another list

courses2 = ['Art','Commerce']

courses.extend(courses2)

print(courses)

# Remove values
courses.remove('Math')
print(courses)

popped = courses2.pop()

print(popped)

courses.reverse()
print(courses)

courses.sort()
print(courses)

nums = [5,4,3,2,1]
nums.sort()
print(nums)

nums.reverse()
print(nums)

# Looping values 

for item in nums:
        print(item)

# Splitting values

numsstr = '-'.join(courses)


newnums = numsstr.split(' - ')
print(newnums)
print(numsstr)

# Tuples - immutable array 

tupule1 = ('A','B','C')

tupule2 = tupule1

print(tupule1)
print(tupule2)

#tupule1[0] = 'D' #Not supported


#Distionaries - like objects key value pair

thisdict = {
        "name": "john",
        "age": 12
}

print(thisdict)


#sets -  contains the unique values it avoids duplicates 

set1 = {'math','hist','math'}

print(set1)

# Check the value in set present or not 

print('math' in set1) 

#Intersection 

set2 = {'math','java','hist'}

print(set1.intersection(set2))

# Difference
print(set1.difference(set2))

#union

print(set1.union(set2))

