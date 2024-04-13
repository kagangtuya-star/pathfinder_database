import os
import json

# 读取同路径下的merged.json文件，作为汉化数据源；读取同路径下的pf-content.pf-feats.json文件，作为被翻译的数据
# 读取merged.json文件
with open('feats-merged.json', 'r', encoding='utf-8') as f:
    data1 = json.load(f)
    print("1")

# 读取pf-content.pf-feats.json文件
with open('pf-content.pf-feats.json', 'r', encoding='utf-8') as f:
    data2 = json.load(f)
    print("2")
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
    ('staminaText_zh', '战策增益：'),
    ('staminaSource', '战策资源出处: ')
]

# 神话版本
fields_with_labels_myth = [
    ('mythicText_zh', '神话专长描述：'),
    ("mythicBenefit_zh", "神话专长效果："),
    ('mythicSource', '资源出处: '),
    ('url', "原文索引: ")
]

for item in data1:
    if item['name'] in data2["entries"]:
        name_en = item['name']
        if item.get('name_zh'):
            name_zh = item['name_zh']
            content_parts = []
            for field, label in fields_with_labels:
                if item.get(field):
                    if field == 'descriptors':
                        descriptors_t = ''.join(
                            item[field]).replace("'", "")
                        content_parts.append(
                            f"<b>{label}</b>{descriptors_t}")
                    elif field == 'text_zh':
                        text_zh = ''.join(item[field]).replace(
                            "'", "").replace('[', '').replace(']', '')
                        content_parts.append(
                            f"<em>{text_zh}</em>")
                    elif field == 'source':
                        source_t = ''.join(item[field]).replace(
                            "'", "").replace('[', '').replace(']', '')
                        content_parts.append(f"<b>{label}</b>{source_t}")
                    else:
                        content_parts.append(
                            f"<b>{label}</b>{item[field]}")
            # 战策版本
            for field, label in fields_with_labels_tactic:
                if item.get(field):
                    content_parts.append(f"<b>{label}</b>{item[field]}")
            content = '<br/><br/>'.join(content_parts)
            data2["entries"][name_en]["name"] = name_zh+f" {name_en}"
            data2["entries"][name_en]["description"] = content

    # 处理神话版本
    if item['name']+" (Mythic)" in data2["entries"]:
        name_en = item['name']+" (Mythic)"
        if item.get('name_zh'):
            name_zh = item['name_zh']+"(神话)"
            content_parts = []
            for field, label in fields_with_labels_myth:
                if item.get(field):
                    if field == 'mythicText_zh':
                        mythicText_zh = ''.join(item[field]).replace(
                            "'", "").replace('[', '').replace(']', '')
                        content_parts.append(
                            f"<em>{mythicText_zh}</em>")
                    else:
                        content_parts.append(
                            f"<b>{label}</b>{item[field]}")
            feat_myth_prerequisite = f"<b>先决条件：</b>{item['name_zh']}<br/><br/>"
            content = '<br/><br/>'.join(content_parts)
            data2["entries"][name_en]["name"] = name_zh+f" {name_en}"
            data2["entries"][name_en]["description"] = feat_myth_prerequisite+content
# 在处理完所有数据后，将修改后的数据保存回pf-content.pf-feats.json文件
with open('pf-content.pf-feats.json', 'w', encoding='utf-8') as f:
    json.dump(data2, f, ensure_ascii=False, indent=4)

with open('pf1.feats.json', 'r', encoding='utf-8') as f:
    data2 = json.load(f)
    print("3")

for item in data1:
    if item['name'] in data2["entries"]:
        name_en = item['name']
        if item.get('name_zh'):
            name_zh = item['name_zh']
            content_parts = []
            for field, label in fields_with_labels:
                if item.get(field):
                    if field == 'descriptors':
                        descriptors_t = ''.join(
                            item[field]).replace("'", "")
                        content_parts.append(
                            f"<b>{label}</b>{descriptors_t}")
                    elif field == 'text_zh':
                        text_zh = ''.join(item[field]).replace(
                            "'", "").replace('[', '').replace(']', '')
                        content_parts.append(
                            f"<em>{text_zh}</em><br/><br/>")
                    elif field == 'source':
                        source_t = ''.join(item[field]).replace(
                            "'", "").replace('[', '').replace(']', '')
                        content_parts.append(f"<b>{label}</b>{source_t}")
                    else:
                        content_parts.append(
                            f"<b>{label}</b>{item[field]}")
            # 战策版本
            for field, label in fields_with_labels_tactic:
                if item.get(field):
                    content_parts.append(f"<b>{label}</b>{item[field]}")
            content = '<br/><br/>'.join(content_parts)
            data2["entries"][name_en]["name"] = name_zh+f" {name_en}"
            data2["entries"][name_en]["description"] = content

    # 处理神话版本
    if item['name']+" (Mythic)" in data2["entries"]:
        name_en = item['name']+" (Mythic)"
        if item.get('name_zh'):
            name_zh = item['name_zh']+"(神话)"
            content_parts = []
            for field, label in fields_with_labels_myth:
                if item.get(field):
                    if field == 'mythicText_zh':
                        mythicText_zh = ''.join(item[field]).replace(
                            "'", "").replace('[', '').replace(']', '')
                        content_parts.append(
                            f"<em>{mythicText_zh}</em><br/><br/>")
                    else:
                        content_parts.append(
                            f"<b>{label}</b>{item[field]}")
            feat_myth_prerequisite = f"<b>先决条件：</b>{item['name_zh']}<br/><br/>"
            content = '<br/><br/>'.join(content_parts)
            data2["entries"][name_en]["name"] = name_zh+f" {name_en}"
            data2["entries"][name_en]["description"] = feat_myth_prerequisite+content
with open('pf1.feats.json', 'w', encoding='utf-8') as f:
    json.dump(data2, f, ensure_ascii=False, indent=4)
