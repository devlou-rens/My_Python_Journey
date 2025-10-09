command =""
started = True
stoped = False
while True:
    command = input(">").lower()
    if command == ("start"):
      if started: 
         print("the car is already started")
      else:
        started = True
        print("the car is star...")

    elif command == ("stop"):
        if stoped:
            print ("car is already stoped")
        else:
            stoped = True
            print("the car stoped")
    elif command == ("help"):
        print('''''
start - to start the car
stop - to stop the car
quit- to quit        
        ''''')
    elif command == ("quit"):
        break
    else:
        print("syntax error")