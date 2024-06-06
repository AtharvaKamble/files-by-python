import os

def clean_dir_name(_dir):
    names = os.listdir(_dir)
    for d in names:
        name_split = d.split(' ')
        if len(name_split) <= 1: continue
        source = f'{_dir}/{d}'
        
        if '.md' in source:
            dest = f"{_dir}/{' '.join(name_split[:-1])}.md"
        else:
            dest = f"{_dir}/{' '.join(name_split[:-1])}"

        os.rename(source, dest)

def prepend_to_file(_dir):
    names = os.listdir(_dir)

    for file_name in names:
        if '.md' not in file_name: continue

        f_path = f'{_dir}/{file_name}'
        new_f_path = f'{_dir}/yeeh.md'
        title = 'some title yeeter'

        new_prepend_data = f'---\ntitle: {title}\ntags:\n\t- medium\n---'
        file_cache = ''

        with open(f_path, encoding='utf-8') as f:
            file_cache += f.read()

        with open(f_path, 'w', encoding='utf-8') as f:
            f.write(new_prepend_data + '\n' + file_cache)
        

        


# clean_dir_name('../../Downloads/lc/Leetcode w me')
prepend_to_file('.')

