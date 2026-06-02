# LocalTensor Tutorial: Single-Process SPMD Debugging

This tutorial introduces `LocalTensor`, a powerful debugging tool for developing
and testing distributed tensor operations without requiring multiple processes or GPUs.

## What is LocalTensor?

`LocalTensor` is a `torch.Tensor` subclass that simulates distributed SPMD
(Single Program, Multiple Data) computations on a single process. It internally
maintains a mapping from rank IDs to their corresponding local tensor shards,
allowing you to debug and test distributed code without infrastructure overhead.

### Key Benefits

1. **No Multi-Process Setup Required**: Test distributed algorithms on a single CPU/GPU
2. **Faster Debugging Cycles**: Iterate quickly without launching multiple processes
3. **Full Visibility**: Inspect each rank's tensor state directly
4. **CI-Friendly**: Run distributed tests in single-process CI pipelines
5. **DTensor Integration**: Seamlessly test DTensor code locally

Note

`LocalTensor` is intended for **debugging and testing** only, not production use.
The overhead of simulating multiple ranks locally is significant.

## Installation and Setup

`LocalTensor` is part of PyTorch's distributed package. No additional installation
is required beyond PyTorch itself.

## Usage Examples

The following examples demonstrate core patterns for using `LocalTensor`. Each
example's code is included directly from source files that are also tested to
ensure correctness. The tests directly invoke these same functions.

### Example 1: Basic LocalTensor Creation and Operations

**Creating a LocalTensor from per-rank tensors:**

```
def create_local_tensor():
 """Create a LocalTensor from per-rank tensors.

 Returns: (local_tensor, (expected_shape, expected_ranks, expected_rank_0, expected_rank_1))
 """
 rank_0_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
 rank_1_tensor = torch.tensor([[5.0, 6.0], [7.0, 8.0]])

 local_tensor = LocalTensor({0: rank_0_tensor, 1: rank_1_tensor})

 expected = (torch.Size([2, 2]), frozenset({0, 1}), rank_0_tensor, rank_1_tensor)
 return local_tensor, expected
```

**Arithmetic operations (applied per-rank):**

```
def arithmetic_operations():
 """Demonstrate arithmetic on LocalTensor.

 Returns: ((doubled, added), (expected_doubled_0, expected_doubled_1, expected_added_0))
 """
 input_0 = torch.tensor([1.0, 2.0, 3.0])
 input_1 = torch.tensor([4.0, 5.0, 6.0])

 lt = LocalTensor({0: input_0, 1: input_1})

 doubled = lt * 2
 added = lt + 10

 expected = (input_0 * 2, input_1 * 2, input_0 + 10)
 return (doubled, added), expected
```

**Extracting a tensor when all shards are identical:**

```
def reconcile_identical_shards():
 """Extract a single tensor when all shards are identical.

 Returns: (result, expected)
 """
 value = torch.tensor([1.0, 2.0, 3.0])
 lt = LocalTensor({0: value.clone(), 1: value.clone(), 2: value.clone()})

 result = lt.reconcile()
 return result, value
```

**Using LocalTensorMode for automatic LocalTensor creation:**

```
def use_local_tensor_mode(world_size: int = 4):
 """Use LocalTensorMode to auto-create LocalTensors.

 Returns: ((is_local, num_ranks), (expected_is_local, expected_num_ranks))
 """
 with LocalTensorMode(world_size):
 x = torch.ones(2, 3)
 is_local = isinstance(x, LocalTensor)
 num_ranks = len(x._ranks)

 return (is_local, num_ranks), (True, world_size)
```

