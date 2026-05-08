# LinearReLU

*class*torch.ao.nn.intrinsic.LinearReLU(*linear*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/3565a492def04bf126af9d46958533d16fb88274/torch/ao/nn/intrinsic/modules/fused.py#L93)

This is a sequential container which calls the Linear and ReLU modules.
During quantization this will be replaced with the corresponding fused module.