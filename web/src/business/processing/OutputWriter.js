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

var __name__ = "__main__";
export var write_to_file = function (rep_cat, groups, psm_exp, pep_psm, peptide_protein_map, protein_peptide_map) {
    var output = "";
    output += "sample category\tsample name\tprotein accessions\tspectrum count\n";
    var peptide_to_groups = dict();
    for (var [group, proteins] of groups.py_items()) {
        for (var protein of proteins) {
            for (var peptide of protein_peptide_map[protein]) {
                if (__in__(peptide, peptide_to_groups)) {
                    peptide_to_groups[peptide].add(group);
                } else {
                    peptide_to_groups[peptide] = new set([group]);
                }
            }
        }
    }
    for (var proteins of groups.py_values()) {
        var experiments = set();
        var experiment_to_count = dict();
        var used_peptides = set();
        for (var protein of proteins) for (var peptide of protein_peptide_map[protein]) {
            if (!__in__(peptide, used_peptides)) for (var psm of pep_psm[peptide]) {
                var divide_by =
                    len(peptide_to_groups[peptide]);
                var experiment = psm_exp[psm];
                if (__in__(experiment, experiment_to_count)) experiment_to_count[experiment] = experiment_to_count[experiment] + 1 / divide_by; else {
                    experiment_to_count[experiment] = 1 / divide_by;
                    if (!__in__(experiment, experiments)) experiments.add(experiment)
                }
            }
            used_peptides.add(peptide)
        }

        for (var experiment of experiments) {
            var category = rep_cat[experiment];
            const experimentStrings = experiment.split("\\");
            const experimentString = experimentStrings[experimentStrings.length - 1].split(".")[0];
            output += `${category}\t${experimentString}\t${proteins.join(',')}\t${experiment_to_count[experiment]}\n`
        }
    }

    return output;
};

//# sourceMappingURL=OutputWriter.map
