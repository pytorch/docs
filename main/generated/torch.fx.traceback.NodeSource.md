# NodeSource

*class*torch.fx.traceback.NodeSource(*node*, *pass_name=''*, *action=None*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/fx/traceback.py#L88)

NodeSource is a data structure that contains the provenance information of a node.
If node a is created from node b, then a.meta["from_node"] may contain NodeSource(b).

Warning

This API is experimental and is *NOT* backward-compatible.