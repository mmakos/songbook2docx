from setuptools import setup

setup(
    name='songbook2docx',
    version='1.1',
    packages=['songbook2docx', 'songbook2docx.utils', 'songbook2docx.styled'],
    url='https://spiewnik.mmakos.pl',
    license='',
    author='Michał Makoś',
    author_email='mmakos.pl@gmail.com',
    description='Tool for converting songbook online to docx',
    install_requires=['python-docx>=0.8.11', 'fonttools>=4.34.4', 'pyinstaller>=5.11.0']
)
