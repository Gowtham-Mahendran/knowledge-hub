# Git

## Sphinx

Sphinx [Themes](https://sphinx-themes.org/)

[Github](https://github.com/sphinx-doc/sphinx)

[Sphinx Docs](https://www.sphinx-doc.org/en/master/index.html)

```bash
uv pip install sphinx
```

**Verify installation**

```bash
sphinx-build --version
```

**To create documentation layout**
```bash
sphinx-quickstart docs
```

???+ note "Initial Setup" 
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
I have moved the `docs` inside `sphinx` because github can either deploy from `root` or `/docs`. I created a `docs` folder in main dir and copied the contents of `docs/build/html` to `docs`.

We also need to add `.nojekyll` file inside `docs` so that the static files are served.

Since I have written down all the docs in wiki as `markdown`, it is better to include a plugin that reads `.md` files. So install, `myst_parser`.

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

Create a folder called `pages` inside `sources` and copy paste all the `.md` files from `wiki`.

Now run sphinx and copy all the files inside `build` to `docs` in the main dir. Add `.nojekyll` file inside `docs/` so that the static files are rendered.

Clone the repo and set the url 

```bash
git remote set-url origin <url>
```

Then, use 

```bash
git config credential.helper store
```

and enter the user name. For password enter the PAT generated from the Github

Now you can push to the repo.

To view the passwords, use
```bash
cat ~/.git-credentials
```

## Git

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
