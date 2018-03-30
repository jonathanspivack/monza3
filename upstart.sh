#!/usr/bin/env bash

#setup
#rm -rf run/instance
#rm run/datastore/master.db
python3 setup/schema.py
python3 setup/seed.py
#python3 setup/something.py

#runtime
python3 setup/generate.py
python3 run/wsgi.py &


#cleanup
#rm -rf run/core/__pychache__
#rm -rf run/core/controllers/__pychache__




