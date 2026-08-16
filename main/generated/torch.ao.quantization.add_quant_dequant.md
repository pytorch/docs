# add_quant_dequant

*class*torch.ao.quantization.add_quant_dequant(*module*)[[source]](https://github.com/pytorch/pytorch/blob/8aac66fb022576e2d13144ab636372f686f23cfa/torch/ao/quantization/quantize.py#L316)

Wrap the leaf child module in QuantWrapper if it has a valid qconfig
Note that this function will modify the children of module inplace and it
can return a new module which wraps the input module as well.

Parameters:

- **module** - input module with qconfig attributes for all the leaf modules
- **quantize** (*that we want to*) -

Returns:

Either the inplace modified module with submodules wrapped in
QuantWrapper based on qconfig or a new QuantWrapper module which
wraps the input module, the latter case only happens when the input
module is a leaf module and we want to quantize it.