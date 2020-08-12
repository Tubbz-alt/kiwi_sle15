from pytest import raises

from kiwi.markup.base import MarkupBase

from kiwi.exceptions import KiwiDescriptionInvalid


class TestMarkupBase:
    def setup(self):
        self.markup = MarkupBase('../data/example_config.xml')

    def test_raises_invalid_description_content(self):
        with raises(KiwiDescriptionInvalid):
            MarkupBase('no-bytes-data')

    def test_get_xml_description(self):
        with raises(NotImplementedError):
            self.markup.get_xml_description()

    def test_get_yaml_description(self):
        with raises(NotImplementedError):
            self.markup.get_yaml_description()

    def test_apply_xslt_stylesheets(self):
        assert 'xslt-' in self.markup.apply_xslt_stylesheets(
            '../data/example_config.xml'
        )
