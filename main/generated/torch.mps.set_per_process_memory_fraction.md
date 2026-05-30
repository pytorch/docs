# torch.mps.set_per_process_memory_fraction

torch.mps.set_per_process_memory_fraction(*fraction*)[[source]](https://github.com/pytorch/pytorch/blob/e5aa1320b162fc3b9d0d53207fe340a6d3aa03d1/torch/mps/__init__.py#L85)

Set memory fraction for limiting process's memory allocation on MPS device.
The allowed value equals the fraction multiplied by recommended maximum device memory
(obtained from Metal API device.recommendedMaxWorkingSetSize).
If trying to allocate more than the allowed value in a process, it will raise an out of
memory error in allocator.

Parameters:

**fraction** ([*float*](https://docs.python.org/3/library/functions.html#float)) - Range: 0~2. Allowed memory equals total_memory * fraction.

Note

Passing 0 to fraction means unlimited allocations
(may cause system failure if out of memory).
Passing fraction greater than 1.0 allows limits beyond the value
returned from device.recommendedMaxWorkingSetSize.