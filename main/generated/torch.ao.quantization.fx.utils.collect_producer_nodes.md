# collect_producer_nodes

*class*torch.ao.quantization.fx.utils.collect_producer_nodes(*node*)[[source]](https://github.com/pytorch/pytorch/blob/6a231d0d3e1ccd63dd51479bcadc969d0a8de2b9/torch/ao/quantization/fx/utils.py#L191)

Starting from a target node, trace back until we hit input or
getattr node. This is used to extract the chain of operators
starting from getattr to the target node, for example:

```
def forward(self, x):
 observed = self.observer(self.weight)
 return F.linear(x, observed)
```

collect_producer_nodes(observed) will either return a list of nodes that
produces the observed node or None if we can't extract a self contained
graph without free variables(inputs of the forward function).

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[*Node*](../fx.html#torch.fx.Node)] | None