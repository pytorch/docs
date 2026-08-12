# Multiprocessing

Library that launches and manages `n` copies of worker subprocesses either specified by a function or a binary.

For functions, it uses `torch.multiprocessing` (and therefore python
`multiprocessing`) to spawn/fork worker processes. For binaries it uses python
`subprocessing.Popen` to create worker processes.

Usage 1: Launching two trainers as a function

```
from torch.distributed.elastic.multiprocessing import Std, start_processes

def trainer(a, b, c):
 pass # train

# runs two trainers
# LOCAL_RANK=0 trainer(1,2,3)
# LOCAL_RANK=1 trainer(4,5,6)
ctx = start_processes(
 name="trainer",
 entrypoint=trainer,
 args={0: (1, 2, 3), 1: (4, 5, 6)},
 envs={0: {"LOCAL_RANK": 0}, 1: {"LOCAL_RANK": 1}},
 log_dir="/tmp/foobar",
 redirects=Std.ALL, # write all worker stdout/stderr to a log file
 tee={0: Std.ERR}, # tee only local rank 0's stderr to console
)

# waits for all copies of trainer to finish
ctx.wait()
```

Usage 2: Launching 2 echo workers as a binary

```
# same as invoking
# echo hello
# echo world > stdout.log
ctx = start_processes(
 name="echo"
 entrypoint="echo",
 log_dir="/tmp/foobar",
 args={0: "hello", 1: "world"},
 redirects={1: Std.OUT},
 )
```

Just like `torch.multiprocessing`, the return value of the function
`start_processes()` is a process context (`api.PContext`). If a function
was launched, a `api.MultiprocessContext` is returned and if a binary
was launched a `api.SubprocessContext` is returned. Both are specific
implementations of the parent `api.PContext` class.

## Starting Multiple Workers

