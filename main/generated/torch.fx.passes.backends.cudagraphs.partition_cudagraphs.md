# torch.fx.passes.backends.cudagraphs.partition_cudagraphs

torch.fx.passes.backends.cudagraphs.partition_cudagraphs(*gm*, *inputs*)[[source]](https://github.com/pytorch/pytorch/blob/80b7a2174586f92cc0af6a820a4c98e73b6fca58/torch/fx/passes/backends/cudagraphs.py#L51)

Partition an FX graph into sub-GraphModules that can be validly run under
CUDA graphs. For a subgraph to be runnable under CUDA, all of the operations
must involve CUDA tensors only/

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)