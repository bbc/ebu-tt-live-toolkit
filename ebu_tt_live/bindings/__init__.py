# ./ebu_tt_live/bindings/__init__.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e3bbecc10c61338063ee2c070f5c7ba59a7cf71e
# Generated 2016-04-08 12:13:18.851907 by PyXB version 1.2.4 using Python 2.7.9.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:e5be8dbd-fd7a-11e5-adc0-6c40089ad95e')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import _ebuttdt as _ImportedBinding__ebuttdt
import pyxb.binding.xml_
import _ttp as _ImportedBinding__ttp
import _tts as _ImportedBinding__tts
import pyxb.binding.datatypes
import _ebutts as _ImportedBinding__ebutts
import _ttm as _ImportedBinding__ttm

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.w3.org/ns/ttml', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ttm = _ImportedBinding__ttm.Namespace
_Namespace_ttm.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ttp = _ImportedBinding__ttp.Namespace
_Namespace_ttp.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_tts = _ImportedBinding__tts.Namespace
_Namespace_tts.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ebutts = _ImportedBinding__ebutts.Namespace
_Namespace_ebutts.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type {http://www.w3.org/ns/ttml}Head with content type ELEMENT_ONLY
class Head (pyxb.binding.basis.complexTypeDefinition):
    """Contains metadata as well as layout and styling information that are
				referenced by the subtitle blocks in the body."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Head')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 55, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_Head_metadata', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 61, 3), )

    
    metadata = property(__metadata.value, __metadata.set, None, 'Generic container for metadata information that applies to the\n\t\t\t\t\t\twhole document.')

    
    # Element styling uses Python identifier styling
    __styling = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'styling'), 'styling', '__httpwww_w3_orgnsttml_Head_styling', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 67, 3), )

    
    styling = property(__styling.value, __styling.set, None, None)

    
    # Element layout uses Python identifier layout
    __layout = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'layout'), 'layout', '__httpwww_w3_orgnsttml_Head_layout', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 68, 3), )

    
    layout = property(__layout.value, __layout.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __styling.name() : __styling,
        __layout.name() : __layout
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Head', Head)


# Complex type {http://www.w3.org/ns/ttml}Metadata with content type ELEMENT_ONLY
class Metadata (pyxb.binding.basis.complexTypeDefinition):
    """Container for metadata information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Metadata')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 72, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Metadata', Metadata)


# Complex type {http://www.w3.org/ns/ttml}Styling with content type ELEMENT_ONLY
class Styling (pyxb.binding.basis.complexTypeDefinition):
    """Container for styling information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Styling')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 81, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_Styling_metadata', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 86, 3), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element style uses Python identifier style
    __style = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'style'), 'style', '__httpwww_w3_orgnsttml_Styling_style', True, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 87, 3), )

    
    style = property(__style.value, __style.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __style.name() : __style
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Styling', Styling)


# Complex type {http://www.w3.org/ns/ttml}Layout with content type ELEMENT_ONLY
class Layout (pyxb.binding.basis.complexTypeDefinition):
    """Container element for layout information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Layout')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 133, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_Layout_metadata', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 138, 3), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element region uses Python identifier region
    __region = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'region'), 'region', '__httpwww_w3_orgnsttml_Layout_region', True, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 139, 3), )

    
    region = property(__region.value, __region.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __region.name() : __region
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'Layout', Layout)