torch.distributed.elastic.multiprocessing.start_processes(*name*, *entrypoint*, *args*, *envs*, *logs_specs*, *log_line_prefixes=None*, *start_method='spawn'*, *numa_options=None*, *duplicate_stdout_filters=None*, *duplicate_stderr_filters=None*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/distributed/elastic/multiprocessing/__init__.py#L103)

Start `n` copies of `entrypoint` processes with the provided options.

`entrypoint` is either a `Callable` (function) or a `str` (binary).
The number of copies is determined by the number of entries for `args` and
`envs` arguments, which need to have the same key set.

`args` and `env` parameters are the arguments and environment variables
to pass down to the entrypoint mapped by the replica index (local rank).
All local ranks must be accounted for.
That is, the keyset should be `{0,1,...,(nprocs-1)}`.

Note

When the `entrypoint` is a binary (`str`), `args` can only be strings.
If any other type is given, then it is casted to a string representation
(e.g. `str(arg1)`). Furthermore, a binary failure will only write
an `error.json` error file if the main function is annotated with
`torch.distributed.elastic.multiprocessing.errors.record`. For function launches,
this is done by default and there is no need to manually annotate
with the `@record` annotation.

Inside `logs_specs`, `redirects` and `tee` are bitmasks specifying which std
stream(s) to redirect to a log file in the `log_dir`. Valid mask values are defined
in `Std`. To redirect/tee only certain local ranks, pass `redirects` as a map
with the key as the local rank to specify the redirect behavior for.
Any missing local ranks will default to `Std.NONE`.

`duplicate_stdout_filters` and `duplicate_stderr_filters`, if non-empty,
duplicate stdouts and stderrs respectively specified in `logs_specs`'s `tee`
to a file containing only lines that match _any_ of the filter strings. The log
file is aggregated across all ranks selected by `tee`.

`tee` acts like the unix "tee" command in that it redirects + prints to console.
To avoid worker stdout/stderr from printing to console, use the `redirects` parameter.

For each process, the `log_dir` will contain:

1. `{local_rank}/error.json`: if the process failed, a file with the error info
2. `{local_rank}/stdout.log`: if `redirect & STDOUT == STDOUT`
3. `{local_rank}/stderr.log`: if `redirect & STDERR == STDERR`
4. `filtered_stdout.log`: if `duplicate_stdout_filters` is non-empty
5. `filtered_stderr.log`: if `duplicate_stderr_filters` is non-empty

Note

It is expected that the `log_dir` exists, is empty, and is a directory.

Example:

```
log_dir = "/tmp/test"

# ok; two copies of foo: foo("bar0"), foo("bar1")
start_processes(
 name="trainer",
 entrypoint=foo,
 args:{0:("bar0",), 1:("bar1",),
 envs:{0:{}, 1:{}},
 log_dir=log_dir
)

# invalid; envs missing for local rank 1
start_processes(
 name="trainer",
 entrypoint=foo,
 args:{0:("bar0",), 1:("bar1",),
 envs:{0:{}},
 log_dir=log_dir
)

# ok; two copies of /usr/bin/touch: touch file1, touch file2
start_processes(
 name="trainer",
 entrypoint="/usr/bin/touch",
 args:{0:("file1",), 1:("file2",),
 envs:{0:{}, 1:{}},
 log_dir=log_dir
 )

# caution; arguments casted to string, runs:
# echo "1" "2" "3" and echo "[1, 2, 3]"
start_processes(
 name="trainer",
 entrypoint="/usr/bin/echo",
 args:{0:(1,2,3), 1:([1,2,3],),
 envs:{0:{}, 1:{}},
 log_dir=log_dir
 )
```

Parameters:

- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - a human readable short name that describes what the processes are
(used as header when tee'ing stdout/stderr outputs)
- **entrypoint** ([*Callable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)*|*[*str*](https://docs.python.org/3/library/stdtypes.html#str)) - either a `Callable` (function) or `cmd` (binary)
- **args** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple)*]*) - arguments to each replica
- **envs** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,*[*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**]*) - env vars to each replica
- **log_dir** - directory used to write log files
- **start_method** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - multiprocessing start method (spawn, fork, forkserver)
ignored for binaries
- **logs_specs** (*LogsSpecs*) - defines `log_dir`, `redirects`, and `tee`.
inside `logs_specs`:
- redirects: which std streams to redirect to a log file
- tee: which std streams to redirect + print to console
- **local_ranks_filter** - which ranks' logs to print to console
- **duplicate_stdout_filters** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**|**None*) - filters for the duplicated stdout logs
- **duplicate_stderr_filters** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**|**None*) - filters for the duplicated stderr logs

Return type:

*PContext*

## Process Context

