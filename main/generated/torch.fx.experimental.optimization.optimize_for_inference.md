# torch.fx.experimental.optimization.optimize_for_inference

torch.fx.experimental.optimization.optimize_for_inference(*model*, *pass_config=None*, *tracer=<class 'torch.fx._symbolic_trace.Tracer'>*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/fx/experimental/optimization.py#L329)

Performs a set of optimization passes to optimize a model for the
purposes of inference. Specifically, the passes that are run are:
1. Conv/BN fusion
2. Dropout removal
3. MKL layout optimizations

The third optimization takes a function use_mkl_heuristic that's used
to determine whether a subgraph should be explicitly run in MKL layout.

Note: As FX does not currently handle aliasing, this pass currently
assumes nothing aliases. If that isn't true, use at your own risk.

Return type:

[*Module*](torch.nn.Module.html#torch.nn.Module)