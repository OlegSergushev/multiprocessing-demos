import multiprocessing


def process_1(conn1a):
    word = "Start: "
    conn1a.send(word)
    print(f"Process 1: Отправлено слово '{word}'")
    conn1a.close()
    

def process_2(conn1b, conn2a):
    word = conn1b.recv()
    word += "Однажды храбрый программист "
    conn2a.send(word)
    print(f"Process 2: Получено '{word}' и отправлено дальше")
    conn1b.close()
    conn2a.close()
    

def process_3(conn2b, conn3a):
    word = conn2b.recv()
    word += "отправился в страну Python "
    conn3a.send(word)
    print(f"Process 3: Получено '{word}' и отправлено дальше")
    conn2b.close()
    conn3a.close()
    

def process_4(conn3b, conn4a):
    word = conn3b.recv()
    word += "и победил все ошибки!"
    conn4a.send(word)
    print(f"Process 4: Получено '{word}' и отправлено в основной процесс")
    conn3b.close()
    conn4a.close()
    

if __name__ == "__main__":
    # Создайте каналы для передачи данных между процессами
    conn1a, conn1b =  multiprocessing.Pipe()     # Канал для передачи от process1 к process2
    conn2a, conn2b =  multiprocessing.Pipe()     # Канал для передачи от process2 к process3
    conn3a, conn3b =  multiprocessing.Pipe()     # Канал для передачи от process3 к process4
    conn4a, conn4b =  multiprocessing.Pipe()     # Канал для передачи от process4 в основной процесс

    # Создайте процессы
    process1 = multiprocessing.Process(target=process_1, args=(conn1b,))
    process2 = multiprocessing.Process(target=process_2, args=(conn1a, conn2b))
    process3 = multiprocessing.Process(target=process_3, args=(conn2a, conn3b))
    process4 = multiprocessing.Process(target=process_4, args=(conn3a, conn4b))
    
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    
    result_text = conn4a.recv()
    
    process1.join()
    process2.join()
    process3.join()
    process4.join()
    
    print(f"Итоговая строка: {result_text}")
