# Events

Module contains events processing mechanisms that are integrated with the standard python logging.

Example of usage:

```
from torch.distributed.elastic import events

event = events.Event(
 name="test_event", source=events.EventSource.WORKER, metadata={...}
)
events.get_logging_handler(destination="console").info(event)
```

## API Methods

torch.distributed.elastic.events.record(*event*, *destination='null'*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/distributed/elastic/events/__init__.py#L69)

torch.distributed.elastic.events.construct_and_record_rdzv_event(*run_id*, *message*, *node_state*, *name=''*, *hostname=''*, *pid=None*, *master_endpoint=''*, *local_id=None*, *rank=None*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/distributed/elastic/events/__init__.py#L77)

Initialize rendezvous event object and record its operations.

Parameters:

- **run_id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The run id of the rendezvous.
- **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The message describing the event.
- **node_state** (*NodeState*) - The state of the node (INIT, RUNNING, SUCCEEDED, FAILED).
- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Event name. (E.g. Current action being performed).
- **hostname** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - Hostname of the node.
- **pid** (*Optional**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - The process id of the node.
- **master_endpoint** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - The master endpoint for the rendezvous store, if known.
- **local_id** (*Optional**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - The local_id of the node, if defined in dynamic_rendezvous.py
- **rank** (*Optional**[*[*int*](https://docs.python.org/3/library/functions.html#int)*]*) - The rank of the node, if known.

Returns:

None

Return type:

None

Example

```
>>> # See DynamicRendezvousHandler class
>>> def _record(
... self,
... message: str,
... node_state: NodeState = NodeState.RUNNING,
... rank: Optional[int] = None,
... ) -> None:
... construct_and_record_rdzv_event(
... name=f"{self.__class__.__name__}.{get_method_name()}",
... run_id=self._settings.run_id,
... message=message,
... node_state=node_state,
... hostname=self._this_node.addr,
... pid=self._this_node.pid,
... local_id=self._this_node.local_id,
... rank=rank,
... )
```

torch.distributed.elastic.events.get_logging_handler(*destination='null'*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/distributed/elastic/events/handlers.py#L19)

Return type:

[*Handler*](https://docs.python.org/3/library/logging.html#logging.Handler)

torch.distributed.elastic.events.record_rdzv_event(*event*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/distributed/elastic/events/__init__.py#L73)

## Event Objects

*class*torch.distributed.elastic.events.api.Event(*name*, *source*, *timestamp=0*, *metadata=<factory>*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/distributed/elastic/events/api.py#L28)

The class represents the generic event that occurs during the torchelastic job execution.

The event can be any kind of meaningful action.

Parameters:

- **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - event name.
- **source** (*EventSource*) - the event producer, e.g. agent or worker
- **timestamp** ([*int*](https://docs.python.org/3/library/functions.html#int)) - timestamp in milliseconds when event occurred.
- **metadata** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*|*[*int*](https://docs.python.org/3/library/functions.html#int)*|*[*float*](https://docs.python.org/3/library/functions.html#float)*|*[*bool*](https://docs.python.org/3/library/functions.html#bool)*|**None**]*) - additional data that is associated with the event.

*class*torch.distributed.elastic.events.api.EventSource(*value*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/distributed/elastic/events/api.py#L21)

Known identifiers of the event producers.

torch.distributed.elastic.events.api.EventMetadataValue

alias of [`str`](https://docs.python.org/3/library/stdtypes.html#str) | [`int`](https://docs.python.org/3/library/functions.html#int) | [`float`](https://docs.python.org/3/library/functions.html#float) | [`bool`](https://docs.python.org/3/library/functions.html#bool) | [`None`](https://docs.python.org/3/library/constants.html#None)

*class*torch.distributed.elastic.events.api.NodeState(*value*)[[source]](https://github.com/pytorch/pytorch/blob/c7cc4bfa9ed99a2c007afe3e21208bc892c5aa18/torch/distributed/elastic/events/api.py#L64)

The states that a node can be in rendezvous.