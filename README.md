# Usage Documentation

This script merges all PDF files in a specified directory or the current working directory into a single PDF file. To use this script, follow the steps below:

## Prerequisites

This script requires the following:

- Python 3
- PyPDF2 library

If the PyPDF2 library is not installed, run the following command to install it:

```
pip install PyPDF2
```

## Arguments

The script accepts the following command-line arguments:

- `-r`, `--root`: Use the current working directory as the directory to search for PDF files. This is a mutually exclusive argument with `-d`.
- `-d`, `--directory`: Specify a directory to use as the directory to search for PDF files. This is a mutually exclusive argument with `-r` and requires a directory path to be provided as an argument.

## Usage

To use this script, navigate to the directory where the Python file is saved and run the following command:

```
python merge_pdfs.py [-h] [-r | -d DIRECTORY]
```

If the `-r` argument is used, the script will use the current working directory as the directory to search for PDF files. If the `-d` argument is used, the script will use the directory path specified after `-d` as the directory to search for PDF files.

Once the script is executed, it will display a list of PDF files found in the specified directory and ask for confirmation to merge them. If confirmed, the script will create a new PDF file in the specified directory called MERGED_PDFS.pdf containing all the PDF files found.

## Example

To merge all PDF files in the current working directory, run the following command:

```
python merge_pdfs.py -r
```
To merge all PDF files in a directory called _path_to_pdfs_ located in the current working directory, run the following command:

```
python merge_pdfs.py -d path_to_pdfs
```