# Complex type {http://www.w3.org/ns/ttml}Body with content type ELEMENT_ONLY
class Body (pyxb.binding.basis.complexTypeDefinition):
    """Container of the subtitle and the timing
				information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Body')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 180, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_Body_metadata', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 186, 3), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element div uses Python identifier div
    __div = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'div'), 'div', '__httpwww_w3_orgnsttml_Body_div', True, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 187, 3), )

    
    div = property(__div.value, __div.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}agent uses Python identifier agent
    __agent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'agent'), 'agent', '__httpwww_w3_orgnsttml_Body_httpwww_w3_orgnsttmlmetadataagent', pyxb.binding.datatypes.IDREFS)
    __agent._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 10, 1)
    __agent._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 189, 2)
    
    agent = property(__agent.value, __agent.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'role'), 'role', '__httpwww_w3_orgnsttml_Body_httpwww_w3_orgnsttmlmetadatarole', pyxb.binding.datatypes.NMTOKENS)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 11, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 190, 2)
    
    role = property(__role.value, __role.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __div.name() : __div
    })
    _AttributeMap.update({
        __agent.name() : __agent,
        __role.name() : __role
    })
Namespace.addCategoryObject('typeBinding', 'Body', Body)


# Complex type {http://www.w3.org/ns/ttml}Div with content type ELEMENT_ONLY
class Div (pyxb.binding.basis.complexTypeDefinition):
    """Logical container of textual content."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Div')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 194, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_Div_metadata', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 199, 3), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element div uses Python identifier div
    __div = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'div'), 'div', '__httpwww_w3_orgnsttml_Div_div', True, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 201, 4), )

    
    div = property(__div.value, __div.set, None, None)

    
    # Element p uses Python identifier p
    __p = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'p'), 'p', '__httpwww_w3_orgnsttml_Div_p', True, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 202, 4), )

    
    p = property(__p.value, __p.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'id'), 'id', '__httpwww_w3_orgnsttml_Div_httpwww_w3_orgXML1998namespaceid', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = None
    __id._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 205, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute region uses Python identifier region
    __region = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'region'), 'region', '__httpwww_w3_orgnsttml_Div_region', pyxb.binding.datatypes.IDREF)
    __region._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 211, 2)
    __region._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 211, 2)
    
    region = property(__region.value, __region.set, None, 'Application of layout and style information through reference of a\n\t\t\t\t\tregion.')

    
    # Attribute style uses Python identifier style
    __style = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'style'), 'style', '__httpwww_w3_orgnsttml_Div_style', pyxb.binding.datatypes.IDREFS)
    __style._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 217, 2)
    __style._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 217, 2)
    
    style = property(__style.value, __style.set, None, 'ID(s) of one or more style element(s). The style information shall\n\t\t\t\t\tbe applied to the enclosed content of the tt:div element.')

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}agent uses Python identifier agent
    __agent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'agent'), 'agent', '__httpwww_w3_orgnsttml_Div_httpwww_w3_orgnsttmlmetadataagent', pyxb.binding.datatypes.IDREFS)
    __agent._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 10, 1)
    __agent._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 223, 2)
    
    agent = property(__agent.value, __agent.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'role'), 'role', '__httpwww_w3_orgnsttml_Div_httpwww_w3_orgnsttmlmetadatarole', pyxb.binding.datatypes.NMTOKENS)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 11, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 224, 2)
    
    role = property(__role.value, __role.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __div.name() : __div,
        __p.name() : __p
    })
    _AttributeMap.update({
        __id.name() : __id,
        __region.name() : __region,
        __style.name() : __style,
        __agent.name() : __agent,
        __role.name() : __role
    })
Namespace.addCategoryObject('typeBinding', 'Div', Div)


