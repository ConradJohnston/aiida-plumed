# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
Parsers provided by the plugin

Register parsers via the "aiida.parsers" entry point in setup.json.
"""
from aiida.parsers.parser import Parser
from aiida.parsers.exceptions import OutputParsingError

from aiida.orm import CalculationFactory
DiffCalculation = CalculationFactory('plumed')


class PlumedParser(Parser):
    """
    Parser class for parsing COLVAR files.
    """

    def __init__(self, calculation):
        """
        Initialize Parser instance
        """
        super(DiffParser, self).__init__(calculation)

        # check for valid input
        if not isinstance(calculation, DiffCalculation):
            raise OutputParsingError("Can only parse DiffCalculation")

    # pylint: disable=protected-access
    def parse_with_retrieved(self, retrieved):
        """
        Parse outputs, store results in database.

        :param retrieved: a dictionary of retrieved nodes, where
          the key is the link name
        :returns: a tuple with two values ``(bool, node_list)``, 
          where:

          * ``bool``: variable to tell if the parsing succeeded
          * ``node_list``: list of new nodes to be stored in the db
            (as a list of tuples ``(link_name, node)``)
        """
        from aiida.orm.data.singlefile import SinglefileData
        success = False
        node_list = []

        # Check that the retrieved folder is there
        try:
            out_folder = retrieved[self._calc._get_linkname_retrieved()]
        except KeyError:
            self.logger.error("No retrieved folder found")
            return success, node_list

        # Check the folder content is as expected
        list_of_files = out_folder.get_folder_list()
        output_files = [self._calc._OUTPUT_FILE_NAME]
        output_links = ['plumed']
        # Note: set(A) <= set(B) checks whether A is a subset
        if set(output_files) <= set(list_of_files):
            pass
        else:
            self.logger.error(
                "Not all expected output files {} were found".format(
                    output_files))

        # Use something like this to loop over multiple output files
        for fname, link in list(zip(output_files, output_links)):

            node = SinglefileData(file=out_folder.get_abs_path(fname))
            node_list.append((link, node))

        success = True
        return success, node_list
=======
Parsers provided by aiida_plumed.

Register parsers via the "aiida.parsers" entry point in setup.json.
"""
from __future__ import absolute_import

from aiida.engine import ExitCode
from aiida.parsers.parser import Parser
from aiida.plugins import CalculationFactory

DiffCalculation = CalculationFactory('plumed')


class DiffParser(Parser):
    """
    Parser class for parsing output of calculation.
    """

    def __init__(self, node):
        """
        Initialize Parser instance

        Checks that the ProcessNode being passed was produced by a DiffCalculation.

        :param node: ProcessNode of calculation
        :param type node: :class:`aiida.orm.ProcessNode`
        """
        from aiida.common import exceptions
        super(DiffParser, self).__init__(node)
        if not issubclass(node.process_class, DiffCalculation):
            raise exceptions.ParsingError("Can only parse DiffCalculation")

    def parse(self, **kwargs):
        """
        Parse outputs, store results in database.

        :returns: an exit code, if parsing fails (or nothing if parsing succeeds)
        """
        from aiida.orm import SinglefileData

        output_filename = self.node.get_option('output_filename')

        # Check that folder content is as expected
        files_retrieved = self.retrieved.list_object_names()
        files_expected = [output_filename]
        # Note: set(A) <= set(B) checks whether A is a subset of B
        if not set(files_expected) <= set(files_retrieved):
            self.logger.error("Found files '{}', expected to find '{}'".format(
                files_retrieved, files_expected))
            return self.exit_codes.ERROR_MISSING_OUTPUT_FILES

        # add output file
        self.logger.info("Parsing '{}'".format(output_filename))
        with self.retrieved.open(output_filename, 'rb') as handle:
            output_node = SinglefileData(file=handle)
        self.out('plumed', output_node)

        return ExitCode(0)
>>>>>>> cutter/master
