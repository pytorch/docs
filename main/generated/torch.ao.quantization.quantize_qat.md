# quantize_qat

*class*torch.ao.quantization.quantize_qat(*model*, *run_fn*, *run_args*, *inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/8ab13d788b9dab3e338e618576e65bb8b0c75e1a/torch/ao/quantization/quantize.py#L605)

Do quantization aware training and output a quantized model

Parameters:

- **model** - input model
- **run_fn** - a function for evaluating the prepared model, can be a
function that simply runs the prepared model or a training
loop
- **run_args** - positional arguments for run_fn

Returns:

Quantized model.