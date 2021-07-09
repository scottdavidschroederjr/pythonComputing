import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      add = 0 
      while add < int(value):
        self.contents.append(key)
        add = add + 1

  def draw(self, numberToDraw):
      drawn = 0
      results = []
      while drawn < numberToDraw:
        if len(self.contents) == 0:
          return results
          break
        else:
          draw = self.contents.pop(random.randint(0,len(self.contents)-1))
          results.append(draw)
          drawn = drawn + 1
      return results
      
      
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  experimentsRun = 0
  failedExperiments = 0
  while experimentsRun < num_experiments:
    contents = list(hat.contents)
    drawn = 0
    results = []
    while drawn < num_balls_drawn:
      if len(contents) == 0:
        break
      else:
        draw = contents.pop(random.randint(0,len(contents)-1))
        results.append(draw)
        drawn = drawn + 1
    for key, value in expected_balls.items():
      if results.count(key) >= int(value):
        continue
      else:
        failedExperiments = failedExperiments + 1
        break
    experimentsRun = experimentsRun + 1  
  results = (num_experiments - failedExperiments) / (num_experiments)
  return results

