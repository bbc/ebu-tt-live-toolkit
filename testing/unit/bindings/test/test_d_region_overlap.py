from unittest import TestCase
from ebu_tt_live.bindings import d_region_type


class TestEBUTTDRegionNoOverlap(TestCase):

    _fixed_region = d_region_type(
        id="fixed",
        origin="25% 35%",
        extent="50% 30%"
    )

    _test_cases = [
        # ("x% y%", "w% h%"),  
        ("25% 5%", "50% 30%"),  # above
        ("25% 65%", "50% 30%"),  # below
        ("0% 35%", "25% 30%"),  # left
        ("75% 35%", "25% 30%"),  # right
        ("0% 5%", "25% 30%"),  # above left
        ("75% 65%", "25% 30%"),  # below right
        ("75% 5%", "25% 30%"),  # above right
        ("0% 65%", "25% 30%"),  # below left
    ]

    def test_regions_do_not_overlap(self):
        for (o, e) in self._test_cases:
            with self.subTest("o=({}), e=({})".format(o, e)):
                test_region = d_region_type(
                    id="id",
                    origin=o,
                    extent=e
                )
                self.assertFalse(
                    self._fixed_region.overlaps(test_region))
                self.assertFalse(
                    test_region.overlaps(self._fixed_region))


class TestEBUTTDRegionYesOverlap(TestCase):

    _fixed_region = d_region_type(
        id="fixed",
        origin="25% 35%",
        extent="50% 30%"
    )

    _test_cases = [
        # ("x% y%", "w% h%"),  
        ("25% 5%", "50% 31%"),  # above
        ("25% 64%", "50% 30%"),  # below
        ("1% 35%", "25% 30%"),  # left
        ("74% 35%", "25% 30%"),  # right
        ("1% 5%", "25% 31%"),  # above left
        ("74% 64%", "25% 30%"),  # below right
        ("74% 5%", "25% 31%"),  # above right
        ("1% 64%", "25% 30%"),  # below left
        ("0% 0%", "100% 100%"),  # all around
    ]

    def test_regions_do_overlap(self):
        for (o, e) in self._test_cases:
            with self.subTest(msg="o=({}), e=({})".format(o, e)):
                test_region = d_region_type(
                    id="id",
                    origin=o,
                    extent=e
                )
                self.assertTrue(
                    self._fixed_region.overlaps(test_region))
                self.assertTrue(
                    test_region.overlaps(self._fixed_region))
