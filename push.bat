git status
timeout /t 3
git add .
timeout /t 3
git commit -m "Actualización automática - $(date +'%Y-%m-%d %H:%M:%S')"
timeout /t 10
git push

