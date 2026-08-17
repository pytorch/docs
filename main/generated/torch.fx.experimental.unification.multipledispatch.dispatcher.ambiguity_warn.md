# torch.fx.experimental.unification.multipledispatch.dispatcher.ambiguity_warn

torch.fx.experimental.unification.multipledispatch.dispatcher.ambiguity_warn(*dispatcher*, *ambiguities*)[[source]](https://github.com/pytorch/pytorch/blob/99fcf9fd884002c14d4c19cce5dfe2469ba5a7fc/torch/fx/experimental/unification/multipledispatch/dispatcher.py#L40)

Raise warning when ambiguity is detected.

Parameters:

- **dispatcher** (*Dispatcher*) - The dispatcher on which the ambiguity was detected
- **ambiguities** ([*set*](https://docs.python.org/3/library/stdtypes.html#set)) - Set of type signature pairs that are ambiguous within this dispatcher

See also

`Dispatcher.add`, [`warning_text`](torch.fx.experimental.unification.multipledispatch.dispatcher.warning_text.html#torch.fx.experimental.unification.multipledispatch.dispatcher.warning_text)