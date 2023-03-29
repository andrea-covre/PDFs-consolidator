"""
Merge PDFs in a directory
Andrea Covre
March 29th, 2023

This script merges all PDFs in a directory into a single PDF file.
"""

import os
import argparse

try:
    import PyPDF2
    
except ModuleNotFoundError as e:
    print("PyPDF2 library is not installed, please install it using pip (e.g. pip install PyPDF2).")

def parse_args():

	# create an argparse object and set up the command-line arguments
	parser = argparse.ArgumentParser(description='Program to process files in a directory.')
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('-r', '--root', action='store_true', help='Use the root directory.')
	group.add_argument('-d', '--directory', type=str, help='Specify a directory to use.')

	args = parser.parse_args()

	if args.root:
		directory = os.getcwd()
		print(f"\n> Using ROOT directory: {directory}\n")
	else:
		directory = args.directory
		print(f"\n> Using directory: {directory}\n")

	return directory

def merge_pdfs(pdfs_list, destination):
	# create a new PDF file object
	output_pdf = PyPDF2.PdfWriter()

	counter = 0
	# loop through the list of pdf files and add them to the output pdf file object
	for pdf_file in pdfs_list:
		# adding TOC entry
		output_pdf.add_outline_item(pdf_file, counter)
		pdf_path = os.path.join(destination, pdf_file)
		input_pdf = open(pdf_path, 'rb')
		input_pdf_reader = PyPDF2.PdfReader(input_pdf)
  
		for i in range(len(input_pdf_reader.pages)):
			output_pdf.add_page(input_pdf_reader.pages[i])
			counter += 1
   
		input_pdf.close()
	

	# create the output pdf file
	dest_path = os.path.join(destination, 'MERGED_PDFS.pdf')
	with open(dest_path, 'wb') as output_file:
		output_pdf.write(output_file)
  
	print("\n> Merged PDFs created successfully at:", dest_path)

def main():
	dir_path = parse_args()

	# loop through all files in the directory
	file_list = os.listdir(dir_path)
	file_list.sort()
	pdfs_list = []
	
	print("Files to be merged:")
	for file_name in file_list:
		if os.path.isfile(os.path.join(dir_path, file_name)) and file_name.endswith(".pdf"):
			print('\t-', file_name)
			pdfs_list.append(file_name)
	
	continue_ = input(f"\nContinue to merge {len(pdfs_list)} PDFs? (y/n): ")
 
	if continue_.lower() == 'y':
		merge_pdfs(pdfs_list, dir_path)
		print("\n> Done\n")
	
	else:
		print("\n> Aborted\n")


if __name__ == '__main__':
    main()