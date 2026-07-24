# Control Plane

This module contains optional helpers that add extra debug and control handlers
into your application.

torch.distributed.elastic.control_plane.worker_main()[[source]](https://github.com/pytorch/pytorch/blob/d1e2802e366c287c4773a50f4f0e8c35e8647bbb/torch/distributed/elastic/control_plane.py#L26)

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