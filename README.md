# SAKAI-Auto-Judge-MOSS-Detection
Some useful scripts for SAKAI code extraction and plagiarism detection

## Installation
Install all extracting support packages.
### Ubuntu/Debain
```bash
sudo apt-get update
sudo apt-get install p7zip-full rar
```

## Usage
```bash
# Eaxmple
./extract.py bulk_download.zip
./moss.sh -l java -m 20 -d ./judge/*/*/*/*.java ./judge/*/*/*/*/*.java ./judge/*/*/*/*/*/*.java
```
