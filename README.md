## Tic-Tac-Toe using minimax algorithm in python ##

- This is Tic Tac Toe game using Minimax algorithm with alpha-beta pruning.
- This algorithm recursively searches the game tree and returns the best move that leads the Max player to win or atleast not lose. 
- Minimax principle: compute the utility of being in a state assuming both players play optimally from there until the end of the game
- Now propagate minimax values up the tree once terminal nodes are discovered.
- Utility(s,p) function or Objective function for a game that ends in terminal state 's' for player p. For tic-tac-toe we use a utility of +1 for win, -1 for loss and 0 for draw.
-  Alpha-Beta pruning is an optimization technique for minimax algorithm. It eliminates the large parts of the tree because there already exists a better move available. Using this the computation time reduces by a huge factor.
- It keeps track of two bounds, namely alpha and beta.
- Alpha stores the largest value for Max across seen children (current lower bound on MAX's outcome).
- Beta stores the lowest value for Min across seen children (current upper bound on MIN's outcome).
- We update the values of alpha and beta by propagating upwards from terminal nodes.
- Update alpha only at Max nodes and update beta only at Min nodes.
- Prune any remaining branches whenever alpha greater than or equal to beta.
### This Algorithm is widely used in games such as Tic-Tac-Toe, Chess, Backgammon etc. These are known as Zero-sum games as one player wins (+1) and other player loses (-1) or both neither wins nor loses (draw) (0). ###