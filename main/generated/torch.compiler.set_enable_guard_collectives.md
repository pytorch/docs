# torch.compiler.set_enable_guard_collectives

torch.compiler.set_enable_guard_collectives(*enabled*)[[source]](https://github.com/pytorch/pytorch/blob/fd6d216e3e8bf07c470716dfbf022d82fadd521d/torch/compiler/__init__.py#L382)

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
compiled code to guard on; if this the first time we encounter a frame or
the frame is skipped, we don't issue collectives.

Returns the previous setting of enabled.