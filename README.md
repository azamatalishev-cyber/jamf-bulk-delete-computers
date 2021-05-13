# Bulk Delete Computer in Jamf

This is a fast and easy way to delete computers in bulk from JAMF.

> :warning: **This is a blunt force tool! Please triple check before deleting devices**

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required modules.

```bash
pip install -r requirements.txt
```
(Please note that if you have the `brew python` formula installed, you will use ```pip3`` instead)
 
Please execute the following in your terminal:

```bash
defaults write ~/Library/Preferences/com.github.sheagcraig.python-jss.plist jss_user <username>
defaults write ~/Library/Preferences/com.github.sheagcraig.python-jss.plist jss_pass <password>
defaults write ~/Library/Preferences/com.github.sheagcraig.python-jss.plist jss_url <url>
```


## Usage
```bash
python3 main.py --help
Usage: main.py [OPTIONS]

Options:
  --csv TEXT  Path to the csv with the objects you would like to delete in
              Jamf

  --help      Show this message and exit.
```
```bash
python3 main.py --csv list_of_computers_i_need_to_delete.csv
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
