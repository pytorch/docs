# LinearReLU

*class*torch.ao.nn.intrinsic.LinearReLU(*linear*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/460262116930c46e505df88f1fcd347abab536c4/torch/ao/nn/intrinsic/modules/fused.py#L93)

This is a sequential container which calls the Linear and ReLU modules.
During quantization this will be replaced with the corresponding fused module.