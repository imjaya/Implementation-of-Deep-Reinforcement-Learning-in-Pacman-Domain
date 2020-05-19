# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
import heapq 
  
from heapq import heappush, heappop
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    expandable_nodes=util.Stack();   # Creating a Stack to store all the nodes that can be explored its srored and accessed in Last-In-First-Out Manner
    #expandable_nodes = util.Queue()   
    already_visited = []   # An List to maintain all the visited nodes
    expandable_nodes.push((problem.getStartState(), []))   # The nodes are pushed from the start node till the current node
    while True:
        #print("inside while")
        node, path_to_the_node = expandable_nodes.pop()
        
        if problem.isGoalState(node):   # If current node = Goal node then exit
            #print("inside if")
            break
        else:
            if node not in already_visited:  # Ensuring not to visit already visited nodes that are stored in the already_visited list
                #print("inside else-if")
                already_visited.append(node)    # If new node occurs it is added to already_visited list.
                successors = problem.getSuccessors(node)  #Accesing succesive node to the current node
                
                
                
                
                
                for successor in successors:
                    
                    
                    next_path = successor[1]
                    
                    next_node= successor[0]

                    #next_path=successor[1]
                    total_path = path_to_the_node + [next_path]    # Calculating path from start node to children node
                    expandable_nodes.push((next_node, total_path))   # Adding the child node to the expandable_nodes 

    return path_to_the_node





def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    expandable_nodes=util.Queue();   # Creating a Queue to store all the nodes that can be explored its srored and accessed in First-In-First-Out Manner
    #expandable_nodes = util.Stack()   
    already_visited = []   # An List to maintain all the visited nodes
    expandable_nodes.push((problem.getStartState(), []))   # The nodes are pushed from the start node till the current node
    while True:
        #print("inside while")
        node, path_to_the_node = expandable_nodes.pop()
        
        if problem.isGoalState(node):   # If current node = Goal node then exit
            #print("inside if")
            break
        else:
            if node not in already_visited:  # Ensuring not to visit already visited nodes that are stored in the already_visited list
                #print("inside else-if")
                already_visited.append(node)    # If new node occurs it is added to already_visited list.
                successors = problem.getSuccessors(node)  #Accesing succesive node to the current node
                
                
                
                
                
                for successor in successors:
                    #print("inside for")
                    
                    
                    child_path = successor[1]
                    
                    child_node= successor[0]

                    #child_path=successor[1]
                    total_path = path_to_the_node + [child_path]    # Calculating path from start node to children node
                    expandable_nodes.push((child_node, total_path))   # Adding the child node to the expandable_nodes 

    return path_to_the_node


def uniformCostSearch(problem):
    expandable_nodes = util.PriorityQueue()       #Creating a Priority queue in order to pop out node that has higher priority
    already_visited = []                          # The UCS algorithm is similar to bfs algorithm where it explores nodes based upon priority
    expandable_nodes.push((problem.getStartState(), [], 0), 0)   # we get the current state(start state) 
    while expandable_nodes.isEmpty()==0:
        #print("inside while")
        n_state,path_till_node,cost_till_node = expandable_nodes.pop()
        if problem.isGoalState(n_state):   # checking if the current state is goal state or not
            #print("inside if")
            break
        else:
            if n_state not in already_visited:   #if the current node is not already visited, then it is added.
                #print("inside else if")
                already_visited.append(n_state)    
                next = problem.getSuccessors(n_state)
                for successor in next:
                    next_node,next_path,next_cost = successor
                    totla_path = path_till_node + [next_path]   # calculating the path from start node to children node
                    totla_cost = cost_till_node + next_cost     # calculating the total cost
                    expandable_nodes.push((next_node, totla_path, totla_cost), totla_cost) #child node is added to expandable_nodes along with its cost and path 
    return path_till_node     

    #util.raiseNotDefined()


   




def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    expandable_nodes = util.PriorityQueue()       #Creating a Priority queue in order to pop out node that has higher priority
    already_visited = []                          # The UCS algorithm is similar to bfs algorithm where it explores nodes based upon priority
    expandable_nodes.push((problem.getStartState(), [], 0), 0)   # we get the current state(start state) 
    while expandable_nodes.isEmpty()==0:
         #print("inside while")
        
        n_state,path_till_node,cost_till_node = expandable_nodes.pop()
        if problem.isGoalState(n_state):   # checking if the current state is goal state or not
             #print("inside if")
            break
        else:
            if n_state not in already_visited:   #if the current node is not already visited, then it is added.
                 #print("inside else if")
                already_visited.append(n_state)    
                next = problem.getSuccessors(n_state)
                for successor in next:
                    child_node,child_path,child_cost = successor
                    totla_path = path_till_node + [child_path]   # calculating the path from start node to children node
                    totla_cost = cost_till_node + child_cost     # calculating the total cost
                    expandable_nodes.push((child_node, totla_path, totla_cost), totla_cost+heuristic(child_node,problem)) #child node is added to expandable_nodes along with its cost and path the heuristic cost is also taken into consideration by adding it to the path cost
    #util.raiseNotDefined()
    return path_till_node     

    
    


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
