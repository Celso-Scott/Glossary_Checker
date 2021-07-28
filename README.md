# 84000
# Glossary Checker
This is a simple script for markup to double check the glossary entries in our TEI to assure that there aren't any spelling errors in the Tibetan field.

## Requirements:
You'll need to install [Python 3 or higher](https://www.python.org/downloads/) to run the script. I have not yet tested if there are any issues for Mac users. On Windows, once Python is installed you only need to double click the .py script to run it.

To download the script simply click on the green "Code" button above and select "Download ZIP". Then unzip the downloaded file.

## Running the script:
To run the script. You will need to place a copy of the TEI file into the "Glossary Checker" folder. Then rename the file to "input.xml". This will tell the script to read and check this file's glossary. The script reads the Tibetan Unicode, so the TEI file will need to first be minimally processed in terms of having 1) the glossary added, 2) Wylie terms separated into there own tags if they are separated by commas or semicolons, and 3) the Tibetan Unicode automatically generated after the file is saved to the database.

You will need to place the text file in which the glossary will be searched against into the "Glossary Checker" folder as well. Go to [Utilities](utilities.84000-translate.org) Find the text's Toh number and download the "toh###-bo.txt" file. Place the downloaded text file in the folder and rename it as "source.txt". No need to worry about removing the page number tags in the text file, the script will ignore these.

Then simply, double click the "check_glossary.py" script to run it. If it is set up correctly it will generate a file called "not_in_source.txt". This will give you a list of every glossary term with a string that is not found in the source text.

You will need to investigate why that is. Sometimes there is a legit reason the term isn't in the source: perhaps an alternate Kangyur edition was used and indicated by a note; sometimes there is a ། between the syllables; or a suitable ommission/inclusion of a case particle; I'll leave it up to you to investigate what is fine and what needs to be corrected.

Beware that often there are input errors in the eKangyur. If you suspect there is one use the "dege_kangyur_scan_checker-v3" included in this folder to check the scans. If you find that it is an input error rather than an error in the glossary, please report the error [here](https://docs.google.com/spreadsheets/d/1Wdsygc_EI8GUNl3_-4Z50q_D0FChWS1hFPj9oIpaT18/edit?usp=sharing), and I will correct it when I get a chance. 
