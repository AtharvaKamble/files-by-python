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

        title = file_name.replace('.md', '')

        new_prepend_data = f'---\ntitle: {title}\ntags:\n' + ' ' * 4 + '- medium\n---'
        file_cache = ''

        with open(f_path, encoding='utf-8') as f:
            file_cache += f.read()

        with open(f_path, 'w', encoding='utf-8') as f:
            f.write(new_prepend_data + '\n' + file_cache)
        
def remove_prepend_data(_dir):
    names = os.listdir(_dir)

    for file_name in names:
        if '.md' not in file_name: continue

        f_path = f'{_dir}/{file_name}'

        title = file_name.replace('.md', '')

        # confirm this data with the above function
        # new_prepend_data = f'---\ntitle: {title}\ntags:\n    - medium\n---'
        new_prepend_data = f'---\ntitle: {title}\ntags:\n' + ' ' * 4 + '- medium\n---'

        file_cache = ''

        with open(f_path, encoding='utf-8') as f:
            file_cache += f.read()

        file_cache = file_cache.replace(new_prepend_data, '')

        with open(f_path, 'w', encoding='utf-8') as f:
            f.write(file_cache)
        

def remove_markdown_title(_dir):
    names = os.listdir(_dir)

    for file_name in names:
        if '.md' not in file_name: continue

        f_path = f'{_dir}/{file_name}'

        title = file_name.split(' ')
        to_replace = f"# {title[0]}. {' '.join(title[1:]).replace('.md', '')}\n"

        file_cache = ''

        with open(f_path, encoding='utf-8') as f:
             file_cache += f.read()

        if to_replace in file_cache:
            file_cache = file_cache.replace(to_replace, '')

            with open(f_path, 'w', encoding='utf-8') as f:
                f.write(file_cache)



dir_you_want_to_clean = ''

# uncomment function to use

# use to remove the last word in a file directory name
# clean_dir_name(dir_you_want_to_clean)

# prepend the file with the metadata for quartz 4 to recognize it as a valid markdown file
# prepend_to_file(dir_you_want_to_clean)

# remove the prepended data that was attached by the above function
# remove_prepend_data(dir_you_want_to_clean)

# remove the markdown title that matches perfectly with the title of the file
# remove_markdown_title(dir_you_want_to_clean)
