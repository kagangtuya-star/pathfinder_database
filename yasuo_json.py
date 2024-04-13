import os
import json


def minimize_json_files(directory):
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(subdir, file)
                with open(file_path, 'r', encoding='utf-8') as f_in:
                    data = json.load(f_in)
                with open(file_path, 'w', encoding='utf-8') as f_out:
                    json.dump(data, f_out, separators=(
                        ',', ':'), ensure_ascii=False)


current_directory = os.getcwd()
minimize_json_files(current_directory)
