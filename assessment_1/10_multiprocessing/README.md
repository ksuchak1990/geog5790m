# 10 - Multiprocessing

The aim of this practical is to introduce the concept of multiprocessing, i.e.
the process of breaking down of the overall task into smaller parts that can be
run concurrently with each other by the individual computational units at our
disposal.

In order to demonstrate this, a pre-built agent-based model is used (see [this
paper](https://www.sciencedirect.com/science/article/pii/S0304380006002894
"Aphid population response...")) in conjunction with Python's `multiprocessing`
module.
This implements a Message Passing Interface (MPI) whereby we have a parent
process connected to each of the child processes by 'pipes'.
The child node undertake the bulk of the work for the model, sending their
results back to the parent node.
Upon receiving the results from the child nodes, the parent node collates them
together.
