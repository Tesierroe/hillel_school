import os
import pickle

def count_folders_and_files(path, processed_paths):
    folders_count = 0
    files_count = 0
    largest_file = None
    smallest_file = None
    longest_name = None
    shortest_name = None

    for root, dirs, files in os.walk(path):

        if root in processed_paths:
            continue

        folders_count += len(dirs)
        files_count += len(files)

        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)

            if largest_file is None or file_size > os.path.getsize(largest_file):
                largest_file = file_path

            if smallest_file is None or file_size < os.path.getsize(smallest_file):
                smallest_file = file_path

            if longest_name is None or len(file) > len(longest_name):
                longest_name = file

            if shortest_name is None or len(file) < len(shortest_name):
                shortest_name = file

    return folders_count, files_count, largest_file, smallest_file, longest_name, shortest_name


def save_processed_paths(path, processed_paths):
    with open(path, 'wb') as file:
        pickle.dump(processed_paths, file)


def load_processed_paths(path):
    if not os.path.exists(path):
        return []

    with open(path, 'rb') as file:
        return pickle.load(file)


path = '/Users/janenuts/PycharmProjects/pythonProject/lesson_7'
processed_paths_file = 'processed_paths.pkl'

try:
    processed_paths = load_processed_paths(processed_paths_file)
    folders, files, largest_file, smallest_file, longest_name, shortest_name = count_folders_and_files(path, processed_paths)

    print(f"Количество папок: {folders}")
    print(f"Количество файлов: {files}")
    print(f"Самый большой файл: {largest_file} ({os.path.getsize(largest_file)} байт)")
    print(f"Самый маленький файл: {smallest_file} ({os.path.getsize(smallest_file)} байт)")
    print(f"Самое длинное имя файла: {longest_name}")
    print(f"Самое короткое имя файла: {shortest_name}")

    processed_paths.append(path)
    save_processed_paths(processed_paths_file, processed_paths)

except KeyboardInterrupt:
    print("\nПрерывание скрипта. Сохранение промежуточных результатов...")

    processed_paths.append(path)
    save_processed_paths(processed_paths_file, processed_paths)

    print("Промежуточные результаты сохранены.")
