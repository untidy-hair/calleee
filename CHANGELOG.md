# Changelog

## 0.4.0

* The first version as `calleee`
* Python 3.8 & 3.9 support
* Drop 2.6, 2.7, pypy2, 3.4, 3.5

## 0.3.1

* Python 3.6 & 3.7 support

## 0.3

* `strict=` param in `SubclassOf`.
* `exact=` param in `InstanceOf`.

### New matchers

* `Either` (alias: `OneOf`, `Xor`)
* `FileLike`
* `OrderedDict`
* `Coroutine` and `CoroutineFunction`

## 0.2.2

* Fix a bug in `__repr__` of `And` and `Or` matchers

## 0.2.1

* `desc=` argument to the `Matching` / `ArgThat` matcher

### New matchers

* `Captor` (an argument captor)

## 0.1.2

* Better `repr()` of the `Matching` / `ArgThat` matcher's predicate
