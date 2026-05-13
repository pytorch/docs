# torch.nn

These are the basic building blocks for graphs:

| [`Buffer`](generated/torch.nn.parameter.Buffer.html#torch.nn.parameter.Buffer) | A kind of Tensor that should not be considered a model parameter. |
| --- | --- |
| [`Parameter`](generated/torch.nn.parameter.Parameter.html#torch.nn.parameter.Parameter) | A kind of Tensor that is to be considered a module parameter. |
| [`UninitializedParameter`](generated/torch.nn.parameter.UninitializedParameter.html#torch.nn.parameter.UninitializedParameter) | A parameter that is not initialized. |
| [`UninitializedBuffer`](generated/torch.nn.parameter.UninitializedBuffer.html#torch.nn.parameter.UninitializedBuffer) | A buffer that is not initialized. |

## Containers

| [`Module`](generated/torch.nn.Module.html#torch.nn.Module) | Base class for all neural network modules. |
| --- | --- |
| [`Sequential`](generated/torch.nn.Sequential.html#torch.nn.Sequential) | A sequential container. |
| [`ModuleList`](generated/torch.nn.ModuleList.html#torch.nn.ModuleList) | Holds submodules in a list. |
| [`ModuleDict`](generated/torch.nn.ModuleDict.html#torch.nn.ModuleDict) | Holds submodules in a dictionary. |
| [`ParameterList`](generated/torch.nn.ParameterList.html#torch.nn.ParameterList) | Holds parameters in a list. |
| [`ParameterDict`](generated/torch.nn.ParameterDict.html#torch.nn.ParameterDict) | Holds parameters in a dictionary. |

Global Hooks For Module

| [`register_module_forward_pre_hook`](generated/torch.nn.modules.module.register_module_forward_pre_hook.html#torch.nn.modules.module.register_module_forward_pre_hook) | Register a forward pre-hook common to all modules. |
| --- | --- |
| [`register_module_forward_hook`](generated/torch.nn.modules.module.register_module_forward_hook.html#torch.nn.modules.module.register_module_forward_hook) | Register a global forward hook for all the modules. |
| [`register_module_backward_hook`](generated/torch.nn.modules.module.register_module_backward_hook.html#torch.nn.modules.module.register_module_backward_hook) | Register a backward hook common to all the modules. |
| [`register_module_full_backward_pre_hook`](generated/torch.nn.modules.module.register_module_full_backward_pre_hook.html#torch.nn.modules.module.register_module_full_backward_pre_hook) | Register a backward pre-hook common to all the modules. |
| [`register_module_full_backward_hook`](generated/torch.nn.modules.module.register_module_full_backward_hook.html#torch.nn.modules.module.register_module_full_backward_hook) | Register a backward hook common to all the modules. |
| [`register_module_buffer_registration_hook`](generated/torch.nn.modules.module.register_module_buffer_registration_hook.html#torch.nn.modules.module.register_module_buffer_registration_hook) | Register a buffer registration hook common to all modules. |
| [`register_module_module_registration_hook`](generated/torch.nn.modules.module.register_module_module_registration_hook.html#torch.nn.modules.module.register_module_module_registration_hook) | Register a module registration hook common to all modules. |
| [`register_module_parameter_registration_hook`](generated/torch.nn.modules.module.register_module_parameter_registration_hook.html#torch.nn.modules.module.register_module_parameter_registration_hook) | Register a parameter registration hook common to all modules. |

## Convolution Layers

| [`nn.Conv1d`](generated/torch.nn.Conv1d.html#torch.nn.Conv1d) | Applies a 1D convolution over an input signal composed of several input planes. |
| --- | --- |
| [`nn.Conv2d`](generated/torch.nn.Conv2d.html#torch.nn.Conv2d) | Applies a 2D convolution over an input signal composed of several input planes. |
| [`nn.Conv3d`](generated/torch.nn.Conv3d.html#torch.nn.Conv3d) | Applies a 3D convolution over an input signal composed of several input planes. |
| [`nn.ConvTranspose1d`](generated/torch.nn.ConvTranspose1d.html#torch.nn.ConvTranspose1d) | Applies a 1D transposed convolution operator over an input image composed of several input planes. |
| [`nn.ConvTranspose2d`](generated/torch.nn.ConvTranspose2d.html#torch.nn.ConvTranspose2d) | Applies a 2D transposed convolution operator over an input image composed of several input planes. |
| [`nn.ConvTranspose3d`](generated/torch.nn.ConvTranspose3d.html#torch.nn.ConvTranspose3d) | Applies a 3D transposed convolution operator over an input image composed of several input planes. |
| [`nn.LazyConv1d`](generated/torch.nn.LazyConv1d.html#torch.nn.LazyConv1d) | A [`torch.nn.Conv1d`](generated/torch.nn.Conv1d.html#torch.nn.Conv1d) module with lazy initialization of the `in_channels` argument. |
| [`nn.LazyConv2d`](generated/torch.nn.LazyConv2d.html#torch.nn.LazyConv2d) | A [`torch.nn.Conv2d`](generated/torch.nn.Conv2d.html#torch.nn.Conv2d) module with lazy initialization of the `in_channels` argument. |
| [`nn.LazyConv3d`](generated/torch.nn.LazyConv3d.html#torch.nn.LazyConv3d) | A [`torch.nn.Conv3d`](generated/torch.nn.Conv3d.html#torch.nn.Conv3d) module with lazy initialization of the `in_channels` argument. |
| [`nn.LazyConvTranspose1d`](generated/torch.nn.LazyConvTranspose1d.html#torch.nn.LazyConvTranspose1d) | A [`torch.nn.ConvTranspose1d`](generated/torch.nn.ConvTranspose1d.html#torch.nn.ConvTranspose1d) module with lazy initialization of the `in_channels` argument. |
| [`nn.LazyConvTranspose2d`](generated/torch.nn.LazyConvTranspose2d.html#torch.nn.LazyConvTranspose2d) | A [`torch.nn.ConvTranspose2d`](generated/torch.nn.ConvTranspose2d.html#torch.nn.ConvTranspose2d) module with lazy initialization of the `in_channels` argument. |
| [`nn.LazyConvTranspose3d`](generated/torch.nn.LazyConvTranspose3d.html#torch.nn.LazyConvTranspose3d) | A [`torch.nn.ConvTranspose3d`](generated/torch.nn.ConvTranspose3d.html#torch.nn.ConvTranspose3d) module with lazy initialization of the `in_channels` argument. |
| [`nn.Unfold`](generated/torch.nn.Unfold.html#torch.nn.Unfold) | Extracts sliding local blocks from a batched input tensor. |
| [`nn.Fold`](generated/torch.nn.Fold.html#torch.nn.Fold) | Combines an array of sliding local blocks into a large containing tensor. |

## Pooling layers

| [`nn.MaxPool1d`](generated/torch.nn.MaxPool1d.html#torch.nn.MaxPool1d) | Applies a 1D max pooling over an input signal composed of several input planes. |
| --- | --- |
| [`nn.MaxPool2d`](generated/torch.nn.MaxPool2d.html#torch.nn.MaxPool2d) | Applies a 2D max pooling over an input signal composed of several input planes. |
| [`nn.MaxPool3d`](generated/torch.nn.MaxPool3d.html#torch.nn.MaxPool3d) | Applies a 3D max pooling over an input signal composed of several input planes. |
| [`nn.MaxUnpool1d`](generated/torch.nn.MaxUnpool1d.html#torch.nn.MaxUnpool1d) | Computes a partial inverse of `MaxPool1d`. |
| [`nn.MaxUnpool2d`](generated/torch.nn.MaxUnpool2d.html#torch.nn.MaxUnpool2d) | Computes a partial inverse of `MaxPool2d`. |
| [`nn.MaxUnpool3d`](generated/torch.nn.MaxUnpool3d.html#torch.nn.MaxUnpool3d) | Computes a partial inverse of `MaxPool3d`. |
| [`nn.AvgPool1d`](generated/torch.nn.AvgPool1d.html#torch.nn.AvgPool1d) | Applies a 1D average pooling over an input signal composed of several input planes. |
| [`nn.AvgPool2d`](generated/torch.nn.AvgPool2d.html#torch.nn.AvgPool2d) | Applies a 2D average pooling over an input signal composed of several input planes. |
| [`nn.AvgPool3d`](generated/torch.nn.AvgPool3d.html#torch.nn.AvgPool3d) | Applies a 3D average pooling over an input signal composed of several input planes. |
| [`nn.FractionalMaxPool2d`](generated/torch.nn.FractionalMaxPool2d.html#torch.nn.FractionalMaxPool2d) | Applies a 2D fractional max pooling over an input signal composed of several input planes. |
| [`nn.FractionalMaxPool3d`](generated/torch.nn.FractionalMaxPool3d.html#torch.nn.FractionalMaxPool3d) | Applies a 3D fractional max pooling over an input signal composed of several input planes. |
| [`nn.LPPool1d`](generated/torch.nn.LPPool1d.html#torch.nn.LPPool1d) | Applies a 1D power-average pooling over an input signal composed of several input planes. |
| [`nn.LPPool2d`](generated/torch.nn.LPPool2d.html#torch.nn.LPPool2d) | Applies a 2D power-average pooling over an input signal composed of several input planes. |
| [`nn.LPPool3d`](generated/torch.nn.LPPool3d.html#torch.nn.LPPool3d) | Applies a 3D power-average pooling over an input signal composed of several input planes. |
| [`nn.AdaptiveMaxPool1d`](generated/torch.nn.AdaptiveMaxPool1d.html#torch.nn.AdaptiveMaxPool1d) | Applies a 1D adaptive max pooling over an input signal composed of several input planes. |
| [`nn.AdaptiveMaxPool2d`](generated/torch.nn.AdaptiveMaxPool2d.html#torch.nn.AdaptiveMaxPool2d) | Applies a 2D adaptive max pooling over an input signal composed of several input planes. |
| [`nn.AdaptiveMaxPool3d`](generated/torch.nn.AdaptiveMaxPool3d.html#torch.nn.AdaptiveMaxPool3d) | Applies a 3D adaptive max pooling over an input signal composed of several input planes. |
| [`nn.AdaptiveAvgPool1d`](generated/torch.nn.AdaptiveAvgPool1d.html#torch.nn.AdaptiveAvgPool1d) | Applies a 1D adaptive average pooling over an input signal composed of several input planes. |
| [`nn.AdaptiveAvgPool2d`](generated/torch.nn.AdaptiveAvgPool2d.html#torch.nn.AdaptiveAvgPool2d) | Applies a 2D adaptive average pooling over an input signal composed of several input planes. |
| [`nn.AdaptiveAvgPool3d`](generated/torch.nn.AdaptiveAvgPool3d.html#torch.nn.AdaptiveAvgPool3d) | Applies a 3D adaptive average pooling over an input signal composed of several input planes. |

## Padding Layers

| [`nn.ReflectionPad1d`](generated/torch.nn.ReflectionPad1d.html#torch.nn.ReflectionPad1d) | Pads the input tensor using the reflection of the input boundary. |
| --- | --- |
| [`nn.ReflectionPad2d`](generated/torch.nn.ReflectionPad2d.html#torch.nn.ReflectionPad2d) | Pads the input tensor using the reflection of the input boundary. |
| [`nn.ReflectionPad3d`](generated/torch.nn.ReflectionPad3d.html#torch.nn.ReflectionPad3d) | Pads the input tensor using the reflection of the input boundary. |
| [`nn.ReplicationPad1d`](generated/torch.nn.ReplicationPad1d.html#torch.nn.ReplicationPad1d) | Pads the input tensor using replication of the input boundary. |
| [`nn.ReplicationPad2d`](generated/torch.nn.ReplicationPad2d.html#torch.nn.ReplicationPad2d) | Pads the input tensor using replication of the input boundary. |
| [`nn.ReplicationPad3d`](generated/torch.nn.ReplicationPad3d.html#torch.nn.ReplicationPad3d) | Pads the input tensor using replication of the input boundary. |
| [`nn.ZeroPad1d`](generated/torch.nn.ZeroPad1d.html#torch.nn.ZeroPad1d) | Pads the input tensor boundaries with zero. |
| [`nn.ZeroPad2d`](generated/torch.nn.ZeroPad2d.html#torch.nn.ZeroPad2d) | Pads the input tensor boundaries with zero. |
| [`nn.ZeroPad3d`](generated/torch.nn.ZeroPad3d.html#torch.nn.ZeroPad3d) | Pads the input tensor boundaries with zero. |
| [`nn.ConstantPad1d`](generated/torch.nn.ConstantPad1d.html#torch.nn.ConstantPad1d) | Pads the input tensor boundaries with a constant value. |
| [`nn.ConstantPad2d`](generated/torch.nn.ConstantPad2d.html#torch.nn.ConstantPad2d) | Pads the input tensor boundaries with a constant value. |
| [`nn.ConstantPad3d`](generated/torch.nn.ConstantPad3d.html#torch.nn.ConstantPad3d) | Pads the input tensor boundaries with a constant value. |
| [`nn.CircularPad1d`](generated/torch.nn.CircularPad1d.html#torch.nn.CircularPad1d) | Pads the input tensor using circular padding of the input boundary. |
| [`nn.CircularPad2d`](generated/torch.nn.CircularPad2d.html#torch.nn.CircularPad2d) | Pads the input tensor using circular padding of the input boundary. |
| [`nn.CircularPad3d`](generated/torch.nn.CircularPad3d.html#torch.nn.CircularPad3d) | Pads the input tensor using circular padding of the input boundary. |

## Non-linear Activations (weighted sum, nonlinearity)

| [`nn.ELU`](generated/torch.nn.ELU.html#torch.nn.ELU) | Applies the Exponential Linear Unit (ELU) function, element-wise. |
| --- | --- |
| [`nn.Hardshrink`](generated/torch.nn.Hardshrink.html#torch.nn.Hardshrink) | Applies the Hard Shrinkage (Hardshrink) function element-wise. |
| [`nn.Hardsigmoid`](generated/torch.nn.Hardsigmoid.html#torch.nn.Hardsigmoid) | Applies the Hardsigmoid function element-wise. |
| [`nn.Hardtanh`](generated/torch.nn.Hardtanh.html#torch.nn.Hardtanh) | Applies the HardTanh function element-wise. |
| [`nn.Hardswish`](generated/torch.nn.Hardswish.html#torch.nn.Hardswish) | Applies the Hardswish function, element-wise. |
| [`nn.LeakyReLU`](generated/torch.nn.LeakyReLU.html#torch.nn.LeakyReLU) | Applies the LeakyReLU function element-wise. |
| [`nn.LogSigmoid`](generated/torch.nn.LogSigmoid.html#torch.nn.LogSigmoid) | Applies the Logsigmoid function element-wise. |
| [`nn.MultiheadAttention`](generated/torch.nn.MultiheadAttention.html#torch.nn.MultiheadAttention) | Allows the model to jointly attend to information from different representation subspaces. |
| [`nn.PReLU`](generated/torch.nn.PReLU.html#torch.nn.PReLU) | Applies the element-wise PReLU function. |
| [`nn.ReLU`](generated/torch.nn.ReLU.html#torch.nn.ReLU) | Applies the rectified linear unit function element-wise. |
| [`nn.ReLU6`](generated/torch.nn.ReLU6.html#torch.nn.ReLU6) | Applies the ReLU6 function element-wise. |
| [`nn.RReLU`](generated/torch.nn.RReLU.html#torch.nn.RReLU) | Applies the randomized leaky rectified linear unit function, element-wise. |
| [`nn.SELU`](generated/torch.nn.SELU.html#torch.nn.SELU) | Applies the SELU function element-wise. |
| [`nn.CELU`](generated/torch.nn.CELU.html#torch.nn.CELU) | Applies the CELU function element-wise. |
| [`nn.GELU`](generated/torch.nn.GELU.html#torch.nn.GELU) | Applies the Gaussian Error Linear Units function. |
| [`nn.Sigmoid`](generated/torch.nn.Sigmoid.html#torch.nn.Sigmoid) | Applies the Sigmoid function element-wise. |
| [`nn.SiLU`](generated/torch.nn.SiLU.html#torch.nn.SiLU) | Applies the Sigmoid Linear Unit (SiLU) function, element-wise. |
| [`nn.Mish`](generated/torch.nn.Mish.html#torch.nn.Mish) | Applies the Mish function, element-wise. |
| [`nn.Softplus`](generated/torch.nn.Softplus.html#torch.nn.Softplus) | Applies the Softplus function element-wise. |
| [`nn.Softshrink`](generated/torch.nn.Softshrink.html#torch.nn.Softshrink) | Applies the soft shrinkage function element-wise. |
| [`nn.Softsign`](generated/torch.nn.Softsign.html#torch.nn.Softsign) | Applies the element-wise Softsign function. |
| [`nn.Tanh`](generated/torch.nn.Tanh.html#torch.nn.Tanh) | Applies the Hyperbolic Tangent (Tanh) function element-wise. |
| [`nn.Tanhshrink`](generated/torch.nn.Tanhshrink.html#torch.nn.Tanhshrink) | Applies the element-wise Tanhshrink function. |
| [`nn.Threshold`](generated/torch.nn.Threshold.html#torch.nn.Threshold) | Thresholds each element of the input Tensor. |
| [`nn.GLU`](generated/torch.nn.GLU.html#torch.nn.GLU) | Applies the gated linear unit function. |

## Non-linear Activations (other)

| [`nn.Softmin`](generated/torch.nn.Softmin.html#torch.nn.Softmin) | Applies the Softmin function to an n-dimensional input Tensor. |
| --- | --- |
| [`nn.Softmax`](generated/torch.nn.Softmax.html#torch.nn.Softmax) | Applies the Softmax function to an n-dimensional input Tensor. |
| [`nn.Softmax2d`](generated/torch.nn.Softmax2d.html#torch.nn.Softmax2d) | Applies SoftMax over features to each spatial location. |
| [`nn.LogSoftmax`](generated/torch.nn.LogSoftmax.html#torch.nn.LogSoftmax) | Applies the log⁡(Softmax(x))\log(\text{Softmax}(x))log(Softmax(x)) function to an n-dimensional input Tensor. |
| [`nn.AdaptiveLogSoftmaxWithLoss`](generated/torch.nn.AdaptiveLogSoftmaxWithLoss.html#torch.nn.AdaptiveLogSoftmaxWithLoss) | Efficient softmax approximation. |

## Normalization Layers

| [`nn.BatchNorm1d`](generated/torch.nn.BatchNorm1d.html#torch.nn.BatchNorm1d) | Applies Batch Normalization over a 2D or 3D input. |
| --- | --- |
| [`nn.BatchNorm2d`](generated/torch.nn.BatchNorm2d.html#torch.nn.BatchNorm2d) | Applies Batch Normalization over a 4D input. |
| [`nn.BatchNorm3d`](generated/torch.nn.BatchNorm3d.html#torch.nn.BatchNorm3d) | Applies Batch Normalization over a 5D input. |
| [`nn.LazyBatchNorm1d`](generated/torch.nn.LazyBatchNorm1d.html#torch.nn.LazyBatchNorm1d) | A [`torch.nn.BatchNorm1d`](generated/torch.nn.BatchNorm1d.html#torch.nn.BatchNorm1d) module with lazy initialization. |
| [`nn.LazyBatchNorm2d`](generated/torch.nn.LazyBatchNorm2d.html#torch.nn.LazyBatchNorm2d) | A [`torch.nn.BatchNorm2d`](generated/torch.nn.BatchNorm2d.html#torch.nn.BatchNorm2d) module with lazy initialization. |
| [`nn.LazyBatchNorm3d`](generated/torch.nn.LazyBatchNorm3d.html#torch.nn.LazyBatchNorm3d) | A [`torch.nn.BatchNorm3d`](generated/torch.nn.BatchNorm3d.html#torch.nn.BatchNorm3d) module with lazy initialization. |
| [`nn.GroupNorm`](generated/torch.nn.GroupNorm.html#torch.nn.GroupNorm) | Applies Group Normalization over a mini-batch of inputs. |
| [`nn.SyncBatchNorm`](generated/torch.nn.SyncBatchNorm.html#torch.nn.SyncBatchNorm) | Applies Batch Normalization over a N-Dimensional input. |
| [`nn.InstanceNorm1d`](generated/torch.nn.InstanceNorm1d.html#torch.nn.InstanceNorm1d) | Applies Instance Normalization. |
| [`nn.InstanceNorm2d`](generated/torch.nn.InstanceNorm2d.html#torch.nn.InstanceNorm2d) | Applies Instance Normalization. |
| [`nn.InstanceNorm3d`](generated/torch.nn.InstanceNorm3d.html#torch.nn.InstanceNorm3d) | Applies Instance Normalization. |
| [`nn.LazyInstanceNorm1d`](generated/torch.nn.LazyInstanceNorm1d.html#torch.nn.LazyInstanceNorm1d) | A [`torch.nn.InstanceNorm1d`](generated/torch.nn.InstanceNorm1d.html#torch.nn.InstanceNorm1d) module with lazy initialization of the `num_features` argument. |
| [`nn.LazyInstanceNorm2d`](generated/torch.nn.LazyInstanceNorm2d.html#torch.nn.LazyInstanceNorm2d) | A [`torch.nn.InstanceNorm2d`](generated/torch.nn.InstanceNorm2d.html#torch.nn.InstanceNorm2d) module with lazy initialization of the `num_features` argument. |
| [`nn.LazyInstanceNorm3d`](generated/torch.nn.LazyInstanceNorm3d.html#torch.nn.LazyInstanceNorm3d) | A [`torch.nn.InstanceNorm3d`](generated/torch.nn.InstanceNorm3d.html#torch.nn.InstanceNorm3d) module with lazy initialization of the `num_features` argument. |
| [`nn.LayerNorm`](generated/torch.nn.LayerNorm.html#torch.nn.LayerNorm) | Applies Layer Normalization over a mini-batch of inputs. |
| [`nn.LocalResponseNorm`](generated/torch.nn.LocalResponseNorm.html#torch.nn.LocalResponseNorm) | Applies local response normalization over an input signal. |
| [`nn.RMSNorm`](generated/torch.nn.RMSNorm.html#torch.nn.RMSNorm) | Applies Root Mean Square Layer Normalization over a mini-batch of inputs. |

## Recurrent Layers

| [`nn.RNNBase`](generated/torch.nn.RNNBase.html#torch.nn.RNNBase) | Base class for RNN modules (RNN, LSTM, GRU). |
| --- | --- |
| [`nn.RNN`](generated/torch.nn.RNN.html#torch.nn.RNN) | Apply a multi-layer Elman RNN with tanh⁡\tanhtanh or ReLU\text{ReLU}ReLU non-linearity to an input sequence. |
| [`nn.LSTM`](generated/torch.nn.LSTM.html#torch.nn.LSTM) | Apply a multi-layer long short-term memory (LSTM) RNN to an input sequence. |
| [`nn.GRU`](generated/torch.nn.GRU.html#torch.nn.GRU) | Apply a multi-layer gated recurrent unit (GRU) RNN to an input sequence. |
| [`nn.RNNCell`](generated/torch.nn.RNNCell.html#torch.nn.RNNCell) | An Elman RNN cell with tanh or ReLU non-linearity. |
| [`nn.LSTMCell`](generated/torch.nn.LSTMCell.html#torch.nn.LSTMCell) | A long short-term memory (LSTM) cell. |
| [`nn.GRUCell`](generated/torch.nn.GRUCell.html#torch.nn.GRUCell) | A gated recurrent unit (GRU) cell. |

## Transformer Layers

| [`nn.Transformer`](generated/torch.nn.Transformer.html#torch.nn.Transformer) | A basic transformer layer. |
| --- | --- |
| [`nn.TransformerEncoder`](generated/torch.nn.TransformerEncoder.html#torch.nn.TransformerEncoder) | TransformerEncoder is a stack of N encoder layers. |
| [`nn.TransformerDecoder`](generated/torch.nn.TransformerDecoder.html#torch.nn.TransformerDecoder) | TransformerDecoder is a stack of N decoder layers. |
| [`nn.TransformerEncoderLayer`](generated/torch.nn.TransformerEncoderLayer.html#torch.nn.TransformerEncoderLayer) | TransformerEncoderLayer is made up of self-attn and feedforward network. |
| [`nn.TransformerDecoderLayer`](generated/torch.nn.TransformerDecoderLayer.html#torch.nn.TransformerDecoderLayer) | TransformerDecoderLayer is made up of self-attn, multi-head-attn and feedforward network. |

## Linear Layers

| [`nn.Identity`](generated/torch.nn.Identity.html#torch.nn.Identity) | A placeholder identity operator that is argument-insensitive. |
| --- | --- |
| [`nn.Linear`](generated/torch.nn.Linear.html#torch.nn.Linear) | Applies an affine linear transformation to the incoming data: y=xAT+by = xA^T + by=xAT+b. |
| [`nn.Bilinear`](generated/torch.nn.Bilinear.html#torch.nn.Bilinear) | Applies a bilinear transformation to the incoming data: y=x1TAx2+by = x_1^T A x_2 + by=x1T​Ax2​+b. |
| [`nn.LazyLinear`](generated/torch.nn.LazyLinear.html#torch.nn.LazyLinear) | A [`torch.nn.Linear`](generated/torch.nn.Linear.html#torch.nn.Linear) module where in_features is inferred. |

## Dropout Layers

| [`nn.Dropout`](generated/torch.nn.Dropout.html#torch.nn.Dropout) | During training, randomly zeroes some of the elements of the input tensor with probability `p`. |
| --- | --- |
| [`nn.Dropout1d`](generated/torch.nn.Dropout1d.html#torch.nn.Dropout1d) | Randomly zero out entire channels. |
| [`nn.Dropout2d`](generated/torch.nn.Dropout2d.html#torch.nn.Dropout2d) | Randomly zero out entire channels. |
| [`nn.Dropout3d`](generated/torch.nn.Dropout3d.html#torch.nn.Dropout3d) | Randomly zero out entire channels. |
| [`nn.AlphaDropout`](generated/torch.nn.AlphaDropout.html#torch.nn.AlphaDropout) | Applies Alpha Dropout over the input. |
| [`nn.FeatureAlphaDropout`](generated/torch.nn.FeatureAlphaDropout.html#torch.nn.FeatureAlphaDropout) | Randomly masks out entire channels. |

## Sparse Layers

| [`nn.Embedding`](generated/torch.nn.Embedding.html#torch.nn.Embedding) | A simple lookup table that stores embeddings of a fixed dictionary and size. |
| --- | --- |
| [`nn.EmbeddingBag`](generated/torch.nn.EmbeddingBag.html#torch.nn.EmbeddingBag) | Compute sums or means of 'bags' of embeddings, without instantiating the intermediate embeddings. |

## Distance Functions

| [`nn.CosineSimilarity`](generated/torch.nn.CosineSimilarity.html#torch.nn.CosineSimilarity) | Returns cosine similarity between x1x_1x1​ and x2x_2x2​, computed along dim. |
| --- | --- |
| [`nn.PairwiseDistance`](generated/torch.nn.PairwiseDistance.html#torch.nn.PairwiseDistance) | Computes the pairwise distance between input vectors, or between columns of input matrices. |

## Loss Functions

| [`nn.L1Loss`](generated/torch.nn.L1Loss.html#torch.nn.L1Loss) | Creates a criterion that measures the mean absolute error (MAE) between each element in the input xxx and target yyy. |
| --- | --- |
| [`nn.MSELoss`](generated/torch.nn.MSELoss.html#torch.nn.MSELoss) | Creates a criterion that measures the mean squared error (squared L2 norm) between each element in the input xxx and target yyy. |
| [`nn.CrossEntropyLoss`](generated/torch.nn.CrossEntropyLoss.html#torch.nn.CrossEntropyLoss) | This criterion computes the cross entropy loss between input logits and target. |
| [`nn.CTCLoss`](generated/torch.nn.CTCLoss.html#torch.nn.CTCLoss) | The Connectionist Temporal Classification loss. |
| [`nn.NLLLoss`](generated/torch.nn.NLLLoss.html#torch.nn.NLLLoss) | The negative log likelihood loss. |
| [`nn.PoissonNLLLoss`](generated/torch.nn.PoissonNLLLoss.html#torch.nn.PoissonNLLLoss) | Negative log likelihood loss with Poisson distribution of target. |
| [`nn.GaussianNLLLoss`](generated/torch.nn.GaussianNLLLoss.html#torch.nn.GaussianNLLLoss) | Gaussian negative log likelihood loss. |
| [`nn.KLDivLoss`](generated/torch.nn.KLDivLoss.html#torch.nn.KLDivLoss) | The Kullback-Leibler divergence loss. |
| [`nn.BCELoss`](generated/torch.nn.BCELoss.html#torch.nn.BCELoss) | Creates a criterion that measures the Binary Cross Entropy between the target and the input probabilities: |
| [`nn.BCEWithLogitsLoss`](generated/torch.nn.BCEWithLogitsLoss.html#torch.nn.BCEWithLogitsLoss) | This loss combines a Sigmoid layer and the BCELoss in one single class. |
| [`nn.MarginRankingLoss`](generated/torch.nn.MarginRankingLoss.html#torch.nn.MarginRankingLoss) | Creates a criterion that measures the loss given inputs x1x1x1, x2x2x2, two 1D mini-batch or 0D Tensors, and a label 1D mini-batch or 0D Tensor yyy (containing 1 or -1). |
| [`nn.HingeEmbeddingLoss`](generated/torch.nn.HingeEmbeddingLoss.html#torch.nn.HingeEmbeddingLoss) | Measures the loss given an input tensor xxx and a labels tensor yyy (containing 1 or -1). |
| [`nn.MultiLabelMarginLoss`](generated/torch.nn.MultiLabelMarginLoss.html#torch.nn.MultiLabelMarginLoss) | Creates a criterion that optimizes a multi-class multi-classification hinge loss (margin-based loss) between input xxx (a 2D mini-batch Tensor) and output yyy (which is a 2D Tensor of target class indices). |
| [`nn.HuberLoss`](generated/torch.nn.HuberLoss.html#torch.nn.HuberLoss) | Creates a criterion that uses a squared term if the absolute element-wise error falls below delta and a delta-scaled L1 term otherwise. |
| [`nn.SmoothL1Loss`](generated/torch.nn.SmoothL1Loss.html#torch.nn.SmoothL1Loss) | Creates a criterion that uses a squared term if the absolute element-wise error falls below beta and an L1 term otherwise. |
| [`nn.SoftMarginLoss`](generated/torch.nn.SoftMarginLoss.html#torch.nn.SoftMarginLoss) | Creates a criterion that optimizes a two-class classification logistic loss between input tensor xxx and target tensor yyy (containing 1 or -1). |
| [`nn.MultiLabelSoftMarginLoss`](generated/torch.nn.MultiLabelSoftMarginLoss.html#torch.nn.MultiLabelSoftMarginLoss) | Creates a criterion that optimizes a multi-label one-versus-all loss based on max-entropy, between input xxx and target yyy of size (N,C)(N, C)(N,C). |
| [`nn.CosineEmbeddingLoss`](generated/torch.nn.CosineEmbeddingLoss.html#torch.nn.CosineEmbeddingLoss) | Creates a criterion that measures the loss given input tensors x1x_1x1​, x2x_2x2​ and a Tensor label yyy with values 1 or -1. |
| [`nn.MultiMarginLoss`](generated/torch.nn.MultiMarginLoss.html#torch.nn.MultiMarginLoss) | Creates a criterion that optimizes a multi-class classification hinge loss (margin-based loss) between input xxx (a 2D mini-batch Tensor) and output yyy (which is a 1D tensor of target class indices, 0≤y≤x.size(1)−10 \leq y \leq \text{x.size}(1)-10≤y≤x.size(1)−1): |
| [`nn.TripletMarginLoss`](generated/torch.nn.TripletMarginLoss.html#torch.nn.TripletMarginLoss) | Creates a criterion that measures the triplet loss given an input tensors x1x1x1, x2x2x2, x3x3x3 and a margin with a value greater than 000. |
| [`nn.TripletMarginWithDistanceLoss`](generated/torch.nn.TripletMarginWithDistanceLoss.html#torch.nn.TripletMarginWithDistanceLoss) | Creates a criterion that measures the triplet loss given input tensors aaa, ppp, and nnn (representing anchor, positive, and negative examples, respectively), and a nonnegative, real-valued function ("distance function") used to compute the relationship between the anchor and positive example ("positive distance") and the anchor and negative example ("negative distance"). |

## Vision Layers

| [`nn.PixelShuffle`](generated/torch.nn.PixelShuffle.html#torch.nn.PixelShuffle) | Rearrange elements in a tensor according to an upscaling factor. |
| --- | --- |
| [`nn.PixelUnshuffle`](generated/torch.nn.PixelUnshuffle.html#torch.nn.PixelUnshuffle) | Reverse the PixelShuffle operation. |
| [`nn.Upsample`](generated/torch.nn.Upsample.html#torch.nn.Upsample) | Upsamples a given multi-channel 1D (temporal), 2D (spatial) or 3D (volumetric) data. |
| [`nn.UpsamplingNearest2d`](generated/torch.nn.UpsamplingNearest2d.html#torch.nn.UpsamplingNearest2d) | Applies a 2D nearest neighbor upsampling to an input signal composed of several input channels. |
| [`nn.UpsamplingBilinear2d`](generated/torch.nn.UpsamplingBilinear2d.html#torch.nn.UpsamplingBilinear2d) | Applies a 2D bilinear upsampling to an input signal composed of several input channels. |

## Shuffle Layers

| [`nn.ChannelShuffle`](generated/torch.nn.ChannelShuffle.html#torch.nn.ChannelShuffle) | Divides and rearranges the channels in a tensor. |
| --- | --- |

## DataParallel Layers (multi-GPU, distributed)

| [`nn.DataParallel`](generated/torch.nn.DataParallel.html#torch.nn.DataParallel) | Implements data parallelism at the module level. |
| --- | --- |
| [`nn.parallel.DistributedDataParallel`](generated/torch.nn.parallel.DistributedDataParallel.html#torch.nn.parallel.DistributedDataParallel) | Implement distributed data parallelism based on `torch.distributed` at module level. |

## Utilities

From the `torch.nn.utils` module:

Utility functions to clip parameter gradients.

| [`clip_grad_norm_`](generated/torch.nn.utils.clip_grad_norm_.html#torch.nn.utils.clip_grad_norm_) | Clip the gradient norm of an iterable of parameters. |
| --- | --- |
| [`clip_grad_norm`](generated/torch.nn.utils.clip_grad_norm.html#torch.nn.utils.clip_grad_norm) | Clip the gradient norm of an iterable of parameters. |
| [`clip_grad_value_`](generated/torch.nn.utils.clip_grad_value_.html#torch.nn.utils.clip_grad_value_) | Clip the gradients of an iterable of parameters at specified value. |
| [`get_total_norm`](generated/torch.nn.utils.get_total_norm.html#torch.nn.utils.get_total_norm) | Compute the norm of an iterable of tensors. |
| [`clip_grads_with_norm_`](generated/torch.nn.utils.clip_grads_with_norm_.html#torch.nn.utils.clip_grads_with_norm_) | Scale the gradients of an iterable of parameters given a pre-calculated total norm and desired max norm. |

Utility functions to flatten and unflatten Module parameters to and from a single vector.

| [`parameters_to_vector`](generated/torch.nn.utils.parameters_to_vector.html#torch.nn.utils.parameters_to_vector) | Flatten an iterable of parameters into a single vector. |
| --- | --- |
| [`vector_to_parameters`](generated/torch.nn.utils.vector_to_parameters.html#torch.nn.utils.vector_to_parameters) | Copy slices of a vector into an iterable of parameters. |

Utility functions to fuse Modules with BatchNorm modules.

| [`fuse_conv_bn_eval`](generated/torch.nn.utils.fuse_conv_bn_eval.html#torch.nn.utils.fuse_conv_bn_eval) | Fuse a convolutional module and a BatchNorm module into a single, new convolutional module. |
| --- | --- |
| [`fuse_conv_bn_weights`](generated/torch.nn.utils.fuse_conv_bn_weights.html#torch.nn.utils.fuse_conv_bn_weights) | Fuse convolutional module parameters and BatchNorm module parameters into new convolutional module parameters. |
| [`fuse_linear_bn_eval`](generated/torch.nn.utils.fuse_linear_bn_eval.html#torch.nn.utils.fuse_linear_bn_eval) | Fuse a linear module and a BatchNorm module into a single, new linear module. |
| [`fuse_linear_bn_weights`](generated/torch.nn.utils.fuse_linear_bn_weights.html#torch.nn.utils.fuse_linear_bn_weights) | Fuse linear module parameters and BatchNorm module parameters into new linear module parameters. |

Utility functions to convert Module parameter memory formats.

| [`convert_conv2d_weight_memory_format`](generated/torch.nn.utils.convert_conv2d_weight_memory_format.html#torch.nn.utils.convert_conv2d_weight_memory_format) | Convert `memory_format` of `nn.Conv2d.weight` to `memory_format`. |
| --- | --- |
| [`convert_conv3d_weight_memory_format`](generated/torch.nn.utils.convert_conv3d_weight_memory_format.html#torch.nn.utils.convert_conv3d_weight_memory_format) | Convert `memory_format` of `nn.Conv3d.weight` to `memory_format` The conversion recursively applies to nested `nn.Module`, including `module`. |

Utility functions to apply and remove weight normalization from Module parameters.

| [`weight_norm`](generated/torch.nn.utils.weight_norm.html#torch.nn.utils.weight_norm) | Apply weight normalization to a parameter in the given module. |
| --- | --- |
| [`remove_weight_norm`](generated/torch.nn.utils.remove_weight_norm.html#torch.nn.utils.remove_weight_norm) | Remove the weight normalization reparameterization from a module. |
| [`spectral_norm`](generated/torch.nn.utils.spectral_norm.html#torch.nn.utils.spectral_norm) | Apply spectral normalization to a parameter in the given module. |
| [`remove_spectral_norm`](generated/torch.nn.utils.remove_spectral_norm.html#torch.nn.utils.remove_spectral_norm) | Remove the spectral normalization reparameterization from a module. |

Utility functions for initializing Module parameters.

| [`skip_init`](generated/torch.nn.utils.skip_init.html#torch.nn.utils.skip_init) | Given a module class object and args / kwargs, instantiate the module without initializing parameters / buffers. |
| --- | --- |

Utility classes and functions for pruning Module parameters.

| [`prune.BasePruningMethod`](generated/torch.nn.utils.prune.BasePruningMethod.html#torch.nn.utils.prune.BasePruningMethod) | Abstract base class for creation of new pruning techniques. |
| --- | --- |
| [`prune.PruningContainer`](generated/torch.nn.utils.prune.PruningContainer.html#torch.nn.utils.prune.PruningContainer) | Container holding a sequence of pruning methods for iterative pruning. |
| [`prune.Identity`](generated/torch.nn.utils.prune.Identity_class.html#torch.nn.utils.prune.Identity) | Utility pruning method that does not prune any units but generates the pruning parametrization with a mask of ones. |
| [`prune.RandomUnstructured`](generated/torch.nn.utils.prune.RandomUnstructured.html#torch.nn.utils.prune.RandomUnstructured) | Prune (currently unpruned) units in a tensor at random. |
| [`prune.L1Unstructured`](generated/torch.nn.utils.prune.L1Unstructured.html#torch.nn.utils.prune.L1Unstructured) | Prune (currently unpruned) units in a tensor by zeroing out the ones with the lowest L1-norm. |
| [`prune.RandomStructured`](generated/torch.nn.utils.prune.RandomStructured.html#torch.nn.utils.prune.RandomStructured) | Prune entire (currently unpruned) channels in a tensor at random. |
| [`prune.LnStructured`](generated/torch.nn.utils.prune.LnStructured.html#torch.nn.utils.prune.LnStructured) | Prune entire (currently unpruned) channels in a tensor based on their L`n`-norm. |
| [`prune.CustomFromMask`](generated/torch.nn.utils.prune.CustomFromMask.html#torch.nn.utils.prune.CustomFromMask) | |
| [`prune.identity`](generated/torch.nn.utils.prune.identity_function.html#torch.nn.utils.prune.identity) | Apply pruning reparameterization without pruning any units. |
| [`prune.random_unstructured`](generated/torch.nn.utils.prune.random_unstructured.html#torch.nn.utils.prune.random_unstructured) | Prune tensor by removing random (currently unpruned) units. |
| [`prune.l1_unstructured`](generated/torch.nn.utils.prune.l1_unstructured.html#torch.nn.utils.prune.l1_unstructured) | Prune tensor by removing units with the lowest L1-norm. |
| [`prune.random_structured`](generated/torch.nn.utils.prune.random_structured.html#torch.nn.utils.prune.random_structured) | Prune tensor by removing random channels along the specified dimension. |
| [`prune.ln_structured`](generated/torch.nn.utils.prune.ln_structured.html#torch.nn.utils.prune.ln_structured) | Prune tensor by removing channels with the lowest L`n`-norm along the specified dimension. |
| [`prune.global_unstructured`](generated/torch.nn.utils.prune.global_unstructured.html#torch.nn.utils.prune.global_unstructured) | Globally prunes tensors corresponding to all parameters in `parameters` by applying the specified `pruning_method`. |
| [`prune.custom_from_mask`](generated/torch.nn.utils.prune.custom_from_mask.html#torch.nn.utils.prune.custom_from_mask) | Prune tensor corresponding to parameter called `name` in `module` by applying the pre-computed mask in `mask`. |
| [`prune.remove`](generated/torch.nn.utils.prune.remove.html#torch.nn.utils.prune.remove) | Remove the pruning reparameterization from a module and the pruning method from the forward hook. |
| [`prune.is_pruned`](generated/torch.nn.utils.prune.is_pruned.html#torch.nn.utils.prune.is_pruned) | Check if a module is pruned by looking for pruning pre-hooks. |

Parametrizations implemented using the new parametrization functionality
in `torch.nn.utils.parameterize.register_parametrization()`.

| [`parametrizations.orthogonal`](generated/torch.nn.utils.parametrizations.orthogonal.html#torch.nn.utils.parametrizations.orthogonal) | Apply an orthogonal or unitary parametrization to a matrix or a batch of matrices. |
| --- | --- |
| [`parametrizations.weight_norm`](generated/torch.nn.utils.parametrizations.weight_norm.html#torch.nn.utils.parametrizations.weight_norm) | Apply weight normalization to a parameter in the given module. |
| [`parametrizations.spectral_norm`](generated/torch.nn.utils.parametrizations.spectral_norm.html#torch.nn.utils.parametrizations.spectral_norm) | Apply spectral normalization to a parameter in the given module. |

Utility functions to parametrize Tensors on existing Modules.
Note that these functions can be used to parametrize a given Parameter
or Buffer given a specific function that maps from an input space to the
parametrized space. They are not parameterizations that would transform
an object into a parameter. See the
[Parametrizations tutorial](https://pytorch.org/tutorials/intermediate/parametrizations.html)
for more information on how to implement your own parametrizations.

| [`parametrize.register_parametrization`](generated/torch.nn.utils.parametrize.register_parametrization.html#torch.nn.utils.parametrize.register_parametrization) | Register a parametrization to a tensor in a module. |
| --- | --- |
| [`parametrize.remove_parametrizations`](generated/torch.nn.utils.parametrize.remove_parametrizations.html#torch.nn.utils.parametrize.remove_parametrizations) | Remove the parametrizations on a tensor in a module. |
| [`parametrize.cached`](generated/torch.nn.utils.parametrize.cached.html#torch.nn.utils.parametrize.cached) | Context manager that enables the caching system within parametrizations registered with `register_parametrization()`. |
| [`parametrize.is_parametrized`](generated/torch.nn.utils.parametrize.is_parametrized.html#torch.nn.utils.parametrize.is_parametrized) | Determine if a module has a parametrization. |
| [`parametrize.transfer_parametrizations_and_params`](generated/torch.nn.utils.parametrize.transfer_parametrizations_and_params.html#torch.nn.utils.parametrize.transfer_parametrizations_and_params) | Transfer parametrizations and the parameters they parametrize from `from_module` to `to_module`. |
| [`parametrize.type_before_parametrizations`](generated/torch.nn.utils.parametrize.type_before_parametrizations.html#torch.nn.utils.parametrize.type_before_parametrizations) | Return the module type before parametrizations were applied and if not, then it returns the module type. |

| [`parametrize.ParametrizationList`](generated/torch.nn.utils.parametrize.ParametrizationList.html#torch.nn.utils.parametrize.ParametrizationList) | A sequential container that holds and manages the original parameters or buffers of a parametrized [`torch.nn.Module`](generated/torch.nn.Module.html#torch.nn.Module). |
| --- | --- |

Utility functions to call a given Module in a stateless manner.

| [`stateless.functional_call`](generated/torch.nn.utils.stateless.functional_call.html#torch.nn.utils.stateless.functional_call) | Perform a functional call on the module by replacing the module parameters and buffers with the provided ones. |
| --- | --- |

Utility functions in other modules

| [`nn.utils.rnn.PackedSequence`](generated/torch.nn.utils.rnn.PackedSequence.html#torch.nn.utils.rnn.PackedSequence) | Holds the data and list of `batch_sizes` of a packed sequence. |
| --- | --- |
| [`nn.utils.rnn.pack_padded_sequence`](generated/torch.nn.utils.rnn.pack_padded_sequence.html#torch.nn.utils.rnn.pack_padded_sequence) | Packs a Tensor containing padded sequences of variable length. |
| [`nn.utils.rnn.pad_packed_sequence`](generated/torch.nn.utils.rnn.pad_packed_sequence.html#torch.nn.utils.rnn.pad_packed_sequence) | Pad a packed batch of variable length sequences. |
| [`nn.utils.rnn.pad_sequence`](generated/torch.nn.utils.rnn.pad_sequence.html#torch.nn.utils.rnn.pad_sequence) | Pad a list of variable length Tensors with `padding_value`. |
| [`nn.utils.rnn.pack_sequence`](generated/torch.nn.utils.rnn.pack_sequence.html#torch.nn.utils.rnn.pack_sequence) | Packs a list of variable length Tensors. |
| [`nn.utils.rnn.unpack_sequence`](generated/torch.nn.utils.rnn.unpack_sequence.html#torch.nn.utils.rnn.unpack_sequence) | Unpack PackedSequence into a list of variable length Tensors. |
| [`nn.utils.rnn.unpad_sequence`](generated/torch.nn.utils.rnn.unpad_sequence.html#torch.nn.utils.rnn.unpad_sequence) | Unpad padded Tensor into a list of variable length Tensors. |
| [`nn.utils.rnn.invert_permutation`](generated/torch.nn.utils.rnn.invert_permutation.html#torch.nn.utils.rnn.invert_permutation) | Returns the inverse of `permutation`. |
| [`nn.parameter.is_lazy`](generated/torch.nn.parameter.is_lazy.html#torch.nn.parameter.is_lazy) | Returns whether `param` is an `UninitializedParameter` or `UninitializedBuffer`. |
| [`nn.factory_kwargs`](generated/torch.nn.factory_kwargs.html#torch.nn.factory_kwargs) | Return a canonicalized dict of factory kwargs. |

| [`nn.modules.flatten.Flatten`](generated/torch.nn.modules.flatten.Flatten.html#torch.nn.modules.flatten.Flatten) | Flattens a contiguous range of dims into a tensor. |
| --- | --- |
| [`nn.modules.flatten.Unflatten`](generated/torch.nn.modules.flatten.Unflatten.html#torch.nn.modules.flatten.Unflatten) | Unflattens a tensor dim expanding it to a desired shape. |

## Quantized Functions

Quantization refers to techniques for performing computations and storing tensors at lower bitwidths than
floating point precision. PyTorch supports both per tensor and per channel asymmetric linear quantization. To learn more how to use quantized functions in PyTorch, please refer to the [Quantization](quantization.html#quantization-doc) documentation.

## Lazy Modules Initialization

| [`nn.modules.lazy.LazyModuleMixin`](generated/torch.nn.modules.lazy.LazyModuleMixin.html#torch.nn.modules.lazy.LazyModuleMixin) | A mixin for modules that lazily initialize parameters, also known as "lazy modules". |
| --- | --- |