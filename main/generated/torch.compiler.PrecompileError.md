# torch.compiler.PrecompileError

*exception*torch.compiler.PrecompileError

The error type raised by `torch.compiler.precompile` and its artifacts.

Raised when capture, lowering, `load`, or a runtime call violates the precompile
contract - e.g. a tensor baked as a constant (invariant 1), an unsupported /
effectful op, a non-tensor output the inductor backend cannot lower, or a runtime
input whose shape or memory format differs from the example (invariants 3 and 6).
See Note [precompile programming model] in this module for the full contract.