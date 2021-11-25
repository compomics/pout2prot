'use strict';
import {
    AssertionError,
    AttributeError,
    BaseException,
    DeprecationWarning,
    Exception,
    IndexError,
    IterableError,
    KeyError,
    NotImplementedError,
    RuntimeWarning,
    StopIteration,
    UserWarning,
    ValueError,
    Warning,
    __JsIterator__,
    __PyIterator__,
    __Terminal__,
    __add__,
    __and__,
    __call__,
    __class__,
    __envir__,
    __eq__,
    __floordiv__,
    __ge__,
    __get__,
    __getcm__,
    __getitem__,
    __getslice__,
    __getsm__,
    __gt__,
    __i__,
    __iadd__,
    __iand__,
    __idiv__,
    __ijsmod__,
    __ilshift__,
    __imatmul__,
    __imod__,
    __imul__,
    __in__,
    __init__,
    __ior__,
    __ipow__,
    __irshift__,
    __isub__,
    __ixor__,
    __jsUsePyNext__,
    __jsmod__,
    __k__,
    __kwargtrans__,
    __le__,
    __lshift__,
    __lt__,
    __matmul__,
    __mergefields__,
    __mergekwargtrans__,
    __mod__,
    __mul__,
    __ne__,
    __neg__,
    __nest__,
    __or__,
    __pow__,
    __pragma__,
    __pyUseJsNext__,
    __rshift__,
    __setitem__,
    __setproperty__,
    __setslice__,
    __sort__,
    __specialattrib__,
    __sub__,
    __super__,
    __t__,
    __terminal__,
    __truediv__,
    __withblock__,
    __xor__,
    abs,
    all,
    any,
    assert,
    bool,
    bytearray,
    bytes,
    callable,
    chr,
    copy,
    deepcopy,
    delattr,
    dict,
    dir,
    divmod,
    enumerate,
    filter,
    float,
    getattr,
    hasattr,
    input,
    int,
    isinstance,
    issubclass,
    len,
    list,
    map,
    max,
    min,
    object,
    ord,
    pow,
    print,
    property,
    py_TypeError,
    py_iter,
    py_metatype,
    py_next,
    py_reversed,
    py_typeof,
    range,
    repr,
    round,
    set,
    setattr,
    sorted,
    str,
    sum,
    tuple,
    zip
} from "./org.transcrypt.__runtime__.js";

