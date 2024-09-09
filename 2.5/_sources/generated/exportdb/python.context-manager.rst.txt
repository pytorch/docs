python.context-manager
==========================
null_context_manager
^^^^^^^^^^^^^^^^^^^^

.. note::

    Tags: :doc:`python.context-manager <python.context-manager>`

    Support Level: SUPPORTED

Original source code:

.. code-block:: python

    # mypy: allow-untyped-defs
    import contextlib
    
    import torch
    
    class NullContextManager(torch.nn.Module):
        """
        Null context manager in Python will be traced out.
        """
    
        def forward(self, x):
            """
            Null context manager in Python will be traced out.
            """
            ctx = contextlib.nullcontext()
            with ctx:
                return x.sin() + x.cos()
    
    example_args = (torch.randn(3, 2),)
    tags = {"python.context-manager"}
    model = NullContextManager()
    

    torch.export.export(model, example_args)

Result:

.. code-block::

    ExportedProgram:
        class GraphModule(torch.nn.Module):
            def forward(self, x: "f32[3, 2]"):
                     sin: "f32[3, 2]" = torch.ops.aten.sin.default(x)
                cos: "f32[3, 2]" = torch.ops.aten.cos.default(x);  x = None
                add: "f32[3, 2]" = torch.ops.aten.add.Tensor(sin, cos);  sin = cos = None
                return (add,)
                
    Graph signature: ExportGraphSignature(input_specs=[InputSpec(kind=<InputKind.USER_INPUT: 1>, arg=TensorArgument(name='x'), target=None, persistent=None)], output_specs=[OutputSpec(kind=<OutputKind.USER_OUTPUT: 1>, arg=TensorArgument(name='add'), target=None)])
    Range constraints: {}
    
