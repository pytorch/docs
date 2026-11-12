# ScalingAlgorithm

*class*torch.nn.functional.ScalingAlgorithm(*value*, *names=None*, ***, *module=None*, *qualname=None*, *type=None*, *start=1*, *boundary=None*)[[source]](https://github.com/pytorch/pytorch/blob/c5a2c86d66eda12ed122b796baae9cb0aaf5aefb/torch/nn/functional.py#L42)

Algorithm used to compute and encode block scales for [`quantize_tensor()`](torch.nn.functional.quantize_tensor.html#torch.nn.functional.quantize_tensor).

MXFP_E8M0_RU*= 0*

MXFP E8M0 round-up scaling, described in [Algorithm 1](https://arxiv.org/pdf/2506.08027).

The block's maximum absolute input value, divided by the largest
representable quantized value, is rounded up to E8M0. If any input in the
block is `NaN` or `+/-Inf`, the scale is E8M0 `NaN` (byte `0xff`).
An all-zero block instead receives the smallest E8M0 scale,
2−1272^{-127}2−127 (byte `0x00`), because E8M0 has no zero encoding.

as_integer_ratio()

Return integer ratio.

Return a pair of integers, whose ratio is exactly equal to the original int
and with a positive denominator.

```
>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)
```

bit_count()

Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

```
>>> bin(13)
'0b1101'
>>> (13).bit_count()
3
```

bit_length()

Number of bits necessary to represent self in binary.

```
>>> bin(37)
'0b100101'
>>> (37).bit_length()
6
```

conjugate()

Returns self, the complex conjugate of any int.

denominator

the denominator of a rational number in lowest terms

imag

the imaginary part of a complex number

numerator

the numerator of a rational number in lowest terms

real

the real part of a complex number