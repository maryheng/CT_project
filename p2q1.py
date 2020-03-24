# <Your Team ID>
# <Team members' names>

# project 2 Q1

# replace the content of this function with your own algorithm
# inputs: 
#   p: min target no. of points player must collect. p>0
#   v: 1 (non-cycle) or 2 (cycle)
#   flags: 2D list [[flagID, value, x, y], [flagID, value, x, y]....]
# returns:
#   1D list of flagIDs to represent a route. e.g. [F002, F005, F003, F009]

def get_route(p, v, flags):
  # code here
  output = []
  current_point = 0
  flag_pool = []
  #idk hahahha
  while (current_point < p):
    #insert function? 
    currentpoint = current_point#filler

  return ["F002", "F009", "F010"]

#Gets Euclidean distance between 2 flags based on their coordinates
def get_distance(x1,x2,y1,y2):
  distance = ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))**(1/2)
  return distance

#gets points gained per distance AKA effieciency 
def get_points_per_distance(distance, points):
  return points/distance