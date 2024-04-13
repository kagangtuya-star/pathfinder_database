import json


def transform_json(input_file, output_file):
    # 加载输入文件
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 遍历entries中的每一个条目
    for entry in data['entries'].values():
        # 创建actions字典，并设置默认值
        action = {
            'name': '施法',
            'savingThrow': entry.get('savingThrow', ''),
            'target': entry.get('target', ''),
            'duration': entry.get('duration', ''),
            'area': entry.get('area', ''),
            'effectNotes': [],
            'effect': entry.get('effect', '')
        }

        # 使用新的actions字典替换旧的字段
        entry['actions'] = [action]

        # 移除不再需要的字段
        for field in ['savingThrow', 'target', 'area', 'duration', 'effect']:
            if field in entry:
                del entry[field]

    # 写入输出文件
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# 调用函数
transform_json('input.json', 'pf1.spells.json')
