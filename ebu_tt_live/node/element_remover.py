from .base import AbstractCombinedNode
from ebu_tt_live.documents.ebutt3 import EBUTT3Document
from pyxb.binding.basis import NonElementContent, ElementContent, \
    complexTypeDefinition, simpleTypeDefinition
from ebu_tt_live.bindings import div_type, p_type, span_type, ebuttdt, style_type
from ebu_tt_live.bindings._ebuttm import divMetadata_type
import copy
import re
from datetime import timedelta


class ElementRemoverNode(AbstractCombinedNode):
    """
    Removes unwanted elements from a document.

    Matches elements by local names only. Restricted to
    XML elements that have bindings; non-bound elements
    are left in place. 
    """

    _expects = EBUTT3Document
    _provides = EBUTT3Document

    _remove_list = []
    _sequence_identifier = None
    _last_sequence_number = None

    def __init__(self,
                 node_id,
                 sequence_identifier,
                 consumer_carriage=None,
                 producer_carriage=None,
                 remove_list={}):
        super(ElementRemoverNode, self).__init__(
            node_id=node_id,
            producer_carriage=producer_carriage,
            consumer_carriage=consumer_carriage
        )

        self.remove(remove_list)
        print('remove_list = {}'.format(self._remove_list))
        self._sequence_identifier = sequence_identifier
        self._last_sequence_number = 0

    def remove(self, remove_list):
        """
        Specify the list of element local names to remove.

        :param remove_list: Comma separated list of element names (can have white space)
        """
        self._remove_list = []
        for r in remove_list.split(','):
            self._remove_list.append(r.strip())

    def process_document(self, document, **kwargs):
        if self.is_document(document):
            if self.check_if_document_seen(document=document) is True:

                print('Input document is:')
                print(document.get_xml())
                # Remove the elements we don't want
                self.remove_unwanted_elements(document.binding)

                # Update the sequence identifier and number and emit the
                # document
                self._last_sequence_number += 1
                document.sequence_identifier = self._sequence_identifier
                document.sequence_number = self._last_sequence_number
                print('Output document is:')
                print(document.get_xml())
                self.producer_carriage.emit_data(
                    data=document,
                    **kwargs
                    )
        else:
            document.sequence_identifier = self._sequence_identifier
            self.producer_carriage.emit_data(
                data=document,
                **kwargs
            )

    def remove_unwanted_elements(self, element):
        """Recursive function."""
        import pdb

        children = []
        try:
            if isinstance(element, list):
                print('this item is a list')
            elif isinstance(element, complexTypeDefinition) and \
                not element._IsSimpleTypeContent():
                children = element.orderedContent()
            elif isinstance(element, simpleTypeDefinition):
                print('this item is too simple to iterate through')
            elif element._IsSimpleTypeContent():
                print('this item looks complex but it is only pretending')
            else:
                #pdb.set_trace()
                print('this element is not a complex type, now what?')
        except Exception as e:
            print('got an exception type {}'.format(type(e)))
            pdb.set_trace()
            print('exception making orderedContent()')

        for item in children:
            if isinstance(item, NonElementContent):
                print('this is not element content')
                #pdb.set_trace()
            elif isinstance(item, ElementContent):
                if item.elementDeclaration is not None:
                    #pdb.set_trace()
                    local_name = item.elementDeclaration.name().localName()
                    namespace_uri = item.elementDeclaration.name().namespaceURI()
                    fully_qualified_name = namespace_uri + '%%' + local_name
                    print('Found an element with fully qualified name {}'.format(fully_qualified_name))
                    if (local_name in self._remove_list):
                        print('I want to remove a {}'.format(local_name))
                        setattr(element, local_name, None)
                    else:
                        self.remove_unwanted_elements(item.value)
            else:
                print('this is neither NonElementContent nor ElementContent')
                pdb.set_trace()
                raise Exception('Can this even happen!??!?!?!')

