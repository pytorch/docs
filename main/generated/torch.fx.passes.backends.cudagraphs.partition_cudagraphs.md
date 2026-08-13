# torch.fx.passes.backends.cudagraphs.partition_cudagraphs

torch.fx.passes.backends.cudagraphs.partition_cudagraphs(*gm*, *inputs*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/fx/passes/backends/cudagraphs.py#L51)

Partition an FX graph into sub-GraphModules that can be validly run under
CUDA graphs. For a subgraph to be runnable under CUDA, all of the operations
must involve CUDA tensors only.

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)