echo "======== update... all folders ======== "
git init
git add .
curTime = date -d ˇ°$currentTimeˇ± +%s 
git commit -m curTime
git push origin master  
read -p "Press any key to continue." var