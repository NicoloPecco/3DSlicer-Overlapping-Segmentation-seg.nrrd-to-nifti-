**NRRD to NIfTI Converter for 3D Slicer Segmentations**

This script converts an **overlapping segmentation .seg.nrrd file from 3D Slicer into separate .nii.gz NIfTI files**. The code processes each segmentation within the .nrrd file and saves them as individual NIfTI files.

Requirements

To use this script, ensure the following Python packages are installed:

- SimpleITK
- numpy
- slicerio

**Usage**

Update the nrrd_file_path and output_dir variables in the script with your desired .nrrd input file and output directory:

1) nrrd_file_path = "your_path_to_seg.nrrd_file/target_biopsy_new.seg.nrrd"  # Replace with your NRRD file path
2) output_dir = "your_output_path/"  # Replace with your output directory
3) Run the script in terminal: python3 path_to_py_code/code.py

**Key Features**

Overlapping Segmentations: Supports segmentations with overlapping regions from 3D Slicer.
NRRD to NIfTI: Converts .nrrd files to .nii.gz format for easier handling in other medical image processing tools.
Segmentation Labels: Each segmentation is saved as a separate file, with filenames reflecting the segmentation names.

Hope you'll find it usefull! 
