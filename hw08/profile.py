"""
Memory profiling with LRUCache
"""

import random
import weakref
from memory_profiler import profile
from faker import Faker
from hw05.LRUCache import LRUCache


class Student:
    """
    Simple student class
    """
    def __init__(self, name="Ivan", age=20, gpa=3.0):
        """
        Student's initialization
        """
        self.name = name
        self.age = age
        self.gpa = gpa


class StudentSlot:
    """
    Student class with slots
    """
    __slots__ = ("name", "age", "gpa")

    def __init__(self, name="Ivan", age=20, gpa=3.0):
        """
        Student initialization
        """
        self.name = name
        self.age = age
        self.gpa = gpa


@profile
def add_simple_students():
    """
    Add simple students to LRUCache
    """
    faker = Faker()
    cache = LRUCache(10000)
    for i in range(20000):
        cache.set(f"k{i}", Student(
                                faker.name(),
                                random.randint(16, 26),
                                round(random.uniform(2.0, 5.0), 2)
        ))


@profile
def add_slots_students():
    """
    Add students with slots to LRUCache
    """
    faker = Faker()
    cache = LRUCache(10000)
    for i in range(20000):
        cache.set(f"k{i}", StudentSlot(
                                faker.name(),
                                random.randint(16, 26),
                                round(random.uniform(2.0, 5.0), 2)
        ))


@profile
def add_weakref_students():
    """
    Add weakrefs on students to LRUCache
    """
    faker = Faker()
    cache = LRUCache(10000)
    for i in range(20000):
        cache.set(f"k{i}", weakref.ref(Student(
                                faker.name(),
                                random.randint(16, 26),
                                round(random.uniform(2.0, 5.0), 2)
        )))


if __name__ == "__main__":
    print("====Start add_simple_students====")
    add_simple_students()
    print("====Start add_slots_students====")
    add_slots_students()
    print("====Start add_weakref_students====")
    add_weakref_students()