# Complex type {http://www.w3.org/ns/ttml}Br with content type ELEMENT_ONLY
class Br (pyxb.binding.basis.complexTypeDefinition):
    """Forced line break."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Br')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 335, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_Br_metadata', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 340, 3), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'role'), 'role', '__httpwww_w3_orgnsttml_Br_httpwww_w3_orgnsttmlmetadatarole', pyxb.binding.datatypes.NMTOKENS)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 11, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 342, 2)
    
    role = property(__role.value, __role.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata
    })
    _AttributeMap.update({
        __role.name() : __role
    })
Namespace.addCategoryObject('typeBinding', 'Br', Br)


# Complex type {http://www.w3.org/ns/ttml}Tt with content type ELEMENT_ONLY
class Tt (pyxb.binding.basis.complexTypeDefinition):
    """Root element of an EBU-TT XML document."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Tt')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 19, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element head uses Python identifier head
    __head = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'head'), 'head', '__httpwww_w3_orgnsttml_Tt_head', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 24, 3), )

    
    head = property(__head.value, __head.set, None, None)

    
    # Element body uses Python identifier body
    __body = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'body'), 'body', '__httpwww_w3_orgnsttml_Tt_body', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 25, 3), )

    
    body = property(__body.value, __body.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_orgnsttml_Tt_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang, required=True)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 47, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}space uses Python identifier space
    __space = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'space'), 'space', '__httpwww_w3_orgnsttml_Tt_httpwww_w3_orgXML1998namespacespace', pyxb.binding.xml_.STD_ANON_space)
    __space._DeclarationLocation = None
    __space._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 27, 2)
    
    space = property(__space.value, __space.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#parameter}timeBase uses Python identifier timeBase
    __timeBase = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttp, 'timeBase'), 'timeBase', '__httpwww_w3_orgnsttml_Tt_httpwww_w3_orgnsttmlparametertimeBase', _ImportedBinding__ttp.STD_ANON, required=True)
    __timeBase._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 11, 1)
    __timeBase._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 33, 2)
    
    timeBase = property(__timeBase.value, __timeBase.set, None, 'The timebase defines the time coordinate system for all time\n\t\t\t\texpressions in EBU-TT.')

    
    # Attribute {http://www.w3.org/ns/ttml#parameter}dropMode uses Python identifier dropMode
    __dropMode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttp, 'dropMode'), 'dropMode', '__httpwww_w3_orgnsttml_Tt_httpwww_w3_orgnsttmlparameterdropMode', _ImportedBinding__ttp.STD_ANON_)
    __dropMode._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 24, 1)
    __dropMode._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 37, 2)
    
    dropMode = property(__dropMode.value, __dropMode.set, None, 'The attribute specifies constraints on the interpretation and use of\n\t\t\t\tframe counts that correspond with time expressions of type ebuttdt:smpteTimingType.\n\t\t\t\tThe attribute shall be specified when the value of the ttp:timebase attribute is\n\t\t\t\t"smpte".')

    
    # Attribute {http://www.w3.org/ns/ttml#parameter}clockMode uses Python identifier clockMode
    __clockMode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttp, 'clockMode'), 'clockMode', '__httpwww_w3_orgnsttml_Tt_httpwww_w3_orgnsttmlparameterclockMode', _ImportedBinding__ttp.STD_ANON_2)
    __clockMode._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 39, 1)
    __clockMode._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 38, 2)
    
    clockMode = property(__clockMode.value, __clockMode.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#parameter}frameRate uses Python identifier frameRate
    __frameRate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttp, 'frameRate'), 'frameRate', '__httpwww_w3_orgnsttml_Tt_httpwww_w3_orgnsttmlparameterframeRate', _ImportedBinding__ttp.STD_ANON_3)
    __frameRate._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 48, 1)
    __frameRate._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 34, 2)
    
    frameRate = property(__frameRate.value, __frameRate.set, None, 'The frame rate used to interpret time expressions of type\n\t\t\t\tebuttdt:smpteTimingType')

    
    # Attribute {http://www.w3.org/ns/ttml#parameter}frameRateMultiplier uses Python identifier frameRateMultiplier
    __frameRateMultiplier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttp, 'frameRateMultiplier'), 'frameRateMultiplier', '__httpwww_w3_orgnsttml_Tt_httpwww_w3_orgnsttmlparameterframeRateMultiplier', _ImportedBinding__ebuttdt.frameRateMultiplierType)
    __frameRateMultiplier._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 57, 1)
    __frameRateMultiplier._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 35, 2)
    
    frameRateMultiplier = property(__frameRateMultiplier.value, __frameRateMultiplier.set, None, 'Multiplier that shall be applied to the frame rate specified by a\n\t\t\t\tttp:frameRate attribute in order to compute the effective frame\n\t\t\t\trate.')

    
    # Attribute {http://www.w3.org/ns/ttml#parameter}markerMode uses Python identifier markerMode
    __markerMode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttp, 'markerMode'), 'markerMode', '__httpwww_w3_orgnsttml_Tt_httpwww_w3_orgnsttmlparametermarkerMode', _ImportedBinding__ttp.STD_ANON_4)
    __markerMode._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 64, 1)
    __markerMode._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 36, 2)
    
    markerMode = property(__markerMode.value, __markerMode.set, None, 'If the timebase is \u201csmpte\u201d ttp:markerMode shall be specified and shall\n\t\t\t\thave the value \u201cdiscontinuous\u201d. The value \u201cdiscontinuous\u201d implies that because of\n\t\t\t\tthe marker mode of operation no assumption may be made regarding linearity or\n\t\t\t\tmonotonicity of time coordinates.')

    
    # Attribute {http://www.w3.org/ns/ttml#parameter}cellResolution uses Python identifier cellResolution
    __cellResolution = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttp, 'cellResolution'), 'cellResolution', '__httpwww_w3_orgnsttml_Tt_httpwww_w3_orgnsttmlparametercellResolution', _ImportedBinding__ebuttdt.cellResolutionType)
    __cellResolution._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/parameter.xsd', 77, 1)
    __cellResolution._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 39, 2)
    
    cellResolution = property(__cellResolution.value, __cellResolution.set, None, 'Expresses a virtual visual grid composed of horizontal and vertical\n\t\t\t\tcells. This virtual grid shall divide the active video in rows and\n\t\t\t\tcolumns.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}extent uses Python identifier extent
    __extent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'extent'), 'extent', '__httpwww_w3_orgnsttml_Tt_httpwww_w3_orgnsttmlstylingextent', _ImportedBinding__ebuttdt.extentType)
    __extent._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 172, 1)
    __extent._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 40, 2)
    
    extent = property(__extent.value, __extent.set, None, None)

    _ElementMap.update({
        __head.name() : __head,
        __body.name() : __body
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __space.name() : __space,
        __timeBase.name() : __timeBase,
        __dropMode.name() : __dropMode,
        __clockMode.name() : __clockMode,
        __frameRate.name() : __frameRate,
        __frameRateMultiplier.name() : __frameRateMultiplier,
        __markerMode.name() : __markerMode,
        __cellResolution.name() : __cellResolution,
        __extent.name() : __extent
    })
Namespace.addCategoryObject('typeBinding', 'Tt', Tt)


