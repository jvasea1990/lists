p=[None, "Toyota", "Audi", "Toyota", "BMW", "Mercedes", "Mercedes"]
z=[]
brand_count=[]
count_free_places=0


for i in range (len(p)):
    if p[i] not in z and p[i]!=None:
        z.append(p[i])
    if p[i]==None:
        count_free_places+=1
    

for j in range(len(z)):
    brand_count.append(0)
    for i in range (len(p)):
        if p[i]==z[j]:
            brand_count[j]+=1
print("\nList of parked brands: ", z, "\n")
print ("There are", count_free_places, "free places out of", len(p))
if count_free_places==len(p):
    print ("There are no cars in the parking")
else:
    for i in range(len(z)):  
        print ("There are", brand_count[i], z[i])
print()
