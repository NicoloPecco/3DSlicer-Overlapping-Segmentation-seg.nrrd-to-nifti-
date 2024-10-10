#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:58:27 2024

@author: pecco.nicolo
"""

import SimpleITK as sitk
import numpy as np
import os
import slicerio

def remove_files_with_prefix(folder_path, prefix):
    # List all files in the specified directory
    for filename in os.listdir(folder_path):
        # Check if the file starts with the specified prefix
        if filename.startswith(prefix):
            file_path = os.path.join(folder_path, filename)
            try:
                # Remove the file
                os.remove(file_path)
                print(f'Removed: {file_path}')
            except Exception as e:
                print(f'Error removing {file_path}: {e}')


# Load the NRRD file

nrrd_file_path = "your_path_to_seg.nrrd_file/target_biopsy_new.seg.nrrd"  # Replace with your NRRD file path
output_dir = "your_output_path/"  # Replace with your output directory

segmentation = slicerio.read_segmentation(nrrd_file_path)

seg_names=slicerio.segment_names(segmentation)

# Create a loop to save each segmentation
for segment_name in seg_names:
    # Assuming each segment corresponds to a unique label value
    # label_value = seg_names.index(segment_name) + 1  # Labels typically start from 1
    segment_names_to_labels = [(segment_name, 1)]
    
    # Extract the segment
    extracted_segmentation = slicerio.extract_segments(segmentation, segment_names_to_labels)
    
    # Define the output filename for each segment
    segment_output_filename = os.path.join(output_dir, f"{segment_name}.nrrd")
    segment_output_filename_nifti=os.path.join(output_dir, f"Biopsy_{segment_name}.nii.gz")
    # Save the extracted segment
    slicerio.write_segmentation(segment_output_filename, extracted_segmentation)
    
    img = sitk.ReadImage(segment_output_filename)
    sitk.WriteImage(img, segment_output_filename_nifti)

# prefix = 'Seg'                # Replace with your desired prefix
# remove_files_with_prefix(output_dir, prefix)
    
# subprocess.run(["fslmerge","-t","/Users/pecco.nicolo/Desktop/prova_nrrd/out.nii.gz","/Users/pecco.nicolo/Desktop/prova_nrrd/Bio*"], capture_output=True)

# files_to_merge = glob.glob('/Users/pecco.nicolo/Desktop/prova_nrrd/Bio*')
# command = ['fslmerge', '-t', '/Users/pecco.nicolo/Desktop/prova_nrrd/All_Biopsy.nii.gz'] + files_to_merge
    
#     # Run the command

# result = subprocess.run(command, capture_output=True, text=True)

# # Example usage
# prefix = 'Bio'                # Replace with your desired prefix
# remove_files_with_prefix(output_dir, prefix)






