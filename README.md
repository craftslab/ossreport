# ossreport

[![Actions Status](https://github.com/craftslab/ossreport/workflows/CI/badge.svg?branch=master&event=push)](https://github.com/craftslab/ossreport/actions?query=workflow%3ACI)
[![Docker](https://img.shields.io/docker/pulls/craftslab/ossreport)](https://hub.docker.com/r/craftslab/ossreport)
[![License](https://img.shields.io/github/license/craftslab/ossreport.svg?color=brightgreen)](https://github.com/craftslab/ossreport/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/ossreport.svg?color=brightgreen)](https://pypi.org/project/ossreport)
[![Tag](https://img.shields.io/github/tag/craftslab/ossreport.svg?color=brightgreen)](https://github.com/craftslab/ossreport/tags)



## Introduction

*ossreport* is a report tool for *[SCANOSS](https://github.com/scanoss)* written in Python.



## Prerequisites

- Python >= 3.7.0



## Run

```bash
git clone https://github.com/craftslab/ossreport.git

cd ossreport
pip install -Ur requirements.txt
python report.py --config-file="config.yml" --license-file "license.json" --scanoss-file "scanoss.json" --output-file "output.pdf"
```



## Docker

```bash
git clone https://github.com/craftslab/ossreport.git

cd ossreport
docker build --no-cache -f Dockerfile -t craftslab/ossreport:latest .
docker run -it -v /tmp:/tmp craftslab/ossreport:latest ./ossreport --config-file="config.yml" --license-file "license.json" --scanoss-file "/tmp/scanoss.json" --output-file "/tmp/output.pdf"
```



## Usage

```
usage: report.py [-h] [--config-file CONFIG_FILE]
                 [--license-file LICENSE_FILE] --output-file OUTPUT_FILE
                 --scanoss-file SCANOSS_FILE [-v]

SCANOSS Report

optional arguments:
  -h, --help            show this help message and exit
  --config-file CONFIG_FILE
                        config file (default: ossreport/config/config.yml)
  --license-file LICENSE_FILE
                        license file (default: ossreport/data/license.json)
  --output-file OUTPUT_FILE
                        output file (.pdf|.xlsx)
  --scanoss-file SCANOSS_FILE
                        scanoss file (.json)
  -v, --version         show program's version number and exit
```



## Settings

*ossreport* parameters can be set in the directory [config](https://github.com/craftslab/ossreport/blob/master/ossreport/config).

An example of configuration in [config.yml](https://github.com/craftslab/ossreport/blob/master/ossreport/config/config.yml):

```yaml
apiVersion: v1
kind: worker
metadata:
  name: ossreport
spec:
  risk:
    license:
      critical:
      high:
        permissions:
          - commercial-use
          - modifications
          - distribution
          - patent-use
          - private-use
        conditions:
          - include-copyright
          - document-changes
          - disclose-source
          - same-license
        limitations:
          - liability
          - warranty
      medium:
        permissions:
        conditions:
        limitations:
      low:
        permissions:
          - commercial-use
          - modifications
          - distribution
          - patent-use
          - private-use
        conditions:
          - include-copyright
          - document-changes
        limitations:
          - trademark-use
          - liability
          - warranty
      none:
        permissions:
        conditions:
        limitations:
```



## License

Project License can be found [here](LICENSE).



## Reference

### License

- [choosealicense-rules](https://github.com/github/choosealicense.com/blob/gh-pages/_data/rules.yml)
- [choosealicense-table](https://choosealicense.com/appendix/)
- [github-licenses](https://docs.github.com/en/rest/reference/licenses)
- [spdx-license](https://github.com/spdx/license-list-data)



### ReportLab

- [reportlab-example](https://blog.csdn.net/bocai_xiaodaidai/article/details/102820431)
- [reportlab-userguide](https://www.reportlab.com/docs/reportlab-userguide.pdf)



### Seaborn

- [seaborn-data](https://github.com/mwaskom/seaborn-data)
- [seabarn-examples](http://seaborn.pydata.org/examples)
