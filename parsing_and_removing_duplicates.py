import requests
from bs4 import BeautifulSoup
from multiprocessing import Manager
from concurrent.futures import ProcessPoolExecutor


def download_images_from_page(page_url, current_dict, lock):
    local_dict = {}
    try:
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, "html.parser")
        img_tags = soup.find_all("img")

        for img_tag in img_tags:
            file_url = img_tag.get('src')
            full_url = requests.compat.urljoin(page_url, file_url)
            img_response = requests.get(full_url)
            key = len(img_response.content)
            local_dict[key] = local_dict.get(key, 0) + 1
    except Exception as e:
        print(f"Ошибка при обработке {page_url}: {e}")

    with lock:
        for key, value in local_dict.items():
            current_dict[key] = current_dict.get(key, 0) + value


if __name__ == '__main__':
    urls = [
        "https://asyncio.ru/multiprocessing/verif/4/folder_1/",
        "https://asyncio.ru/multiprocessing/verif/4/folder_2/",
        "https://asyncio.ru/multiprocessing/verif/4/folder_3/",
        "https://asyncio.ru/multiprocessing/verif/4/folder_4/",
        "https://asyncio.ru/multiprocessing/verif/4/folder_5/",
    ]
    with Manager() as manager:
        current_dict = manager.dict()
        lock = manager.Lock()
        result = 0
        result_lst = []
        with ProcessPoolExecutor(5) as executor:
            futures = [executor.submit(download_images_from_page, url, current_dict, lock) for url in urls]
            for future in futures:
                print(future.result())
        result_dict = dict(current_dict)

        for key, value in result_dict.items():
            if value == 1:
                result += key
                result_lst.append(key)
        print(len(result_lst))
        print(result)
