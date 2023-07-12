#!/bin/bash

tmux kill-server
cd ./MLH_portfolio_alfonso
git fetch && git reset origin/main --hard
pwd
source python3-virtualenv/bin/activate && pip install -r requirements.txt && deactivate && echo "\n\n\n"
tmux new -s portfolio -d # Create a new session but dont attach to it
tmux send-keys -t portfolio 'source python3-virtualenv/bin/activate' C-m
tmux send-keys -t portfolio 'flask run --host 0.0.0.0' C-m
tmux attach -t portfolio
