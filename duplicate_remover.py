import os
import hashlib
import argparse

def get_file_hash(file_path):
    """Compute SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicates(folder):
    """Find duplicate files in each folder separately and return files to delete."""
    files_to_delete = []
    total_size = 0

    for root, _, files in os.walk(folder):
        file_map = {}  # {hash: (earliest_created_file, creation_time)}

        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_hash = get_file_hash(file_path)
                creation_time = os.path.getctime(file_path)
                
                if file_hash in file_map:
                    # Compare creation times
                    if creation_time < file_map[file_hash][1]:
                        files_to_delete.append(file_map[file_hash][0])
                        total_size += os.path.getsize(file_map[file_hash][0])
                        file_map[file_hash] = (file_path, creation_time)
                    else:
                        files_to_delete.append(file_path)
                        total_size += os.path.getsize(file_path)
                else:
                    file_map[file_hash] = (file_path, creation_time)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

    return files_to_delete, total_size

def main():
    parser = argparse.ArgumentParser(description="Delete duplicate files in each folder separately, keeping the earliest created file.")
    parser.add_argument("folder", help="Path to the folder to process.")
    parser.add_argument("--dry-run", action="store_true", help="List files that would be deleted without deleting them.")

    args = parser.parse_args()
    
    files_to_delete, total_size = find_duplicates(args.folder)
    
    if args.dry_run:
        print("\nDry Run: Files that would be deleted:")
        for file in files_to_delete:
            print(file)
        print(f"\nTotal files: {len(files_to_delete)}")
        print(f"Total size: {total_size / (1024 * 1024):.2f} MB")
    else:
        for file in files_to_delete:
            os.remove(file)
        print(f"Deleted {len(files_to_delete)} files, freeing up {total_size / (1024 * 1024):.2f} MB.")

if __name__ == "__main__":
    main()
