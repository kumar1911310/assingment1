if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    myList = []
for item in arr:
    myList.append(item) 
maxItem = max(myList)
if myList.count(maxItem) != 1:  
    myList = list(dict.fromkeys(myList))    
myList.remove(maxItem)
print(max(myList))