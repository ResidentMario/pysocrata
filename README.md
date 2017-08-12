
### About
`pysocrata` is a small Python module which provides an interface to the [Socrata](https://socrata.com/) open data 
portal [catalog API](http://docs.socratadiscovery.apiary.io/).

It is *not* a binding for the [Socrata SODA API](https://dev.socrata.com/consumers/getting-started.html), which
implements direct access to data within individual dataset. For that, see [`sodapy`](https://github.com/xmunoz/sodapy)
or [`rsocrata`](https://github.com/Chicago/RSocrata). `pysocrata` instead provides a way of getting a list of *all*
datasets on a portal, for example, or of querying them for various dataset-level characteristics.

### Quickstart

In the following brief overview I take **domain** to mean the open data portal of interest (for example, the New York
City Open Data Portal, or the New York State Open Data Portal). An **endpoint** is a URL-accessible "thing" on a 
Socrata open data portal. A **resource** (or data endpoint) is an endpoint which contains actual novel data; this 
definition purposefully excludes endpoints which publish data filtered or remixed from another source. For instance, 
in the case of a map-type endpoint that displays a sub-selection of data from a different geospatial type resource, 
the originator is a *resource*, while the map endpoint is merely a *non-data endpoint*.

The methodology implemented in this module solves the surprisingly non-trivial problem of distinguishing between data 
and non-data endpoints on a Socrata open data portal, which are not immediately differenciable in the Socrata catalog
API.

Keeping these definitions in mind, this module has two user-facing top-level methods:

* `pysocrata.get_resources(domain, token)` returns the metadata for every resource on a domain of interest.
* `pysocrata.count_resources(domain, token)` returns a counter of resources by type.

You may also peruse `pysocrata.get_endpoints_using_raw_json_emission` and `pysocrata.get_endpoints_using_catalog_api`
 to fetch the raw catalog API streams.
 
### Further Reading
* [`socrata-portal-metadata`](https://github.com/ResidentMario/socrata-portal-metadata)
* [The anatomy of an open data portal](http://www.residentmar.io/2016/08/11/nyc-open-data-portal.html)
