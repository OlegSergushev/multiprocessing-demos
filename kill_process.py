from multiprocessing import Process
import time


# Функция для выполнения серверной задачи
def server_task(server_name):
    time.sleep(2)
    print(f"{server_name} работает...")


if __name__ == "__main__":
    servers = ['Charlie', 'Alpha', 'Bravo', 'Delta', 'Echo', 'Zeta', 'Omega', 'Nova', 'Aurora', 'Phoenix']

    # Создаем процессы с именами
    name = 'Charlie'
    kill_process = None
    processes = [Process(target=server_task, args=(server_name,), name=server_name) for server_name in servers]
    for process in processes:
        process.start()
        time.sleep(1)
        if process.name == name:
            process.terminate()
            kill_process = process

    [p.join() for p in processes]
    print(f"Charlie завершился с кодом: {kill_process.exitcode}")
