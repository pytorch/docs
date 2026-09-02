# torch.autograd.graph.Node.next_functions

*abstract property*Node.next_functions*: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[Node | [None](https://docs.python.org/3/library/constants.html#None), [int](https://docs.python.org/3/library/functions.html#int)], ...]*

Return the edges from this node to its input functions.

Each entry is a `(Node, int)` pair. The node is `None` for an input
that does not require gradients. The integer is the output index of the
input function to which this edge connects.