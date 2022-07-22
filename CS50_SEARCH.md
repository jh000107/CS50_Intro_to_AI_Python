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