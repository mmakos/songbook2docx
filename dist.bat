@echo off

del "installer\Songbook2docx.exe"
@RD /S /Q "dist"
pip install .
@RD /S /Q "songbook2docx.egg-info"
pyinstaller main.spec
@RD /S /Q "build"

mkdir "dist/fonts"
copy "conf.ini" "dist/conf.ini"

"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" "installer\setup.iss"