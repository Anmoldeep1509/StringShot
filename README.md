# StringShot
Simple Project to handle and manipulate large data sets made of strings


## Todo-

 - [ ] Write XLS to CSV converter
 - [X] Write appending function
 - [ ] Create feature chooser method
 - [ ] Make GUI for operations
 - [ ] Shift System to NodeJS and Python3 for future support


## Setup

Just install the dependencies using this:
```python
pip install -r requirements.txt
```

put your data in a new folder named 'data' this way:

* put excel files in 'xls' folder
* generated csv files will be saved in 'csv' folder


## Files and purpose:

### dataSetSpacer: (temporary hack) 
	Creates txt file for every excel file to put the data into simple text format.

## Reference Links

1. Excel to CSV conversions:
Method 1 from https://www.geeksforgeeks.org/convert-excel-to-csv-in-python/
2. Directory Listing: 
os.listdir() method from https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
3. sample requirements.txt (python): 
https://github.com/uber/Python-Sample-Application/blob/master/requirements.txt
4. Checking python module versions: 
pip freeze method from https://stackoverflow.com/questions/20180543/how-to-check-version-of-python-modules
5. File base name extraction:
path.plittext method from https://stackoverflow.com/questions/678236/how-to-get-the-filename-without-the-extension-from-a-path-in-python 
