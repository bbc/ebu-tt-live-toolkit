# ./ebu_tt_live/bindings/_ebuttm.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:ca3389a21c0cafded0139f24017756c1e6ca4da7
# Generated 2016-04-07 17:03:00.125306 by PyXB version 1.2.4 using Python 2.7.9.final.0
# Namespace urn:ebu:tt:metadata [xmlns:ebuttm]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:335fe6ae-fcda-11e5-890b-6c40089ad95e')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import _ebuttdt as _ImportedBinding__ebuttdt

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:ebu:tt:metadata', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 23, 6)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.BASE64 = STD_ANON._CF_enumeration.addEnumeration(unicode_value='BASE64', tag='BASE64')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 78, 5)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.v1_0 = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='v1.0', tag='v1_0')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 143, 9)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.topBottom = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='topBottom', tag='topBottom')
STD_ANON_2.leftRight = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='leftRight', tag='leftRight')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 224, 5)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.live = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='live', tag='live')
STD_ANON_3.prepared = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='prepared', tag='prepared')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """EBU-TT specific metadata that applies to the whole EBU-TT
				document."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 64, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ebu:tt:metadata}conformsToStandard uses Python identifier conformsToStandard
    __conformsToStandard = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'conformsToStandard'), 'conformsToStandard', '__urnebuttmetadata_CTD_ANON_urnebuttmetadataconformsToStandard', True, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 66, 4), )

    
    conformsToStandard = property(__conformsToStandard.value, __conformsToStandard.set, None, 'Indicates the conformance with a specific standard that is\n\t\t\t\t\t\t\tderived from TTML.')

    
    # Element {urn:ebu:tt:metadata}documentEbuttVersion uses Python identifier documentEbuttVersion
    __documentEbuttVersion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentEbuttVersion'), 'documentEbuttVersion', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentEbuttVersion', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 73, 4), )

    
    documentEbuttVersion = property(__documentEbuttVersion.value, __documentEbuttVersion.set, None, 'The version of the EBU-TT standard used by the document\n\t\t\t\t\t\t\tinstance.')

    
    # Element {urn:ebu:tt:metadata}documentIdentifier uses Python identifier documentIdentifier
    __documentIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentIdentifier'), 'documentIdentifier', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentIdentifier', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 84, 4), )

    
    documentIdentifier = property(__documentIdentifier.value, __documentIdentifier.set, None, 'Identifier for an EBU-TT document that may be used as\n\t\t\t\t\t\t\texternal reference to an EBU-TT document.')

    
    # Element {urn:ebu:tt:metadata}documentOriginatingSystem uses Python identifier documentOriginatingSystem
    __documentOriginatingSystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentOriginatingSystem'), 'documentOriginatingSystem', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentOriginatingSystem', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 90, 4), )

    
    documentOriginatingSystem = property(__documentOriginatingSystem.value, __documentOriginatingSystem.set, None, 'Software and version used to create the EBU-TT\n\t\t\t\t\t\t\tdocument.')

    
    # Element {urn:ebu:tt:metadata}documentCopyright uses Python identifier documentCopyright
    __documentCopyright = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentCopyright'), 'documentCopyright', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentCopyright', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 96, 4), )

    
    documentCopyright = property(__documentCopyright.value, __documentCopyright.set, None, 'The copyright of the document.')

    
    # Element {urn:ebu:tt:metadata}documentReadingSpeed uses Python identifier documentReadingSpeed
    __documentReadingSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentReadingSpeed'), 'documentReadingSpeed', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentReadingSpeed', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 101, 4), )

    
    documentReadingSpeed = property(__documentReadingSpeed.value, __documentReadingSpeed.set, None, 'The intended reading speed for the subtitles in words per\n\t\t\t\t\t\t\tminute.')

    
    # Element {urn:ebu:tt:metadata}documentTargetAspectRatio uses Python identifier documentTargetAspectRatio
    __documentTargetAspectRatio = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentTargetAspectRatio'), 'documentTargetAspectRatio', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentTargetAspectRatio', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 107, 4), )

    
    documentTargetAspectRatio = property(__documentTargetAspectRatio.value, __documentTargetAspectRatio.set, None, 'The aspect ratio of the video the EBU-TT document was\n\t\t\t\t\t\t\tauthored for, in width by height.')

    
    # Element {urn:ebu:tt:metadata}documentTargetActiveFormatDescriptor uses Python identifier documentTargetActiveFormatDescriptor
    __documentTargetActiveFormatDescriptor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentTargetActiveFormatDescriptor'), 'documentTargetActiveFormatDescriptor', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentTargetActiveFormatDescriptor', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 113, 4), )

    
    documentTargetActiveFormatDescriptor = property(__documentTargetActiveFormatDescriptor.value, __documentTargetActiveFormatDescriptor.set, None, 'The code for the Active Format Descriptor (AFD) that\n\t\t\t\t\t\t\tspecifies the active image in the active video (see \u201cDefinitions of\n\t\t\t\t\t\t\tterms\u201d). The code shall be one of the AFD codes specified in SMPTE ST\n\t\t\t\t\t\t\t2016 1:2009 \u201cFormat for Active Format Description and Bar Data\u201d Table\n\t\t\t\t\t\t\t1.')

    
    # Element {urn:ebu:tt:metadata}documentIntendedTargetBarData uses Python identifier documentIntendedTargetBarData
    __documentIntendedTargetBarData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentIntendedTargetBarData'), 'documentIntendedTargetBarData', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentIntendedTargetBarData', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 123, 4), )

    
    documentIntendedTargetBarData = property(__documentIntendedTargetBarData.value, __documentIntendedTargetBarData.set, None, 'When an ebuttm:documentTargetActiveFormatDescriptor\n\t\t\t\t\t\t\telement is used in an EBU-TT document, an\n\t\t\t\t\t\t\tebuttm:documentIntendedTargetBarData element may be used whenever the\n\t\t\t\t\t\t\tAFD alone is insufficient to describe the extent of the image (i.e. AFD\n\t\t\t\t\t\t\tvalues 0000 and 0100). The Bar Data shall be specified in accordance\n\t\t\t\t\t\t\twith SMPTE ST 2016 1:2009 \u201cFormat for Active Format Description and Bar\n\t\t\t\t\t\t\tData\u201d Table 3.')

    
    # Element {urn:ebu:tt:metadata}documentIntendedTargetFormat uses Python identifier documentIntendedTargetFormat
    __documentIntendedTargetFormat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentIntendedTargetFormat'), 'documentIntendedTargetFormat', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentIntendedTargetFormat', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 200, 4), )

    
    documentIntendedTargetFormat = property(__documentIntendedTargetFormat.value, __documentIntendedTargetFormat.set, None, 'Indicates the subtitle format an author had in mind when\n\t\t\t\t\t\t\tauthoring an EBU-TT document or transforming another format to an EBU-TT\n\t\t\t\t\t\t\tdocument.')

    
    # Element {urn:ebu:tt:metadata}documentCreationMode uses Python identifier documentCreationMode
    __documentCreationMode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentCreationMode'), 'documentCreationMode', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentCreationMode', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 219, 4), )

    
    documentCreationMode = property(__documentCreationMode.value, __documentCreationMode.set, None, 'Identifies the overall workflow used to create the content\n\t\t\t\t\t\t\tin the document.')

    
    # Element {urn:ebu:tt:metadata}documentContentType uses Python identifier documentContentType
    __documentContentType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentContentType'), 'documentContentType', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentContentType', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 231, 4), )

    
    documentContentType = property(__documentContentType.value, __documentContentType.set, None, None)

    
    # Element {urn:ebu:tt:metadata}relatedMediaIdentifier  uses Python identifier relatedMediaIdentifier
    __relatedMediaIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relatedMediaIdentifier '), 'relatedMediaIdentifier', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatarelatedMediaIdentifier', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 245, 4), )

    
    relatedMediaIdentifier = property(__relatedMediaIdentifier.value, __relatedMediaIdentifier.set, None, None)

    
    # Element {urn:ebu:tt:metadata}relatedObjectIdentifier uses Python identifier relatedObjectIdentifier
    __relatedObjectIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relatedObjectIdentifier'), 'relatedObjectIdentifier', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatarelatedObjectIdentifier', True, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 246, 4), )

    
    relatedObjectIdentifier = property(__relatedObjectIdentifier.value, __relatedObjectIdentifier.set, None, None)

    
    # Element {urn:ebu:tt:metadata}appliedProcessing uses Python identifier appliedProcessing
    __appliedProcessing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'appliedProcessing'), 'appliedProcessing', '__urnebuttmetadata_CTD_ANON_urnebuttmetadataappliedProcessing', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 251, 4), )

    
    appliedProcessing = property(__appliedProcessing.value, __appliedProcessing.set, None, None)

    
    # Element {urn:ebu:tt:metadata}relatedMediaDuration uses Python identifier relatedMediaDuration
    __relatedMediaDuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relatedMediaDuration'), 'relatedMediaDuration', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatarelatedMediaDuration', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 260, 4), )

    
    relatedMediaDuration = property(__relatedMediaDuration.value, __relatedMediaDuration.set, None, None)

    
    # Element {urn:ebu:tt:metadata}documentBeginDate uses Python identifier documentBeginDate
    __documentBeginDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentBeginDate'), 'documentBeginDate', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentBeginDate', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 261, 4), )

    
    documentBeginDate = property(__documentBeginDate.value, __documentBeginDate.set, None, None)

    
    # Element {urn:ebu:tt:metadata}localTimeOffset uses Python identifier localTimeOffset
    __localTimeOffset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'localTimeOffset'), 'localTimeOffset', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatalocalTimeOffset', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 262, 4), )

    
    localTimeOffset = property(__localTimeOffset.value, __localTimeOffset.set, None, None)

    
    # Element {urn:ebu:tt:metadata}clockIdentifier uses Python identifier clockIdentifier
    __clockIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'clockIdentifier'), 'clockIdentifier', '__urnebuttmetadata_CTD_ANON_urnebuttmetadataclockIdentifier', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 263, 4), )

    
    clockIdentifier = property(__clockIdentifier.value, __clockIdentifier.set, None, None)

    
    # Element {urn:ebu:tt:metadata}broadcastServiceIdentifier uses Python identifier broadcastServiceIdentifier
    __broadcastServiceIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcastServiceIdentifier'), 'broadcastServiceIdentifier', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatabroadcastServiceIdentifier', True, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 264, 4), )

    
    broadcastServiceIdentifier = property(__broadcastServiceIdentifier.value, __broadcastServiceIdentifier.set, None, None)

    
    # Element {urn:ebu:tt:metadata}documentOriginalProgrammeTitle uses Python identifier documentOriginalProgrammeTitle
    __documentOriginalProgrammeTitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentOriginalProgrammeTitle'), 'documentOriginalProgrammeTitle', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentOriginalProgrammeTitle', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 270, 4), )

    
    documentOriginalProgrammeTitle = property(__documentOriginalProgrammeTitle.value, __documentOriginalProgrammeTitle.set, None, 'The programme title in the original language. STL mapping:\n\t\t\t\t\t\t\tOriginal Programme Title (OPT).')

    
    # Element {urn:ebu:tt:metadata}documentOriginalEpisodeTitle uses Python identifier documentOriginalEpisodeTitle
    __documentOriginalEpisodeTitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentOriginalEpisodeTitle'), 'documentOriginalEpisodeTitle', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentOriginalEpisodeTitle', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 276, 4), )

    
    documentOriginalEpisodeTitle = property(__documentOriginalEpisodeTitle.value, __documentOriginalEpisodeTitle.set, None, 'The title of the episode of the programme in the original\n\t\t\t\t\t\t\tlanguage. STL mapping: Original Episode Title (OET).')

    
    # Element {urn:ebu:tt:metadata}documentTranslatedProgrammeTitle uses Python identifier documentTranslatedProgrammeTitle
    __documentTranslatedProgrammeTitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatedProgrammeTitle'), 'documentTranslatedProgrammeTitle', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentTranslatedProgrammeTitle', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 282, 4), )

    
    documentTranslatedProgrammeTitle = property(__documentTranslatedProgrammeTitle.value, __documentTranslatedProgrammeTitle.set, None, 'The programme title in the local language. STL mapping:\n\t\t\t\t\t\t\tTranslated Programme Title (TPT).')

    
    # Element {urn:ebu:tt:metadata}documentTranslatedEpisodeTitle uses Python identifier documentTranslatedEpisodeTitle
    __documentTranslatedEpisodeTitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatedEpisodeTitle'), 'documentTranslatedEpisodeTitle', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentTranslatedEpisodeTitle', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 288, 4), )

    
    documentTranslatedEpisodeTitle = property(__documentTranslatedEpisodeTitle.value, __documentTranslatedEpisodeTitle.set, None, 'The title of the episode of the programme in the local\n\t\t\t\t\t\t\tlanguage. STL mapping: Translated Episode Title\n\t\t\t\t\t\t\t(TET).')

    
    # Element {urn:ebu:tt:metadata}documentTranslatorsName uses Python identifier documentTranslatorsName
    __documentTranslatorsName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatorsName'), 'documentTranslatorsName', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentTranslatorsName', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 295, 4), )

    
    documentTranslatorsName = property(__documentTranslatorsName.value, __documentTranslatorsName.set, None, "Name of the translator. STL mapping: Translator's Name\n\t\t\t\t\t\t\t(TN). ")

    
    # Element {urn:ebu:tt:metadata}documentTranslatorsContactDetails uses Python identifier documentTranslatorsContactDetails
    __documentTranslatorsContactDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatorsContactDetails'), 'documentTranslatorsContactDetails', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentTranslatorsContactDetails', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 301, 4), )

    
    documentTranslatorsContactDetails = property(__documentTranslatorsContactDetails.value, __documentTranslatorsContactDetails.set, None, "The translator's contact details. STL mapping:\n\t\t\t\t\t\t\tTranslator's Contact Details (TCD).")

    
    # Element {urn:ebu:tt:metadata}documentSubtitleListReferenceCode uses Python identifier documentSubtitleListReferenceCode
    __documentSubtitleListReferenceCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentSubtitleListReferenceCode'), 'documentSubtitleListReferenceCode', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentSubtitleListReferenceCode', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 307, 4), )

    
    documentSubtitleListReferenceCode = property(__documentSubtitleListReferenceCode.value, __documentSubtitleListReferenceCode.set, None, 'Free-format character string which may be used to provide\n\t\t\t\t\t\t\tan additional reference for the subtitle list. Note: This attribute is\n\t\t\t\t\t\t\tprovided to support conversion of STL subtitle files and to retain the\n\t\t\t\t\t\t\tmetadata from the GSI block. STL mapping: Subtitle List Reference Code\n\t\t\t\t\t\t\t(SLR)')

    
    # Element {urn:ebu:tt:metadata}documentCreationDate uses Python identifier documentCreationDate
    __documentCreationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentCreationDate'), 'documentCreationDate', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentCreationDate', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 316, 4), )

    
    documentCreationDate = property(__documentCreationDate.value, __documentCreationDate.set, None, 'The date of creation of the EBU-TT document.\n\t\t\t\t\t\t')

    
    # Element {urn:ebu:tt:metadata}documentRevisionDate uses Python identifier documentRevisionDate
    __documentRevisionDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentRevisionDate'), 'documentRevisionDate', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentRevisionDate', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 322, 4), )

    
    documentRevisionDate = property(__documentRevisionDate.value, __documentRevisionDate.set, None, 'The date of the most-recent modifications to the EBU-TT\n\t\t\t\t\t\t\tdocument. ')

    
    # Element {urn:ebu:tt:metadata}documentRevisionNumber uses Python identifier documentRevisionNumber
    __documentRevisionNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentRevisionNumber'), 'documentRevisionNumber', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentRevisionNumber', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 328, 4), )

    
    documentRevisionNumber = property(__documentRevisionNumber.value, __documentRevisionNumber.set, None, 'The revision number of the EBU-TT document may be used to\n\t\t\t\t\t\t\tspecify a particular version of the subtitle list. ')

    
    # Element {urn:ebu:tt:metadata}documentTotalNumberOfSubtitles uses Python identifier documentTotalNumberOfSubtitles
    __documentTotalNumberOfSubtitles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentTotalNumberOfSubtitles'), 'documentTotalNumberOfSubtitles', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentTotalNumberOfSubtitles', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 334, 4), )

    
    documentTotalNumberOfSubtitles = property(__documentTotalNumberOfSubtitles.value, __documentTotalNumberOfSubtitles.set, None, 'The number of subtitles. STL mapping: Total Number of\n\t\t\t\t\t\t\tSubtitles (TNS).')

    
    # Element {urn:ebu:tt:metadata}documentMaximumNumberOfDisplayableCharacterInAnyRow uses Python identifier documentMaximumNumberOfDisplayableCharacterInAnyRow
    __documentMaximumNumberOfDisplayableCharacterInAnyRow = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentMaximumNumberOfDisplayableCharacterInAnyRow'), 'documentMaximumNumberOfDisplayableCharacterInAnyRow', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentMaximumNumberOfDisplayableCharacterInAnyRow', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 341, 4), )

    
    documentMaximumNumberOfDisplayableCharacterInAnyRow = property(__documentMaximumNumberOfDisplayableCharacterInAnyRow.value, __documentMaximumNumberOfDisplayableCharacterInAnyRow.set, None, 'Maximum number of displayable rows per television frame\n\t\t\t\t\t\t\twhich could be occupied at any one time by the subtitles defined in the\n\t\t\t\t\t\t\tTTI blocks. STL mapping: Maximum Number of Displayable Characters in any\n\t\t\t\t\t\t\ttext row (MNC). ')

    
    # Element {urn:ebu:tt:metadata}documentStartOfProgramme uses Python identifier documentStartOfProgramme
    __documentStartOfProgramme = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentStartOfProgramme'), 'documentStartOfProgramme', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentStartOfProgramme', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 350, 4), )

    
    documentStartOfProgramme = property(__documentStartOfProgramme.value, __documentStartOfProgramme.set, None, 'The time code of the first frame of the recorded video\n\t\t\t\t\t\t\tsignal which is intended for transmission. Note: When the referenced\n\t\t\t\t\t\t\tstart timecode of the video material the subtitles were authored for is\n\t\t\t\t\t\t\tgreater than 00:00:00:00 (e.g. 10:00:00:00) it is recommended to specify\n\t\t\t\t\t\t\tthe attribute ebuttm:documentStartOfPrograme. STL mapping: Timecode:\n\t\t\t\t\t\t\tStart-of-Programme (TCP).')

    
    # Element {urn:ebu:tt:metadata}documentCountryOfOrigin uses Python identifier documentCountryOfOrigin
    __documentCountryOfOrigin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentCountryOfOrigin'), 'documentCountryOfOrigin', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentCountryOfOrigin', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 361, 4), )

    
    documentCountryOfOrigin = property(__documentCountryOfOrigin.value, __documentCountryOfOrigin.set, None, 'The country of origin of the subtitle list. STL mapping:\n\t\t\t\t\t\t\tCountry of Origin (CO). ')

    
    # Element {urn:ebu:tt:metadata}documentPublisher uses Python identifier documentPublisher
    __documentPublisher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentPublisher'), 'documentPublisher', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentPublisher', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 367, 4), )

    
    documentPublisher = property(__documentPublisher.value, __documentPublisher.set, None, 'Name of the publisher of the subtitle list. STL mapping:\n\t\t\t\t\t\t\tPublisher (PUB).')

    
    # Element {urn:ebu:tt:metadata}documentEditorsName uses Python identifier documentEditorsName
    __documentEditorsName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentEditorsName'), 'documentEditorsName', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentEditorsName', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 373, 4), )

    
    documentEditorsName = property(__documentEditorsName.value, __documentEditorsName.set, None, "Name of the editor of the subtitle list. STL mapping:\n\t\t\t\t\t\t\tEditor's Name (EN).")

    
    # Element {urn:ebu:tt:metadata}documentEditorsContactDetails uses Python identifier documentEditorsContactDetails
    __documentEditorsContactDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentEditorsContactDetails'), 'documentEditorsContactDetails', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentEditorsContactDetails', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 379, 4), )

    
    documentEditorsContactDetails = property(__documentEditorsContactDetails.value, __documentEditorsContactDetails.set, None, "Information about the editor named in the metadata element\n\t\t\t\t\t\t\tdocumentEditorsName. STL mapping: Editor's Contact Details (ECD).\n\t\t\t\t\t\t")

    
    # Element {urn:ebu:tt:metadata}documentUserDefinedArea uses Python identifier documentUserDefinedArea
    __documentUserDefinedArea = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentUserDefinedArea'), 'documentUserDefinedArea', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatadocumentUserDefinedArea', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 386, 4), )

    
    documentUserDefinedArea = property(__documentUserDefinedArea.value, __documentUserDefinedArea.set, None, 'This field may be used to carry information about the\n\t\t\t\t\t\t\tprogramme or subtitle list, or other relevant details. STL mapping:\n\t\t\t\t\t\t\tUser-Defined Area (UDA).')

    
    # Element {urn:ebu:tt:metadata}stlCreationDate uses Python identifier stlCreationDate
    __stlCreationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stlCreationDate'), 'stlCreationDate', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatastlCreationDate', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 393, 4), )

    
    stlCreationDate = property(__stlCreationDate.value, __stlCreationDate.set, None, '')

    
    # Element {urn:ebu:tt:metadata}stlRevisionDate uses Python identifier stlRevisionDate
    __stlRevisionDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stlRevisionDate'), 'stlRevisionDate', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatastlRevisionDate', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 398, 4), )

    
    stlRevisionDate = property(__stlRevisionDate.value, __stlRevisionDate.set, None, '')

    
    # Element {urn:ebu:tt:metadata}stlRevisionNumber uses Python identifier stlRevisionNumber
    __stlRevisionNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'stlRevisionNumber'), 'stlRevisionNumber', '__urnebuttmetadata_CTD_ANON_urnebuttmetadatastlRevisionNumber', False, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 403, 4), )

    
    stlRevisionNumber = property(__stlRevisionNumber.value, __stlRevisionNumber.set, None, '')

    _ElementMap.update({
        __conformsToStandard.name() : __conformsToStandard,
        __documentEbuttVersion.name() : __documentEbuttVersion,
        __documentIdentifier.name() : __documentIdentifier,
        __documentOriginatingSystem.name() : __documentOriginatingSystem,
        __documentCopyright.name() : __documentCopyright,
        __documentReadingSpeed.name() : __documentReadingSpeed,
        __documentTargetAspectRatio.name() : __documentTargetAspectRatio,
        __documentTargetActiveFormatDescriptor.name() : __documentTargetActiveFormatDescriptor,
        __documentIntendedTargetBarData.name() : __documentIntendedTargetBarData,
        __documentIntendedTargetFormat.name() : __documentIntendedTargetFormat,
        __documentCreationMode.name() : __documentCreationMode,
        __documentContentType.name() : __documentContentType,
        __relatedMediaIdentifier.name() : __relatedMediaIdentifier,
        __relatedObjectIdentifier.name() : __relatedObjectIdentifier,
        __appliedProcessing.name() : __appliedProcessing,
        __relatedMediaDuration.name() : __relatedMediaDuration,
        __documentBeginDate.name() : __documentBeginDate,
        __localTimeOffset.name() : __localTimeOffset,
        __clockIdentifier.name() : __clockIdentifier,
        __broadcastServiceIdentifier.name() : __broadcastServiceIdentifier,
        __documentOriginalProgrammeTitle.name() : __documentOriginalProgrammeTitle,
        __documentOriginalEpisodeTitle.name() : __documentOriginalEpisodeTitle,
        __documentTranslatedProgrammeTitle.name() : __documentTranslatedProgrammeTitle,
        __documentTranslatedEpisodeTitle.name() : __documentTranslatedEpisodeTitle,
        __documentTranslatorsName.name() : __documentTranslatorsName,
        __documentTranslatorsContactDetails.name() : __documentTranslatorsContactDetails,
        __documentSubtitleListReferenceCode.name() : __documentSubtitleListReferenceCode,
        __documentCreationDate.name() : __documentCreationDate,
        __documentRevisionDate.name() : __documentRevisionDate,
        __documentRevisionNumber.name() : __documentRevisionNumber,
        __documentTotalNumberOfSubtitles.name() : __documentTotalNumberOfSubtitles,
        __documentMaximumNumberOfDisplayableCharacterInAnyRow.name() : __documentMaximumNumberOfDisplayableCharacterInAnyRow,
        __documentStartOfProgramme.name() : __documentStartOfProgramme,
        __documentCountryOfOrigin.name() : __documentCountryOfOrigin,
        __documentPublisher.name() : __documentPublisher,
        __documentEditorsName.name() : __documentEditorsName,
        __documentEditorsContactDetails.name() : __documentEditorsContactDetails,
        __documentUserDefinedArea.name() : __documentUserDefinedArea,
        __stlCreationDate.name() : __stlCreationDate,
        __stlRevisionDate.name() : __stlRevisionDate,
        __stlRevisionNumber.name() : __stlRevisionNumber
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Indicates the subtitle format an author had in mind when
							authoring an EBU-TT document or transforming another format to an EBU-TT
							document."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 206, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute link uses Python identifier link
    __link = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'link'), 'link', '__urnebuttmetadata_CTD_ANON__link', pyxb.binding.datatypes.anyURI)
    __link._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 209, 8)
    __link._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 209, 8)
    
    link = property(__link.value, __link.set, None, 'Reference to a term in a classification\n\t\t\t\t\t\t\t\t\t\t\tscheme.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __link.name() : __link
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 232, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute link uses Python identifier link
    __link = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'link'), 'link', '__urnebuttmetadata_CTD_ANON_2_link', pyxb.binding.datatypes.anyURI)
    __link._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 235, 8)
    __link._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 235, 8)
    
    link = property(__link.value, __link.set, None, 'Reference to a term in a classification\n\t\t\t\t\t\t\t\t\t\t\tscheme.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __link.name() : __link
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 247, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__urnebuttmetadata_CTD_ANON_3_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 248, 6)
    __type._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 248, 6)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })



# Complex type [anonymous] with content type MIXED
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 252, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute appliedDateTime uses Python identifier appliedDateTime
    __appliedDateTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'appliedDateTime'), 'appliedDateTime', '__urnebuttmetadata_CTD_ANON_4_appliedDateTime', pyxb.binding.datatypes.dateTime)
    __appliedDateTime._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 257, 6)
    __appliedDateTime._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 257, 6)
    
    appliedDateTime = property(__appliedDateTime.value, __appliedDateTime.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __appliedDateTime.name() : __appliedDateTime
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 265, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute serviceBegin uses Python identifier serviceBegin
    __serviceBegin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'serviceBegin'), 'serviceBegin', '__urnebuttmetadata_CTD_ANON_5_serviceBegin', pyxb.binding.datatypes.dateTime, required=True)
    __serviceBegin._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 266, 6)
    __serviceBegin._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 266, 6)
    
    serviceBegin = property(__serviceBegin.value, __serviceBegin.set, None, None)

    
    # Attribute serviceEnd uses Python identifier serviceEnd
    __serviceEnd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'serviceEnd'), 'serviceEnd', '__urnebuttmetadata_CTD_ANON_5_serviceEnd', pyxb.binding.datatypes.dateTime, required=True)
    __serviceEnd._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 267, 6)
    __serviceEnd._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 267, 6)
    
    serviceEnd = property(__serviceEnd.value, __serviceEnd.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __serviceBegin.name() : __serviceBegin,
        __serviceEnd.name() : __serviceEnd
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 412, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute link uses Python identifier link
    __link = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'link'), 'link', '__urnebuttmetadata_CTD_ANON_6_link', pyxb.binding.datatypes.anyURI)
    __link._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 415, 5)
    __link._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 415, 5)
    
    link = property(__link.value, __link.set, None, 'Reference to a term in a classification\n\t\t\t\t\t\t\t\tscheme.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __link.name() : __link
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 426, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:ebu:tt:metadata}fontFaceSource uses Python identifier fontFaceSource
    __fontFaceSource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fontFaceSource'), 'fontFaceSource', '__urnebuttmetadata_CTD_ANON_7_urnebuttmetadatafontFaceSource', True, pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 428, 4), )

    
    fontFaceSource = property(__fontFaceSource.value, __fontFaceSource.set, None, None)

    
    # Attribute fontFamilyName uses Python identifier fontFamilyName
    __fontFamilyName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fontFamilyName'), 'fontFamilyName', '__urnebuttmetadata_CTD_ANON_7_fontFamilyName', pyxb.binding.datatypes.anySimpleType)
    __fontFamilyName._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 434, 3)
    __fontFamilyName._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 434, 3)
    
    fontFamilyName = property(__fontFamilyName.value, __fontFamilyName.set, None, None)

    _ElementMap.update({
        __fontFaceSource.name() : __fontFaceSource
    })
    _AttributeMap.update({
        __fontFamilyName.name() : __fontFamilyName
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 429, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute url uses Python identifier url
    __url = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'url'), 'url', '__urnebuttmetadata_CTD_ANON_8_url', pyxb.binding.datatypes.anyURI)
    __url._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 430, 6)
    __url._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 430, 6)
    
    url = property(__url.value, __url.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __url.name() : __url
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Binary data of the input formats or associated documents used to
				generate an EBU-TT document."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 16, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute textEncoding uses Python identifier textEncoding
    __textEncoding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'textEncoding'), 'textEncoding', '__urnebuttmetadata_CTD_ANON_9_textEncoding', STD_ANON, required=True)
    __textEncoding._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 19, 5)
    __textEncoding._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 19, 5)
    
    textEncoding = property(__textEncoding.value, __textEncoding.set, None, 'Text encoding of the binary data.')

    
    # Attribute binaryDataType uses Python identifier binaryDataType
    __binaryDataType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'binaryDataType'), 'binaryDataType', '__urnebuttmetadata_CTD_ANON_9_binaryDataType', pyxb.binding.datatypes.string, required=True)
    __binaryDataType._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 29, 5)
    __binaryDataType._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 29, 5)
    
    binaryDataType = property(__binaryDataType.value, __binaryDataType.set, None, 'Internal format of the binary data.')

    
    # Attribute fileName uses Python identifier fileName
    __fileName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fileName'), 'fileName', '__urnebuttmetadata_CTD_ANON_9_fileName', pyxb.binding.datatypes.string)
    __fileName._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 34, 5)
    __fileName._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 34, 5)
    
    fileName = property(__fileName.value, __fileName.set, None, 'A filename that may be used to identify the original\n\t\t\t\t\t\t\t\tfilename of the tunnelled binary data.')

    
    # Attribute creationDate uses Python identifier creationDate
    __creationDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'creationDate'), 'creationDate', '__urnebuttmetadata_CTD_ANON_9_creationDate', pyxb.binding.datatypes.date)
    __creationDate._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 40, 5)
    __creationDate._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 40, 5)
    
    creationDate = property(__creationDate.value, __creationDate.set, None, '')

    
    # Attribute revisionDate uses Python identifier revisionDate
    __revisionDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'revisionDate'), 'revisionDate', '__urnebuttmetadata_CTD_ANON_9_revisionDate', pyxb.binding.datatypes.date)
    __revisionDate._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 45, 5)
    __revisionDate._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 45, 5)
    
    revisionDate = property(__revisionDate.value, __revisionDate.set, None, '')

    
    # Attribute revisionNumber uses Python identifier revisionNumber
    __revisionNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'revisionNumber'), 'revisionNumber', '__urnebuttmetadata_CTD_ANON_9_revisionNumber', pyxb.binding.datatypes.nonNegativeInteger)
    __revisionNumber._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 50, 5)
    __revisionNumber._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 50, 5)
    
    revisionNumber = property(__revisionNumber.value, __revisionNumber.set, None, '')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __textEncoding.name() : __textEncoding,
        __binaryDataType.name() : __binaryDataType,
        __fileName.name() : __fileName,
        __creationDate.name() : __creationDate,
        __revisionDate.name() : __revisionDate,
        __revisionNumber.name() : __revisionNumber
    })



# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """When an ebuttm:documentTargetActiveFormatDescriptor
							element is used in an EBU-TT document, an
							ebuttm:documentIntendedTargetBarData element may be used whenever the
							AFD alone is insufficient to describe the extent of the image (i.e. AFD
							values 0000 and 0100). The Bar Data shall be specified in accordance
							with SMPTE ST 2016 1:2009 “Format for Active Format Description and Bar
							Data” Table 3."""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 133, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute position uses Python identifier position
    __position = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'position'), 'position', '__urnebuttmetadata_CTD_ANON_10_position', STD_ANON_2, required=True)
    __position._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 136, 8)
    __position._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 136, 8)
    
    position = property(__position.value, __position.set, None, 'Bar Data is defined in pairs, either top\n\t\t\t\t\t\t\t\t\t\t\tand bottom bars or left and right bars, but not both\n\t\t\t\t\t\t\t\t\t\t\tpairs at once. Bars may be unequal in size. One bar of a\n\t\t\t\t\t\t\t\t\t\t\tpair may be zero width or height.')

    
    # Attribute lineNumberEndOfTopBar uses Python identifier lineNumberEndOfTopBar
    __lineNumberEndOfTopBar = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lineNumberEndOfTopBar'), 'lineNumberEndOfTopBar', '__urnebuttmetadata_CTD_ANON_10_lineNumberEndOfTopBar', pyxb.binding.datatypes.nonNegativeInteger)
    __lineNumberEndOfTopBar._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 150, 8)
    __lineNumberEndOfTopBar._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 150, 8)
    
    lineNumberEndOfTopBar = property(__lineNumberEndOfTopBar.value, __lineNumberEndOfTopBar.set, None, 'Last line of a horizontal letter box bar\n\t\t\t\t\t\t\t\t\t\t\tarea at the top of the reconstructed frame. Designation\n\t\t\t\t\t\t\t\t\t\t\tof line numbers shall be based on the video standards\n\t\t\t\t\t\t\t\t\t\t\tand information specified in accordance with SMPTE ST\n\t\t\t\t\t\t\t\t\t\t\t2016 1:2009. All Bar Data values shall be stated in\n\t\t\t\t\t\t\t\t\t\t\tvalues appropriate to a progressive frame\n\t\t\t\t\t\t\t\t\t\t\tsystem.')

    
    # Attribute lineNumberStartOfBottomBar uses Python identifier lineNumberStartOfBottomBar
    __lineNumberStartOfBottomBar = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lineNumberStartOfBottomBar'), 'lineNumberStartOfBottomBar', '__urnebuttmetadata_CTD_ANON_10_lineNumberStartOfBottomBar', pyxb.binding.datatypes.nonNegativeInteger)
    __lineNumberStartOfBottomBar._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 162, 8)
    __lineNumberStartOfBottomBar._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 162, 8)
    
    lineNumberStartOfBottomBar = property(__lineNumberStartOfBottomBar.value, __lineNumberStartOfBottomBar.set, None, 'First line of a horizontal letter box bar\n\t\t\t\t\t\t\t\t\t\t\tarea at the bottom of the reconstructed frame.\n\t\t\t\t\t\t\t\t\t\t\tDesignation of line numbers shall be based on the video\n\t\t\t\t\t\t\t\t\t\t\tstandards and information specified in accordance with\n\t\t\t\t\t\t\t\t\t\t\tSMPTE ST 2016 1:2009. All Bar Data values shall be\n\t\t\t\t\t\t\t\t\t\t\tstated in values appropriate to a progressive frame\n\t\t\t\t\t\t\t\t\t\t\tsystem.')

    
    # Attribute pixelNumberEndOfLeftBar uses Python identifier pixelNumberEndOfLeftBar
    __pixelNumberEndOfLeftBar = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'pixelNumberEndOfLeftBar'), 'pixelNumberEndOfLeftBar', '__urnebuttmetadata_CTD_ANON_10_pixelNumberEndOfLeftBar', pyxb.binding.datatypes.nonNegativeInteger)
    __pixelNumberEndOfLeftBar._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 174, 8)
    __pixelNumberEndOfLeftBar._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 174, 8)
    
    pixelNumberEndOfLeftBar = property(__pixelNumberEndOfLeftBar.value, __pixelNumberEndOfLeftBar.set, None, 'Last horizontal luminance sample of a\n\t\t\t\t\t\t\t\t\t\t\tvertical pillar box bar area at the left side of the\n\t\t\t\t\t\t\t\t\t\t\treconstructed frame. Pixels shall be numbered from zero,\n\t\t\t\t\t\t\t\t\t\t\tstarting with the leftmost pixel, based on the video\n\t\t\t\t\t\t\t\t\t\t\tstandards and information specified in accordance with\n\t\t\t\t\t\t\t\t\t\t\tSMPTE ST 2016 1:2009.')

    
    # Attribute pixelNumberStartOfRightBar uses Python identifier pixelNumberStartOfRightBar
    __pixelNumberStartOfRightBar = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'pixelNumberStartOfRightBar'), 'pixelNumberStartOfRightBar', '__urnebuttmetadata_CTD_ANON_10_pixelNumberStartOfRightBar', pyxb.binding.datatypes.nonNegativeInteger)
    __pixelNumberStartOfRightBar._DeclarationLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 185, 8)
    __pixelNumberStartOfRightBar._UseLocation = pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 185, 8)
    
    pixelNumberStartOfRightBar = property(__pixelNumberStartOfRightBar.value, __pixelNumberStartOfRightBar.set, None, 'First horizontal luminance sample of a\n\t\t\t\t\t\t\t\t\t\t\tvertical pillar box bar area at the right side of the\n\t\t\t\t\t\t\t\t\t\t\treconstructed frame. Pixels shall be numbered from zero,\n\t\t\t\t\t\t\t\t\t\t\tstarting with the leftmost pixel, based on the video\n\t\t\t\t\t\t\t\t\t\t\tstandards and information specified in accordance with\n\t\t\t\t\t\t\t\t\t\t\tSMPTE ST 2016 1:2009.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __position.name() : __position,
        __lineNumberEndOfTopBar.name() : __lineNumberEndOfTopBar,
        __lineNumberStartOfBottomBar.name() : __lineNumberStartOfBottomBar,
        __pixelNumberEndOfLeftBar.name() : __pixelNumberEndOfLeftBar,
        __pixelNumberStartOfRightBar.name() : __pixelNumberStartOfRightBar
    })



documentMetadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentMetadata'), CTD_ANON, documentation='EBU-TT specific metadata that applies to the whole EBU-TT\n\t\t\t\tdocument.', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 59, 1))
Namespace.addCategoryObject('elementBinding', documentMetadata.name().localName(), documentMetadata)

authoringTechnique = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'authoringTechnique'), CTD_ANON_6, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 411, 1))
Namespace.addCategoryObject('elementBinding', authoringTechnique.name().localName(), authoringTechnique)

fontFace = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fontFace'), CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 425, 1))
Namespace.addCategoryObject('elementBinding', fontFace.name().localName(), fontFace)

binaryData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'binaryData'), CTD_ANON_9, documentation='Binary data of the input formats or associated documents used to\n\t\t\t\tgenerate an EBU-TT document.', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 11, 1))
Namespace.addCategoryObject('elementBinding', binaryData.name().localName(), binaryData)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'conformsToStandard'), pyxb.binding.datatypes.anyURI, scope=CTD_ANON, documentation='Indicates the conformance with a specific standard that is\n\t\t\t\t\t\t\tderived from TTML.', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 66, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentEbuttVersion'), STD_ANON_, scope=CTD_ANON, documentation='The version of the EBU-TT standard used by the document\n\t\t\t\t\t\t\tinstance.', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 73, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentIdentifier'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='Identifier for an EBU-TT document that may be used as\n\t\t\t\t\t\t\texternal reference to an EBU-TT document.', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 84, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentOriginatingSystem'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='Software and version used to create the EBU-TT\n\t\t\t\t\t\t\tdocument.', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 90, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentCopyright'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='The copyright of the document.', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 96, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentReadingSpeed'), pyxb.binding.datatypes.positiveInteger, scope=CTD_ANON, documentation='The intended reading speed for the subtitles in words per\n\t\t\t\t\t\t\tminute.', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 101, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentTargetAspectRatio'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='The aspect ratio of the video the EBU-TT document was\n\t\t\t\t\t\t\tauthored for, in width by height.', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 107, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentTargetActiveFormatDescriptor'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='The code for the Active Format Descriptor (AFD) that\n\t\t\t\t\t\t\tspecifies the active image in the active video (see \u201cDefinitions of\n\t\t\t\t\t\t\tterms\u201d). The code shall be one of the AFD codes specified in SMPTE ST\n\t\t\t\t\t\t\t2016 1:2009 \u201cFormat for Active Format Description and Bar Data\u201d Table\n\t\t\t\t\t\t\t1.', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 113, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentIntendedTargetBarData'), CTD_ANON_10, scope=CTD_ANON, documentation='When an ebuttm:documentTargetActiveFormatDescriptor\n\t\t\t\t\t\t\telement is used in an EBU-TT document, an\n\t\t\t\t\t\t\tebuttm:documentIntendedTargetBarData element may be used whenever the\n\t\t\t\t\t\t\tAFD alone is insufficient to describe the extent of the image (i.e. AFD\n\t\t\t\t\t\t\tvalues 0000 and 0100). The Bar Data shall be specified in accordance\n\t\t\t\t\t\t\twith SMPTE ST 2016 1:2009 \u201cFormat for Active Format Description and Bar\n\t\t\t\t\t\t\tData\u201d Table 3.', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 123, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentIntendedTargetFormat'), CTD_ANON_, scope=CTD_ANON, documentation='Indicates the subtitle format an author had in mind when\n\t\t\t\t\t\t\tauthoring an EBU-TT document or transforming another format to an EBU-TT\n\t\t\t\t\t\t\tdocument.', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 200, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentCreationMode'), STD_ANON_3, scope=CTD_ANON, documentation='Identifies the overall workflow used to create the content\n\t\t\t\t\t\t\tin the document.', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 219, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentContentType'), CTD_ANON_2, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 231, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relatedMediaIdentifier '), pyxb.binding.datatypes.anyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 245, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relatedObjectIdentifier'), CTD_ANON_3, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 246, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'appliedProcessing'), CTD_ANON_4, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 251, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relatedMediaDuration'), _ImportedBinding__ebuttdt.mediaTimingType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 260, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentBeginDate'), pyxb.binding.datatypes.date, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 261, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'localTimeOffset'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 262, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'clockIdentifier'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 263, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcastServiceIdentifier'), CTD_ANON_5, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 264, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentOriginalProgrammeTitle'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='The programme title in the original language. STL mapping:\n\t\t\t\t\t\t\tOriginal Programme Title (OPT).', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 270, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentOriginalEpisodeTitle'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='The title of the episode of the programme in the original\n\t\t\t\t\t\t\tlanguage. STL mapping: Original Episode Title (OET).', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 276, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatedProgrammeTitle'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='The programme title in the local language. STL mapping:\n\t\t\t\t\t\t\tTranslated Programme Title (TPT).', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 282, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatedEpisodeTitle'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='The title of the episode of the programme in the local\n\t\t\t\t\t\t\tlanguage. STL mapping: Translated Episode Title\n\t\t\t\t\t\t\t(TET).', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 288, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatorsName'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation="Name of the translator. STL mapping: Translator's Name\n\t\t\t\t\t\t\t(TN). ", location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 295, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatorsContactDetails'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation="The translator's contact details. STL mapping:\n\t\t\t\t\t\t\tTranslator's Contact Details (TCD).", location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 301, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentSubtitleListReferenceCode'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='Free-format character string which may be used to provide\n\t\t\t\t\t\t\tan additional reference for the subtitle list. Note: This attribute is\n\t\t\t\t\t\t\tprovided to support conversion of STL subtitle files and to retain the\n\t\t\t\t\t\t\tmetadata from the GSI block. STL mapping: Subtitle List Reference Code\n\t\t\t\t\t\t\t(SLR)', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 307, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentCreationDate'), pyxb.binding.datatypes.date, scope=CTD_ANON, documentation='The date of creation of the EBU-TT document.\n\t\t\t\t\t\t', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 316, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentRevisionDate'), pyxb.binding.datatypes.date, scope=CTD_ANON, documentation='The date of the most-recent modifications to the EBU-TT\n\t\t\t\t\t\t\tdocument. ', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 322, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentRevisionNumber'), pyxb.binding.datatypes.nonNegativeInteger, scope=CTD_ANON, documentation='The revision number of the EBU-TT document may be used to\n\t\t\t\t\t\t\tspecify a particular version of the subtitle list. ', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 328, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentTotalNumberOfSubtitles'), pyxb.binding.datatypes.nonNegativeInteger, scope=CTD_ANON, documentation='The number of subtitles. STL mapping: Total Number of\n\t\t\t\t\t\t\tSubtitles (TNS).', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 334, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentMaximumNumberOfDisplayableCharacterInAnyRow'), pyxb.binding.datatypes.nonNegativeInteger, scope=CTD_ANON, documentation='Maximum number of displayable rows per television frame\n\t\t\t\t\t\t\twhich could be occupied at any one time by the subtitles defined in the\n\t\t\t\t\t\t\tTTI blocks. STL mapping: Maximum Number of Displayable Characters in any\n\t\t\t\t\t\t\ttext row (MNC). ', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 341, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentStartOfProgramme'), _ImportedBinding__ebuttdt.smpteTimingType, scope=CTD_ANON, documentation='The time code of the first frame of the recorded video\n\t\t\t\t\t\t\tsignal which is intended for transmission. Note: When the referenced\n\t\t\t\t\t\t\tstart timecode of the video material the subtitles were authored for is\n\t\t\t\t\t\t\tgreater than 00:00:00:00 (e.g. 10:00:00:00) it is recommended to specify\n\t\t\t\t\t\t\tthe attribute ebuttm:documentStartOfPrograme. STL mapping: Timecode:\n\t\t\t\t\t\t\tStart-of-Programme (TCP).', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 350, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentCountryOfOrigin'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='The country of origin of the subtitle list. STL mapping:\n\t\t\t\t\t\t\tCountry of Origin (CO). ', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 361, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentPublisher'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='Name of the publisher of the subtitle list. STL mapping:\n\t\t\t\t\t\t\tPublisher (PUB).', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 367, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentEditorsName'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation="Name of the editor of the subtitle list. STL mapping:\n\t\t\t\t\t\t\tEditor's Name (EN).", location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 373, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentEditorsContactDetails'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation="Information about the editor named in the metadata element\n\t\t\t\t\t\t\tdocumentEditorsName. STL mapping: Editor's Contact Details (ECD).\n\t\t\t\t\t\t", location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 379, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentUserDefinedArea'), pyxb.binding.datatypes.string, scope=CTD_ANON, documentation='This field may be used to carry information about the\n\t\t\t\t\t\t\tprogramme or subtitle list, or other relevant details. STL mapping:\n\t\t\t\t\t\t\tUser-Defined Area (UDA).', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 386, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stlCreationDate'), pyxb.binding.datatypes.date, scope=CTD_ANON, documentation='', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 393, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stlRevisionDate'), pyxb.binding.datatypes.date, scope=CTD_ANON, documentation='', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 398, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stlRevisionNumber'), pyxb.binding.datatypes.nonNegativeInteger, scope=CTD_ANON, documentation='', location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 403, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 66, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 73, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 84, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 90, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 96, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 101, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 107, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 113, 4))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 123, 4))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 200, 4))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 219, 4))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 231, 4))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 245, 4))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 246, 4))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 260, 4))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 261, 4))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 262, 4))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 263, 4))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 264, 4))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 270, 4))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 276, 4))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 282, 4))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 288, 4))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 295, 4))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 301, 4))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 307, 4))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 316, 4))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 322, 4))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 328, 4))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 334, 4))
    counters.add(cc_29)
    cc_30 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 341, 4))
    counters.add(cc_30)
    cc_31 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 350, 4))
    counters.add(cc_31)
    cc_32 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 361, 4))
    counters.add(cc_32)
    cc_33 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 367, 4))
    counters.add(cc_33)
    cc_34 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 373, 4))
    counters.add(cc_34)
    cc_35 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 379, 4))
    counters.add(cc_35)
    cc_36 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 386, 4))
    counters.add(cc_36)
    cc_37 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 393, 4))
    counters.add(cc_37)
    cc_38 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 398, 4))
    counters.add(cc_38)
    cc_39 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 403, 4))
    counters.add(cc_39)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'conformsToStandard')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 66, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentEbuttVersion')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 73, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentIdentifier')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 84, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentOriginatingSystem')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 90, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentCopyright')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 96, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentReadingSpeed')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 101, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentTargetAspectRatio')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 107, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentTargetActiveFormatDescriptor')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 113, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentIntendedTargetBarData')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 123, 4))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentIntendedTargetFormat')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 200, 4))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentCreationMode')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 219, 4))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentContentType')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 231, 4))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relatedMediaIdentifier ')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 245, 4))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relatedObjectIdentifier')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 246, 4))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'appliedProcessing')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 251, 4))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relatedMediaDuration')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 260, 4))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentBeginDate')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 261, 4))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'localTimeOffset')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 262, 4))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'clockIdentifier')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 263, 4))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcastServiceIdentifier')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 264, 4))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentOriginalProgrammeTitle')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 270, 4))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentOriginalEpisodeTitle')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 276, 4))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatedProgrammeTitle')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 282, 4))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatedEpisodeTitle')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 288, 4))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatorsName')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 295, 4))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentTranslatorsContactDetails')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 301, 4))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentSubtitleListReferenceCode')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 307, 4))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_26, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentCreationDate')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 316, 4))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_27, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentRevisionDate')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 322, 4))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_28, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentRevisionNumber')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 328, 4))
    st_29 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_29, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentTotalNumberOfSubtitles')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 334, 4))
    st_30 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_30, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentMaximumNumberOfDisplayableCharacterInAnyRow')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 341, 4))
    st_31 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_31, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentStartOfProgramme')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 350, 4))
    st_32 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_32, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentCountryOfOrigin')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 361, 4))
    st_33 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_33, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentPublisher')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 367, 4))
    st_34 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_34, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentEditorsName')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 373, 4))
    st_35 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_35)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_35, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentEditorsContactDetails')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 379, 4))
    st_36 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_36)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_36, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentUserDefinedArea')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 386, 4))
    st_37 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_37)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_37, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stlCreationDate')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 393, 4))
    st_38 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_38)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_38, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stlRevisionDate')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 398, 4))
    st_39 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_39)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_39, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'stlRevisionNumber')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 403, 4))
    st_40 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_40)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    transitions.append(fac.Transition(st_23, [
         ]))
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    transitions.append(fac.Transition(st_30, [
         ]))
    transitions.append(fac.Transition(st_31, [
         ]))
    transitions.append(fac.Transition(st_32, [
         ]))
    transitions.append(fac.Transition(st_33, [
         ]))
    transitions.append(fac.Transition(st_34, [
         ]))
    transitions.append(fac.Transition(st_35, [
         ]))
    transitions.append(fac.Transition(st_36, [
         ]))
    transitions.append(fac.Transition(st_37, [
         ]))
    transitions.append(fac.Transition(st_38, [
         ]))
    transitions.append(fac.Transition(st_39, [
         ]))
    transitions.append(fac.Transition(st_40, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_28, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_29, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_29, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_30, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_30, False) ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_31, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_31, False) ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_32, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_32, False) ]))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_33, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_33, False) ]))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_34, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_34, False) ]))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_35, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_35, False) ]))
    st_36._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_36, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_36, False) ]))
    st_37._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_37, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_37, False) ]))
    st_38._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_38, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_38, False) ]))
    st_39._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_39, True) ]))
    st_40._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 254, 7))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:ebu:tt:metadata')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 254, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_()




CTD_ANON_7._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fontFaceSource'), CTD_ANON_8, scope=CTD_ANON_7, location=pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 428, 4)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_7._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fontFaceSource')), pyxb.utils.utility.Location('/Users/kozmaz01/Projects/ebu-tt-live-toolkit/ebu_tt_live/xsd/ebutt_metadata.xsd', 428, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_2()

