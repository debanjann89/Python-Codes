words = {'A':'Ant','K' : 'King','B': 'Big','S':'Small','B':'Busy','G':'Great'}
print(words)
#f = input("Enter a index: ")
#search = words[f]
for i in sorted(words):
    print((i, words[i]), end=" ")
r = input("Enter the item")
for i in words:
    if r == words[i]:
        print(words[i],"is available in dictionary")
