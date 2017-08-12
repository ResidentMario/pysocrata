import sys; sys.path.append("../")
import pysocrata
import unittest
import json


class TestCatalogAPI(unittest.TestCase):
    """
    Tests that the catalog API fetch works as expected. This is a networked test against the New York City Open Data
    Portal.
    """
    def test(self):
        with open("auth/nyc-open-data.json", "r") as f:
            auth = json.load(f)
        result = pysocrata.get_endpoints_using_catalog_api(**auth)

        # Assert the result list is long enough.
        assert len(result) > 1000
        # Assert the resource IDs are fully unique.
        assert len(result) == len({r['resource']['id'] for r in result})


class TestJSONEndpointAPI(unittest.TestCase):
    """
    Tests that the JSON endpoint works. This is a networked test against the New York City Open Data Portal.
    """
    def test(self):
        result = pysocrata.get_endpoints_using_raw_json_emission("data.cityofnewyork.us")
        assert len(result['dataset']) > 1000


class TestGetResources(unittest.TestCase):
    """
    Tests that fetching resources, the module 'master method', works as expected. This is a networked test against
    the New York City Open Data Portal.
    """
    def test(self):
        with open("auth/nyc-open-data.json", "r") as f:
            auth = json.load(f)
        result = pysocrata.get_resources(**auth)

        # Assert the result list is long enough and contains unique datasets.
        # cf. https://github.com/ResidentMario/pysocrata/issues/1
        assert len(result) > 1000
        assert len(result) == len({r['resource']['id'] for r in result})


class TestCountDatasets(unittest.TestCase):
    """
    Tests that counting datasets works as expected. This is a networked test against the New York City Open Data
    Portal.
    """
    def test(self):
        with open("auth/nyc-open-data.json", "r") as f:
            auth = json.load(f)
        result = pysocrata.count_resources(**auth)
        assert {'dataset', 'href', 'file', 'map'}.issuperset(set(result.keys()))
