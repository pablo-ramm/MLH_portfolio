#!/bin/sh
tmux kill-server
cd MLH_portfolio/
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new
source python3-virtualenv/bin/activate
flask run --host=0.0.0.0
