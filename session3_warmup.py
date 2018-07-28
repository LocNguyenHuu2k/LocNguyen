# menu = []
# print(menu)

# menu = ["Steak"]
# print(menu)

# ( C-R-U-D ).( CREATE - READ - UPDATE - DELETE )
#
# CREATE ( append , insert )
#
# READ ( print )


#
# index = int(input("position = "))
#
# menu[index] = "Sweets"
#
#
# print(menu)
#
# no = 1
#
# for item in menu:
#     # print(no ,". " ,item,sep="")
#     text = "{0}. {1}".format(no ,item)
#     print(text)
#     no += 1
# for  index , item in enumerate(menu):
# #     print(index , item)


prefixes = ['I','II','III','IV']
menu = ["Steak", "Chicken", "Meat", "Seafood"]


a = len(menu)
print(a)

for p,item in zip(prefixes,menu):
    print(p,item)
