import re
import os
from datetime import datetime

# 指定目标 Wiki 文件的路径（在 wiki 目录下）
wiki_file = os.path.join("wiki", "直翻通道.md")

# 检查文件是否存在
if not os.path.exists(wiki_file):
    raise FileNotFoundError(f"{wiki_file} 不存在，请检查路径。")

# 读取页面内容
with open(wiki_file, "r", encoding="utf-8") as file:
    content = file.read()

# 正则匹配并递增二级域名数字
def increment_domain(match):
    base = match.group(1)
    num = int(match.group(2)) + 1
    suffix = match.group(3)
    return f"{base}{num}{suffix}"

# 更新内容
updated_content = re.sub(r"(fan)(\d+)(\.113513\.xyz)", increment_domain, content)
updated_content = re.sub(r"(fan)(\d+)(\.420820\.xyz)", increment_domain, updated_content)

# 添加更新时间
updated_content = re.sub(
    r"北京时间\d{4}年\d{1,2}月\d{1,2}日\d{2}点\d{2}分更新",
    f"北京时间{datetime.now().strftime('%Y年%m月%d日%H点%M分')}更新",
    updated_content
)

# 将更新后的内容写回文件
with open(wiki_file, "w", encoding="utf-8") as file:
    file.write(updated_content)

print("Wiki 页面内容已更新。")
