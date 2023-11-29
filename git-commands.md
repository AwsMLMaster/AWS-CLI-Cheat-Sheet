## Git Commands
1. update a local repository with changes from a hosting server GitHub repository   
   ```git clone <remote-url>```   
   ```git pull origin <branch-name>```
2. if you want to check how many changes your local repo is behind the remote   
   ```git fetch origin master```
3. in case no important changes were made on the local repo, just reset the local repo from the remote   
   ```git reset --hard origin/master```
5. create python virtual environment   
   ```python3 -m venv .venv```
6. start python virtual environment   
   ```source .venv/bin/activate```
7. got ModuleNotFoundError: No module named 'six' ???   
   Solution: ```pip install --upgrade git-remote-codecommit```
9. 
