"""Singly-linked lists."""

from __future__ import annotations
from typing import Generic, TypeVar, Optional

T = TypeVar('T')  # Generic type variable


class Link(Generic[T]):
    """A link in a singly linked list."""

    head: T
    tail: LList[T]

    def __init__(self, head: T, tail: LList[T]):
        """Prepend a new head to tail."""
        self.head = head
        self.tail = tail

    def __repr__(self) -> str:
        """Representation string."""
        return f'Link({self.head}, {self.tail})'


LList = Optional[Link[T]]  # A list is just a reference to the head or None


def length(x: LList[T], acc = 1) -> int:
    """
    Get the length of x.

    >>> length(None)
    0
    >>> length(Link(1, None))
    1
    >>> length(Link(1, Link(2, None)))
    2
    """
    if x is None:
        return 0

    while x.tail != None:
        return length(x.tail, acc + 1)
    return acc




def drop(x: LList[T], k: int) -> LList[T]:
    """
    Drop the first k elements in the list.

    If length(x) < k, return the empty list.

    >>> drop(None, 1) is None
    True
    >>> drop(Link(1, None), 1) is None
    True
    >>> drop(Link(1, Link(2, None)), 1)
    Link(2, None)
    """

    if x is None or k == 0:
        return x
    else:
        return drop(x.tail, k - 1)



def take(x: LList[T], k: int) -> LList[T]:
    """
    Return a list with the first k elements in x.

    If length(x) < k, return the full list. You decide whether you
    want to return a copy of x or the original list.

    >>> take(None, 1) is None
    True
    >>> take(Link(1, None), 1)
    Link(1, None)
    >>> take(Link(1, Link(2, Link(3, None))), 2)
    Link(1, Link(2, None))
    """

    if length(x) < k or k == 0:
        return drop(x, 1)

    else:
        return Link(x.head, take(x.tail, k - 1))



def reverse(x: LList[T], acc = None) -> LList[T]:
    """
    Reverse a list.

    You decide whether you are allowed to modify the existing list
    or if you want to return a new list and leave the original one
    intact.

    >>> reverse(None) is None
    True
    >>> reverse(Link(1, None))
    Link(1, None)
    >>> reverse(Link(1, Link(2, Link(3, None))))
    Link(3, Link(2, Link(1, None)))
    """
    if x is None:
        return acc
    else:
        return reverse(x.tail, Link(x.head, acc))
