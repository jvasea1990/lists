people =["Johny", "Marry", "Francis", "Anthony"]
from_where = int(input("from which pos to move = "))
to_where = int(input("to which pos to move = "))
print()


if len(people)-1>=from_where>=0 and len(people)-1>=to_where>=0 and from_where!=to_where:
    print ("BEFORE", people)
    temp=people[from_where]
    people[from_where]=people[to_where]
    people[to_where]=temp
    print ("AFTER ", people)
elif from_where==to_where:
    print("you have chosen the same person\n")
else:
    print ("Invalid index\n")

