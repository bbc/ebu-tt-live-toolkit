# ./ebu_tt_live/bindings/raw/__init__.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e3bbecc10c61338063ee2c070f5c7ba59a7cf71e
# Generated 2023-10-04 16:45:22.904982 by PyXB version 1.2.6 using Python 3.11.5.final.0
# Namespace http://www.w3.org/ns/ttml

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
import ebu_tt_live.bindings._ebuttdt as _ImportedBinding_ebu_tt_live_bindings__ebuttdt
import ebu_tt_live.bindings._ebuttm as _ImportedBinding_ebu_tt_live_bindings__ebuttm
import ebu_tt_live.bindings._ebuttp as _ImportedBinding_ebu_tt_live_bindings__ebuttp
import ebu_tt_live.bindings._ebutts as _ImportedBinding_ebu_tt_live_bindings__ebutts
import ebu_tt_live.bindings._ittp as _ImportedBinding_ebu_tt_live_bindings__ittp
import ebu_tt_live.bindings._itts as _ImportedBinding_ebu_tt_live_bindings__itts
import ebu_tt_live.bindings._ttm as _ImportedBinding_ebu_tt_live_bindings__ttm
import ebu_tt_live.bindings._ttp as _ImportedBinding_ebu_tt_live_bindings__ttp
import ebu_tt_live.bindings._tts as _ImportedBinding_ebu_tt_live_bindings__tts
import pyxb.binding.datatypes
import pyxb.binding.xml_

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.w3.org/ns/ttml', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ttm = _ImportedBinding_ebu_tt_live_bindings__ttm.Namespace
_Namespace_ttm.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_tts = _ImportedBinding_ebu_tt_live_bindings__tts.Namespace
_Namespace_tts.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_itts = _ImportedBinding_ebu_tt_live_bindings__itts.Namespace
_Namespace_itts.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ebutts = _ImportedBinding_ebu_tt_live_bindings__ebutts.Namespace
_Namespace_ebutts.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ttp = _ImportedBinding_ebu_tt_live_bindings__ttp.Namespace
_Namespace_ttp.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ittp = _ImportedBinding_ebu_tt_live_bindings__ittp.Namespace
_Namespace_ittp.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ebuttm = _ImportedBinding_ebu_tt_live_bindings__ebuttm.Namespace
_Namespace_ebuttm.configureCategories(['typeBinding', 'elementBinding'])
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


# Complex type {http://www.w3.org/ns/ttml}d_head_type with content type ELEMENT_ONLY
class d_head_type (pyxb.binding.basis.complexTypeDefinition):
    """Contains metadata as well as layout and styling information that are
				referenced by the subtitle blocks in the body."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'd_head_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 22, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_d_head_type_httpwww_w3_orgnsttmlmetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 30, 3), )

    
    metadata = property(__metadata.value, __metadata.set, None, 'Generic container for metadata information that applies to\n\t\t\t\t\t\tthe whole document.')

    
    # Element {http://www.w3.org/ns/ttml}styling uses Python identifier styling
    __styling = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'styling'), 'styling', '__httpwww_w3_orgnsttml_d_head_type_httpwww_w3_orgnsttmlstyling', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 36, 3), )

    
    styling = property(__styling.value, __styling.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml}layout uses Python identifier layout
    __layout = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'layout'), 'layout', '__httpwww_w3_orgnsttml_d_head_type_httpwww_w3_orgnsttmllayout', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 37, 3), )

    
    layout = property(__layout.value, __layout.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml#metadata}copyright uses Python identifier copyright
    __copyright = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ttm, 'copyright'), 'copyright', '__httpwww_w3_orgnsttml_d_head_type_httpwww_w3_orgnsttmlmetadatacopyright', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 68, 2), )

    
    copyright = property(__copyright.value, __copyright.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __styling.name() : __styling,
        __layout.name() : __layout,
        __copyright.name() : __copyright
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.d_head_type = d_head_type
Namespace.addCategoryObject('typeBinding', 'd_head_type', d_head_type)


# Complex type {http://www.w3.org/ns/ttml}d_metadata_type with content type ELEMENT_ONLY
class d_metadata_type (pyxb.binding.basis.complexTypeDefinition):
    """Container for metadata information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'd_metadata_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 41, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.d_metadata_type = d_metadata_type
Namespace.addCategoryObject('typeBinding', 'd_metadata_type', d_metadata_type)


# Complex type {http://www.w3.org/ns/ttml}d_styling_type with content type ELEMENT_ONLY
class d_styling_type (pyxb.binding.basis.complexTypeDefinition):
    """Container for styling information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'd_styling_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 52, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_d_styling_type_httpwww_w3_orgnsttmlmetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 57, 3), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml}style uses Python identifier style
    __style = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'style'), 'style', '__httpwww_w3_orgnsttml_d_styling_type_httpwww_w3_orgnsttmlstyle', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 58, 3), )

    
    style = property(__style.value, __style.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __style.name() : __style
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.d_styling_type = d_styling_type
Namespace.addCategoryObject('typeBinding', 'd_styling_type', d_styling_type)


# Complex type {http://www.w3.org/ns/ttml}d_layout_type with content type ELEMENT_ONLY
class d_layout_type (pyxb.binding.basis.complexTypeDefinition):
    """Container element for layout information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'd_layout_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 90, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_d_layout_type_httpwww_w3_orgnsttmlmetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 95, 3), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml}region uses Python identifier region
    __region = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'region'), 'region', '__httpwww_w3_orgnsttml_d_layout_type_httpwww_w3_orgnsttmlregion', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 96, 3), )

    
    region = property(__region.value, __region.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __region.name() : __region
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.d_layout_type = d_layout_type
Namespace.addCategoryObject('typeBinding', 'd_layout_type', d_layout_type)


# Complex type {http://www.w3.org/ns/ttml}d_body_type with content type ELEMENT_ONLY
class d_body_type (pyxb.binding.basis.complexTypeDefinition):
    """Container of the subtitle and the timing
				information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'd_body_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 136, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_d_body_type_httpwww_w3_orgnsttmlmetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 142, 3), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml}div uses Python identifier div
    __div = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'div'), 'div', '__httpwww_w3_orgnsttml_d_body_type_httpwww_w3_orgnsttmldiv', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 143, 3), )

    
    div = property(__div.value, __div.set, None, None)

    
    # Attribute style uses Python identifier style
    __style = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'style'), 'style', '__httpwww_w3_orgnsttml_d_body_type_style', pyxb.binding.datatypes.IDREFS)
    __style._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 145, 2)
    __style._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 145, 2)
    
    style = property(__style.value, __style.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}agent uses Python identifier agent
    __agent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'agent'), 'agent', '__httpwww_w3_orgnsttml_d_body_type_httpwww_w3_orgnsttmlmetadataagent', pyxb.binding.datatypes.IDREFS)
    __agent._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 12, 2)
    __agent._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 146, 2)
    
    agent = property(__agent.value, __agent.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'role'), 'role', '__httpwww_w3_orgnsttml_d_body_type_httpwww_w3_orgnsttmlmetadatarole', pyxb.binding.datatypes.NMTOKENS)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 13, 2)
    __role._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 147, 2)
    
    role = property(__role.value, __role.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __div.name() : __div
    })
    _AttributeMap.update({
        __style.name() : __style,
        __agent.name() : __agent,
        __role.name() : __role
    })
_module_typeBindings.d_body_type = d_body_type
Namespace.addCategoryObject('typeBinding', 'd_body_type', d_body_type)


# Complex type {http://www.w3.org/ns/ttml}d_div_type with content type ELEMENT_ONLY
class d_div_type (pyxb.binding.basis.complexTypeDefinition):
    """Logical container of textual content."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'd_div_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 149, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_d_div_type_httpwww_w3_orgnsttmlmetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 154, 3), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml}p uses Python identifier p
    __p = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'p'), 'p', '__httpwww_w3_orgnsttml_d_div_type_httpwww_w3_orgnsttmlp', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 156, 4), )

    
    p = property(__p.value, __p.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'id'), 'id', '__httpwww_w3_orgnsttml_d_div_type_httpwww_w3_orgXML1998namespaceid', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = None
    __id._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 159, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_orgnsttml_d_div_type_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 180, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute region uses Python identifier region
    __region = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'region'), 'region', '__httpwww_w3_orgnsttml_d_div_type_region', pyxb.binding.datatypes.IDREF)
    __region._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 165, 2)
    __region._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 165, 2)
    
    region = property(__region.value, __region.set, None, 'Application of layout and style information through reference\n\t\t\t\t\tof a region.')

    
    # Attribute style uses Python identifier style
    __style = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'style'), 'style', '__httpwww_w3_orgnsttml_d_div_type_style', pyxb.binding.datatypes.IDREFS)
    __style._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 171, 2)
    __style._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 171, 2)
    
    style = property(__style.value, __style.set, None, 'ID(s) of one or more style element(s). The style information\n\t\t\t\t\tshall be applied to the enclosed content of the tt:div\n\t\t\t\t\telement.')

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}agent uses Python identifier agent
    __agent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'agent'), 'agent', '__httpwww_w3_orgnsttml_d_div_type_httpwww_w3_orgnsttmlmetadataagent', pyxb.binding.datatypes.IDREFS)
    __agent._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 12, 2)
    __agent._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 178, 2)
    
    agent = property(__agent.value, __agent.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'role'), 'role', '__httpwww_w3_orgnsttml_d_div_type_httpwww_w3_orgnsttmlmetadatarole', pyxb.binding.datatypes.NMTOKENS)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 13, 2)
    __role._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 179, 2)
    
    role = property(__role.value, __role.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __p.name() : __p
    })
    _AttributeMap.update({
        __id.name() : __id,
        __lang.name() : __lang,
        __region.name() : __region,
        __style.name() : __style,
        __agent.name() : __agent,
        __role.name() : __role
    })
_module_typeBindings.d_div_type = d_div_type
Namespace.addCategoryObject('typeBinding', 'd_div_type', d_div_type)


