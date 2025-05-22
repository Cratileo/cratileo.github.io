from glob import glob

in_path_s = glob('content/publication/*/index.md')

for in_path in in_path_s:
    content = open(in_path).read()
    if 'arXiv' in content:
        content = content.replace("- article-journal", "- article")
    with open(in_path, 'w', encoding='utf-8') as f:
        f.write(content)
