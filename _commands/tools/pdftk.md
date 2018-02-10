---
---

pdftk
---
'pdftk' is a command that is used to manipulate Portable Document Format (PDF) files. There are many ways to manipulate PDFs through the command such as merging, splitting, encrypting and much more. 
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~bash
$ pdftk in1.pdf in2.pdf cat output combinedIn.pdf
~~~

<!--more-->

### Useful Options / Examples

#### 'pdftk locked.pdf input_pw YouShallPass output unlocked.pdf'
~~~bash
$ pdftk locked.pdf input_pw YouShallPass output unlocked.pdf
~~~

This allows you to decrpyt pdf files through inputing a password 'YouShallPass' and create an output of the decrypted file. 

#### 'pdftk in1.pdf burst'
~~~bash
$ pdftk in1.pdf burst
~~~

This allows you to split each of the pdf pages within the 'in1.pdf' file into seperate pages within the current directory. In addition, it will also create a 'doc_data.txt' that will give you the data of the original pdf.

#### 'pdftk in1.pdf cat 1-4 12-end output out1.pdf'
~~~bash
$ pdftk in1.pdf cat 1-4 12-end output out1.pdf
~~~

This allows you to remove pages from a pdf. In this example pages 5 through 11 will be removed from the 'out1.pdf'

#### 'pdftk in1.pdf cat 1east 2-end output out1.pdf'
~~~bash
$ pdftk in1.pdf cat 1east 2-end output out1.pdf
~~~

This allows you to rotate the first page of the pdf file by 90 degrees clockwise.

