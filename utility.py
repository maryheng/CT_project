# utility.py v1.0

import csv

# reads a CSV file and returns every line as a list
# e.g. for a CSV file with the following 2 lines:
#   apple, orange
#   banana, durian
# this function will return this list: [['apple', ' orange'], ['banana', ' durian']]
def list_reader(csv_file):
  the_list = []
  with open(csv_file, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    for row in csv_reader:
      the_list.append(row)
  return the_list


# calculates euclidian distance between two points (float). 
def get_distance(node_A, node_B):
  return ((node_A[2] - node_B[2]) ** 2 + (node_A[3] - node_B[3]) ** 2) ** 0.5


# returns dictionary that looks like this:
#    key/value: flagID/[flagID, points, x, y]
#    e.g. {'F001': ['F001', 9, 34.20121897, -23.8463234], 'F002': ['F001', 2, 27.71818372, 7.088271019]....}
def generate_flags_dict(flags_list):
  d = {}
  for item in flags_list:
    #             flagID,  points,       x,              y
    d[item[0]] = [item[0], int(item[1]), float(item[2]), float(item[3])]
  return d


# checks if your answer (route) has syntax errors
def get_syntax_error_msg_q1(your_route):
  if type(your_route) != list:
    return "Your answer is not a list. Your route must be a list of flag IDs"

  if not all(type(elem)==str for elem in your_route):
    return "Your answer must be a list of strings (FlagIDs) only."

  # check if there are duplicate flagIDs in your_route
  if len(your_route) != len(set(your_route)):
    return "There are duplicate flag IDs in your route. FlagIDs in your route must be unique."

  return None # all ok

# checks if your answer (routes) has syntax errors
def get_syntax_error_msg_q2(your_routes, n):
  if type(your_routes) != list:
    return "Your answer is not a list. Your route must be a 2D list of flag IDs"

  if not all(type(elem)==list for elem in your_routes):
    return "Your answer must be a list of lists."

  if len(your_routes) != n:
    return "Your answer has " + str(len(your_routes)) + " routes. This does not match n. n is " + str(n)

  for route in your_routes:
    if not all(type(elem)==str for elem in route):
      return "Your answer must be a list of list of strings (FlagIDs) only."

  # check if there are duplicate flagIDs in all routes
  flat_list = [item for sublist in your_routes for item in sublist]
  if len(flat_list) != len(set(flat_list)):
    return "There are duplicate flag IDs in your routes. Routes must not share common flag IDs"
    
  return None # all ok



# used for computing quality score for Q1
# will return error message (string) if there is an error
# returns error_msg (or None if all ok), score (tot dist travelled), accumulated points (for comparison with p)
def get_dist_and_points_q1(your_route, flags_dict, v, verbose=False):

  # check for syntax error first
  err_msg = get_syntax_error_msg_q1(your_route)
  if err_msg != None:
    return err_msg, 0, 0


  # calculate distance and points
  dist = 0
  points = 0

  start_node = ["Start", 0, 0, 0] # starting point (0, 0)
  last_node = start_node
  
  for flagID in your_route:
    if not flagID in flags_dict:
      return "Flag ID in your route is not valid : " + flagID, 0, 0 # error

    curr_node = flags_dict[flagID]
    dist_to_curr_node = get_distance(last_node, curr_node)
    dist += dist_to_curr_node
    points += curr_node[1]
    
    if verbose:
      print("last_node:" + str(last_node) + ", curr_node:" + str(curr_node))
      print("dist_to_curr_node:" + str(dist_to_curr_node))
      print("dist so far:" + str(dist) +", points so far:" + str(points) + "\n---")

    last_node = curr_node

  # to go back to SP?
  if v == 2:   # cycle back to SP
    dist += get_distance(last_node, start_node)
    if verbose: print("v = 2, so go back to SP")

  if verbose:
    print("final dist for this route:" + str(dist) + "\n---")
    
  return None, dist, points # no error


# used for computing quality score for Q2
# will return error message (string) if there is an error
# returns error_msg (or None if all ok), score (tot dist travelled), accumulated points (for comparison with p)
def get_dist_and_points_q2(your_routes, flags_dict, v, n, verbose=False):

  # check for syntax error first
  err_msg = get_syntax_error_msg_q2(your_routes, n)
  if err_msg != None:
    return err_msg, 0, 0
  
  # need to call get_dist_and_points_q1 for every route in your_routes
  tot_dist = 0
  tot_points = 0
  
  for route in your_routes:
    err_msg, curr_dist, curr_points = get_dist_and_points_q1(route, flags_dict, v, verbose)

    if err_msg != None:
      return err_msg, 0, 0

    tot_dist += curr_dist
    tot_points += curr_points

    if verbose:
      print("dist for this route  :" + str(curr_dist)   + ", tot distance so far:" + str(tot_dist))
      print("points for this route:" + str(curr_points) + ", tot points so far:"   + str(tot_points))
      print("============================================")
      
  return None, tot_dist, tot_points   # all OK
   
