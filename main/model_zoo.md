# torch.utils.model_zoo

Moved to `torch.hub`.

torch.utils.model_zoo.load_url(*url*, *model_dir=None*, *map_location=None*, *progress=True*, *check_hash=False*, *file_name=None*, *weights_only=False*)[[source]](https://github.com/pytorch/pytorch/blob/94de2113ebf2891e498dd58ed1a16fedac39b5c6/torch/hub.py#L829)

Loads the Torch serialized object at the given URL.

If downloaded file is a zip file, it will be automatically
decompressed.

If the object is already present in model_dir, it's deserialized and
returned.
The default value of `model_dir` is `<hub_dir>/checkpoints` where
`hub_dir` is the directory returned by [`get_dir()`](hub.html#torch.hub.get_dir).

Parameters:

- **url** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) - URL of the object to download
- **model_dir** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - directory in which to save the object
- **map_location** (*optional*) - a function or a dict specifying how to remap storage locations (see torch.load)
- **progress** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - whether or not to display a progress bar to stderr.
Default: True
- **check_hash** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If True, the filename part of the URL should follow the naming convention
`filename-<sha256>.ext` where `<sha256>` is the first eight or more
digits of the SHA256 hash of the contents of the file. The hash is used to
ensure unique names and to verify the contents of the file.
Default: False
- **file_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)*,**optional*) - name for the downloaded file. Filename from `url` will be used if not set.
- **weights_only** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,**optional*) - If True, only weights will be loaded and no complex pickled objects.
Recommended for untrusted sources. See [`load()`](generated/torch.load.html#torch.load) for more details.

Return type:

[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)]

Example

```
>>> state_dict = torch.hub.load_state_dict_from_url(
... "https://s3.amazonaws.com/pytorch/models/resnet18-5c106cde.pth"
... )
```