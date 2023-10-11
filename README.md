# Chemical Similarity Calculation Script

## Overview

This script is designed to perform chemical similarity calculations between a set of molecular templates and a collection of compounds. It utilizes the Open Babel (`obabel`) tool for generating molecular fingerprints and computing the similarity between each template and compound pair. The results are stored in CSV format for further analysis.

## Prerequisites

Before using this script, ensure you have the following prerequisites:

1. **Open Babel (`obabel`) Tool**: This script relies on the 'obabel' command-line tool to calculate chemical similarity. Make sure 'obabel' is installed and accessible from the command line.

2. **Python**: The script is written in Python and should be executed using a Python interpreter.

3. **Input Data**: Prepare a directory structure containing your molecular templates and compounds in SDF (Structure-Data File) format. The script reads SDF files from two specified directories: 'template/' for templates and 'cpds/' for compounds.

## Configuration

At the beginning of the script, you can configure the following parameters:

- `file_type`: The file extension for your SDF files (e.g., '.sdf').

- `similarity_threshold`: The similarity threshold to consider two molecules as highly similar.

- `fp_type`: The fingerprint type to be used for similarity calculations. You can choose between 'MACCS' or 'fFP2' by commenting/uncommenting the lines accordingly.

## Usage

1. Place the script in a directory where you have the 'template/' and 'cpds/' subdirectories containing your SDF files.

2. Run the script by executing it with Python. You can use the following command:

   ```bash
   python chemical_similarity.py
   ```

   This will initiate the similarity calculations between the templates and compounds.

3. The script generates two output files:

   - `output<fp_type>.csv`: A CSV file containing similarity values between templates and compounds.

   - `outfile_<fp_type>.res`: A text file listing combinations with high similarity.

## Output

- The CSV output file (`output<fp_type>.csv`) contains rows and columns, with each cell representing the similarity score between a template and a compound.

- The text output file (`outfile_<fp_type>.res`) lists combinations where the similarity value is equal to or greater than the specified threshold.

## Notes

- Ensure that the 'obabel' tool is installed and accessible from your command line. The script constructs and executes 'obabel' commands for each template-compound pair.

- If you choose to use 'fFP2' instead of 'MACCS', uncomment the corresponding line in the script.

- Please review and clean the output CSV file and text file for your specific analysis.

- If you encounter any issues or have questions, feel free to ask for assistance.

Enjoy using this script for your chemical similarity calculations!
