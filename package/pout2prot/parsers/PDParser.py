from package.pout2prot.parsers.Parser import Parser

from glob import glob
import os.path
import string


class PDParser(Parser):
    def parse(path, fdr_treshold, decoy_flag, sample_categories_flag):
        table = str.maketrans('', '', string.ascii_lowercase)

