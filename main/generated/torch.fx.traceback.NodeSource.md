# NodeSource

*class*torch.fx.traceback.NodeSource(*node*, *pass_name=''*, *action=None*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/fx/traceback.py#L89)

NodeSource is a data structure that contains the provenance information of a node.
If node a is created from node b, then a.meta["from_node"] may contain NodeSource(b).

Warning

This API is experimental and is *NOT* backward-compatible.