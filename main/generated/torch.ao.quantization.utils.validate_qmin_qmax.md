# validate_qmin_qmax

*class*torch.ao.quantization.utils.validate_qmin_qmax(*quant_min*, *quant_max*)[[source]](https://github.com/pytorch/pytorch/blob/e74021214a802c9136769de0046dff0e7710d800/torch/ao/quantization/utils.py#L615)

Validates that the user-specified quantization range is properly initialized
and within the given bound supported by the observer dtype.

To accommodate lower-bit quantization with respect to the existing torch.qint8 and
torch.quint8 datatypes, the user can choose to use dynamic quantization range by passing
in a tuple of initial qmin and qmax values. One use case is these customized qmin and qmax
values are used to calculate static estimates of the scale and zero point for aggressive lower-bit
fake quantization. These estimates are compared against parameters learned through backpropagation.
The related literature for scale and zero point via backpropagation are as follows:

Learned Step Size Quantization: [https://openreview.net/pdf?id=rkgO66VKDS](https://openreview.net/pdf?id=rkgO66VKDS)
Trained Quantization Thresholds: [https://arxiv.org/pdf/1903.08066.pdf](https://arxiv.org/pdf/1903.08066.pdf)