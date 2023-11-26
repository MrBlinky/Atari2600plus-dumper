@echo off
pushd "%~dp0"
Path = %CD%\Python;%CD%\Python\Scripts;%PATH%
python.exe dump2600p.py %*
popd