# Complex type {http://www.w3.org/ns/ttml}Region with content type ELEMENT_ONLY
class Region (pyxb.binding.basis.complexTypeDefinition):
    """Defines a space or area for the display of subtitle
				content."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Region')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 143, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_Region_metadata', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 149, 3), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'id'), 'id', '__httpwww_w3_orgnsttml_Region_httpwww_w3_orgXML1998namespaceid', pyxb.binding.datatypes.ID, required=True)
    __id._DeclarationLocation = None
    __id._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 151, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute style uses Python identifier style
    __style = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'style'), 'style', '__httpwww_w3_orgnsttml_Region_style', pyxb.binding.datatypes.IDREFS)
    __style._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 163, 2)
    __style._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 163, 2)
    
    style = property(__style.value, __style.set, None, 'ID(s) of one or more style element(s).')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}displayAlign uses Python identifier displayAlign
    __displayAlign = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'displayAlign'), 'displayAlign', '__httpwww_w3_orgnsttml_Region_httpwww_w3_orgnsttmlstylingdisplayAlign', _ImportedBinding__tts.STD_ANON_7)
    __displayAlign._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 119, 1)
    __displayAlign._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 168, 2)
    
    displayAlign = property(__displayAlign.value, __displayAlign.set, None, 'Alignment in the block progression direction.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}padding uses Python identifier padding
    __padding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'padding'), 'padding', '__httpwww_w3_orgnsttml_Region_httpwww_w3_orgnsttmlstylingpadding', _ImportedBinding__ebuttdt.paddingType)
    __padding._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 131, 1)
    __padding._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 169, 2)
    
    padding = property(__padding.value, __padding.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#styling}writingMode uses Python identifier writingMode
    __writingMode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'writingMode'), 'writingMode', '__httpwww_w3_orgnsttml_Region_httpwww_w3_orgnsttmlstylingwritingMode', _ImportedBinding__tts.STD_ANON_8)
    __writingMode._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 132, 1)
    __writingMode._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 175, 2)
    
    writingMode = property(__writingMode.value, __writingMode.set, None, 'Writing mode of subtitle content.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}showBackground uses Python identifier showBackground
    __showBackground = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'showBackground'), 'showBackground', '__httpwww_w3_orgnsttml_Region_httpwww_w3_orgnsttmlstylingshowBackground', _ImportedBinding__tts.STD_ANON_9)
    __showBackground._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 148, 1)
    __showBackground._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 176, 2)
    
    showBackground = property(__showBackground.value, __showBackground.set, None, 'Constraints on when the background color of a region is intended to be\n\t\t\t\tpresented.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}overflow uses Python identifier overflow
    __overflow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'overflow'), 'overflow', '__httpwww_w3_orgnsttml_Region_httpwww_w3_orgnsttmlstylingoverflow', _ImportedBinding__tts.STD_ANON_10)
    __overflow._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 160, 1)
    __overflow._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 177, 2)
    
    overflow = property(__overflow.value, __overflow.set, None, 'Defines whether a region area is clipped if the content of the region\n\t\t\t\toverflows the specified extent of the region.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}extent uses Python identifier extent
    __extent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'extent'), 'extent', '__httpwww_w3_orgnsttml_Region_httpwww_w3_orgnsttmlstylingextent', _ImportedBinding__ebuttdt.extentType, required=True)
    __extent._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 172, 1)
    __extent._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 157, 2)
    
    extent = property(__extent.value, __extent.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#styling}origin uses Python identifier origin
    __origin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'origin'), 'origin', '__httpwww_w3_orgnsttml_Region_httpwww_w3_orgnsttmlstylingorigin', _ImportedBinding__ebuttdt.originType, required=True)
    __origin._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 173, 1)
    __origin._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 156, 2)
    
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
Namespace.addCategoryObject('typeBinding', 'Region', Region)


# Complex type {http://www.w3.org/ns/ttml}Style with content type ELEMENT_ONLY
class Style (pyxb.binding.basis.complexTypeDefinition):
    """Set of style information."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Style')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 91, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_Style_metadata', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 96, 3), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'id'), 'id', '__httpwww_w3_orgnsttml_Style_httpwww_w3_orgXML1998namespaceid', pyxb.binding.datatypes.ID, required=True)
    __id._DeclarationLocation = None
    __id._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 98, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute style uses Python identifier style
    __style = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'style'), 'style', '__httpwww_w3_orgnsttml_Style_style', pyxb.binding.datatypes.IDREFS)
    __style._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 104, 2)
    __style._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 104, 2)
    
    style = property(__style.value, __style.set, None, 'Reference to one or more other tt:style\n\t\t\t\t\telements.')

    
    # Attribute {urn:ebu:tt:style}multiRowAlign uses Python identifier multiRowAlign
    __multiRowAlign = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ebutts, 'multiRowAlign'), 'multiRowAlign', '__httpwww_w3_orgnsttml_Style_urnebuttstylemultiRowAlign', _ImportedBinding__ebutts.STD_ANON)
    __multiRowAlign._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_styling.xsd', 9, 1)
    __multiRowAlign._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 129, 2)
    
    multiRowAlign = property(__multiRowAlign.value, __multiRowAlign.set, None, 'Alignment of multiple \u2018rows\u2019 of inline areas within a containing block\n\t\t\t\tarea.')

    
    # Attribute {urn:ebu:tt:style}linePadding uses Python identifier linePadding
    __linePadding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ebutts, 'linePadding'), 'linePadding', '__httpwww_w3_orgnsttml_Style_urnebuttstylelinePadding', _ImportedBinding__ebutts.STD_ANON_)
    __linePadding._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_styling.xsd', 23, 1)
    __linePadding._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 130, 2)
    
    linePadding = property(__linePadding.value, __linePadding.set, None, ' Padding (or inset) space on the start and end edges of each rendered\n\t\t\t\tline area ')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}direction uses Python identifier direction
    __direction = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'direction'), 'direction', '__httpwww_w3_orgnsttml_Style_httpwww_w3_orgnsttmlstylingdirection', _ImportedBinding__tts.STD_ANON)
    __direction._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 11, 1)
    __direction._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 110, 2)
    
    direction = property(__direction.value, __direction.set, None, 'Directionality if bi-directional text is used.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}fontFamily uses Python identifier fontFamily
    __fontFamily = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'fontFamily'), 'fontFamily', '__httpwww_w3_orgnsttml_Style_httpwww_w3_orgnsttmlstylingfontFamily', _ImportedBinding__ebuttdt.fontFamilyType)
    __fontFamily._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 22, 1)
    __fontFamily._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 111, 2)
    
    fontFamily = property(__fontFamily.value, __fontFamily.set, None, 'Font-family from which glyphs are selected.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}fontSize uses Python identifier fontSize
    __fontSize = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'fontSize'), 'fontSize', '__httpwww_w3_orgnsttml_Style_httpwww_w3_orgnsttmlstylingfontSize', _ImportedBinding__ebuttdt.fontSizeType)
    __fontSize._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 27, 1)
    __fontSize._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 112, 2)
    
    fontSize = property(__fontSize.value, __fontSize.set, None, 'The font-size of a glyph.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}lineHeight uses Python identifier lineHeight
    __lineHeight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'lineHeight'), 'lineHeight', '__httpwww_w3_orgnsttml_Style_httpwww_w3_orgnsttmlstylinglineHeight', _ImportedBinding__ebuttdt.lineHeightType)
    __lineHeight._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 32, 1)
    __lineHeight._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 113, 2)
    
    lineHeight = property(__lineHeight.value, __lineHeight.set, None, 'Inter-baseline separation between line areas.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}textAlign uses Python identifier textAlign
    __textAlign = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'textAlign'), 'textAlign', '__httpwww_w3_orgnsttml_Style_httpwww_w3_orgnsttmlstylingtextAlign', _ImportedBinding__tts.STD_ANON_)
    __textAlign._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 37, 1)
    __textAlign._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 114, 2)
    
    textAlign = property(__textAlign.value, __textAlign.set, None, 'Alignment of inline areas in a containing block.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}color uses Python identifier color
    __color = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'color'), 'color', '__httpwww_w3_orgnsttml_Style_httpwww_w3_orgnsttmlstylingcolor', _ImportedBinding__ebuttdt.colorType)
    __color._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 51, 1)
    __color._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 115, 2)
    
    color = property(__color.value, __color.set, None, 'Foreground colour of an area.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}backgroundColor uses Python identifier backgroundColor
    __backgroundColor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'backgroundColor'), 'backgroundColor', '__httpwww_w3_orgnsttml_Style_httpwww_w3_orgnsttmlstylingbackgroundColor', _ImportedBinding__ebuttdt.colorType)
    __backgroundColor._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 56, 1)
    __backgroundColor._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 116, 2)
    
    backgroundColor = property(__backgroundColor.value, __backgroundColor.set, None, 'Background colour of a subtitle or a region.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}fontStyle uses Python identifier fontStyle
    __fontStyle = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'fontStyle'), 'fontStyle', '__httpwww_w3_orgnsttml_Style_httpwww_w3_orgnsttmlstylingfontStyle', _ImportedBinding__tts.STD_ANON_2)
    __fontStyle._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 61, 1)
    __fontStyle._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 117, 2)
    
    fontStyle = property(__fontStyle.value, __fontStyle.set, None, 'Font style that applies to glyphs.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}fontWeight uses Python identifier fontWeight
    __fontWeight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'fontWeight'), 'fontWeight', '__httpwww_w3_orgnsttml_Style_httpwww_w3_orgnsttmlstylingfontWeight', _ImportedBinding__tts.STD_ANON_3)
    __fontWeight._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 72, 1)
    __fontWeight._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 118, 2)
    
    fontWeight = property(__fontWeight.value, __fontWeight.set, None, 'Font weight that applies to glyphs.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}textDecoration uses Python identifier textDecoration
    __textDecoration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'textDecoration'), 'textDecoration', '__httpwww_w3_orgnsttml_Style_httpwww_w3_orgnsttmlstylingtextDecoration', _ImportedBinding__tts.STD_ANON_4)
    __textDecoration._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 83, 1)
    __textDecoration._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 119, 2)
    
    textDecoration = property(__textDecoration.value, __textDecoration.set, None, 'Whether a glyph is underlined.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}unicodeBidi uses Python identifier unicodeBidi
    __unicodeBidi = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'unicodeBidi'), 'unicodeBidi', '__httpwww_w3_orgnsttml_Style_httpwww_w3_orgnsttmlstylingunicodeBidi', _ImportedBinding__tts.STD_ANON_5)
    __unicodeBidi._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 94, 1)
    __unicodeBidi._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 120, 2)
    
    unicodeBidi = property(__unicodeBidi.value, __unicodeBidi.set, None, 'Directional embedding or override according to the Unicode\n\t\t\t\tbidirectional algorithm.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}wrapOption uses Python identifier wrapOption
    __wrapOption = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'wrapOption'), 'wrapOption', '__httpwww_w3_orgnsttml_Style_httpwww_w3_orgnsttmlstylingwrapOption', _ImportedBinding__tts.STD_ANON_6)
    __wrapOption._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 107, 1)
    __wrapOption._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 121, 2)
    
    wrapOption = property(__wrapOption.value, __wrapOption.set, None, 'Defines whether or not automatic line wrapping (breaking) applies\n\t\t\t\twithin the context of the affected element.')

    
    # Attribute {http://www.w3.org/ns/ttml#styling}padding uses Python identifier padding
    __padding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_tts, 'padding'), 'padding', '__httpwww_w3_orgnsttml_Style_httpwww_w3_orgnsttmlstylingpadding', _ImportedBinding__ebuttdt.paddingType)
    __padding._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/styling.xsd', 131, 1)
    __padding._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 122, 2)
    
    padding = property(__padding.value, __padding.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata
    })
    _AttributeMap.update({
        __id.name() : __id,
        __style.name() : __style,
        __multiRowAlign.name() : __multiRowAlign,
        __linePadding.name() : __linePadding,
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
        __padding.name() : __padding
    })
