# -*- coding: utf-8 -*-
"""
Functions to parse a Plumed Colvar file
"""

def parse_raw_colvar(colvar_file):
    """
    Parses the COLVAR file from a Plumed calculation.

    :param colvar_file: path to Plumed COLVAR file
    
    :returns out_dict: dictionary with parsed data 
    """

    # Load the COLVAR file
    try:
        with open(colvar_file, 'r') as f:
            all_lines = f.readlines()
    except IOError: 
        print("Failed to open COLVAR file: {}".format(colvar_file))
    # TODO: Convert to OutputParsingError 
    
    # Parse   
    colvar_raw_dict = {}

    # Check if the data looks like a COLVAR file
    if all_lines[0][0:2] != '#!':
        raise ValueError("File {} does not contain a valid header or "
                         "is not a valid COLVAR file".format(colvar_file))

    # Separate the header lines (those which start with !#) from data lines
    header_lines = []
    data_lines = []
    for line in all_lines:
        if line[0:2] == '#!':
            header_lines.append(line)
        else: 
            data_lines.append(line)

    # Parse the header 
    # The first header line documentes the fields
    # Split the line on spaces, ignore the first two items ('#!' and 'FIELDS')
    # and add the rest to the dictionary
    colvar_raw_dict['fields'] =  header_lines[0].split()[2:]
    # The rest of the header sets limits and flags.
    # These have a common format of : SET key value
    # Store these in a dictionary
    header_params = {}
    for line in header_lines:
        line_items = line.split()
        if line_items[1] == 'SET':
            header_params[line_items[2]] = line_items[3]
    colvar_raw_dict['params'] = header_params

    # Parse the data
    data = {}
    # Run over the fields parased from the header, and store each 
    # col as a list in the dictionary with the field name as the key.
    for idx,col in enumerate(colvar_raw_dict['fields']):
        col_data_list = []
        for line in data_lines:
            col_data_list.append(line.split()[idx])
        data[col] = col_data_list
    colvar_raw_dict['data'] = data

    return colvar_raw_dict

            
        

     
            

    

            
     
        



