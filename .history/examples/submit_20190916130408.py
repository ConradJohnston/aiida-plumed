# -*- coding: utf-8 -*-
"""Submit a test calculation on localhost.

Usage: verdi run submit.py
<<<<<<< HEAD

Note: This script assumes you have set up computer and code as in README.md.
"""
import aiida_plumed.tests as tests
from aiida.orm.data.singlefile import SinglefileData
import os

code = tests.get_code(entry_point='plumed')

# Prepare input parameters
from aiida.orm import DataFactory
DiffParameters = DataFactory('plumed')
parameters = DiffParameters({'ignore-case': True})

file1 = SinglefileData(file=os.path.join(tests.TEST_DIR, 'file1.txt'))
file2 = SinglefileData(file=os.path.join(tests.TEST_DIR, 'file2.txt'))

# set up calculation
calc = code.new_calc()
calc.label = "aiida_plumed test"
calc.description = "Test job submission with the aiida_plumed plugin"
calc.set_max_wallclock_seconds(30)
calc.set_withmpi(False)
calc.set_resources({"num_machines": 1, "num_mpiprocs_per_machine": 1})

calc.use_parameters(parameters)
calc.use_file1(file1)
calc.use_file2(file2)

calc.store_all()
calc.submit()
print("submitted calculation; calc=Calculation(uuid='{}') # ID={}"\
        .format(calc.uuid,calc.dbnode.pk))
=======
"""
from __future__ import absolute_import
from __future__ import print_function
import os
from aiida_plumed import tests, helpers
from aiida.plugins import DataFactory, CalculationFactory
from aiida.engine import run

# get code
computer = helpers.get_computer()
code = helpers.get_code(entry_point='plumed', computer=computer)

# Prepare input parameters
DiffParameters = DataFactory('plumed')
parameters = DiffParameters({'ignore-case': True})

SinglefileData = DataFactory('singlefile')
file1 = SinglefileData(
    file=os.path.join(tests.TEST_DIR, "input_files", 'file1.txt'))
file2 = SinglefileData(
    file=os.path.join(tests.TEST_DIR, "input_files", 'file2.txt'))

# set up calculation
inputs = {
    'code': code,
    'parameters': parameters,
    'file1': file1,
    'file2': file2,
    'metadata': {
        'description': "Test job submission with the aiida_plumed plugin",
    },
}

# Note: in order to submit your calculation to the aiida daemon, do:
# from aiida.engine import submit
# future = submit(CalculationFactory('plumed'), **inputs)
result = run(CalculationFactory('plumed'), **inputs)

computed_diff = result['plumed'].get_content()
print("Computed diff between files: \n{}".format(computed_diff))
>>>>>>> cutter/master
