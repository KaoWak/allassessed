def find_maximum_difference(a, b):
#     # code implementation here...
 max_1 = max(a)
 min_1 = min(a)
 max_2 = max(b)
 min_2 = min(b)

 differance_1 = (max_1 - min_2)
 differance_2 = (max_2 - min_1)
 maximum = (differance_1, differance_2)

 return maximum


#print(find_maximum_difference(a =[1, 5, 600], b =[100, 7, 3, 29, 39]))
print(find_maximum_difference( a =[1,5 ,600], b =[100 ,7, 3 , 602, 39]))



