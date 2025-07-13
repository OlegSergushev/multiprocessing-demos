import multiprocessing
from concurrent.futures import ProcessPoolExecutor


def initializer_worker():
    print(f'💻 Инициализация процесса {multiprocessing.current_process().pid}.')


def handle_request(user_name):
    print(f'✅ Запрос от пользователя {user_name} обработан процессом {multiprocessing.current_process().pid}')


def main(users):
    with ProcessPoolExecutor(max_workers=3, max_tasks_per_child=2, initializer=initializer_worker) as executor:
        executor.map(handle_request, users)


if __name__ == '__main__':
    users = ['Анна', 'Борис', 'Виктор', 'Галина', 'Дмитрий', 'Елена']
    main(users)
