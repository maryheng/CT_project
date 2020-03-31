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
  output = test_nn_v1(p, flags)
  print(get_route_distance(output))
  output = two_opt(output)
  output = deflag(output)
  print(get_route_distance(output))
  print(output)
  return output

#Gets Euclidean distance between 2 flags based on their coordinates
def get_distance(x1,y1,x2,y2):
  distance = 0
  x1=float(x1)
  y1 = float(y1)
  x2 = float(x2)
  y2 = float(y2)
  distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
  return distance


#gets points gained per distance AKA effieciency 
def get_effieciency(distance, points):
  eff = float(points)/float(distance)
  return eff

def test_nn_v1(p, flags):
  output = []
  current_point = 0
  i=0
  #idk hahahha
  flags = get_ordered_list(flags, 0 , 0)
  while (current_point < p):
    #insert function? 
    output.append(flags[i])
    i += 1
    current_point += float(flags[i][1])
  
  return output


#ref from https://stackoverflow.com/questions/30636014/how-to-order-a-list-of-points-by-distance-to-a-given-point/30636169
def get_ordered_list(points, x, y):
   points.sort(key = lambda p: ((float(p[2]) - float(x))**2 + (float(p[3]) - float(y))**2)**(1/2))
   return points

#code from http://pedrohfsd.com/2017/08/09/2opt-part1.html
def two_opt(route):
     best = route
     improved = True
     while improved:
          improved = False
          for i in range(1, len(route)-2):
               for j in range(i+1, len(route)):
                    if j-i == 1: continue # changes nothing, skip then
                    new_route = route[:]
                    new_route[i:j] = route[j-1:i-1:-1] # this is the 2woptSwap
                    if get_route_distance(new_route) < get_route_distance(best):
                         best = new_route
                         improved = True
          route = best
     return best

def get_route_distance(route):
  output = 0
  for i in range(len(route)-1):
    output += get_distance(route[i][2], route[i][3], route[i+1][2], route[i+1][3])
  return output

def deflag(flags):
  output = []
  for flag in flags:
    output.append(flag[0])
  return output