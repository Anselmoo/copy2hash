# copy2hash

## Copy or rename any file(s) to a _hash-secured_ filename via terminal
---

`copy2hash` copies or renames file(s) with regular titles to file(s) with a _hash-secured_ title by using the terminal or in `python`-framework. Having unique filenames is essential for the correct indexing of databases, especially if the data come from different pipelines. Also, it is important if the filename or/and directory contains _meta_-information, which extend the length of the valid file lengths.

Having *regular*-filename pairs such as `example.input` &rlarr; `example.output` can brings very fast confusion and makes analysis of data very confusing. The secured hash algorithms (**SHA**) [1-5] in `copy2hash` provides a safe way to generate distinguishable filenames like:

`example.input` &rlarr; `example.output`  &xrarr; `7e2229daab26b247b877565505b6aaf131014f2cb64e4c4ca796fbe0dc2fadc4.input` &rlarr; `4bd077ed771af9ad97e3f2dc45583a14af014ebafb73a846f2436a168ae3eafa.output`

The following **SHA** algorithms [1-5] are available:
1. `sha1`
2. `sha224`
3. `sha256`
4. `sha384`
5. `sha512`
6. `blake2b`
7. `blake2s`
8. `md5`
9. `sha3_224`
10. `sha3_256`
11. `sha3_384`
12. `sha3_512`
13. `shake_128` with fixed `32` character length
14. `shake_256` with fixed `32` character length

and the copied or moved processed will be automatically logged as: 
 1. `*.csv`-file:
 2. `*.json`-file
 3. `*.pkl`-file
 4. `*.txt`-file
 5. `*.yaml`-file
 6. `*.xml`-file


## Installation
---

`pip install copy2hash`

or

`pip install https://github.com/Anselmoo/copy2hash.git`

or

```bash
pip install -r requirements.txt
python setup.py install
```

## Requirments
---

