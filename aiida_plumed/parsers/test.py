import raw_parser
import pprint
d = raw_parser.parse_raw_colvar('colvar_example.dat')
pprint.pprint(d)
