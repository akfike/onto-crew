import os

# Specify the directory containing the markdown files
directory = 'mds'
output_file = 'proposal_summary.md'

# Open the output file in write mode
with open(output_file, 'w') as outfile:
    # Iterate over all files in the directory
    for filename in sorted(os.listdir(directory)):
        # Check if the file is a markdown file
        if filename.endswith('.md'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as infile:
                # Write the content of each markdown file into the output file
                outfile.write(infile.read())
                # Add a newline or two between files
                outfile.write("\n\n")

print(f'All markdown files have been concatenated into {output_file}')
