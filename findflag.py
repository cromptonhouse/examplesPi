# C.Raynerd 11.2.14 - Find the flag
# Version 1.0 of the code - basic

print "Welcome to find the flag!"
print "There are, 50 doors and you have to find the flag in the least moves" 

count = 0          #somewhere to count the number of moves
flagDoor = 17

while 1:
   print "Please pick a door..."
   count = count + 1                     #add one to the number of moves
   currentDoor = raw_input(">")          #input a door number  
   
   if int(currentDoor) == flagDoor:
       print "You found the flag in", count,"moves" 
       break

   else:
        
        distance = int(currentDoor) - flagDoor   # calculates the distance away
        if -4 < distance < 4:
		print "You are close!!"
	else:
		print "Miles away" 
	

   

