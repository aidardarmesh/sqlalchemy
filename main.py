import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from core import create_tables


create_tables()
