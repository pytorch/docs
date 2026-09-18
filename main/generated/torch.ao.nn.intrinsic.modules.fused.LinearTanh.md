# LinearTanh

*class*torch.ao.nn.intrinsic.modules.fused.LinearTanh(*linear*, *tanh*)[[source]](https://github.com/pytorch/pytorch/blob/0c8b4a78ffbbce776adc0823e790158b26435f40/torch/ao/nn/intrinsic/modules/fused.py#L282)

This is a sequential container which calls the Linear and Tanh modules.
During quantization this will be replaced with the corresponding fused module.