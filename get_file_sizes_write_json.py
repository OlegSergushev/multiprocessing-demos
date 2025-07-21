from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager
import os
import json


def update_dict(file, current_dict):
    file_size = os.path.getsize(file)
    file_name = os.path.basename(file)
    current_dict[file_name] = file_size


if __name__ == '__main__':
    with Manager() as manager:
        current_dict = manager.dict()
        path = [empty.path for empty in os.scandir('insert the folder with files here') if os.path.splitext(empty.name)[1].lower() == '.jpg']
        with ProcessPoolExecutor() as executor:
            futures = [executor.submit(update_dict, file, current_dict) for file in path]
            for future in futures:
                print(future.result())
        current_dict = dict(sorted(current_dict.items(), key=lambda item: item[0]))
        json_file = json.dumps(current_dict, indent=4)
        with open('sizes.txt', 'w', encoding='utf-8') as file:
            file.write(json_file)
