import os

import atomman.lammps as lmp

def check_lammps_version(lammps_command):

    emptyscript = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'empty.in')
    log = lmp.run(lammps_command, emptyscript, logfile='empty.lammps')
    os.remove('empty.lammps')
    return {'lammps_version': log.lammps_version, 'lammps_date': log.lammps_date}