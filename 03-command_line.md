# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 1. mkdir = makes directory
> > 2. cp = copy a file or directory
> > 3. mv = move a file or directory
> > 4. rmdir = remove directory
> > 5. less = page through a file ("q" to quit)
> > 6. grep = find things inside files
> > 7. cd = change directory
> > 8. ls = list directory
> > 9. xargs = execute arguments
> > 10. man = read a manual page

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 1. ls = list directory
> > 2. ls -a = list all files and folders
> > 3. ls -l = list directory in long list format
> > 4. ls -lh = list directory with unix suffixes
> > 5. ls -lah = list all files and folder with unix suffixes
> > 6. ls -t = list directory sorted by time modified
> > 7. ls -Glp = list directory colored, long list format, and with a / after if file is a directory

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 1. ls -d
> > 2. ls -R
> > 3. ls -g
> > 4. ls -m
> > 5. ls -G

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > 'xargs' is used to "construct argument list(s) and execute utility" according to the man page. An example of how to use it: find ./temp -print | xargs grep "file". This finds all the files in my temp folder and passes grep to search for "file".

 

