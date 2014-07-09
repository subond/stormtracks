import os

# expandvars expands e.g. $HOME
DATA_DIR = os.path.expandvars('$HOME/stormtracks/data')
OUTPUT_DIR = os.path.expandvars('$HOME/stormtracks/output')

C20_FULL_DATA_DIR = os.path.join(DATA_DIR, 'c20_full')
C20_MEAN_DATA_DIR = os.path.join(DATA_DIR, 'c20_mean')
IBTRACS_DATA_DIR = os.path.join(DATA_DIR, 'ibtracs')
