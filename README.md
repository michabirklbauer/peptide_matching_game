# Peptide Matching Game

A simple game to illustrate how peptide identification in mass spectra works
using database search engines like [MS Amanda](https://pubs.acs.org/doi/full/10.1021/pr500202e).

## Usage

**How the game works:**
- Read through the [game instructions](https://github.com/michabirklbauer/peptide_matching_game/blob/master/Game_Rules.pdf).

**Setting up the game:**
- Print the [game poster](https://github.com/michabirklbauer/peptide_matching_game/blob/master/Game_Poster.pdf).
- Print at least one copy of each spectrum in `spectrum_cards`.
- Print the [game instructions](https://github.com/michabirklbauer/peptide_matching_game/blob/master/Game_Rules.pdf) for people to understand the game.
- [Optional] Set up your own game solution browser or use [https://michabirklbauer.github.io/peptide_matching_game/](https://michabirklbauer.github.io/peptide_matching_game/) so people are able to check their solutions.

**Setting up the game solution browser:**
- Install requirements: `pip install -r requirements.txt`
- Run streamlit app: `streamlit run streamlit_app.py`
- Alternatively pull and run the docker container: `docker run -p 8501:8501 michabirklbauer/peptidematchinggame:latest`
- Open your browser and navigate to `localhost:8501`.

## References

- PDB structure [3RFM](https://www.rcsb.org/structure/3RFM) by [Dore et al.](http://dx.doi.org/10.1016/j.str.2011.06.014) is shown on the poster.

## License

- [MIT](https://github.com/michabirklbauer/peptide_matching_game/blob/master/LICENSE)

## Contact

- [micha.birklbauer@gmail.com](mailto:micha.birklbauer@gmail.com)
