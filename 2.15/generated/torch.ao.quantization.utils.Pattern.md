# Pattern

*class*torch.ao.quantization.utils.Pattern

Create named, parameterized type aliases.

This provides a backport of the new type statement in Python 3.12:

> type ListOrSet[T] = list[T] | set[T]

is equivalent to:

> T = TypeVar("T")
> ListOrSet = TypeAliasType("ListOrSet", list[T] | set[T], type_params=(T,))

The name ListOrSet can then be used as an alias for the type it refers to.

The type_params argument should contain all the type parameters used
in the value of the type alias. If the alias is not generic, this
argument is omitted.

Static type checkers should only support type aliases declared using
TypeAliasType that follow these rules:

- The first argument (the name) must be a string literal.
- The TypeAliasType instance must be immediately assigned to a variable
of the same name. (For example, 'X = TypeAliasType("Y", int)' is invalid,
as is 'X, Y = TypeAliasType("X", int), TypeAliasType("Y", int)').