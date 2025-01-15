git status
timeout /t 3
git add .
timeout /t 3
rem git commit -m "Actualizacion automatica - $(date +'%Y-%m-%d %H:%M:%S')"
for /f "tokens=*" %%A in ('powershell -command "Get-Date -Format yyyy-MM-dd HH:mm:ss"') do git commit -m "Actualizacion automatica - %%A"
timeout /t 10
git push

