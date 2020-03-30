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
  output = nn_v1(p, flags)
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

def nn_v1(p, flags):
  output = []
  current_point = 0
  current_coord = [0,0]
  highest_eff = 0
  current_eff = 0

  #idk hahahha
  while (current_point < p):
    #insert function? 
    i=0
    chosen_i = 0

    for flag in flags:
      
      distance = get_distance(current_coord[0], current_coord[1], flag[2], flag[3])
      # current_eff = get_effieciency(flag[1], distance)
      if distance >= highest_eff:
        highest_eff = distance
        chosen_i = i
      i+=1
    current_coord = [flags[chosen_i][2], flags[chosen_i][3]][:]
    current_point += float(flags[chosen_i][1])
    output.append(flags[chosen_i])
    flags.pop(chosen_i)
  
  return output

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