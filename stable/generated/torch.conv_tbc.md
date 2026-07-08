# torch.conv_tbc

torch.conv_tbc()

Applies a 1-dimensional sequence convolution over an input sequence.
Input and output dimensions are (Time, Batch, Channels) - hence TBC.

Parameters:

- **input** - input tensor of shape (sequence length×batch×in_channels)(\text{sequence length} \times batch \times \text{in\_channels})(sequence length×batch×in_channels)
- **weight** - filter of shape (kernel width×in_channels×out_channels\text{kernel width} \times \text{in\_channels} \times \text{out\_channels}kernel width×in_channels×out_channels)
- **bias** - bias of shape (out_channels\text{out\_channels}out_channels)
- **pad** - number of timesteps to pad. Default: 0