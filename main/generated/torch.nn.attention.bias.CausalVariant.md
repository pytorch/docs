# CausalVariant

*class*torch.nn.attention.bias.CausalVariant(*value*, *names=None*, ***, *module=None*, *qualname=None*, *type=None*, *start=1*, *boundary=None*)[[source]](https://github.com/pytorch/pytorch/blob/9b9978943e4030e97eeee36a9968db27a3b21163/torch/nn/attention/bias.py#L33)

Enum for causal variants used in attention mechanisms.

Defines two types of causal biases:

`UPPER_LEFT`: Represents upper-left triangular bias for standard causal attention.
The equivalent pytorch code for constructing this bias is:

```
torch.tril(torch.ones(size, dtype=torch.bool))
```

For instance, with `shape=(3,4)`, the materialized bias tensor will be:

```
[[1, 0, 0, 0],
 [1, 1, 0, 0],
 [1, 1, 1, 0]]
```

`LOWER_RIGHT`: Represents lower-right triangular bias, the include values are aligned to the lower
right corner of the matrix.

The equivalent pytorch code for constructing this bias is:

```
diagonal_offset = size[1] - size[0]
torch.tril(
 torch.ones(size, dtype=torch.bool),
 diagonal=diagonal_offset,
)
```

For instance, with `shape=(3,4)`, the materialized bias tensor will be:

```
[[1, 1, 0, 0],
 [1, 1, 1, 0],
 [1, 1, 1, 1]]
```

Note that these variants are equivalent to each other when the sequence lengths of the query and key/value
tensors are equal since the triangular matrix is square.

Warning

This enum is a prototype and subject to change.

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