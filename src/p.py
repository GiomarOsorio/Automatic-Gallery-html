from os import listdir
from bs4 import BeautifulSoup

MESSAGE = 'This script is designed by Giomar Osorio so that it automatically adds gallery to the html, according to a specific structure in the files. to see more go to:'
PROJECTS_FOLDER = "images/projects/"

def get_template_html(template_name):
    template = None
    try:
        with open(template_name) as fp:
            template = BeautifulSoup(fp, 'html.parser')
    except FileNotFoundError:
        pass
    return template

def create_element(element_tag, **attrs):
    element_string = '<{}></{}>'.format(element_tag, element_tag)
    element = BeautifulSoup(element_string, 'html.parser')
    if attrs is not None:
        tag = element.find(element_tag)
        for attr, attr_value in attrs.items():
            tag[attr[1:]] = attr_value
    return element

def get_projects_folder():
    folders = []
    try:
        folders = listdir(PROJECTS_FOLDER)
        folders.sort()
    except folders.FileNotFoundError:
        pass
    return folders

def get_files(folder):
    files = []
    try:
        files = listdir(folder)
        files.sort()
    except files.FileNotFoundError:
        pass
    return files

def path_join(parent, children):
    return '{}{}/'.format(parent, children)

def safe_string(text):
    return text.replace(' ', '-')

def get_first_filepath_from_gallery(gallery):
    return gallery.find('article').find('a')['href']

def create_article(folder_path, file, data_id):
    path = file[1] if folder_path is None else '{}{}'.format(folder_path, file)
    file_name = file[1].split('/')[len(file[1].split('/'))-1].split('.')[0] if folder_path is None else file.split('.')[0]
    file_name = file_name.split('-')[1] if '-' in file_name else file_name

    img_element = create_element('img', _src=path, _title=file_name, _alt='image {}'.format(file_name))

    if folder_path is None:
        a_element = create_element('a', _label='#{}'.format(safe_string(file_name)), _class='image fit pointer')
        p_element = create_element('p')
        p_element.p.string = 'Proyecto: {}'.format(file[0].split('/')[len(file[0].split('/'))-2].split('-')[1])
    else:
        a_element = create_element('a', _id='{}'.format(safe_string(file_name)), _href=path, _class='image fit')
    a_element.a.append(img_element)

    if data_id%2!=0:
        article_element = create_element('article', _class='from-left', _data_id=data_id)
    else:
        article_element = create_element('article', _class='from-right', _data_id=data_id)
    article_element.article.append(a_element)

    if folder_path is None:
        article_element.article.append(p_element)

    return article_element

def create_gallery(folder_path, folder_name, files=None, **attrs):
    files_in_folder = get_files(folder_path) if files is None else files
    if files_in_folder:
        files_in_folder_index = [index+1 for index in range(len(files_in_folder))]
        gallery_element = create_element('div', **attrs)
        for file,data_id in zip(files_in_folder,files_in_folder_index):
            if files is not None:
                gallery_element.div.append(create_article(None,(file, files[file]), data_id))
                continue
            gallery_element.div.append(create_article(folder_path,file, data_id))
        return gallery_element
    else:
        return None

def create_galleries(template_name, output_name):
    files = {}
    gallery_list = []

    index_html = get_template_html('{}.html'.format(template_name))
    if index_html is None:
        return False
    div_content = index_html.find(id='work').find('div')
    folders = get_projects_folder()

    for folder in folders:
        gallery_temp = create_gallery(path_join(PROJECTS_FOLDER,folder), folder, _id=folder, _class='gallery-hide')
        if gallery_temp:
            gallery_list.append(gallery_temp)
            files[folder]= get_first_filepath_from_gallery(gallery_temp)

    gallery_list.insert(0, create_gallery(None, None, files, _class='gallery'))
    for gallery in gallery_list:
        div_content.append(gallery)

    with open('{}.html'.format(output_name), 'w') as file:
        file.write(str(index_html.prettify()))

    return True

def main():
    print(MESSAGE)
    template_name = input('Enter the template file name (without the extension): ')
    output_name = input('Enter the output file name (without the extension): ')
    if create_galleries(template_name, output_name):
        print('modification completed!')
    else:
        print('There is no file with the name "{}"'.format(template_name))

if __name__ == '__main__':
    main()
