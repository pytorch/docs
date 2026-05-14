# torch.fx.experimental.optimization.gen_mkl_autotuner

torch.fx.experimental.optimization.gen_mkl_autotuner(*example_inputs*, *iters=10*, *warmup=1*)[[source]](https://github.com/pytorch/pytorch/blob/8e57bf150e06e0d3c3fa0bd28964c572270d2c4c/torch/fx/experimental/optimization.py#L237)

This generates a heuristic that can be passed into optimize_for_inference that
determines whether a subgraph should be run in MKL by running it with the example_inputs.

Example usage:

heuristic = gen_mkl_autotuner(example_inputs, iters=10)
fast_model = optimization.optimize_for_inference(model, heuristic)

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[*MklSubgraph*], [bool](https://docs.python.org/3/library/functions.html#bool)]