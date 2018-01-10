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
./moss.sh -l java -m 20 -d $(find ./judge -type f \( -iname "*.java" ! -iname "._*" \) )
```

## TODO

 - [] Integrate with [mosspy](https://github.com/soachishti/moss.py)
 - [] Auto ditinguish different language
 - [] move one students' code into the root of the same directory