# Complex type {http://www.w3.org/ns/ttml}d_br_type with content type ELEMENT_ONLY
class d_br_type (pyxb.binding.basis.complexTypeDefinition):
    """Forced line break."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'd_br_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 289, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_d_br_type_httpwww_w3_orgnsttmlmetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 294, 3), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'role'), 'role', '__httpwww_w3_orgnsttml_d_br_type_httpwww_w3_orgnsttmlmetadatarole', pyxb.binding.datatypes.NMTOKENS)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 13, 2)
    __role._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 296, 2)
    
    role = property(__role.value, __role.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata
    })
    _AttributeMap.update({
        __role.name() : __role
    })
_module_typeBindings.d_br_type = d_br_type
Namespace.addCategoryObject('typeBinding', 'd_br_type', d_br_type)


# Complex type {http://www.w3.org/ns/ttml}head_type with content type ELEMENT_ONLY
class head_type (pyxb.binding.basis.complexTypeDefinition):
    """Contains metadata as well as layout and styling information that are
				referenced by the subtitle blocks in the body."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'head_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 30, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_head_type_httpwww_w3_orgnsttmlmetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 36, 6), )

    
    metadata = property(__metadata.value, __metadata.set, None, 'Generic container for metadata information that applies to the\n\t\t\t\t\t\twhole document.')

    
    # Element {http://www.w3.org/ns/ttml}styling uses Python identifier styling
    __styling = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'styling'), 'styling', '__httpwww_w3_orgnsttml_head_type_httpwww_w3_orgnsttmlstyling', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 43, 3), )

    
    styling = property(__styling.value, __styling.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml}layout uses Python identifier layout
    __layout = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'layout'), 'layout', '__httpwww_w3_orgnsttml_head_type_httpwww_w3_orgnsttmllayout', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 44, 3), )

    
    layout = property(__layout.value, __layout.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml#metadata}copyright uses Python identifier copyright
    __copyright = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ttm, 'copyright'), 'copyright', '__httpwww_w3_orgnsttml_head_type_httpwww_w3_orgnsttmlmetadatacopyright', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 68, 2), )

    
    copyright = property(__copyright.value, __copyright.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __styling.name() : __styling,
        __layout.name() : __layout,
        __copyright.name() : __copyright
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.head_type = head_type
Namespace.addCategoryObject('typeBinding', 'head_type', head_type)


# Complex type {http://www.w3.org/ns/ttml}styling with content type ELEMENT_ONLY
class styling (pyxb.binding.basis.complexTypeDefinition):
    """Container for styling information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'styling')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 47, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_styling_httpwww_w3_orgnsttmlmetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 52, 6), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml}style uses Python identifier style
    __style = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'style'), 'style', '__httpwww_w3_orgnsttml_styling_httpwww_w3_orgnsttmlstyle', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 53, 3), )

    
    style = property(__style.value, __style.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __style.name() : __style
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.styling = styling
Namespace.addCategoryObject('typeBinding', 'styling', styling)


# Complex type {http://www.w3.org/ns/ttml}layout with content type ELEMENT_ONLY
class layout (pyxb.binding.basis.complexTypeDefinition):
    """Container element for layout information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'layout')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 101, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_layout_httpwww_w3_orgnsttmlmetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 106, 6), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml}region uses Python identifier region
    __region = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'region'), 'region', '__httpwww_w3_orgnsttml_layout_httpwww_w3_orgnsttmlregion', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 107, 3), )

    
    region = property(__region.value, __region.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __region.name() : __region
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.layout = layout
Namespace.addCategoryObject('typeBinding', 'layout', layout)


# Complex type {http://www.w3.org/ns/ttml}br_type with content type ELEMENT_ONLY
class br_type (pyxb.binding.basis.complexTypeDefinition):
    """Forced line break."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'br_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 344, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_br_type_httpwww_w3_orgnsttmlmetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 349, 6), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'role'), 'role', '__httpwww_w3_orgnsttml_br_type_httpwww_w3_orgnsttmlmetadatarole', pyxb.binding.datatypes.NMTOKENS)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 13, 2)
    __role._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 351, 2)
    
    role = property(__role.value, __role.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata
    })
    _AttributeMap.update({
        __role.name() : __role
    })
_module_typeBindings.br_type = br_type
Namespace.addCategoryObject('typeBinding', 'br_type', br_type)


# Complex type {http://www.w3.org/ns/ttml}d_style_type with content type ELEMENT_ONLY
class d_style_type (pyxb.binding.basis.complexTypeDefinition):
    """Set of style information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'd_style_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 61, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_d_style_type_httpwww_w3_orgnsttmlmetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 66, 3), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'id'), 'id', '__httpwww_w3_orgnsttml_d_style_type_httpwww_w3_orgXML1998namespaceid', pyxb.binding.datatypes.ID, required=True)
    __id._DeclarationLocation = None
    __id._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 68, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#styling}direction uses Python identifier direction
    __direction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'direction'), 'direction', '__httpwww_w3_orgnsttml_d_style_type_httpwww_w3_orgnsttmlstylingdirection', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON)
    __direction._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 11, 1)
    __direction._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 74, 2)
    
    direction = property(__direction.value, __direction.set, None, 'Directionality if bi-directional text is used.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}fontFamily uses Python identifier fontFamily
    __fontFamily = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'fontFamily'), 'fontFamily', '__httpwww_w3_orgnsttml_d_style_type_httpwww_w3_orgnsttmlstylingfontFamily', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.fontFamilyType)
    __fontFamily._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 22, 1)
    __fontFamily._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 75, 2)
    
    fontFamily = property(__fontFamily.value, __fontFamily.set, None, 'Font-family from which glyphs are selected.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}fontSize uses Python identifier fontSize
    __fontSize = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'fontSize'), 'fontSize', '__httpwww_w3_orgnsttml_d_style_type_httpwww_w3_orgnsttmlstylingfontSize', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.fontSizeType)
    __fontSize._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 27, 1)
    __fontSize._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 76, 2)
    
    fontSize = property(__fontSize.value, __fontSize.set, None, 'The font-size of a glyph.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}lineHeight uses Python identifier lineHeight
    __lineHeight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'lineHeight'), 'lineHeight', '__httpwww_w3_orgnsttml_d_style_type_httpwww_w3_orgnsttmlstylinglineHeight', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.lineHeightType)
    __lineHeight._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 32, 1)
    __lineHeight._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 77, 2)
    
    lineHeight = property(__lineHeight.value, __lineHeight.set, None, 'Inter-baseline separation between line areas.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}textAlign uses Python identifier textAlign
    __textAlign = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'textAlign'), 'textAlign', '__httpwww_w3_orgnsttml_d_style_type_httpwww_w3_orgnsttmlstylingtextAlign', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON_)
    __textAlign._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 37, 1)
    __textAlign._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 78, 2)
    
    textAlign = property(__textAlign.value, __textAlign.set, None, 'Alignment of inline areas in a containing block.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}color uses Python identifier color
    __color = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'color'), 'color', '__httpwww_w3_orgnsttml_d_style_type_httpwww_w3_orgnsttmlstylingcolor', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.colorType)
    __color._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 51, 1)
    __color._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 79, 2)
    
    color = property(__color.value, __color.set, None, 'Foreground colour of an area.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}backgroundColor uses Python identifier backgroundColor
    __backgroundColor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'backgroundColor'), 'backgroundColor', '__httpwww_w3_orgnsttml_d_style_type_httpwww_w3_orgnsttmlstylingbackgroundColor', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.colorType)
    __backgroundColor._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 56, 1)
    __backgroundColor._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 80, 2)
    
    backgroundColor = property(__backgroundColor.value, __backgroundColor.set, None, 'Background colour of a subtitle or a region.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}fontStyle uses Python identifier fontStyle
    __fontStyle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'fontStyle'), 'fontStyle', '__httpwww_w3_orgnsttml_d_style_type_httpwww_w3_orgnsttmlstylingfontStyle', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON_2)
    __fontStyle._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 61, 1)
    __fontStyle._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 81, 2)
    
    fontStyle = property(__fontStyle.value, __fontStyle.set, None, 'Font style that applies to glyphs.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}fontWeight uses Python identifier fontWeight
    __fontWeight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'fontWeight'), 'fontWeight', '__httpwww_w3_orgnsttml_d_style_type_httpwww_w3_orgnsttmlstylingfontWeight', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON_3)
    __fontWeight._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 72, 1)
    __fontWeight._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 82, 2)
    
    fontWeight = property(__fontWeight.value, __fontWeight.set, None, 'Font weight that applies to glyphs.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}textDecoration uses Python identifier textDecoration
    __textDecoration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'textDecoration'), 'textDecoration', '__httpwww_w3_orgnsttml_d_style_type_httpwww_w3_orgnsttmlstylingtextDecoration', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON_4)
    __textDecoration._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 83, 1)
    __textDecoration._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 83, 2)
    
    textDecoration = property(__textDecoration.value, __textDecoration.set, None, 'Whether a glyph is underlined.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}unicodeBidi uses Python identifier unicodeBidi
    __unicodeBidi = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'unicodeBidi'), 'unicodeBidi', '__httpwww_w3_orgnsttml_d_style_type_httpwww_w3_orgnsttmlstylingunicodeBidi', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON_5)
    __unicodeBidi._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 94, 1)
    __unicodeBidi._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 84, 2)
    
    unicodeBidi = property(__unicodeBidi.value, __unicodeBidi.set, None, 'Directional embedding or override according to the Unicode\n\t\t\t\tbidirectional algorithm.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}wrapOption uses Python identifier wrapOption
    __wrapOption = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'wrapOption'), 'wrapOption', '__httpwww_w3_orgnsttml_d_style_type_httpwww_w3_orgnsttmlstylingwrapOption', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON_6)
    __wrapOption._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 107, 1)
    __wrapOption._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 85, 2)
    
    wrapOption = property(__wrapOption.value, __wrapOption.set, None, 'Defines whether or not automatic line wrapping (breaking) applies\n\t\t\t\twithin the context of the affected element.')

    
    # Attribute {http://www.w3.org/ns/ttml/profile/imsc1#styling}fillLineGap uses Python identifier fillLineGap
    __fillLineGap = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_itts, 'fillLineGap'), 'fillLineGap', '__httpwww_w3_orgnsttml_d_style_type_httpwww_w3_orgnsttmlprofileimsc1stylingfillLineGap', _ImportedBinding_ebu_tt_live_bindings__itts.STD_ANON)
    __fillLineGap._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/imsc1-styling.xsd', 6, 4)
    __fillLineGap._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 88, 2)
    
    fillLineGap = property(__fillLineGap.value, __fillLineGap.set, None, 'Controls the application of background between successive line areas.')

    
    # Attribute {urn:ebu:tt:style}multiRowAlign uses Python identifier multiRowAlign
    __multiRowAlign = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ebutts, 'multiRowAlign'), 'multiRowAlign', '__httpwww_w3_orgnsttml_d_style_type_urnebuttstylemultiRowAlign', _ImportedBinding_ebu_tt_live_bindings__ebutts.STD_ANON)
    __multiRowAlign._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_styling.xsd', 11, 1)
    __multiRowAlign._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 86, 2)
    
    multiRowAlign = property(__multiRowAlign.value, __multiRowAlign.set, None, 'Alignment of multiple ‘rows’ of inline areas within a containing block\n\t\t\t\tarea.')

    
    # Attribute {urn:ebu:tt:style}linePadding uses Python identifier linePadding
    __linePadding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ebutts, 'linePadding'), 'linePadding', '__httpwww_w3_orgnsttml_d_style_type_urnebuttstylelinePadding', _ImportedBinding_ebu_tt_live_bindings__ebutts.STD_ANON_)
    __linePadding._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_styling.xsd', 25, 1)
    __linePadding._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 87, 2)
    
    linePadding = property(__linePadding.value, __linePadding.set, None, ' Padding (or inset) space on the start and end edges of each rendered\n\t\t\t\tline area ')

    _ElementMap.update({
        __metadata.name() : __metadata
    })
    _AttributeMap.update({
        __id.name() : __id,
        __direction.name() : __direction,
        __fontFamily.name() : __fontFamily,
        __fontSize.name() : __fontSize,
        __lineHeight.name() : __lineHeight,
        __textAlign.name() : __textAlign,
        __color.name() : __color,
        __backgroundColor.name() : __backgroundColor,
        __fontStyle.name() : __fontStyle,
        __fontWeight.name() : __fontWeight,
        __textDecoration.name() : __textDecoration,
        __unicodeBidi.name() : __unicodeBidi,
        __wrapOption.name() : __wrapOption,
        __fillLineGap.name() : __fillLineGap,
        __multiRowAlign.name() : __multiRowAlign,
        __linePadding.name() : __linePadding
    })
