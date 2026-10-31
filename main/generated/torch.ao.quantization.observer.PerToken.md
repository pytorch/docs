# PerToken

*class*torch.ao.quantization.observer.PerToken[[source]](https://github.com/pytorch/pytorch/blob/08c2d21eeac45d7bb2b95f497938e99c0250222d/torch/ao/quantization/observer.py#L1797)

Represents per-token granularity in quantization.

This granularity type calculates a different set of quantization parameters
for each token, which is represented as the last dimension of the tensor.

For example, if the input tensor has shape [2, 3, 4], then there are 6 tokens
with 4 elements each, and we will calculate 6 sets of quantization parameters,
one for each token.

If the input tensor has only two dimensions, e.g. [8, 16], then this is
equivalent to PerAxis(axis=0), which yields 8 sets of quantization parameters.