Namespace.addCategoryObject('typeBinding', 'Style', Style)


# Complex type {http://www.w3.org/ns/ttml}P with content type MIXED
class P (pyxb.binding.basis.complexTypeDefinition):
    """Logical paragraph."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'P')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 228, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_P_metadata', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 233, 3), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element br uses Python identifier br
    __br = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'br'), 'br', '__httpwww_w3_orgnsttml_P_br', True, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 235, 4), )

    
    br = property(__br.value, __br.set, None, None)

    
    # Element span uses Python identifier span
    __span = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'span'), 'span', '__httpwww_w3_orgnsttml_P_span', True, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 236, 4), )

    
    span = property(__span.value, __span.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}space uses Python identifier space
    __space = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'space'), 'space', '__httpwww_w3_orgnsttml_P_httpwww_w3_orgXML1998namespacespace', pyxb.binding.xml_.STD_ANON_space)
    __space._DeclarationLocation = None
    __space._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 244, 2)
    
    space = property(__space.value, __space.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_orgnsttml_P_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 250, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'id'), 'id', '__httpwww_w3_orgnsttml_P_httpwww_w3_orgXML1998namespaceid', pyxb.binding.datatypes.ID, required=True)
    __id._DeclarationLocation = None
    __id._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 239, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute region uses Python identifier region
    __region = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'region'), 'region', '__httpwww_w3_orgnsttml_P_region', pyxb.binding.datatypes.IDREF)
    __region._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 256, 2)
    __region._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 256, 2)
    
    region = property(__region.value, __region.set, None, 'Application of layout information through reference of a\n\t\t\t\t\tregion.')

    
    # Attribute style uses Python identifier style
    __style = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'style'), 'style', '__httpwww_w3_orgnsttml_P_style', pyxb.binding.datatypes.IDREFS)
    __style._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 262, 2)
    __style._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 262, 2)
    
    style = property(__style.value, __style.set, None, 'ID(s) of one or more style element(s). The style information shall\n\t\t\t\t\tbe applied to the enclosed content of the tt:p element.')

    
    # Attribute begin uses Python identifier begin
    __begin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'begin'), 'begin', '__httpwww_w3_orgnsttml_P_begin', _ImportedBinding__ebuttdt.timingType, required=True)
    __begin._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 268, 2)
    __begin._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 268, 2)
    
    begin = property(__begin.value, __begin.set, None, 'Start point of a temporal interval associated with a tt:p\n\t\t\t\t\telement.')

    
    # Attribute end uses Python identifier end
    __end = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'end'), 'end', '__httpwww_w3_orgnsttml_P_end', _ImportedBinding__ebuttdt.timingType, required=True)
    __end._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 274, 2)
    __end._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 274, 2)
    
    end = property(__end.value, __end.set, None, 'End point of a temporal interval associated with a tt:p\n\t\t\t\t\telement.')

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}agent uses Python identifier agent
    __agent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'agent'), 'agent', '__httpwww_w3_orgnsttml_P_httpwww_w3_orgnsttmlmetadataagent', pyxb.binding.datatypes.IDREFS)
    __agent._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 10, 1)
    __agent._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 280, 2)
    
    agent = property(__agent.value, __agent.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'role'), 'role', '__httpwww_w3_orgnsttml_P_httpwww_w3_orgnsttmlmetadatarole', pyxb.binding.datatypes.NMTOKENS)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 11, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 281, 2)
    
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
        __region.name() : __region,
        __style.name() : __style,
        __begin.name() : __begin,
        __end.name() : __end,
        __agent.name() : __agent,
        __role.name() : __role
    })
Namespace.addCategoryObject('typeBinding', 'P', P)


# Complex type {http://www.w3.org/ns/ttml}Span with content type MIXED
class Span (pyxb.binding.basis.complexTypeDefinition):
    """Inline element to allow the application of local style information,
				annotation or metadata."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Span')
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 283, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element metadata uses Python identifier metadata
    __metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'metadata'), 'metadata', '__httpwww_w3_orgnsttml_Span_metadata', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 289, 3), )

    
    metadata = property(__metadata.value, __metadata.set, None, None)

    
    # Element br uses Python identifier br
    __br = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'br'), 'br', '__httpwww_w3_orgnsttml_Span_br', True, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 291, 4), )

    
    br = property(__br.value, __br.set, None, None)

    
    # Element span uses Python identifier span
    __span = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'span'), 'span', '__httpwww_w3_orgnsttml_Span_span', True, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 292, 4), )

    
    span = property(__span.value, __span.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'id'), 'id', '__httpwww_w3_orgnsttml_Span_httpwww_w3_orgXML1998namespaceid', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = None
    __id._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 307, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}space uses Python identifier space
    __space = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'space'), 'space', '__httpwww_w3_orgnsttml_Span_httpwww_w3_orgXML1998namespacespace', pyxb.binding.xml_.STD_ANON_space)
    __space._DeclarationLocation = None
    __space._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 295, 2)
    
    space = property(__space.value, __space.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_orgnsttml_Span_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 301, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    
    # Attribute style uses Python identifier style
    __style = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'style'), 'style', '__httpwww_w3_orgnsttml_Span_style', pyxb.binding.datatypes.IDREFS)
    __style._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 313, 2)
    __style._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 313, 2)
    
    style = property(__style.value, __style.set, None, 'ID(s) of one or more style element(s). The style information shall\n\t\t\t\t\tbe applied to the enclosed content of the tt:span element.')

    
    # Attribute begin uses Python identifier begin
    __begin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'begin'), 'begin', '__httpwww_w3_orgnsttml_Span_begin', _ImportedBinding__ebuttdt.timingType)
    __begin._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 319, 2)
    __begin._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 319, 2)
    
    begin = property(__begin.value, __begin.set, None, 'Start point of a temporal interval associated with the\n\t\t\t\t\telement.')

    
    # Attribute end uses Python identifier end
    __end = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'end'), 'end', '__httpwww_w3_orgnsttml_Span_end', _ImportedBinding__ebuttdt.timingType)
    __end._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 325, 2)
    __end._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 325, 2)
    
    end = property(__end.value, __end.set, None, 'End point of a temporal interval associated with the\n\t\t\t\t\telement.')

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}agent uses Python identifier agent
    __agent = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'agent'), 'agent', '__httpwww_w3_orgnsttml_Span_httpwww_w3_orgnsttmlmetadataagent', pyxb.binding.datatypes.IDREFS)
    __agent._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 10, 1)
    __agent._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 331, 2)
    
    agent = property(__agent.value, __agent.set, None, None)

    
    # Attribute {http://www.w3.org/ns/ttml#metadata}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_ttm, 'role'), 'role', '__httpwww_w3_orgnsttml_Span_httpwww_w3_orgnsttmlmetadatarole', pyxb.binding.datatypes.NMTOKENS)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/metadata.xsd', 11, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 332, 2)
    
    role = property(__role.value, __role.set, None, None)

    _ElementMap.update({
        __metadata.name() : __metadata,
        __br.name() : __br,
        __span.name() : __span
    })
    _AttributeMap.update({
        __id.name() : __id,
        __space.name() : __space,
        __lang.name() : __lang,
        __style.name() : __style,
        __begin.name() : __begin,
        __end.name() : __end,
        __agent.name() : __agent,
        __role.name() : __role
    })
