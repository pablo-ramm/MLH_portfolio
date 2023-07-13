#!/bin/bash

systemctl stop myportfolio
cd /home/MLH_portfolio_alfonso
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate && pip install -r requirements.txt && deactivate
systemctl restart myportfolio
