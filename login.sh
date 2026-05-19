#!/usr/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd $SCRIPT_DIR && /home/cdy/.venv/bin/python $SCRIPT_DIR/login.py --username=[your username] --passwd=[your password] --login_host=[your login host]

