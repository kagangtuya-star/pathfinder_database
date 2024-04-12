import os
import json
import re


with open('spell-merged.json', 'r', encoding='utf-8') as f:
    traned_spell_data = json.load(f)
    print("traned_spell_data loading!")

# 读取pf-content.pf-feats.json文件
with open('pf1.spells.json', 'r', encoding='utf-8') as f:
    fvtt_data = json.load(f)
    print("pf1.spells.json loading!")


# 需要额外增补的法术正文相关
spell_extra = [
    ('text_zh', '法术描述：'),
    ('source', '资源出处: '),
    ('url', "原文索引: ")
]

# 对于神话法术
sepll_myth_extar = [
    ('mythicText_zh', '神话版本：'),
    ('mythicSource', '资源出处: '),
    ('url', "原文索引: ")
]

# 法术描述符补全,acid air chaotic cold curse darkness death disease draconic earth electricity emotion evil fear fire force good language-dependent law lawful light meditative mind-affecting pain poison polymorph ruse see below see text shadow sonic travel water
spell_type_extra = [
    ('acid', '酸'),
    ('air', '气'),
    ('chaotic', '混乱'),
    ('cold', '寒冷'),
    ('curse', '诅咒'),
    ('darkness', '黑暗'),
    ('death', '死亡'),
    ('disease', '疾病'),
    ('draconic', '龙类'),
    ('earth', '土'),
    ('electricity', '电'),
    ('emotion', '情绪'),
    ('evil', '邪恶'),
    ('fear', '恐惧'),
    ('fire', '火'),
    ('force', '力场'),
    ('good', '善良'),
    ('language-dependent', '依赖语言'),
    ('law', '守序'),
    ('lawful', '秩序'),
    ('light', '光亮'),
    ('meditative', '冥想'),
    ('mind-affecting', '影响心灵'),
    ('pain', '痛苦'),
    ('poison', '毒素'),
    ('polymorph', '变形'),
    ('ruse', '诡计'),
    ('see below', '见下文'),
    ('see text', '见下文'),
    ('shadow', '阴影'),
    ('sonic', '音波'),
    ('travel', '旅行'),
    ('water', '水')
]

# 子学派补全 calling charm compulsion creation figment glamer haunted healing phantasm polymorph scrving summoning teleportation
spell_subschool_extra = [
    ('calling', '呼唤'),
    ('charm', '魅惑'),
    ('compulsion', '胁迫'),
    ('creation', '创造'),
    ('figment', '虚假幻觉'),
    ('glamer', '五官幻觉'),
    ('haunted', '作祟'),
    ('healing', '医疗'),
    ('phantasm', '魅影幻觉'),
    ('polymorph', '变形'),
    ('scrying', '探知'),
    ('summoning', '召唤'),
    ('teleportation', '传送')
]

# 领域补全 Ambush,5 Darkness Glory Greed.6 Isolation,6 Madness Ruins,1 Ruins,2 Ruins,4 Ruins,5 Ruins.6 Ruins,8 Scalykind,1 Scalykind,2 Scalykind,3 Scalykind,4 Scalykind,5 Scalykind,6 Scalykind,7 Scalykind,8 Scalykind,9 Vermin,1 Vermin,3 Vermin,4 Vermin,7 Vermin,9 Void.1 Void.2 Void,3 Void,4 Void.5 Void.6 Void,7 Void.8
spell_domain_extra = [
    ('Ambush', '伏击子域'),
    ('Darkness', '黑暗子域'),
    ('Glory', '荣耀子域'),
    ('Greed', '贪婪子域'),
    ('Isolation', '孤寂子域'),
    ('Madness', '狂乱子域'),
    ('Ruins', '废墟（Ruins）子域'),
    ('Scalykind', '鳞类子域'),
    ('Vermin', '昆虫子域'),
    ('Void', '虚空子域')
]

