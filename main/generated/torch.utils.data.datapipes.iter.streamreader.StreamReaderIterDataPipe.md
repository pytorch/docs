# StreamReaderIterDataPipe

*class*torch.utils.data.datapipes.iter.streamreader.StreamReaderIterDataPipe(*datapipe*, *chunk=None*)[[source]](https://github.com/pytorch/pytorch/blob/a533e5c93d4fb8c4eb7bd23c7d297cbba493caa1/torch/utils/data/datapipes/iter/streamreader.py#L11)

Given IO streams and their label names, yield bytes with label name as tuple.

(functional name: `read_from_stream`).

Parameters:

- **datapipe** (*IterDataPipe**[*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*IOBase*](https://docs.python.org/3/library/io.html#io.IOBase)*]**]*) - Iterable DataPipe provides label/URL and byte stream
- **chunk** ([*int*](https://docs.python.org/3/library/functions.html#int)*|**None*) - Number of bytes to be read from stream per iteration.
If `None`, all bytes will be read until the EOF.

Example

```
>>> from torchdata.datapipes.iter import IterableWrapper, StreamReader
>>> from io import StringIO
>>> dp = IterableWrapper([("alphabet", StringIO("abcde"))])
>>> list(StreamReader(dp, chunk=1))
[('alphabet', 'a'), ('alphabet', 'b'), ('alphabet', 'c'), ('alphabet', 'd'), ('alphabet', 'e')]
```

reset()[[source]](https://github.com/pytorch/pytorch/blob/a533e5c93d4fb8c4eb7bd23c7d297cbba493caa1/torch/utils/data/datapipes/datapipe.py#L233)

Reset the IterDataPipe to the initial state.

By default, no-op. For subclasses of IterDataPipe, depending on their functionalities,
they may want to override this method with implementations that
may clear the buffers and reset pointers of the DataPipe.
The reset method is always called when __iter__ is called as part of hook_iterator.