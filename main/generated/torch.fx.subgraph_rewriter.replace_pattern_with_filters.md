# torch.fx.subgraph_rewriter.replace_pattern_with_filters

torch.fx.subgraph_rewriter.replace_pattern_with_filters(*gm*, *pattern*, *replacement=None*, *match_filters=None*, *ignore_literals=False*, *replacement_callback=None*, *node_name_match=''*)[[source]](https://github.com/pytorch/pytorch/blob/9f02f17d134eee814f47e416bd6bf8036d7170ff/torch/fx/subgraph_rewriter.py#L225)

See replace_pattern for documentation. This function is an overload with an additional match_filter argument.

Parameters:

- **match_filters** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)*[**[**InternalMatch**,*[*Graph*](../fx.html#torch.fx.Graph)*,*[*Graph*](../fx.html#torch.fx.Graph)*]**,*[*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]**|**None*) - A list of functions that take in
(match: InternalMatch, original_graph: Graph, pattern_graph: Graph) and return a boolean indicating
whether the match satisfies the condition.
See matcher_utils.py for definition of InternalMatch.
- **replacement_callback** ([*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)*[**[**InternalMatch**,*[*Graph*](../fx.html#torch.fx.Graph)*,*[*Graph*](../fx.html#torch.fx.Graph)*]**,*[*Graph*](../fx.html#torch.fx.Graph)*]**|**None*) - A function that takes in a match and returns a
Graph to be used as the replacement. This allows you to construct a
replacement graph based on the match.
- **node_name_match** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Node name to match. If not empty, it will try to match the node name.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[*ReplacedPatterns*]

Warning

This API is experimental and is *NOT* backward-compatible.