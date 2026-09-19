# QuantizedGraphModule

*class*torch.ao.quantization.fx.graph_module.QuantizedGraphModule(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/b7954b2399da4803024b9a2850e39c588522015f/torch/ao/quantization/fx/graph_module.py#L142)

This class is created to make sure PackedParams
(e.g. LinearPackedParams, Conv2dPackedParams) to appear in state_dict
so that we can serialize and deserialize quantized graph module with
torch.save(m.state_dict()) and m.load_state_dict(state_dict)