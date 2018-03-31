---
---

pdftk
---
`pdftk` is a command that is used to manipulate Portable Document Format (PDF) files. There are many ways to manipulate PDFs through the command such as merging, splitting, encrypting and much more. 
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~bash
$ pdftk in1.pdf in2.pdf cat output combinedIn.pdf
~~~

<!--more-->

### Useful Options / Examples

#### Unlock a PDF File -- Decryption
~~~bash
$ pdftk locked.pdf input_pw YouShallPass output unlocked.pdf
~~~

This allows you to decrpyt pdf files through inputing a password, in this case "YouShallPass", and direct the output into a file named `unlocked.pdf`.

#### Split a PDF File into Seperate Pages
~~~bash
$ pdftk in1.pdf burst
~~~

This allows you to split each of the pdf pages within the 'in1.pdf' file into seperate pages within the current directory. In addition, it will also create a 'doc_data.txt' that will give you the data of the original pdf.

#### Remove Pages Within a PDF File
~~~bash
$ pdftk in1.pdf cat 1-4 12-end output out1.pdf
~~~

This allows you to remove pages from a pdf. In this example pages 5 through 11 will be removed from the 'in1.pdf'. So, in order to remove pages in the command type which pages you want to keep i.e. 1-4 and 12-end which means that page 1 through 4 as well as page 12 until the end of the document.

#### Page Rotation
~~~bash
$ pdftk in1.pdf cat 1east 2-end output out1.pdf
~~~

This allows you to rotate the first page of the file in1.pdf by 90 degrees clockwise. Other flags could include `1west`, which would rotate first page by 90 degrees counter-clockwise. Or `1south`, which would rotate the first page 180 degrees. Other possible flags include `left`, `right`, and `down`. 

