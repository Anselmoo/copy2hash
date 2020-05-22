# copy2hash

## Copy or rename any file(s) to a *hash-secured* filename via terminal
---

**copy2hash** copies or renames file(s) with regular titles to file(s) with a *hash-secured* title by using the terminal or in `python`-framework. Having unique filenames is essential for the correct indexing of databases, especially if the data come from different pipelines. Also, it is important if the filename or/and directory contains *meta*-information, which extend the length of the valid file lengths.


### Example

|
|
|

The copy or rename processed will be automatically logged as: 
 1. `*.csv`-file
 2. `*.json`-file
 3. `*.pkl`-file
 4. `*.txt`-file
 5. `*.yaml`-file
 6. `*.xml`-file
 
 ## Installation
---
```pip install copy2hash```

or

```pip install https://github.com/Anselmoo/copy2hash.git```

or 

```bash
pip install -r requirements.txt
python setup.py install
```
## Requirments
---

 1. Python3 >= 3.6
 2. [dict2xml>=1.7.0](https://github.com/lucasicf/dict2xml)
 3. [PyYAML>=5.3.1](https://github.com/yaml/pyyaml)
 
## Usage
---
 

## Author
---

 * [Anselm Hahn](https://github.com/Anselmoo)

## Contributions
---

I'm happy to accept how to improve batchplot; please forward your [issues](https://github.com/Anselmoo/copy2hash/issues) or [pull requests](https://github.com/Anselmoo/copy2hash/pulls).

Keep in mind that [pull requests](https://github.com/Anselmoo/bashplot/pulls) have to pass TravisCI in combination with [flake8](https://github.com/PyCQA/flake8), [black](https://github.com/psf/black), and [pydocstyle](https://github.com/PyCQA/pydocstyle).

## License
---

The source code of `bashplot` is licensed under the [MIT license](https://github.com/Anselmoo/copy2hash/blob/master/LICENSE).


## References
---
 
 1. https://docs.python.org/3/library/hashlib.html
 2. https://tools.ietf.org/html/rfc1321.html
 3. https://en.wikipedia.org/wiki/NIST_hash_function_competition
 4. https://131002.net/blake/
 5. https://docs.python.org/3/library/hashlib.html#hashlib.blake2
