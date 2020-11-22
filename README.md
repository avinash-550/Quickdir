# Quickdir
JSON object to quick directory creator using python.

## Installation

Clone the repository and import Quickdir.py file.

## Usage

Json object structure. Terminating value has to be supplied to end(leaf) nodes in dir structure. Supply 1 if it ends with a file, 0 if it ends with a folder.

```json
json = {"root": {
                "logs": {
                        "test": 0,
                        "log.txt": 1
                    },
                "css" : {
                        "style.css" : 1,
                        "bootstrap.css": 1
                    },
                "js": {
                        "mainFunction.js":1,
                        "bootstrap.js":1,
                        "jquery.js":1
                    },
                "common":{
                        "navbar.html" :1,
                        "footer.html" :1
                    },
                "Readme.md": 1,
                "fonts": {
                    "sample.txt" :1
                  },
                "img": 0,
                "index.html":1
                
        } 
    }

```

Creating dir using Quickdir object
```python
import Quickdir

# only if using config.json
import config

# create object of Quickdir class 
quick = Quickdir("Quickdir")

# give custom path instead of 'Quickdir' if required
quick2 = Quickdir("S:/Files")

# Create and pass your json object or edit config.json in config.py
quick.make(config.json)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
