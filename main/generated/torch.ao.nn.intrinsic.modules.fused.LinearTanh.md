# LinearTanh

*class*torch.ao.nn.intrinsic.modules.fused.LinearTanh(*linear*, *tanh*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/ao/nn/intrinsic/modules/fused.py#L282)

This is a sequential container which calls the Linear and Tanh modules.
During quantization this will be replaced with the corresponding fused module.