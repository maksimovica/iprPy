import os

def schema():
    dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(dir, 'record-calculation-system-relax.xsd')