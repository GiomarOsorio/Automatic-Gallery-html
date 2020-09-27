# Automatic Gallery

A simple script that allows adding html content, specifically a gallery, tested only with the [HTML5 UP](https://html5up.net/) template.

This script creates multiple galleries, the main one is always visible, the secondary ones are not.

The main gallery is made up of the first image of each of the secondary libraries, when you click on it you will begin to see each of the images that make up the linked secondary gallery.

To achieve this, the main.css and main.js files of the original files that provide [HTML5 UP](https://html5up.net/) have also been modified, so it is advisable to replace these files, the template.html file is also provided as a convenience, it is nothing more than the original file without the html segment containing the 'gallery' class.

## Getting Started 🚀

### Prerequisites 📋

The following list describes the dependencies used during the development of the project.

```
appdirs==1.4.4
asgiref==3.2.10
astroid==2.4.2
attrs==19.3.0
beautifulsoup4==4.9.1
black==19.10b0
click==7.1.2
Django==3.0.8
isort==5.0.3
lazy-object-proxy==1.5.0
mccabe==0.6.1
pathspec==0.8.0
Pillow==7.2.0
pylint==2.5.3
pytz==2020.1
regex==2020.6.8
six==1.15.0
soupsieve==2.0.1
sqlparse==0.3.1
toml==0.10.1
typed==0.6
typed-ast==1.4.1
wrapt==1.12.1
```

You must download the original files provided by [HTML5 UP](https://html5up.net/) from its web portal: [template](https://html5up.net/big-picture)

Unzip the downloaded file, find the files main.css, main.js and folders fulls and thumbs, delete them

If your file tree looks like this, skip to the next part.

```bash
├── LICENSE.txt
├── README.txt
├── assets
│   ├── css
│   │   ├── fontawesome-all.min.css
│   │   ├── images
│   │   │   ├── arrow.svg
│   │   │   ├── dark-arrow.svg
│   │   │   ├── overlay.png
│   │   │   ├── poptrox-closer.svg
│   │   │   └── poptrox-nav.svg
│   │   └── noscript.css
│   ├── js
│   │   ├── breakpoints.min.js
│   │   ├── browser.min.js
│   │   ├── jquery.min.js
│   │   ├── jquery.poptrox.min.js
│   │   ├── jquery.scrollex.min.js
│   │   ├── jquery.scrolly.min.js
│   │   └── util.js
│   ├── sass
│   │   ├── base
│   │   │   ├── _page.scss
│   │   │   ├── _reset.scss
│   │   │   └── _typography.scss
│   │   ├── components
│   │   │   ├── _actions.scss
│   │   │   ├── _box.scss
│   │   │   ├── _button.scss
│   │   │   ├── _form.scss
│   │   │   ├── _gallery.scss
│   │   │   ├── _icon.scss
│   │   │   ├── _icons.scss
│   │   │   ├── _image.scss
│   │   │   ├── _list.scss
│   │   │   ├── _poptrox-popup.scss
│   │   │   ├── _section.scss
│   │   │   └── _table.scss
│   │   ├── layout
│   │   │   ├── _footer.scss
│   │   │   ├── _header.scss
│   │   │   └── _main.scss
│   │   ├── libs
│   │   │   ├── _breakpoints.scss
│   │   │   ├── _functions.scss
│   │   │   ├── _mixins.scss
│   │   │   ├── _vars.scss
│   │   │   └── _vendor.scss
│   │   ├── main.scss
│   │   └── noscript.scss
│   └── webfonts
│       ├── fa-brands-400.eot
│       ├── fa-brands-400.svg
│       ├── fa-brands-400.ttf
│       ├── fa-brands-400.woff
│       ├── fa-brands-400.woff2
│       ├── fa-regular-400.eot
│       ├── fa-regular-400.svg
│       ├── fa-regular-400.ttf
│       ├── fa-regular-400.woff
│       ├── fa-regular-400.woff2
│       ├── fa-solid-900.eot
│       ├── fa-solid-900.svg
│       ├── fa-solid-900.ttf
│       ├── fa-solid-900.woff
│       └── fa-solid-900.woff2
├── images
│   ├── intro.jpg
│   ├── one.jpg
│   └── two.jpg
└── index.html
```

### Installing 🔧

Copy this repo in your local machine with:

```
git clone https://github.com/GiomarOsorio/Automatic-Gallery-html
```

always you can donwload a zip: [Automatic Gallery HTML](https://github.com/GiomarOsorio/Automatic-Gallery-html/archive/master.zip)

move to folder project and install dependencies (only if you want use virtualenv):

```
pip install -r requirements.txt
```

copy all the files from the folder modified in the previous step and paste it inside the src folder, the file tree should look like this:

```bash
├── LICENSE.txt
├── README.txt
├── assets
│   ├── css
│   │   ├── fontawesome-all.min.css
│   │   ├── images
│   │   │   ├── arrow.svg
│   │   │   ├── dark-arrow.svg
│   │   │   ├── overlay.png
│   │   │   ├── poptrox-closer.svg
│   │   │   └── poptrox-nav.svg
│   │   ├── main.css
│   │   └── noscript.css
│   ├── js
│   │   ├── breakpoints.min.js
│   │   ├── browser.min.js
│   │   ├── jquery.min.js
│   │   ├── jquery.poptrox.min.js
│   │   ├── jquery.scrollex.min.js
│   │   ├── jquery.scrolly.min.js
│   │   ├── main.js
│   │   └── util.js
│   ├── sass
│   │   ├── base
│   │   │   ├── _page.scss
│   │   │   ├── _reset.scss
│   │   │   └── _typography.scss
│   │   ├── components
│   │   │   ├── _actions.scss
│   │   │   ├── _box.scss
│   │   │   ├── _button.scss
│   │   │   ├── _form.scss
│   │   │   ├── _gallery.scss
│   │   │   ├── _icon.scss
│   │   │   ├── _icons.scss
│   │   │   ├── _image.scss
│   │   │   ├── _list.scss
│   │   │   ├── _poptrox-popup.scss
│   │   │   ├── _section.scss
│   │   │   └── _table.scss
│   │   ├── layout
│   │   │   ├── _footer.scss
│   │   │   ├── _header.scss
│   │   │   └── _main.scss
│   │   ├── libs
│   │   │   ├── _breakpoints.scss
│   │   │   ├── _functions.scss
│   │   │   ├── _mixins.scss
│   │   │   ├── _vars.scss
│   │   │   └── _vendor.scss
│   │   ├── main.scss
│   │   └── noscript.scss
│   └── webfonts
│       ├── fa-brands-400.eot
│       ├── fa-brands-400.svg
│       ├── fa-brands-400.ttf
│       ├── fa-brands-400.woff
│       ├── fa-brands-400.woff2
│       ├── fa-regular-400.eot
│       ├── fa-regular-400.svg
│       ├── fa-regular-400.ttf
│       ├── fa-regular-400.woff
│       ├── fa-regular-400.woff2
│       ├── fa-solid-900.eot
│       ├── fa-solid-900.svg
│       ├── fa-solid-900.ttf
│       ├── fa-solid-900.woff
│       └── fa-solid-900.woff2
├── images
│   ├── intro.jpg
│   ├── one.jpg
│   └── two.jpg
├── index.html
├── p.py
└── template.html
```

### How to use it 📦

for the script to work properly, the images must be added inside the 'images/projects' folder, if it does not exist you must create it.

```bash
├── images
│   ├── intro.jpg
│   ├── one.jpg
│   ├── projects
│   │   ├── 1-project one
│   │   │   ├── 1-img.png
│   │   │   ├── 2-img.png
│   │   │   ├── 3-img.png
│   │   │   ├── 4-img.png
│   │   │   └── 5-img.png
│   │   └── 2-project two
│   │       ├── 1-img.png
│   │       ├── 10-img.png
│   │       ├── 11-img.png
│   │       ├── 12-img.png
│   │       ├── 13-img.png
│   │       ├── 14-img.png
│   │       ├── 15-img.png
│   │       ├── 2-img.png
│   │       ├── 3-img.png
│   │       ├── 4-img.png
│   │       ├── 5-img.png
│   │       ├── 6-img.png
│   │       ├── 7-img.png
│   │       ├── 8-img.png
│   │       └── 9-img.png
│   └── two.jpg
```

Note that both the folders and the image files have their names preceded by '(number) -', this is so to assign the order of appearance of the files in the galleries.

___Important:___ the file name will be the same shown in the gallery (without the extension).

Run the script from a terminal, it should supply the name of the template and the output file, ignoring the extension.


![](/images/home-screen.png?raw=true)

## Built With 🛠️

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Python package


## Authors ✒️

* **Giomar Osorio** - *Initial work* - [GiomarOsorio](https://github.com/GiomarOsorio)

## License 📄

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

