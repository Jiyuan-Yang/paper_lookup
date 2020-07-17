# Paper Lookup

## Introduction

A simple command line tool to manage you papers. You could manage papers you've saved in your computer in a more efficient way based on this tool.

## Environment

```
Python 3.7.7
colorama 0.4.3
```

`colorama` is a tool for colorful output in command line, you could install it by `conda` or `pip`.

## Installation

- Find a proper directory to place this tool

  ```shell
  cd your/directory
  git clone https://github.com/Jiyuan-Yang/paper_lookup.git
  ```

- Then check the version of your Python interpreter and install other requirements

  ```shell
  python --version
  Python 3.7.7
  conda install colorama
  ```

- In `paper_lookup/meta_params.py`, you need to change `config_file_name` to the *absolute* path of your own directory to place the configuration file.

  ```python
  import os
  import json
  
  # change the following line to ‘/your/path/paper_lookup/config.json’
  config_file_name = '/Users/yangjiyuan/Desktop/projects/paper_lookup/config.json'
  db_file_name = 'db.json'
  ```

- In order to use it in a more efficient way, you could add an alias in the configuration file of your shell (e.g. ~/.bashrc ~/.zshrc etc.)

  ```shell
  cd
  vim .zshrc # (or .bashrc if you use Bash)
  # add the following alias
  alias plup="python /your/path/paper_lookup/main.py"
  ```

- Check if this tool works

  ```shell
  plup -v # or plup --version, plup is the abbreviation of Paper LookUP
  Paper Lookup version 1.0.0
  # done!
  ```

## Usage

- First you should make an initialization

  ```shell
  plup init
  ```

  Following the steps the set the root folder and backup folder. All the papers and relative files will be placed in the root folder, and backup folder is an option.

- You could use `env` to reset or change the path of you backup folder

  ``` 
  plup env --reset backup_path
  ```

- Use the `import` instruation to import papers. In order to make better use of other functions, please place the `.bib` file with your paper, and make sure they have the same name (e.g. paper: some_name.pdf, bib file: some_name.bib). You could place them in a folder, like this

  ```
  papers_to_import
           └─┬─paper0.bib
             ├─paper0.pdf
             ├─paper1.bib
             └─paper1.pdf
  ```

  Then use the following instruction

  ```shell
  plup -f /absolute/path/to/papers_to_import -t 'tag0;tag1'
  ```

  This will import the papers into the root folder you've set during initialization

- Then you could list or search paper by the `find` command

  ```shell
  plup find # this will list all papers
  plup find -n 'keyword in title' -a 'author name' -t 'tag0;tag1'
   id   | title                     | author          | tags            
      0 | paper_a                   | author0         | tag0;tag1
  ```

- Use the `open` command to open the paper

  ```shell
  plup open 0 # open + paper_id
  # this has been tested on macOS, which use the `open` command in shell to open 
  # the pdf file
  # you may change it to the command in you own OS
  ```

  You could find it in `paper_loopup/exec/open_exec.py`.

- Use the `export` command to export the bib file of the paper

  ```shell
  plup export 0 # export + paper_id
  ```

- For more information, use `-h` flag, for example

  ```shell
  $ plup -h
  usage: main.py [-h] [-v] {init,env,import,find,open,export,backup} ...
  
  Paper Lookup, an easier way to manage your papers.
  
  positional arguments:
    {init,env,import,find,open,export,backup}
                          sub parsers for Paper Lookup
      init                initialize a configuration file
      env                 edit env arg
      import              import papers, paper and its bib file should have the
                          same name (eg. paper: some_paper.pdf, bib:
                          some_paper.bib)
      find                fetch info about papers, use ';' to add more keywords
                          and use '' to quote add the keywords
      open                open paper
      export              export bib files
      backup              backup the whole root directory
  
  optional arguments:
    -h, --help            show this help message and exit
    -v, --version         print version info
  
  $ plup import -h
  usage: main.py import [-h] [-s SINGLE] [-f FOLDER] [-t TAGS] [-nb]
  
  optional arguments:
    -h, --help            show this help message and exit
    -s SINGLE, --single SINGLE
                          import single paper, -s [paper path]
    -f FOLDER, --folder FOLDER
                          import all papers in a folder, -s [paper path]
    -t TAGS, --tags TAGS  add tags for the papers, please use ';'tosplit tags,
                          and don't forget to use '' toquote the args
    -nb, --no-bib         if there is no bib file, use this flag
  ```

  


