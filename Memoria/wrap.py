import os
import glob
import re

def wrap_text(text, max_len=110):
    lines = text.split('\n')
    new_lines = []
    for line in lines:
        if len(line) <= max_len or re.search(r'(?<!\\\\)%', line):
            new_lines.append(line)
        else:
            curr_line = line
            while len(curr_line) > max_len:
                split_idx = curr_line.rfind(' ', 0, max_len)
                if split_idx == -1:
                    split_idx = curr_line.find(' ', max_len)
                    if split_idx == -1:
                        break
                new_lines.append(curr_line[:split_idx])
                curr_line = curr_line[split_idx+1:]
            if curr_line:
                new_lines.append(curr_line)
    return '\n'.join(new_lines)

files = glob.glob('source/*.tex') + ['main.tex']
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = wrap_text(content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Wrapped: {f}")
print("Done")
