# -*- coding: utf-8 -*-

from ossreport.cmd.banner import BANNER


def test_banner():
    assert BANNER is not None and len(BANNER) != 0
