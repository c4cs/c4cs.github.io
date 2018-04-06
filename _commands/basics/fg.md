---
---

fg
--
The fg command continues a stopped job by running it in the foreground
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
fg  jobId 
~~~
jobId specifies the program you want to send to the foreground
<!--more-->

### Useful Options / Examples


##### Will run the latest program that was suspended or backgrounded

~~~ bash
fg
~~~

##### Will bring the program with the id 1 into the foreground

~~~ bash
fg %1
~~~

##### You may bring more than one program into the foreground at once

~~~ bash
fg jobId1 jobId2 ...
~~~

##### Job Id specifications

~~~ bash
%number: Use the job number such as %1 or %2
%+ or %%: refers to the current job
%-: refers to the previous job
%string: Use the string whose name begins with the suspended command such as %commandname or %ping
~~~



#### Once a program is brought into the foreground, you can kill it with ctrl-c, let it complete, or suspend and background it again.
