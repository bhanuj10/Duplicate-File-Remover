### **Title:**  
**Duplicate File Remover (Per Folder Basis)**  

---

### **Description:**  
This Python script scans a given directory and its subdirectories, identifying duplicate files **within each folder separately** based on their content. It keeps only the earliest created file and deletes the rest. It does not check for duplicates across different folders.  

Features:  
✅ Detects duplicate files using SHA-256 hashing.  
✅ Keeps the earliest created file in each folder.  
✅ Provides a **dry-run** mode to preview deletions before executing them.  
✅ Supports recursive scanning of subdirectories.  

---

### **Usage Instructions**  

#### **1. Prerequisites**  
Ensure you have Python installed (Python 3.x recommended).  

#### **2. Installation**  
Clone this repository or download the script:  
```sh
git clone https://github.com/yourusername/duplicate-file-remover.git
cd duplicate-file-remover
```

#### **3. Running the Script**  

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

### **Example Output (Dry Run Mode)**  
```
Dry Run: Files that would be deleted:
  /path/to/folder/file1 (Duplicate of file2)
  /path/to/folder/subfolder/file3 (Duplicate of file4)

Total files: 10
Total size: 45.32 MB
```

---

### **How It Works**
1. The script scans all files in each folder separately.  
2. It computes a **SHA-256 hash** for each file to detect duplicates.  
3. Among duplicates, it retains the **earliest created file** and schedules the others for deletion.  
4. The `--dry-run` mode allows safe preview before actual deletion.  

---

Enjoy deleting 🗑️🗑️🗑️🚮