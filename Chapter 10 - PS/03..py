class amigos:
    a = "friend"
    
object = amigos()
print (object.a)
object.a = 0
print (object.a)
print (amigos.a)

#so the class attribute doesn't change at all, it just doesn't get called out at all