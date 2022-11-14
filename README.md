# Singly linked lists

This is a link for a single-linked lists:

```python
class Link(object):
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
    def __repr__(self):
        return f'Link({self.head}, {self.tail})'
```

(The implementation in `src/lists.py` differs slightly, but that is only relevant for type checking, so you don't need to worry about it).

It is not that differenrent from the lists we used when we exercised our skills on recursive functions, here we have just implemented the list ourselves instead of relying on `dataclass` magic…

You can create lists using e.g.

```python
Link(21, Link(43, None))
```

and always prepend a value `val` to a list `lst` using 

```python
new_lst = Link(al, lst)
```

and if you want the tail (all except the first element) of a list, you have it right at your hands with

```python
lst.next
```

**Exercise:** Write a function `length(x)` that returns the length of a list `x`.

**Exercise:** Implement a function, `drop(x,k)`, that removes `k` elements from a list `x`, i.e., a function that returns a new list that contains all the elements from a list except the first `k`.

**Exercise:** Write a function, `take(x,k)`, that creates a list of only the first `k` elements of a list `x`.

**Exercise:** Write a function, `reverse(x)`, that reverses a linked list.

**Exercise:** Write a function that makes a copy of a linked list.
