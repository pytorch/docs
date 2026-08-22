# record_function

*class*torch.autograd.profiler.record_function(*name*, *args=None*)[[source]](https://github.com/pytorch/pytorch/blob/f744a6b99cda942b3dd232f56c0ebf413660c13f/torch/autograd/profiler.py#L875)

Context manager/function decorator that adds a label to a code block/function when running autograd profiler.
Label will only appear if CPU activity tracing is enabled.

It is useful when tracing the code profile.

Parameters:

- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Label assigned to the block of code.
- **node_id** ([*int*](https://docs.python.org/3/library/functions.html#int)) - ID of node, for distributed profiling. Unset in
- **cases.** (*non-distributed*) -

Example

```
>>> x = torch.randn((1, 1), requires_grad=True)
>>> with torch.autograd.profiler.profile() as prof:
... y = x**2
... with torch.autograd.profiler.record_function(
... "label-z"
... ): # label the block
... z = y**3
... y.backward()
>>> # NOTE: some columns were removed for brevity
>>> print(prof.key_averages().table(sort_by="self_cpu_time_total"))
----------------------------------- --------------- --------------- ---------------
Name Self CPU total % CPU time avg Number of Calls
----------------------------------- --------------- --------------- ---------------
pow 60.77% 47.470us 3
mul 21.73% 25.465us 2
PowBackward0 12.03% 121.891us 1
torch::autograd::AccumulateGrad 2.70% 6.324us 1
label-z 2.13% 12.421us 1
torch::autograd::GraphRoot 0.64% 1.503us 1
----------------------------------- --------------- --------------- ---------------
Self CPU time total: 234.344us
CUDA time total: 0.000us
```