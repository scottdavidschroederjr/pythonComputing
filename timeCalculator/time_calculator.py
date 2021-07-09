def add_time(start, duration, day=False):
  
  #break start down into elements
  startTime = start.split()
  startTime[0] = startTime[0].split(":")

  #break duration down into elements
  durationTime = duration.split(":")
  
  #create solution time to be added to
  hoursPassed = int(durationTime[0])
  solutionMinutes = int(startTime[0][1]) + int(durationTime[1])
  daysPassed = 0
  solutionHours = startTime[0][0]

  #set proper minutes for solution
  while int(solutionMinutes) >= 60:
    hoursPassed = int(hoursPassed) + 1
    solutionMinutes = int(solutionMinutes) - 60

  if int(solutionMinutes) < 10:
    solutionMinutes = str(0) + str(solutionMinutes)

  #set proper hours for solution
  while hoursPassed != 0:
    hoursPassed = int(hoursPassed) - 1
    solutionHours = int(solutionHours) + 1

    if solutionHours == 12:
      if startTime[1] == "AM":
        startTime[1] = "PM"
      else:
        startTime[1] = "AM"
        daysPassed = daysPassed + 1
    if solutionHours > 12:
      solutionHours = 1
        

  #put together new_time for printing
  new_time = str(solutionHours) + ":" + str(solutionMinutes) + " " + str(startTime[1])

  #print results if days aren't needed
  if day == False:
    if daysPassed == 0:
      return new_time
    elif daysPassed == 1:
      new_time = new_time + " (next day)"
      return new_time   
    else:
      new_time = new_time + " " + "(" + str(daysPassed) + " days later)"
      return new_time

  #print results if days are needed
  else:
    
    #setting start day of the week
    daysList = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6, "sunday": 7}
    currentDay = day.lower()
    dayCounter = daysList.get(currentDay)

    #keeping track of day of the week
    countingDaysPassed = daysPassed
    while countingDaysPassed > 0:
      countingDaysPassed = countingDaysPassed - 1
      dayCounter = dayCounter + 1

      if dayCounter == 8:
        dayCounter = 1

    #getting end day ready for print
    printDaysList = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

    printDay = printDaysList.get(dayCounter)

    #printing final result
    if daysPassed == 0:
      new_time = new_time + ", " + printDay
      return new_time
    elif daysPassed == 1:
      new_time = new_time + ", " + printDay + " (next day)"
      return new_time   
    else:
      new_time = new_time + ", " + printDay + " (" + str(daysPassed) + " days later)"
      return new_time




