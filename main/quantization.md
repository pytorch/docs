# Quantization

We are centralizing all quantization related development to [torchao](https://github.com/pytorch/ao), please checkout our new doc page: [https://docs.pytorch.org/ao/stable/index.html](https://docs.pytorch.org/ao/stable/index.html)

Plan for the existing quantization flows:

1. **Eager mode quantization** (`torch.ao.quantization.quantize`, `torch.ao.quantization.quantize_dynamic`): please migrate to use torchao eager mode [`quantize_`](https://docs.pytorch.org/ao/main/api_reference/generated/torchao.quantization.quantize_.html#torchao.quantization.quantize_) API instead.
2. **FX graph mode quantization** (`torch.ao.quantization.quantize_fx.prepare_fx`, `torch.ao.quantization.quantize_fx.convert_fx`): please migrate to use torchao pt2e quantization API instead (`torchao.quantization.pt2e.quantize_pt2e.prepare_pt2e`, `torchao.quantization.pt2e.quantize_pt2e.convert_pt2e`).
3. **pt2e quantization** has been migrated to torchao ([pytorch/ao](https://github.com/pytorch/ao/tree/main/torchao/quantization/pt2e)); see [pytorch/ao#2259](https://github.com/pytorch/ao/issues/2259) for more details.

We plan to delete `torch.ao.quantization` in 2.10 if there are no blockers, or in the earliest PyTorch version until all the blockers are cleared.

## Quantization API Reference (Kept since APIs are still public)

The [Quantization API Reference](quantization-support.html) contains documentation
of quantization APIs, such as quantization passes, quantized tensor operations,
and supported quantized modules and functions.

 torch.ao is missing documentation. Since part of it is mentioned here, adding them here for now. 
 They are here for tracking purposes until they are more permanently fixed. 

torch.ao.ns.fx.utils.compute_sqnr(*x*, *y*)[[source]](https://github.com/pytorch/pytorch/blob/2e3c34c8bd8296fe6b14c14ec67f82e8af85507e/torch/ao/ns/fx/utils.py#L441)

torch.ao.ns.fx.utils.compute_normalized_l2_error(*x*, *y*)[[source]](https://github.com/pytorch/pytorch/blob/2e3c34c8bd8296fe6b14c14ec67f82e8af85507e/torch/ao/ns/fx/utils.py#L441)

torch.ao.ns.fx.utils.compute_cosine_similarity(*x*, *y*)[[source]](https://github.com/pytorch/pytorch/blob/2e3c34c8bd8296fe6b14c14ec67f82e8af85507e/torch/ao/ns/fx/utils.py#L441)