var __name__ = "OccamsRazorPreprocessor";
export var occam_filter = function (peptides_to_proteins, proteins_to_peptides, pre_protein_groups) {
    var remove_proteins = set();
    for (var prots of pre_protein_groups.py_values()) {
        var checked_proteins = set();
        for (var prot of prots) {
            var peps = proteins_to_peptides[prot];
            if (!__in__(prot, remove_proteins)) for (var prot2 of prots) {
                var peps2 = proteins_to_peptides[prot2];
                if (!__in__(prot2, checked_proteins)) {
                    if (isProperSubset(peps, peps2)) {
                        remove_proteins.add(prot);
                        break
                    }
                    if (isProperSubset(peps2, peps)) {
                        remove_proteins.add(prot2)
                    }
                }
            }
            checked_proteins.add(prot)
        }
        var remaining_proteins = set();
        for (var prot of prots) if (!__in__(prot, remove_proteins)) remaining_proteins.add(prot);

        var duplicate_dict = dict();
        var removed_duplicates = set();
        for (var protein1 of remaining_proteins) for (var protein2 of remaining_proteins) if (protein1 !=
            protein2) if (proteins_to_peptides[protein1] == proteins_to_peptides[protein2]) if (__in__(protein2, duplicate_dict.py_keys())) {
            removed_duplicates.add(protein1);
            duplicate_dict[protein2].add(protein1)
        } else if (__in__(protein1, duplicate_dict.py_keys())) {
            removed_duplicates.add(protein2);
            duplicate_dict[protein1].add(protein2)
        } else {
            removed_duplicates.add(protein2);
            var duplicate_set = set();
            duplicate_set.add(protein2);
            duplicate_dict[protein1] = duplicate_set
        }
        for (var duplicate of removed_duplicates) remaining_proteins.remove(duplicate);
        var unique_proteins = set();
        var unique_peptides = set();
        var remaining_peps = set();
        for (var prot of remaining_proteins) for (var pep of proteins_to_peptides[prot]) if (!(__in__(pep, unique_peptides) || __in__(pep, remaining_peps))) {
            var unique_count = 0;
            for (var prot_2 of peptides_to_proteins[pep]) if (__in__(prot_2, remaining_proteins)) var unique_count = unique_count + 1;
            if (unique_count == 1) {
                unique_peptides.add(pep);
                unique_proteins.add(prot)
            } else remaining_peps.add(pep)
        }
        for (var unqiue of unique_proteins) {
            remaining_proteins.remove(unqiue);
            for (var pep of proteins_to_peptides[unqiue]) if (__in__(pep, remaining_peps)) remaining_peps.remove(pep)
        }
        if (len(remaining_peps) == 0) {
            for (var prot of remaining_proteins) if (!__in__(prot, unique_proteins)) remove_proteins.add(prot);
            continue
        }
        var protein_count = 1;
        while (!(protein_count == len(remaining_proteins))) {
            var i = 0;
            var solution_attempts = list();
            while (i < protein_count) {
                var old_solution_attempts = solution_attempts.slice();
                var solution_attempts = list();
                for (var prot of remaining_proteins) if (i == 0) {
                    var current_solution =
                        set();
                    current_solution.add(prot);
                    solution_attempts.append(current_solution)
                } else for (var old_solution_attempt of old_solution_attempts) if (!__in__(prot, old_solution_attempt)) {
                    var solution_attempt = old_solution_attempt.slice();
                    solution_attempt.add(prot);
                    if (!__in__(solution_attempt, solution_attempts)) solution_attempts.append(solution_attempt)
                }
                var i = i + 1
            }
            var solutions = list();
            for (var solution_attempt of solution_attempts) {
                var peptide_set = set();
                for (var prot of solution_attempt) for (var pep of proteins_to_peptides[prot]) peptide_set.add(pep);
                if (peptide_set.issuperset(remaining_peps)) solutions.append(solution_attempt)
            }
            if (len(solutions) == 1) {
                var solution = solutions[0];
                for (var prot of remaining_proteins) if (!__in__(prot, solution)) {
                    remove_proteins.add(prot);
                    if (__in__(prot, duplicate_dict)) for (var other_prot of duplicate_dict[prot]) remove_proteins.add(other_prot)
                }
                break
            }
            if (len(solutions) > 1) {
                var protein_score = dict();
                for (var solution of solutions) for (var prot of solution) if (__in__(prot, protein_score.py_keys())) protein_score[prot] = protein_score[prot] +
                    1; else protein_score[prot] = 1;
                var highest_score = 0;
                var ambigouos_highscore = false;
                for (var solution of solutions) {
                    var solution_score = 0;
                    for (var prot of solution) var solution_score = solution_score + protein_score[prot];
                    if (solution_score > highest_score) {
                        var highest_score = solution_score;
                        var highscore_solution = solution;
                        var ambigouos_highscore = false
                    } else if (solution_score == highest_score) var ambigouos_highscore = true
                }
                if (!ambigouos_highscore) {
                    for (var prot of remaining_proteins) if (!(__in__(prot, highscore_solution) ||
                        __in__(prot, unique_proteins))) {
                        remove_proteins.add(prot);
                        if (__in__(prot, duplicate_dict)) for (var other_prot of duplicate_dict[prot]) remove_proteins.add(other_prot)
                    }
                    break
                }
            }
            var protein_count = protein_count + 1
        }
    }
    var peptides_marked_for_update = set();
    for (var prot_remove of remove_proteins) {
        for (var pep of proteins_to_peptides[prot_remove]) peptides_marked_for_update.add(pep);
        delete proteins_to_peptides[prot_remove]
    }
    for (var pept_marked of peptides_marked_for_update) peptides_to_proteins[pept_marked] = peptides_to_proteins[pept_marked].difference(remove_proteins)
};

function isProperSubset(s1, s2) {
    return s1.every(p1 => s2.includes(p1)) && s1.length < s2.length;
}

//# sourceMappingURL=OccamsRazorPreprocessor.map
