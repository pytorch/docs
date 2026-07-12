# torch.monitor

Warning

This module is a prototype release, and its interfaces and functionality may
change without warning in future PyTorch releases.

`torch.monitor` provides an interface for logging events and counters from
PyTorch.

The stat interfaces are designed to be used for tracking high level metrics that
are periodically logged out to be used for monitoring system performance. Since
the stats aggregate with a specific window size you can log to them from
critical loops with minimal performance impact.

For more infrequent events or values such as loss, accuracy, usage tracking the
event interface can be directly used.

Event handlers can be registered to handle the events and pass them to an
external event sink.

## API Reference

*class*torch.monitor.Aggregation

> These are types of aggregations that can be used to accumulate stats.

Members:

> VALUE :
> 
> VALUE returns the last value to be added.
> 
> 
> 
> MEAN :
> 
> MEAN computes the arithmetic mean of all the added values.
> 
> 
> 
> COUNT :
> 
> COUNT returns the total number of added values.
> 
> 
> 
> SUM :
> 
> SUM returns the sum of the added values.
> 
> 
> 
> MAX :
> 
> MAX returns the max of the added values.
> 
> 
> 
> MIN :
> 
> MIN returns the min of the added values.

*property*name

*class*torch.monitor.Stat

Stat is used to compute summary statistics in a performant way over
fixed intervals. Stat logs the statistics as an Event once every
`window_size` duration. When the window closes the stats are logged
via the event handlers as a `torch.monitor.Stat` event.

`window_size` should be set to something relatively high to avoid a
huge number of events being logged. Ex: 60s. Stat uses millisecond
precision.

If `max_samples` is set, the stat will cap the number of samples per
window by discarding add calls once `max_samples` adds have
occurred. If it's not set, all `add` calls during the window will be
included. This is an optional field to make aggregations more directly
comparable across windows when the number of samples might vary.

When the Stat is destructed it will log any remaining data even if the
window hasn't elapsed.

__init__(*self: torch._C._monitor.Stat*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str)*, *aggregations: [collections.abc.Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[torch._C._monitor.Aggregation]*, *window_size: [datetime.timedelta](https://docs.python.org/3/library/datetime.html#datetime.timedelta)*, *max_samples: [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt) | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex) = 9223372036854775807*) → [None](https://docs.python.org/3/library/constants.html#None)

Constructs the `Stat`.

add(*self: torch._C._monitor.Stat*, *v: [SupportsFloat](https://docs.python.org/3/library/typing.html#typing.SupportsFloat) | [SupportsIndex](https://docs.python.org/3/library/typing.html#typing.SupportsIndex)*) → [None](https://docs.python.org/3/library/constants.html#None)

Adds a value to the stat to be aggregated according to the
configured stat type and aggregations.

*property*count

Number of data points that have currently been collected. Resets
once the event has been logged.

get(*self: torch._C._monitor.Stat*) → [dict](https://docs.python.org/3/library/stdtypes.html#dict)[torch._C._monitor.Aggregation, [float](https://docs.python.org/3/library/functions.html#float)]

Returns the current value of the stat, primarily for testing
purposes. If the stat has logged and no additional values have been
added this will be zero.

*property*name

The name of the stat that was set during creation.

*class*torch.monitor.data_value_t

data_value_t is one of `str`, `float`, `int`, `bool`.

*class*torch.monitor.Event

Event represents a specific typed event to be logged. This can represent
high-level data points such as loss or accuracy per epoch or more
low-level aggregations such as through the Stats provided through this
library.

All Events of the same type should have the same name so downstream
handlers can correctly process them.

__init__(*self: torch._C._monitor.Event*, *name: [str](https://docs.python.org/3/library/stdtypes.html#str)*, *timestamp: [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime)*, *data: [collections.abc.Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), data_value_t]*) → [None](https://docs.python.org/3/library/constants.html#None)

Constructs the `Event`.

*property*data

The structured data contained within the `Event`.

*property*name

The name of the `Event`.

*property*timestamp

The timestamp when the `Event` happened.

*class*torch.monitor.EventHandlerHandle

EventHandlerHandle is a wrapper type returned by
`register_event_handler` used to unregister the handler via
`unregister_event_handler`. This cannot be directly initialized.

torch.monitor.log_event(*event: torch._C._monitor.Event*) → [None](https://docs.python.org/3/library/constants.html#None)

log_event logs the specified event to all of the registered event
handlers. It's up to the event handlers to log the event out to the
corresponding event sink.

If there are no event handlers registered this method is a no-op.

torch.monitor.register_event_handler(*callback: [collections.abc.Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[torch._C._monitor.Event], [None](https://docs.python.org/3/library/constants.html#None)]*) → torch._C._monitor.EventHandlerHandle

register_event_handler registers a callback to be called whenever an
event is logged via `log_event`. These handlers should avoid blocking
the main thread since that may interfere with training as they run
during the `log_event` call.

torch.monitor.unregister_event_handler(*handler: torch._C._monitor.EventHandlerHandle*) → [None](https://docs.python.org/3/library/constants.html#None)

unregister_event_handler unregisters the `EventHandlerHandle` returned
after calling `register_event_handler`. After this returns the event
handler will no longer receive events.

*class*torch.monitor.TensorboardEventHandler(*writer*)[[source]](https://github.com/pytorch/pytorch/blob/dea5f568512cef2ab009ee7858b1cfd9be8ba924/torch/monitor/__init__.py#L13)

TensorboardEventHandler is an event handler that will write known events to
the provided SummaryWriter.

This currently only supports `torch.monitor.Stat` events which are logged
as scalars.

Example

```
>>> from torch.utils.tensorboard import SummaryWriter
>>> from torch.monitor import TensorboardEventHandler, register_event_handler
>>> writer = SummaryWriter("log_dir")
>>> register_event_handler(TensorboardEventHandler(writer))
```

__init__(*writer*)[[source]](https://github.com/pytorch/pytorch/blob/dea5f568512cef2ab009ee7858b1cfd9be8ba924/torch/monitor/__init__.py#L30)

Constructs the `TensorboardEventHandler`.