_module_typeBindings.d_style_type = d_style_type
Namespace.addCategoryObject('typeBinding', 'd_style_type', d_style_type)


# Complex type {http://www.w3.org/ns/ttml}d_region_type with content type ELEMENT_ONLY
class d_region_type (pyxb.binding.basis.complexTypeDefinition):
    """Defines a space or area for the display of subtitle
				content."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'd_region_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 99, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_d_region_type_httpwww_w3_orgnsttmlmetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 105, 4), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'id'), 'id', '__httpwww_w3_orgnsttml_d_region_type_httpwww_w3_orgXML1998namespaceid', pyxb.binding.datatypes.ID, required=True)
    __id._DeclarationLocation = None
    __id._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 107, 3)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute style uses Python identifier style
    __style = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'style'), 'style', '__httpwww_w3_orgnsttml_d_region_type_style', pyxb.binding.datatypes.IDREFS)
    __style._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 120, 3)
    __style._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 120, 3)
    
    style = property(__style.value, __style.set, None, 'ID(s) of one or more style element(s).')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}displayAlign uses Python identifier displayAlign
    __displayAlign = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'displayAlign'), 'displayAlign', '__httpwww_w3_orgnsttml_d_region_type_httpwww_w3_orgnsttmlstylingdisplayAlign', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON_7)
    __displayAlign._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 119, 1)
    __displayAlign._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 125, 3)
    
    displayAlign = property(__displayAlign.value, __displayAlign.set, None, 'Alignment in the block progression direction.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}padding uses Python identifier padding
    __padding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'padding'), 'padding', '__httpwww_w3_orgnsttml_d_region_type_httpwww_w3_orgnsttmlstylingpadding', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.paddingType)
    __padding._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 131, 1)
    __padding._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 126, 3)
    
    padding = property(__padding.value, __padding.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#styling}writingMode uses Python identifier writingMode
    __writingMode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'writingMode'), 'writingMode', '__httpwww_w3_orgnsttml_d_region_type_httpwww_w3_orgnsttmlstylingwritingMode', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON_8)
    __writingMode._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 132, 1)
    __writingMode._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 132, 3)
    
    writingMode = property(__writingMode.value, __writingMode.set, None, 'Writing mode of subtitle content.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}showBackground uses Python identifier showBackground
    __showBackground = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'showBackground'), 'showBackground', '__httpwww_w3_orgnsttml_d_region_type_httpwww_w3_orgnsttmlstylingshowBackground', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON_9)
    __showBackground._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 148, 1)
    __showBackground._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 133, 3)
    
    showBackground = property(__showBackground.value, __showBackground.set, None, 'Constraints on when the background color of a region is intended to be\n\t\t\t\tpresented.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}overflow uses Python identifier overflow
    __overflow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'overflow'), 'overflow', '__httpwww_w3_orgnsttml_d_region_type_httpwww_w3_orgnsttmlstylingoverflow', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON_10)
    __overflow._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 160, 1)
    __overflow._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 134, 3)
    
    overflow = property(__overflow.value, __overflow.set, None, 'Defines whether a region area is clipped if the content of the region\n\t\t\t\toverflows the specified extent of the region.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}extent uses Python identifier extent
    __extent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'extent'), 'extent', '__httpwww_w3_orgnsttml_d_region_type_httpwww_w3_orgnsttmlstylingextent', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.extentType, required=True)
    __extent._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 172, 1)
    __extent._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 113, 3)
    
    extent = property(__extent.value, __extent.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#styling}origin uses Python identifier origin
    __origin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'origin'), 'origin', '__httpwww_w3_orgnsttml_d_region_type_httpwww_w3_orgnsttmlstylingorigin', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.originType, required=True)
    __origin._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 173, 1)
    __origin._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 112, 3)
    
    origin = property(__origin.value, __origin.set, None, 'The x and y coordinates of the top left corner of a region with\n\t\t\t\trespect to the active video the document was authored for. The (0, 0) coordinate\n\t\t\t\tshall be assumed to be the top left corner of the active video. Values in percentage\n\t\t\t\tshall be relative to the width and height of the active video. oordinates of the\n\t\t\t\torigin of a region with respect to the active video the document was authored for.\n\t\t\t\tValues in percentage shall be relative to the width and height of the active\n\t\t\t\tvideo.')

    _ElementMap.update({
        __metadata.name() : __metadata
    })
    _AttributeMap.update({
        __id.name() : __id,
        __style.name() : __style,
        __displayAlign.name() : __displayAlign,
        __padding.name() : __padding,
        __writingMode.name() : __writingMode,
        __showBackground.name() : __showBackground,
        __overflow.name() : __overflow,
        __extent.name() : __extent,
        __origin.name() : __origin
    })
_module_typeBindings.d_region_type = d_region_type
Namespace.addCategoryObject('typeBinding', 'd_region_type', d_region_type)


# Complex type {http://www.w3.org/ns/ttml}d_p_type with content type MIXED
class d_p_type (pyxb.binding.basis.complexTypeDefinition):
    """Logical paragraph."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'd_p_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 182, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_d_p_type_httpwww_w3_orgnsttmlmetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 187, 3), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml}br uses Python identifier br
    __br = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'br'), 'br', '__httpwww_w3_orgnsttml_d_p_type_httpwww_w3_orgnsttmlbr', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 189, 4), )

    
    br = property(__br.value, __br.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml}span uses Python identifier span
    __span = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'span'), 'span', '__httpwww_w3_orgnsttml_d_p_type_httpwww_w3_orgnsttmlspan', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 190, 4), )

    
    span = property(__span.value, __span.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_orgnsttml_d_p_type_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 204, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}space uses Python identifier space
    __space = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'space'), 'space', '__httpwww_w3_orgnsttml_d_p_type_httpwww_w3_orgXML1998namespacespace', pyxb.binding.xml_.STD_ANON_space)
    __space._DeclarationLocation = None
    __space._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 198, 2)
    
    space = property(__space.value, __space.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'id'), 'id', '__httpwww_w3_orgnsttml_d_p_type_httpwww_w3_orgXML1998namespaceid', pyxb.binding.datatypes.ID, required=True)
    __id._DeclarationLocation = None
    __id._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 193, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute region uses Python identifier region
    __region = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'region'), 'region', '__httpwww_w3_orgnsttml_d_p_type_region', pyxb.binding.datatypes.IDREF)
    __region._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 210, 2)
    __region._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 210, 2)
    
    region = property(__region.value, __region.set, None, 'Application of layout information through reference of a\n\t\t\t\t\tregion.')

    
    # Attribute style uses Python identifier style
    __style = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'style'), 'style', '__httpwww_w3_orgnsttml_d_p_type_style', pyxb.binding.datatypes.IDREFS)
    __style._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 216, 2)
    __style._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 216, 2)
    
    style = property(__style.value, __style.set, None, 'ID(s) of one or more style element(s). The style information\n\t\t\t\t\tshall be applied to the enclosed content of the tt:p\n\t\t\t\t\telement.')

    
    # Attribute begin uses Python identifier begin
    __begin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'begin'), 'begin', '__httpwww_w3_orgnsttml_d_p_type_begin', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.mediaTimingType)
    __begin._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 223, 2)
    __begin._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 223, 2)
    
    begin = property(__begin.value, __begin.set, None, 'Start point of a temporal interval associated with a tt:p\n\t\t\t\t\telement.')

    
    # Attribute end uses Python identifier end
    __end = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'end'), 'end', '__httpwww_w3_orgnsttml_d_p_type_end', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.mediaTimingType)
    __end._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 229, 2)
    __end._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 229, 2)
    
    end = property(__end.value, __end.set, None, 'End point of a temporal interval associated with a tt:p\n\t\t\t\t\telement.')

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}agent uses Python identifier agent
    __agent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'agent'), 'agent', '__httpwww_w3_orgnsttml_d_p_type_httpwww_w3_orgnsttmlmetadataagent', pyxb.binding.datatypes.IDREFS)
    __agent._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 12, 2)
    __agent._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 235, 2)
    
    agent = property(__agent.value, __agent.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'role'), 'role', '__httpwww_w3_orgnsttml_d_p_type_httpwww_w3_orgnsttmlmetadatarole', pyxb.binding.datatypes.NMTOKENS)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 13, 2)
    __role._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 236, 2)
    
    role = property(__role.value, __role.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __br.name() : __br,
        __span.name() : __span
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __space.name() : __space,
        __id.name() : __id,
        __region.name() : __region,
        __style.name() : __style,
        __begin.name() : __begin,
        __end.name() : __end,
        __agent.name() : __agent,
        __role.name() : __role
    })
_module_typeBindings.d_p_type = d_p_type
Namespace.addCategoryObject('typeBinding', 'd_p_type', d_p_type)


