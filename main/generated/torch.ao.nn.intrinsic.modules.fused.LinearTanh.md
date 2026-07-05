# LinearTanh

*class*torch.ao.nn.intrinsic.modules.fused.LinearTanh(*linear*, *tanh*)[[source]](https://github.com/pytorch/pytorch/blob/5abd8608770f0b56abd2b52412c9b39feeb6153e/torch/ao/nn/intrinsic/modules/fused.py#L282)

This is a sequential container which calls the Linear and Tanh modules.
During quantization this will be replaced with the corresponding fused module.