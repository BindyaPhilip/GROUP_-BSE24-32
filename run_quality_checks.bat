@echo off
echo Running code quality checks...

rem Run Black
black .

rem Run Flake8
flake8 .

echo Code quality checks completed.
pause
