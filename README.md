# KnockKnockJokeEmailScript
Will automatically email a knock knock joke to a person using a list of jokes


# Manifest

./resources - Directory contains information needed by python script <br>
&nbsp;&nbsp;&nbsp;- ./database - Contains information used to track jokes <br>
&nbsp;&nbsp;&nbsp;- ./jokes - Contains list of jokes. Can be edited if following same format <br><br>
./.gitignore - Git config file <br><br>
./Main.py - Main python script<br><br>
./README.md - This file<br><br>
./install - Install script for related dependencies



# RUNNING

Ensure that you have python 3 and pip, then run the install script. From the directory containing source files, run the 
commands:

 $ chmod +x install <br>
 $ ./install
 
 Note that you may have to run the install script as sudo
 
After that, create a .env file. Do this by copying the sample file and changing its attributes. First use:

 $ cp SAMPLE_ENV .env
 
This will create the proper .env file for use with the script. Next, edit the file to contain valid information. Open 
in an editor and change the EMAIL value to the sender address, the PASS to the password of the sender's account, and the
TO value to the intended recipient of the mail. 

(NOTE!)

This will only work with gmail accounts that have been set up to use less secure apps applications through security settings and
have generated a password key for the script. See less secure apps and app passwords.