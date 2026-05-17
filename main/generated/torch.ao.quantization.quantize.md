# quantize

*class*torch.ao.quantization.quantize(*model*, *run_fn*, *run_args*, *mapping=None*, *inplace=False*)[[source]](https://github.com/pytorch/pytorch/blob/da74fecc24c85f9694061e961858303c44be4338/torch/ao/quantization/quantize.py#L453)

Quantize the input float model with post training static quantization.

First it will prepare the model for calibration, then it calls
run_fn which will run the calibration step, after that we will
convert the model to a quantized model.

Parameters:

- **model** - input float model
- **run_fn** - a calibration function for calibrating the prepared model
- **run_args** - positional arguments for run_fn
- **inplace** - carry out model transformations in-place, the original module is mutated
- **mapping** - correspondence between original module types and quantized counterparts

Returns:

Quantized model.