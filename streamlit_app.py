#!/usr/bin/env python3

# PEPTIDE SPECTRUM MATCHING SOLUTION BROWSER
# 2022 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

import streamlit as st

def success():
    st.balloons()
    st.success("Congratulations! You have found the correct Peptide Spectrum Match (PSM). Give yourself a pat on the shoulder and make sure to claim your protein bar! :)")
    return

def get_response(entry):

    solutions = ["A3", "B2", "C3", "D1", "E4"]
    clean_entry = entry.upper().lstrip().rstrip().replace(" ", "")

    if clean_entry[0] not in ["A", "B", "C", "D", "E"]:
        st.error("Could not recognize peptide group! Please enter your answer in the format LETTERNUMBER e.g. A1 for peptide group A and spectrum 1.")
        return

    if clean_entry[:2] in solutions:
        success()
        return

    responses = {"A": "Sorry that is not the correct solution! You might want to have a look at the y4 ion and try again! ;)",
                 "B": "Sorry that is not the correct solution! You might want to have a look at the b3 ion and try again! ;)",
                 "C": "Sorry that is not the correct solution! You might want to have a look at the b3 ion intensity and try again! ;)",
                 "D": "Sorry that is not the correct solution! You might want to have a look at the b3 and y4 ions and try again! ;)",
                 "E": "Sorry that is not the correct solution! You might want to have a look at b4 and b5 ions and try again! ;)",}
    st.error(responses[clean_entry[0]])
    return

# main page content
def main_page():

    title = st.title("Peptide Spectrum Matching Solution Browser")

    entry = st.text_input("Enter your solution:", "A1", help = "Enter the peptide group and spectrum number (e.g. A1) to verify your solution.")

    if st.button("Check!", help = "Verify your solution."):
        get_response(entry)

# side bar and main page loader
def main():

    about_str = \
    """
    **Peptide Spectrum Matching Solution Browser**

    A small webservice to check your solution for the Peptide Spectrum Matching Game presented by the Proteomics Research Group of FHOOE Hagenberg.

    **Contact:** [Micha Birklbauer](mailto:micha.birklbauer@gmail.com)
    
    **GitHub:** [github.com/michabirklbauer/peptide-matching-game](https://github.com/michabirklbauer/peptide-matching-game)
    """

    st.set_page_config(page_title = "Peptide Spectrum Matching Solution Browser",
                       page_icon = ":test_tube:",
                       layout = "centered",
                       initial_sidebar_state = "expanded",
                       menu_items = {"Get Help": "https://github.com/michabirklbauer/peptide-matching-game/discussions",
                                     "Report a bug": "https://github.com/michabirklbauer/peptide-matching-game/issues",
                                     "About": about_str}
                       )

    title = st.sidebar.title("Peptide Spectrum Matching Solution Browser")

    logo = st.sidebar.image("img/fhooe_logo.png", caption = "Presented by the Bioinformatics Research Group of the University of Applied Sciences Upper Austria, Hagenberg.")

    doc = st.sidebar.markdown("Check your solution for the Peptide Spectrum Matching Game and verify if you managed to match the correct spectra!")

    socials_str = \
        """
        **More About Us:**

        **Bioinformatics Research Group Hagenberg:**  """ + """
        [Who we are](https://bioinformatics.fh-hagenberg.at/bin_typo3/htdocs/index.php?id=home)

        **Study Bioinformatics in Hagenberg:**  """ + """
        [Study MBI](https://www.fh-ooe.at/campus-hagenberg/studiengaenge/bachelor/medizin-und-bioinformatik/)

        **Study Data Science and Engineering in Hagenberg:**  """ + """
        [Study DSE](https://www.fh-ooe.at/campus-hagenberg/studiengaenge/master/data-science-und-engineering/)
        """
    socials = st.sidebar.markdown(socials_str)

    main_page()

if __name__ == "__main__":
    main()
