# torch.fx.experimental.optimization.optimize_for_inference

torch.fx.experimental.optimization.optimize_for_inference(*model*, *pass_config=None*, *tracer=<class 'torch.fx._symbolic_trace.Tracer'>*)[[source]](https://github.com/pytorch/pytorch/blob/a533e5c93d4fb8c4eb7bd23c7d297cbba493caa1/torch/fx/experimental/optimization.py#L331)

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