# Complex type {http://www.w3.org/ns/ttml}d_span_type with content type MIXED
class d_span_type (pyxb.binding.basis.complexTypeDefinition):
    """Inline element to allow the application of local style information,
				annotation or metadata."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'd_span_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 238, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_d_span_type_httpwww_w3_orgnsttmlmetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 244, 3), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml}br uses Python identifier br
    __br = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'br'), 'br', '__httpwww_w3_orgnsttml_d_span_type_httpwww_w3_orgnsttmlbr', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 246, 4), )

    
    br = property(__br.value, __br.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'id'), 'id', '__httpwww_w3_orgnsttml_d_span_type_httpwww_w3_orgXML1998namespaceid', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = None
    __id._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 249, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_orgnsttml_d_span_type_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 261, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}space uses Python identifier space
    __space = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'space'), 'space', '__httpwww_w3_orgnsttml_d_span_type_httpwww_w3_orgXML1998namespacespace', pyxb.binding.xml_.STD_ANON_space)
    __space._DeclarationLocation = None
    __space._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 255, 2)
    
    space = property(__space.value, __space.set, None, None)

    
    # Attribute style uses Python identifier style
    __style = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'style'), 'style', '__httpwww_w3_orgnsttml_d_span_type_style', pyxb.binding.datatypes.IDREFS)
    __style._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 267, 2)
    __style._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 267, 2)
    
    style = property(__style.value, __style.set, None, 'ID(s) of one or more style element(s). The style information\n\t\t\t\t\tshall be applied to the enclosed content of the tt:span\n\t\t\t\t\telement.')

    
    # Attribute begin uses Python identifier begin
    __begin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'begin'), 'begin', '__httpwww_w3_orgnsttml_d_span_type_begin', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.mediaTimingType)
    __begin._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 274, 2)
    __begin._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 274, 2)
    
    begin = property(__begin.value, __begin.set, None, 'Start point of a temporal interval associated with the\n\t\t\t\t\telement.')

    
    # Attribute end uses Python identifier end
    __end = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'end'), 'end', '__httpwww_w3_orgnsttml_d_span_type_end', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.mediaTimingType)
    __end._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 280, 2)
    __end._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 280, 2)
    
    end = property(__end.value, __end.set, None, 'End point of a temporal interval associated with the\n\t\t\t\t\telement.')

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}agent uses Python identifier agent
    __agent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'agent'), 'agent', '__httpwww_w3_orgnsttml_d_span_type_httpwww_w3_orgnsttmlmetadataagent', pyxb.binding.datatypes.IDREFS)
    __agent._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 12, 2)
    __agent._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 286, 2)
    
    agent = property(__agent.value, __agent.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'role'), 'role', '__httpwww_w3_orgnsttml_d_span_type_httpwww_w3_orgnsttmlmetadatarole', pyxb.binding.datatypes.NMTOKENS)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 13, 2)
    __role._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 287, 2)
    
    role = property(__role.value, __role.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __br.name() : __br
    })
    _AttributeMap.update({
        __id.name() : __id,
        __lang.name() : __lang,
        __space.name() : __space,
        __style.name() : __style,
        __begin.name() : __begin,
        __end.name() : __end,
        __agent.name() : __agent,
        __role.name() : __role
    })
_module_typeBindings.d_span_type = d_span_type
Namespace.addCategoryObject('typeBinding', 'd_span_type', d_span_type)


# Complex type {http://www.w3.org/ns/ttml}style with content type ELEMENT_ONLY
class style (pyxb.binding.basis.complexTypeDefinition):
    """Set of style information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'style')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 57, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_style_httpwww_w3_orgnsttmlmetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 62, 6), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'id'), 'id', '__httpwww_w3_orgnsttml_style_httpwww_w3_orgXML1998namespaceid', pyxb.binding.datatypes.ID, required=True)
    __id._DeclarationLocation = None
    __id._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 64, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute style uses Python identifier style
    __style = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'style'), 'style', '__httpwww_w3_orgnsttml_style_style', pyxb.binding.datatypes.IDREFS)
    __style._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 70, 2)
    __style._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 70, 2)
    
    style = property(__style.value, __style.set, None, 'Reference to one or more other tt:style\n\t\t\t\t\telements.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}direction uses Python identifier direction
    __direction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'direction'), 'direction', '__httpwww_w3_orgnsttml_style_httpwww_w3_orgnsttmlstylingdirection', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON)
    __direction._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 11, 1)
    __direction._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 76, 2)
    
    direction = property(__direction.value, __direction.set, None, 'Directionality if bi-directional text is used.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}fontFamily uses Python identifier fontFamily
    __fontFamily = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'fontFamily'), 'fontFamily', '__httpwww_w3_orgnsttml_style_httpwww_w3_orgnsttmlstylingfontFamily', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.fontFamilyType)
    __fontFamily._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 22, 1)
    __fontFamily._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 77, 2)
    
    fontFamily = property(__fontFamily.value, __fontFamily.set, None, 'Font-family from which glyphs are selected.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}fontSize uses Python identifier fontSize
    __fontSize = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'fontSize'), 'fontSize', '__httpwww_w3_orgnsttml_style_httpwww_w3_orgnsttmlstylingfontSize', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.fontSizeType)
    __fontSize._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 27, 1)
    __fontSize._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 78, 2)
    
    fontSize = property(__fontSize.value, __fontSize.set, None, 'The font-size of a glyph.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}lineHeight uses Python identifier lineHeight
    __lineHeight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'lineHeight'), 'lineHeight', '__httpwww_w3_orgnsttml_style_httpwww_w3_orgnsttmlstylinglineHeight', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.lineHeightType)
    __lineHeight._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 32, 1)
    __lineHeight._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 79, 2)
    
    lineHeight = property(__lineHeight.value, __lineHeight.set, None, 'Inter-baseline separation between line areas.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}textAlign uses Python identifier textAlign
    __textAlign = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'textAlign'), 'textAlign', '__httpwww_w3_orgnsttml_style_httpwww_w3_orgnsttmlstylingtextAlign', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON_)
    __textAlign._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 37, 1)
    __textAlign._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 80, 2)
    
    textAlign = property(__textAlign.value, __textAlign.set, None, 'Alignment of inline areas in a containing block.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}color uses Python identifier color
    __color = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'color'), 'color', '__httpwww_w3_orgnsttml_style_httpwww_w3_orgnsttmlstylingcolor', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.colorType)
    __color._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 51, 1)
    __color._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 81, 2)
    
    color = property(__color.value, __color.set, None, 'Foreground colour of an area.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}backgroundColor uses Python identifier backgroundColor
    __backgroundColor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'backgroundColor'), 'backgroundColor', '__httpwww_w3_orgnsttml_style_httpwww_w3_orgnsttmlstylingbackgroundColor', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.colorType)
    __backgroundColor._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 56, 1)
    __backgroundColor._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 82, 2)
    
    backgroundColor = property(__backgroundColor.value, __backgroundColor.set, None, 'Background colour of a subtitle or a region.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}fontStyle uses Python identifier fontStyle
    __fontStyle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'fontStyle'), 'fontStyle', '__httpwww_w3_orgnsttml_style_httpwww_w3_orgnsttmlstylingfontStyle', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON_2)
    __fontStyle._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 61, 1)
    __fontStyle._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 83, 2)
    
    fontStyle = property(__fontStyle.value, __fontStyle.set, None, 'Font style that applies to glyphs.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}fontWeight uses Python identifier fontWeight
    __fontWeight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'fontWeight'), 'fontWeight', '__httpwww_w3_orgnsttml_style_httpwww_w3_orgnsttmlstylingfontWeight', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON_3)
    __fontWeight._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 72, 1)
    __fontWeight._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 84, 2)
    
    fontWeight = property(__fontWeight.value, __fontWeight.set, None, 'Font weight that applies to glyphs.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}textDecoration uses Python identifier textDecoration
    __textDecoration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'textDecoration'), 'textDecoration', '__httpwww_w3_orgnsttml_style_httpwww_w3_orgnsttmlstylingtextDecoration', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON_4)
    __textDecoration._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 83, 1)
    __textDecoration._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 85, 2)
    
    textDecoration = property(__textDecoration.value, __textDecoration.set, None, 'Whether a glyph is underlined.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}unicodeBidi uses Python identifier unicodeBidi
    __unicodeBidi = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'unicodeBidi'), 'unicodeBidi', '__httpwww_w3_orgnsttml_style_httpwww_w3_orgnsttmlstylingunicodeBidi', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON_5)
    __unicodeBidi._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 94, 1)
    __unicodeBidi._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 86, 2)
    
    unicodeBidi = property(__unicodeBidi.value, __unicodeBidi.set, None, 'Directional embedding or override according to the Unicode\n\t\t\t\tbidirectional algorithm.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}wrapOption uses Python identifier wrapOption
    __wrapOption = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'wrapOption'), 'wrapOption', '__httpwww_w3_orgnsttml_style_httpwww_w3_orgnsttmlstylingwrapOption', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON_6)
    __wrapOption._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 107, 1)
    __wrapOption._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 87, 2)
    
    wrapOption = property(__wrapOption.value, __wrapOption.set, None, 'Defines whether or not automatic line wrapping (breaking) applies\n\t\t\t\twithin the context of the affected element.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}padding uses Python identifier padding
    __padding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'padding'), 'padding', '__httpwww_w3_orgnsttml_style_httpwww_w3_orgnsttmlstylingpadding', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.paddingType)
    __padding._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 131, 1)
    __padding._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 88, 2)
    
    padding = property(__padding.value, __padding.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml/profile/imsc1#styling}fillLineGap uses Python identifier fillLineGap
    __fillLineGap = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_itts, 'fillLineGap'), 'fillLineGap', '__httpwww_w3_orgnsttml_style_httpwww_w3_orgnsttmlprofileimsc1stylingfillLineGap', _ImportedBinding_ebu_tt_live_bindings__itts.STD_ANON)
    __fillLineGap._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/imsc1-styling.xsd', 6, 4)
    __fillLineGap._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 97, 2)
    
    fillLineGap = property(__fillLineGap.value, __fillLineGap.set, None, 'Controls the application of background between successive line areas.')

    
    # Attribute {urn:ebu:tt:style}multiRowAlign uses Python identifier multiRowAlign
    __multiRowAlign = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ebutts, 'multiRowAlign'), 'multiRowAlign', '__httpwww_w3_orgnsttml_style_urnebuttstylemultiRowAlign', _ImportedBinding_ebu_tt_live_bindings__ebutts.STD_ANON)
    __multiRowAlign._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_styling.xsd', 11, 1)
    __multiRowAlign._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 95, 2)
    
    multiRowAlign = property(__multiRowAlign.value, __multiRowAlign.set, None, 'Alignment of multiple ‘rows’ of inline areas within a containing block\n\t\t\t\tarea.')

    
    # Attribute {urn:ebu:tt:style}linePadding uses Python identifier linePadding
    __linePadding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ebutts, 'linePadding'), 'linePadding', '__httpwww_w3_orgnsttml_style_urnebuttstylelinePadding', _ImportedBinding_ebu_tt_live_bindings__ebutts.STD_ANON_)
    __linePadding._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_styling.xsd', 25, 1)
    __linePadding._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 96, 2)
    
    linePadding = property(__linePadding.value, __linePadding.set, None, ' Padding (or inset) space on the start and end edges of each rendered\n\t\t\t\tline area ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/ns/ttml'))
    _ElementMap.update({
        __metadata.name() : __metadata
    })
    _AttributeMap.update({
        __id.name() : __id,
        __style.name() : __style,
        __direction.name() : __direction,
        __fontFamily.name() : __fontFamily,
        __fontSize.name() : __fontSize,
        __lineHeight.name() : __lineHeight,
        __textAlign.name() : __textAlign,
        __color.name() : __color,
        __backgroundColor.name() : __backgroundColor,
        __fontStyle.name() : __fontStyle,
        __fontWeight.name() : __fontWeight,
        __textDecoration.name() : __textDecoration,
        __unicodeBidi.name() : __unicodeBidi,
        __wrapOption.name() : __wrapOption,
        __padding.name() : __padding,
        __fillLineGap.name() : __fillLineGap,
        __multiRowAlign.name() : __multiRowAlign,
        __linePadding.name() : __linePadding
    })
