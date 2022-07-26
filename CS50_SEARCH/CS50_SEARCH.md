# SEARCH

> Search problems involve an agent that is given an initial state and a goal state, and it returns a solution of how to get from the former to the latter. A navigator app uses a typical search process, where the agent (the thinking part of the program) receives as input your current location and your desired destination, and, based on a search algorithm, returns a suggested path.

## TERMS

- [ ] Agent

  An entity that perceives its environment and acts upon that environment.					<img src="CS50_SEARCH.assets/15puzzle.png" alt="15 puzzle" style="zoom:25%;" />

- [ ] State

  - A configuration of an agent in its environment.

- [ ] Actions

  - Choices that can be made in a state. More precisely, actions can be defined as a function. Upon receiving state `s` as input, `Actions(s)` returns as output the set of actions that can be executed in state `s` .

- [ ] Transition Model

  - A description of what state results from performing any applicable action in any state. More precisely, the transition model can be defined as a function. Upon receiving state `s` and action `a` as input, `Results(s,a)` returns the state resulting from performing action `a` in state `s`.

- [ ] State Space

  - The set of all states reachable from the initial state by any sequence of actions.

  <img src="CS50_SEARCH.assets/statespace.png" alt="State Space" style="zoom:67%;" />

- [ ] Goal Test

  - The condition that determines whether a given state is a goal state.

- [ ] Path Cost

  - A numerical cost associated with a given path.

- [ ] Solution
  - A sequence of actions that leads from the initial state to the goal state.
- [ ] Optimal Solution
  - A solution that has the lowest path cost among all solutions.

## Solving Search Problems

In a search process, data is often stored in a **node**, a data structure that contains the following data:

- A state
- Its *parent node*, through which the current node was generated
- The *action* that was applied to the state of the parent to get to the current node
- The *path cost* from the initial state to this node

To actually search, we use the **frontier**, the mechanism that "manages" the nodes. The *frontier* starts by containing an initial state and an empty set of explored items, and then repeats the following actions until a solution is reached:

Repeat:

1. If the frontier is empty,
   - STOP. There is no solution to the problem.
2. Remove a node from the frontier. This is the node that will be considered.
3. If the node contains the goal state,
   - Return the solution. STOP

Else,

```
* Expand the node (find all the new nodes that could be reached from this node), and add resulting nodes to the frontier
* Add the current node to the explored set.
```

**Depth-First Search**

In the previous description of the *frontier*, one thing went unmentioned. Which node should be removed? This choice has implications on the quality of the solution and how fast it is achieved. There are multiple ways, two of which can be represented by the data structures of **stack**(in depth-first search) and **queue**(breadth-first search)

A *depth-first* search algorithm exhausts each one direction before trying another direction. In these cases, the frontier is managed as a *stack* data structure. "*Last-in first-out*". This results in a search algorithm that goes as deep as possible in the first direction that gets in its way while leaving all other directions for later.

- Pros:
  - At best, this algorithm is the fastest. If we are lucky and it always chooses the right path to the solution, then it takes the least possible time to get to a solution.
- Cons:
  - It is possible that the found solution is not optimal.
  - At worst, this algorithm will explore every possible path before finding the solution, thus taking the longest possible time before reaching the solution.

Code example:

```python
# Define the function that removes a node from the frontier and returns it.
def remove(self):
    #T Terminate the search if the frontier is empty, because this means that there is no solution.
    if self.empty():
        raise Exception("empty frontier")
    else:
       	# Save the last item in the list (which is the newest node added)
        node = self.frontier[-1]
        # Save all the items on the list besides the last node (i.e removing the last node)
        self.frontier = self.frontier[:-1]
        return node
```

**Breadth-First Search**

The opposite of depth-first search would be breath-first search.

A *breadth-first* search algorithm will follow multiple directions at the same time, taking one step in each possible direction before taking the second step in each direction. In this case, the frontier is managed as a *queue* data structure. "*first-in first-out*".

- Pros:
  - this algorithm is guaranteed to find the optimal solution.
- Cons:
  - This algorithm is almost guaranteed to take longer than the minimal time to run.
  - At worst, this algorithm takes the longest possible time to run.

Code example:

```python
# Define the function that removes a node from the frontier and returns it.
    def remove(self):
    	  # Terminate the search if the frontier is empty, because this means that there is no solution.
        if self.empty():
            raise Exception("empty frontier")
        else:
            # Save the oldest item on the list (which was the first one to be added)
            node = self.frontier[0]
            # Save all the items on the list besides the first one (i.e. removing the first node)
            self.frontier = self.frontier[1:]
            return node
```

**Greedy Best-First Search**

