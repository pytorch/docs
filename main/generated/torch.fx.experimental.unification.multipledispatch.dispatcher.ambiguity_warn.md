# torch.fx.experimental.unification.multipledispatch.dispatcher.ambiguity_warn

torch.fx.experimental.unification.multipledispatch.dispatcher.ambiguity_warn(*dispatcher*, *ambiguities*)[[source]](https://github.com/pytorch/pytorch/blob/42ce6b4043d9279c8e3672392306dacc772c1b43/torch/fx/experimental/unification/multipledispatch/dispatcher.py#L40)

Raise warning when ambiguity is detected.

Parameters:

- **dispatcher** (*Dispatcher*) - The dispatcher on which the ambiguity was detected
- **ambiguities** ([*set*](https://docs.python.org/3/builtins/stdtypes.html#set)) - Set of type signature pairs that are ambiguous within this dispatcher

See also

`Dispatcher.add`, [`warning_text`](torch.fx.experimental.unification.multipledispatch.dispatcher.warning_text.html#torch.fx.experimental.unification.multipledispatch.dispatcher.warning_text)