1.  Python3 >= 3.6
2.  [dict2xml>=1.7.0](https://github.com/lucasicf/dict2xml)
3.  [PyYAML>=5.3.1](https://github.com/yaml/pyyaml)

## Usage
---
```bash
╰─ copy2hash * -h
usage: copy2hash [-h] [-r [REPORT [REPORT ...]]] [-rn REPORT_NAME]
                 [-s [SHA [SHA ...]]] [-dir DIRECTORY] [-mv] [-fxt] [-sxt]
                 [-nfxt] [-ver] [-v]
                 [infile [infile ...]]

copy or rename any file(s) to a hash-secured filename via terminal

positional arguments:
  infile                file(s) to copy or to rename with regular filename to
                        secured hash filename

optional arguments:
  -h, --help            show this help message and exit
  -r [REPORT [REPORT ...]], --report [REPORT [REPORT ...]]
                        define one or a series of file format(s) for the
                        rename-report(s) to retrace the copying or rename of
                        the file(s). The availabel file formats are:'csv',
                        'json', 'pkl', 'txt', 'yaml', 'xml', or own file-
                        extension as ASCII; default is 'json'
  -rn REPORT_NAME, --report_name REPORT_NAME
                        define the report name for the copied or move file(s);
                        default is 'copy_report'
  -s [SHA [SHA ...]], --sha [SHA [SHA ...]]
                        define one or a series of secure hash algorithms (sha)
                        for copying or rename of the file(s). The availabel
                        secure hash algorithms (sha) are: 'sha1', 'sha224',
                        'sha256', 'sha384', 'sha512', 'blake2b', 'blake2s',
                        'md5', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512',
                        'shake_128', 'shake_256'; default 'sha256'. The
                        'shake_128' and 'shake_256' are defined for 32
                        character length.
  -dir DIRECTORY, --directory DIRECTORY
                        replace the standard directory ('./') by a specific
                        directory ('./path'). If the specific directory not
                        exist, the directory will be created. This can
                        required sudo rights.
  -mv, --move           moving the file(s) instead of copying the files with
                        regular filename to secure hash filename
  -fxt, --file_extension
                        replaced the given file-extension by the abbreviations
                        of the used secure hash algorithms (sha)
  -sxt, --file_suffix   removed the given file-extension and add a suffix in
                        front of the file based on the abbreviations of the
                        used secure hash algorithms (sha). It is seperated by
                        colon like 'sha256-e3b0c44298fc1c149afbf4c8996fb92427a
                        e41e4649b934ca495991b7852b855'
  -nfxt, --no_file_extension
                        removed the any file-extension and just copy or move
                        the file(s) as sha renamed file(s)
  -ver, --verbose       enable the verbose mode
  -v, --version         displays the current version of cop2hash
```

## Other Examples
---

For keeping the regular file-extension, use: 

```copy2hash * -r json csv yaml```

|*regular*-filename||*sha256*-filename|
|---|---|---|
|`example.out`|&rarr;|`c8e1f67ad67b8f456afe76b5eb5d6dd0a919b1537cd67b9419f86158e4d9c1b4.out`|
|`example.t`|&rarr;|`97c7bc3705df72f76cf3d3d55228751bc6895a488fb004b112914d4a05447c16.t`|
|`example.tx`|&rarr;|`11297eae82d7866c4dd42e79b8082a5256fa3d54e7e1bf60ab87747e9b664303.tx`|
|`example.txt`|&rarr;|`e7cb632359a2be17c1008b50f9ec85691cd5d66834d5fe8f63ef65ceb06682ee.txt`|
|`example_1.txt`|&rarr;|`85a6fae2fca1342a85222088ff0342cbea8222e4140aba96690691c9d58e5786.txt`|
|`example_2.txt`|&rarr;|`0329cb55ddfab933d9753686ddb193148003611df672a4a41aad014ead4767f9.txt`|
|`example_l.txt`|&rarr;|`eb4d990362cbf5cccd0b49374b71ca3f799c7262352c9fda7ba875ba034f7168.txt`|

Removing the regular file-extension and adding the SHA-key in front, use:

```copy2hash * -r json csv yaml -sxt```

|*regular*-filename||*sha256*-filename|
|---|---|---|
|`example.out`|&rarr;|`sha256-c8e1f67ad67b8f456afe76b5eb5d6dd0a919b1537cd67b9419f86158e4d9c1b4`|
|`example.t`|&rarr;|`sha256-97c7bc3705df72f76cf3d3d55228751bc6895a488fb004b112914d4a05447c16`|
|`example.tx`|&rarr;|`sha256-11297eae82d7866c4dd42e79b8082a5256fa3d54e7e1bf60ab87747e9b664303`|
|`example.txt`|&rarr;|`sha256-e7cb632359a2be17c1008b50f9ec85691cd5d66834d5fe8f63ef65ceb06682ee`|
|`example_1.txt`|&rarr;|`sha256-85a6fae2fca1342a85222088ff0342cbea8222e4140aba96690691c9d58e5786`|
|`example_2.txt`|&rarr;|`sha256-0329cb55ddfab933d9753686ddb193148003611df672a4a41aad014ead4767f9`|
|`example_l.txt`|&rarr;|`sha256-eb4d990362cbf5cccd0b49374b71ca3f799c7262352c9fda7ba875ba034f7168`|


### More Examples


Generate a report in the `json`- and `yaml`-format:

```copy2hash example.input example.output -r json yaml```

```json
{
    "index": [
        0,
        1
    ],
    "filename": [
        "example.input",
        "example.output"
    ],
    "mode": [
        "copy",
        "copy"
    ],
    "home_dir": [
        ".",
        "."
    ],
    "copy_dir": [
        ".",
        "."
    ],
    "sha256": [
        "7e2229daab26b247b877565505b6aaf131014f2cb64e4c4ca796fbe0dc2fadc4.input",
        "4bd077ed771af9ad97e3f2dc45583a14af014ebafb73a846f2436a168ae3eafa.output"
    ]
}
```

```yaml
copy_dir:
- .
- .
filename:
- example.input
- example.output
home_dir:
- .
- .
index:
- 0
- 1
mode:
- copy
- copy
sha256:
- 7e2229daab26b247b877565505b6aaf131014f2cb64e4c4ca796fbe0dc2fadc4.input
- 4bd077ed771af9ad97e3f2dc45583a14af014ebafb73a846f2436a168ae3eafa.output
```
## Using as Built-in
---

```python
from copy2hash import copy2hash
from pathlib import Path

args = {
            "infile": list(Path("test").glob("example1.txt")),
            "report": ["json"],
            "report_name": "copy_report",
            "sha": ["sha256"],
            "directory": None,
            "move": None,
            "file_extension": False,
            "file_suffix": False,
            "no_file_extension": False,
            "verbose": True,
            "version": False,
        }

copy2hash.command_line_runner(opt=args)
```
## Author
---

- [Anselm Hahn](https://github.com/Anselmoo)

## Contributions
---

I'm happy to accept how to improve batchplot; please forward your [issues](https://github.com/Anselmoo/copy2hash/issues) or [pull requests](https://github.com/Anselmoo/copy2hash/pulls).

Keep in mind that [pull requests](https://github.com/Anselmoo/bashplot/pulls) have to pass TravisCI in combination with [flake8](https://github.com/PyCQA/flake8), [black](https://github.com/psf/black), and [pydocstyle](https://github.com/PyCQA/pydocstyle).

## License
---

The source code of `bashplot` is licensed under the [MIT license](https://github.com/Anselmoo/copy2hash/blob/master/LICENSE).

## References
---

1.  https://docs.python.org/3/library/hashlib.html
2.  https://tools.ietf.org/html/rfc1321.html
3.  https://en.wikipedia.org/wiki/NIST_hash_function_competition
4.  https://131002.net/blake/
5.  https://docs.python.org/3/library/hashlib.html#hashlib.blake2
