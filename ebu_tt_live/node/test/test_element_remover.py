from unittest import TestCase
from ebu_tt_live.documents.ebutt3 import EBUTT3Document
from ebu_tt_live.node.element_remover import ElementRemoverNode
from ebu_tt_live.carriage.interface import IProducerCarriage
from mock import MagicMock


class TestDenesterNode(TestCase):
    # Given a div within a div, only a single div is returned

    def setUp(self):
        xml_file = \
            'ebu_tt_live/documents/test/' \
            'converter_ericsson3.xml'
        with open(xml_file, 'r') as in_file:
            input_xml = in_file.read()
        self.input_doc = EBUTT3Document.create_from_xml(input_xml)

        carriage = MagicMock(spec=IProducerCarriage)
        carriage.expects.return_value = EBUTT3Document

        self.element_remover = ElementRemoverNode(
            node_id='testElementRemover',
            sequence_identifier='testSeqId',
            producer_carriage=carriage
        )

    def test_remove_list_parsing(self):
        remove_list = 'nospaces1, spacebefore,spaceafter ,' \
                      '\t  tabbefore, spacesaround ,nospaces2, tabafter\t'
        expected_output = ['nospaces1',
                           'spacebefore',
                           'spaceafter',
                           'tabbefore',
                           'spacesaround',
                           'nospaces2',
                           'tabafter']

        self.element_remover.remove(remove_list)
        self.assertSequenceEqual(
            self.element_remover._remove_list, expected_output)

    def test_remove_elements(self):
        remove_list = 'facet, documentReadingSpeed, '\
            'documentIntendedTargetFormat, ' \
            'documentMaximumNumberOfDisplayableCharacterInAnyRow'

        self.element_remover.remove(remove_list)

        # Check the elements to be removed are there - this catches if anyone
        # edits them out of the test input file!
        self.assertEqual(len(self.input_doc.binding.body.div[0].metadata.facet), 1)
        self.assertIsNotNone(
            self.input_doc.binding.head.metadata.documentMetadata.
            documentReadingSpeed)
        self.assertIsNotNone(
            self.input_doc.binding.head.metadata.documentMetadata.
            documentIntendedTargetFormat)
        self.assertIsNotNone(
            self.input_doc.binding.head.metadata.documentMetadata.
            documentMaximumNumberOfDisplayableCharacterInAnyRow)

        self.element_remover.process_document(document=self.input_doc)
        self.element_remover.producer_carriage.emit_data.assert_called_once()
        output_doc = \
            self.element_remover.producer_carriage.emit_data. \
            call_args[1]['data']

        # Check we got a valid document out
        self.assertIsInstance(
            output_doc,
            EBUTT3Document
            )

        # Check the removed elements are not there - dependent on the
        # specific input document loaded in setUp()
        self.assertEqual(len(output_doc.binding.body.div[0].metadata.facet), 0)
        self.assertIsNone(
            output_doc.binding.head.metadata.documentMetadata.
            documentReadingSpeed)
        self.assertIsNone(
            output_doc.binding.head.metadata.documentMetadata.
            documentIntendedTargetFormat)
        self.assertIsNone(
            output_doc.binding.head.metadata.documentMetadata.
            documentMaximumNumberOfDisplayableCharacterInAnyRow)
