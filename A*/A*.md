/**
# A* (A-star) — Documentation

## Summary (short)
A* is a very useful and smart BFS algorithm to search for the shortest node from start node to an end node in state-space graphs. General formula is f(n) = g(n) + h(n), g(n) is the shortest distance from start to n-node in the graph meanwhile h(n) is heruistic which is basically nothing but a smart guess from n node to the goal node(neighboring since BFS). h(n) is pretty vital when it comes to A* since A* cost and performance heavily relies on h(n)'s quality. Ideally, h(n) must be admissable which means never overestimate the distance but can be underestimate or equal to distance between n-node to goal.

---

## Formal / Theoretical Description

- Problem model
  - State space as a directed (or undirected) weighted graph G = (V, E) with nonnegative edge costs.
  - A start node s belongs to V and a set of goal nodes G is a subset of V.
  - The objective is to find a path from s to some g ∈ G minimizing path cost (sum of edge weights).

- Core quantities
  - g(n): exact cost of the best known path from the start node s to node n.
  - h(n): heuristic estimate of the minimal cost from n to any goal (domain knowledge).
  - f(n) = g(n) + h(n): estimated total cost of a path through n to a goal.

- Node selection and data structures
  - Open set: a priority queue ordered by f(n) (ties broken deterministically).
  - Closed set (or explored set): nodes already expanded (prevents immediate re-expansion in graph search).
  - Expansion: remove node n with minimal f(n) from open, generate successors, relax/update g and f values, insert/update open as appropriate.

- Admissibility and optimality
  - Admissible heuristic: ∀n, h(n) ≤ h*(n) where h*(n) is the true minimal remaining cost. If h is admissible, A* (tree search) is admissible: the first goal popped from open has minimal possible cost.
  - Consistent (monotone) heuristic: ∀(n, n'), h(n) ≤ c(n, n') + h(n'). Consistency implies f-values along any path are nondecreasing (f(n') ≥ f(n) for child n' of n). Consistency ensures that once a node is expanded in graph search its g-value is optimal and it need not be reopened; thus consistency simplifies correctness and implementation.
  - Graph-search correctness: with admissible h and correct handling of node re‑insertion on improved g, A* will find an optimal path. Consistency obviates the need to reopen nodes.

- Completeness
  - A* is complete (will find a solution if one exists) provided branching factor is finite and there is a positive lower bound ε > 0 on step costs (prevents infinite sequences of zero‑cost moves). Practical implementations also rely on finite memory.

- Complexity
  - Worst‑case time complexity is exponential in the depth (or cost) of the optimal solution; typical notation O(b^d) where b is the branching factor and d is the depth of the optimal solution in unweighted uniform branching models.
  - Informedness and effective branching factor: the practical expense depends on heuristic quality. Better (more informative) heuristics reduce the number of expanded nodes; the effective branching factor b* quantifies that reduction.
  - Memory complexity is likewise high: A* stores all generated nodes (open + closed), so peak memory often grows exponentially with solution depth. This is the primary practical limitation of plain A*.

- Heuristic design and properties
  - Admissibility is necessary for guaranteed optimality; consistency is stronger and often desirable for graph search.
  - Dominance: if h1(n) ≥ h2(n) for all n and both are admissible, then h1 dominates h2 and A* with h1 will expand no more nodes than with h2 (typically fewer).
  - Common admissible heuristics: exact solution to a relaxed version of the problem, Manhattan distance (grid with 4‑neighborhood), Euclidean distance (continuous plane), pattern databases (precomputed exact costs for subproblems).
  - Weighted A*: f(n) = g(n) + w·h(n) (w > 1) trades solution optimality for fewer expansions (approximate, faster). When w = 1, standard A*.

- Practical considerations
  - Tie‑breaking: when f values tie, choosing the node with larger g (i.e., deeper node) can reduce expansions and reach goal earlier in practice.
  - Duplicate detection and path improvement: for graph search maintain a map of best g values per state; if a better path to an already discovered state is found, update and reinsert as needed (unless heuristic is consistent).
  - Variants for memory limits: IDA* (iterative deepening A*), SMA* (simplified memory‑bounded A*), beam search and others reduce memory at the cost of other tradeoffs.

- Correctness sketch (admissibility)
  - Let C* be the optimal solution cost. Suppose A* returns a goal G' with cost C > C*. At the moment A* pops G' from open, consider any node n on an optimal path to the true goal with f(n) ≤ C*. Because h is admissible, for nodes on an optimal prefix f(n) ≤ C*. A* pops nodes in nondecreasing f order, so it must pop some node on the optimal path before popping G', contradiction. Hence A* cannot pop a suboptimal goal.

---

## Intuition / Layman's Explanation

- What A* does, simply:
  - Imagine you want the fastest route on a map from your home to a destination. For every intersection you consider you know:
    1. How far you've already driven to get there (g).
    2. A guess for how far it still is to the destination (h), e.g., "as the crow flies".
  - A* always explores the intersection that looks most promising by adding what you've done so far to what seems left (g + h). It repeats until it reaches the destination.
  - If your guess (h) never overestimates the true remaining distance, the first time you actually reach the destination you'll have taken the shortest possible route.

- Why heuristics matter
  - If your guess is terrible (e.g., always zero), A* becomes Dijkstra's algorithm: correct but potentially very slow. If your guess is great (closer to the true remaining cost), A* will explore far fewer roads and find the answer quickly.
  - If your guess overestimates (says it’s farther than it really is), you might find a route quickly but it could be suboptimal (not the shortest).

- Practical tradeoffs
  - A* is powerful and often the algorithm of choice for pathfinding and many search problems, but it can require a lot of memory because it remembers lots of partial routes. If memory is limited, use memory‑bounded variants (IDA*, SMA*) or accept approximate solutions (weighted A*).

---

## Quick Practical Checklist
- Use an admissible heuristic to guarantee optimality.
- Prefer consistent heuristics for simpler graph‑search implementations (no reopenings).
- Profile and measure the effective branching factor; improve heuristics if expansions are too many.
- Watch memory use: A* holds both open and closed sets; consider memory‑bounded variants for large problems.
- Consider tie‑breaking strategies (e.g., prefer larger g on equal f) to reduce unnecessary expansions.
- For faster but approximate results, use Weighted A* (w > 1), accepting a bounded suboptimality.

*/