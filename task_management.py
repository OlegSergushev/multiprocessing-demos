from time import sleep
from multiprocessing import Manager
from concurrent.futures import ProcessPoolExecutor, wait, FIRST_EXCEPTION


# Функция проверки
def check_passanger(event, name):
    for _ in range(10):
        sleep(1)
        if name == 'John':
            raise Exception(f'Задача завершилась с ошибкой, name={name}')
        if event.is_set():
            print(f'Остановка, name={name}')
            return
        print(f'Работа продолжается, name={name}')


if __name__ == '__main__':
    with Manager() as manager:
        names = ["Alice", "Bob", "Charlie", "John", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack"]
        event = manager.Event()
        
        with ProcessPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(check_passanger, event, name) for name in names]
            print('Ожидание завершения задач или появления ошибки...')
            done, not_done = wait(futures, return_when=FIRST_EXCEPTION)
            event.set()
            if any((err := future.exception()) for future in done):
                print(err)
