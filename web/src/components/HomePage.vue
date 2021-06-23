<template>
    <v-container>
        <v-row>
            <v-col cols="12">
                <h1>
                    Welcome
                </h1>
                <div class="mb-2">
                    This application can be used to perform protein grouping and subgrouping on the
                    proteins recorded in a .pout file. Complete all steps in the wizard below to fulfil the analysis.
                    All conversion steps take place on the client side. This means that none of your files are sent to
                    our web server and that they are only used by the browser itself to perform the requested analysis.
                </div>
                <v-stepper vertical v-model="currentStep">
                    <v-stepper-step :complete="currentStep > 1" step="1">
                        Select all input files
                        <small>This application only accepts .pout-files</small>
                    </v-stepper-step>
                    <v-stepper-content step="1">
                        <v-file-input v-model="files" multiple></v-file-input>
                        <div class="d-flex mt-2">
                            <v-btn class="ml-auto" color="primary" @click="currentStep = 2">
                                Continue
                            </v-btn>
                        </div>
                    </v-stepper-content>
                    <v-stepper-step :complete="currentStep > 2" step="2">
                        Configure experiment names
                    </v-stepper-step>
                    <v-stepper-content step="2">
                        <v-simple-table>
                            <template v-slot:default>
                                <thead>
                                    <tr>
                                        <th class="text-left">File</th>
                                        <th class="text-left">Experiment name</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(file, idx) in files" :key="file.name">
                                        <td>{{ file.name }}</td>
                                        <td>
                                            <v-text-field v-model="experimentNames[idx]">
                                            </v-text-field>
                                        </td>
                                    </tr>
                                </tbody>
                            </template>
                        </v-simple-table>

                        <div class="d-flex mt-2">
                            <v-btn text @click="currentStep = 1">
                                Go back
                            </v-btn>
                            <v-btn class="ml-auto" color="primary" @click="currentStep = 3">
                                Continue
                            </v-btn>
                        </div>
                    </v-stepper-content>
                    <v-stepper-step :complete="currentStep > 3" step="3">
                        Parameters
                    </v-stepper-step>
                    <v-stepper-content step="3">
                        <v-container fluid>
                            <v-row>
                                <v-col cols="5">
                                    <div class="settings-title">Occam's razor</div>
                                    <span class="settings-text">
                                        This setting only affects the subgroup analysis. If enabled, all proteins that
                                        not uniquely identify at least one peptide are discarded.
                                    </span>
                                </v-col>
                                <v-col cols="1" class="d-flex justify-center">
                                    <v-switch v-model="occam"></v-switch>
                                </v-col>
                                <v-col cols="5">
                                    <div class="settings-title">FDR threshold</div>
                                    <span class="settings-text">
                                        This setting affects the parsing of the input files. Only entries for which the
                                        FDR is larger than the value given here are retained, all other entries are
                                        not taken into account while performing the protein grouping analysis.
                                    </span>
                                </v-col>
                                <v-col cols="1">
                                    <v-text-field
                                        label="0.05"
                                        step="0.01"
                                        min="0"
                                        max="1"
                                        single-line filled
                                        type="number"
                                        v-model="fdr">
                                    </v-text-field>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col cols="5">
                                    <div class="settings-title">Decoy flag</div>
                                    <span class="settings-text">
                                        Which flag is used to indicate decoy proteins in the input data set? All
                                        proteins that include this substring in their name are discarded from the
                                        analysis. Leave empty if no such flag has been set.
                                    </span>
                                </v-col>
                                <v-col cols="1">
                                    <v-text-field single-line filled v-model="decoyFlag">
                                    </v-text-field>
                                </v-col>
                            </v-row>
                        </v-container>
                        <div class="d-flex mt-2">
                            <v-btn text @click="currentStep = 2">
                                Go back
                            </v-btn>
                            <v-btn class="ml-auto" color="primary" @click="startAnalysis">
                                Continue
                            </v-btn>
                        </div>
                    </v-stepper-content>
                    <v-stepper-step :complete="currentStep > 4" step="4">
                        View results
                    </v-stepper-step>
                    <v-stepper-content step="4">
                        <div class="d-flex align-center flex-column" v-if="analysisInProgress">
                            <v-progress-circular indeterminate color="primary"></v-progress-circular>
                            <span>Performing analysis, please wait...</span>
                        </div>
                        <div class="d-flex align-center flex-column" v-else>
                            <span>
                                Protein grouping has successfully been performed. Click the button below to download the
                                generated files.
                            </span>
                            <v-btn color="primary" outlined x-large fab class="mt-2" @click="downloadFiles">
                                <v-icon>
                                    mdi-cloud-download-outline
                                </v-icon>
                            </v-btn>
                        </div>
                        <div class="d-flex mt-2">
                            <v-btn class="ml-auto" color="primary" @click="currentStep = 1">
                                Start over
                            </v-btn>
                        </div>
                    </v-stepper-content>
                </v-stepper>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import { protein_grouping_analysis } from "@/business/processing/Analyzer";
