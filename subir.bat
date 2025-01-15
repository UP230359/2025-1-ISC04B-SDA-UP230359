git status
timeout /t 3
git add .
timeout /t 3
git commit -m "Actualizacion automatica - $(date +'%Y-%m-%d %H:%M:%S')"
timeout /t 10
git push