_module_typeBindings.style = style
Namespace.addCategoryObject('typeBinding', 'style', style)


# Complex type {http://www.w3.org/ns/ttml}region with content type ELEMENT_ONLY
class region (pyxb.binding.basis.complexTypeDefinition):
    """Defines a space or area for the display of subtitle
				content."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'region')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 111, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_region_httpwww_w3_orgnsttmlmetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 117, 6), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'id'), 'id', '__httpwww_w3_orgnsttml_region_httpwww_w3_orgXML1998namespaceid', pyxb.binding.datatypes.ID, required=True)
    __id._DeclarationLocation = None
    __id._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 119, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute style uses Python identifier style
    __style = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'style'), 'style', '__httpwww_w3_orgnsttml_region_style', pyxb.binding.datatypes.IDREFS)
    __style._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 131, 2)
    __style._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 131, 2)
    
    style = property(__style.value, __style.set, None, 'ID(s) of one or more style element(s).')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}displayAlign uses Python identifier displayAlign
    __displayAlign = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'displayAlign'), 'displayAlign', '__httpwww_w3_orgnsttml_region_httpwww_w3_orgnsttmlstylingdisplayAlign', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON_7)
    __displayAlign._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 119, 1)
    __displayAlign._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 136, 2)
    
    displayAlign = property(__displayAlign.value, __displayAlign.set, None, 'Alignment in the block progression direction.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}padding uses Python identifier padding
    __padding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'padding'), 'padding', '__httpwww_w3_orgnsttml_region_httpwww_w3_orgnsttmlstylingpadding', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.paddingType)
    __padding._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 131, 1)
    __padding._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 137, 2)
    
    padding = property(__padding.value, __padding.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#styling}writingMode uses Python identifier writingMode
    __writingMode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'writingMode'), 'writingMode', '__httpwww_w3_orgnsttml_region_httpwww_w3_orgnsttmlstylingwritingMode', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON_8)
    __writingMode._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 132, 1)
    __writingMode._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 143, 2)
    
    writingMode = property(__writingMode.value, __writingMode.set, None, 'Writing mode of subtitle content.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}showBackground uses Python identifier showBackground
    __showBackground = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'showBackground'), 'showBackground', '__httpwww_w3_orgnsttml_region_httpwww_w3_orgnsttmlstylingshowBackground', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON_9)
    __showBackground._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 148, 1)
    __showBackground._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 144, 2)
    
    showBackground = property(__showBackground.value, __showBackground.set, None, 'Constraints on when the background color of a region is intended to be\n\t\t\t\tpresented.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}overflow uses Python identifier overflow
    __overflow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'overflow'), 'overflow', '__httpwww_w3_orgnsttml_region_httpwww_w3_orgnsttmlstylingoverflow', _ImportedBinding_ebu_tt_live_bindings__tts.STD_ANON_10)
    __overflow._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 160, 1)
    __overflow._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 145, 2)
    
    overflow = property(__overflow.value, __overflow.set, None, 'Defines whether a region area is clipped if the content of the region\n\t\t\t\toverflows the specified extent of the region.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}extent uses Python identifier extent
    __extent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'extent'), 'extent', '__httpwww_w3_orgnsttml_region_httpwww_w3_orgnsttmlstylingextent', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.extentType, required=True)
    __extent._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 172, 1)
    __extent._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 125, 2)
    
    extent = property(__extent.value, __extent.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#styling}origin uses Python identifier origin
    __origin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'origin'), 'origin', '__httpwww_w3_orgnsttml_region_httpwww_w3_orgnsttmlstylingorigin', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.originType, required=True)
    __origin._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 173, 1)
    __origin._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 124, 2)
    
    origin = property(__origin.value, __origin.set, None, 'The x and y coordinates of the top left corner of a region with\n\t\t\t\trespect to the active video the document was authored for. The (0, 0) coordinate\n\t\t\t\tshall be assumed to be the top left corner of the active video. Values in percentage\n\t\t\t\tshall be relative to the width and height of the active video. oordinates of the\n\t\t\t\torigin of a region with respect to the active video the document was authored for.\n\t\t\t\tValues in percentage shall be relative to the width and height of the active\n\t\t\t\tvideo.')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/ns/ttml'))
    _ElementMap.update({
        __metadata.name() : __metadata
    })
    _AttributeMap.update({
        __id.name() : __id,
        __style.name() : __style,
        __displayAlign.name() : __displayAlign,
        __padding.name() : __padding,
        __writingMode.name() : __writingMode,
        __showBackground.name() : __showBackground,
        __overflow.name() : __overflow,
        __extent.name() : __extent,
        __origin.name() : __origin
    })
_module_typeBindings.region = region
Namespace.addCategoryObject('typeBinding', 'region', region)


# Complex type {http://www.w3.org/ns/ttml}body_type with content type ELEMENT_ONLY
class body_type (pyxb.binding.basis.complexTypeDefinition):
    """Container of the subtitle and the timing
				information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'body_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 149, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_body_type_httpwww_w3_orgnsttmlmetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 155, 6), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml}div uses Python identifier div
    __div = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'div'), 'div', '__httpwww_w3_orgnsttml_body_type_httpwww_w3_orgnsttmldiv', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 156, 3), )

    
    div = property(__div.value, __div.set, None, None)

    
    # Attribute begin uses Python identifier begin
    __begin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'begin'), 'begin', '__httpwww_w3_orgnsttml_body_type_begin', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.timingType)
    __begin._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 160, 2)
    __begin._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 160, 2)
    
    begin = property(__begin.value, __begin.set, None, 'Start point of a temporal interval associated with a tt:body\n\t\t\t\t\telement.')

    
    # Attribute end uses Python identifier end
    __end = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'end'), 'end', '__httpwww_w3_orgnsttml_body_type_end', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.timingType)
    __end._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 166, 2)
    __end._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 166, 2)
    
    end = property(__end.value, __end.set, None, 'End point of a temporal interval associated with a tt:body\n\t\t\t\t\telement.')

    
    # Attribute dur uses Python identifier dur
    __dur = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dur'), 'dur', '__httpwww_w3_orgnsttml_body_type_dur', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.durationTimingType)
    __dur._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 172, 2)
    __dur._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 172, 2)
    
    dur = property(__dur.value, __dur.set, None, '\n\t\t\t\t\tThe maximum duration of the document relative to the resolved begin time, as defined in TTML 1.\n\t\t\t\t')

    
    # Attribute style uses Python identifier style
    __style = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'style'), 'style', '__httpwww_w3_orgnsttml_body_type_style', pyxb.binding.datatypes.IDREFS)
    __style._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 179, 2)
    __style._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 179, 2)
    
    style = property(__style.value, __style.set, None, 'ID(s) of one or more style element(s). The style information shall\n\t\t\t\t\tbe applied to the enclosed content of the tt:body element.')

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}agent uses Python identifier agent
    __agent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'agent'), 'agent', '__httpwww_w3_orgnsttml_body_type_httpwww_w3_orgnsttmlmetadataagent', pyxb.binding.datatypes.IDREFS)
    __agent._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 12, 2)
    __agent._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 158, 2)
    
    agent = property(__agent.value, __agent.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'role'), 'role', '__httpwww_w3_orgnsttml_body_type_httpwww_w3_orgnsttmlmetadatarole', pyxb.binding.datatypes.NMTOKENS)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 13, 2)
    __role._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 159, 2)
    
    role = property(__role.value, __role.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __div.name() : __div
    })
    _AttributeMap.update({
        __begin.name() : __begin,
        __end.name() : __end,
        __dur.name() : __dur,
        __style.name() : __style,
        __agent.name() : __agent,
        __role.name() : __role
    })
_module_typeBindings.body_type = body_type
Namespace.addCategoryObject('typeBinding', 'body_type', body_type)


