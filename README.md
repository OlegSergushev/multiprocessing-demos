# multiprocessing-demos
A set of short and simple scripts demonstrating the use of the `multiprocessing` module in Python. Suitable for learning, experimenting and reusing.
# What's inside
- 'multiprocessor_data_transfer.py': This code uses four processes to assemble a string in sequence, passing data from one process to the next via Pipes. Each process adds its part of the sentence to the resulting string, and eventually the final process passes the assembled string back to the main process, where it is printed to the screen.
