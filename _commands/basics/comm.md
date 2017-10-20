---
---

comm
---
Compares two sorted files line by line and writes three columns to standard output.
<!-- one line explanation would go here -->

<!-- minimal example -->
~~~ bash
cat words1.txt
Apple
Banana
Orange

cat words2.txt
apple
banana
orange

comm words comm words1.txt words2.txt
Apple
Banana
Orange
        apple
        banana
        orange

comm -i words1.txt words2.txt
            Apple
            Banana
            Orange
~~~

<!--more-->

### Useful Options / Examples

#### Example command

##### Break it down

#### Example command

##### Break it down
