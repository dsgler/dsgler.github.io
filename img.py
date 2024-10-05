import os
import re

def replace_text_in_md_files(directory):
    # 定义需要替换的文本和替换后的文本
    pattern = re.compile(r'!\[\[(.*?)\]\]')
    replacement = r'![](\1)'

    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as md_file:
                    content = md_file.read()

                # 替换文本
                new_content = re.sub(pattern, replacement, content)

                # 将新内容写回文件
                with open(file_path, 'w', encoding='utf-8') as md_file:
                    md_file.write(new_content)
                print(f'Updated: {file_path}')

# 调用函数，替换指定文件夹下所有.md文件中的文本
for dirpath, dirnames, filenames in os.walk('./'):
    for dirname in dirnames:
        replace_text_in_md_files(dirname)