Breadth-first and depth-first are both **uninformed** search algorithms, meaning that these algorithms do not utilize any knowledge about the problem that they did not acquire through their own exploration. A type of algorithm that considers additional knowledge to try to improve its performance is called an **informed** search algorithm.

**Greedy best-first** search expands the node that is the closest to the goal, as determined by a **heuristic function** *h(n)*. The function estimates how close to the goal the next node is, but it can be mistaken. In a maze, an algorithm can use a heuristic function that relies on the **Manhattan distance** between the possible nodes and the end of the maze. The *Manhattan distance* ignores walls and counts how many steps it would take to get from one location to the goal location. 

![Manhattan Distance](CS50_SEARCH.assets/manhattandistance.png)

**A* Search**

A development of the *greedy best-first* algorithm, *A* search* considers not only *h(n)*, the estimated cost from the current location to the goal, but also *g(n)*, the cost that was accrued until the current location. By combining both these values, the algorithm has a more accurate way of determining the cost of the solution and optimizing its choices on the go. Once it exceeds the estimated cost of some previous option, the algorithm will ditch the current path and go back to the previous option, thus preventing itself from going down a long, inefficcient path that *h(n)* erroneously marked as best.

For A* search to be optimal, the heuristic function, h(n), should be:

1. *Admissible*, or never overestimating the true cost, and
2. *Consistent*, which means that the estimated path cost to the goal of a new node in addition to the cost of transitioning it from the previous node is greater or equal to the estimated path cost to the goal of the previous node. To put it an equation form, *h(n)* is consistent if for every node *n* and successor node *n'* with step cost *c*, *h(n) <= h(n')+c*

#### Adversarial Search

In **adversarial search**, the algorithm faces an opponent that tries to achieve the opposite goal. Often, AI that uses adversarial search is encountered in games, such as tic tac toe.

**Minimax**

A type of algorithm in adversarial search, Minimax represents winning conditions as (-1) for one side and (+1) for the other side. Further actions will be driven by these conditions,

**Representing a Tic-Tac-Toe AI:**

- *S₀*: Initial state (in our case, an empty 3X3 board)
- *Players(s)*: a function that, given a state *s*, returns which player’s turn it is (X or O).
- *Actions(s)*: a function that, given a state *s*, return all the legal moves in this state (what spots are free on the board).
- *Result(s, a)*: a function that, given a state *s* and action *a*, returns a new state. This is the board that resulted from performing the action *a* on state *s* (making a move in the game).
- *Terminal(s)*: a function that, given a state *s*, checks whether this is the last step in the game, i.e. if someone won or there is a tie. Returns *True* if the game has ended, *False* otherwise.
- *Utility(s)*: a function that, given a terminal state *s*, returns the utility value of the state: -1, 0, or 1.

**How the algorithm works:**

Recursively, the algorithm simulates all possible games that can take place beginning at the current state and until a terminal state is reached. Each terminal state is valued as either (-1), 0, or (+1).

![Minimax in Tic Tac Toe](CS50_SEARCH.assets/minimax_tictactoe.png)

To put it in pseudocode, the Minimax algorithm works the following way:

- Given a state *s*

  - The maximizing player picks action *a* in *Actions(s)* that produces the highest value of *Min-Value(Result(s, a))*.
  - The minimizing player picks action *a* in *Actions(s)* that produces the lowest value of *Max-Value(Result(s, a))*.

- Function *Max-Value(state)*

  - *v = -∞*

  - if *Terminal(state)*:

     return *Utility(state)*

  - for *action* in *Actions(state)*:

     *v = Max(v, Min-Value(Result(state, action)))*

    return *v*

- Function *Min-Value(state)*:

  - *v = ∞*

  - if *Terminal(state)*:

     return *Utility(state)*

  - for *action* in *Actions(state)*:

     *v = Min(v, Max-Value(Result(state, action)))*

    return *v*

**Alpha-Beta Pruning**

A way to optimize Minimax, Alpha-Beta Pruning skips some of the recursive computations that are decidedly unfavorable. After establishing the value of one action, if there is initial evidence that the following action can bring the opponent to get to a better score than the already established action, there is no need to further investigate this action.

![Alpha Beta Pruning](CS50_SEARCH.assets/alphabeta.png)



**Depth-Limited Minimax**

**Depth-limited Minimax** considers only a pre-defined number of moves before it stops, without ever getting to a terminal state. However, this doesn't allow for getting a precise value for each action, since the end of the hypothetical games has not been reached. To deal with this problem, Depth-limited Minimax relies on an **evaluation function** that estimates the expected utility of the game from a given state, or, assigns values to states. 