Namespace.addCategoryObject('typeBinding', 'Span', Span)


tt = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tt'), Tt, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 346, 1))
Namespace.addCategoryObject('elementBinding', tt.name().localName(), tt)



Head._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'metadata'), Metadata, scope=Head, documentation='Generic container for metadata information that applies to the\n\t\t\t\t\t\twhole document.', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 61, 3)))

Head._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'styling'), Styling, scope=Head, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 67, 3)))

Head._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'layout'), Layout, scope=Head, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 68, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Head._UseForTag(pyxb.namespace.ExpandedName(None, 'metadata')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 61, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Head._UseForTag(pyxb.namespace.ExpandedName(None, 'styling')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 67, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Head._UseForTag(pyxb.namespace.ExpandedName(None, 'layout')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 68, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Head._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 77, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/ns/ttml')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 77, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Metadata._Automaton = _BuildAutomaton_()




Styling._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'metadata'), Metadata, scope=Styling, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 86, 3)))

Styling._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'style'), Style, scope=Styling, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 87, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 86, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Styling._UseForTag(pyxb.namespace.ExpandedName(None, 'metadata')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 86, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Styling._UseForTag(pyxb.namespace.ExpandedName(None, 'style')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 87, 3))
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
Styling._Automaton = _BuildAutomaton_2()




