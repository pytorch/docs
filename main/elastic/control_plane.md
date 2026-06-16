# Control Plane

This module contains optional helpers that add extra debug and control handlers
into your application.

torch.distributed.elastic.control_plane.worker_main()[[source]](https://github.com/pytorch/pytorch/blob/053a82e9f95b79ebe852f2372f1452e4c8537230/torch/distributed/elastic/control_plane.py#L26)

This is a context manager that wraps your main entry function. This combines
the existing `errors.record` logic as well as a new `_WorkerServer` that
exposes handlers via a unix socket specified by
`TORCH_WORKER_SERVER_SOCKET`.

Example

```
@worker_main()
def main():
 pass

if __name__ == "__main__":
 main()
```

Return type:

[*Generator*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator)[None, None, None]