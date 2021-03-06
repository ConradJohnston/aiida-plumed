""" Tests for calculations

"""
import aiida_plumed.tests as tests
from aiida.utils.fixtures import PluginTestCase
import os


class TestDiff(PluginTestCase):
    def setUp(self):
        # Set up code, if it does not exist
        self.code = tests.get_code(entry_point='plumed')

    def test_submit(self):
        """Test submitting a calculation"""
        from aiida.orm.data.singlefile import SinglefileData

        code = self.code

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
