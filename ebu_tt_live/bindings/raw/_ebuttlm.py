# ./ebu_tt_live/bindings/raw/_ebuttlm.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:6ddd049f6e7bfeeff5fc8cd93c2a70773009a59e
# Generated 2023-10-04 16:45:22.905376 by PyXB version 1.2.6 using Python 3.11.5.final.0
# Namespace urn:ebu:tt:livemessage [xmlns:ebuttlm]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:9bb88651-48ec-4447-927f-cd1113ebcec5')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import ebu_tt_live.bindings._ebuttp as _ImportedBinding_ebu_tt_live_bindings__ebuttp
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:ebu:tt:livemessage', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ebuttp = _ImportedBinding_ebu_tt_live_bindings__ebuttp.Namespace
_Namespace_ebuttp.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, fallback_namespace=None, location_base=None, default_namespace=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword fallback_namespace An absent L{pyxb.Namespace} instance
    to use for unqualified names when there is no default namespace in
    scope.  If unspecified or C{None}, the namespace of the module
    containing this function will be used, if it is an absent
    namespace.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.

    @keyword default_namespace An alias for @c fallback_namespace used
    in PyXB 1.1.4 through 1.2.6.  It behaved like a default namespace
    only for absent namespaces.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=fallback_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, fallback_namespace=None, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, fallback_namespace)


# Complex type {urn:ebu:tt:livemessage}message_header_type with content type ELEMENT_ONLY
class message_header_type (pyxb.binding.basis.complexTypeDefinition):
    """Message header to help a recipient identify the purpose of the message
            and decide whether it is relevant to them and if so what type of payload it contains if any
            and how to process that payload"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'message_header_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ebu:tt:livemessage}sender uses Python identifier sender
    __sender = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sender'), 'sender', '__urnebuttlivemessage_message_header_type_urnebuttlivemessagesender', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 18, 12), )

    
    sender = property(__sender.value, __sender.set, None, None)

    
    # Element {urn:ebu:tt:livemessage}recipient uses Python identifier recipient
    __recipient = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'recipient'), 'recipient', '__urnebuttlivemessage_message_header_type_urnebuttlivemessagerecipient', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 19, 12), )

    
    recipient = property(__recipient.value, __recipient.set, None, None)

    
    # Element {urn:ebu:tt:livemessage}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__urnebuttlivemessage_message_header_type_urnebuttlivemessagetype', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 20, 12), )

    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __sender.name() : __sender,
        __recipient.name() : __recipient,
        __type.name() : __type
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.message_header_type = message_header_type
Namespace.addCategoryObject('typeBinding', 'message_header_type', message_header_type)


# Complex type {urn:ebu:tt:livemessage}message_type with content type ELEMENT_ONLY
class message_type (pyxb.binding.basis.complexTypeDefinition):
    """The message container type that can be used as a root document element
            to create a new message. It shall specify its header and it could specify a payload.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'message_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 24, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ebu:tt:livemessage}header uses Python identifier header
    __header = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'header'), 'header', '__urnebuttlivemessage_message_type_urnebuttlivemessageheader', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 32, 12), )

    
    header = property(__header.value, __header.set, None, None)

    
    # Element {urn:ebu:tt:livemessage}payload uses Python identifier payload
    __payload = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'payload'), 'payload', '__urnebuttlivemessage_message_type_urnebuttlivemessagepayload', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 33, 12), )

    
    payload = property(__payload.value, __payload.set, None, None)

    
    # Attribute {urn:ebu:tt:parameters}sequenceIdentifier uses Python identifier sequenceIdentifier
    __sequenceIdentifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ebuttp, 'sequenceIdentifier'), 'sequenceIdentifier', '__urnebuttlivemessage_message_type_urnebuttparameterssequenceIdentifier', _ImportedBinding_ebu_tt_live_bindings__ebuttp.STD_ANON, required=True)
    __sequenceIdentifier._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_parameters.xsd', 17, 4)
    __sequenceIdentifier._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 36, 8)
    
    sequenceIdentifier = property(__sequenceIdentifier.value, __sequenceIdentifier.set, None, 'Every document with the same ebuttp:sequenceIdentifier\n                shall be uniquely numbered using the ebuttp:sequenceNumber attribute.')

    _ElementMap.update({
        __header.name() : __header,
        __payload.name() : __payload
    })
    _AttributeMap.update({
        __sequenceIdentifier.name() : __sequenceIdentifier
    })
_module_typeBindings.message_type = message_type
Namespace.addCategoryObject('typeBinding', 'message_type', message_type)


message = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'message'), message_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 39, 4))
Namespace.addCategoryObject('elementBinding', message.name().localName(), message)



message_header_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sender'), pyxb.binding.datatypes.string, scope=message_header_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 18, 12)))

message_header_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'recipient'), pyxb.binding.datatypes.string, scope=message_header_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 19, 12)))

message_header_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type'), pyxb.binding.datatypes.NCName, scope=message_header_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 20, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 18, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 19, 12))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(message_header_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sender')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 18, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(message_header_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'recipient')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 19, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(message_header_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'type')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 20, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
message_header_type._Automaton = _BuildAutomaton()




message_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'header'), message_header_type, scope=message_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 32, 12)))

message_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'payload'), pyxb.binding.datatypes.anyType, scope=message_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 33, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(message_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'header')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 32, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(message_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'payload')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_livemessage.xsd', 33, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
message_type._Automaton = _BuildAutomaton_()

