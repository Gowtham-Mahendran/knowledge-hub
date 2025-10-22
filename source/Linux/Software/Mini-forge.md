# Miniforge

- Download conda-forge installer from the [website](https://conda-forge.org/download/)

- Go to the directory and run

```bash
bash Miniforge3-$(uname)-$(uname -m).sh
```

Since `uname` outputs `Linux` and `uname -m` outputs `x86_64`, running the command `Miniforge3-$(uname)-$(uname -m).sh` is similar to mentioning the actual file name `Miniforge3-Linux-x86_64.sh`.


- It will ask to read the license agreement and now it will show `end`. Now type `yes` and the installation will begin.

```bash
Miniforge3 will now be installed into this location:
/home/gowtham/miniforge3

- Press ENTER to confirm the location
- Press CTRL-C to abort the installation
- Or specify a different location below
```

Press `ENTER`


- Once installation is done, it prompts

```bash
Do you wish to update your shell profile to automatically initialize conda?
This will activate conda on startup and change the command prompt when activated.
If you'd prefer that conda's base environment not be activated on startup,
run the following command when conda is activated:

conda config --set auto_activate_base false

You can undo this by running `conda init --reverse $SHELL`? [yes|no]
```

If `yes` - Adds Conda to your shell startup file. conda is ready every time. 
If `no` - You’ll have to manually source `~/miniforge3/bin/activate` each time.

press `yes` in this case. 


- Successfully installed

```bash
no change     /home/gowtham/miniforge3/condabin/conda
no change     /home/gowtham/miniforge3/bin/conda
no change     /home/gowtham/miniforge3/bin/conda-env
no change     /home/gowtham/miniforge3/bin/activate
no change     /home/gowtham/miniforge3/bin/deactivate
no change     /home/gowtham/miniforge3/etc/profile.d/conda.sh
no change     /home/gowtham/miniforge3/etc/fish/conf.d/conda.fish
no change     /home/gowtham/miniforge3/shell/condabin/Conda.psm1
no change     /home/gowtham/miniforge3/shell/condabin/conda-hook.ps1
no change     /home/gowtham/miniforge3/lib/python3.12/site-packages/xontrib/conda.xsh
no change     /home/gowtham/miniforge3/etc/profile.d/conda.csh
modified      /home/gowtham/.bashrc

==> For changes to take effect, close and re-open your current shell. <==

Running `shell init`, which:
 - modifies RC file: "/home/gowtham/.bashrc"
 - generates config for root prefix: "/home/gowtham/miniforge3"
 - sets mamba executable to: "/home/gowtham/miniforge3/bin/mamba"
The following has been added in your "/home/gowtham/.bashrc" file

# >>> mamba initialize >>>
# !! Contents within this block are managed by 'mamba shell init' !!
export MAMBA_EXE='/home/gowtham/miniforge3/bin/mamba';
export MAMBA_ROOT_PREFIX='/home/gowtham/miniforge3';
__mamba_setup="$("$MAMBA_EXE" shell hook --shell bash --root-prefix "$MAMBA_ROOT_PREFIX" 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__mamba_setup"
else
    alias mamba="$MAMBA_EXE"  # Fallback on help from mamba activate
fi
unset __mamba_setup
# <<< mamba initialize <<<

Thank you for installing Miniforge3!
```

- Close terminal window (Konsole) and open a new one. *conda env base* can be seen.

```bash
(base) gowtham@deb-gowarc:~$ conda --version
conda 25.3.0
```

- To prevent the automatic activation of the conda base environment when you open a new terminal
```bash
conda config --set auto_activate_base false
```

Once again, reopen the terminal. Conda can still be accessed in Konsole but we need to activate the environment when needed.
```bash
gowtham@deb-gowarc:~$ conda --version
conda 25.3.0
gowtham@deb-gowarc:~$ conda activate base
(base) gowtham@deb-gowarc:~$ conda deactivate
gowtham@deb-gowarc:~$ conda env list

# conda environments:
#
base                   /home/gowtham/miniforge3
```
