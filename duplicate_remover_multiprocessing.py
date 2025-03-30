import os
import hashlib
import argparse
import multiprocessing

def get_file_hash(file_path):
    """Compute SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None
    return hasher.hexdigest()

def process_folder(folder):
    """Find duplicate files in a given folder and return files to delete."""
    file_map = {}  # {hash: (earliest_created_file, creation_time)}
    files_to_delete = []
    total_size = 0

    try:
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)

            if os.path.isfile(file_path):
                file_hash = get_file_hash(file_path)
                if file_hash is None:
                    continue  # Skip unreadable files

                creation_time = os.path.getctime(file_path)

                if file_hash in file_map:
                    # Keep the earliest created file
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
        print(f"Error processing {folder}: {e}")

    return files_to_delete, total_size

def find_duplicates_parallel(root_folder, dry_run):
    """Use multiprocessing to handle each folder separately."""
    folders = [os.path.join(root_folder, d) for d in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, d))]
    folders.append(root_folder)  # Also process the root folder itself

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(process_folder, folders)

    total_files_deleted = sum(len(files) for files, _ in results)
    total_size_deleted = sum(size for _, size in results)

    if dry_run:
        print("\nDry Run: Files that would be deleted:")
        for files, _ in results:
            for file in files:
                print(file)
        print(f"\nTotal files: {total_files_deleted}")
        print(f"Total size: {total_size_deleted / (1024 * 1024):.2f} MB")
    else:
        for files, _ in results:
            for file in files:
                try:
                    os.remove(file)
                except Exception as e:
                    print(f"Failed to delete {file}: {e}")
        print(f"Deleted {total_files_deleted} files, freeing up {total_size_deleted / (1024 * 1024):.2f} MB.")

def main():
    parser = argparse.ArgumentParser(description="Delete duplicate files in each folder separately using multiprocessing, keeping the earliest created file.")
    parser.add_argument("folder", help="Path to the folder to process.")
    parser.add_argument("--dry-run", action="store_true", help="List files that would be deleted without deleting them.")
    
    args = parser.parse_args()
    find_duplicates_parallel(args.folder, args.dry_run)

if __name__ == "__main__":
    main()
