# torch.compiler.set_enable_guard_collectives

torch.compiler.set_enable_guard_collectives(*enabled*)[[source]](https://github.com/pytorch/pytorch/blob/ca0571943b5289419bf52b30ee31769eb76a58c8/torch/compiler/__init__.py#L384)

Enables use of collectives *during* guard evaluation to synchronize behavior
across ranks. This is expensive: we have to issue a collective every time
we enter a compiled code region, even if no rank actually would need to
compile. This can help prevent NCCL hangs by ensuring that we never have a
situation where one rank starts recompiling while other ranks don't compile;
it is especially useful in conjunction with enable_compiler_collectives
where such a situation would immediately cause a hang (as it is necessary
for all ranks to compile at the same time to run compiler collectives). Like
compiler collectives, you can only run this on SPMD programs; you will hang
otherwise. Note that a guard collective is only issued if there is any
compiled code to guard on; if this is the first time we encounter a frame or
the frame is skipped, we don't issue collectives.

Returns the previous setting of enabled.