#!/usr/bin/env python
import os

def check_virtual_env():
    try:
        virtual_env = os.environ['VIRTUAL_ENV']
        print(f"Your current virtual env is {virtual_env}")
    except KeyError:
        print("No virtual environment is currently active")

if __name__ == "__main__":
    check_virtual_env()

# python3 -m venv <name> - создание виртиальной среды
# source <name>/bin/activate - активация в.с.
# deactivate - деактивация в.с.