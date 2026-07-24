# LinearReLU

*class*torch.ao.nn.intrinsic.LinearReLU(*linear*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/ao/nn/intrinsic/modules/fused.py#L93)

This is a sequential container which calls the Linear and ReLU modules.
During quantization this will be replaced with the corresponding fused module.