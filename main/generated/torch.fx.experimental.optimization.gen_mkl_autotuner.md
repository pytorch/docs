# torch.fx.experimental.optimization.gen_mkl_autotuner

torch.fx.experimental.optimization.gen_mkl_autotuner(*example_inputs*, *iters=10*, *warmup=1*)[[source]](https://github.com/pytorch/pytorch/blob/8df61039f8235b92b0ca250355cc296020f46e2d/torch/fx/experimental/optimization.py#L237)

This generates a heuristic that can be passed into optimize_for_inference that
determines whether a subgraph should be run in MKL by running it with the example_inputs.

Example usage:

heuristic = gen_mkl_autotuner(example_inputs, iters=10)
fast_model = optimization.optimize_for_inference(model, heuristic)

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[*MklSubgraph*], [bool](https://docs.python.org/3/library/functions.html#bool)]