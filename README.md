<HTML>
  <h1>RUN - COMMAND LINE TOOL</h1>
  <p>Do you think that it sucks having to gcc and ./ every time you want to <br>
    run a .c file?</p>
  <p>THEN THIS TOOL IS FOR YOU<br>
    Written in Python, this quick script will compile and run your .c file in no <br>
    time! You even have the opportunity to add options and redirect input and output!
  </p>
</HTML>

# INSTALLATION
```
cd path/to/where/you/want/to/keep/the/program
git clone <this repository>
cd run/
sudo ./setup.sh
```
The setup only puts a symlink from /usr/local/bin/run to where you cloned the repository.

## Uninstall
```
rm /usr/local/bin/run
rm -r /path/to/repo
```
