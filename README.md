# **Duplicate File Remover (Per Folder Basis)**  

## **Description**  
This Python script scans a given directory and its subdirectories, identifying duplicate files **within each folder separately** based on their content. It keeps only the earliest created file and deletes the rest. It does not check for duplicates across different folders.  

There are two versions of the script:  

1. **`duplicate_remover.py`** – Single-threaded version (Processes one folder at a time).  
2. **`duplicate_remover_multiprocessing.py`** – Multi-threaded version (Uses multiprocessing to handle multiple folders simultaneously for faster execution).  

---

## **Features**  
✅ Detects duplicate files using SHA-256 hashing.  
✅ Keeps the earliest created file in each folder.  
✅ Provides a **dry-run** mode to preview deletions before executing them.  
✅ Supports recursive scanning of subdirectories.  
✅ **Multiprocessing version speeds up processing by handling multiple folders concurrently.**  

---

## **Usage Instructions**  

### **1. Prerequisites**  
Ensure you have Python installed (Python 3.x recommended).  

### **2. Installation**  
Clone this repository or download the scripts:  
```sh
git clone https://github.com/yourusername/duplicate-file-remover.git
cd duplicate-file-remover
```

---

## **3. Running the Script**  

### **🔹 Using the Single-Threaded Version (`duplicate_remover.py`)**  
This version processes one folder at a time and is useful for smaller directories.  

- **Dry Run (Preview Files to be Deleted):**  
  ```sh
  python duplicate_remover.py /path/to/folder --dry-run
  ```
  - Lists duplicate files per folder.  
  - Shows total number of files and space that would be freed.  

- **Delete Duplicate Files (Permanent Action):**  
  ```sh
  python duplicate_remover.py /path/to/folder
  ```
  - Deletes duplicate files, keeping only the earliest created file in each folder.  

---

### **🚀 Using the Multi-Processing Version (`duplicate_remover_multiprocessing.py`)**  
This version speeds up the process by handling multiple folders simultaneously.  

- **Dry Run (Preview Files to be Deleted):**  
  ```sh
  python duplicate_remover_multiprocessing.py /path/to/folder --dry-run
  ```
  - Uses multiple CPU cores to scan folders in parallel.  
  - Displays duplicate files that would be deleted.  
  - Shows total number of files and space that would be freed.  

- **Delete Duplicate Files (Permanent Action):**  
  ```sh
  python duplicate_remover_multiprocessing.py /path/to/folder
  ```
  - Uses multiprocessing to delete duplicate files faster.  
  - Keeps the earliest created file in each folder.  

---

## **Example Output (Dry Run Mode)**  
```
Dry Run: Files that would be deleted:
  /path/to/folder/file1 (Duplicate of file2)
  /path/to/folder/subfolder/file3 (Duplicate of file4)

Total files: 10
Total size: 45.32 MB
```

---

## **How It Works**
1. The script scans all files in each folder separately.  
2. It computes a **SHA-256 hash** for each file to detect duplicates.  
3. Among duplicates, it retains the **earliest created file** and schedules the others for deletion.  
4. The `--dry-run` mode allows safe preview before actual deletion.  
5. **Multiprocessing version speeds up the process by handling multiple folders in parallel.**  

---

## **Performance Comparison**
| Version                         | Speed     | Best For            |
|---------------------------------|-----------|---------------------|
| **`duplicate_remover.py`**       | Slower🐌    | Small directories   |
| **`duplicate_remover_multiprocessing.py`** | Faster 🚀 | Large directories with many folders |

---

### **License**
This project is open-source under the **MIT License**.  

---

## **Enjoy deleting duplicates 🗑️🗑️🗑️🚮**
