# Plagiarism-Checker

**Plagiarism Checker**


This repository contains a plagiarism checker tool that allows users to compare a source file with one or more target files and calculate a plagiarism score based on their textual similarity. The plagiarism checker is built using TF-IDF embeddings and cosine similarity.

**Usage**

To use the plagiarism checker:

Clone this repository to your local machine:
git clone https://github.com/koundinyapk/Plagiarism-Checker.git

Navigate to the cloned repository directory:
cd plagiarism-checker

Run the plagiarism checker script:

python plagiarism_checker.py
Follow the prompts to upload the source file and one or more target files.

The plagiarism checker will calculate a plagiarism score for each pair of source and target files based on their textual similarity.

**Methodology**

The plagiarism checker utilizes TF-IDF (Term Frequency-Inverse Document Frequency) embeddings to represent the textual content of the source and target files. Cosine similarity is then applied to measure the similarity between the embeddings of the source and target files. The resulting similarity score indicates the degree of plagiarism between the files, with higher scores indicating greater similarity.

**Dependencies**


The plagiarism checker requires the following dependencies:

numpy: For numerical operations and array manipulation.
sklearn: For TF-IDF vectorization and cosine similarity calculation.
django: For web framework support (optional).

These dependencies can be installed using pip:
pip install numpy scikit-learn django

**Contributing**


Contributions to the plagiarism checker tool are welcome! If you encounter any issues, have feature requests, or would like to contribute enhancements, please feel free to open an issue or submit a pull request.

