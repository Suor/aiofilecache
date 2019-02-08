AioFilecache
============

A file-based backend for `aiocache <https://github.com/argaen/aiocache>`_.


Installation
-------------

::

    pip install aiofilecache


Usage
-----

.. code:: python

    from aiocache import cached
    from aiocache.serializers import PickleSerializer
    from aiofilecache import FileCache

    @cached(cache=FileCache, serializer=PickleSerializer(), basedir='/tmp/...')
    async def cached_func(...):
        # ...
