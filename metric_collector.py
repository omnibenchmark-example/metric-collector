import argparse
import os

def concatenate_input_content(input_files):
    concatenated_content = ""  # Initialize an empty string to hold the concatenated content
    
    # Iterate over each input file
    for input_file in input_files:
        # Open each input file in read mode and read its content
        with open(input_file, 'r') as file:
            # Read the content of the input file and append it to the concatenated_content string
            concatenated_content += file.read()
            # Optionally, you can add a newline between the content of each file
            concatenated_content += '\n'

    return concatenated_content


def aggregate_metrics_mapping(output_dir, input_files):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    content = concatenate_input_content(input_files)

    biometrics_tsv = os.path.join(output_dir, 'biometrics.tsv')
    with open(method_mapping_file, 'w') as file:
        file.write(content)

    biometrics_report_html = os.path.join(output_dir, 'biometrics_report.html')
    with open(biometrics_report_html, 'w') as file:
        file.write("<html><body>\n")
        file.write("<h2>Input Files</h2>\n<ul>\n")
        for file_name in input_files:
            file.write(f"<li>{file_name}</li>\n")
        
        file.write("</ul>\n</body></html>\n")


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Run method on files.')

    # Add arguments
    parser.add_argument('--output_dir', type=str, help='output directory where method will store results.')
    parser.add_argument('--metrics.mapping', type=str, nargs='+', help='Metrics mapping file.')

    # Parse arguments
    args, _ = parser.parse_known_args()

    metrics_mapping_files = getattr(args, 'metrics.mapping')
    output_dir = getattr(args, 'output_dir')

    aggregate_metrics_mapping(output_dir, metrics_mapping_files)


if __name__ == "__main__":
    main()