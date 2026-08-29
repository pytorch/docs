# Aliases in torch.optim

Most optimizer classes are available both from `torch.optim` and from the
nested module in which they are defined. For example, `torch.optim.Adam` and
`torch.optim.adam.Adam` refer to the same class. While some functional optimizer APIs are exposed in their respective nested modules, all functional
optimizer APIs are available in the [`torch.optim.functional`](optim.functional.html#module-torch.optim.functional) namespace; see
[Functional optimizer API](optim.html#functional-optimizer-api) for usage guidance.

| [`Adadelta`](generated/torch.optim.adadelta.Adadelta_class.html#torch.optim.adadelta.Adadelta) | Implements Adadelta algorithm. |
| --- | --- |
| [`adadelta`](generated/torch.optim.adadelta.adadelta_function.html#torch.optim.adadelta.adadelta) | Functional API that performs Adadelta algorithm computation. |

| [`Adagrad`](generated/torch.optim.adagrad.Adagrad_class.html#torch.optim.adagrad.Adagrad) | Implements Adagrad algorithm. |
| --- | --- |
| [`adagrad`](generated/torch.optim.adagrad.adagrad_function.html#torch.optim.adagrad.adagrad) | Functional API that performs Adagrad algorithm computation. |

| [`Adam`](generated/torch.optim.adam.Adam_class.html#torch.optim.adam.Adam) | Implements Adam algorithm. |
| --- | --- |
| [`adam`](generated/torch.optim.adam.adam_function.html#torch.optim.adam.adam) | Functional API that performs Adam algorithm computation. |

| [`Adamax`](generated/torch.optim.adamax.Adamax_class.html#torch.optim.adamax.Adamax) | Implements Adamax algorithm (a variant of Adam based on infinity norm). |
| --- | --- |
| [`adamax`](generated/torch.optim.adamax.adamax_function.html#torch.optim.adamax.adamax) | Functional API that performs Adamax algorithm computation. |

| [`AdamW`](generated/torch.optim.adamw.AdamW_class.html#torch.optim.adamw.AdamW) | Implements AdamW algorithm, where weight decay does not accumulate in the momentum nor variance. |
| --- | --- |
| [`adamw`](generated/torch.optim.adamw.adamw_function.html#torch.optim.adamw.adamw) | Functional API that performs AdamW algorithm computation. |

| [`ASGD`](generated/torch.optim.asgd.ASGD_class.html#torch.optim.asgd.ASGD) | Implements Averaged Stochastic Gradient Descent. |
| --- | --- |
| [`asgd`](generated/torch.optim.asgd.asgd_function.html#torch.optim.asgd.asgd) | Functional API that performs ASGD algorithm computation. |

| [`LBFGS`](generated/torch.optim.lbfgs.LBFGS.html#torch.optim.lbfgs.LBFGS) | Implements L-BFGS algorithm. |
| --- | --- |

Implementation for the NAdam algorithm.

| [`NAdam`](generated/torch.optim.nadam.NAdam_class.html#torch.optim.nadam.NAdam) | Implements NAdam algorithm. |
| --- | --- |
| [`nadam`](generated/torch.optim.nadam.nadam_function.html#torch.optim.nadam.nadam) | Functional API that performs NAdam algorithm computation. |

Implementation for the RAdam algorithm.

| [`RAdam`](generated/torch.optim.radam.RAdam_class.html#torch.optim.radam.RAdam) | Implements RAdam algorithm. |
| --- | --- |
| [`radam`](generated/torch.optim.radam.radam_function.html#torch.optim.radam.radam) | Functional API that performs RAdam algorithm computation. |

Implementation for the RMSprop algorithm.

| [`RMSprop`](generated/torch.optim.rmsprop.RMSprop_class.html#torch.optim.rmsprop.RMSprop) | Implements RMSprop algorithm. |
| --- | --- |
| [`rmsprop`](generated/torch.optim.rmsprop.rmsprop_function.html#torch.optim.rmsprop.rmsprop) | Functional API that performs RMSprop algorithm computation. |

Implementation for the Resilient backpropagation.

| [`Rprop`](generated/torch.optim.rprop.Rprop_class.html#torch.optim.rprop.Rprop) | Implements the resilient backpropagation algorithm. |
| --- | --- |
| [`rprop`](generated/torch.optim.rprop.rprop_function.html#torch.optim.rprop.rprop) | Functional API that performs Rprop algorithm computation. |

Implementation for Stochastic Gradient Descent optimizer.

| [`SGD`](generated/torch.optim.sgd.SGD_class.html#torch.optim.sgd.SGD) | Implements stochastic gradient descent (optionally with momentum). |
| --- | --- |
| [`sgd`](generated/torch.optim.sgd.sgd_function.html#torch.optim.sgd.sgd) | Functional API that performs SGD algorithm computation. |

| [`SparseAdam`](generated/torch.optim.sparse_adam.SparseAdam.html#torch.optim.sparse_adam.SparseAdam) | SparseAdam implements a masked version of the Adam algorithm suitable for sparse gradients. |
| --- | --- |