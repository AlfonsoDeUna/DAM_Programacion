from collections import deque
# lista con más funciones sobre todo par añadir y eliminar por los dos lados de la lista

d = deque('ghi')   

d.append ('a')

print (d)

d.appendleft ('a')

print (d)
d.rotate(-1)
print (d)

d.insert (3,'x')

print (d)

print (d.pop())
print (d.pop())
print (d.popleft())
print (d.popleft())
