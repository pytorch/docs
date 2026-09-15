# torch.fx.passes.backends.cudagraphs.partition_cudagraphs

torch.fx.passes.backends.cudagraphs.partition_cudagraphs(*gm*, *inputs*)[[source]](https://github.com/pytorch/pytorch/blob/0519eef7e2a6d24aba3db4d6f13aa0ee998c0d9f/torch/fx/passes/backends/cudagraphs.py#L51)

Partition an FX graph into sub-GraphModules that can be validly run under
CUDA graphs. For a subgraph to be runnable under CUDA, all of the operations
must involve CUDA tensors only.

Return type:

[*GraphModule*](../fx.html#torch.fx.GraphModule)