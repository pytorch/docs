# torch.fx.experimental.unification.multipledispatch.dispatcher.ambiguity_warn

torch.fx.experimental.unification.multipledispatch.dispatcher.ambiguity_warn(*dispatcher*, *ambiguities*)[[source]](https://github.com/pytorch/pytorch/blob/a62499b17156f49891b06593215215c6df2f94b4/torch/fx/experimental/unification/multipledispatch/dispatcher.py#L40)

Raise warning when ambiguity is detected.

Parameters:

- **dispatcher** (*Dispatcher*) - The dispatcher on which the ambiguity was detected
- **ambiguities** ([*set*](https://docs.python.org/3/library/stdtypes.html#set)) - Set of type signature pairs that are ambiguous within this dispatcher

See also

`Dispatcher.add`, [`warning_text`](torch.fx.experimental.unification.multipledispatch.dispatcher.warning_text.html#torch.fx.experimental.unification.multipledispatch.dispatcher.warning_text)