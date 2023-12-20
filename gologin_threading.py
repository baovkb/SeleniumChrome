import threading
from goprofile import ProfileGL


class Gologin_Threading(threading.Thread):
    def __init__(self,group=None, target=None, name=None,
                args=(), kwargs=None, *, daemon=None):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self._return = None
    
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)
    
    def join(self):
        threading.Thread.join(self)
        return self._return
    
