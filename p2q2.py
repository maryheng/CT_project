# <Your Team ID>
# <Team members' names>

# project 2 Q2

# replace the content of this function with your own algorithm
# inputs: 
#   p: min target no. of points team must collect. p>0
#   v: 1 (non-cycle) or 2 (cycle)
#   flags: 2D list [[flagID, value, x, y], [flagID, value, x, y]....]
# returns:
#   A list of n lists. Each "inner list" represents a route. There must be n routes in your answer

def get_routes(p, v, flags, n):
  # code here
  # return [["F001", "F002", "F003"], ["F009", "F006"]]
  output = []

  output = []
  flagpool = []
  point = 0
  flag_dict = to_dict(flags)
  currentflag = ['sp',0,0,0]
  
  flag_data = get_next_flag_data(flags, [], currentflag)

  while(point < p):
    temp = get_next_flag_data(flags, flagpool, currentflag)[0]
    flagpool.append(temp[0])
    point += float(temp[2])
    currentflag = [temp[0], temp[2], temp[3], temp[4]]
  # print(output)
  flag_pool = two_opt(output, flag_dict)

  return [[]]*n

def get_next_flag_data(flags, flagpool, current_flag):
  output = []
  for flag in flags:
    if flag[0] not in flagpool:
      dist = get_distance(flag, current_flag)
      eff = get_effieciency(dist, flag[1])
      output.append([flag[0], eff, flag[1], flag[2], flag[3]])
    output.sort(key=lambda x: (-x[1]))
  return output

def get_distance(node_A, node_B):
  return ((float(node_A[2]) - float(node_B[2])) ** 2 + (float(node_A[3]) - float(node_B[3])) ** 2) ** 0.5

def get_effieciency(distance, points):
  eff = float(points)/float(distance)
  return eff

def to_dict(flags):
  output = {}
  for flag in flags:
    a = float(flag[1])
    b = float(flag[2])
    c = float(flag[3])
    output[flag[0]] = [a,b,c]

  return output

#code from http://pedrohfsd.com/2017/08/09/2opt-part1.html
def two_opt(route, flag_dic):
     best = route
     improved = True
     while improved:
          improved = False
          for i in range(1, len(route)-2):
               for j in range(i+1, len(route)):
                    if j-i == 1: continue # changes nothing, skip then
                    new_route = route[:]
                    new_route[i:j] = route[j-1:i-1:-1] # this is the 2woptSwap
                    if get_route_distance(new_route, flag_dic) < get_route_distance(best, flag_dic):
                         best = new_route
                         improved = True
          route = best
     return best

def get_route_distance(route, flag_dic):
  output = 0

  current_temp = [route[0]] + flag_dic[route[0]]
  for i in range(len(route)-1):
    next_temp = [route[i+1]] + flag_dic[route[i+1]]
    output += get_distance(current_temp, next_temp)
    current_temp = next_temp
  output += get_distance(current_temp,next_temp)
    
  return output
