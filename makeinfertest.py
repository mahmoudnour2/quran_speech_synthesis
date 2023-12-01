# import os

# # Set the path to the directory containing your files
# directory_path = '/home/hamza/Downloads/tts-arabic-pytorch/lab_files_bw'

# # Set the output file path
# output_file_path = '/home/hamza/Downloads/tts-arabic-pytorch/data2/infer_test.txt'

# # Create or overwrite the output file
# with open(output_file_path, 'w') as output_file:
#     # Loop through files from 1 to 700
#     for i in range(1, 701):
#         file_name = f'verse_{i}_bw.lab'
#         file_path = os.path.join(directory_path, file_name)

#         # Check if the file exists
#         if os.path.exists(file_path):
#             # Read the content of the file and write it to the output file
#             with open(file_path, 'r') as input_file:
#                 content = input_file.read()
#                 output_file.write(content)
#                 output_file.write('\n')  # Add a newline for separation if needed
#         else:
#             print(f"File not found: {file_name}")

# print(f"Content of files 1 to 700 has been written to {output_file_path}")


# import os

# # Set the path to the directory containing your files
# directory_path = '/home/hamza/Downloads/tts-arabic-pytorch/lab_files'

# # Loop through files in the directory
# for filename in os.listdir(directory_path):
#     if filename.startswith('verse_') and filename.endswith('.lab'):
#         # Extract the number i from the filename
#         i = filename.split('_')[1].split('.')[0]

#         # Construct the new filename
#         new_filename = f'verse_{i}_bw.lab'

#         # Create the full path for the old and new filenames
#         old_path = os.path.join(directory_path, filename)
#         new_path = os.path.join(directory_path, new_filename)

#         # Rename the file
#         os.rename(old_path, new_path)

# print("Files have been renamed.")
###########
import os

# Set the path to the directory containing your verse_i_bw.lab files
lab_directory_path = '/home/hamza/Desktop/quran_speech_synthesis/phones'

# Set the output file path
output_file_path = '/home/hamza/Desktop/quran_speech_synthesis/data2/train_phon.txt'

# Create or overwrite the output file
with open(output_file_path, 'w') as output_file:
    # Loop through files from 1 to 700
    for i in range(701, 4501):
        lab_filename = f'verse_{i}_bw.lab'
        lab_filename2 = f'verse_{i}_bw.wav'
        lab_filepath = os.path.join(lab_directory_path, lab_filename)

        # Check if the lab file exists
        if os.path.exists(lab_filepath):
            # Read the content of the lab file
            with open(lab_filepath, 'r') as lab_file:
                lab_content = lab_file.read().strip()  # Assuming the content should be stripped

            # Write the line to the output file with double quotations
            output_line = f'"{lab_filename2}" "{lab_content}"\n'
            output_file.write(output_line)
        else:
            print(f"Lab file not found: {lab_filename}")

print(f"Content has been written to {output_file_path}")
###########

# import os

# def rename_files(directory_path):
#     for filename in os.listdir(directory_path):
#         if filename.startswith("verse_") and filename.endswith("_phon.lab"):
#             index_str = filename[len("verse_"):-len("_phon.lab")]
            
#             try:
#                 index = int(index_str)
#                 new_filename = f"verse_{index}_bw.lab"
#                 old_filepath = os.path.join(directory_path, filename)
#                 new_filepath = os.path.join(directory_path, new_filename)
                
#                 print(f"Renaming: {old_filepath} to {new_filepath}")
#                 os.rename(old_filepath, new_filepath)
#                 print("Done.")
#             except ValueError:
#                 print(f"Skipping: {filename} - Unable to extract index.")

# if __name__ == "__main__":
#     directory_path = "/home/hamza/Desktop/quran_speech_synthesis/phones"
#     rename_files(directory_path)

