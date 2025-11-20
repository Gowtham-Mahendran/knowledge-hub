# Development

## 1. Git

To check which user the repo is linked to,

```bash
git config --get user.name
git config --get user.email
```

To check all the details,

```bash
git config --list
```

To set the repo to a user and mail,
```bash
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

Omit `--global` to set the identity only in this repository.

Git doesn't allow changes by password. It will accept only Personalized Access Tokens (PAT). So, the remote url should have PAT included. To change this,

Profile > Settings > Developer settings > PAT > Fine-grained tokens

**Grant these permissions:**

* Read access to metadata
* Read and Write access to code

```bash
git remote set-url origin https://<username>:<PAT>@github.com/<username>/<repo_name>.git
```

## 2. VSCodium

Here is the official guide from the VSCodium [website](https://vscodium.com/)

1. Add the GPG key of the repository:
```bash
wget -qO - https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg \
   | gpg --dearmor \
   | sudo dd of=/usr/share/keyrings/vscodium-archive-keyring.gpg
```

2. Add the repository:
```bash
echo 'deb [arch=amd64,arm64 signed-by=/usr/share/keyrings/vscodium-archive-keyring.gpg] https://download.vscodium.com/debs vscodium main' \
   | sudo tee /etc/apt/sources.list.d/vscodium.list
```
3. Update then install vscodium (if you want vscodium-insiders, then replace codium by codium-insiders):
```bash
sudo apt update && sudo apt install codium
```

4. To open VSCodium, execute `codium` in terminal

## 3. Docker

Install using the official [Documentation](https://docs.docker.com/engine/install/debian/#install-using-the-repository)

Follow [this](https://docs.docker.com/engine/install/linux-postinstall/) after installation

## 4. Miniforge

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

??? note "Installation Note"
    ```text
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

## 5. UV - astral

My personal favourite python package and project manager.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 6. Sphinx

The official [Github](https://github.com/sphinx-doc/sphinx) page of Sphinx, Sphinx [Themes](https://sphinx-themes.org/) and Sphinx [Docs](https://www.sphinx-doc.org/en/master/index.html)

```bash
uv pip install sphinx
```

Verify installation using,

```bash
sphinx-build --version
```

To create documentation layout,

```bash
sphinx-quickstart docs
```

??? note "Initial Setup" 
    ```text
    Welcome to the Sphinx 8.2.3 quickstart utility.

    Please enter values for the following settings (just press Enter to
    accept a default value, if one is given in brackets).

    Selected root path: docs

    You have two options for placing the build directory for Sphinx output.
    Either, you use a directory "_build" within the root path, or you separate
    "source" and "build" directories within the root path.
    > Separate source and build directories (y/n) [n]: y

    The project name will occur in several places in the built documentation.
    > Project name: Debian Linux Docs
    > Author name(s): Gowtham Mahendran
    > Project release []: 1.0

    If the documents are to be written in a language other than English,
    you can select a language here by its language code. Sphinx will then
    translate text that it generates into that language.

    For a list of supported codes, see
    https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
    > Project language [en]: 

    Creating file /home/gowtham/Documents/Git/Github/operation_linux/docs/source/conf.py.
    Creating file /home/gowtham/Documents/Git/Github/operation_linux/docs/source/index.rst.
    Creating file /home/gowtham/Documents/Git/Github/operation_linux/docs/Makefile.
    Creating file /home/gowtham/Documents/Git/Github/operation_linux/docs/make.bat.

    Finished: An initial directory structure has been created.

    You should now populate your master file /home/gowtham/Documents/Git/Github/operation_linux/docs/source/index.rst and create other documentation
    source files. Use the Makefile to build the docs, like so:
        make builder
    where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
    ```

**Docs folder should be there**

```bash
ls
```

It should show the `docs` folder inside the directory

**To build**

```bash
sphinx-build -M html docs/source/ docs/build/
```

I have moved the `docs` inside `sphinx` because github can either deploy from `root` or `/docs`. I created a `docs` folder in main dir and copied the contents of `docs/build/html` to `docs`. We also need to add `.nojekyll` file inside `docs` so that the static files are served. Since I have written down all the docs in wiki as `markdown`, it is better to include a plugin that reads `.md` files. So install, `myst_parser`.

Add the plugin to the `conf.py` file

```python
extensions = ["myst_parser",]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
```

In `index.rst`, include the code to read the pages,

```bash
.. toctree::
   :maxdepth: 2
   :caption: Contents:
   :glob:

   pages/*
```

Create a folder called `pages` inside `sources` and copy paste all the `.md` files from `wiki`. Now run sphinx and copy all the files inside `build` to `docs` in the main dir. Add `.nojekyll` file inside `docs/` so that the static files are rendered.

Clone the repo and set the url,

```bash
git remote set-url origin <url>
```

Then, use 

```bash
git config credential.helper store
```

and enter the user name. For password enter the PAT generated from the Github. Now you can push to the repo. To view the passwords, use

```bash
cat ~/.git-credentials
```

