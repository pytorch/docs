# NodeEvent

*class*torch.fx.passes.splitter_base.NodeEvent(*source*, *desc*, *dep=None*)[[source]](https://github.com/pytorch/pytorch/blob/83e3e8add0ddb03f2c26481b528c463acdc7fb00/torch/fx/passes/splitter_base.py#L157)

An event in graph split that happened on a node.
source: Subject of the event
desc: readable description
dep: Optional dependency, usually the node that caused the event.

Warning

This API is experimental and is *NOT* backward-compatible.