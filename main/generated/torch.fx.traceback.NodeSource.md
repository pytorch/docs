# NodeSource

*class*torch.fx.traceback.NodeSource(*node*, *pass_name=''*, *action=None*)[[source]](https://github.com/pytorch/pytorch/blob/c0efb74fed099321e3bbddbd846a41d15257615d/torch/fx/traceback.py#L89)

NodeSource is a data structure that contains the provenance information of a node.
If node a is created from node b, then a.meta["from_node"] may contain NodeSource(b).

Warning

This API is experimental and is *NOT* backward-compatible.