**Full source:** [example_01_basic_operations.py](https://github.com/pytorch/pytorch/blob/main/test/distributed/local_tensor_tutorial_examples/example_01_basic_operations.py)

### Example 2: Simulating Collective Operations

Test collective operations like `all_reduce`, `broadcast`, and `all_gather`
without multiple processes.

**All-reduce with SUM:**

```
def all_reduce_sum(process_group):
 """Simulate all_reduce with SUM across ranks.

 Returns: (result, expected)
 """
 tensors = {
 0: torch.tensor([[1.0, 2.0], [3.0, 4.0]]),
 1: torch.tensor([[5.0, 6.0], [7.0, 8.0]]),
 2: torch.tensor([[9.0, 10.0], [11.0, 12.0]]),
 }

 expected = sum(tensors.values())

 with LocalTensorMode(frozenset(tensors.keys())):
 lt = LocalTensor({k: v.clone() for k, v in tensors.items()})
 dist.all_reduce(lt, op=dist.ReduceOp.SUM, group=process_group)
 result = lt.reconcile()

 return result, expected
```

**Broadcast from a source rank:**

```
def broadcast_from_rank(process_group, src_rank: int = 0):
 """Simulate broadcast from a source rank.

 Returns: (result, expected)
 """
 tensors = {
 0: torch.tensor([10.0, 20.0, 30.0]),
 1: torch.tensor([40.0, 50.0, 60.0]),
 2: torch.tensor([70.0, 80.0, 90.0]),
 }

 expected = tensors[src_rank].clone()

 with LocalTensorMode(frozenset(tensors.keys())):
 lt = LocalTensor({k: v.clone() for k, v in tensors.items()})
 dist.broadcast(lt, src=src_rank, group=process_group)
 result = lt.reconcile()

 return result, expected
```

**All-gather to collect tensors from all ranks:**

```
def all_gather_tensors(process_group):
 """Simulate all_gather to collect tensors from all ranks.

 Returns: (results_list, expected_list)
 """
 tensors = {
 0: torch.tensor([[1.0, 2.0]]),
 1: torch.tensor([[3.0, 4.0]]),
 2: torch.tensor([[5.0, 6.0]]),
 }
 num_ranks = len(tensors)

 expected = [tensors[i].clone() for i in range(num_ranks)]

 with LocalTensorMode(frozenset(tensors.keys())):
 lt = LocalTensor(tensors)
 output_list = [torch.zeros_like(lt) for _ in range(num_ranks)]
 dist.all_gather(output_list, lt, group=process_group)
 results = [out.reconcile() for out in output_list]

 return results, expected
```

**Full source:** [example_02_collective_operations.py](https://github.com/pytorch/pytorch/blob/main/test/distributed/local_tensor_tutorial_examples/example_02_collective_operations.py)

### Example 3: Working with DTensor

`LocalTensor` integrates with DTensor for testing distributed tensor parallelism.

**Distribute a tensor and verify reconstruction:**

```
def distribute_and_verify(world_size: int = 4):
 """Distribute a tensor and verify reconstruction.

 Returns: ((sharded_actual, replicated_actual), (sharded_expected, replicated_expected))
 """
 with LocalTensorMode(world_size):
 mesh = init_device_mesh("cpu", (world_size,))
 tensor = torch.arange(16).reshape(4, 4).float()

 dt_sharded = distribute_tensor(tensor, mesh, [Shard(0)])
 dt_replicated = distribute_tensor(tensor, mesh, [Replicate()])

 sharded_actual = dt_sharded.full_tensor().reconcile()
 replicated_actual = dt_replicated.to_local().reconcile()

 return (sharded_actual, replicated_actual), (tensor, tensor)
```

**Distributed matrix multiplication:**

```
def dtensor_matmul(world_size: int = 4):
 """Perform matrix multiplication with DTensors.

 Returns: (actual, expected)
 """
 with LocalTensorMode(world_size):
 mesh = init_device_mesh("cpu", (world_size,))

 a = torch.randn(8, 4)
 b = torch.randn(4, 6)

 da = distribute_tensor(a, mesh, [Shard(0)])
 db = distribute_tensor(b, mesh, [Replicate()])

 dc = da @ db

 expected = a @ b
 actual = dc.full_tensor().reconcile()

 return actual, expected
```

**Simulating a distributed linear layer:**

```
def dtensor_linear_layer(world_size: int = 4):
 """Simulate a distributed linear layer forward pass.

 Returns: (actual, expected)
 """
 batch_size, in_features, out_features = 16, 8, 4

 with LocalTensorMode(world_size):
 mesh = init_device_mesh("cpu", (world_size,))

 x = torch.randn(batch_size, in_features)
 w = torch.randn(in_features, out_features)
 b = torch.randn(out_features)

 dx = distribute_tensor(x, mesh, [Shard(0)])
 dw = distribute_tensor(w, mesh, [Replicate()])
 db = distribute_tensor(b, mesh, [Replicate()])

 dy = torch.relu(dx @ dw + db)

 expected = torch.relu(x @ w + b)
 actual = dy.full_tensor().reconcile()

 return actual, expected
```

**Full source:** [example_03_dtensor_integration.py](https://github.com/pytorch/pytorch/blob/main/test/distributed/local_tensor_tutorial_examples/example_03_dtensor_integration.py)

### Example 4: Handling Uneven Sharding

Real-world distributed systems often have uneven data distribution across ranks.
`LocalTensor` handles this using `LocalIntNode`.

**Creating LocalTensor with different sizes per rank:**

```
def create_uneven_shards():
 """Create LocalTensor with different sizes per rank.

 Returns: ((local_tensor, is_symint), expected_shapes_dict)
 """
 tensors = {
 0: torch.tensor([[1.0, 2.0, 3.0, 4.0]]), # 1 row
 1: torch.tensor([[5.0, 6.0, 7.0, 8.0], [9.0, 10.0, 11.0, 12.0]]), # 2 rows
 2: torch.tensor([[13.0, 14.0, 15.0, 16.0]]), # 1 row
 }

 lt = LocalTensor(tensors)
 is_symint = isinstance(lt.shape[0], torch.SymInt)

 expected_shapes = {rank: t.shape for rank, t in tensors.items()}
 return (lt, is_symint), expected_shapes
```

**LocalIntNode arithmetic operations:**

```
def local_int_node_arithmetic():
 """LocalIntNode for per-rank integer values.

 Returns: ((add_result, mul_result), (expected_add, expected_mul))
 """
 values_a = {0: 10, 1: 20, 2: 30}
 values_b = {0: 1, 1: 2, 2: 3}
 local_a = LocalIntNode(values_a)
 local_b = LocalIntNode(values_b)

 result_add = local_a.add(local_b)
 result_mul = local_a.mul(local_b)

 expected_add = {k: values_a[k] + values_b[k] for k in values_a}
 expected_mul = {k: values_a[k] * values_b[k] for k in values_a}

 return (
 (dict(result_add._local_ints), dict(result_mul._local_ints)),
 (expected_add, expected_mul),
 )
```

**DTensor with unevenly divisible dimensions:**

```
def dtensor_uneven_sharding(world_size: int = 3):
 """DTensor with unevenly divisible tensor dimension.

 Returns: ((rows_per_rank, matches), expected_total_rows)
 """
 total_rows = 10

 with LocalTensorMode(world_size):
 mesh = init_device_mesh("cpu", (world_size,))

 tensor = torch.arange(total_rows * 4).reshape(total_rows, 4).float()
 dt = distribute_tensor(tensor, mesh, [Shard(0)])

 local = dt.to_local()
 rows_per_rank = {
 rank: local._local_tensors[rank].shape[0] for rank in range(world_size)
 }

 reconstructed = dt.full_tensor().reconcile()
 matches = torch.equal(reconstructed, tensor)

 return (rows_per_rank, matches), total_rows
```

**Full source:** [example_04_uneven_sharding.py](https://github.com/pytorch/pytorch/blob/main/test/distributed/local_tensor_tutorial_examples/example_04_uneven_sharding.py)

### Example 5: Rank-Specific Computations

Sometimes you need to perform different operations on different ranks.

**Using rank_map() to create per-rank values:**

```
def use_rank_map(world_size: int = 4):
 """Create LocalTensors with per-rank values using rank_map.

 Returns: (values_dict, expected_dict)
 """
 with LocalTensorMode(world_size):
 lt = rank_map(lambda rank: torch.full((2, 3), float(rank)))
 values = {
 rank: lt._local_tensors[rank][0, 0].item() for rank in range(world_size)
 }

 expected = {rank: float(rank) for rank in range(world_size)}
 return values, expected
```

**Using tensor_map() to transform shards per-rank:**

```
def use_tensor_map(world_size: int = 4):
 """Transform each shard differently using tensor_map.

 Returns: (values_dict, expected_dict)
 """
 with LocalTensorMode(world_size):
 lt = rank_map(lambda rank: torch.ones(2, 2) * (rank + 1))

 def scale_by_rank(rank: int, tensor: torch.Tensor) -> torch.Tensor:
 return tensor * (rank + 1)

 scaled = tensor_map(lt, scale_by_rank)
 values = {
 rank: scaled._local_tensors[rank][0, 0].item() for rank in range(world_size)
 }

 # (rank + 1) * (rank + 1) = (rank + 1)^2
 expected = {rank: float((rank + 1) ** 2) for rank in range(world_size)}
 return values, expected
```

**Temporarily exiting LocalTensorMode:**

```
def disable_mode_temporarily(world_size: int = 4):
 """Temporarily exit LocalTensorMode for regular tensor ops.

 Returns: ((inside_type, disabled_type), (expected_inside, expected_disabled))
 """
 with LocalTensorMode(world_size) as mode:
 lt = torch.ones(2, 2)
 inside_type = type(lt).__name__

 with mode.disable():
 regular = torch.ones(2, 2)
 disabled_type = type(regular).__name__

 return (inside_type, disabled_type), ("LocalTensor", "Tensor")
```

**Full source:** [example_05_rank_specific.py](https://github.com/pytorch/pytorch/blob/main/test/distributed/local_tensor_tutorial_examples/example_05_rank_specific.py)

### Example 6: Multi-Dimensional Meshes

Use 2D/3D device meshes for hybrid parallelism (e.g., data parallel + tensor parallel).

**Creating a 2D mesh:**

```
def create_2d_mesh():
 """Create a 2D mesh for hybrid parallelism.

 Returns: ((shape, dim_names, total_size), (expected_shape, expected_names, expected_size))
 """
 world_size = 8
 dp_size, tp_size = 4, 2

 with LocalTensorMode(world_size):
 mesh = init_device_mesh("cpu", (dp_size, tp_size), mesh_dim_names=("dp", "tp"))
 shape = mesh.shape
 dim_names = mesh.mesh_dim_names
 total_size = mesh.size()

 expected = ((dp_size, tp_size), ("dp", "tp"), world_size)
 return (shape, dim_names, total_size), expected
```

**Hybrid parallelism (DP + TP):**

```
def hybrid_parallelism():
 """Combine data parallel and tensor parallel.

 Returns: (actual, expected)
 """
 world_size = 8
 dp_size, tp_size = 4, 2

 with LocalTensorMode(world_size):
 mesh = init_device_mesh("cpu", (dp_size, tp_size), mesh_dim_names=("dp", "tp"))

 x = torch.randn(16, 8)
 dx = distribute_tensor(x, mesh, [Shard(0), Replicate()])

 w = torch.randn(8, 12)
 dw = distribute_tensor(w, mesh, [Replicate(), Shard(1)])

 dy = dx @ dw

 expected = x @ w
 actual = dy.full_tensor().reconcile()

 return actual, expected
```

**3D mesh for DP + TP + PP:**

```
def create_3d_mesh():
 """Create a 3D mesh for DP + TP + PP.

 Returns: (actual, expected)
 """
 world_size = 24
 pp_size, dp_size, tp_size = 2, 3, 4

 with LocalTensorMode(world_size):
 mesh = init_device_mesh(
 "cpu",
 (pp_size, dp_size, tp_size),
 mesh_dim_names=("pp", "dp", "tp"),
 )

 tensor = torch.randn(8, 16, 32)
 dt = distribute_tensor(tensor, mesh, [Replicate(), Shard(0), Shard(2)])

 actual = dt.full_tensor().reconcile()

 return actual, tensor
```

**Full source:** [example_06_multidim_mesh.py](https://github.com/pytorch/pytorch/blob/main/test/distributed/local_tensor_tutorial_examples/example_06_multidim_mesh.py)

## Testing Tutorial Examples

All examples in this tutorial are tested to ensure correctness. The test suite
directly invokes the same functions included above:

```
# From test_local_tensor_tutorial_examples.py
from example_01_basic_operations import create_local_tensor

def test_create_local_tensor(self):
 lt = create_local_tensor()
 self.assertIsInstance(lt, LocalTensor)
 self.assertEqual(lt.shape, torch.Size([2, 2]))
```

**Test suite:** [test_local_tensor_tutorial_examples.py](https://github.com/pytorch/pytorch/blob/main/test/distributed/local_tensor_tutorial_examples/test_local_tensor_tutorial_examples.py)

## API Reference

### Core Classes

*class*torch.distributed._local_tensor.LocalTensor(*local_tensors*, *requires_grad=False*)[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/distributed/_local_tensor/__init__.py#L922)

LocalTensor is a Tensor subclass that simulates a tensor distributed across multiple SPMD
(Single Program, Multiple Data) ranks. Each LocalTensor instance internally holds a mapping from
global rank ids to their corresponding local Tensor shards.Operations performed on a LocalTensor
are applied independently to each local shard, mimicking distributed computation. Collectives
and other distributed operations are handled by mapping them to the local shards as appropriate.

Note

This class is primarily intended for debugging and simulating distributed tensor computations
on a single process.

Return type:

LocalTensor

reconcile()[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/distributed/_local_tensor/__init__.py#L1124)

Reconciles the LocalTensor into a single torch.Tensor by ensuring all local
shards are identical and returning a detached clone of one of them.

Note

This method is useful for extracting a representative tensor from a LocalTensor
when all shards are expected to be the same, such as after a collective operation
that synchronizes all ranks.

Return type:

[*Tensor*](../tensors.html#torch.Tensor)

tolist()[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/distributed/_local_tensor/__init__.py#L1103)

Try to reconcile, if successful convert to list, otherwise if dtype is integer,
convert to list of local integers.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]

*class*torch.distributed._local_tensor.LocalTensorMode(*ranks*)[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/distributed/_local_tensor/__init__.py#L1225)

A TorchDispatchMode that simulates SPMD (Single Program, Multiple Data) execution
for LocalTensor objects across a set of ranks.

LocalTensorMode enables PyTorch operations to be transparently applied to each
local shard of a LocalTensor, as if they were distributed across multiple ranks.
When active, this mode intercepts tensor operations and dispatches them to each
rank's local tensor, collecting and wrapping the results as LocalTensors. It also
handles collective operations by mapping them to local implementations.

This mode is primarily intended for debugging and simulating distributed tensor
computations on a single process, rather than for high-performance distributed
training. It maintains a stack of active modes, patches DeviceMesh coordinate
resolution, and provides utilities for temporarily disabling the mode or mapping
functions over ranks.

disable()[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/distributed/_local_tensor/__init__.py#L1467)

Disables LocalTensorMode temporarily. Primarily is intended to be used to perform
rank specific computations and merge results back before enabling LocalTensorMode back.

Return type:

[*Generator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator)[None, None, None]

rank_map(*cb*)[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/distributed/_local_tensor/__init__.py#L1490)

Creates a LocalTensor instance by mapping rank id to ids local shard.

Return type:

*LocalTensor*

tensor_map(*tensor*, *cb*)[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/distributed/_local_tensor/__init__.py#L1499)

Creates a LocalTensor instance by mapping rank id to ids local shard.

Return type:

*LocalTensor*

*class*torch.distributed._local_tensor.LocalIntNode(*local_ints*)[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/distributed/_local_tensor/__init__.py#L423)

Like a LocalTensor, but for an int. We can't use a 0D tensor to represent this
because often only a SymInt is accepted where we wish to use this.

Return type:

ConstantIntNode | LocalIntNode

### Utility Functions

torch.distributed._local_tensor.local_tensor_mode()[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/distributed/_local_tensor/__init__.py#L1738)

Returns the current active LocalTensorMode if one exists.

This function checks the global stack of LocalTensorMode instance. If there
is at least one LocalTensorMode active, it returns the most recently entered
(top of the stack) LocalTensorMode. If no LocalTensorMode is active, it returns None.

Returns:

The current LocalTensorMode if active, else None.

Return type:

Optional[LocalTensorMode]

torch.distributed._local_tensor.enabled_local_tensor_mode()[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/distributed/_local_tensor/__init__.py#L1755)

Returns the current active LocalTensorMode only if it's enabled.

This is a convenience function that combines the common pattern of checking
if local_tensor_mode() is not None and not disabled.

Returns:

The current LocalTensorMode if active and enabled, else None.

Return type:

Optional[LocalTensorMode]

torch.distributed._local_tensor.maybe_run_for_local_tensor(*func*)[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/distributed/_local_tensor/__init__.py#L1771)

Decorator that ensures a function is executed for each local tensor shard
when running under LocalTensorMode. If not in LocalTensorMode, the function
is executed normally. When in LocalTensorMode, the function is run for each
rank, and the results are collected appropriately.

This decorator is useful for functions that exhibit non-SPMD behavior, such
as those requiring rank specific actions. For example, a function that computes
offset into input tensor based on rank.

Note that the function being decorated must not have any side effects and
contain operations for a single rank only. For example, wrapping a function
that performs a collective operation will not work.

Parameters:

**func** (*Callable**[**...**,**Any**]*) - The function to be decorated.

Returns:

The wrapped function that handles LocalTensorMode logic.

Return type:

Callable[..., Any]

torch.distributed._local_tensor.maybe_disable_local_tensor_mode()[[source]](https://github.com/pytorch/pytorch/blob/c42e39b73c4b6bab2e78f982765bd2029abc2a2a/torch/distributed/_local_tensor/__init__.py#L1842)

Context manager that disables LocalTensorMode for the duration of the context.

Return type:

[*AbstractContextManager*](https://docs.python.org/3/library/contextlib.html#contextlib.AbstractContextManager)

## Best Practices

1. **Use for Testing Only**: LocalTensor has significant overhead and should not
be used in production code.
2. **Initialize Process Groups**: Even for local testing, you need to initialize
a process group (use the "fake" backend).
3. **Avoid requires_grad on Inner Tensors**: LocalTensor expects inner tensors
to not have `requires_grad=True`. Set gradients on the LocalTensor wrapper instead.
4. **Reconcile for Assertions**: Use `reconcile()` to extract a single tensor
when all ranks should have identical values (e.g., after an all-reduce).
5. **Debug with Direct Access**: Access individual shards via `tensor._local_tensors[rank]`
for debugging.

## Common Pitfalls

1. **Forgetting the Context Manager**: Operations on LocalTensor outside
`LocalTensorMode` still work but won't create new LocalTensors from factories.
2. **Mismatched Ranks**: Ensure all LocalTensors in an operation have compatible ranks.
3. **Inner Tensor Gradients**: Creating LocalTensor from tensors with `requires_grad=True`
will raise an error.