# only for Occams razor (PAPSSO): go through proteins and remove those that have no unique peptides
# Remove all proteins that don't contain unique peptides

# Input
# 1) Peptide -> Set<Protein>
# 2) Protein -> Set<Peptide>

# We need to check whether some of these proteins do not contain unique peptides. We can check this by iterating over
# all proteins, for each protein extract all associated peptides and check if these peptides are all associated to
# another at least one other protein. If that's the case, we remove the current protein.


def occam_filter(peptides_to_proteins, proteins_to_peptides, pre_protein_groups):
    """ Perform filtering on the proteins, based on Occam's razor decisions.

    :param peptides_to_proteins: A dictionary that maps every peptide onto a set of all proteins (that are associated
    with ths peptide).
    :param proteins_to_peptides: A dictionary that maps every protein onto a set of all peptides (which are associated
    with this protein).
    :param pre_protein_groups: A dictionary that maps a protein group id to a set of protein accessions (the members
    of this group). These are equivalent to Anti-Occam-groups and are useful to drastically reduce the computation of
    Occam's razor processing.
    :return: Both set's given are updated in-place. This means that no explicit value is returned, but rather that the
    arguments passed will be changed.
    """
    remove_proteins = set()
    # --> using only the groups means we can drastically reduce computation
    for prots in pre_protein_groups.values():

        # 1. detecting strict subsets
        checked_proteins = set()
        for prot in prots:
            peps = proteins_to_peptides[prot]
            if not (prot in remove_proteins):
                for prot2 in prots:
                    peps2 = proteins_to_peptides[prot2]
                    if not (prot2 in checked_proteins):
                        if peps < peps2:
                            remove_proteins.add(prot)
                            break
                        if peps2 < peps:
                            remove_proteins.add(prot2)
            checked_proteins.add(prot)

        remaining_proteins = set()
        for prot in prots:
            if not (prot in remove_proteins):
                remaining_proteins.add(prot)

        # 2. detect duplicates
        # remove duplicate peptide sets - proteins that have the exact same peptide set will be considered as one
        duplicate_dict = dict()
        removed_duplicates = set()
        for protein1 in remaining_proteins:
            for protein2 in remaining_proteins:
                if protein1 != protein2:
                    if proteins_to_peptides[protein1] == proteins_to_peptides[protein2]:
                        # exact same peptide set, save the duplicates
                        # protein1 will be the key by default
                        # but maybe protein2 was already chosen as primary protein
                        if protein2 in duplicate_dict.keys():
                            removed_duplicates.add(protein1)
                            duplicate_dict[protein2].add(protein1)
                        else:
                            if protein1 in duplicate_dict.keys():
                                removed_duplicates.add(protein2)
                                duplicate_dict[protein1].add(protein2)
                            else:
                                removed_duplicates.add(protein2)
                                duplicate_set = set()
                                duplicate_set.add(protein2)
                                duplicate_dict[protein1] = duplicate_set

        for duplicate in removed_duplicates:
            remaining_proteins.remove(duplicate)

        # 3. detecting unique proteins, 4. collect the unexplained/remaining peptides
        unique_proteins = set()
        unique_peptides = set()
        remaining_peps = set()
        for prot in remaining_proteins:
            for pep in proteins_to_peptides[prot]:
                if not ((pep in unique_peptides) or (pep in remaining_peps)):
                    unique_count = 0
                    for prot_2 in peptides_to_proteins[pep]:
                        if prot_2 in remaining_proteins:
                            unique_count = unique_count + 1
                    if unique_count == 1:
                        unique_peptides.add(pep)
                        unique_proteins.add(prot)
                    else:
                        remaining_peps.add(pep)

        for unqiue in unique_proteins:
            remaining_proteins.remove(unqiue)
            for pep in proteins_to_peptides[unqiue]:
                if pep in remaining_peps:
                    remaining_peps.remove(pep)

        # 5. if we already explain all peptides at this point, remove all group proteins that are not unique
        if len(remaining_peps) == 0:
            for prot in remaining_proteins:
                if not (prot in unique_proteins):
                    remove_proteins.add(prot)
            # move on to next group
            continue

        # 6. This is the meat of the algorithm: We check for combinations of proteins that can explain all remaining
        # peptides. We start with one protein and count up.
        protein_count = 1
        # if the protein_count reaches the size of remaining proteins, we have to keep all remaining proteins
        while not (protein_count == len(remaining_proteins)):
            # we try to explain the remaining peptides with the current protein count
            # 6.1. first we try all combinations as solution attempts
            i = 0
            solution_attempts = list()
            while i < protein_count:
                old_solution_attempts = solution_attempts.copy()
                solution_attempts = list()
                for prot in remaining_proteins:
                    if i == 0:
                        current_solution = set()
                        current_solution.add(prot)
                        solution_attempts.append(current_solution)
                    else:
                        for old_solution_attempt in old_solution_attempts:
                            if not (prot in old_solution_attempt):
                                solution_attempt = old_solution_attempt.copy()
                                solution_attempt.add(prot)
                                if not (solution_attempt in solution_attempts):
                                    solution_attempts.append(solution_attempt)
                i = i + 1
            # 6.2. second we filter out solution attempts that dont explain all peptides
            # solutions is a list of sets of proteins that explain all peptides
            solutions = list()
            for solution_attempt in solution_attempts:
                peptide_set = set()
                for prot in solution_attempt:
                    for pep in proteins_to_peptides[prot]:
                        peptide_set.add(pep)
                if peptide_set.issuperset(remaining_peps):
                    solutions.append(solution_attempt)

            # third we evaluate the set of solution attempts at this protein count
            # 0 solutions means we have to continue, 1 solution means we are finished
            if len(solutions) == 1:
                # simple case
                solution = solutions[0]
                for prot in remaining_proteins:
                    if not (prot in solution):
                        remove_proteins.add(prot)
                        # also add all duplicates
                        if prot in duplicate_dict:
                            for other_prot in duplicate_dict[prot]:
                                remove_proteins.add(other_prot)
                break
            if len(solutions) > 1:
                # if there are more than 1 solution, we can evaluate it by scoring each solution
                protein_score = dict()
                for solution in solutions:
                    for prot in solution:
                        if prot in protein_score.keys():
                            protein_score[prot] = protein_score[prot] + 1
                        else:
                            protein_score[prot] = 1
                highest_score = 0
                ambigouos_highscore = False
                for solution in solutions:
                    solution_score = 0
                    for prot in solution:
                        solution_score = solution_score + protein_score[prot]
                    if solution_score > highest_score:
                        highest_score = solution_score
                        highscore_solution = solution
                        ambigouos_highscore = False
                    elif solution_score == highest_score:
                        ambigouos_highscore = True
                if not ambigouos_highscore:
                    # this is an unambigouos solution, we can remove all other proteins and finish
                    for prot in remaining_proteins:
                        if not ((prot in highscore_solution) or (prot in unique_proteins)):
                            remove_proteins.add(prot)
                            # also add all duplicates
                            if prot in duplicate_dict:
                                for other_prot in duplicate_dict[prot]:
                                    remove_proteins.add(other_prot)
                    break
            # reaching here means no unambigouos solution was found at the current protein count
            protein_count = protein_count + 1

    # 4. Removal step
    peptides_marked_for_update = set()
    for prot_remove in remove_proteins:
        for pep in proteins_to_peptides[prot_remove]:
            peptides_marked_for_update.add(pep)
        del proteins_to_peptides[prot_remove]

    for pept_marked in peptides_marked_for_update:
        peptides_to_proteins[pept_marked] = peptides_to_proteins[pept_marked].difference(remove_proteins)