# 子域补全 Aeon,1 Aeon,5 Aeon,6 Ambush,1 Ambush,6 Arson,2 Arson,5 Arson,7 Cannibalism,1 Cannibalism,3 Competition,1 Competition,6 Corruption,2 Comuption,6 Demodand,2 Dragon,6 Education,2 Entropy,1 Entropy,3 Entropy,5 Entropy,7 Espionage,4 Espionage,9 Fear,1 Fear,2 Fear,4 Fist,1 Fist,3 Flotsam,2 Flotsam,5 Flotsam,6 Flowing,2 Flowing,4 Flowing,8 Fortifications,5 Fortifications,9 Friendship,2 Friendship,5 Imagination,1 Imagination,2 Imagination,3 Imagination,5 Industry,7 Innuendo,3 Innuendo,6 Isolation,4 Isolation,8 Judgment,5 Kyton,5 Legislation,9 Loyalty,1 Loyalty,5 Moon,1 Moon,6 Plague,3 Plague,8 Psychopomp,6 Psychopomp,8 Radiation,2 Radiation,4 Radiation,8 Redemption,5 Revelation,1 Revelation,2 Revelation,5 Revelry,2 Revelry,3 Revelry,6 Revelry,8 Riot,4 Riot,7 Rivers,5 Saurian,5 Saurian,7 Shadow,9 Slavery,1 Slavery,5 Slavery,8 Solitude,2 Solitude,4 Solitude,5 Stars,2 Stars,7 Stars,9 Torture,5 Torture,8 Trap,2 Trap,7 Tyranny,1 Tyranny,3 Tyranny,7 Venom,6 Whimsy,1 Whimsy,4
spell_subdomain_extra = [
    ('Aeon', '御衡者子域'),
    ('Ambush', '伏击子领'),
    ('Arson', '纵火子域'),
    ('Cannibalism', '食族子域'),
    ('Competition', '竞赛子域'),
    ('Corruption', '腐化子域'),
    ('Demodand', '魔孽子域'),
    ('Dragon', '龙子域'),
    ('Education', '教育子域'),
    ('Entropy', '熵子域'),
    ('Espionage', '间谍子域'),
    ('Fear', '恐惧子域'),
    ('Fist', '拳头子域'),
    ('Flotsam', '漂浮子域'),
    ('Flowing', '流动子域'),
    ('Fortifications', '碉堡子域'),
    ('Friendship', '友谊子域'),
    ('Imagination', '想象子域'),
    ('Industry', '工厂子域'),
    ('Innuendo', '影射子域'),
    ('Isolation', '孤寂子域'),
    ('Judgment', '审判子域'),
    ('Kyton', '链魔子域'),
    ('Legislation', '法律子域'),
    ('Loyalty', '忠诚领域'),
    ('Moon', '月子域'),
    ('Plague', '瘟疫子域'),
    ('Psychopomp', '招魂者子域'),
    ('Radiation', '辐射子域'),
    ('Redemption', '救赎子域'),
    ('Revelation', '启示子域'),
    ('Revelry', '狂欢子域'),
    ('Riot', '暴动子域'),
    ('Rivers', '河流子域'),
    ('Saurian', '蜥类子域'),
    ('Shadow', '阴影子域'),
    ('Slavery', '奴役子域'),
    ('Solitude', '孤独子域'),
    ('Stars', '星子域'),
    ('Torture', '折磨子域'),
    ('Trap', '陷阱子域'),
    ('Tyranny', '暴政子域'),
    ('Venom', '毒液子域'),
    ('Whimsy', '滑稽子域')
]

