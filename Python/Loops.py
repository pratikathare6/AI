#While loop 


cnt = 10 

while cnt >= 1:
    print(cnt)
    cnt-=1


#for loop

items = [1,2,3,4,5]

for item in items:
    print(item*2)

for item in range(20):
    print(item)

for index,item in enumerate(items):
    print(index,item)

#Break --stops the loop and continue -- continue the loop 


for item in items:
    if item == 2:
        break # continue
    print(item)

