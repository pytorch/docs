# torch.utils.flop_counter.register_flop_formula

torch.utils.flop_counter.register_flop_formula(*targets*, *get_raw=False*)[[source]](https://github.com/pytorch/pytorch/blob/38cca96300da024842405ecefa081e4761254922/torch/utils/flop_counter.py#L133)

Register a FLOP counting formula for custom operations.

This allows FlopCounterMode to count FLOPs for custom operations by providing
a function that calculates FLOPs based on input tensor shapes.

Parameters:

- **targets** - OpOverloadPacket(s) (e.g., torch.ops.mylib.my_op), Triton JITFunction(s),
or HigherOrderOperator(s) to register the formula for. Can be a single
target or a list of targets.
- **get_raw** - If False (default), the formula receives tensor shapes.
If True, the formula receives actual tensors.

Returns:

Decorator that registers the FLOP counting formula.

Return type:

[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[~_P], *_T*]], [*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[~_P], *_T*]]

Example:

```
from torch.utils.flop_counter import register_flop_formula

# Define a custom operation
@torch.library.custom_op("mylib::my_rope", mutates_args=())
def my_rope(x: torch.Tensor) -> torch.Tensor:
 return x # RoPE implementation

@my_rope.register_fake
def _(x):
 return torch.empty_like(x)

# Register FLOP formula (return 0 for negligible ops like RoPE)
@register_flop_formula(torch.ops.mylib.my_rope)
def my_rope_flops(x_shape, out_shape=None, **kwargs):
 return 0 # RoPE doesn't add meaningful FLOPs

# Or calculate actual FLOPs based on shape, assuming mylib::my_attention
# is a custom op defined the same way as mylib::my_rope above
@register_flop_formula(torch.ops.mylib.my_attention)
def my_attention_flops(q_shape, k_shape, v_shape, out_shape=None, **kwargs):
 b, h, s_q, d = q_shape
 s_k = k_shape[2]
 # Q @ K^T + Scores @ V
 return b * h * s_q * s_k * 2 * d + b * h * s_q * d * 2 * s_k

# Now FlopCounterMode will count FLOPs for these operations
with FlopCounterMode(display=True) as mode:
 result = torch.ops.mylib.my_rope(x) # 0 FLOPs counted
 result = torch.ops.mylib.my_attention(q, k, v) # Actual FLOPs counted
```

Note

This decorator also works for Higher Order Operators (HOPs) like flex_attention.
For HOPs without a registered formula, use skip_unsupported=True to execute
them without counting FLOPs (they will be tracked via get_unsupported_ops()).