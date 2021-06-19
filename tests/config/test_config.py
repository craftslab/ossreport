# -*- coding: utf-8 -*-

import os

from ossreport.config.config import Config, ConfigException


def test_exception():
    exception = ConfigException("exception")
    assert str(exception) == "exception"


def test_config():
    config = Config()

    try:
        config.config_file = 0
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.config_file = ""
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.config_file = "config.json"
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.config_file = "foo.yml"
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.config_file = os.path.join(
            os.path.dirname(__file__), "../data/config.yml".replace("/", os.path.sep)
        )
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
        config.license_file = 0
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.license_file = ""
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.license_file = "license.json"
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.license_file = os.path.join(
            os.path.dirname(__file__), "../data/license.json".replace("/", os.path.sep)
        )
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
        config.output_file = 0
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.output_file = ""
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.output_file = "output.foo"
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.output_file = "output.pdf"
    except ConfigException as _:
        assert False
    else:
        assert True

    try:
        config.scanoss_file = 0
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.scanoss_file = ""
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.scanoss_file = "scanoss.json"
    except ConfigException as _:
        assert True
    else:
        assert False

    try:
        config.scanoss_file = os.path.join(
            os.path.dirname(__file__), "../data/scanoss.json".replace("/", os.path.sep)
        )
    except ConfigException as _:
        assert False
    else:
        assert True
