# multiprocessing-demos
A set of short and simple scripts demonstrating the use of the `multiprocessing` module in Python. Suitable for learning, experimenting and reusing.
# What's inside
- 'multiprocessor_data_transfer.py': This code uses four processes to assemble a string in sequence, passing data from one process to the next via Pipes. Each process adds its part of the sentence to the resulting string, and eventually the final process passes the assembled string back to the main process, where it is printed to the screen.
- 'notification _of_processes.py': The code creates five processes, each of which waits for notification. The main process notifies only three of them using the `notify(n)` method.
- 'kill_process.py': Killing a process by name using `process.terminate()`.
- 'processing_user_requests_with_max_tasks_per_child.py': In this code, each process in the pool undergoes initialization before starting work and then processes a certain number of tasks coming from users.
- 'task_management.py': This code manages the checking process for participants and stops the checking if one of them encounters problems, using an event object.
