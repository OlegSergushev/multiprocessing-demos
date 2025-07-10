from multiprocessing import Condition, Process
from time import sleep


def wait_for_signal(condition, name, item):
    print(f'{name} ожидает уведомления...')
    with condition:
        if condition.wait(timeout=5):
            print(f'{name} получил уведомление и забрал {item}')
        else:
            print(f'{name} не получил уведомление и ушёл без {item}')


if __name__ == '__main__':
    # Имена персонажей и их "предметы"
    characters = ["Шрек", "Ослик", "Кот в сапогах", "Фиона", "Дракониха"]
    items = ["гиря", "гантеля", "скакалка", "коврик для йоги", "бутылка с водой"]

    condition = Condition()
    processes = [Process(target=wait_for_signal, args=(condition, name, item)) for name, item in zip(characters,items)]
    
    [p.start() for p in processes]
    time.sleep(2)
    
    with condition:
        print('Главный процесс отправляет уведомления 3 персонажам...')
        condition.notify(3)
    
    [p.join() for p in processes]
