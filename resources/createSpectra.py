#!/usr/bin/env python3

from matplotlib import pyplot as plt
import ms2pip.single_prediction
import spectrum_utils.spectrum as spectrum
import spectrum_utils.plot as spectrum_plot

## 5 x 4 matrix

peptide_1 = "PLPGER"
peptide_2 = "FIYAYR"
peptide_3 = "GEQVSLR"
peptide_4 = "DRYIAIR"
peptide_5 = "ARSTLQK"

# a 3 - easy
# y4 matches only 3
peptides_1 = ["PLFGER", "PLHGER", "PLPGER", "PLGGER"]
# b 2 - medium
# b3 is only correct in 2
peptides_2 = ["FIFAYR", "FIYAYR", "FIHAYR", "FIKAYR"]
# c 3 - medium
# b3 intensity only matches 3
peptides_3 = ["GEQASLR", "GEQTSLR", "GEQVSLR", "GEQSSLR"]
# d 1 - hard
# b3 and y4 only correct in 1
peptides_4 = ["DRYIAIR", "DRYFAIR", "DRYWAIR", "DRYPAIR"]
# e 4 - hard
# b4 and b5 of 1, 2 are too intense, b4 of 3 is off by ~15 Da
peptides_5 = ["ARSILQK", "ARSLLQK", "ARSSLQK", "ARSTLQK"]

gridlines = False


all_peptides = [peptides_1,
                peptides_2,
                peptides_3,
                peptides_4,
                peptides_5]

def get_spectrum(peptide_sequence, charge = 1):

    model = ms2pip.single_prediction.SinglePrediction()
    mz, intensity, annotation = model.predict(peptide_sequence, "-", charge, model = "HCD2021")
    identifier = f"{peptide_sequence}/{charge}/-"
    precursor_mz = model.mod_info.calc_precursor_mz(peptide_sequence, "-", charge)
    mod_dict = model._modifications_to_dict("-")
    spectrum_annotation = model._get_sus_annotation(mz, annotation)

    s = spectrum.MsmsSpectrum(identifier,
                              precursor_mz,
                              charge,
                              mz,
                              intensity,
                              annotation = spectrum_annotation,
                              peptide = peptide_sequence,
                              modifications = mod_dict)

    return s

def main():
    fig, axs = plt.subplots(5,4, figsize = (25,20), dpi = 300, tight_layout = True)
    i = 0
    rows = ["A", "B", "C", "D", "E"]
    for peptide_group in all_peptides:
        j = 0
        for peptide in peptide_group:
            s = get_spectrum(peptide)
            spectrum_plot.spectrum(s, ax = axs[i, j])
            axs[i, j].set_title(rows[i] + str(j + 1) + " - " + peptide)
            axs[i, j].set_xlim([0, 900])
            axs[i, j].grid(visible = gridlines, which = "both")
            j += 1
        i += 1

    plt.savefig("result.svg")

def main2():
    rows = ["A", "B", "C", "D", "E"]
    for i, peptide in enumerate([peptide_1, peptide_2, peptide_3, peptide_4, peptide_5]):
        s = get_spectrum(peptide)
        fig = plt.figure(figsize = (8,4.5))
        plt.title("Peptide Group " + rows[i])
        spectrum_plot.spectrum(s)
        plt.xlim([0, 900])
        plt.grid(visible = gridlines, which = "both")
        plt.savefig(rows[i] + ".svg")


if __name__ == "__main__":
    main()
    main2()
