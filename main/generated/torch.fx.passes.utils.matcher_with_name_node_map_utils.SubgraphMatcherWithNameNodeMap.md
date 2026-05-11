# SubgraphMatcherWithNameNodeMap

*class*torch.fx.passes.utils.matcher_with_name_node_map_utils.SubgraphMatcherWithNameNodeMap(*pattern_gm*, *match_output=False*, *match_placeholder=False*, *remove_overlapping_matches=True*, *ignore_literals=False*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/fx/passes/utils/matcher_with_name_node_map_utils.py#L43)

Extends SubgraphMatcher to support querying the matched subgraph nodes through node name,

this requires pattern to have specific format (returning and additional dictionary at the output,
that has node name as key, and the node in the pattern graph as value, see Example for more details)

Difference with SubgraphMatcher is that it takes a pattern_gm GraphModule as input during
initialization since we need to modify the graph (which requires recompile the GraphModule)

Example:

```
def pattern(x, weight):
 conv = F.conv2d(x, weight)
 relu = F.relu(conv)
 return relu, {"conv": conv, "relu": relu}

def target_graph(x, weight):
 conv = F.conv2d(x, weight)
 relu = F.relu(conv)
 relu *= 2
 return relu

pattern_gm = export(pattern, example_inputs).module()
target_gm = export(target_graph, example_inputs).module()
matcher = SubgraphMatcherWithNameNodeMap(pattern_gm)
matches = matcher.match(target_gm)
for match in matches:
 match.name_node_map["conv"].meta["annotation"] = ...
```

Warning

This API is experimental and is *NOT* backward-compatible.

match(*graph*, *node_name_match=''*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/fx/passes/utils/matcher_with_name_node_map_utils.py#L94)

The returned InternalMatch will have name_node_map populated with a map
from node name (str) to the target node, e.g.
`{"conv": target_conv_ndoe, "relu": target_relu_node}`

This requires the pattern graph returns an additional
output of node name to node, e.g. instead of:

```
def pattern(...):
 ...
 return relu
```

we should do:

```
def pattern(...):
 ...
 return relu, {"conv": conv, "relu": relu}
```

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[*InternalMatch*]