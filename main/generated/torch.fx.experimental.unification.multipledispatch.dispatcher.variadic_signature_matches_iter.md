# torch.fx.experimental.unification.multipledispatch.dispatcher.variadic_signature_matches_iter

torch.fx.experimental.unification.multipledispatch.dispatcher.variadic_signature_matches_iter(*types*, *full_signature*)[[source]](https://github.com/pytorch/pytorch/blob/56964c25c21235cf3a06679d2e400195087f64fb/torch/fx/experimental/unification/multipledispatch/dispatcher.py#L77)

Check if a set of input types matches a variadic signature.

Notes

The algorithm is as follows:

Initialize the current signature to the first in the sequence.
For each type in `types`:

- If the current signature is variadic

- If the type matches the signature, yield True
- Else, try to get the next signature.
If no signatures are left we can't possibly have a match,
so yield False.
- Else, yield True if the type matches the current signature.
Get the next signature.

Return type:

[Generator](torch.Generator.html#torch.Generator)[[bool](https://docs.python.org/3/library/functions.html#bool), None, None]