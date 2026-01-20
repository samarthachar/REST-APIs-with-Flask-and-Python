lst = [
    "apple",
    "banana",
    "cherry",
    ,
    "elderberry",
    "fig",
    "grape"
]

lst = [str(item) for item in lst]


print(lst)

lst.sort()
item = str("fig")
if item not in lst:
    print("Item not in list") 
    exit()

found = False
while not found:
    print(lst)
    middleIndex = (len(lst) - 1) // 2
    if lst[middleIndex] == item:
        found = True
    elif lst[middleIndex] < item:
        lst = lst[middleIndex+1:]
    else:
        lst = lst[:middleIndex]



print(f"Yay! we found the item: {lst[middleIndex]}")