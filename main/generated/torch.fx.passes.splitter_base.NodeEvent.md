# NodeEvent

*class*torch.fx.passes.splitter_base.NodeEvent(*source*, *desc*, *dep=None*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/fx/passes/splitter_base.py#L150)

An event in graph split that happened on a node.
source: Subject of the event
desc: readable description
dep: Optional dependency, usually the node that caused the event.

Warning

This API is experimental and is *NOT* backward-compatible.