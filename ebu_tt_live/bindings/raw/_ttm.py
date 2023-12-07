# ./ebu_tt_live/bindings/raw/_ttm.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:20bf17fcf9b73854cba2c110c3abf6a8b2d3ceeb
# Generated 2023-10-04 16:45:22.903912 by PyXB version 1.2.6 using Python 3.11.5.final.0
# Namespace http://www.w3.org/ns/ttml#metadata [xmlns:ttm]

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
import pyxb.binding.datatypes
import pyxb.binding.xml_

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.w3.org/ns/ttml#metadata', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 22, 14)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON)
STD_ANON.full = STD_ANON._CF_enumeration.addEnumeration(unicode_value='full', tag='full')
STD_ANON.family = STD_ANON._CF_enumeration.addEnumeration(unicode_value='family', tag='family')
STD_ANON.given = STD_ANON._CF_enumeration.addEnumeration(unicode_value='given', tag='given')
STD_ANON.alias = STD_ANON._CF_enumeration.addEnumeration(unicode_value='alias', tag='alias')
STD_ANON.other = STD_ANON._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 50, 8)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_)
STD_ANON_.person = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='person', tag='person')
STD_ANON_.character = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='character', tag='character')
STD_ANON_.group = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='group', tag='group')
STD_ANON_.organization = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='organization', tag='organization')
STD_ANON_.other = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='other', tag='other')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Complex type [anonymous] with content type EMPTY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 39, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_orgnsttmlmetadata_CTD_ANON_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 42, 12)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'id'), 'id', '__httpwww_w3_orgnsttmlmetadata_CTD_ANON_httpwww_w3_orgXML1998namespaceid', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = None
    __id._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 41, 12)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}space uses Python identifier space
    __space = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'space'), 'space', '__httpwww_w3_orgnsttmlmetadata_CTD_ANON_httpwww_w3_orgXML1998namespacespace', pyxb.binding.xml_.STD_ANON_space)
    __space._DeclarationLocation = None
    __space._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 43, 12)
    
    space = property(__space.value, __space.set, None, None)

    
    # Attribute agent uses Python identifier agent
    __agent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'agent'), 'agent', '__httpwww_w3_orgnsttmlmetadata_CTD_ANON_agent', pyxb.binding.datatypes.IDREF, required=True)
    __agent._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 40, 12)
    __agent._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 40, 12)
    
    agent = property(__agent.value, __agent.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __id.name() : __id,
        __space.name() : __space,
        __agent.name() : __agent
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 16, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml#metadata}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpwww_w3_orgnsttmlmetadata_CTD_ANON__httpwww_w3_orgnsttmlmetadataname', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 19, 8), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml#metadata}actor uses Python identifier actor
    __actor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'actor'), 'actor', '__httpwww_w3_orgnsttmlmetadata_CTD_ANON__httpwww_w3_orgnsttmlmetadataactor', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 38, 8), )

    
    actor = property(__actor.value, __actor.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}space uses Python identifier space
    __space = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'space'), 'space', '__httpwww_w3_orgnsttmlmetadata_CTD_ANON__httpwww_w3_orgXML1998namespacespace', pyxb.binding.xml_.STD_ANON_space)
    __space._DeclarationLocation = None
    __space._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 62, 6)
    
    space = property(__space.value, __space.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_orgnsttmlmetadata_CTD_ANON__httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 61, 6)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'id'), 'id', '__httpwww_w3_orgnsttmlmetadata_CTD_ANON__httpwww_w3_orgXML1998namespaceid', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = None
    __id._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 60, 6)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_w3_orgnsttmlmetadata_CTD_ANON__type', _module_typeBindings.STD_ANON_)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 49, 6)
    __type._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 49, 6)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __actor.name() : __actor
    })
    _AttributeMap.update({
        __space.name() : __space,
        __lang.name() : __lang,
        __id.name() : __id,
        __type.name() : __type
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type MIXED
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 20, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/XML/1998/namespace}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'id'), 'id', '__httpwww_w3_orgnsttmlmetadata_CTD_ANON_2_httpwww_w3_orgXML1998namespaceid', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = None
    __id._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 32, 12)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}space uses Python identifier space
    __space = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'space'), 'space', '__httpwww_w3_orgnsttmlmetadata_CTD_ANON_2_httpwww_w3_orgXML1998namespacespace', pyxb.binding.xml_.STD_ANON_space)
    __space._DeclarationLocation = None
    __space._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 34, 12)
    
    space = property(__space.value, __space.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_orgnsttmlmetadata_CTD_ANON_2_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 33, 12)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__httpwww_w3_orgnsttmlmetadata_CTD_ANON_2_type', _module_typeBindings.STD_ANON)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 21, 12)
    __type._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 21, 12)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __space.name() : __space,
        __lang.name() : __lang,
        __type.name() : __type
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


title = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'title'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 66, 2))
Namespace.addCategoryObject('elementBinding', title.name().localName(), title)

desc = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'desc'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 67, 2))
Namespace.addCategoryObject('elementBinding', desc.name().localName(), desc)

copyright = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'copyright'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 68, 2))
Namespace.addCategoryObject('elementBinding', copyright.name().localName(), copyright)

agent = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'agent'), CTD_ANON_, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 15, 2))
Namespace.addCategoryObject('elementBinding', agent.name().localName(), agent)



CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 19, 8)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'actor'), CTD_ANON, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 38, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 19, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 38, 8))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 19, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'actor')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 38, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 20, 10))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_()

