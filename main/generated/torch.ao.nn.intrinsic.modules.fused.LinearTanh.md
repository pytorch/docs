# LinearTanh

*class*torch.ao.nn.intrinsic.modules.fused.LinearTanh(*linear*, *tanh*)[[source]](https://github.com/pytorch/pytorch/blob/c9b5004c45376c912422325d032b2d74b4828d5c/torch/ao/nn/intrinsic/modules/fused.py#L282)

This is a sequential container which calls the Linear and Tanh modules.
During quantization this will be replaced with the corresponding fused module.