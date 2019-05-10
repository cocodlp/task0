# for i in range(1,10):
#     for j in range(1,i+1):
#       print("{}*{}=".format(i,j),i*j,end=" ")
#     print(" ")

# i = 1
# while i <=9:
#   j = 1
#   while j<= i:
#       print("{}*{}=".format(i,j),i*j,end=" ")
#       j +=1
#   print("")
#   i +=1

# list1 = [1,2,3]
# for i in list1:
#     for j in list1:
#         for  m in list1:
#           if i!=j & i!=m &j!= m:
#            print(i,j,m)

# x = int(input())
# y = int(input())
# z = int(input())
# list2 = [x,y,z]
# print(list2)
# list2.sort()
# print(list2)

list2 = ['physics','chemistry',1997,2000]
list3 =[1,2,3,4,5,6,7]
for i in list2:
  print(i,end=" ")
print(" ")
for i in list3:
  print(i,end=" ")
print(" ")
list2[2] = 2016
list3.remove(5)
list3.insert(6,"hellobeifeng")
print(list2,list3)

tuple1 = ('physics', 'chemistry', 1997, 2000)
tuple2 = (1, 2, 3, 4, 5, 3, 3)
# tuple1[2] = 2016
tuple3 = tuple1 + tuple2
print(tuple3)
