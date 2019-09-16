""" Tests for command line interface.

"""
from __future__ import print_function
from __future__ import absolute_import

from aiida.manage.fixtures import PluginTestCase


class TestDataCli(PluginTestCase):
    def setUp(self):
        from click.testing import CliRunner
        from aiida.plugins import DataFactory

        DiffParameters = DataFactory('plumed')
        self.parameters = DiffParameters({'ignore-case': True})
        self.parameters.store()
        self.runner = CliRunner()

    def test_data_diff_list(self):
        """Test 'verdi data plumed list'

        Tests that it can be reached and that it lists the node we have set up.
        """
        from aiida_plumed.cli import list_

        result = self.runner.invoke(list_, catch_exceptions=False)
        self.assertIn(str(self.parameters.pk), result.output)

    def test_data_diff_export(self):
        """Test 'verdi data plumed export'

        Tests that it can be reached and that it shows the contents of the node
        we have set up.
        """
        from aiida_plumed.cli import export

        result = self.runner.invoke(
            export, [str(self.parameters.pk)], catch_exceptions=False)
        self.assertIn('ignore-case', result.output)
