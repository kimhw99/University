@echo off
call env\Scripts\activate
cd aim5005-main
pytest -s --color=yes
cmd /k