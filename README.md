## pysocrata [![PyPi version](https://img.shields.io/pypi/v/pysocrata.svg)](https://pypi.python.org/pypi/pysocrata/) ![t](https://img.shields.io/badge/status-beta-yellow.svg)

### About
`pysocrata` is a small Python module which provides an interface for fetching and consuming metadata about the data
on any [Socrata](https://socrata.com/) open data portal.

It is *not* a binding for the [Socrata SODA API](https://dev.socrata.com/consumers/getting-started.html), which
implements direct access to data within individual dataset. For that, see [`sodapy`](https://github.com/xmunoz/sodapy)
or [`rsocrata`](https://github.com/Chicago/RSocrata). `pysocrata` instead provides a way of getting a list of *all*
datasets on a portal, for example, or of querying them for various dataset-level characteristics.

This repository is a further development of the [`socrata-portal-metadata`](https://github.com/ResidentMario/socrata-portal-metadata) repository.
For more information [read the accompanying blog post](http://www.residentmar.io/2016/08/11/nyc-open-data-portal.html).