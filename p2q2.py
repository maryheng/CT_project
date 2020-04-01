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
