# PerToken

*class*torch.ao.quantization.observer.PerToken[[source]](https://github.com/pytorch/pytorch/blob/c5a2c86d66eda12ed122b796baae9cb0aaf5aefb/torch/ao/quantization/observer.py#L1797)

Represents per-token granularity in quantization.

This granularity type calculates a different set of quantization parameters
for each token, which is represented as the last dimension of the tensor.

For example, if the input tensor has shape [2, 3, 4], then there are 6 tokens
with 4 elements each, and we will calculate 6 sets of quantization parameters,
one for each token.

If the input tensor has only two dimensions, e.g. [8, 16], then this is
equivalent to PerAxis(axis=0), which yields 8 sets of quantization parameters.