from setuptools import setup

setup(name='qrcgen', 
        version = '0.2', 
        author = 'Flavio Codeco Coelho', 
        author_email = 'fccoelho@gmail.com', 
        url = 'http://github.com/fccoelho/qrcgen',
        description = 'Automated generator of Qt resource files (*.qrc), by recursive scanning of directory trees',
        zip_safe = True,
        py_modules = ['qrcgen'],
        scripts = ['qrcgen.py'],
        license = 'GPLv3',  
      )