# Complex type {http://www.w3.org/ns/ttml}div_type with content type ELEMENT_ONLY
class div_type (pyxb.binding.basis.complexTypeDefinition):
    """Logical container of textual content."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'div_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 186, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_div_type_httpwww_w3_orgnsttmlmetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 191, 6), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml}div uses Python identifier div
    __div = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'div'), 'div', '__httpwww_w3_orgnsttml_div_type_httpwww_w3_orgnsttmldiv', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 193, 4), )

    
    div = property(__div.value, __div.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml}p uses Python identifier p
    __p = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'p'), 'p', '__httpwww_w3_orgnsttml_div_type_httpwww_w3_orgnsttmlp', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 194, 4), )

    
    p = property(__p.value, __p.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_orgnsttml_div_type_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 203, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'id'), 'id', '__httpwww_w3_orgnsttml_div_type_httpwww_w3_orgXML1998namespaceid', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = None
    __id._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 197, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute region uses Python identifier region
    __region = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'region'), 'region', '__httpwww_w3_orgnsttml_div_type_region', pyxb.binding.datatypes.IDREF)
    __region._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 209, 2)
    __region._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 209, 2)
    
    region = property(__region.value, __region.set, None, 'Application of layout and style information through reference of a\n\t\t\t\t\tregion.')

    
    # Attribute style uses Python identifier style
    __style = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'style'), 'style', '__httpwww_w3_orgnsttml_div_type_style', pyxb.binding.datatypes.IDREFS)
    __style._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 215, 2)
    __style._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 215, 2)
    
    style = property(__style.value, __style.set, None, 'ID(s) of one or more style element(s). The style information shall\n\t\t\t\t\tbe applied to the enclosed content of the tt:div element.')

    
    # Attribute begin uses Python identifier begin
    __begin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'begin'), 'begin', '__httpwww_w3_orgnsttml_div_type_begin', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.timingType)
    __begin._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 223, 2)
    __begin._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 223, 2)
    
    begin = property(__begin.value, __begin.set, None, 'Start point of a temporal interval associated with a tt:div\n\t\t\t\t\telement.')

    
    # Attribute end uses Python identifier end
    __end = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'end'), 'end', '__httpwww_w3_orgnsttml_div_type_end', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.timingType)
    __end._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 229, 2)
    __end._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 229, 2)
    
    end = property(__end.value, __end.set, None, 'End point of a temporal interval associated with a tt:div\n\t\t\t\t\telement.')

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}agent uses Python identifier agent
    __agent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'agent'), 'agent', '__httpwww_w3_orgnsttml_div_type_httpwww_w3_orgnsttmlmetadataagent', pyxb.binding.datatypes.IDREFS)
    __agent._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 12, 2)
    __agent._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 221, 2)
    
    agent = property(__agent.value, __agent.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'role'), 'role', '__httpwww_w3_orgnsttml_div_type_httpwww_w3_orgnsttmlmetadatarole', pyxb.binding.datatypes.NMTOKENS)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 13, 2)
    __role._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 222, 2)
    
    role = property(__role.value, __role.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __div.name() : __div,
        __p.name() : __p
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __id.name() : __id,
        __region.name() : __region,
        __style.name() : __style,
        __begin.name() : __begin,
        __end.name() : __end,
        __agent.name() : __agent,
        __role.name() : __role
    })
_module_typeBindings.div_type = div_type
Namespace.addCategoryObject('typeBinding', 'div_type', div_type)


# Complex type {http://www.w3.org/ns/ttml}p_type with content type MIXED
class p_type (pyxb.binding.basis.complexTypeDefinition):
    """Logical paragraph."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'p_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 237, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_p_type_httpwww_w3_orgnsttmlmetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 242, 6), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml}br uses Python identifier br
    __br = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'br'), 'br', '__httpwww_w3_orgnsttml_p_type_httpwww_w3_orgnsttmlbr', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 244, 4), )

    
    br = property(__br.value, __br.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml}span uses Python identifier span
    __span = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'span'), 'span', '__httpwww_w3_orgnsttml_p_type_httpwww_w3_orgnsttmlspan', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 245, 4), )

    
    span = property(__span.value, __span.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'id'), 'id', '__httpwww_w3_orgnsttml_p_type_httpwww_w3_orgXML1998namespaceid', pyxb.binding.datatypes.ID, required=True)
    __id._DeclarationLocation = None
    __id._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 248, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_orgnsttml_p_type_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 259, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}space uses Python identifier space
    __space = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'space'), 'space', '__httpwww_w3_orgnsttml_p_type_httpwww_w3_orgXML1998namespacespace', pyxb.binding.xml_.STD_ANON_space)
    __space._DeclarationLocation = None
    __space._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 253, 2)
    
    space = property(__space.value, __space.set, None, None)

    
    # Attribute region uses Python identifier region
    __region = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'region'), 'region', '__httpwww_w3_orgnsttml_p_type_region', pyxb.binding.datatypes.IDREF)
    __region._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 265, 2)
    __region._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 265, 2)
    
    region = property(__region.value, __region.set, None, 'Application of layout information through reference of a\n\t\t\t\t\tregion.')

    
    # Attribute style uses Python identifier style
    __style = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'style'), 'style', '__httpwww_w3_orgnsttml_p_type_style', pyxb.binding.datatypes.IDREFS)
    __style._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 271, 2)
    __style._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 271, 2)
    
    style = property(__style.value, __style.set, None, 'ID(s) of one or more style element(s). The style information shall\n\t\t\t\t\tbe applied to the enclosed content of the tt:p element.')

    
    # Attribute begin uses Python identifier begin
    __begin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'begin'), 'begin', '__httpwww_w3_orgnsttml_p_type_begin', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.timingType)
    __begin._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 277, 2)
    __begin._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 277, 2)
    
    begin = property(__begin.value, __begin.set, None, 'Start point of a temporal interval associated with a tt:p\n\t\t\t\t\telement.')

    
    # Attribute end uses Python identifier end
    __end = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'end'), 'end', '__httpwww_w3_orgnsttml_p_type_end', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.timingType)
    __end._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 283, 2)
    __end._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 283, 2)
    
    end = property(__end.value, __end.set, None, 'End point of a temporal interval associated with a tt:p\n\t\t\t\t\telement.')

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}agent uses Python identifier agent
    __agent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'agent'), 'agent', '__httpwww_w3_orgnsttml_p_type_httpwww_w3_orgnsttmlmetadataagent', pyxb.binding.datatypes.IDREFS)
    __agent._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 12, 2)
    __agent._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 289, 2)
    
    agent = property(__agent.value, __agent.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'role'), 'role', '__httpwww_w3_orgnsttml_p_type_httpwww_w3_orgnsttmlmetadatarole', pyxb.binding.datatypes.NMTOKENS)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 13, 2)
    __role._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 290, 2)
    
    role = property(__role.value, __role.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __br.name() : __br,
        __span.name() : __span
    })
    _AttributeMap.update({
        __id.name() : __id,
        __lang.name() : __lang,
        __space.name() : __space,
        __region.name() : __region,
        __style.name() : __style,
        __begin.name() : __begin,
        __end.name() : __end,
        __agent.name() : __agent,
        __role.name() : __role
    })
_module_typeBindings.p_type = p_type
Namespace.addCategoryObject('typeBinding', 'p_type', p_type)


# Complex type {http://www.w3.org/ns/ttml}span_type with content type MIXED
class span_type (pyxb.binding.basis.complexTypeDefinition):
    """Inline element to allow the application of local style information,
				annotation or metadata."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'span_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 292, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_span_type_httpwww_w3_orgnsttmlmetadata', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 298, 6), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml}br uses Python identifier br
    __br = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'br'), 'br', '__httpwww_w3_orgnsttml_span_type_httpwww_w3_orgnsttmlbr', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 300, 4), )

    
    br = property(__br.value, __br.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml}span uses Python identifier span
    __span = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'span'), 'span', '__httpwww_w3_orgnsttml_span_type_httpwww_w3_orgnsttmlspan', True, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 301, 4), )

    
    span = property(__span.value, __span.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}space uses Python identifier space
    __space = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'space'), 'space', '__httpwww_w3_orgnsttml_span_type_httpwww_w3_orgXML1998namespacespace', pyxb.binding.xml_.STD_ANON_space)
    __space._DeclarationLocation = None
    __space._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 304, 2)
    
    space = property(__space.value, __space.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_orgnsttml_span_type_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 310, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'id'), 'id', '__httpwww_w3_orgnsttml_span_type_httpwww_w3_orgXML1998namespaceid', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = None
    __id._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 316, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute style uses Python identifier style
    __style = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'style'), 'style', '__httpwww_w3_orgnsttml_span_type_style', pyxb.binding.datatypes.IDREFS)
    __style._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 322, 2)
    __style._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 322, 2)
    
    style = property(__style.value, __style.set, None, 'ID(s) of one or more style element(s). The style information shall\n\t\t\t\t\tbe applied to the enclosed content of the tt:span element.')

    
    # Attribute begin uses Python identifier begin
    __begin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'begin'), 'begin', '__httpwww_w3_orgnsttml_span_type_begin', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.timingType)
    __begin._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 328, 2)
    __begin._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 328, 2)
    
    begin = property(__begin.value, __begin.set, None, 'Start point of a temporal interval associated with the\n\t\t\t\t\telement.')

    
    # Attribute end uses Python identifier end
    __end = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'end'), 'end', '__httpwww_w3_orgnsttml_span_type_end', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.timingType)
    __end._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 334, 2)
    __end._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 334, 2)
    
    end = property(__end.value, __end.set, None, 'End point of a temporal interval associated with the\n\t\t\t\t\telement.')

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}agent uses Python identifier agent
    __agent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'agent'), 'agent', '__httpwww_w3_orgnsttml_span_type_httpwww_w3_orgnsttmlmetadataagent', pyxb.binding.datatypes.IDREFS)
    __agent._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 12, 2)
    __agent._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 340, 2)
    
    agent = property(__agent.value, __agent.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'role'), 'role', '__httpwww_w3_orgnsttml_span_type_httpwww_w3_orgnsttmlmetadatarole', pyxb.binding.datatypes.NMTOKENS)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 13, 2)
    __role._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 341, 2)
    
    role = property(__role.value, __role.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __br.name() : __br,
        __span.name() : __span
    })
    _AttributeMap.update({
        __space.name() : __space,
        __lang.name() : __lang,
        __id.name() : __id,
        __style.name() : __style,
        __begin.name() : __begin,
        __end.name() : __end,
        __agent.name() : __agent,
        __role.name() : __role
    })
_module_typeBindings.span_type = span_type
Namespace.addCategoryObject('typeBinding', 'span_type', span_type)


# Complex type {http://www.w3.org/ns/ttml}d_tt_type with content type ELEMENT_ONLY
class d_tt_type (pyxb.binding.basis.complexTypeDefinition):
    """Root element of an EBU-TT-D XML document."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'd_tt_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 298, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}head uses Python identifier head
    __head = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'head'), 'head', '__httpwww_w3_orgnsttml_d_tt_type_httpwww_w3_orgnsttmlhead', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 303, 3), )

    
    head = property(__head.value, __head.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml}body uses Python identifier body
    __body = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'body'), 'body', '__httpwww_w3_orgnsttml_d_tt_type_httpwww_w3_orgnsttmlbody', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 304, 3), )

    
    body = property(__body.value, __body.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}space uses Python identifier space
    __space = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'space'), 'space', '__httpwww_w3_orgnsttml_d_tt_type_httpwww_w3_orgXML1998namespacespace', pyxb.binding.xml_.STD_ANON_space)
    __space._DeclarationLocation = None
    __space._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 306, 2)
    
    space = property(__space.value, __space.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_orgnsttml_d_tt_type_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang, required=True)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 314, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#parameter}timeBase uses Python identifier timeBase
    __timeBase = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttp, 'timeBase'), 'timeBase', '__httpwww_w3_orgnsttml_d_tt_type_httpwww_w3_orgnsttmlparametertimeBase', _ImportedBinding_ebu_tt_live_bindings__ttp.timeBaseType, required=True)
    __timeBase._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 27, 1)
    __timeBase._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 312, 2)
    
    timeBase = property(__timeBase.value, __timeBase.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#parameter}cellResolution uses Python identifier cellResolution
    __cellResolution = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttp, 'cellResolution'), 'cellResolution', '__httpwww_w3_orgnsttml_d_tt_type_httpwww_w3_orgnsttmlparametercellResolution', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.cellResolutionType, unicode_default='32 15')
    __cellResolution._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 82, 1)
    __cellResolution._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 313, 2)
    
    cellResolution = property(__cellResolution.value, __cellResolution.set, None, 'Expresses a virtual visual grid composed of horizontal and vertical\n\t\t\t\tcells. This virtual grid shall divide the active video in rows and\n\t\t\t\tcolumns.')

    
    # Attribute {http://www.w3.org/ns/ttml/profile/imsc1#parameter}activeArea uses Python identifier activeArea
    __activeArea = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ittp, 'activeArea'), 'activeArea', '__httpwww_w3_orgnsttml_d_tt_type_httpwww_w3_orgnsttmlprofileimsc1parameteractiveArea', _ImportedBinding_ebu_tt_live_bindings__ittp.STD_ANON_2)
    __activeArea._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/imsc1-parameters.xsd', 4, 4)
    __activeArea._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 320, 2)
    
    activeArea = property(__activeArea.value, __activeArea.set, None, 'Area within the Root Container Region that \n                the author intends to be minimally visible to the viewer.')

    _ElementMap.update({
        __head.name() : __head,
        __body.name() : __body
    })
    _AttributeMap.update({
        __space.name() : __space,
        __lang.name() : __lang,
        __timeBase.name() : __timeBase,
        __cellResolution.name() : __cellResolution,
        __activeArea.name() : __activeArea
    })
_module_typeBindings.d_tt_type = d_tt_type
Namespace.addCategoryObject('typeBinding', 'd_tt_type', d_tt_type)


