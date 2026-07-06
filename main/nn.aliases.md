# Aliases in torch.nn

The following are aliases to their counterparts in `torch.nn` in nested namespaces.

## torch.nn.modules

The following are aliases to their counterparts in `torch.nn` in the `torch.nn.modules` namespace.

### Containers (Aliases)

| [`container.Sequential`](generated/torch.nn.modules.container.Sequential.html#torch.nn.modules.container.Sequential) | A sequential container. |
| --- | --- |
| [`container.ModuleList`](generated/torch.nn.modules.container.ModuleList.html#torch.nn.modules.container.ModuleList) | Holds submodules in a list. |
| [`container.ModuleDict`](generated/torch.nn.modules.container.ModuleDict.html#torch.nn.modules.container.ModuleDict) | Holds submodules in a dictionary. |
| [`container.ParameterList`](generated/torch.nn.modules.container.ParameterList.html#torch.nn.modules.container.ParameterList) | Holds parameters in a list. |
| [`container.ParameterDict`](generated/torch.nn.modules.container.ParameterDict.html#torch.nn.modules.container.ParameterDict) | Holds parameters in a dictionary. |

### Convolution Layers (Aliases)

| [`conv.Conv1d`](generated/torch.nn.modules.conv.Conv1d.html#torch.nn.modules.conv.Conv1d) | Applies a 1D convolution over an input signal composed of several input planes. |
| --- | --- |
| [`conv.Conv2d`](generated/torch.nn.modules.conv.Conv2d.html#torch.nn.modules.conv.Conv2d) | Applies a 2D convolution over an input signal composed of several input planes. |
| [`conv.Conv3d`](generated/torch.nn.modules.conv.Conv3d.html#torch.nn.modules.conv.Conv3d) | Applies a 3D convolution over an input signal composed of several input planes. |
| [`conv.ConvTranspose1d`](generated/torch.nn.modules.conv.ConvTranspose1d.html#torch.nn.modules.conv.ConvTranspose1d) | Applies a 1D transposed convolution operator over an input image composed of several input planes. |
| [`conv.ConvTranspose2d`](generated/torch.nn.modules.conv.ConvTranspose2d.html#torch.nn.modules.conv.ConvTranspose2d) | Applies a 2D transposed convolution operator over an input image composed of several input planes. |
| [`conv.ConvTranspose3d`](generated/torch.nn.modules.conv.ConvTranspose3d.html#torch.nn.modules.conv.ConvTranspose3d) | Applies a 3D transposed convolution operator over an input image composed of several input planes. |
| [`conv.LazyConv1d`](generated/torch.nn.modules.conv.LazyConv1d.html#torch.nn.modules.conv.LazyConv1d) | A [`torch.nn.Conv1d`](generated/torch.nn.Conv1d.html#torch.nn.Conv1d) module with lazy initialization of the `in_channels` argument. |
| [`conv.LazyConv2d`](generated/torch.nn.modules.conv.LazyConv2d.html#torch.nn.modules.conv.LazyConv2d) | A [`torch.nn.Conv2d`](generated/torch.nn.Conv2d.html#torch.nn.Conv2d) module with lazy initialization of the `in_channels` argument. |
| [`conv.LazyConv3d`](generated/torch.nn.modules.conv.LazyConv3d.html#torch.nn.modules.conv.LazyConv3d) | A [`torch.nn.Conv3d`](generated/torch.nn.Conv3d.html#torch.nn.Conv3d) module with lazy initialization of the `in_channels` argument. |
| [`conv.LazyConvTranspose1d`](generated/torch.nn.modules.conv.LazyConvTranspose1d.html#torch.nn.modules.conv.LazyConvTranspose1d) | A [`torch.nn.ConvTranspose1d`](generated/torch.nn.ConvTranspose1d.html#torch.nn.ConvTranspose1d) module with lazy initialization of the `in_channels` argument. |
| [`conv.LazyConvTranspose2d`](generated/torch.nn.modules.conv.LazyConvTranspose2d.html#torch.nn.modules.conv.LazyConvTranspose2d) | A [`torch.nn.ConvTranspose2d`](generated/torch.nn.ConvTranspose2d.html#torch.nn.ConvTranspose2d) module with lazy initialization of the `in_channels` argument. |
| [`conv.LazyConvTranspose3d`](generated/torch.nn.modules.conv.LazyConvTranspose3d.html#torch.nn.modules.conv.LazyConvTranspose3d) | A [`torch.nn.ConvTranspose3d`](generated/torch.nn.ConvTranspose3d.html#torch.nn.ConvTranspose3d) module with lazy initialization of the `in_channels` argument. |
| [`fold.Unfold`](generated/torch.nn.modules.fold.Unfold.html#torch.nn.modules.fold.Unfold) | Extracts sliding local blocks from a batched input tensor. |
| [`fold.Fold`](generated/torch.nn.modules.fold.Fold.html#torch.nn.modules.fold.Fold) | Combines an array of sliding local blocks into a large containing tensor. |

### Pooling layers (Aliases)

| [`pooling.MaxPool1d`](generated/torch.nn.modules.pooling.MaxPool1d.html#torch.nn.modules.pooling.MaxPool1d) | Applies a 1D max pooling over an input signal composed of several input planes. |
| --- | --- |
| [`pooling.MaxPool2d`](generated/torch.nn.modules.pooling.MaxPool2d.html#torch.nn.modules.pooling.MaxPool2d) | Applies a 2D max pooling over an input signal composed of several input planes. |
| [`pooling.MaxPool3d`](generated/torch.nn.modules.pooling.MaxPool3d.html#torch.nn.modules.pooling.MaxPool3d) | Applies a 3D max pooling over an input signal composed of several input planes. |
| [`pooling.MaxUnpool1d`](generated/torch.nn.modules.pooling.MaxUnpool1d.html#torch.nn.modules.pooling.MaxUnpool1d) | Computes a partial inverse of `MaxPool1d`. |
| [`pooling.MaxUnpool2d`](generated/torch.nn.modules.pooling.MaxUnpool2d.html#torch.nn.modules.pooling.MaxUnpool2d) | Computes a partial inverse of `MaxPool2d`. |
| [`pooling.MaxUnpool3d`](generated/torch.nn.modules.pooling.MaxUnpool3d.html#torch.nn.modules.pooling.MaxUnpool3d) | Computes a partial inverse of `MaxPool3d`. |
| [`pooling.AvgPool1d`](generated/torch.nn.modules.pooling.AvgPool1d.html#torch.nn.modules.pooling.AvgPool1d) | Applies a 1D average pooling over an input signal composed of several input planes. |
| [`pooling.AvgPool2d`](generated/torch.nn.modules.pooling.AvgPool2d.html#torch.nn.modules.pooling.AvgPool2d) | Applies a 2D average pooling over an input signal composed of several input planes. |
| [`pooling.AvgPool3d`](generated/torch.nn.modules.pooling.AvgPool3d.html#torch.nn.modules.pooling.AvgPool3d) | Applies a 3D average pooling over an input signal composed of several input planes. |
| [`pooling.FractionalMaxPool2d`](generated/torch.nn.modules.pooling.FractionalMaxPool2d.html#torch.nn.modules.pooling.FractionalMaxPool2d) | Applies a 2D fractional max pooling over an input signal composed of several input planes. |
| [`pooling.FractionalMaxPool3d`](generated/torch.nn.modules.pooling.FractionalMaxPool3d.html#torch.nn.modules.pooling.FractionalMaxPool3d) | Applies a 3D fractional max pooling over an input signal composed of several input planes. |
| [`pooling.LPPool1d`](generated/torch.nn.modules.pooling.LPPool1d.html#torch.nn.modules.pooling.LPPool1d) | Applies a 1D power-average pooling over an input signal composed of several input planes. |
| [`pooling.LPPool2d`](generated/torch.nn.modules.pooling.LPPool2d.html#torch.nn.modules.pooling.LPPool2d) | Applies a 2D power-average pooling over an input signal composed of several input planes. |
| [`pooling.LPPool3d`](generated/torch.nn.modules.pooling.LPPool3d.html#torch.nn.modules.pooling.LPPool3d) | Applies a 3D power-average pooling over an input signal composed of several input planes. |
| [`pooling.AdaptiveMaxPool1d`](generated/torch.nn.modules.pooling.AdaptiveMaxPool1d.html#torch.nn.modules.pooling.AdaptiveMaxPool1d) | Applies a 1D adaptive max pooling over an input signal composed of several input planes. |
| [`pooling.AdaptiveMaxPool2d`](generated/torch.nn.modules.pooling.AdaptiveMaxPool2d.html#torch.nn.modules.pooling.AdaptiveMaxPool2d) | Applies a 2D adaptive max pooling over an input signal composed of several input planes. |
| [`pooling.AdaptiveMaxPool3d`](generated/torch.nn.modules.pooling.AdaptiveMaxPool3d.html#torch.nn.modules.pooling.AdaptiveMaxPool3d) | Applies a 3D adaptive max pooling over an input signal composed of several input planes. |
| [`pooling.AdaptiveAvgPool1d`](generated/torch.nn.modules.pooling.AdaptiveAvgPool1d.html#torch.nn.modules.pooling.AdaptiveAvgPool1d) | Applies a 1D adaptive average pooling over an input signal composed of several input planes. |
| [`pooling.AdaptiveAvgPool2d`](generated/torch.nn.modules.pooling.AdaptiveAvgPool2d.html#torch.nn.modules.pooling.AdaptiveAvgPool2d) | Applies a 2D adaptive average pooling over an input signal composed of several input planes. |
| [`pooling.AdaptiveAvgPool3d`](generated/torch.nn.modules.pooling.AdaptiveAvgPool3d.html#torch.nn.modules.pooling.AdaptiveAvgPool3d) | Applies a 3D adaptive average pooling over an input signal composed of several input planes. |

### Padding Layers (Aliases)

| [`padding.ReflectionPad1d`](generated/torch.nn.modules.padding.ReflectionPad1d.html#torch.nn.modules.padding.ReflectionPad1d) | Pads the input tensor using the reflection of the input boundary. |
| --- | --- |
| [`padding.ReflectionPad2d`](generated/torch.nn.modules.padding.ReflectionPad2d.html#torch.nn.modules.padding.ReflectionPad2d) | Pads the input tensor using the reflection of the input boundary. |
| [`padding.ReflectionPad3d`](generated/torch.nn.modules.padding.ReflectionPad3d.html#torch.nn.modules.padding.ReflectionPad3d) | Pads the input tensor using the reflection of the input boundary. |
| [`padding.ReplicationPad1d`](generated/torch.nn.modules.padding.ReplicationPad1d.html#torch.nn.modules.padding.ReplicationPad1d) | Pads the input tensor using replication of the input boundary. |
| [`padding.ReplicationPad2d`](generated/torch.nn.modules.padding.ReplicationPad2d.html#torch.nn.modules.padding.ReplicationPad2d) | Pads the input tensor using replication of the input boundary. |
| [`padding.ReplicationPad3d`](generated/torch.nn.modules.padding.ReplicationPad3d.html#torch.nn.modules.padding.ReplicationPad3d) | Pads the input tensor using replication of the input boundary. |
| [`padding.ZeroPad1d`](generated/torch.nn.modules.padding.ZeroPad1d.html#torch.nn.modules.padding.ZeroPad1d) | Pads the input tensor boundaries with zero. |
| [`padding.ZeroPad2d`](generated/torch.nn.modules.padding.ZeroPad2d.html#torch.nn.modules.padding.ZeroPad2d) | Pads the input tensor boundaries with zero. |
| [`padding.ZeroPad3d`](generated/torch.nn.modules.padding.ZeroPad3d.html#torch.nn.modules.padding.ZeroPad3d) | Pads the input tensor boundaries with zero. |
| [`padding.ConstantPad1d`](generated/torch.nn.modules.padding.ConstantPad1d.html#torch.nn.modules.padding.ConstantPad1d) | Pads the input tensor boundaries with a constant value. |
| [`padding.ConstantPad2d`](generated/torch.nn.modules.padding.ConstantPad2d.html#torch.nn.modules.padding.ConstantPad2d) | Pads the input tensor boundaries with a constant value. |
| [`padding.ConstantPad3d`](generated/torch.nn.modules.padding.ConstantPad3d.html#torch.nn.modules.padding.ConstantPad3d) | Pads the input tensor boundaries with a constant value. |
| [`padding.CircularPad1d`](generated/torch.nn.modules.padding.CircularPad1d.html#torch.nn.modules.padding.CircularPad1d) | Pads the input tensor using circular padding of the input boundary. |
| [`padding.CircularPad2d`](generated/torch.nn.modules.padding.CircularPad2d.html#torch.nn.modules.padding.CircularPad2d) | Pads the input tensor using circular padding of the input boundary. |
| [`padding.CircularPad3d`](generated/torch.nn.modules.padding.CircularPad3d.html#torch.nn.modules.padding.CircularPad3d) | Pads the input tensor using circular padding of the input boundary. |

### Non-linear Activations (weighted sum, nonlinearity) (Aliases)

| [`activation.ELU`](generated/torch.nn.modules.activation.ELU.html#torch.nn.modules.activation.ELU) | Applies the Exponential Linear Unit (ELU) function, element-wise. |
| --- | --- |
| [`activation.Hardshrink`](generated/torch.nn.modules.activation.Hardshrink.html#torch.nn.modules.activation.Hardshrink) | Applies the Hard Shrinkage (Hardshrink) function element-wise. |
| [`activation.Hardsigmoid`](generated/torch.nn.modules.activation.Hardsigmoid.html#torch.nn.modules.activation.Hardsigmoid) | Applies the Hardsigmoid function element-wise. |
| [`activation.Hardtanh`](generated/torch.nn.modules.activation.Hardtanh.html#torch.nn.modules.activation.Hardtanh) | Applies the HardTanh function element-wise. |
| [`activation.Hardswish`](generated/torch.nn.modules.activation.Hardswish.html#torch.nn.modules.activation.Hardswish) | Applies the Hardswish function, element-wise. |
| [`activation.LeakyReLU`](generated/torch.nn.modules.activation.LeakyReLU.html#torch.nn.modules.activation.LeakyReLU) | Applies the LeakyReLU function element-wise. |
| [`activation.LogSigmoid`](generated/torch.nn.modules.activation.LogSigmoid.html#torch.nn.modules.activation.LogSigmoid) | Applies the Logsigmoid function element-wise. |
| [`activation.MultiheadAttention`](generated/torch.nn.modules.activation.MultiheadAttention.html#torch.nn.modules.activation.MultiheadAttention) | Allows the model to jointly attend to information from different representation subspaces. |
| [`activation.PReLU`](generated/torch.nn.modules.activation.PReLU.html#torch.nn.modules.activation.PReLU) | Applies the element-wise PReLU function. |
| [`activation.ReLU`](generated/torch.nn.modules.activation.ReLU.html#torch.nn.modules.activation.ReLU) | Applies the rectified linear unit function element-wise. |
| [`activation.ReLU6`](generated/torch.nn.modules.activation.ReLU6.html#torch.nn.modules.activation.ReLU6) | Applies the ReLU6 function element-wise. |
| [`activation.RReLU`](generated/torch.nn.modules.activation.RReLU.html#torch.nn.modules.activation.RReLU) | Applies the randomized leaky rectified linear unit function, element-wise. |
| [`activation.SELU`](generated/torch.nn.modules.activation.SELU.html#torch.nn.modules.activation.SELU) | Applies the SELU function element-wise. |
| [`activation.CELU`](generated/torch.nn.modules.activation.CELU.html#torch.nn.modules.activation.CELU) | Applies the CELU function element-wise. |
| [`activation.GELU`](generated/torch.nn.modules.activation.GELU.html#torch.nn.modules.activation.GELU) | Applies the Gaussian Error Linear Units function. |
| [`activation.Sigmoid`](generated/torch.nn.modules.activation.Sigmoid.html#torch.nn.modules.activation.Sigmoid) | Applies the Sigmoid function element-wise. |
| [`activation.SiLU`](generated/torch.nn.modules.activation.SiLU.html#torch.nn.modules.activation.SiLU) | Applies the Sigmoid Linear Unit (SiLU) function, element-wise. |
| [`activation.Mish`](generated/torch.nn.modules.activation.Mish.html#torch.nn.modules.activation.Mish) | Applies the Mish function, element-wise. |
| [`activation.Softplus`](generated/torch.nn.modules.activation.Softplus.html#torch.nn.modules.activation.Softplus) | Applies the Softplus function element-wise. |
| [`activation.Softshrink`](generated/torch.nn.modules.activation.Softshrink.html#torch.nn.modules.activation.Softshrink) | Applies the soft shrinkage function element-wise. |
| [`activation.Softsign`](generated/torch.nn.modules.activation.Softsign.html#torch.nn.modules.activation.Softsign) | Applies the element-wise Softsign function. |
| [`activation.Tanh`](generated/torch.nn.modules.activation.Tanh.html#torch.nn.modules.activation.Tanh) | Applies the Hyperbolic Tangent (Tanh) function element-wise. |
| [`activation.Tanhshrink`](generated/torch.nn.modules.activation.Tanhshrink.html#torch.nn.modules.activation.Tanhshrink) | Applies the element-wise Tanhshrink function. |
| [`activation.Threshold`](generated/torch.nn.modules.activation.Threshold.html#torch.nn.modules.activation.Threshold) | Thresholds each element of the input Tensor. |
| [`activation.GLU`](generated/torch.nn.modules.activation.GLU.html#torch.nn.modules.activation.GLU) | Applies the gated linear unit function. |

### Non-linear Activations (other) (Aliases)

| [`activation.Softmin`](generated/torch.nn.modules.activation.Softmin.html#torch.nn.modules.activation.Softmin) | Applies the Softmin function to an n-dimensional input Tensor. |
| --- | --- |
| [`activation.Softmax`](generated/torch.nn.modules.activation.Softmax.html#torch.nn.modules.activation.Softmax) | Applies the Softmax function to an n-dimensional input Tensor. |
| [`activation.Softmax2d`](generated/torch.nn.modules.activation.Softmax2d.html#torch.nn.modules.activation.Softmax2d) | Applies SoftMax over features to each spatial location. |
| [`activation.LogSoftmax`](generated/torch.nn.modules.activation.LogSoftmax.html#torch.nn.modules.activation.LogSoftmax) | Applies the log⁡(Softmax(x))\log(\text{Softmax}(x))log(Softmax(x)) function to an n-dimensional input Tensor. |
| [`adaptive.AdaptiveLogSoftmaxWithLoss`](generated/torch.nn.modules.adaptive.AdaptiveLogSoftmaxWithLoss.html#torch.nn.modules.adaptive.AdaptiveLogSoftmaxWithLoss) | Efficient softmax approximation. |

### Normalization Layers (Aliases)

| [`batchnorm.BatchNorm1d`](generated/torch.nn.modules.batchnorm.BatchNorm1d.html#torch.nn.modules.batchnorm.BatchNorm1d) | Applies Batch Normalization over a 2D or 3D input. |
| --- | --- |
| [`batchnorm.BatchNorm2d`](generated/torch.nn.modules.batchnorm.BatchNorm2d.html#torch.nn.modules.batchnorm.BatchNorm2d) | Applies Batch Normalization over a 4D input. |
| [`batchnorm.BatchNorm3d`](generated/torch.nn.modules.batchnorm.BatchNorm3d.html#torch.nn.modules.batchnorm.BatchNorm3d) | Applies Batch Normalization over a 5D input. |
| [`batchnorm.LazyBatchNorm1d`](generated/torch.nn.modules.batchnorm.LazyBatchNorm1d.html#torch.nn.modules.batchnorm.LazyBatchNorm1d) | A [`torch.nn.BatchNorm1d`](generated/torch.nn.BatchNorm1d.html#torch.nn.BatchNorm1d) module with lazy initialization. |
| [`batchnorm.LazyBatchNorm2d`](generated/torch.nn.modules.batchnorm.LazyBatchNorm2d.html#torch.nn.modules.batchnorm.LazyBatchNorm2d) | A [`torch.nn.BatchNorm2d`](generated/torch.nn.BatchNorm2d.html#torch.nn.BatchNorm2d) module with lazy initialization. |
| [`batchnorm.LazyBatchNorm3d`](generated/torch.nn.modules.batchnorm.LazyBatchNorm3d.html#torch.nn.modules.batchnorm.LazyBatchNorm3d) | A [`torch.nn.BatchNorm3d`](generated/torch.nn.BatchNorm3d.html#torch.nn.BatchNorm3d) module with lazy initialization. |
| [`normalization.GroupNorm`](generated/torch.nn.modules.normalization.GroupNorm.html#torch.nn.modules.normalization.GroupNorm) | Applies Group Normalization over a mini-batch of inputs. |
| [`batchnorm.SyncBatchNorm`](generated/torch.nn.modules.batchnorm.SyncBatchNorm.html#torch.nn.modules.batchnorm.SyncBatchNorm) | Applies Batch Normalization over a N-Dimensional input. |
| [`instancenorm.InstanceNorm1d`](generated/torch.nn.modules.instancenorm.InstanceNorm1d.html#torch.nn.modules.instancenorm.InstanceNorm1d) | Applies Instance Normalization. |
| [`instancenorm.InstanceNorm2d`](generated/torch.nn.modules.instancenorm.InstanceNorm2d.html#torch.nn.modules.instancenorm.InstanceNorm2d) | Applies Instance Normalization. |
| [`instancenorm.InstanceNorm3d`](generated/torch.nn.modules.instancenorm.InstanceNorm3d.html#torch.nn.modules.instancenorm.InstanceNorm3d) | Applies Instance Normalization. |
| [`instancenorm.LazyInstanceNorm1d`](generated/torch.nn.modules.instancenorm.LazyInstanceNorm1d.html#torch.nn.modules.instancenorm.LazyInstanceNorm1d) | A [`torch.nn.InstanceNorm1d`](generated/torch.nn.InstanceNorm1d.html#torch.nn.InstanceNorm1d) module with lazy initialization of the `num_features` argument. |
| [`instancenorm.LazyInstanceNorm2d`](generated/torch.nn.modules.instancenorm.LazyInstanceNorm2d.html#torch.nn.modules.instancenorm.LazyInstanceNorm2d) | A [`torch.nn.InstanceNorm2d`](generated/torch.nn.InstanceNorm2d.html#torch.nn.InstanceNorm2d) module with lazy initialization of the `num_features` argument. |
| [`instancenorm.LazyInstanceNorm3d`](generated/torch.nn.modules.instancenorm.LazyInstanceNorm3d.html#torch.nn.modules.instancenorm.LazyInstanceNorm3d) | A [`torch.nn.InstanceNorm3d`](generated/torch.nn.InstanceNorm3d.html#torch.nn.InstanceNorm3d) module with lazy initialization of the `num_features` argument. |
| [`normalization.LayerNorm`](generated/torch.nn.modules.normalization.LayerNorm.html#torch.nn.modules.normalization.LayerNorm) | Applies Layer Normalization over a mini-batch of inputs. |
| [`normalization.LocalResponseNorm`](generated/torch.nn.modules.normalization.LocalResponseNorm.html#torch.nn.modules.normalization.LocalResponseNorm) | Applies local response normalization over an input signal. |
| [`normalization.RMSNorm`](generated/torch.nn.modules.normalization.RMSNorm.html#torch.nn.modules.normalization.RMSNorm) | Applies Root Mean Square Layer Normalization over a mini-batch of inputs. |

### Recurrent Layers (Aliases)

| [`rnn.RNNBase`](generated/torch.nn.modules.rnn.RNNBase.html#torch.nn.modules.rnn.RNNBase) | Base class for RNN modules (RNN, LSTM, GRU). |
| --- | --- |
| [`rnn.RNN`](generated/torch.nn.modules.rnn.RNN.html#torch.nn.modules.rnn.RNN) | Apply a multi-layer Elman RNN with tanh⁡\tanhtanh or ReLU\text{ReLU}ReLU non-linearity to an input sequence. |
| [`rnn.LSTM`](generated/torch.nn.modules.rnn.LSTM.html#torch.nn.modules.rnn.LSTM) | Apply a multi-layer long short-term memory (LSTM) RNN to an input sequence. |
| [`rnn.GRU`](generated/torch.nn.modules.rnn.GRU.html#torch.nn.modules.rnn.GRU) | Apply a multi-layer gated recurrent unit (GRU) RNN to an input sequence. |
| [`rnn.RNNCell`](generated/torch.nn.modules.rnn.RNNCell.html#torch.nn.modules.rnn.RNNCell) | An Elman RNN cell with tanh or ReLU non-linearity. |
| [`rnn.LSTMCell`](generated/torch.nn.modules.rnn.LSTMCell.html#torch.nn.modules.rnn.LSTMCell) | A long short-term memory (LSTM) cell. |
| [`rnn.GRUCell`](generated/torch.nn.modules.rnn.GRUCell.html#torch.nn.modules.rnn.GRUCell) | A gated recurrent unit (GRU) cell. |

### Transformer Layers (Aliases)

| [`transformer.Transformer`](generated/torch.nn.modules.transformer.Transformer.html#torch.nn.modules.transformer.Transformer) | A basic transformer layer. |
| --- | --- |
| [`transformer.TransformerEncoder`](generated/torch.nn.modules.transformer.TransformerEncoder.html#torch.nn.modules.transformer.TransformerEncoder) | TransformerEncoder is a stack of N encoder layers. |
| [`transformer.TransformerDecoder`](generated/torch.nn.modules.transformer.TransformerDecoder.html#torch.nn.modules.transformer.TransformerDecoder) | TransformerDecoder is a stack of N decoder layers. |
| [`transformer.TransformerEncoderLayer`](generated/torch.nn.modules.transformer.TransformerEncoderLayer.html#torch.nn.modules.transformer.TransformerEncoderLayer) | TransformerEncoderLayer is made up of self-attn and feedforward network. |
| [`transformer.TransformerDecoderLayer`](generated/torch.nn.modules.transformer.TransformerDecoderLayer.html#torch.nn.modules.transformer.TransformerDecoderLayer) | TransformerDecoderLayer is made up of self-attn, multi-head-attn and feedforward network. |

### Linear Layers (Aliases)

| [`linear.Identity`](generated/torch.nn.modules.linear.Identity.html#torch.nn.modules.linear.Identity) | A placeholder identity operator that is argument-insensitive. |
| --- | --- |
| [`linear.Linear`](generated/torch.nn.modules.linear.Linear.html#torch.nn.modules.linear.Linear) | Applies an affine linear transformation to the incoming data: y=xAT+by = xA^T + by=xAT+b. |
| [`linear.Bilinear`](generated/torch.nn.modules.linear.Bilinear.html#torch.nn.modules.linear.Bilinear) | Applies a bilinear transformation to the incoming data: y=x1TAx2+by = x_1^T A x_2 + by=x1T​Ax2​+b. |
| [`linear.LazyLinear`](generated/torch.nn.modules.linear.LazyLinear.html#torch.nn.modules.linear.LazyLinear) | A [`torch.nn.Linear`](generated/torch.nn.Linear.html#torch.nn.Linear) module where in_features is inferred. |

### Dropout Layers (Aliases)

| [`dropout.Dropout`](generated/torch.nn.modules.dropout.Dropout.html#torch.nn.modules.dropout.Dropout) | During training, randomly zeroes some of the elements of the input tensor with probability `p`. |
| --- | --- |
| [`dropout.Dropout1d`](generated/torch.nn.modules.dropout.Dropout1d.html#torch.nn.modules.dropout.Dropout1d) | Randomly zero out entire channels. |
| [`dropout.Dropout2d`](generated/torch.nn.modules.dropout.Dropout2d.html#torch.nn.modules.dropout.Dropout2d) | Randomly zero out entire channels. |
| [`dropout.Dropout3d`](generated/torch.nn.modules.dropout.Dropout3d.html#torch.nn.modules.dropout.Dropout3d) | Randomly zero out entire channels. |
| [`dropout.AlphaDropout`](generated/torch.nn.modules.dropout.AlphaDropout.html#torch.nn.modules.dropout.AlphaDropout) | Applies Alpha Dropout over the input. |
| [`dropout.FeatureAlphaDropout`](generated/torch.nn.modules.dropout.FeatureAlphaDropout.html#torch.nn.modules.dropout.FeatureAlphaDropout) | Randomly masks out entire channels. |

### Sparse Layers (Aliases)

| [`sparse.Embedding`](generated/torch.nn.modules.sparse.Embedding.html#torch.nn.modules.sparse.Embedding) | A simple lookup table that stores embeddings of a fixed dictionary and size. |
| --- | --- |
| [`sparse.EmbeddingBag`](generated/torch.nn.modules.sparse.EmbeddingBag.html#torch.nn.modules.sparse.EmbeddingBag) | Compute sums or means of 'bags' of embeddings, without instantiating the intermediate embeddings. |

### Distance Functions (Aliases)

| [`distance.CosineSimilarity`](generated/torch.nn.modules.distance.CosineSimilarity.html#torch.nn.modules.distance.CosineSimilarity) | Returns cosine similarity between x1x_1x1​ and x2x_2x2​, computed along dim. |
| --- | --- |
| [`distance.PairwiseDistance`](generated/torch.nn.modules.distance.PairwiseDistance.html#torch.nn.modules.distance.PairwiseDistance) | Computes the pairwise distance between input vectors, or between columns of input matrices. |

### Loss Functions (Aliases)

| [`loss.L1Loss`](generated/torch.nn.modules.loss.L1Loss.html#torch.nn.modules.loss.L1Loss) | Creates a criterion that measures the mean absolute error (MAE) between each element in the input xxx and target yyy. |
| --- | --- |
| [`loss.MSELoss`](generated/torch.nn.modules.loss.MSELoss.html#torch.nn.modules.loss.MSELoss) | Creates a criterion that measures the mean squared error (squared L2 norm) between each element in the input xxx and target yyy. |
| [`loss.CrossEntropyLoss`](generated/torch.nn.modules.loss.CrossEntropyLoss.html#torch.nn.modules.loss.CrossEntropyLoss) | This criterion computes the cross entropy loss between input logits and target. |
| [`loss.CTCLoss`](generated/torch.nn.modules.loss.CTCLoss.html#torch.nn.modules.loss.CTCLoss) | The Connectionist Temporal Classification loss. |
| [`loss.NLLLoss`](generated/torch.nn.modules.loss.NLLLoss.html#torch.nn.modules.loss.NLLLoss) | The negative log likelihood loss. |
| [`loss.PoissonNLLLoss`](generated/torch.nn.modules.loss.PoissonNLLLoss.html#torch.nn.modules.loss.PoissonNLLLoss) | Negative log likelihood loss with Poisson distribution of target. |
| [`loss.GaussianNLLLoss`](generated/torch.nn.modules.loss.GaussianNLLLoss.html#torch.nn.modules.loss.GaussianNLLLoss) | Gaussian negative log likelihood loss. |
| [`loss.KLDivLoss`](generated/torch.nn.modules.loss.KLDivLoss.html#torch.nn.modules.loss.KLDivLoss) | The Kullback-Leibler divergence loss. |
| [`loss.BCELoss`](generated/torch.nn.modules.loss.BCELoss.html#torch.nn.modules.loss.BCELoss) | Creates a criterion that measures the Binary Cross Entropy between the target and the input probabilities: |
| [`loss.BCEWithLogitsLoss`](generated/torch.nn.modules.loss.BCEWithLogitsLoss.html#torch.nn.modules.loss.BCEWithLogitsLoss) | This loss combines a Sigmoid layer and the BCELoss in one single class. |
| [`loss.MarginRankingLoss`](generated/torch.nn.modules.loss.MarginRankingLoss.html#torch.nn.modules.loss.MarginRankingLoss) | Creates a criterion that measures the loss given inputs x1x1x1, x2x2x2, two 1D mini-batch or 0D Tensors, and a label 1D mini-batch or 0D Tensor yyy (containing 1 or -1). |
| [`loss.HingeEmbeddingLoss`](generated/torch.nn.modules.loss.HingeEmbeddingLoss.html#torch.nn.modules.loss.HingeEmbeddingLoss) | Measures the loss given an input tensor xxx and a labels tensor yyy (containing 1 or -1). |
| [`loss.MultiLabelMarginLoss`](generated/torch.nn.modules.loss.MultiLabelMarginLoss.html#torch.nn.modules.loss.MultiLabelMarginLoss) | Creates a criterion that optimizes a multi-class multi-classification hinge loss (margin-based loss) between input xxx (a 2D mini-batch Tensor) and output yyy (which is a 2D Tensor of target class indices). |
| [`loss.HuberLoss`](generated/torch.nn.modules.loss.HuberLoss.html#torch.nn.modules.loss.HuberLoss) | Creates a criterion that uses a squared term if the absolute element-wise error falls below delta and a delta-scaled L1 term otherwise. |
| [`loss.SmoothL1Loss`](generated/torch.nn.modules.loss.SmoothL1Loss.html#torch.nn.modules.loss.SmoothL1Loss) | Creates a criterion that uses a squared term if the absolute element-wise error falls below beta and an L1 term otherwise. |
| [`loss.SoftMarginLoss`](generated/torch.nn.modules.loss.SoftMarginLoss.html#torch.nn.modules.loss.SoftMarginLoss) | Creates a criterion that optimizes a two-class classification logistic loss between input tensor xxx and target tensor yyy (containing 1 or -1). |
| [`loss.MultiLabelSoftMarginLoss`](generated/torch.nn.modules.loss.MultiLabelSoftMarginLoss.html#torch.nn.modules.loss.MultiLabelSoftMarginLoss) | Creates a criterion that optimizes a multi-label one-versus-all loss based on max-entropy, between input xxx and target yyy of size (N,C)(N, C)(N,C). |
| [`loss.CosineEmbeddingLoss`](generated/torch.nn.modules.loss.CosineEmbeddingLoss.html#torch.nn.modules.loss.CosineEmbeddingLoss) | Creates a criterion that measures the loss given input tensors x1x_1x1​, x2x_2x2​ and a Tensor label yyy with values 1 or -1. |
| [`loss.MultiMarginLoss`](generated/torch.nn.modules.loss.MultiMarginLoss.html#torch.nn.modules.loss.MultiMarginLoss) | Creates a criterion that optimizes a multi-class classification hinge loss (margin-based loss) between input xxx (a 2D mini-batch Tensor) and output yyy (which is a 1D tensor of target class indices, 0≤y≤x.size(1)−10 \leq y \leq \text{x.size}(1)-10≤y≤x.size(1)−1): |
| [`loss.TripletMarginLoss`](generated/torch.nn.modules.loss.TripletMarginLoss.html#torch.nn.modules.loss.TripletMarginLoss) | Creates a criterion that measures the triplet loss given an input tensors x1x1x1, x2x2x2, x3x3x3 and a margin with a value greater than 000. |
| [`loss.TripletMarginWithDistanceLoss`](generated/torch.nn.modules.loss.TripletMarginWithDistanceLoss.html#torch.nn.modules.loss.TripletMarginWithDistanceLoss) | Creates a criterion that measures the triplet loss given input tensors aaa, ppp, and nnn (representing anchor, positive, and negative examples, respectively), and a nonnegative, real-valued function ("distance function") used to compute the relationship between the anchor and positive example ("positive distance") and the anchor and negative example ("negative distance"). |

### Vision Layers (Aliases)

| [`pixelshuffle.PixelShuffle`](generated/torch.nn.modules.pixelshuffle.PixelShuffle.html#torch.nn.modules.pixelshuffle.PixelShuffle) | Rearrange elements in a tensor according to an upscaling factor. |
| --- | --- |
| [`pixelshuffle.PixelUnshuffle`](generated/torch.nn.modules.pixelshuffle.PixelUnshuffle.html#torch.nn.modules.pixelshuffle.PixelUnshuffle) | Reverse the PixelShuffle operation. |
| [`upsampling.Upsample`](generated/torch.nn.modules.upsampling.Upsample.html#torch.nn.modules.upsampling.Upsample) | Upsamples a given multi-channel 1D (temporal), 2D (spatial) or 3D (volumetric) data. |
| [`upsampling.UpsamplingNearest2d`](generated/torch.nn.modules.upsampling.UpsamplingNearest2d.html#torch.nn.modules.upsampling.UpsamplingNearest2d) | Applies a 2D nearest neighbor upsampling to an input signal composed of several input channels. |
| [`upsampling.UpsamplingBilinear2d`](generated/torch.nn.modules.upsampling.UpsamplingBilinear2d.html#torch.nn.modules.upsampling.UpsamplingBilinear2d) | Applies a 2D bilinear upsampling to an input signal composed of several input channels. |

### Shuffle Layers (Aliases)

| [`channelshuffle.ChannelShuffle`](generated/torch.nn.modules.channelshuffle.ChannelShuffle.html#torch.nn.modules.channelshuffle.ChannelShuffle) | Divides and rearranges the channels in a tensor. |
| --- | --- |

## torch.nn.modules.utils

torch.nn.modules.utils.consume_prefix_in_state_dict_if_present(*state_dict*, *prefix*)[[source]](https://github.com/pytorch/pytorch/blob/a059c4af8933be96044a8625669869fe560baf61/torch/nn/modules/utils.py#L48)

Strip the prefix in state_dict in place, if any.

Note

Given a state_dict from a DP/DDP model, a local model can load it by applying
consume_prefix_in_state_dict_if_present(state_dict, "module.") before calling
[`torch.nn.Module.load_state_dict()`](generated/torch.nn.Module.html#torch.nn.Module.load_state_dict).

Parameters:

- **state_dict** (*OrderedDict*) - a state-dict to be loaded to the model.
- **prefix** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - prefix.

## torch.nn.utils

The following are aliases to their counterparts in `torch.nn.utils` in nested namespaces.

Utility functions to clip parameter gradients.

| [`clip_grad.clip_grad_norm_`](generated/torch.nn.utils.clip_grad.clip_grad_norm_.html#torch.nn.utils.clip_grad.clip_grad_norm_) | Clip the gradient norm of an iterable of parameters. |
| --- | --- |
| [`clip_grad.clip_grad_norm`](generated/torch.nn.utils.clip_grad.clip_grad_norm.html#torch.nn.utils.clip_grad.clip_grad_norm) | Clip the gradient norm of an iterable of parameters. |
| [`clip_grad.clip_grad_value_`](generated/torch.nn.utils.clip_grad.clip_grad_value_.html#torch.nn.utils.clip_grad.clip_grad_value_) | Clip the gradients of an iterable of parameters at specified value. |

Utility functions to flatten and unflatten Module parameters to and from a single vector.

| [`convert_parameters.parameters_to_vector`](generated/torch.nn.utils.convert_parameters.parameters_to_vector.html#torch.nn.utils.convert_parameters.parameters_to_vector) | Flatten an iterable of parameters into a single vector. |
| --- | --- |
| [`convert_parameters.vector_to_parameters`](generated/torch.nn.utils.convert_parameters.vector_to_parameters.html#torch.nn.utils.convert_parameters.vector_to_parameters) | Copy slices of a vector into an iterable of parameters. |

Utility functions to fuse Modules with BatchNorm modules.

| [`fusion.fuse_conv_bn_eval`](generated/torch.nn.utils.fusion.fuse_conv_bn_eval.html#torch.nn.utils.fusion.fuse_conv_bn_eval) | Fuse a convolutional module and a BatchNorm module into a single, new convolutional module. |
| --- | --- |
| [`fusion.fuse_conv_bn_weights`](generated/torch.nn.utils.fusion.fuse_conv_bn_weights.html#torch.nn.utils.fusion.fuse_conv_bn_weights) | Fuse convolutional module parameters and BatchNorm module parameters into new convolutional module parameters. |
| [`fusion.fuse_linear_bn_eval`](generated/torch.nn.utils.fusion.fuse_linear_bn_eval.html#torch.nn.utils.fusion.fuse_linear_bn_eval) | Fuse a linear module and a BatchNorm module into a single, new linear module. |
| [`fusion.fuse_linear_bn_weights`](generated/torch.nn.utils.fusion.fuse_linear_bn_weights.html#torch.nn.utils.fusion.fuse_linear_bn_weights) | Fuse linear module parameters and BatchNorm module parameters into new linear module parameters. |

Utility functions to convert Module parameter memory formats.

| [`memory_format.convert_conv2d_weight_memory_format`](generated/torch.nn.utils.memory_format.convert_conv2d_weight_memory_format.html#torch.nn.utils.memory_format.convert_conv2d_weight_memory_format) | Convert `memory_format` of `nn.Conv2d.weight` to `memory_format`. |
| --- | --- |
| [`memory_format.convert_conv3d_weight_memory_format`](generated/torch.nn.utils.memory_format.convert_conv3d_weight_memory_format.html#torch.nn.utils.memory_format.convert_conv3d_weight_memory_format) | Convert `memory_format` of `nn.Conv3d.weight` to `memory_format` The conversion recursively applies to nested `nn.Module`, including `module`. |

Utility functions to apply and remove weight normalization from Module parameters.

| [`weight_norm.weight_norm`](generated/torch.nn.utils.weight_norm.weight_norm.html#torch.nn.utils.weight_norm.weight_norm) | Apply weight normalization to a parameter in the given module. |
| --- | --- |
| [`weight_norm.remove_weight_norm`](generated/torch.nn.utils.weight_norm.remove_weight_norm.html#torch.nn.utils.weight_norm.remove_weight_norm) | Remove the weight normalization reparameterization from a module. |
| [`spectral_norm.spectral_norm`](generated/torch.nn.utils.spectral_norm.spectral_norm.html#torch.nn.utils.spectral_norm.spectral_norm) | Apply spectral normalization to a parameter in the given module. |
| [`spectral_norm.remove_spectral_norm`](generated/torch.nn.utils.spectral_norm.remove_spectral_norm.html#torch.nn.utils.spectral_norm.remove_spectral_norm) | Remove the spectral normalization reparameterization from a module. |

Utility functions for initializing Module parameters.

| [`init.skip_init`](generated/torch.nn.utils.init.skip_init.html#torch.nn.utils.init.skip_init) | Given a module class object and args / kwargs, instantiate the module without initializing parameters / buffers. |
| --- | --- |