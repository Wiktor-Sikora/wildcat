# Project Wildcat
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Wildcat is project created for [Platynowy indeks contest 2023](https://tu.kielce.pl/platynowy-indeks-2023/)

## To lounch dev server

1. clone the repository
   `git clone https://github.com/Wiktor-Sikora/wildcat.git`
2. create python virtual enviroment and install dependencies
   ```bash
   python -m venv venv
   venv\Scripts\activate.bat # windows
   source venv/bin/activate # linux

   pip install -r requirments/local.txt
   ```
3. make migrations
   ```bash
   cd wildcat
   python manage.py makemigrations
   python manage.py migrate
   ```