# Complex type {http://www.w3.org/ns/ttml}tt_type with content type ELEMENT_ONLY
class tt_type (pyxb.binding.basis.complexTypeDefinition):
    """Root element of an EBU-TT XML document."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tt_type')
    _XSDLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 353, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/ns/ttml}head uses Python identifier head
    __head = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'head'), 'head', '__httpwww_w3_orgnsttml_tt_type_httpwww_w3_orgnsttmlhead', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 358, 3), )

    
    head = property(__head.value, __head.set, None, None)

    
    # Element {http://www.w3.org/ns/ttml}body uses Python identifier body
    __body = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'body'), 'body', '__httpwww_w3_orgnsttml_tt_type_httpwww_w3_orgnsttmlbody', False, pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 359, 3), )

    
    body = property(__body.value, __body.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}space uses Python identifier space
    __space = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'space'), 'space', '__httpwww_w3_orgnsttml_tt_type_httpwww_w3_orgXML1998namespacespace', pyxb.binding.xml_.STD_ANON_space)
    __space._DeclarationLocation = None
    __space._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 361, 2)
    
    space = property(__space.value, __space.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_orgnsttml_tt_type_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang, required=True)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 388, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {urn:ebu:tt:metadata}authoringDelay uses Python identifier authoringDelay
    __authoringDelay = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ebuttm, 'authoringDelay'), 'authoringDelay', '__httpwww_w3_orgnsttml_tt_type_urnebuttmetadataauthoringDelay', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.authoringDelayType)
    __authoringDelay._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 510, 1)
    __authoringDelay._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 376, 2)
    
    authoringDelay = property(__authoringDelay.value, __authoringDelay.set, None, '\n\t\t\t\tThe authoring delay associated with the timed content within this document may be indicated using the ebuttm:authoringDelay attribute.\n\t\t\t\tNOTE: This delay may be estimated or measured, and is intended to represent the duration between when the subitle authoring tool\n\t\t\t\treceived the instantaneous media for which subtitles were authored and the moment that the authoring tool emitted those subtitles.\n\t\t\t')

    
    # Attribute {urn:ebu:tt:metadata}authorsGroupSelectedSequenceIdentifier uses Python identifier authorsGroupSelectedSequenceIdentifier
    __authorsGroupSelectedSequenceIdentifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ebuttm, 'authorsGroupSelectedSequenceIdentifier'), 'authorsGroupSelectedSequenceIdentifier', '__httpwww_w3_orgnsttml_tt_type_urnebuttmetadataauthorsGroupSelectedSequenceIdentifier', _ImportedBinding_ebu_tt_live_bindings__ebuttm.STD_ANON_6)
    __authorsGroupSelectedSequenceIdentifier._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 520, 1)
    __authorsGroupSelectedSequenceIdentifier._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 379, 2)
    
    authorsGroupSelectedSequenceIdentifier = property(__authorsGroupSelectedSequenceIdentifier.value, __authorsGroupSelectedSequenceIdentifier.set, None, '\n\t\t\t\tThe selected sequenceIdentifier is to be moved here by the handover node.\n\t\t\t')

    
    # Attribute {http://www.w3.org/ns/ttml#parameter}timeBase uses Python identifier timeBase
    __timeBase = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttp, 'timeBase'), 'timeBase', '__httpwww_w3_orgnsttml_tt_type_httpwww_w3_orgnsttmlparametertimeBase', _ImportedBinding_ebu_tt_live_bindings__ttp.timeBaseType, required=True)
    __timeBase._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 27, 1)
    __timeBase._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 367, 2)
    
    timeBase = property(__timeBase.value, __timeBase.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#parameter}dropMode uses Python identifier dropMode
    __dropMode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttp, 'dropMode'), 'dropMode', '__httpwww_w3_orgnsttml_tt_type_httpwww_w3_orgnsttmlparameterdropMode', _ImportedBinding_ebu_tt_live_bindings__ttp.STD_ANON)
    __dropMode._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 28, 1)
    __dropMode._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 371, 2)
    
    dropMode = property(__dropMode.value, __dropMode.set, None, 'The attribute specifies constraints on the interpretation and use of\n\t\t\t\tframe counts that correspond with time expressions of type ebuttdt:smpteTimingType.\n\t\t\t\tThe attribute shall be specified when the value of the ttp:timebase attribute is\n\t\t\t\t"smpte".')

    
    # Attribute {http://www.w3.org/ns/ttml#parameter}clockMode uses Python identifier clockMode
    __clockMode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttp, 'clockMode'), 'clockMode', '__httpwww_w3_orgnsttml_tt_type_httpwww_w3_orgnsttmlparameterclockMode', _ImportedBinding_ebu_tt_live_bindings__ttp.STD_ANON_)
    __clockMode._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 43, 1)
    __clockMode._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 372, 2)
    
    clockMode = property(__clockMode.value, __clockMode.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#parameter}frameRate uses Python identifier frameRate
    __frameRate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttp, 'frameRate'), 'frameRate', '__httpwww_w3_orgnsttml_tt_type_httpwww_w3_orgnsttmlparameterframeRate', _ImportedBinding_ebu_tt_live_bindings__ttp.STD_ANON_2)
    __frameRate._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 52, 1)
    __frameRate._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 368, 2)
    
    frameRate = property(__frameRate.value, __frameRate.set, None, 'The frame rate used to interpret time expressions of type\n\t\t\t\tebuttdt:smpteTimingType')

    
    # Attribute {http://www.w3.org/ns/ttml#parameter}frameRateMultiplier uses Python identifier frameRateMultiplier
    __frameRateMultiplier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttp, 'frameRateMultiplier'), 'frameRateMultiplier', '__httpwww_w3_orgnsttml_tt_type_httpwww_w3_orgnsttmlparameterframeRateMultiplier', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.frameRateMultiplierType)
    __frameRateMultiplier._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 61, 1)
    __frameRateMultiplier._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 369, 2)
    
    frameRateMultiplier = property(__frameRateMultiplier.value, __frameRateMultiplier.set, None, 'Multiplier that shall be applied to the frame rate specified by a\n\t\t\t\tttp:frameRate attribute in order to compute the effective frame\n\t\t\t\trate.')

    
    # Attribute {http://www.w3.org/ns/ttml#parameter}markerMode uses Python identifier markerMode
    __markerMode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttp, 'markerMode'), 'markerMode', '__httpwww_w3_orgnsttml_tt_type_httpwww_w3_orgnsttmlparametermarkerMode', _ImportedBinding_ebu_tt_live_bindings__ttp.STD_ANON_3)
    __markerMode._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 68, 1)
    __markerMode._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 370, 2)
    
    markerMode = property(__markerMode.value, __markerMode.set, None, 'If the timebase is “smpte” ttp:markerMode shall be specified.\n\t\t\t\tThe value “discontinuous” implies that because of the marker mode of operation no assumption\n\t\t\t\tmay be made regarding linearity or monotonicity of time coordinates. The value "continuous" implies\n\t\t\t\tthat we assume linearity and monotonicity of time coordinates.')

    
    # Attribute {http://www.w3.org/ns/ttml#parameter}cellResolution uses Python identifier cellResolution
    __cellResolution = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttp, 'cellResolution'), 'cellResolution', '__httpwww_w3_orgnsttml_tt_type_httpwww_w3_orgnsttmlparametercellResolution', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.cellResolutionType, unicode_default='32 15')
    __cellResolution._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 82, 1)
    __cellResolution._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 373, 2)
    
    cellResolution = property(__cellResolution.value, __cellResolution.set, None, 'Expresses a virtual visual grid composed of horizontal and vertical\n\t\t\t\tcells. This virtual grid shall divide the active video in rows and\n\t\t\t\tcolumns.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}extent uses Python identifier extent
    __extent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'extent'), 'extent', '__httpwww_w3_orgnsttml_tt_type_httpwww_w3_orgnsttmlstylingextent', _ImportedBinding_ebu_tt_live_bindings__ebuttdt.extentType)
    __extent._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 172, 1)
    __extent._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 381, 2)
    
    extent = property(__extent.value, __extent.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml/profile/imsc1#parameter}activeArea uses Python identifier activeArea
    __activeArea = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ittp, 'activeArea'), 'activeArea', '__httpwww_w3_orgnsttml_tt_type_httpwww_w3_orgnsttmlprofileimsc1parameteractiveArea', _ImportedBinding_ebu_tt_live_bindings__ittp.STD_ANON_2)
    __activeArea._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/imsc1-parameters.xsd', 4, 4)
    __activeArea._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 394, 2)
    
    activeArea = property(__activeArea.value, __activeArea.set, None, 'Area within the Root Container Region that \n                the author intends to be minimally visible to the viewer.')

    
    # Attribute {urn:ebu:tt:parameters}sequenceIdentifier uses Python identifier sequenceIdentifier
    __sequenceIdentifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ebuttp, 'sequenceIdentifier'), 'sequenceIdentifier', '__httpwww_w3_orgnsttml_tt_type_urnebuttparameterssequenceIdentifier', _ImportedBinding_ebu_tt_live_bindings__ebuttp.STD_ANON)
    __sequenceIdentifier._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_parameters.xsd', 17, 4)
    __sequenceIdentifier._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 374, 2)
    
    sequenceIdentifier = property(__sequenceIdentifier.value, __sequenceIdentifier.set, None, 'Every document with the same ebuttp:sequenceIdentifier\n                shall be uniquely numbered using the ebuttp:sequenceNumber attribute.')

    
    # Attribute {urn:ebu:tt:parameters}sequenceNumber uses Python identifier sequenceNumber
    __sequenceNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ebuttp, 'sequenceNumber'), 'sequenceNumber', '__httpwww_w3_orgnsttml_tt_type_urnebuttparameterssequenceNumber', _ImportedBinding_ebu_tt_live_bindings__ebuttp.STD_ANON_)
    __sequenceNumber._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_parameters.xsd', 29, 4)
    __sequenceNumber._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 375, 2)
    
    sequenceNumber = property(__sequenceNumber.value, __sequenceNumber.set, None, 'Every document with the same ebuttp:sequenceIdentifier\n                shall be uniquely numbered using the ebuttp:sequenceNumber attribute.')

    
    # Attribute {urn:ebu:tt:parameters}authorsGroupIdentifier uses Python identifier authorsGroupIdentifier
    __authorsGroupIdentifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ebuttp, 'authorsGroupIdentifier'), 'authorsGroupIdentifier', '__httpwww_w3_orgnsttml_tt_type_urnebuttparametersauthorsGroupIdentifier', _ImportedBinding_ebu_tt_live_bindings__ebuttp.STD_ANON_2)
    __authorsGroupIdentifier._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_parameters.xsd', 39, 4)
    __authorsGroupIdentifier._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 377, 2)
    
    authorsGroupIdentifier = property(__authorsGroupIdentifier.value, __authorsGroupIdentifier.set, None, '\n                Identifies the group of authors whose sequences relate to the same content and amongst which a Handover Manager\n                should select documents when generating its output sequence.\n            ')

    
    # Attribute {urn:ebu:tt:parameters}authorsGroupControlToken uses Python identifier authorsGroupControlToken
    __authorsGroupControlToken = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ebuttp, 'authorsGroupControlToken'), 'authorsGroupControlToken', '__httpwww_w3_orgnsttml_tt_type_urnebuttparametersauthorsGroupControlToken', pyxb.binding.datatypes.positiveInteger)
    __authorsGroupControlToken._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_parameters.xsd', 53, 4)
    __authorsGroupControlToken._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 378, 2)
    
    authorsGroupControlToken = property(__authorsGroupControlToken.value, __authorsGroupControlToken.set, None, '\n                The control token used to direct a Handover Manager to select an input sequence from a particular authors group.\n                The input sequence whose document has the greatest ebuttp:authorsGroupControlToken value is selected for output.\n            ')

    
    # Attribute {urn:ebu:tt:parameters}referenceClockIdentifier uses Python identifier referenceClockIdentifier
    __referenceClockIdentifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ebuttp, 'referenceClockIdentifier'), 'referenceClockIdentifier', '__httpwww_w3_orgnsttml_tt_type_urnebuttparametersreferenceClockIdentifier', pyxb.binding.datatypes.anyURI)
    __referenceClockIdentifier._DeclarationLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_parameters.xsd', 62, 4)
    __referenceClockIdentifier._UseLocation = pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 380, 2)
    
    referenceClockIdentifier = property(__referenceClockIdentifier.value, __referenceClockIdentifier.set, None, '\n                Allows the reference clock source to be identified. Permitted only when ttp:timebase="clock" AND ttp:clockMode="local"\n                OR when ttp:timeBase="smpte".\n            ')

    _ElementMap.update({
        __head.name() : __head,
        __body.name() : __body
    })
    _AttributeMap.update({
        __space.name() : __space,
        __lang.name() : __lang,
        __authoringDelay.name() : __authoringDelay,
        __authorsGroupSelectedSequenceIdentifier.name() : __authorsGroupSelectedSequenceIdentifier,
        __timeBase.name() : __timeBase,
        __dropMode.name() : __dropMode,
        __clockMode.name() : __clockMode,
        __frameRate.name() : __frameRate,
        __frameRateMultiplier.name() : __frameRateMultiplier,
        __markerMode.name() : __markerMode,
        __cellResolution.name() : __cellResolution,
        __extent.name() : __extent,
        __activeArea.name() : __activeArea,
        __sequenceIdentifier.name() : __sequenceIdentifier,
        __sequenceNumber.name() : __sequenceNumber,
        __authorsGroupIdentifier.name() : __authorsGroupIdentifier,
        __authorsGroupControlToken.name() : __authorsGroupControlToken,
        __referenceClockIdentifier.name() : __referenceClockIdentifier
    })
_module_typeBindings.tt_type = tt_type
Namespace.addCategoryObject('typeBinding', 'tt_type', tt_type)


ttd = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ttd'), d_tt_type, documentation='This element is deliberately misnamed (should be "tt") to disambiguate\n\t\t\t\trelative to the EBU-TT Part 3 element of the same name, so that the bound classes\n\t\t\t\tcan be distinguished by the bindings generator. This XSD is not intended for\n\t\t\t\tstandalone use outside the EBU-TT Live Interoperability Toolkit\'s EBU-TT-D Encoder.', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 322, 1))
Namespace.addCategoryObject('elementBinding', ttd.name().localName(), ttd)

tt = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tt'), tt_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 396, 1))
Namespace.addCategoryObject('elementBinding', tt.name().localName(), tt)



d_head_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), _ImportedBinding_ebu_tt_live_bindings__ebuttm.headMetadata_type, scope=d_head_type, documentation='Generic container for metadata information that applies to\n\t\t\t\t\t\tthe whole document.', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 30, 3)))

d_head_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'styling'), d_styling_type, scope=d_head_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 36, 3)))

d_head_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'layout'), d_layout_type, scope=d_head_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 37, 3)))

d_head_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ttm, 'copyright'), pyxb.binding.datatypes.string, scope=d_head_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 68, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 29, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 30, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(d_head_type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ttm, 'copyright')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 29, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(d_head_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 30, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(d_head_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'styling')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 36, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(d_head_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'layout')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 37, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
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
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
d_head_type._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 47, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/ns/ttml')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 47, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
d_metadata_type._Automaton = _BuildAutomaton_()




d_styling_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), d_metadata_type, scope=d_styling_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 57, 3)))

d_styling_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'style'), d_style_type, scope=d_styling_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 58, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 57, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(d_styling_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 57, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(d_styling_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'style')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 58, 3))
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
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
d_styling_type._Automaton = _BuildAutomaton_2()




d_layout_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), d_metadata_type, scope=d_layout_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 95, 3)))

d_layout_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'region'), d_region_type, scope=d_layout_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 96, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 95, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(d_layout_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 95, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(d_layout_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'region')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 96, 3))
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
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
d_layout_type._Automaton = _BuildAutomaton_3()




d_body_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), d_metadata_type, scope=d_body_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 142, 3)))

d_body_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'div'), d_div_type, scope=d_body_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 143, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 142, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(d_body_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 142, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(d_body_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'div')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 143, 3))
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
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
d_body_type._Automaton = _BuildAutomaton_4()




d_div_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), d_metadata_type, scope=d_div_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 154, 3)))

d_div_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'p'), d_p_type, scope=d_div_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 156, 4)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 154, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(d_div_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 154, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(d_div_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'p')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 156, 4))
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
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
d_div_type._Automaton = _BuildAutomaton_5()




d_br_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), d_metadata_type, scope=d_br_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 294, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 294, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(d_br_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 294, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
d_br_type._Automaton = _BuildAutomaton_6()




head_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), _ImportedBinding_ebu_tt_live_bindings__ebuttm.headMetadata_type, scope=head_type, documentation='Generic container for metadata information that applies to the\n\t\t\t\t\t\twhole document.', location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 36, 6)))

head_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'styling'), styling, scope=head_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 43, 3)))

head_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'layout'), layout, scope=head_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 44, 3)))

head_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ttm, 'copyright'), pyxb.binding.datatypes.string, scope=head_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 68, 2)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 36, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 42, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 43, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 44, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(head_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 36, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(head_type._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ttm, 'copyright')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 42, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(head_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'styling')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 43, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(head_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'layout')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 44, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
head_type._Automaton = _BuildAutomaton_7()




styling._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), _ImportedBinding_ebu_tt_live_bindings__ebuttm.stylingMetadata_type, scope=styling, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 52, 6)))

styling._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'style'), style, scope=styling, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 53, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 52, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(styling._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 52, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(styling._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'style')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 53, 3))
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
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
styling._Automaton = _BuildAutomaton_8()




layout._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), _ImportedBinding_ebu_tt_live_bindings__ebuttm.anyMetadata_type, scope=layout, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 106, 6)))

layout._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'region'), region, scope=layout, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 107, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 106, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(layout._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 106, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(layout._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'region')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 107, 3))
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
         ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
layout._Automaton = _BuildAutomaton_9()




br_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), _ImportedBinding_ebu_tt_live_bindings__ebuttm.anyMetadata_type, scope=br_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 349, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 349, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(br_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 349, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
br_type._Automaton = _BuildAutomaton_10()




d_style_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), d_metadata_type, scope=d_style_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 66, 3)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 66, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(d_style_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 66, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
d_style_type._Automaton = _BuildAutomaton_11()




d_region_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), d_metadata_type, scope=d_region_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 105, 4)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 105, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(d_region_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 105, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
d_region_type._Automaton = _BuildAutomaton_12()




d_p_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), d_metadata_type, scope=d_p_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 187, 3)))

d_p_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'br'), d_br_type, scope=d_p_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 189, 4)))

d_p_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'span'), d_span_type, scope=d_p_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 190, 4)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 187, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 188, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(d_p_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 187, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(d_p_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'br')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 189, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(d_p_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'span')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 190, 4))
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
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
d_p_type._Automaton = _BuildAutomaton_13()




d_span_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), d_metadata_type, scope=d_span_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 244, 3)))

d_span_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'br'), d_br_type, scope=d_span_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 246, 4)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 244, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 245, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(d_span_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 244, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(d_span_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'br')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 246, 4))
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
d_span_type._Automaton = _BuildAutomaton_14()




style._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), _ImportedBinding_ebu_tt_live_bindings__ebuttm.anyMetadata_type, scope=style, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 62, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 62, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(style._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 62, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
style._Automaton = _BuildAutomaton_15()




region._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), _ImportedBinding_ebu_tt_live_bindings__ebuttm.anyMetadata_type, scope=region, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 117, 6)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 117, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(region._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 117, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
region._Automaton = _BuildAutomaton_16()




body_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), _ImportedBinding_ebu_tt_live_bindings__ebuttm.bodyMetadata_type, scope=body_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 155, 6)))

body_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'div'), div_type, scope=body_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 156, 3)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 155, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 156, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(body_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 155, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(body_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'div')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 156, 3))
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
body_type._Automaton = _BuildAutomaton_17()




div_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), _ImportedBinding_ebu_tt_live_bindings__ebuttm.divMetadata_type, scope=div_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 191, 6)))

div_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'div'), div_type, scope=div_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 193, 4)))

div_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'p'), p_type, scope=div_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 194, 4)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 191, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 192, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(div_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 191, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(div_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'div')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 193, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(div_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'p')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 194, 4))
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
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
div_type._Automaton = _BuildAutomaton_18()




p_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), _ImportedBinding_ebu_tt_live_bindings__ebuttm.pMetadata_type, scope=p_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 242, 6)))

p_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'br'), br_type, scope=p_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 244, 4)))

p_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'span'), span_type, scope=p_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 245, 4)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 242, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 243, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(p_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 242, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(p_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'br')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 244, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(p_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'span')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 245, 4))
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
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
p_type._Automaton = _BuildAutomaton_19()




span_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'metadata'), _ImportedBinding_ebu_tt_live_bindings__ebuttm.spanMetadata_type, scope=span_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 298, 6)))

span_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'br'), br_type, scope=span_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 300, 4)))

span_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'span'), span_type, scope=span_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 301, 4)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 298, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 299, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(span_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'metadata')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 298, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(span_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'br')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 300, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(span_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'span')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 301, 4))
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
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
span_type._Automaton = _BuildAutomaton_20()




d_tt_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'head'), d_head_type, scope=d_tt_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 303, 3)))

d_tt_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'body'), d_body_type, scope=d_tt_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 304, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 304, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(d_tt_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'head')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 303, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(d_tt_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'body')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_d.xsd', 304, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
d_tt_type._Automaton = _BuildAutomaton_21()




tt_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'head'), head_type, scope=tt_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 358, 3)))

tt_type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'body'), body_type, scope=tt_type, location=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 359, 3)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 359, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(tt_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'head')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 358, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tt_type._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'body')), pyxb.utils.utility.Location('/Users/cablej01/Projects/dazzler/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 359, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
tt_type._Automaton = _BuildAutomaton_22()

