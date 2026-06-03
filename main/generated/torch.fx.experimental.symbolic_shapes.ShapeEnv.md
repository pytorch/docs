# ShapeEnv

*class*torch.fx.experimental.symbolic_shapes.ShapeEnv(***, *should_record_events=None*, *tracked_fakes=None*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L3812)

add_backed_var_to_val(*expr*, *val*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L5775)

Adds a new symbol to the symbolic environment.

add_var_to_val(*expr*, *val*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L5791)

Deprecated: use add_backed_var_to_val instead.

bind_symbols(*placeholders*, *args*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L6851)

Given a paired list of placeholders (fake tensors with
symbolic sizes) and concrete arguments (regular tensors
with real sizes), returns a dictionary mapping each
symbol to its real value. So for example, if you
have a placeholder with size (s0, s1), binding
(2, 4) to it will give you {s0: 2, s1: 4}. This is
not guaranteed to bind ALL symbols in the ShapeEnv;
we can't bind a symbol if it doesn't occur in any placeholder,
and symbols that already have replacements won't get bindings.

This is a little duplicative with evaluate_guards but
it's different enough that it seemed cleanest to make
another copy. This assumes the guards are already checked,
though if it's cheap we'll check for shenanigans

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[sympy.Symbol, [int](https://docs.python.org/3/library/functions.html#int)]

bound_sympy(*expr*, *size_oblivious=False*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L6926)

Given a sympy expression, computes a ValueRanges bound for what values it can be

Return type:

*ValueRanges*[*Expr*]

check_equal(*other*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L4245)

Compare another ShapeEnv for equivalence

cleanup()[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L8530)

Break reference cycles.

This destroys the stacks. If you really want to keep them, we
just need some way to break references on code objects.

create_symbol(*val*, *source*, *dynamic_dim=DimDynamic.DUCK*, *constraint_dim=None*, *positive=True*, *do_not_specialize_zero_one=False*, *symbolic_context=None*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L5462)

Create a new symbol which is tracked by this ShapeEnv

Return type:

sympy.Expr

create_symbolic_sizes_strides_storage_offset(*ex*, *source*, ***, *symbolic_context=None*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L4758)

Create symbolic sizes/strides/offset for a tensor.

If the tensor has symbolic sizes from a different ShapeEnv,
delegates to transfer_symbols_from_foreign_shape_env.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[IntLikeType, ...], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[IntLikeType, ...], IntLikeType]

create_symboolnode(*sym*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L5287)

Create a SymBool object from a sympy boolean expression

Return type:

[*SymBool*](../torch.html#torch.SymBool)

create_symfloatnode(*sym*, ***, *hint*, *source=None*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L5219)

Create a SymFloat value from a symbolic expression

Return type:

FloatLikeType

create_symintnode(*sym*, ***, *hint*, *source=None*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L5173)

Create a SymInt value from a symbolic expression

If you know what the current hint value of the SymInt to be created
is, pass it into hint. Otherwise, pass None and we will make our best
guess

Return type:

IntLikeType

create_unbacked_symbool()[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L5405)

Create a symbolic boolean without a hint value

Return type:

[*SymBool*](../torch.html#torch.SymBool)

create_unbacked_symfloat()[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L5330)

Create a symbolic float without a hint value

Return type:

[*SymFloat*](../torch.html#torch.SymFloat)

create_unbacked_symint(*source=None*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L5357)

Create a symbolic integer without a hint value

Return type:

[*SymInt*](../torch.html#torch.SymInt)

create_unspecified_symbol(*val*, *source*, *dynamic_dim=DimDynamic.DUCK*, *constraint_dim=None*, *symbolic_context=None*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L5432)

Create a symbol with an unspecified value

Compared to standard symbols we do not assume the value is positive,
nor do we specialze on zero or one values.

Return type:

*Expr*

create_unspecified_symint_and_symbol(*value*, *source*, *dynamic_dim*, *excluded_value=None*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L5265)

Create a SymInt wrapping a new unspecified symbol

Return type:

IntLikeType

deserialize_symexpr(*code*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L6806)

To be used by compile_fx to deserialize symexprs

Return type:

[*SymInt*](../torch.html#torch.SymInt) | [*SymFloat*](../torch.html#torch.SymFloat) | [*SymBool*](../torch.html#torch.SymBool)

error_on_new_guards()[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L4626)

Context manager that raises _ShapeEnvGuardError if a guard is attempted.

Temporarily freezes the ShapeEnv and makes _check_frozen raise
instead of warn, so that guard-installing code paths produce an
exception that is not cached by the _inner_evaluate_expr LRU cache.

Return type:

[*Generator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator)[None, None, None]

evaluate_expr(*orig_expr*, *hint=None*, *fx_node=None*, *size_oblivious=False*, *fallback_value=None*, ***, *forcing_spec=False*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L8165)

Given an expression, evaluates it, adding guards if necessary
When fallback_value is not None the function return fallback_value instead of failing with data dependent error.

Return type:

*Basic*

evaluate_guards_expression(*code*, *args*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L6816)

Expected to be used with produce_guards_expression(). Evaluates an expression
generated by produce_guards_expression for the given concrete args.

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

evaluate_guards_for_args(*placeholders*, *args*, ***, *ignore_static=True*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L6824)

Generate guards for a graph's placeholder values and evaluate the guards with args

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

evaluate_sym_node(*sym_node*, *size_oblivious=False*, *fallback_value=None*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L8075)

Given a SymNode, evaluates sym_node.expr, adding guards if necessary.

Return type:

*Basic*

evaluate_symexpr(*code*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L6799)

To be used by compile_fx to evaluate symexprs

Return type:

[int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float) | [bool](https://docs.python.org/3/library/functions.html#bool)

format_guards(*verbose=False*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L6918)

Format this shape env's guard expressions with optional traceback info if verbose

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str)

freeze()[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L4483)

Freeze this ShapeEnv to stop accumulating guards

A frozen ShapeEnv will ignore any further guards generated on it and
only emit a warning which may lead to accuracy problems.

freeze_runtime_asserts()[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L4492)

Freeze this ShapeEnv to stop adding deferred runtime asserts.

We will error if you try to install a new runtime assert when it is
frozen. This would indicate a lowering violation, or perhaps something
we know statically is already True but we are checking it again in a way
that is not clearly dischargeable.

get_axioms(*symbols=None*, *compute_hint=False*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L6944)

Given the symbols in an expression, it returns all the runtime asserts that have those symbols
concatenated with all the guards.
If symbols is None, it returns all the runtime asserts (and all the guards)

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[sympy.logic.boolalg.Boolean, ...]

get_implications(*e*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L6975)

Given a expression, it returns a list of predicates that follow from it

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[sympy.logic.boolalg.Boolean, *BooleanAtom*], ...]

get_nontrivial_guards()[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L6907)

Returns a list of guard expressions that aren't statically known (i.e. not trivial)

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[sympy.logic.boolalg.Boolean]

get_pruned_guards(*symints*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L6837)

Get a list of guards, but pruned so it only provides guards that
reference symints from the passed in input

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[*ShapeGuard*]

guard_or_defer_runtime_assert(*orig_expr*, *msg*, *fx_node=None*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L8566)

Adds a guard that orig_expr is True if we can or fall back to adding an assert
that is checked at runtime.

Parameters:

- **orig_expr** (*sympy.Expr*) - Boolean expression to assert is true
- **msg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Message to display on assertion failure
- **fx_node** (*Optional**,*[*torch.fx.Node*](../fx.html#torch.fx.Node)) - node in `self.graph` corresponding
to the expression, if applicable

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

guarding_hint_or_throw(*expr*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L7341)

Return a concrete hint for an expression.

Returns Python bool (True/False) for boolean expressions (e.g. Eq, Ne),
and Python int for integer expressions.

Return type:

[int](https://docs.python.org/3/library/functions.html#int) | [bool](https://docs.python.org/3/library/functions.html#bool)

ignore_fresh_unbacked_symbols()[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L4471)

Indicates that the newly allocated unbacked SymInts are being
discarded

Return type:

[*Generator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator)[None, None, None]

is_unbacked_symint(*symbol*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L5383)

Check if a sympy symbol matches the naming convention for unbacked symbols

Return type:

[bool](https://docs.python.org/3/library/functions.html#bool)

optimization_hint(*expr*, *fallback=None*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L7359)

Return a concrete integer hint for an expression.

This function should be used for non-guarding based optimizations. If you
want a hint that you can guard on, use the guarding_hint API instead.

This function will hint unbacked symbols using user provided optimization
hints. If not provided, fallback will be used along with some heuristics
that try to maximize consistency with the shape environment.

Special cases:

- Complex numbers (containing sympy.I): raises an error since tensor
dimensions cannot be complex.
- Infinity (int_oo, sympy.oo): returns sys.maxsize.
- NaN (sympy.nan): returns the fallback value.

Return type:

[int](https://docs.python.org/3/library/functions.html#int)

patch_source_specialization(*source*, *check_fn*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L4199)

Temporarily add symbol-level axioms to the ShapeEnv. This is useful when you want to "fork"
and have parallel universes of ShapeEnvs. For example, we use this when doing multi-graph
compile so we can support various graphs with varying levels of specializations.

This context manager allows for temporarily adding constraints to the shape environment
based on a specialization function applied to a symbol associated with a source.

Parameters:

- **source** (*Source*) - The source of the symbol to specialize
- **check_fn** ([*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)*[**[**Symbol**]**,**Expr**]*) - A function that takes a sympy Symbol and returns a sympy expression
representing a constraint/specialization to be applied

Return type:

[*Generator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator)[None, None, None]

produce_guards(**args*, ***kwargs*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L5825)

Like produce_guards_verbose, but only returns the non-verbose python guard expressions
(no verbose guards produced.)

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]

produce_guards_expression(*placeholders*, ***, *guards=None*, *ignore_static=True*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L6774)

Expected to be used with evaluate_guards_expression(). Produces the guards
for the given placeholders and returns a string expression to be evaluated
by evaluate_guards_expression given concrete values for the placeholders.

Return type:

[str](https://docs.python.org/3/library/stdtypes.html#str) | None

produce_guards_verbose(*placeholders*, *sources*, *source_ref=<function ShapeEnv.<lambda>>*, ***, *guards=None*, *input_contexts=None*, *equalities_inputs=None*, *_simplified=False*, *ignore_static=True*, *langs=('python'*, *'verbose_python')*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L5832)

Generates a list of guards strings which, when evaluated in a context that
defines tensors for all the sources, returns True or False depending
on if the guards in the list evaluated to True or not. Primarily used by Dynamo,
but this is also helpful for manual testing of guards (see
evaluate_guards_for_args)

For convenience in testing, a source is allowed to be a str,
in which case we will assume it is a LocalSource

simplified lets you omit duck sizing, equality and 0/1 guards.
This is useful for testing when you don't care about the boilerplate
guards, and it may be helpful for user output too (be careful though;
some equality guards are nontrivial! It would be nice to get simplified
output to print them too). It's private because it's not
intended for normal use

Returns guards in python and python with verbose comments (verbose) by
default.

Return type:

[list](https://docs.python.org/3/library/stdtypes.html#list)[_ShapeGuardsHelper]

replace(*expr*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L7173)

Apply symbol replacements to any symbols in the given expression.

IMPORTANT: The output of this method MUST depend only on
self.replacements and the input expr. Do not add dependencies on other
mutable state. SymNode.expr uses _replacements_version_counter (which
tracks only replacement changes) to cache calls to this method, so
depending on other state would cause stale cache results.

Return type:

*_SympyT*

set_real_tensor_prop_unbacked_vals(*k*, *v*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L4343)

Used only when propagate_real_tensors; registers a value for an
unbacked symbol, which can be used last resort to resolve hints.

simplify(*expr*, *size_oblivious=False*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L7211)

Use known constraints and replacements to simplify the given expr

Return type:

*_SympyT*

size_hint(*expr*, ***, *allow_none=False*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L7291)

Gets a size hint for a given expression from the underlying shapes we had.
Does not introduce a guard, so only use this when you can guarantee that
your code is still valid for arbitrary shapes (such as optimization decisions)

Return type:

*Basic* | None

suppress_guards()[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L4622)

Context manager to ignore all guards generated inside.

Return type:

*_GeneratorContextManager*[None]

transfer_symbols_from_foreign_shape_env(*sizes*, *strides*, *storage_offset*, *source*, ***, *symbolic_context=None*, *hint_overrides=None*)[[source]](https://github.com/pytorch/pytorch/blob/9ab94917c245d16efe77f546d30d73800c8d728d/torch/fx/experimental/symbolic_shapes.py#L4792)

Transfer symbolic sizes/strides/offset from a foreign ShapeEnv
into this one.

If symbolic_context is None, each dimension is auto-classified as
STATIC, DUCK, or UNBACKED based on whether the foreign symbol has
a guarding hint. If symbolic_context is provided (e.g. from
_automatic_dynamic), its classification is used instead.

For unbacked dims, strides are derived by substituting old foreign
symbols with the newly created symbols, preserving stride-size
relationships. Hint overrides are read from the foreign ShapeEnv
and transferred to the new one.

Return type:

[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[IntLikeType, ...], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[IntLikeType, ...], IntLikeType]

*property*var_to_val*: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[Symbol, Integer]*

use backed_var_to_val instead.

Type:

Deprecated