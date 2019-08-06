class Stackk:
    def __init__(a):
        a.items = []
 
    def is_empty(a):
        return a.items == []
 
    def push(a, data):
        a.items.append(data)
 
    def pop(a):
        return a.items.pop()
 
 
s = Stackk()
t= input()
 
for character in t:
    s.push(character)
 
reversed_text = ''
while not s.is_empty():
    reversed_text = reversed_text + s.pop()
 
if t== reversed_text:
    print('YES')
else:
    print('NO')
