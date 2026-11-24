# NodeEventTracker

*class*torch.fx.passes.splitter_base.NodeEventTracker(*tracker_mode*, *dump_prefix*)[[source]](https://github.com/pytorch/pytorch/blob/990e1ce56708ce777f2294c04f77e4c28c7ea900/torch/fx/passes/splitter_base.py#L181)

Tracks node events during the splitter execution.

Warning

This API is experimental and is *NOT* backward-compatible.

add(*node*, *desc*, *dep=None*)[[source]](https://github.com/pytorch/pytorch/blob/990e1ce56708ce777f2294c04f77e4c28c7ea900/torch/fx/passes/splitter_base.py#L196)

Add a new event to the tracker.

dump()[[source]](https://github.com/pytorch/pytorch/blob/990e1ce56708ce777f2294c04f77e4c28c7ea900/torch/fx/passes/splitter_base.py#L254)

Function to be invoked at the end of the finder execution to printout tracked events specified by the mode.

print_all(*writer=None*)[[source]](https://github.com/pytorch/pytorch/blob/990e1ce56708ce777f2294c04f77e4c28c7ea900/torch/fx/passes/splitter_base.py#L243)

Print all nodes in a list.
@param writer: function to write to file. If None, use print.

print_node(*node_name*, *recursive=False*, *tab=''*, *writer=None*)[[source]](https://github.com/pytorch/pytorch/blob/990e1ce56708ce777f2294c04f77e4c28c7ea900/torch/fx/passes/splitter_base.py#L208)

Print a node and its events.
@param recursive: if True, print nodes that caused the events on this current node.
@param tab: Indentation for dependencies.
@param writer: function to write to file. If None, use print.

to_dict()[[source]](https://github.com/pytorch/pytorch/blob/990e1ce56708ce777f2294c04f77e4c28c7ea900/torch/fx/passes/splitter_base.py#L231)

Create dict dump on all events.

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), [list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]