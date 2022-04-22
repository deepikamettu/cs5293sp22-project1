# Changes

* ***Firstly the tree structure of the project has been changed. redactor.py has been placed in the base folder.***  
* ***Secondly, the Pipfile has been updated to Python 3.10 version.***  

* Missing/No Features Found- Names  
* Missing/No Features Found - Gender  
* Missing/No Features Found- Phone Number  
* Missing/No Features  Found- Concept  
* Missing/No Features Found - Dates  
* Missing/No Features - Addresses  
* Missing Stats

For the above point deductions, I have just changed the tree structure of the project and placed the redactor.py file in the base folder location. Intially it was inside project1 which led to no execeution of my program.  

* Output files not stored in respective folder  and File names not re-assigned correctly
I have changed the output() function code in redactor.py file, so that the each file's redacted data is stored in it's corresponding file name with .redacted extension in the user specified location.  


* Errors Running Test  
I have added pytest to the pipfile. I have changed the following function:    
*test_output():*  
This method is used to test output(filelist,data,loc) function defined in redactor.py file. This method asserts True is there exists files with ‘.redacted’ extension in files folder else asserts False.  

