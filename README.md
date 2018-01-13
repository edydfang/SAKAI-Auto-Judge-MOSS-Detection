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
# Another formation of find
find . -type f -not -path "*/\.*" -name "*.java"
```

Also, for the usage of the `MOSS` Please refer to the web site of MIT `MOSS` or the content of `moss.sh`.

Useful Option for `moss.sh`: 

-n 600

where `600` is number of matching files to show in the results.

## Features

 - Extract codes from OJ and SAKAI in a good and robust way
 - Upload and get the analysis results of code similarity from MIT MOSS
 - Download the filter the Report
 - Generate `xlsx` format report from the `html` report
  - Auto matching of the student Id from the file path
  - Auto adding student names from an existing source

## TODO

 - [x] Integrate with [mosspy](https://github.com/soachishti/moss.py)
 - [x] Remove code/report records from OJ when there exists code from SAKAI
 - [x] Generate table from the HTML result
 - [ ] Auto ditinguish different language from SAKAI data
 - [ ] Move one students' code into the root of the same directory
 - [ ] Replace all none ASCII characters in the code with ASCII characters
