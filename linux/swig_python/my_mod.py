# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_my_mod', [dirname(__file__)])
        except ImportError:
            import _my_mod
            return _my_mod
        if fp is not None:
            try:
                _mod = imp.load_module('_my_mod', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _my_mod = swig_import_helper()
    del swig_import_helper
else:
    import _my_mod
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _my_mod.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _my_mod.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _my_mod.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _my_mod.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _my_mod.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _my_mod.SwigPyIterator_equal(self, x)

    def copy(self):
        return _my_mod.SwigPyIterator_copy(self)

    def next(self):
        return _my_mod.SwigPyIterator_next(self)

    def __next__(self):
        return _my_mod.SwigPyIterator___next__(self)

    def previous(self):
        return _my_mod.SwigPyIterator_previous(self)

    def advance(self, n):
        return _my_mod.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _my_mod.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _my_mod.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _my_mod.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _my_mod.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _my_mod.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _my_mod.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _my_mod.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


def add(a, b):
    return _my_mod.add(a, b)
add = _my_mod.add

def append(a, b):
    return _my_mod.append(a, b)
append = _my_mod.append

def test(*args):
    return _my_mod.test(*args)
test = _my_mod.test

def point_ret():
    return _my_mod.point_ret()
point_ret = _my_mod.point_ret

def sub2(x, y):
    return _my_mod.sub2(x, y)
sub2 = _my_mod.sub2

def two_ret(x, y):
    return _my_mod.two_ret(x, y)
two_ret = _my_mod.two_ret

def ref_ret():
    return _my_mod.ref_ret()
ref_ret = _my_mod.ref_ret
class vectori(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectori, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectori, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _my_mod.vectori_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _my_mod.vectori___nonzero__(self)

    def __bool__(self):
        return _my_mod.vectori___bool__(self)

    def __len__(self):
        return _my_mod.vectori___len__(self)

    def pop(self):
        return _my_mod.vectori_pop(self)

    def __getslice__(self, i, j):
        return _my_mod.vectori___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _my_mod.vectori___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _my_mod.vectori___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _my_mod.vectori___delitem__(self, *args)

    def __getitem__(self, *args):
        return _my_mod.vectori___getitem__(self, *args)

    def __setitem__(self, *args):
        return _my_mod.vectori___setitem__(self, *args)

    def append(self, x):
        return _my_mod.vectori_append(self, x)

    def empty(self):
        return _my_mod.vectori_empty(self)

    def size(self):
        return _my_mod.vectori_size(self)

    def clear(self):
        return _my_mod.vectori_clear(self)

    def swap(self, v):
        return _my_mod.vectori_swap(self, v)

    def get_allocator(self):
        return _my_mod.vectori_get_allocator(self)

    def begin(self):
        return _my_mod.vectori_begin(self)

    def end(self):
        return _my_mod.vectori_end(self)

    def rbegin(self):
        return _my_mod.vectori_rbegin(self)

    def rend(self):
        return _my_mod.vectori_rend(self)

    def pop_back(self):
        return _my_mod.vectori_pop_back(self)

    def erase(self, *args):
        return _my_mod.vectori_erase(self, *args)

    def __init__(self, *args):
        this = _my_mod.new_vectori(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, x):
        return _my_mod.vectori_push_back(self, x)

    def front(self):
        return _my_mod.vectori_front(self)

    def back(self):
        return _my_mod.vectori_back(self)

    def assign(self, n, x):
        return _my_mod.vectori_assign(self, n, x)

    def resize(self, *args):
        return _my_mod.vectori_resize(self, *args)

    def insert(self, *args):
        return _my_mod.vectori_insert(self, *args)

    def reserve(self, n):
        return _my_mod.vectori_reserve(self, n)

    def capacity(self):
        return _my_mod.vectori_capacity(self)
    __swig_destroy__ = _my_mod.delete_vectori
    __del__ = lambda self: None
vectori_swigregister = _my_mod.vectori_swigregister
vectori_swigregister(vectori)

class vectorstr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorstr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorstr, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _my_mod.vectorstr_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _my_mod.vectorstr___nonzero__(self)

    def __bool__(self):
        return _my_mod.vectorstr___bool__(self)

    def __len__(self):
        return _my_mod.vectorstr___len__(self)

    def pop(self):
        return _my_mod.vectorstr_pop(self)

    def __getslice__(self, i, j):
        return _my_mod.vectorstr___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _my_mod.vectorstr___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _my_mod.vectorstr___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _my_mod.vectorstr___delitem__(self, *args)

    def __getitem__(self, *args):
        return _my_mod.vectorstr___getitem__(self, *args)

    def __setitem__(self, *args):
        return _my_mod.vectorstr___setitem__(self, *args)

    def append(self, x):
        return _my_mod.vectorstr_append(self, x)

    def empty(self):
        return _my_mod.vectorstr_empty(self)

    def size(self):
        return _my_mod.vectorstr_size(self)

    def clear(self):
        return _my_mod.vectorstr_clear(self)

    def swap(self, v):
        return _my_mod.vectorstr_swap(self, v)

    def get_allocator(self):
        return _my_mod.vectorstr_get_allocator(self)

    def begin(self):
        return _my_mod.vectorstr_begin(self)

    def end(self):
        return _my_mod.vectorstr_end(self)

    def rbegin(self):
        return _my_mod.vectorstr_rbegin(self)

    def rend(self):
        return _my_mod.vectorstr_rend(self)

    def pop_back(self):
        return _my_mod.vectorstr_pop_back(self)

    def erase(self, *args):
        return _my_mod.vectorstr_erase(self, *args)

    def __init__(self, *args):
        this = _my_mod.new_vectorstr(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, x):
        return _my_mod.vectorstr_push_back(self, x)

    def front(self):
        return _my_mod.vectorstr_front(self)

    def back(self):
        return _my_mod.vectorstr_back(self)

    def assign(self, n, x):
        return _my_mod.vectorstr_assign(self, n, x)

    def resize(self, *args):
        return _my_mod.vectorstr_resize(self, *args)

    def insert(self, *args):
        return _my_mod.vectorstr_insert(self, *args)

    def reserve(self, n):
        return _my_mod.vectorstr_reserve(self, n)

    def capacity(self):
        return _my_mod.vectorstr_capacity(self)
    __swig_destroy__ = _my_mod.delete_vectorstr
    __del__ = lambda self: None
vectorstr_swigregister = _my_mod.vectorstr_swigregister
vectorstr_swigregister(vectorstr)

# This file is compatible with both classic and new-style classes.


