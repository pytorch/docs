# torch.fx.passes.backends.cudagraphs.partition_cudagraphs

torch.fx.passes.backends.cudagraphs.partition_cudagraphs(*gm*, *inputs*)[[source]](https://github.com/pytorch/pytorch/blob/b896199bee9ca0e125f6ec366a265418a8f3290e/torch/fx/passes/backends/cudagraphs.py#L51)

Partition an FX graph into sub-GraphModules that can be validly run under
CUDA graphs. For a subgraph to be runnable under CUDA, all of the operations
must involve CUDA tensors only.

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)