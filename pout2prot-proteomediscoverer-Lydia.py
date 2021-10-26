from glob import glob
import os.path
import string

pd_data = "C:\\Users\\tvdbo\\OneDrive\\Documents\\Projecten\\pout2prot-Lydia\\pd-data"
pout_files = "C:\\Users\\tvdbo\\OneDrive\\Documents\\Projecten\\pout2prot-Lydia\\pout-files"

def pd_to_pout2prot(pd_data, pout_files):
    """
    Input: ProteomeDiscoverer PSM input file(s)
    Output: Pout2Prot input file(s)
    """
    table = str.maketrans('', '', string.ascii_lowercase)
    pd_file_no = 1

    for pd_file in glob(pd_data + "/*.txt"):
        condition_set = set()  # 1 raw file = 1 condition
        my_dir = os.path.join(pout_files, os.path.basename(pd_file.replace(".txt", "")))
        try:
            os.mkdir(my_dir)
        except FileExistsError:
            pass
        print(my_dir)

        # check for the conditions
        with open(pd_file, "r") as in_f:
            next(in_f)
            for line in in_f:
                line = line.replace('"', '').replace(" ", "_").replace("\t", ", ")
                try:
                    _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, \
                        condition, _, _, _, _, _, _, _, _ = line.split(", ")
                    condition_set.add(condition)
                except ValueError:  # empty lines
                    pass

        # per condition, open a new file in my_dir
        for condition in list(condition_set):
            with open(pd_file, "r") as in_f, \
            open("{}\\{}".format(my_dir, condition.replace("raw", "pout")), "w") as out_f:
                print("PSMId\tscore\tq-value\tposterior_error_prob\tpeptide\tproteinIds", file=out_f)
                next(in_f)
                for line in in_f:
                    line = line.replace('"', '').replace(" ", "_").replace("\t", ", ")
                    try:
                        # Annotated Sequence = peptide
                        # Protein Accessions = proteins
                        # Spectrum_File = condition --> there's only 1 experiment per condition
                        # Percolator q-Value = q_value
                        # Percolator_PEP = pep
                        _, psm_id, _, _, _, _, peptide, _, _, _, proteins, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, \
                            condition_psm, _, _, _, _, q_value, pep, _, _ = line.split(", ")
                        if condition_psm == condition:
                            peptide = peptide.replace("[", "").replace("]", "")
                            peptide = peptide.translate(table)
                            proteins = proteins.replace(";_", "\t")
                            print("{}_{}\tscore\t{}\t{}\t{}\t{}".format(str(pd_file_no).zfill(3), psm_id, q_value, pep, peptide, proteins), file=out_f)
                    except ValueError:  # empty lines
                        pass

        pd_file_no += 1


pd_to_pout2prot(pd_data, pout_files)
