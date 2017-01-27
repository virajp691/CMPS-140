# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """

    def startingState(self):
        """
    Returns the start state for the search problem 
    """
        util.raiseNotDefined()

    def isGoal(self, state):  # isGoal -> isGoal
        """
    state: Search state

    Returns True if and only if the state is a valid goal state
    """
        util.raiseNotDefined()

    def successorStates(self, state):  # successorStates -> successorsOf
        """
    state: Search state
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
    """
        util.raiseNotDefined()

    def actionsCost(self, actions):  # actionsCost -> actionsCost
        """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
    """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
  Search the deepest nodes in the search tree first [p 85].
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.startingState()
  print "Is the start a goal?", problem.isGoal(problem.startingState())
  print "Start's successors:", problem.successorStates(problem.startingState())
  """
    # Initialize a LIFO Stack for the fringe,
    # a visited list to keep track of seen nodes,
    # and an empty list to store the final path
    from util import Stack
    fringe = Stack()
    visited = []
    final_path = []
    fringe.push((problem.startingState(), [], 1))
    while not fringe.isEmpty():
        state, nodepath, cost = fringe.pop()
        if problem.isGoal(state):
            final_path = nodepath
            print "Found Goal"
            break
        if state not in visited:
            visited.append(state)
            for successor in problem.successorStates(state):
                fringe.push((successor[0], nodepath + [successor[1]], cost))
    return final_path
    # return ['West', 'West', 'West', 'West', 'South','South', 'East', 'South', 'South', 'West']

def breadthFirstSearch(problem):
    "Search the shallowest nodes in the search tree first. [p 81]"
    from util import Queue
    fringe = Queue()
    visited = []
    final_path = []
    fringe.push((problem.startingState(), [], 1))

    while not fringe.isEmpty():
        state, nodepath, cost = fringe.pop()
        if problem.isGoal(state):
            final_path = nodepath
            print "Found Goal"
            break
        for successor in problem.successorStates(state):
            if successor[0] not in visited:
                visited.append(successor[0])
                fringe.push((successor[0], nodepath + [successor[1]], cost))
    return final_path

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    from util import PriorityQueue
    fringe = PriorityQueue()
    visited = []
    final_path = []
    fringe.push((problem.startingState(), [], 0), 0)
    while not fringe.isEmpty():
        state, nodepath, pathcost = fringe.pop()
        if problem.isGoal(state):
            final_path = nodepath
            print 'Found Goal'
            break
        visited.append(state)
        for successor in problem.successorStates(state):
            if successor[0] not in visited:
                fringe.push((successor[0], nodepath + [successor[1]], pathcost + successor[2]), pathcost + successor[2])
    return final_path


def nullHeuristic(state, problem=None):
    """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    from util import PriorityQueue
    fringe = PriorityQueue()
    final_path = []
    fringe.push((problem.startingState(), []), 0)
    # fValue is Cost so far from start
    fvalue = {problem.startingState(): 0}

    while not fringe.isEmpty():
        current, nodepath = fringe.pop()
        if problem.isGoal(current):
            final_path = nodepath
            print 'Found Goal'
            break
        for successor in problem.successorStates(current):
            cost = fvalue[current] + successor[2]
            if (successor[0] not in fvalue) or (cost < fvalue[successor[0]]):
                fvalue[successor[0]] = cost
                fringe.push((successor[0], nodepath + [successor[1]]), cost + heuristic(successor[0], problem))
    return final_path


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
