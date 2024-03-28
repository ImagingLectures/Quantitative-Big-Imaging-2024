import argparse
import os
import re

"""
Update the year in the repository. Search for all markdown files and update the urls.
Args:
    year (int): The year to update to
    root_path (str): The root path of the repository
    verbose (bool): Print verbose output
    dry_run (bool): Dry run, do not update files

Example:

```bash
python common/scripts/update_repo_year.py -p path/to/repo -py 2022 -ny 2024 -v -d
```

"""

def setup_parser():
    parser = argparse.ArgumentParser(description='Update the year in the repository. Search for all markdown files and update the urls.')
    parser.add_argument('-ny','--new_year', type=int, help='The year to update to', required=True)
    parser.add_argument('-py','--prev_year', type=int, help='The year to update from', required=True)
    parser.add_argument('-p','--root_path', type=str, help='The root path of the repository', required=True)
    parser.add_argument('-v','--verbose', action='store_true', help='Print verbose output')
    parser.add_argument('-d','--dry_run', action='store_true', help='Dry run, do not update files')

    args = parser.parse_args()

    return args



def main(args):

    new_year = args.new_year
    prev_year = args.prev_year
    root_path = args.root_path

    search_pattern = f"Quantitative-Big-Imaging-{str(prev_year)}"
    target_pattern = f"Quantitative-Big-Imaging-{str(new_year)}"

    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                if search_pattern in content:
                    updated_content = re.sub(search_pattern, target_pattern, content)
                    if args.verbose:
                        print(f"\033[93mFound difference in {file_path=}:\033[0m")
                        for line1, line2 in zip(content.splitlines(), updated_content.splitlines()):
                            if line1 != line2:  
                                print(f"\033[91m-{line1}\033[0m")  # Print in red
                                print(f"\033[92m+{line2}\033[0m")  # Print in green
                                print()
                        print()

                    if not args.dry_run:
                        with open(file_path, 'w') as f:
                            f.write(updated_content)
                if search_pattern.lower() in content:
                    updated_content = re.sub(search_pattern.lower(), target_pattern.lower(), content)
                    if args.verbose:
                        print(f"\033[93mFound difference in {file_path=}:\033[0m")
                        for line1, line2 in zip(content.splitlines(), updated_content.splitlines()):
                            if line1 != line2:  
                                print(f"\033[91m-{line1}\033[0m")  # Print in red
                                print(f"\033[92m+{line2}\033[0m")  # Print in green
                                print()
                        print()

                    if not args.dry_run:
                        with open(file_path, 'w') as f:
                            f.write(updated_content)

                    
    if args.dry_run:
        print(f'Dry run: No file was updated!') 
    else:
        print(f'Updated all markdown files in {root_path} to year {new_year}.')

if __name__ == '__main__':

    args = setup_parser()
    main(args)

    