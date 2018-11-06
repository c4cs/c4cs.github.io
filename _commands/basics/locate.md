---
---
 
locate
---
  
`locate` :  a command used to search a database for the location of files  

```bash
# Sample command and output format
$ locate FILENAME
$ /home/user/Documents/FILENAME
```
<!--more-->

### Common examples of commands using locate:

Each command is followed by a sample output format.

```bash
 $ locate FILENAME # Outputs the complete path of the file
 $ /home/user/Documents/FILENAME 
```

Adding `-i` tells locate to ignore case while searching.

```bash
 $ locate -i *FILENAME*
 $ /home/user/Documents/FILENAME
 $ /home/user/Downloads/filename
```

Locate can also be used to search for a string in a file name. Additionally, adding `-c` outputs the number of occurrences.

```bash
 $ locate -c STRING # Outputs the count of the occurrences of the string
 $ 34
```

Type `man locate` in your terminal to check out the man page for more information!
