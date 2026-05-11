# Aliases in torch.ao

The following are aliases to their counterparts in `torch.ao` in nested namespaces.

## torch.ao.nn.intrinsic.qat.modules

The following are aliases to their counterparts in `torch.ao.nn.intrinsic.qat` in the `torch.ao.nn.intrinsic.qat.module` namespace.

### torch.ao.nn.intrinsic.qat.modules.conv_fused (Aliases)

| [`conv_fused.ConvReLU1d`](generated/torch.ao.nn.intrinsic.qat.modules.conv_fused.ConvReLU1d.html#torch.ao.nn.intrinsic.qat.modules.conv_fused.ConvReLU1d) | A ConvReLU1d module is a fused module of Conv1d and ReLU, attached with FakeQuantize modules for weight for quantization aware training. |
| --- | --- |
| [`conv_fused.ConvReLU2d`](generated/torch.ao.nn.intrinsic.qat.modules.conv_fused.ConvReLU2d.html#torch.ao.nn.intrinsic.qat.modules.conv_fused.ConvReLU2d) | A ConvReLU2d module is a fused module of Conv2d and ReLU, attached with FakeQuantize modules for weight for quantization aware training. |
| [`conv_fused.ConvReLU3d`](generated/torch.ao.nn.intrinsic.qat.modules.conv_fused.ConvReLU3d.html#torch.ao.nn.intrinsic.qat.modules.conv_fused.ConvReLU3d) | A ConvReLU3d module is a fused module of Conv3d and ReLU, attached with FakeQuantize modules for weight for quantization aware training. |
| [`conv_fused.ConvBnReLU1d`](generated/torch.ao.nn.intrinsic.qat.modules.conv_fused.ConvBnReLU1d.html#torch.ao.nn.intrinsic.qat.modules.conv_fused.ConvBnReLU1d) | A ConvBnReLU1d module is a module fused from Conv1d, BatchNorm1d and ReLU, attached with FakeQuantize modules for weight, used in quantization aware training. |
| [`conv_fused.ConvBnReLU2d`](generated/torch.ao.nn.intrinsic.qat.modules.conv_fused.ConvBnReLU2d.html#torch.ao.nn.intrinsic.qat.modules.conv_fused.ConvBnReLU2d) | A ConvBnReLU2d module is a module fused from Conv2d, BatchNorm2d and ReLU, attached with FakeQuantize modules for weight, used in quantization aware training. |
| [`conv_fused.ConvBnReLU3d`](generated/torch.ao.nn.intrinsic.qat.modules.conv_fused.ConvBnReLU3d.html#torch.ao.nn.intrinsic.qat.modules.conv_fused.ConvBnReLU3d) | A ConvBnReLU3d module is a module fused from Conv3d, BatchNorm3d and ReLU, attached with FakeQuantize modules for weight, used in quantization aware training. |

### torch.ao.nn.intrinsic.qat.modules.linear_fused (Aliases)

| [`linear_fused.LinearBn1d`](generated/torch.ao.nn.intrinsic.qat.modules.linear_fused.LinearBn1d.html#torch.ao.nn.intrinsic.qat.modules.linear_fused.LinearBn1d) | A LinearBn1d module is a module fused from Linear and BatchNorm1d, attached with FakeQuantize modules for weight, used in quantization aware training. |
| --- | --- |

### torch.ao.nn.intrinsic.qat.modules.linear_relu (Aliases)

| [`linear_relu.LinearReLU`](generated/torch.ao.nn.intrinsic.qat.modules.linear_relu.LinearReLU.html#torch.ao.nn.intrinsic.qat.modules.linear_relu.LinearReLU) | A LinearReLU module fused from Linear and ReLU modules, attached with FakeQuantize modules for weight, used in quantization aware training. |
| --- | --- |

## torch.ao.nn.intrinsic.quantized.modules

The following are aliases to their counterparts in `torch.ao.nn.intrinsic.quantized` in the `torch.ao.nn.intrinsic.quantized.modules` namespace.

### torch.ao.nn.intrinsic.quantized.modules.conv_relu (Aliases)

| [`conv_relu.ConvReLU1d`](generated/torch.ao.nn.intrinsic.quantized.modules.conv_relu.ConvReLU1d.html#torch.ao.nn.intrinsic.quantized.modules.conv_relu.ConvReLU1d) | A ConvReLU1d module is a fused module of Conv1d and ReLU |
| --- | --- |
| [`conv_relu.ConvReLU2d`](generated/torch.ao.nn.intrinsic.quantized.modules.conv_relu.ConvReLU2d.html#torch.ao.nn.intrinsic.quantized.modules.conv_relu.ConvReLU2d) | A ConvReLU2d module is a fused module of Conv2d and ReLU |
| [`conv_relu.ConvReLU3d`](generated/torch.ao.nn.intrinsic.quantized.modules.conv_relu.ConvReLU3d.html#torch.ao.nn.intrinsic.quantized.modules.conv_relu.ConvReLU3d) | A ConvReLU3d module is a fused module of Conv3d and ReLU |

### torch.ao.nn.intrinsic.quantized.modules.bn_relu (Aliases)

| [`bn_relu.BNReLU2d`](generated/torch.ao.nn.intrinsic.quantized.modules.bn_relu.BNReLU2d.html#torch.ao.nn.intrinsic.quantized.modules.bn_relu.BNReLU2d) | A BNReLU2d module is a fused module of BatchNorm2d and ReLU |
| --- | --- |
| [`bn_relu.BNReLU3d`](generated/torch.ao.nn.intrinsic.quantized.modules.bn_relu.BNReLU3d.html#torch.ao.nn.intrinsic.quantized.modules.bn_relu.BNReLU3d) | A BNReLU3d module is a fused module of BatchNorm3d and ReLU |

### torch.ao.nn.intrinsic.quantized.modules.conv_add (Aliases)

| [`conv_add.ConvAdd2d`](generated/torch.ao.nn.intrinsic.quantized.modules.conv_add.ConvAdd2d.html#torch.ao.nn.intrinsic.quantized.modules.conv_add.ConvAdd2d) | A ConvAdd2d module is a fused module of Conv2d and Add |
| --- | --- |
| [`conv_add.ConvAddReLU2d`](generated/torch.ao.nn.intrinsic.quantized.modules.conv_add.ConvAddReLU2d.html#torch.ao.nn.intrinsic.quantized.modules.conv_add.ConvAddReLU2d) | A ConvAddReLU2d module is a fused module of Conv2d, Add and Relu |

### torch.ao.nn.intrinsic.quantized.modules.linear_relu (Aliases)

| [`linear_relu.LinearLeakyReLU`](generated/torch.ao.nn.intrinsic.quantized.modules.linear_relu.LinearLeakyReLU.html#torch.ao.nn.intrinsic.quantized.modules.linear_relu.LinearLeakyReLU) | For onednn backend only A LinearLeakyReLU module fused from Linear and LeakyReLU modules We adopt the same interface as [`torch.ao.nn.quantized.Linear`](generated/torch.ao.nn.quantized.Linear.html#torch.ao.nn.quantized.Linear). |
| --- | --- |
| [`linear_relu.LinearReLU`](generated/torch.ao.nn.intrinsic.quantized.modules.linear_relu.LinearReLU.html#torch.ao.nn.intrinsic.quantized.modules.linear_relu.LinearReLU) | A LinearReLU module fused from Linear and ReLU modules |
| [`linear_relu.LinearTanh`](generated/torch.ao.nn.intrinsic.quantized.modules.linear_relu.LinearTanh.html#torch.ao.nn.intrinsic.quantized.modules.linear_relu.LinearTanh) | A LinearTanh module fused from Linear and Tanh modules |

## torch.ao.nn.intrinsic.quantized.dynamic.modules

The following are aliases to their counterparts in the `torch.ao.nn.intrinsic.quantized.dynamic` namespace.

### torch.ao.nn.intrinsic.quantized.dynamic.modules.linear_relu (Aliases)

| [`linear_relu.LinearReLU`](generated/torch.ao.nn.intrinsic.quantized.dynamic.modules.linear_relu.LinearReLU.html#torch.ao.nn.intrinsic.quantized.dynamic.modules.linear_relu.LinearReLU) | A LinearReLU module fused from Linear and ReLU modules that can be used for dynamic quantization. |
| --- | --- |

## torch.ao.nn.intrinsic.modules

The following are aliases to their counterparts in the `torch.ao.nn.intrinsic` namespace.

### torch.ao.nn.intrinsic.modules.fused (Aliases)

| [`fused.ConvAdd2d`](generated/torch.ao.nn.intrinsic.modules.fused.ConvAdd2d.html#torch.ao.nn.intrinsic.modules.fused.ConvAdd2d) | This is a sequential container which calls the Conv2d modules with extra Add. |
| --- | --- |
| [`fused.ConvAddReLU2d`](generated/torch.ao.nn.intrinsic.modules.fused.ConvAddReLU2d.html#torch.ao.nn.intrinsic.modules.fused.ConvAddReLU2d) | This is a sequential container which calls the Conv2d, add, Relu. |
| [`fused.LinearBn1d`](generated/torch.ao.nn.intrinsic.modules.fused.LinearBn1d.html#torch.ao.nn.intrinsic.modules.fused.LinearBn1d) | This is a sequential container which calls the Linear and BatchNorm1d modules. |
| [`fused.LinearLeakyReLU`](generated/torch.ao.nn.intrinsic.modules.fused.LinearLeakyReLU.html#torch.ao.nn.intrinsic.modules.fused.LinearLeakyReLU) | This is a sequential container which calls the Linear and LeakyReLU modules. |
| [`fused.LinearTanh`](generated/torch.ao.nn.intrinsic.modules.fused.LinearTanh.html#torch.ao.nn.intrinsic.modules.fused.LinearTanh) | This is a sequential container which calls the Linear and Tanh modules. |

## torch.ao.nn.intrinsic.modules.torch.ao.nn.qat.modules

The following are aliases to their counterparts in the `torch.ao.nn.qat` namespace.

### torch.ao.nn.intrinsic.modules.conv (Aliases)

| [`conv.Conv1d`](generated/torch.ao.nn.qat.modules.conv.Conv1d.html#torch.ao.nn.qat.modules.conv.Conv1d) | A Conv1d module attached with FakeQuantize modules for weight, used for quantization aware training. |
| --- | --- |
| [`conv.Conv2d`](generated/torch.ao.nn.qat.modules.conv.Conv2d.html#torch.ao.nn.qat.modules.conv.Conv2d) | A Conv2d module attached with FakeQuantize modules for weight, used for quantization aware training. |
| [`conv.Conv3d`](generated/torch.ao.nn.qat.modules.conv.Conv3d.html#torch.ao.nn.qat.modules.conv.Conv3d) | A Conv3d module attached with FakeQuantize modules for weight, used for quantization aware training. |

### torch.ao.nn.intrinsic.modules.embedding_ops (Aliases)

| [`embedding_ops.Embedding`](generated/torch.ao.nn.qat.modules.embedding_ops.Embedding.html#torch.ao.nn.qat.modules.embedding_ops.Embedding) | An embedding bag module attached with FakeQuantize modules for weight, used for quantization aware training. |
| --- | --- |
| [`embedding_ops.EmbeddingBag`](generated/torch.ao.nn.qat.modules.embedding_ops.EmbeddingBag.html#torch.ao.nn.qat.modules.embedding_ops.EmbeddingBag) | An embedding bag module attached with FakeQuantize modules for weight, used for quantization aware training. |

### torch.ao.nn.intrinsic.modules.linear (Aliases)

| [`linear.Linear`](generated/torch.ao.nn.qat.modules.linear.Linear.html#torch.ao.nn.qat.modules.linear.Linear) | A linear module attached with FakeQuantize modules for weight, used for quantization aware training. |
| --- | --- |

## torch.ao.nn.quantizable.modules

The following are aliases to their counterparts in the `torch.ao.nn.quantizable` namespace.

### torch.ao.nn.quantizable.modules.activation (Aliases)

| [`activation.MultiheadAttention`](generated/torch.ao.nn.quantizable.modules.activation.MultiheadAttention.html#torch.ao.nn.quantizable.modules.activation.MultiheadAttention) | |
| --- | --- |

### torch.ao.nn.quantizable.modules.rnn (Aliases)

| [`rnn.LSTM`](generated/torch.ao.nn.quantizable.modules.rnn.LSTM.html#torch.ao.nn.quantizable.modules.rnn.LSTM) | A quantizable long short-term memory (LSTM). |
| --- | --- |
| [`rnn.LSTMCell`](generated/torch.ao.nn.quantizable.modules.rnn.LSTMCell.html#torch.ao.nn.quantizable.modules.rnn.LSTMCell) | A quantizable long short-term memory (LSTM) cell. |

## torch.ao.nn.quantized.dynamic.modules

The following are aliases to their counterparts in the `torch.ao.nn.quantized.dynamic` namespace.

### torch.ao.nn.quantized.dynamic.modules.conv (Aliases)

| [`conv.Conv1d`](generated/torch.ao.nn.quantized.dynamic.modules.conv.Conv1d.html#torch.ao.nn.quantized.dynamic.modules.conv.Conv1d) | A dynamically quantized conv module with floating point tensors as inputs and outputs. |
| --- | --- |
| [`conv.Conv2d`](generated/torch.ao.nn.quantized.dynamic.modules.conv.Conv2d.html#torch.ao.nn.quantized.dynamic.modules.conv.Conv2d) | A dynamically quantized conv module with floating point tensors as inputs and outputs. |
| [`conv.Conv3d`](generated/torch.ao.nn.quantized.dynamic.modules.conv.Conv3d.html#torch.ao.nn.quantized.dynamic.modules.conv.Conv3d) | A dynamically quantized conv module with floating point tensors as inputs and outputs. |
| [`conv.ConvTranspose1d`](generated/torch.ao.nn.quantized.dynamic.modules.conv.ConvTranspose1d.html#torch.ao.nn.quantized.dynamic.modules.conv.ConvTranspose1d) | A dynamically quantized transposed convolution module with floating point tensors as inputs and outputs. |
| [`conv.ConvTranspose2d`](generated/torch.ao.nn.quantized.dynamic.modules.conv.ConvTranspose2d.html#torch.ao.nn.quantized.dynamic.modules.conv.ConvTranspose2d) | A dynamically quantized transposed convolution module with floating point tensors as inputs and outputs. |
| [`conv.ConvTranspose3d`](generated/torch.ao.nn.quantized.dynamic.modules.conv.ConvTranspose3d.html#torch.ao.nn.quantized.dynamic.modules.conv.ConvTranspose3d) | A dynamically quantized transposed convolution module with floating point tensors as inputs and outputs. |

### torch.ao.nn.quantized.dynamic.modules.linear (Aliases)

| [`linear.Linear`](generated/torch.ao.nn.quantized.dynamic.modules.linear.Linear.html#torch.ao.nn.quantized.dynamic.modules.linear.Linear) | A dynamic quantized linear module with floating point tensor as inputs and outputs. |
| --- | --- |

### torch.ao.nn.quantized.dynamic.modules.rnn (Aliases)

| [`rnn.GRU`](generated/torch.ao.nn.quantized.dynamic.modules.rnn.GRU.html#torch.ao.nn.quantized.dynamic.modules.rnn.GRU) | Applies a multi-layer gated recurrent unit (GRU) RNN to an input sequence. |
| --- | --- |
| [`rnn.GRUCell`](generated/torch.ao.nn.quantized.dynamic.modules.rnn.GRUCell.html#torch.ao.nn.quantized.dynamic.modules.rnn.GRUCell) | A gated recurrent unit (GRU) cell |
| [`rnn.LSTM`](generated/torch.ao.nn.quantized.dynamic.modules.rnn.LSTM.html#torch.ao.nn.quantized.dynamic.modules.rnn.LSTM) | A dynamic quantized LSTM module with floating point tensor as inputs and outputs. |
| [`rnn.LSTMCell`](generated/torch.ao.nn.quantized.dynamic.modules.rnn.LSTMCell.html#torch.ao.nn.quantized.dynamic.modules.rnn.LSTMCell) | A long short-term memory (LSTM) cell. |
| [`rnn.PackedParameter`](generated/torch.ao.nn.quantized.dynamic.modules.rnn.PackedParameter.html#torch.ao.nn.quantized.dynamic.modules.rnn.PackedParameter) | |
| [`rnn.RNNBase`](generated/torch.ao.nn.quantized.dynamic.modules.rnn.RNNBase.html#torch.ao.nn.quantized.dynamic.modules.rnn.RNNBase) | |
| [`rnn.RNNCell`](generated/torch.ao.nn.quantized.dynamic.modules.rnn.RNNCell.html#torch.ao.nn.quantized.dynamic.modules.rnn.RNNCell) | An Elman RNN cell with tanh or ReLU non-linearity. |
| [`rnn.RNNCellBase`](generated/torch.ao.nn.quantized.dynamic.modules.rnn.RNNCellBase.html#torch.ao.nn.quantized.dynamic.modules.rnn.RNNCellBase) | |