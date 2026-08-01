day = int(input("enter your choice\n1.monday\n2.tuesday\n3.wednesday\n4.thursday\n5.friday\n6.saturday\n7.sunday\n"))
day = day % 7
if day == 1:
  print("monday")
elif day == 2:
  print("tuesday")
elif day == 3:
  print("wednesday")
elif day == 4:
  print("thursday")
elif day == 5:
  print("friday")
elif day == 6:
  print("friday")
elif day == 0:
  print("sunday")
else :
  print("Invalid day")


