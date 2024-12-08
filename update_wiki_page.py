import re
import os
from datetime import datetime

# 指定文件名（对应 Wiki 页面内容的 Markdown 文件）
page_file = "直翻通道.md"

# 拉取的 Wiki 页面路径
wiki_path = os.path.join(os.getcwd(), page_file)

# 检查文件是否存在
if not os.path.exists(wiki_path):
    raise FileNotFoundError(f"{page_file} 不存在，请检查路径。")

# 读取页面内容
with open(wiki_path, "r", encoding="utf-8") as file:
    content = file.read()

# 定义更新二级域名的函数
def increment_domain(match):
    base = match.group(1)
    num = int(match.group(2)) + 1  # 数字加 1
    suffix = match.group(3)
    return f"{base}{num}{suffix}"

# 更新内容：匹配 fan29.113513.xyz 和 fan13.420820.xyz
updated_content = re.sub(r"(fan)(\d+)(\.113513\.xyz)", increment_domain, content)
updated_content = re.sub(r"(fan)(\d+)(\.420820\.xyz)", increment_domain, updated_content)

# 添加更新时间
updated_content = re.sub(
    r"北京时间\d{4}年\d{1,2}月\d{1,2}日\d{2}点\d{2}分更新",
    f"北京时间{datetime.now().strftime('%Y年%m月%d日%H点%M分')}更新",
    updated_content
)

# 将更新后的内容写回文件
with open(wiki_path, "w", encoding="utf-8") as file:
    file.write(updated_content)

print("Wiki 页面内容已更新。")
