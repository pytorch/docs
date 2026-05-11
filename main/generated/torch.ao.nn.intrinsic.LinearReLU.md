# LinearReLU

*class*torch.ao.nn.intrinsic.LinearReLU(*linear*, *relu*)[[source]](https://github.com/pytorch/pytorch/blob/c15e9774278597951aa402693c1bbcb6c8c7b9e8/torch/ao/nn/intrinsic/modules/fused.py#L93)

This is a sequential container which calls the Linear and ReLU modules.
During quantization this will be replaced with the corresponding fused module.