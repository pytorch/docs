# torch.Tensor.record_stream

Tensor.record_stream(*stream*)

Marks the tensor as having been used by this stream. When the tensor
is deallocated, ensure the tensor memory is not reused for another tensor
until all work queued on `stream` at the time of deallocation is
complete.

Note

The caching allocator is aware of only the stream where a tensor was
allocated. Due to the awareness, it already correctly manages the life
cycle of tensors on only one stream. But if a tensor is used on a stream
different from the stream of origin, the allocator might reuse the memory
unexpectedly. Calling this method lets the allocator know which streams
have used the tensor.

Warning

This method is most suitable for use cases where you are providing a
function that created a tensor on a side stream, and want users to be able
to make use of the tensor without having to think carefully about stream
safety when making use of them. These safety guarantees come at some
performance and predictability cost (analogous to the tradeoff between GC
and manual memory management), so if you are in a situation where
you manage the full lifetime of your tensors, you may consider instead
manually managing CUDA events so that calling this method is not necessary.
In particular, when you call this method, on later allocations the
allocator will poll the recorded stream to see if all operations have
completed yet; you can potentially race with side stream computation and
non-deterministically reuse or fail to reuse memory for an allocation.

You can safely use tensors allocated on side streams without
`record_stream()`; you must manually ensure that
any non-creation stream uses of a tensor are synced back to the creation
stream before you deallocate the tensor. As the CUDA caching allocator
guarantees that the memory will only be reused with the same creation stream,
this is sufficient to ensure that writes to future reallocations of the
memory will be delayed until non-creation stream uses are done.
(Counterintuitively, you may observe that on the CPU side we have already
reallocated the tensor, even though CUDA kernels on the old tensor are
still in progress. This is fine, because CUDA operations on the new
tensor will appropriately wait for the old operations to complete, as they
are all on the same stream.)

Concretely, this looks like this:

```
with torch.cuda.stream(s0):
 x = torch.zeros(N)

s1.wait_stream(s0)
with torch.cuda.stream(s1):
 y = some_comm_op(x)

... some compute on s0 ...

# synchronize creation stream s0 to side stream s1
# before deallocating x
s0.wait_stream(s1)
del x
```

Note that some discretion is required when deciding when to perform
`s0.wait_stream(s1)`. In particular, if we were to wait immediately
after `some_comm_op`, there wouldn't be any point in having the side
stream; it would be equivalent to have run `some_comm_op` on `s0`.
Instead, the synchronization must be placed at some appropriate, later
point in time where you expect the side stream `s1` to have finished
work. This location is typically identified via profiling, e.g., using
Chrome traces produced
[`torch.autograd.profiler.profile.export_chrome_trace()`](torch.autograd.profiler.profile.export_chrome_trace.html#torch.autograd.profiler.profile.export_chrome_trace). If you
place the wait too early, work on s0 will block until `s1` has finished,
preventing further overlapping of communication and computation. If you
place the wait too late, you will use more memory than is strictly
necessary (as you are keeping `x` live for longer.) For a concrete
example of how this guidance can be applied in practice, see this post:
[FSDP and CUDACachingAllocator](https://dev-discuss.pytorch.org/t/fsdp-cudacachingallocator-an-outsider-newb-perspective/1486).