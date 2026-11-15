# torch.fx.passes.backends.cudagraphs.partition_cudagraphs

torch.fx.passes.backends.cudagraphs.partition_cudagraphs(*gm*, *inputs*)[[source]](https://github.com/pytorch/pytorch/blob/c79633996ebc2114482ae5a4ff3cb409d79a8a9c/torch/fx/passes/backends/cudagraphs.py#L51)

Partition an FX graph into sub-GraphModules that can be validly run under
CUDA graphs. For a subgraph to be runnable under CUDA, all of the operations
must involve CUDA tensors only.

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)