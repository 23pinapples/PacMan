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

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
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
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    solution = []
    visited = {}  # dict storing what has been visited or not
    parents = {}  # dictionary linking node to parent
    stack = util.Stack()

    start = problem.getStartState()
    if problem.isGoalState(start):
        return solution

    stack.push((start, 'Undefined', 0))  # fringenode, direction, cost
    visited[start] = 'Undefined'
    currState = start


    while (not problem.isGoalState(currState[0])):  # and (not stack.isEmpty()):
        currState = stack.pop()
        successors = problem.getSuccessors(currState[0])
        visited[currState[0]] = currState[1]
        if (problem.isGoalState(currState[0])):
            solState = currState[0]
            break

        for succ in successors:
            if succ[0] not in visited.keys():
                parents[succ[0]] = currState[0]
                stack.push(succ)

    while (solState in parents.keys()):
        solPrev = parents[solState]
        solution.insert(0, visited[solState])
        solState = solPrev

    return solution

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    visited = {}
    queue = util.Queue()
    parents = {}
    solution = []
    start = problem.getStartState()
    queue.push((start, 'Undefined', 0))
    visited[start] = 'Undefined'

    if problem.isGoalState(start):
        return solution

    while not queue.isEmpty():
        curr = queue.pop()
        visited[curr[0]] = curr[1]
        successors = problem.getSuccessors(curr[0])
        if (problem.isGoalState(curr[0])):
            solState = curr[0]
            break
        for succ in successors:
            if succ[0] not in visited.keys() and succ[0] not in parents.keys():
                parents[succ[0]] = curr[0]
                queue.push(succ)

    while (solState in parents.keys()):
        solPrev = parents[solState]
        solution.insert(0, visited[solState])
        solState = solPrev

    return solution

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    visited = {}
    queue = util.PriorityQueue()
    parents = {}
    solution = []
    cost = {}

    start = problem.getStartState()
    if problem.isGoalState(start):
        return solution

    queue.push((start, 'Undefined', 0), 0)
    visited[start] = 'Undefined'
    cost[start] = 0

    while not queue.isEmpty():
        curr = queue.pop()
        visited[curr[0]] = curr[1]
        successors = problem.getSuccessors(curr[0])
        if problem.isGoalState(curr[0]):
            solState = curr[0]
            break

        for succ in successors:

            if succ[0] not in visited.keys():
                sumCost = succ[2] + curr[2]
                if succ[0] in cost.keys() and cost[succ[0]] < sumCost:
                    continue
                queue.push((succ[0], succ[1], sumCost), sumCost)
                parents[succ[0]] = curr[0]
                cost[succ[0]] = sumCost

    while (solState in parents.keys()):
        solPrev = parents[solState]
        solution.insert(0, visited[solState])
        solState = solPrev


    return solution




def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    visited = {}
    solution = []
    queue = util.PriorityQueue()
    parents = {}
    cost = {}

    start = problem.getStartState()
    if problem.isGoalState(start):
        return solution

    queue.push((start,'Undefined',0), 0)
    visited[start] = 'Undefined'
    cost[start] = 0
    #print start[0]

    while not queue.isEmpty():
        curr = queue.pop()
        #print curr
        visited[curr[0]] = curr[1]
        if problem.isGoalState(curr[0]):
            solState = curr[0]
            break
        successors = problem.getSuccessors(curr[0])
        for succ in successors:
            if succ[0] not in visited.keys():
                costH = curr[2] + succ[2] + heuristic(succ[0], problem)
                if succ[0] in cost.keys():
                    if cost[succ[0]] <= costH:
                        continue
                queue.push((succ[0], succ[1], succ[2]+curr[2]), costH)
                cost[succ[0]] = costH
                parents[succ[0]] = curr[0]

    while (solState in parents.keys()):
        solPrev = parents[solState]
        solution.insert(0, visited[solState])
        solState = solPrev

    return solution

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
