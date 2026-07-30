# NUMA Binding

In NUMA (Non-Uniform Memory Access) systems, accessing memory on remote NUMA
nodes incurs additional latency. PyTorch provides NUMA binding utilities to
promote memory locality by binding worker processes to CPUs near their assigned accelerator devices.

In practice, NUMA binding typically results in 1-10% overall performance improvements,
but some workloads may obtain much greater benefits or none at all.

To enable NUMA binding, use the `--numa-binding` flag with [torchrun](run.html#launcher-api), e.g.:

```
torchrun --numa-binding=node --nproc_per_node=8 train.py
```

Alternatively, pass `NumaOptions` to `LaunchConfig`
when using `elastic_launch`.

See `AffinityMode` for available binding modes.

*class*torch.numa.binding.AffinityMode(*value*)[[source]](https://github.com/pytorch/pytorch/blob/9179f2014ca7f941551131fc2315cfcf9e206bd3/torch/numa/binding.py#L44)

An enumeration.

NODE*= 'node'*

Each worker process and its threads will be bound to all the CPUs
on the NUMA node containing the accelerator device whose local index equals the worker's
local rank. If in doubt, use this option rather than the others.

**Ex.:** If device 3 lives on NUMA node 1, then the worker whose local rank is 3 will
only be able to run on the CPUs of NUMA node 1.

SOCKET*= 'socket'*

Each worker process and its threads will be bound to all the CPUs on all the NUMA nodes of the
socket containing the accelerator device whose local index equals the worker's local rank.

**Ex.:** If socket 0 contains device 3 and NUMA nodes 0-1, then the worker whose
local rank is 3 will be bound to the CPUs of NUMA nodes 0-1.

For cases where there is only one NUMA node per socket anyway, this is equivalent to NODE.

EXCLUSIVE*= 'exclusive'*

Each worker process and its threads will be bound to an exclusive subset of CPUs
on the NUMA node containing the accelerator device whose local index equals the worker's
local rank. The CPUs on the NUMA node are divided evenly among all devices on that node,
so no two workers share the same CPU cores.

**Ex.:** If NUMA node 1 has 16 physical cores and devices 2 and 3, then the worker whose
local rank is 2 will be bound to cores 0-7, and the worker whose local rank is 3 will
be bound to cores 8-15.

CORE_COMPLEX*= 'core-complex'*

Each worker process and its threads will be bound to a single core complex (a group of cores
sharing the same L3 cache) on the NUMA node containing the accelerator device whose local
index equals the worker's local rank. Each worker is bound to a different core complex when
possible.

**Ex.:** If NUMA node 1 has two core complexes (cores 0-7 sharing one L3 cache, cores 8-15
sharing another) and devices 2 and 3, then the worker whose local rank is 2 will be bound to
cores 0-7, and the worker whose local rank is 3 will be bound to cores 8-15.

*class*torch.numa.binding.NumaOptions(*affinity_mode: torch.numa.binding.AffinityMode*, *should_fall_back_if_binding_fails: [bool](https://docs.python.org/3/library/functions.html#bool) = False*)[[source]](https://github.com/pytorch/pytorch/blob/9179f2014ca7f941551131fc2315cfcf9e206bd3/torch/numa/binding.py#L91)

affinity_mode*: AffinityMode*

should_fall_back_if_binding_fails*: [bool](https://docs.python.org/3/library/functions.html#bool)**= False*

If `True`, we will silence any exceptions that occur during NUMA binding itself
rather than raising them.

There are no expected exceptions, so avoid using this option. Its purpose is simply
to mitigate crash risk while conducting mass rollouts of NUMA binding.