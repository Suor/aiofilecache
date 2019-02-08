import hashlib
import os

from aiocache.base import BaseCache
import aiofiles


class FileCache(BaseCache):
    """A file based backend for aiocache"""
    def __init__(self, basedir='/tmp/aiocache', **kwargs):
        super().__init__(**kwargs)
        self.basedir = basedir

    def _build_key(self, key, namespace=None):
        """Builds a key which is a filename"""
        ns = namespace if namespace is not None else \
             self.namespace if self.namespace is not None else ''
        digest = hashlib.md5(key.encode()).hexdigest()
        return os.path.join(self.basedir, ns, digest[:2], digest[2:])

    async def _get(self, key, encoding="utf-8", _conn=None):
        try:
            async with aiofiles.open(key, 'rb') as f:
                return await f.read()
        except (IOError, OSError, EOFError):
            return None

    async def _set(self, key, value, ttl=None, _cas_token=None, _conn=None):
        assert ttl is None, 'TTL is not implemented for file backend'

        # TODO: make this in a thread? Or add these to aiofiles?
        dirname = os.path.dirname(key)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        # Use open() with exclusive rights to prevent data corruption
        def opener(filename, flags):
            return os.open(filename, flags | os.O_EXCL | os.O_WRONLY | os.O_CREAT)

        try:
            async with aiofiles.open(key, mode='wb', opener=opener) as f:
                await f.write(value)
        except (IOError, OSError):
            pass

    # def delete(self, fname):
    #     try:
    #         os.remove(fname)
    #         # Trying to remove directory in case it's empty
    #         dirname = os.path.dirname(fname)
    #         os.rmdir(dirname)
    #     except (IOError, OSError):
    #         pass
