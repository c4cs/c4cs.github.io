# locate  
`locate` :  a command used to search a database for the location of files  
#### Examples of commonly used commands:  
```bash
 $ locate FILENAME # Outputs the complete path of the file
 $ /home/user/Documents/FILENAME 
```
```bash
 $ locate -i *FILENAME* # Ignores case when searching for files
 $ /home/user/Documents/FILENAME
 $ /home/user/Downloads/filename
```
Locate can also be used to search for a string in a path where the string is not necessarily a file name. Additionally, adding `-c` outputs the number of occurrences.
```bash
 $ locate -c STRING # Outputs the count of the occurrences of the string
 $ 34
```