# 血统补全 Accursed,5 Accursed.6 Accursed,7 Accursed,8 Accursed,9 Aquatic,5 Aquatic,6 Boreal,1 Boreal,2 Boreal,4 Boreal,6 Boreal,7 Boreal,8 Boreal,9 Div,1 Div,2 Div,3 Div,4 Div,6 Div,7 Div,8 Div,9 Djinni,1 Djinni,2 Djinni,3 Djinni,4 Djinni,5 Djinni,6 Djinni,7 Djinni,8 Djinni,9 Draconic,2 Draconic,3 Draconic,9 Dreamspun,1 Dreamspun,2 Dreamspun,3 Dreamspun,4 Dreamspun,5 Dreamspun,6 Dreamspun,7 Dreamspun,8 Dreamspun,9 Ectoplasm,1 Ectoplasm,4 Ectoplasm,6 Ectoplasm,9 Efreeti,1 Efreeti,2 Efreeti,3 Efreeti,4 Efreeti,6 Efreeti,7 Efreeti,9 Elemental,2 Elemental,3 Fey,3 Fey,6 Ghoul,1 Ghoul,3Ghoul,9 Harrow,2 Harrow,3 Harrow,4 Harrow,6 Harrow,7 Harrow,8 Harrow,9 Imperious,2 Imperious,3 Imperious,5 Imperious,6 Impossible,1 Impossible,2 Impossible,3 Impossible,4 Impossible,5 Impossible,6 Impossible,7 Impossible,8 Impossible,9 Infernal,2 Infernal,6 Infernal,7 Infernal,8 Infernal,9 Kobold,3 Kobold,6 Kobold,7 Maestro,1 Maestro,2 Maestro,3 Maestro,4 Maestro,5 Maestro,6 Maestro,7 Maestro,8 Maestro,9 Marid,1 Marid,2 Marid,3 Marid,4 Marid,6 Marid,7 Marid,8 Marid,9 Nanite,1 Nanite,3 Nanite,7 Nanite,8Orc,6 Orc,7 Orc,8 Orc,9 Pestilence,2 Pestilence,3 Pestilence,4 Pestilence,5 Pestilence,6 Pestilence,7 Pestilence,8 Pestilence,9 Psychic,7 Rakshasa,1 Rakshasa,2 Rakshasa,3 Rakshasa,4 Rakshasa,5 Rakshasa,6 Rakshasa,7 Rakshasa.8 Rakshasa,9 Serpentine,1 Serpentine,2 Serpentine,3 Serpentine,4 Serpentine,5 Serpentine,6 Serpentine,8 Serpentine,9 Shadow,1 Shadow,2 Shadow,3 Shadow,4 Shadow,5 Shadow,6 Shadow,7 Shadow,8 Shaitan,1 Shaitan,2 Shaitan,3 Shaitan,4 Shaitan,5 Shaitan,6 Shaitan,7 Shaitan,8 Shaitan,9 Starsoul,1 Starsoul,2 Starsoul,3 Starsoul,4 Starsoul,5 Starsoul,6 Starsoul,7 Starsoul,8 Starsoul,9 Stormborn,1 Stormborn,2
spell_bloodline_extra = [
    ('Accursed', '咒怨血统'),
    ('Aquatic', '深洋血统'),
    ('Boreal', '极寒血统'),
    ('Div', '妖灵血统'),
    ('Djinni', '风灵血统'),
    ('Draconic', '龙脉血统'),
    ('Dreamspun', '梦见血统'),
    ('Ectoplasm', '灵质血统'),
    ('Efreeti', '火灵血统'),
    ('Elemental', '元素血统'),
    ('Fey', '精类血统'),
    ('Ghoul', '尸鬼血统'),
    ('Harrow', '哈罗血统'),
    ('Imperious', '帝王血统'),
    ('Impossible', '源数血统'),
    ('Infernal', '地狱血统'),
    ('Kobold', '狗头人术士血统'),
    ('Maestro', 'Maestro血统'),
    ('Marid', '水灵血统'),
    ('Nanite', '纳米血统'),
    ('Orc', '兽人血统'),
    ('Pestilence', '疫病血统'),
    ('Psychic', '心灵血统'),
    ('Rakshasa', '罗刹血统'),
    ('Serpentine', '古蛇血统'),
    ('Shadow', '暗影血统'),
    ('Shaitan', '土灵血统'),
    ('Starsoul', '星魄血统'),
    ('Stormborn', '暴风血统'),
    ('Verdant', '苍翠血统')]

# 基础中英映射
tran_dic = [
    # ('castingTime', 'castingTime_zh',),
    ('components', 'components_zh', 'materials'),
    # ('range', 'range_zh'),
    ('target', 'target_zh', 'effect'),
    ('duration', 'duration_zh'),
    ('savingThrow', 'savingThrow_zh'),
    # ('spellResistance', 'spellResistance_zh')
]

