import os
import glob
import json
import pandas as pd


def process_json_to_excel(input_path):
    # 定义输出文件的路径
    output_file = input_path + 'output_data.xlsx'
    print('输出文件路径：', output_file)
    # 创建一个空的DataFrame
    df = pd.DataFrame(
        columns=['Key', 'Synonym', 'Content', 'Description', 'Catalogue', 'Tag'])

    # 读取指定目录下的所有JSON文件
    json_files = glob.glob(input_path + '*.json')

    for file_path in json_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # 处理有翻译的
            if 'name_zh' in data:

                # 构建Content列的内容
                content_parts = []
                fields_with_labels = [
                    ('descriptors', '专长类型：'),
                    ('text_zh', '专长描述：'),
                    ('prerequisites_zh', '先决条件: '),
                    ('benefit_zh', '专长效果: '),
                    ('special_zh', '特殊说明: '),
                    ('goal_zh', '专长目标: '),
                    ('normal_zh', '通常状况: '),
                    ('completionBenefit_zh', '完成收益: '),
                    ('source', '资源出处: '),
                    ('url', "原文索引: ")
                ]
                # 战策版本
                fields_with_labels_tactic = [
                    ('staminaText_zh', '\n战策增益：'),
                    ('staminaSource', '战策资源出处: ')
                ]

                # 神话版本
                fields_with_labels_myth = [
                    ('mythicText_zh', '\n神话版本描述：'),
                    ("mythicBenefit_zh", "神话专长效果："),
                    ('mythicSource', '神话资源出处: ')
                ]

                for field, label in fields_with_labels:
                    if data.get(field):
                        if field == 'descriptors':
                            descriptors_t = ''.join(
                                data[field]).replace("'", "")
                            content_parts.append(f"{label}{descriptors_t}")
                        elif field == 'source':
                            source_t = ''.join(data[field]).replace(
                                "'", "").replace('[', '').replace(']', '')
                            content_parts.append(f"{label}{source_t}")
                        else:
                            content_parts.append(f"{label}{data[field]}")
                for field, label in fields_with_labels_tactic:
                    if data.get(field):
                        content_parts.append(f"{label}{data[field]}")
                for field, label in fields_with_labels_myth:
                    if data.get(field):
                        content_parts.append(f"{label}{data[field]}")
                content = '\n'.join(content_parts)
                if data.get('descriptors'):
                    descriptors_temp = '[' + \
                        ''.join(data.get('descriptors', [])) + '] '
                else:
                    descriptors_temp = ''
                content_result = data.get(
                    'name_zh')+descriptors_temp+data.get('name', '')+'\n'+content.replace("<\/p><p>", "").replace("<p>", "").replace("</p>", "")
                # 将数据追加到DataFrame中
                row = {
                    'Key': data.get('name_zh'),
                    'Synonym': data.get('name', ''),
                    'Content': content_result,
                    'Description': '',  # 根据需要填充这些字段
                    'Catalogue': '',
                    'Tag': 'PF1专长'
                }
                df = df.append(row, ignore_index=True)
                print(row)
            else:
                # 处理没翻译的
                # 构建Content列的内容
                content_parts = []
                fields_with_labels = [
                    ('descriptors', '专长类型：'),
                    ('text', '专长描述：'),
                    ('prerequisites', '先决: '),
                    ('benefit', '专长效果: '),
                    ('special', '特殊说明: '),
                    ('goal', '专长目标: '),
                    ('normal', '通常状况: '),
                    ('completionBenefit', '完成收益: '),
                    ('source', '资源出处: '),
                    ('url', "原文索引: ")
                ]
                # 战策版本
                fields_with_labels_tactic = [
                    ('staminaText', '\n战策增益：'),
                    ('staminaSource', '战策资源出处: ')
                ]

                # 神话版本
                fields_with_labels_myth = [
                    ('mythicText', '\n神话版本描述：'),
                    ("mythicBenefit", "神话专长效果："),
                    ('mythicSource', '神话资源出处: ')
                ]

                for field, label in fields_with_labels:
                    if data.get(field):
                        if field == 'descriptors':
                            descriptors_t = ''.join(
                                data[field]).replace("'", "")
                            content_parts.append(f"{label}{descriptors_t}")
                        elif field == 'source':
                            source_t = ''.join(data[field]).replace(
                                "'", "").replace('[', '').replace(']', '')
                            content_parts.append(f"{label}{source_t}")
                        else:
                            content_parts.append(f"{label}{data[field]}")
                for field, label in fields_with_labels_tactic:
                    if data.get(field):
                        content_parts.append(f"{label}{data[field]}")
                for field, label in fields_with_labels_myth:
                    if data.get(field):
                        content_parts.append(f"{label}{data[field]}")
                content = '\n'.join(content_parts)
                if data.get('descriptors'):
                    descriptors_temp = '[' + \
                        ''.join(data.get('descriptors', [])) + '] '
                else:
                    descriptors_temp = ''
                content_result = data.get(
                    'name')+descriptors_temp+'\n'+content.replace("<\/p><p>", "").replace("<p>", "").replace("</p>", "")
                # 将数据追加到DataFrame中
                row = {
                    'Key': data.get('name', ''),
                    'Synonym': '',
                    'Content':  content_result,
                    'Description': '',  # 根据需要填充这些字段
                    'Catalogue': '',
                    'Tag': 'PF1专长'
                }
                df = df.append(row, ignore_index=True)
                print(row)
    # 将DataFrame保存到Excel文件中
    df.to_excel(output_file, index=False)
    print('处理完成')


# 示例调用：process_json_to_excel('path/to/your/folder')
process_json_to_excel('C:\\Users\\chenzihan\\Desktop\\pathfinder\\feats\\')
print('处理完成')
