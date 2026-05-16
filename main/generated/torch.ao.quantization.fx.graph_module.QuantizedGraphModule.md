# QuantizedGraphModule

*class*torch.ao.quantization.fx.graph_module.QuantizedGraphModule(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/df83f06a8c49a667b9408934fa9eaae1aaf32d04/torch/ao/quantization/fx/graph_module.py#L142)

This class is created to make sure PackedParams
(e.g. LinearPackedParams, Conv2dPackedParams) to appear in state_dict
so that we can serialize and deserialize quantized graph module with
torch.save(m.state_dict()) and m.load_state_dict(state_dict)