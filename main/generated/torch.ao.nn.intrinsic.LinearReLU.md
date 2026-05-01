# LinearReLU

*class*torch.ao.nn.intrinsic.LinearReLU(*linear*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/fbfd15846f570ac46ff9e34a533162fb2054dbd9/torch/ao/nn/intrinsic/modules/fused.py#L93)

This is a sequential container which calls the Linear and ReLU modules.
During quantization this will be replaced with the corresponding fused module.