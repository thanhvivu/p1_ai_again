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
        hanh_dong, stepCost), where 'successor' is a successor to the current
        state, 'hanh_dong' is the hanh_dong required to get there, and 'stepCost' is
        the incremental chi_phi of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOflist_hanh_dong(self, list_hanh_dong):
        """
         list_hanh_dong: A list of list_hanh_dong to take

        This method returns the total chi_phi of a particular sequence of list_hanh_dong.
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

    Your search algorithm needs to return a list of list_hanh_dong that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    "*** YOUR CODE HERE ***"

    Nut_batdau = problem.getStartState()
    if problem.isGoalState(Nut_batdau):
        # kiem tra nut bat dau co phai la dich khong
        return []
#  stack la hang doi duyet theo nguyen tac cuoi vao dau ra
    hang_duyet = util.Stack()
    Nut_da_di_qua = []
# tao mot mang cac nut da di qua
    hang_duyet.push((Nut_batdau, []))
    # day nut bat dau vao hang duyet
    while not hang_duyet.isEmpty():
        # tiep tuc vong lap khi hang duyet khong rong (di het cac nut ma van chua toi dich)
        Nut_hien_tai, list_hanh_dong = hang_duyet.pop()
        if Nut_hien_tai not in Nut_da_di_qua:
            Nut_da_di_qua.append(Nut_hien_tai)
            # neu nut hien tai dang xet khong nam trong mang da di qua, them nut hien tai vao mang do
            if problem.isGoalState(Nut_hien_tai):
                return list_hanh_dong
                # neu nut hien tai da den nut dich thi tra ve list hanh dong da thuc thi
            for nut_tiep_theo, hanh_dong,chi_phi in problem.getSuccessors(Nut_hien_tai):
                list_hanh_dong_moi = list_hanh_dong + [hanh_dong]
                hang_duyet.push((nut_tiep_theo, list_hanh_dong_moi))

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    Nut_batdau = problem.getStartState()
    if problem.isGoalState(Nut_batdau):
        # kiem tra nut bat dau co phai la dich khong
        return []
#  stack la hang doi duyet theo nguyen tac dau vao dau ra
    hang_duyet = util.Queue()
    Nut_da_di_qua = []
# tao mot mang cac nut da di qua
    hang_duyet.push((Nut_batdau, []))
    # day nut bat dau vao hang duyet
    while not hang_duyet.isEmpty():
        # tiep tuc vong lap khi hang duyet khong rong (di het cac nut ma van chua toi dich)
        Nut_hien_tai, list_hanh_dong = hang_duyet.pop()
        if Nut_hien_tai not in Nut_da_di_qua:
            Nut_da_di_qua.append(Nut_hien_tai)
            # neu nut hien tai dang xet khong nam trong mang da di qua, them nut hien tai vao mang do
            if problem.isGoalState(Nut_hien_tai):
                return list_hanh_dong
                # neu nut hien tai da den nut dich thi tra ve list hanh dong da thuc thi
            for nut_tiep_theo, hanh_dong,cost in problem.getSuccessors(Nut_hien_tai):
                list_hanh_dong_moi = list_hanh_dong + [hanh_dong]
                hang_duyet.push((nut_tiep_theo, list_hanh_dong_moi))


def uniformCostSearch(problem):
    "Search the node of least total chi_phi first. "
    "*** YOUR CODE HERE ***"

    Nut_batdau = problem.getStartState()
    if problem.isGoalState(Nut_batdau):
        return []

    Nut_da_di_qua = []
# hang doi co uu tien
    pQueue = util.PriorityQueue()
    #((coordinate/node , hanh_dong to current node , chi_phi to current node),priority)
    pQueue.push((Nut_batdau, [], 0), 0)

    while not pQueue.isEmpty():

        Nut_hien_tai, list_hanh_dong, tong_chi_phi = pQueue.pop()
        if Nut_hien_tai not in Nut_da_di_qua:
            Nut_da_di_qua.append(Nut_hien_tai)

            if problem.isGoalState(Nut_hien_tai):
                return list_hanh_dong

            for Nut_tiep_theo, hanh_dong, chi_phi in problem.getSuccessors(Nut_hien_tai):
                list_hanh_dong_moi = list_hanh_dong + [hanh_dong]
                priority = tong_chi_phi + chi_phi
                pQueue.push((Nut_tiep_theo, list_hanh_dong_moi, priority),priority)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the chi_phi from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined chi_phi and heuristic first."""
    "*** YOUR CODE HERE ***"

    Nut_batdau = problem.getStartState()
    if problem.isGoalState(Nut_batdau):
        return []

    Nut_da_di_qua = []

    pQueue = util.PriorityQueue()
    #((coordinate/node , hanh_dong to current node , chi_phi to current node),priority)
    pQueue.push((Nut_batdau, [], 0), 0)

    while not pQueue.isEmpty():

        Nut_hien_tai, list_hanh_dong, tong_chi_phi = pQueue.pop()

        if Nut_hien_tai not in Nut_da_di_qua:
            Nut_da_di_qua.append(Nut_hien_tai)

            if problem.isGoalState(Nut_hien_tai):
                return list_hanh_dong

            for Nut_tiep_theo, hanh_dong, chi_phi in problem.getSuccessors(Nut_hien_tai):
                list_hanh_dong_moi = list_hanh_dong + [hanh_dong]
                newCostToNode = tong_chi_phi + chi_phi
                heuristicCost = newCostToNode + heuristic(Nut_tiep_theo,problem)
                pQueue.push((Nut_tiep_theo, list_hanh_dong_moi, newCostToNode),heuristicCost)

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
