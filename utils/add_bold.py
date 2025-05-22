from glob import glob

in_path_s = glob('content/publication/*/index.md')

for in_path in in_path_s:
    content = open(in_path).read()
    content = content.replace("- Yu Wang*", "- Yu Wang")
    content = content.replace("- Yu Wang", "- admin")
    content = content.replace("- admin", "- Yu Wang*")
    with open(in_path, 'w', encoding='utf-8') as f:
        f.write(content)
