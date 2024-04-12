import json
import os


def merge_json_files(directory):
    merged_data = []

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(data)
                merged_data.append(data)

    return merged_data


# 使用函数
directory = 'C:\\Users\\chenzihan\\Desktop\\pathfinder\\feats\\'  # 替换为你的目录
merged_data = merge_json_files(directory)

# 将合并的数据保存到新的json文件中
with open('merged.json', 'w', encoding='utf-8') as f:
    json.dump(merged_data, f, ensure_ascii=False)
