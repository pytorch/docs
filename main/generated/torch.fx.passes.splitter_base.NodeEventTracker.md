# NodeEventTracker

*class*torch.fx.passes.splitter_base.NodeEventTracker(*tracker_mode*, *dump_prefix*)[[source]](https://github.com/pytorch/pytorch/blob/25af31d252bc789059a6c3b5511977f4fa7d1d4e/torch/fx/passes/splitter_base.py#L174)

Tracks node events during the splitter execution.

Warning

This API is experimental and is *NOT* backward-compatible.

add(*node*, *desc*, *dep=None*)[[source]](https://github.com/pytorch/pytorch/blob/25af31d252bc789059a6c3b5511977f4fa7d1d4e/torch/fx/passes/splitter_base.py#L189)

Add a new event to the tracker.

dump()[[source]](https://github.com/pytorch/pytorch/blob/25af31d252bc789059a6c3b5511977f4fa7d1d4e/torch/fx/passes/splitter_base.py#L247)

Function to be invoked at the end of the finder execution to printout tracked events specified by the mode.

print_all(*writer=None*)[[source]](https://github.com/pytorch/pytorch/blob/25af31d252bc789059a6c3b5511977f4fa7d1d4e/torch/fx/passes/splitter_base.py#L236)

Print all nodes in a list.
@param writer: function to write to file. If None, use print.

print_node(*node_name*, *recursive=False*, *tab=''*, *writer=None*)[[source]](https://github.com/pytorch/pytorch/blob/25af31d252bc789059a6c3b5511977f4fa7d1d4e/torch/fx/passes/splitter_base.py#L201)

Print a node and its events.
@param recursive: if True, print nodes that caused the events on this current node.
@param tab: Indentation for dependencies.
@param writer: function to write to file. If None, use print.

to_dict()[[source]](https://github.com/pytorch/pytorch/blob/25af31d252bc789059a6c3b5511977f4fa7d1d4e/torch/fx/passes/splitter_base.py#L224)

Create dict dump on all events.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]]