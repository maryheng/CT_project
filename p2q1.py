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
from math import sqrt
def get_route(p, v, flags):
  # code here
  output = []
  
  output = test_nn_v1(p, flags)
  flag_dict = to_dict(flags)
  
  flag_dict2 = to_dict2(flags, p)
  # print(flag_dict2)
  # print(dict_to_list(flag_dict2, p, flags))
  output = two_opt(output, flag_dict2)
  output = deflag(output)
  # print(min(flag_dict2, key=lambda k:float(flag_dict2[k]['F114'])))
  print(output)
  return output

def to_dict(flags):
  output = {}
  for flag in flags:
    a = float(flag[1])
    b = float(flag[2])
    c = float(flag[3])
    output[flag[0]] = [a,b,c]

  return output

def dict_to_list(flag_dict, p, flags):
  output =[]
  points = 0
  current_distance = 10000000
  current_flag = 'sp'
  selected_key = ''
  temp_dic = flag_dict[current_flag]
  # print(min(temp_dic.values()) ,"testest")
  # print(min(flag_dict[current_flag].values()), "testetst")
  while points < p:
    # current_point(min(flag_dict, key=lambda k:float(flag_dict[k][current_point])))
    # output.append(min(flag_dict, key=lambda k:float(flag_dict[k][current_point])))
    # print(min(flag_dict[current_flag].values()), "testetst")
    
    # print(flag_dict['sp'],'hi')
    for key in flag_dict[current_flag]:
      for key2 in key:
        if key2[0] < current_distance and key2 not in output:
          current_distance = key2[0]
          current_point = key2
          current_flag = key2
    output.append(current_flag)
    current_distance = 100000000
    points += flag_dict(current_flag)

  return output

def flag_data(flags, p):
  output = {
  }
  current_flag = ["sp", 0,0,0]

  for flag in flags:
    # distance = get_distance(current_flag, flag)
    for flag2 in flags:
      distance = get_distance(current_flag, flag2)
      output.setdefault(current_flag[0], {})[flag2[0]] = {"distance":distance, "points":float(flag2[1])}
    current_flag = flag

  return output


def to_dict2(flags, p):
  output = {
  }
  current_flag = ["sp", 0,0,0]

  for flag in flags:
    
    for flag2 in flags:
      distance = get_distance(current_flag, flag2)
      output.setdefault(current_flag[0], {})[flag2[0]] = {"distance":distance, "points":float(flag2[1])}
    current_flag = flag

  return output

def get_distance(node_A, node_B):
  # return ((float(node_A[2]) - float(node_B[2])) ** 2 + (float(node_A[3]) - float(node_B[3])) ** 2) ** 0.5
  return sqrt(((float(node_A[2]) - float(node_B[2])) ** 2 + (float(node_A[3]) - float(node_B[3])) ** 2))

def get_distance2(node_A, node_B):
  return ((float(node_A[2-1]) - float(node_B[2-1])) ** 2 + (float(node_A[3-1]) - float(node_B[3-1])) ** 2) ** 0.5

#gets points gained per distance AKA effieciency 
def get_effieciency(distance, points):
  eff = float(points)/float(distance)
  return eff

def test_nn_v1(p, flags):
  output = []
  current_point = 0
  i=0
  sp = ["sp", 0,0,0]
  flags = get_ordered_list(flags, sp)
  while (current_point < p):
    output.append(flags[i])
    current_point += float(flags[i][1])
    i += 1
  
  return output


#ref from https://stackoverflow.com/questions/30636014/how-to-order-a-list-of-points-by-distance-to-a-given-point/30636169
def get_ordered_list(points, sp):
  #points.sort(key = lambda p: ((float(p[2]) - float(x))**2 + (float(p[3]) - float(y))**2)**(1/2))
  #  points.sort(key = lambda p: float(p[1])/((float(p[2]) - float(x))**2 + (float(p[3]) - float(y))**2)**(1/2), reverse=True)
  
  points.sort(key = lambda p: get_distance(p, sp))
  # points.sort(key=lambda p: (-p[1]))
  return points

#code from http://pedrohfsd.com/2017/08/09/2opt-part1.html
def two_opt(route, flag_dict2):
     best = route
     improved = True
     while improved:
          improved = False
          for i in range(1, len(route)-2):
               for j in range(i+1, len(route)):
                    if j-i == 1: continue # changes nothing, skip then
                    new_route = route[:]
                    new_route[i:j] = route[j-1:i-1:-1] # this is the 2woptSwap
                    if get_route_distance(new_route, flag_dict2) < get_route_distance(best, flag_dict2):
                         best = new_route
                         improved = True
          route = best
     return best

def get_route_distance(route, flag_dict):
  output = 0
  for i in range(len(route)-1):
    output += get_distance(route[i], route[i+1])

  # curr_flag = flag_dict[route[0][0]]
  # for i in range(len(route)-1):
  #   next_flag = flag_dict[route[i+1][0]]
  #   output += get_distance2(curr_flag, next_flag)
  #   curr_flag = next_flag

  # current_temp = [route[0]] + flag_dict[route[0][0]]
  # for i in range(len(route)-1):
  #   next_temp = [route[i+1]] + flag_dict[route[i+1][0]]
  #   output += get_distance(current_temp, next_temp)
  #   current_temp = next_temp
  # output += get_distance(current_temp,next_temp)

  

  # current_flag = route[0][0]
  # for i in range(1,len(route)):
  #   next_flag = route[i][0]
  #   output += flag_dict[current_flag][next_flag]['distance']
  #   current_flag = next_flag
    
  return output


def deflag(flags):
  output = []
  for flag in flags:
    output.append(flag[0])
  return output