# NodeEvent

*class*torch.fx.passes.splitter_base.NodeEvent(*source*, *desc*, *dep=None*)[[source]](https://github.com/pytorch/pytorch/blob/e01c6ae6acffaccede59e20d14af54437c5342d8/torch/fx/passes/splitter_base.py#L150)

An event in graph split that happened on a node.
source: Subject of the event
desc: readable description
dep: Optional dependency, usually the node that caused the event.

Warning

This API is experimental and is *NOT* backward-compatible.