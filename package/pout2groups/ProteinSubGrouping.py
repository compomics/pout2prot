def create_protein_subgroups(occam_flag, protein_groups, protein_peptide_dict):
    """takes the protein-groups and divides them into subgroups"""
    # protein_subgroups
    protein_subgroups = dict()
    # loop through the protein groups
    for protein_group_id in protein_groups.keys():
        # protein_subgroup_id will be a string with format "group-id_subgroup-id"
        protein_subgroup_id_first_half = str(protein_group_id) + "_"
        # get the list of proteins from this group and create a copy
        protein_list = protein_groups[protein_group_id].copy()
        # counter to name the subgroups
        subgroup_count = 0
        # take proteins from list until it is empty, which means all proteins are now in a subgroup
        while len(protein_list) > 0:
            # remove a protein from the list
            current_protein = protein_list.pop()
            # create a new protein subgroup, first create the list of proteins
            subgroup_protein_list = {current_protein}
            # then its id
            subgroup_count += 1
            subgroup_id = protein_subgroup_id_first_half + str(subgroup_count)
            # then update dictionary
            protein_subgroups[subgroup_id] = subgroup_protein_list
            # also create a set for all the peptides of this group
            peptide_set_1_group = protein_peptide_dict[current_protein]
            # create a list of proteins to be removed after loop
            list_of_proteins_to_remove = set()
            for compare_protein in protein_list:
                # compare the peptide sets
                peptide_set_2_compare = protein_peptide_dict[compare_protein]
                if peptide_set_1_group.issubset(peptide_set_2_compare):
                    # for anti-occam we need to check if peptide_set_1 is subset of another protein
                    add = True
                    # case 1
                    if not occam_flag:
                        # loop through the remaining proteins
                        for other_protein in protein_list:
                            if other_protein != compare_protein:
                                if other_protein not in list_of_proteins_to_remove:
                                    # and compare the peptide set, we only need to check if its subset of the other
                                    peptide_set_3_other = protein_peptide_dict[other_protein]
                                    if peptide_set_1_group.issubset(peptide_set_3_other):
                                        if (not peptide_set_2_compare < peptide_set_3_other) and \
                                                (not peptide_set_3_other < peptide_set_2_compare):
                                            # new subgroup for this protein, which will be done at the end
                                            add = False
                                            break
                    # add to subgroup
                    if add:
                        # if peptide_set_2_compare is the bigger one, replace subgroup_peptides with it
                        peptide_set_1_group = peptide_set_2_compare
                        subgroup_protein_list.add(compare_protein)
                        # store for removal from protein_list
                        list_of_proteins_to_remove.add(compare_protein)
                elif peptide_set_2_compare.issubset(peptide_set_1_group):
                    # for anti-occam we need to check if peptide_set_1 is subset of another protein
                    add = True
                    # case 2
                    if not occam_flag:
                        # loop through the remaining proteins
                        for other_protein in protein_list:
                            if other_protein != compare_protein:
                                # if other_protein not in list_of_proteins_to_remove:
                                # and compare the peptide set, we only need to check if its subset of the other
                                peptide_set_3_other = protein_peptide_dict[other_protein]
                                if peptide_set_2_compare < peptide_set_3_other:
                                    if (not peptide_set_1_group < peptide_set_3_other) and \
                                            (not peptide_set_3_other.issubset(peptide_set_1_group)):
                                        # new subgroup for this protein, which will be done at the end
                                        add = False
                                        break
                    # add to subgroup
                    if add:
                        # add to subgroup
                        subgroup_protein_list.add(compare_protein)
                        # store for removal from protein_list
                        list_of_proteins_to_remove.add(compare_protein)

            # remove proteins that were added to the subgroup
            for remove_protein in list_of_proteins_to_remove:
                protein_list.remove(remove_protein)

    return protein_subgroups
