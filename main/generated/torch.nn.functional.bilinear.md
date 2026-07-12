# torch.nn.functional.bilinear

torch.nn.functional.bilinear(*input1*, *input2*, *weight*, *bias=None*) → [Tensor](../tensors.html#torch.Tensor)[[source]](https://github.com/pytorch/pytorch/blob/dea5f568512cef2ab009ee7858b1cfd9be8ba924/torch/nn/functional.py#L2406)

Applies a bilinear transformation to the incoming data:
y=x1TAx2+by = x_1^T A x_2 + by=x1T​Ax2​+b

Shape:

> - input1: (N,∗,Hin1)(N, *, H_{in1})(N,∗,Hin1​) where Hin1=in1_featuresH_{in1}=\text{in1\_features}Hin1​=in1_features
> and ∗*∗ means any number of additional dimensions.
> All but the last dimension of the inputs should be the same.
> - input2: (N,∗,Hin2)(N, *, H_{in2})(N,∗,Hin2​) where Hin2=in2_featuresH_{in2}=\text{in2\_features}Hin2​=in2_features
> - weight: (out_features,in1_features,in2_features)(\text{out\_features}, \text{in1\_features},
> \text{in2\_features})(out_features,in1_features,in2_features)
> - bias: (out_features)(\text{out\_features})(out_features)
> - output: (N,∗,Hout)(N, *, H_{out})(N,∗,Hout​) where Hout=out_featuresH_{out}=\text{out\_features}Hout​=out_features
> and all but the last dimension are the same shape as the input.