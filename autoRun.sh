#!/bin/bash

mysqldb()
{
    python3 mysqldb.py
}

until mysqldb; do
    {
        echo "'mysqldb.py' script has been crashed with exit code $?.....Restarting" >&2
        sleep 1
    }

done
