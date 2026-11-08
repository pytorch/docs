# ShapeEnvSettings

*class*torch.fx.experimental.symbolic_shapes.ShapeEnvSettings(*allow_scalar_outputs*, *allow_dynamic_output_shape_ops*, *assume_static_by_default*, *specialize_zero_one*, *duck_shape*, *prefer_deferred_runtime_asserts_over_guards*, *trace_asserts*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/fx/experimental/symbolic_shapes.py#L3916)

Encapsulates all shape env settings that could potentially affect
FakeTensor dispatch. Used when creating dispatch cache keys.