Layout._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'metadata'), Metadata, scope=Layout, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 138, 3)))

Layout._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'region'), Region, scope=Layout, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 139, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 138, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Layout._UseForTag(pyxb.namespace.ExpandedName(None, 'metadata')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 138, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Layout._UseForTag(pyxb.namespace.ExpandedName(None, 'region')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 139, 3))
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
Layout._Automaton = _BuildAutomaton_3()




Body._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'metadata'), Metadata, scope=Body, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 186, 3)))

Body._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'div'), Div, scope=Body, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 187, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 186, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Body._UseForTag(pyxb.namespace.ExpandedName(None, 'metadata')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 186, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Body._UseForTag(pyxb.namespace.ExpandedName(None, 'div')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 187, 3))
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
Body._Automaton = _BuildAutomaton_4()




Div._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'metadata'), Metadata, scope=Div, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 199, 3)))

Div._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'div'), Div, scope=Div, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 201, 4)))

Div._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'p'), P, scope=Div, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 202, 4)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 199, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Div._UseForTag(pyxb.namespace.ExpandedName(None, 'metadata')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 199, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Div._UseForTag(pyxb.namespace.ExpandedName(None, 'div')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 201, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Div._UseForTag(pyxb.namespace.ExpandedName(None, 'p')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 202, 4))
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
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Div._Automaton = _BuildAutomaton_5()




Br._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'metadata'), Metadata, scope=Br, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 340, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 340, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Br._UseForTag(pyxb.namespace.ExpandedName(None, 'metadata')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 340, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Br._Automaton = _BuildAutomaton_6()




Tt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'head'), Head, scope=Tt, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 24, 3)))

