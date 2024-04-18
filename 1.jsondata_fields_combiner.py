import json
import os


def merge_json_files(directory):
    merged_data = []

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
                data = json.load(f)
                # print(data)
                merged_data.append(data)

    return merged_data


directory = 'E:\\Code\\pathfinder_database\\spells\\'
merged_data = merge_json_files(directory)
with open('spell-merged.json', 'w', encoding='utf-8') as f:
    json.dump(merged_data, f, ensure_ascii=False)

directory2 = 'E:\\Code\\pathfinder_database\\feats\\'
merged_data2 = merge_json_files(directory2)
with open('feats-merged.json', 'w', encoding='utf-8') as f:
    json.dump(merged_data, f, ensure_ascii=False)