*class*torch.distributed.elastic.multiprocessing.api.PContext(*name*, *entrypoint*, *args*, *envs*, *logs_specs*, *log_line_prefixes=None*, *duplicate_stdout_filters=None*, *duplicate_stderr_filters=None*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/distributed/elastic/multiprocessing/api.py#L444)

The base class that standardizes operations over a set of processes that are launched via different mechanisms.

The name `PContext` is intentional to disambiguate with `torch.multiprocessing.ProcessContext`.

Warning

stdouts and stderrs should ALWAYS be a superset of
tee_stdouts and tee_stderrs (respectively) this is b/c
tee is implemented as a redirect + tail -f <stdout/stderr.log>

Parameters:

- **duplicate_stdout_filters** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**|**None*) - If non-empty, duplicates stdouts specified in `logs_specs`'s `tee`
to a file containing only lines that match _any_ of the filter strings.
The log file is aggregated across all ranks selected by `tee`.
- **duplicate_stderr_filters** ([*list*](https://docs.python.org/3/library/stdtypes.html#list)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**|**None*) - If non-empty, duplicates stderrs specified in `logs_specs`'s `tee`
to a file containing only lines that match _any_ of the filter strings.
The log file is aggregated across all ranks selected by `tee`.

*class*torch.distributed.elastic.multiprocessing.api.MultiprocessContext(*name*, *entrypoint*, *args*, *envs*, *start_method*, *logs_specs*, *log_line_prefixes=None*, *numa_options=None*, *duplicate_stdout_filters=None*, *duplicate_stderr_filters=None*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/distributed/elastic/multiprocessing/api.py#L711)

`PContext` holding worker processes invoked as a function.

*class*torch.distributed.elastic.multiprocessing.api.SubprocessContext(*name*, *entrypoint*, *args*, *envs*, *logs_specs*, *log_line_prefixes=None*, *numa_options=None*, *duplicate_stdout_filters=None*, *duplicate_stderr_filters=None*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/distributed/elastic/multiprocessing/api.py#L917)

`PContext` holding worker processes invoked as a binary.

*class*torch.distributed.elastic.multiprocessing.api.RunProcsResult(*return_values=<factory>*, *failures=<factory>*, *stdouts=<factory>*, *stderrs=<factory>*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/distributed/elastic/multiprocessing/api.py#L421)

Results of a completed run of processes started with `start_processes()`. Returned by `PContext`.

Note the following:

1. All fields are mapped by local rank
2. `return_values` - only populated for functions (not the binaries).
3. `stdouts` - path to stdout.log (empty string if no redirect)
4. `stderrs` - path to stderr.log (empty string if no redirect)

*class*torch.distributed.elastic.multiprocessing.api.DefaultLogsSpecs(*log_dir=None*, *redirects=Std.NONE*, *tee=Std.NONE*, *local_ranks_filter=None*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/distributed/elastic/multiprocessing/api.py#L245)

Default LogsSpecs implementation:

- log_dir will be created if it doesn't exist
- Generates nested folders for each attempt and rank.

reify(*envs*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/distributed/elastic/multiprocessing/api.py#L283)

Uses following scheme to build log destination paths:

- <log_dir>/<rdzv_run_id>/attempt_<attempt>/<rank>/stdout.log
- <log_dir>/<rdzv_run_id>/attempt_<attempt>/<rank>/stderr.log
- <log_dir>/<rdzv_run_id>/attempt_<attempt>/<rank>/error.json
- <log_dir>/<rdzv_run_id>/attempt_<attempt>/filtered_stdout.log
- <log_dir>/<rdzv_run_id>/attempt_<attempt>/filtered_stderr.log

Return type:

*LogsDest*

*class*torch.distributed.elastic.multiprocessing.api.LogsDest(*stdouts=<factory>*, *stderrs=<factory>*, *tee_stdouts=<factory>*, *tee_stderrs=<factory>*, *error_files=<factory>*, *filtered_stdout=<factory>*, *filtered_stderr=<factory>*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/distributed/elastic/multiprocessing/api.py#L183)

For each log type, holds mapping of local rank ids to file paths.

*class*torch.distributed.elastic.multiprocessing.api.LogsSpecs(*log_dir=None*, *redirects=Std.NONE*, *tee=Std.NONE*, *local_ranks_filter=None*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/distributed/elastic/multiprocessing/api.py#L198)

Defines logs processing and redirection for each worker process.

Parameters:

- **log_dir** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*|**None*) - Base directory where logs will be written.
- **redirects** (*Std**|*[*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,**Std**]*) - Streams to redirect to files. Pass a single `Std`
enum to redirect for all workers, or a mapping keyed
by local_rank to selectively redirect.
- **tee** (*Std**|*[*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*int*](https://docs.python.org/3/library/functions.html#int)*,**Std**]*) - Streams to duplicate to stdout/stderr.
Pass a single `Std` enum to duplicate streams for all workers,
or a mapping keyed by local_rank to selectively duplicate.

*abstract*reify(*envs*)[[source]](https://github.com/pytorch/pytorch/blob/5ad9b8adb58904fa51d72bb483f93b8514080068/torch/distributed/elastic/multiprocessing/api.py#L227)

Given the environment variables, builds destination of log files for each of the local ranks.

Envs parameter contains env variables dict for each of the local ranks, where entries are defined in:
`_start_workers()`.

Return type:

*LogsDest*