import { write_to_file } from "@/business/processing/OutputWriter";
import { set, dict } from '@/business/processing/org.transcrypt.__runtime__.js'
import Parser from "@/business/processing/Parser";

import JSZip from 'jszip';
import FileSaver from 'file-saver';

export default {
    name: 'HomePage',

    data: () => ({
        files: [],
        experimentNames: [],
        currentStep: 1,
        occam: false,
        fdr: 0.05,
        decoyFlag: "decoy_",
        analysisInProgress: false,
        zipResult: null
    }),

    watch: {
        // Process newly uploaded file and start the parser.
        files: function() {
            this.experimentNames.splice(0, this.experimentNames.length);
            for (const file of this.files) {
                this.experimentNames.push(file.name);
            }
        }
    },

    methods: {
        startAnalysis: async function() {
            if (this.files) {
                this.currentStep = 4;

                const [
                    psmExp, pepPsm, pepProt, protPept, repCat
                ] = await Parser.parseFiles(
                    this.files,
                    this.experimentNames,
                    this.fdr,
                    this.decoyFlag
                );

                const peptPsmArray = [];
                for (const entry of pepPsm.entries()) {
                    const newSet = set();
                    for (const item of entry[1]) {
                        newSet.add(item);
                    }
                    peptPsmArray.push([entry[0], newSet]);
                }

                const protPeptArray = [];
                for (const entry of protPept.entries()) {
                    const newSet = set();
                    for (const peptide of entry[1]) {
                        newSet.add(peptide);
                    }
                    protPeptArray.push([entry[0], newSet]);
                }

                const peptProtArray = [];
                for (const entry of pepProt.entries()) {
                    const newSet = set();
                    for (const prot of entry[1]) {
                        newSet.add(prot);
                    }
                    peptProtArray.push([entry[0], newSet]);
                }

                const [proteinGroups, proteinSubgroups] = protein_grouping_analysis(
                    this.occam,
                    dict(protPeptArray),
                    dict(peptProtArray)
                );

                const groupFile = write_to_file(dict([...repCat]), proteinGroups, dict([...psmExp.entries()]), dict(peptPsmArray), dict(peptProtArray), dict(protPeptArray));
                const subGroupFile = write_to_file(dict([...repCat]), proteinSubgroups, dict([...psmExp.entries()]), dict(peptPsmArray), dict(peptProtArray), dict(protPeptArray));

                const zip = new JSZip();
                zip.file("groups.out", groupFile);
                zip.file("subgroups.out", subGroupFile);
                this.zipResult = zip;
            }
        },
        downloadFiles: async function() {
            this.zipResult.generateAsync({type: "blob"}).then(function(content) {
                FileSaver.saveAs(content, "pout2prot.zip");
            });
        }
    }
}
</script>

<style>
    .settings-title {
        color: black;
        font-size: 18px;
    }

    .settings-important-text {
        font-style: italic;
        font-weight: bold;
        display: block;
    }
</style>
