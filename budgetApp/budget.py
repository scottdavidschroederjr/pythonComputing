
class Category:
  
  def __init__ (self, name):
    self.title = name
    self.balance = 0
    self.ledger = []
    self.deposits = 0
    
  def check_funds(self, amount):
    if amount > self.balance:
      return False
    else:
      return True

  def deposit (self, amount, description=""):
    self.balance = self.balance + float(amount)
    self.ledger.append({"amount": amount, "description": description})

  def withdraw (self, amount, description=""):
    if self.check_funds(amount) == True:
      self.balance = self.balance - float(amount)
      self.ledger.append({"amount": -amount, "description": description})
      self.deposits = float(self.deposits) + float(amount)
      return True
    else:
      return False
    

  def get_balance(self):
    return self.balance

  def transfer(self, amount, destination):
    if self.check_funds(amount) == True:
      self.balance = self.balance - float(amount)
      destination.balance = destination.balance + float(amount)
      
      noteOut = "Transfer to " + str(destination.title)
      noteIn = "Transfer from " + str(self.title)

      self.ledger.append({"amount": -amount, "description": noteOut})
      destination.ledger.append({"amount": amount, "description": noteIn})

      return True
      
    else:
      return False  

  def __str__(self):
    
    #set up header of the ledger
    headerLength = len(self.title)
    aster = 30 - headerLength
    aster = aster/2
    aster = int(aster) * str("*")
    header = aster + self.title + aster + "\n"

    transactions = ""
    # build up deposits and withdraws
    x = 0
    for i in self.ledger:
      
      
      #get description from ledger and add to transactions
      ledgeDescription = self.ledger[x].get("description")
      ledgeDescription = ledgeDescription[0:23]
      transactions = transactions + ledgeDescription
      
      formatValue = self.ledger[x].get("amount")
      formatValue = "{:.2f}".format(formatValue)

      space = 30 - len(ledgeDescription) - len(formatValue)
      space = space * " "

      transactions = transactions + space + formatValue + "\n"
      
      x = x + 1

    x = 0

    fullLedger = header + str(transactions) + "Total: " + str("{:.2f}".format(self.balance))
    
    return fullLedger

     
def create_spend_chart(catagories):
  totals = {}
  totalSpent = 0
  float(totalSpent)
  sortedCatagories = []
  sortedTotals = []
  
  for i in catagories:
    sortedCatagories.append(i.title)
    sortedTotals.append(i.deposits)
  

  longestName = sorted(sortedCatagories, key=len, reverse=True)
  longestName = len(longestName[0])

  for i in sortedTotals:
    totalSpent = totalSpent + i

  x = 0
  for i in sortedTotals:
    sortedTotals[x] = i / totalSpent
    sortedTotals[x] = round(sortedTotals[x], 2)
    x = x + 1

  

  chart = "Percentage spent by category" + "\n"
  
  #add line for 100
  chart = chart + "100|"
  for i in sortedTotals:
    if i == 1:
      chart = chart + " o "
    else:
      chart = chart + "   "  
  chart = chart + " " + "\n"

  #add line for 90
  chart = chart + " 90|"
  for i in sortedTotals:
    if i >= 0.9:
      chart = chart + " o "
    else:
      chart = chart + "   "  
  chart = chart + " " + "\n"

  #add line for 80
  chart = chart + " 80|"
  for i in sortedTotals:
    if i >= 0.8:
      chart = chart + " o "
    else:
      chart = chart + "   "  
  chart = chart + " " + "\n"

  #add line for 70
  chart = chart + " 70|"
  for i in sortedTotals:
    if i >= 0.7:
      chart = chart + " o "
    else:
      chart = chart + "   "  
  chart = chart + " " + "\n"    

  #add line for 60
  chart = chart + " 60|"
  for i in sortedTotals:
    if i >= 0.6:
      chart = chart + " o "
    else:
      chart = chart + "   "  
  chart = chart + " " + "\n"  

  #add line for 50
  chart = chart + " 50|"
  for i in sortedTotals:
    if i >= 0.5:
      chart = chart + " o "
    else:
      chart = chart + "   "  
  chart = chart + " " + "\n"  

  #add line for 40
  chart = chart + " 40|"
  for i in sortedTotals:
    if i >= 0.4:
      chart = chart + " o "
    else:
      chart = chart + "   "  
  chart = chart + " " + "\n" 

  #add line for 30
  chart = chart + " 30|"
  for i in sortedTotals:
    if i >= 0.3:
      chart = chart + " o "
    else:
      chart = chart + "   "  
  chart = chart + " " + "\n" 

  #add line for 20
  chart = chart + " 20|"
  for i in sortedTotals:
    if i >= 0.2:
      chart = chart + " o "
    else:
      chart = chart + "   "  
  chart = chart + " " + "\n" 

  #add line for 10
  chart = chart + " 10|"
  for i in sortedTotals:
    if i >= 0.1:
      chart = chart + " o "
    else:
      chart = chart + "   "  
  chart = chart + " " + "\n" 

  #add line for 0
  chart = chart + "  0|"
  for i in sortedTotals:
    if i >= 0.0:
      chart = chart + " o "
    else:
      chart = chart + "   "  
  chart = chart + " " + "\n" 

  #add bottom chart line
  
  chart = chart + "    "
  numCatagories = len(sortedTotals)
  chart = chart + "---" * int(numCatagories) + "-" + "\n"

  #add catagory names
  z = 0
  while z < longestName:
    chart = chart + "    "
    for i in sortedCatagories:
      try:
        chart = chart + " " + i[z] + " "
      except:
        chart = chart + "   "
    if z == longestName - 1:
      chart = chart + " "
      z = z + 1
    else:       
      chart = chart + " " + "\n"
      z = z + 1

    

  return chart