Tt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'body'), Body, scope=Tt, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 25, 3)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Tt._UseForTag(pyxb.namespace.ExpandedName(None, 'head')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 24, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Tt._UseForTag(pyxb.namespace.ExpandedName(None, 'body')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 25, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Tt._Automaton = _BuildAutomaton_7()




Region._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'metadata'), Metadata, scope=Region, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 149, 3)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 149, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Region._UseForTag(pyxb.namespace.ExpandedName(None, 'metadata')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 149, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Region._Automaton = _BuildAutomaton_8()




Style._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'metadata'), Metadata, scope=Style, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 96, 3)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 96, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Style._UseForTag(pyxb.namespace.ExpandedName(None, 'metadata')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 96, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Style._Automaton = _BuildAutomaton_9()




P._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'metadata'), Metadata, scope=P, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 233, 3)))

P._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'br'), Br, scope=P, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 235, 4)))

P._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'span'), Span, scope=P, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 236, 4)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 233, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 234, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(P._UseForTag(pyxb.namespace.ExpandedName(None, 'metadata')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 233, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(P._UseForTag(pyxb.namespace.ExpandedName(None, 'br')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 235, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(P._UseForTag(pyxb.namespace.ExpandedName(None, 'span')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 236, 4))
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
P._Automaton = _BuildAutomaton_10()




Span._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'metadata'), Metadata, scope=Span, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 289, 3)))

Span._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'br'), Br, scope=Span, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 291, 4)))

Span._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'span'), Span, scope=Span, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 292, 4)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 289, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 290, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Span._UseForTag(pyxb.namespace.ExpandedName(None, 'metadata')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 289, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Span._UseForTag(pyxb.namespace.ExpandedName(None, 'br')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 291, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Span._UseForTag(pyxb.namespace.ExpandedName(None, 'span')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_live.xsd', 292, 4))
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
Span._Automaton = _BuildAutomaton_11()