for traned_spell in traned_spell_data:
    traned_spell['name'] = re.sub(
        r'\s?\(.*?\)|\s?（.*?）', '', traned_spell['name'])
    if traned_spell['name'] in fvtt_data['entries']:
        name_en = traned_spell['name']
        # 存在翻译在进行操作
        if traned_spell.get('name_zh'):
            # 改名字
            fvtt_data['entries'][name_en]['name'] = traned_spell['name_zh'] + \
                f' ({name_en})'
            # VSM材料
            if fvtt_data['entries'][name_en].get('materials') and fvtt_data['entries'][name_en].get('materials') != '' and traned_spell.get('components_zh'):
                fvtt_data['entries'][name_en]['materials'] = traned_spell['components_zh'].replace(
                    '语言', '').replace('姿势', '').replace(',', '').replace(' ', '').replace('，', '').replace('材料', '').replace('（', '').replace('）', '').replace("\(", '').replace('\)', '').replace('、', '').replace('/', '')
            # 施法目标，如果目标是空的，就是得填进效果
            if fvtt_data['entries'][name_en].get('target') and fvtt_data['entries'][name_en].get('target') != '':
                fvtt_data['entries'][name_en]['target'] = traned_spell.get(
                    'target_zh', '')
            elif fvtt_data['entries'][name_en].get('effect') and fvtt_data['entries'][name_en].get('effect') != '':
                fvtt_data['entries'][name_en]['effect'] = traned_spell.get(
                    'effect_zh', fvtt_data['entries'][name_en]['effect'])
            else:
                pass

            # 豁免
            if fvtt_data['entries'][name_en].get('savingThrow'):
                fvtt_data['entries'][name_en]['savingThrow'] = traned_spell.get(
                    'savingThrow_zh', fvtt_data['entries'][name_en]['savingThrow'])
            # 持续时间
            if fvtt_data['entries'][name_en].get('duration'):
                fvtt_data['entries'][name_en]['duration'] = traned_spell['duration_zh']

            # 补全法术描述符翻译
            if fvtt_data['entries'][name_en].get('type'):
                # 对这个字符串遍历字典spell_type_extra，如果找到了就替换
                for key, value in spell_type_extra:
                    fvtt_data['entries'][name_en]['type'] = fvtt_data['entries'][name_en]['type'].replace(
                        key, value)

            # 补全法术学派subschool翻译
            if fvtt_data['entries'][name_en].get('subschool'):
                for key, value in spell_subschool_extra:
                    fvtt_data['entries'][name_en]['subschool'] = fvtt_data['entries'][name_en]['subschool'].replace(
                        key, value)
            # 遍历领域domain翻译
            if fvtt_data['entries'][name_en].get('domain'):
                for i in range(len(fvtt_data['entries'][name_en]['domain'])):
                    if isinstance(fvtt_data['entries'][name_en]['domain'][i], list):
                        for j in range(len(fvtt_data['entries'][name_en]['domain'][i])):
                            for key, value in spell_domain_extra:
                                fvtt_data['entries'][name_en]['domain'][i][j] = str(fvtt_data['entries'][name_en]['domain'][i][j]).replace(
                                    str(key), str(value))
                    else:
                        for key, value in spell_domain_extra:
                            fvtt_data['entries'][name_en]['domain'][i] = str(fvtt_data['entries'][name_en]['domain'][i]).replace(
                                str(key), str(value))

            # 然后是子领域subdomain
            if fvtt_data['entries'][name_en].get('subDomain'):
                for i in range(len(fvtt_data['entries'][name_en]['subDomain'])):
                    if isinstance(fvtt_data['entries'][name_en]['subDomain'][i], list):
                        for j in range(len(fvtt_data['entries'][name_en]['subDomain'][i])):
                            for key, value in spell_subdomain_extra:
                                fvtt_data['entries'][name_en]['subDomain'][i][j] = str(fvtt_data['entries'][name_en]['subDomain'][i][j]).replace(
                                    str(key), str(value))
                    else:
                        for key, value in spell_subdomain_extra:
                            fvtt_data['entries'][name_en]['subDomain'][i] = str(fvtt_data['entries'][name_en]['subDomain'][i]).replace(
                                str(key), str(value))
            # 还有血脉bloodline
            if fvtt_data['entries'][name_en].get('bloodline'):
                for i in range(len(fvtt_data['entries'][name_en]['bloodline'])):
                    if isinstance(fvtt_data['entries'][name_en]['bloodline'][i], list):
                        for j in range(len(fvtt_data['entries'][name_en]['bloodline'][i])):
                            for key, value in spell_bloodline_extra:
                                fvtt_data['entries'][name_en]['bloodline'][i][j] = str(fvtt_data['entries'][name_en]['bloodline'][i][j]).replace(
                                    str(key), str(value))
                    else:
                        for key, value in spell_bloodline_extra:
                            fvtt_data['entries'][name_en]['bloodline'][i] = str(fvtt_data['entries'][name_en]['bloodline'][i]).replace(
                                str(key), str(value))
                # 拼接法术正文
            content_parts = []
            for field, label in spell_extra:
                if traned_spell.get(field):
                    if field == 'text_zh':
                        content_parts.append(traned_spell['text_zh'])
                    elif field == 'source':
                        source_t = ''.join(traned_spell[field]).replace(
                            "'", "").replace('[', '').replace(']', '')
                        content_parts.append(f"<b>{label}</b>{source_t}")
                    else:
                        content_parts.append(
                            f"<b>{label}</b>{traned_spell[field]}")
            # 法术的神话版本描述
            if traned_spell.get('mythicText_zh'):
                content_parts.append(
                    f"<br></br><b>神话版本</b>")
                for field, label in sepll_myth_extar:
                    if traned_spell.get(field):
                        if field == 'mythicText_zh':
                            content_parts.append(traned_spell['mythicText_zh'])
                        elif field == 'mythicSource':
                            source_t = ''.join(traned_spell[field]).replace(
                                "'", "").replace('[', '').replace(']', '')
                            content_parts.append(
                                f"<b>{label}</b>{source_t}")
                        else:
                            content_parts.append(
                                f"<b>{label}</b>{traned_spell[field]}")
            content = '<br/><br/>'.join(content_parts)
            # 重新赋值
            fvtt_data['entries'][name_en]['shortDescription'] = content

with open('pf1.spells.json', 'w', encoding='utf-8') as f:
    json.dump(fvtt_data, f, ensure_ascii=False, indent=4)
