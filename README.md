## 🧠
Here I am exploring Python's [threading](https://docs.python.org/3/library/threading.html) module and learning more about the [GIL](https://realpython.com/python-gil/) by attempting to solve the _Sleeping Barber problem_.

To quote:
> Imagine a hypothetical barbershop with one barber, one barber chair, and a waiting room with _n_ chairs (_n_ may be 0) for waiting customers. The following rules apply:
>
> - If there are no customers, the barber falls asleep in the chair
> - A customer must wake the barber if he is asleep
> - If a customer arrives while the barber is working, the customer leaves if all chairs are occupied and sits in an empty chair if it's available
> - When the barber finishes a haircut, he inspects the waiting room to see if there are any waiting customers and falls asleep if there are none

For this problem, I've decided to set the following rules:

- The barbershop will have 5 waiting chairs
- There are 5 max workers
- By the end, the total threads should be 500 - 1000

This is a work-in-progress. My goal here is to understand **Multi-threading** and also take a step in improving my Python skills.
