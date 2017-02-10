---
---

make
-------

Simply put, this command can compile code into an executable without having to type a super long compilation sequence. We can use the make utility to automate many tasks in the development process, including compilation and regression testing.

~~~ bash
$ make main
c++     main.cpp   -o main
$ ./main
~~~


<!--more-->

### Useful Options / Examples

In order to do more, we need to create something called a Makefile. There's quite a few tutorials online for how to write a Makefile, but it's usually easiest to grab a Makefile that already exists and modifying the recipes for your project. Take a look at the Makefile below from EECS 280.

Makefiles are comprised of "targets" which execute some task.

~~~ bash
# Here is a comment!
target: dependencies
[tab] command
# Careful! make is one of those old programs that's really finicky about whitespace
# It has to be an actual <tab> character here, not a bunch of spaces!
~~~

If you just type `make` without specifying a target, it will run the first target in the file. If you type a specific target name like `make test` it will run the target with that name. If we haven't run the target before or if any of the dependencies have changed, make will go ahead and run whatever command is specified after the tab character on the next line.

There are some special characters in Makefiles that might be confusing. [Here](https://www.gnu.org/software/make/manual/make.html#Automatic-Variables) is a good reference. Basically we need to tell make what to do with the files we have listed for the target. We want to compile all the files listed into an executable, using the compiler flags (denoted as the variable `CXXFLAGS`) we've set at the beginning.

#### Example command
~~~ bash
$ make Matrix_tests.exe
g++ --std=c++11 -Wall -Werror -pedantic -O1 Matrix_public_test.cpp Matrix.cpp Matrix_test_helpers.cpp -o Matrix_public_test.exe
~~~

##### Break it down
`make Matrix_tests.exe` refers to the target by the same name. This target stitches together all the cpp files needed to compile `Matrix_public_test.exe`. Take a look at the target:

```make
Matrix_tests.exe: Matrix_tests.cpp Matrix.cpp Matrix_test_helpers.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@
```

The _name_ of the target is `Matrix_tests.exe`. The cpp files we want to compile are `Matrix_tests.cpp`, `Matrix.cpp`, and `Matrix_test_helpers.cpp`. We want to use the compiler on our machine which is the _variable_ `CXX` with the flags from the _variable_ `CXXFLAGS`. We have to denote that we want to use a variable by using the `$` symbol.

#### Example command
~~~ bash
$ make clean
rm -vf *.exe *.out.txt *.out.ppm
Image_public_test.exe
Image_tests.exe
Matrix_public_test.exe
Matrix_tests.exe
processing_public_tests.exe
resize.exe
~~~

##### Break it down
`make clean` in this Makefile is set up to remove all executables, `.out.txt` and `.out.ppm` files. This is good to have if you want a nice clean start before you compile again.


### Final Remarks

Makefiles can save you a lot of time from having to type out long compilation sequences or running test suites!

If Makefiles really excite you, check out this [Super Makefile](https://github.com/awdeorio/supermakefilecxx/blob/master/Makefile) Professor DeOrio has created!


```make
# Makefile
# Build rules for EECS 280 project 2

# Compiler can be changed by changing the variable CXX. It is pre-defined by make to be set to the default system.
# I.e. Mac = clang, CAEN = g++, etc...
# CXX =

# Set this at the command line using: make debug_or_optimize=<flag> <target> ...
debug_or_optimize = -O1

# Compiler flags
CXXFLAGS = --std=c++11 -Wall -Werror -pedantic $(debug_or_optimize)

test: release
	./Matrix_public_test.exe
	./Image_public_test.exe
	./processing_public_tests.exe dog
	./processing_public_tests.exe crabster
	./processing_public_tests.exe horses
	./resize.exe dog.ppm dog_4x5.out.ppm 4 5
	diff dog_4x5.out.ppm dog_4x5.correct.ppm

release: Matrix_public_test.exe Matrix_tests.exe Image_public_test.exe \
		 Image_tests.exe processing_public_tests.exe resize.exe

debug: debug_or_optimize = -g
debug: Matrix_public_test.exe Matrix_tests.exe Image_public_test.exe \
	   Image_tests.exe processing_public_tests.exe resize.exe

Matrix_public_test.exe: Matrix_public_test.cpp Matrix.cpp Matrix_test_helpers.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

Matrix_tests.exe: Matrix_tests.cpp Matrix.cpp Matrix_test_helpers.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

Image_public_test.exe: Image_public_test.cpp Matrix.cpp Image.cpp \
			Matrix_test_helpers.cpp Image_test_helpers.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

Image_tests.exe: Image_tests.cpp Matrix.cpp Image.cpp Matrix_test_helpers.cpp \
			Image_test_helpers.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

processing_public_tests.exe: processing_public_tests.cpp Matrix.cpp \
				Image.cpp processing.cpp \
				Matrix_test_helpers.cpp Image_test_helpers.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

resize.exe: resize.cpp Matrix.cpp Image.cpp processing.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

clean:
	rm -vf *.exe *.out.txt *.out.ppm

```