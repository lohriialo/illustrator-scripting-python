# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)]
# From type library 'ScriptingSupport.aip'
# On Wed Jun 20 00:19:05 2018
'Adobe Illustrator 21 Type Library'
makepy_version = '0.5.01'
python_version = 0x30601f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{3271C7D8-D207-4C7C-B2B4-7F3DA9D1A8F9}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class constants:
	aiDefaultForm                 =0          # from enum AiAlternateGlyphsForm
	aiExpert                      =2          # from enum AiAlternateGlyphsForm
	aiFullWidth                   =8          # from enum AiAlternateGlyphsForm
	aiHalfWidth                   =5          # from enum AiAlternateGlyphsForm
	aiJIS04Form                   =11         # from enum AiAlternateGlyphsForm
	aiJIS78Form                   =3          # from enum AiAlternateGlyphsForm
	aiJIS83Form                   =4          # from enum AiAlternateGlyphsForm
	aiJIS90Form                   =10         # from enum AiAlternateGlyphsForm
	aiProportionalWidth           =9          # from enum AiAlternateGlyphsForm
	aiQuarterWidth                =7          # from enum AiAlternateGlyphsForm
	aiThirdWidth                  =6          # from enum AiAlternateGlyphsForm
	aiTraditional                 =1          # from enum AiAlternateGlyphsForm
	aiArtOptimized                =1          # from enum AiAntiAliasingMethod
	aiNoAntiAliasing              =0          # from enum AiAntiAliasingMethod
	aiTypeOptimized               =2          # from enum AiAntiAliasingMethod
	aiOutputArtBounds             =1          # from enum AiArtClippingOption
	aiOutputArtboardBounds        =2          # from enum AiArtClippingOption
	aiOutputCropRectBounds        =3          # from enum AiArtClippingOption
	aiMax16Colors                 =1          # from enum AiAutoCADColors
	aiMax256Colors                =2          # from enum AiAutoCADColors
	aiMax8Colors                  =0          # from enum AiAutoCADColors
	aiTrueColors                  =3          # from enum AiAutoCADColors
	aiAutoCADRelease13            =0          # from enum AiAutoCADCompatibility
	aiAutoCADRelease14            =1          # from enum AiAutoCADCompatibility
	aiAutoCADRelease15            =2          # from enum AiAutoCADCompatibility
	aiAutoCADRelease18            =3          # from enum AiAutoCADCompatibility
	aiAutoCADRelease21            =4          # from enum AiAutoCADCompatibility
	aiAutoCADRelease24            =5          # from enum AiAutoCADCompatibility
	aiDWG                         =1          # from enum AiAutoCADExportFileFormat
	aiDXF                         =0          # from enum AiAutoCADExportFileFormat
	aiMaintainAppearance          =0          # from enum AiAutoCADExportOption
	aiMaximumEditability          =1          # from enum AiAutoCADExportOption
	aiFitArtboard                 =1          # from enum AiAutoCADGlobalScaleOption
	aiOriginalSize                =0          # from enum AiAutoCADGlobalScaleOption
	aiScaleByValue                =2          # from enum AiAutoCADGlobalScaleOption
	aiRasterJPEG                  =1          # from enum AiAutoCADRasterFormat
	aiRasterPNG                   =0          # from enum AiAutoCADRasterFormat
	aiCentimeters                 =4          # from enum AiAutoCADUnit
	aiInches                      =2          # from enum AiAutoCADUnit
	aiMillimeters                 =3          # from enum AiAutoCADUnit
	aiPicas                       =1          # from enum AiAutoCADUnit
	aiPixels                      =5          # from enum AiAutoCADUnit
	aiPoints                      =0          # from enum AiAutoCADUnit
	aiAuto                        =1          # from enum AiAutoKernType
	aiMetricsRomanOnly            =3          # from enum AiAutoKernType
	aiNoAutoKern                  =0          # from enum AiAutoKernType
	aiOptical                     =2          # from enum AiAutoKernType
	aiBottomToBottom              =0          # from enum AiAutoLeadingType
	aiTopToTop                    =1          # from enum AiAutoLeadingType
	aiStandardBaseline            =1          # from enum AiBaselineDirectionType
	aiTateChuYokoBaseline         =3          # from enum AiBaselineDirectionType
	aiVerticalRotatedBaseline     =2          # from enum AiBaselineDirectionType
	aiInBuild                     =2          # from enum AiBlendAnimationType
	aiInSequence                  =1          # from enum AiBlendAnimationType
	aiNoBlendAnimation            =0          # from enum AiBlendAnimationType
	aiColorBlend                  =14         # from enum AiBlendModes
	aiColorBurn                   =7          # from enum AiBlendModes
	aiColorDodge                  =6          # from enum AiBlendModes
	aiDarken                      =8          # from enum AiBlendModes
	aiDifference                  =10         # from enum AiBlendModes
	aiExclusion                   =11         # from enum AiBlendModes
	aiHardLight                   =5          # from enum AiBlendModes
	aiHue                         =12         # from enum AiBlendModes
	aiLighten                     =9          # from enum AiBlendModes
	aiLuminosity                  =15         # from enum AiBlendModes
	aiMultiply                    =1          # from enum AiBlendModes
	aiNormalBlend                 =0          # from enum AiBlendModes
	aiOverlay                     =3          # from enum AiBlendModes
	aiSaturationBlend             =13         # from enum AiBlendModes
	aiScreen                      =2          # from enum AiBlendModes
	aiSoftLight                   =4          # from enum AiBlendModes
	aiAutomaticallyConvertBlends  =1          # from enum AiBlendsExpandPolicy
	aiRasterizeBlends             =2          # from enum AiBlendsExpandPolicy
	aiBurasagariForced            =2          # from enum AiBurasagariTypeEnum
	aiBurasagariNone              =0          # from enum AiBurasagariTypeEnum
	aiBurasagariStandard          =1          # from enum AiBurasagariTypeEnum
	aiLowerCase                   =1          # from enum AiCaseChangeType
	aiSentenceCase                =3          # from enum AiCaseChangeType
	aiTitleCase                   =2          # from enum AiCaseChangeType
	aiUpperCase                   =0          # from enum AiCaseChangeType
	aiKumiMoji                    =3          # from enum AiCharacterDirection
	aiNormal                      =1          # from enum AiCharacterDirection
	aiRotated                     =2          # from enum AiCharacterDirection
	aiColorCMYK                   =1          # from enum AiColor
	aiColorGradient               =6          # from enum AiColor
	aiColorGray                   =2          # from enum AiColor
	aiColorNone                   =0          # from enum AiColor
	aiColorPattern                =5          # from enum AiColor
	aiColorRGB                    =3          # from enum AiColor
	aiColorSpot                   =4          # from enum AiColor
	aiColorConversionRepurpose    =2          # from enum AiColorConversion
	aiColorConversionToDest       =1          # from enum AiColorConversion
	aiNoColorConversion           =0          # from enum AiColorConversion
	aiDefaultPurpose              =0          # from enum AiColorConvertPurpose
	aiDummyPurpose                =4          # from enum AiColorConvertPurpose
	aiForExportPurpose            =2          # from enum AiColorConvertPurpose
	aiForPreviewPurpose           =1          # from enum AiColorConvertPurpose
	aiColorDestinationDocCMYK     =1          # from enum AiColorDestination
	aiColorDestinationDocRGB      =3          # from enum AiColorDestination
	aiColorDestinationProfile     =5          # from enum AiColorDestination
	aiColorDestinationWorkingCMYK =2          # from enum AiColorDestination
	aiColorDestinationWorkingRGB  =4          # from enum AiColorDestination
	aiNoDestination               =0          # from enum AiColorDestination
	aiDiffusion                   =1147564910 # from enum AiColorDitherMethod
	aiNoReduction                 =1315925605 # from enum AiColorDitherMethod
	aiNoise                       =1112436585 # from enum AiColorDitherMethod
	aiPatternDither               =1349808750 # from enum AiColorDitherMethod
	aiProcess                     =1          # from enum AiColorModel
	aiRegistration                =0          # from enum AiColorModel
	aiSpot                        =2          # from enum AiColorModel
	aiDontIncludeProfile          =0          # from enum AiColorProfile
	aiIncludeAllProfile           =1          # from enum AiColorProfile
	aiIncludeDestProfile          =4          # from enum AiColorProfile
	aiIncludeRGBProfile           =3          # from enum AiColorProfile
	aiLeaveProfileUnchanged       =2          # from enum AiColorProfile
	aiAdaptive                    =1097101428 # from enum AiColorReductionMethod
	aiPerceptual                  =1349673840 # from enum AiColorReductionMethod
	aiSelective                   =1399616630 # from enum AiColorReductionMethod
	aiWeb                         =1466262048 # from enum AiColorReductionMethod
	aiIllustrator10               =10         # from enum AiCompatibility
	aiIllustrator11               =11         # from enum AiCompatibility
	aiIllustrator12               =12         # from enum AiCompatibility
	aiIllustrator13               =13         # from enum AiCompatibility
	aiIllustrator14               =14         # from enum AiCompatibility
	aiIllustrator15               =15         # from enum AiCompatibility
	aiIllustrator16               =16         # from enum AiCompatibility
	aiIllustrator17               =17         # from enum AiCompatibility
	aiIllustrator3                =3          # from enum AiCompatibility
	aiIllustrator8                =8          # from enum AiCompatibility
	aiIllustrator9                =9          # from enum AiCompatibility
	aiJapaneseVersion3            =3          # from enum AiCompatibility
	aiAutomaticJPEG2000High       =18         # from enum AiCompressionQuality
	aiAutomaticJPEG2000Lossless   =20         # from enum AiCompressionQuality
	aiAutomaticJPEG2000Low        =16         # from enum AiCompressionQuality
	aiAutomaticJPEG2000Maximum    =19         # from enum AiCompressionQuality
	aiAutomaticJPEG2000Medium     =17         # from enum AiCompressionQuality
	aiAutomaticJPEG2000Minimum    =15         # from enum AiCompressionQuality
	aiAutomaticJPEGHigh           =13         # from enum AiCompressionQuality
	aiAutomaticJPEGLow            =11         # from enum AiCompressionQuality
	aiAutomaticJPEGMaximum        =14         # from enum AiCompressionQuality
	aiAutomaticJPEGMedium         =12         # from enum AiCompressionQuality
	aiAutomaticJPEGMinimum        =10         # from enum AiCompressionQuality
	aiJPEG2000High                =24         # from enum AiCompressionQuality
	aiJPEG2000Lossless            =26         # from enum AiCompressionQuality
	aiJPEG2000Low                 =22         # from enum AiCompressionQuality
	aiJPEG2000Maximum             =25         # from enum AiCompressionQuality
	aiJPEG2000Medium              =23         # from enum AiCompressionQuality
	aiJPEG2000Minimum             =21         # from enum AiCompressionQuality
	aiJPEGHigh                    =6          # from enum AiCompressionQuality
	aiJPEGLow                     =4          # from enum AiCompressionQuality
	aiJPEGMaximum                 =7          # from enum AiCompressionQuality
	aiJPEGMedium                  =5          # from enum AiCompressionQuality
	aiJPEGMinimum                 =3          # from enum AiCompressionQuality
	aiNoCompression               =1          # from enum AiCompressionQuality
	aiZIP4Bit                     =8          # from enum AiCompressionQuality
	aiZIP8Bit                     =9          # from enum AiCompressionQuality
	aiArtboardCoordinateSystem    =1          # from enum AiCoordinateSystem
	aiDocumentCoordinateSystem    =0          # from enum AiCoordinateSystem
	aiCropJapanese                =2          # from enum AiCropOptions
	aiCropStandard                =1          # from enum AiCropOptions
	aiColumn                      =4          # from enum AiDocumentArtboardLayout
	aiGridByCol                   =2          # from enum AiDocumentArtboardLayout
	aiGridByRow                   =1          # from enum AiDocumentArtboardLayout
	aiRLGridByCol                 =6          # from enum AiDocumentArtboardLayout
	aiRLGridByRow                 =5          # from enum AiDocumentArtboardLayout
	aiRLRow                       =7          # from enum AiDocumentArtboardLayout
	aiRow                         =3          # from enum AiDocumentArtboardLayout
	aiDocumentCMYKColor           =2          # from enum AiDocumentColorSpace
	aiDocumentRGBColor            =1          # from enum AiDocumentColorSpace
	aiCascade                     =0          # from enum AiDocumentLayoutStyle
	aiConsolidateAll              =4          # from enum AiDocumentLayoutStyle
	aiFloatAll                    =3          # from enum AiDocumentLayoutStyle
	aiHorizontalTile              =1          # from enum AiDocumentLayoutStyle
	aiVerticalTile                =2          # from enum AiDocumentLayoutStyle
	aiBasicCMYKPreset             =5          # from enum AiDocumentPresetType
	aiBasicRGBPreset              =6          # from enum AiDocumentPresetType
	aiMobilePreset                =3          # from enum AiDocumentPresetType
	aiPrintPreset                 =1          # from enum AiDocumentPresetType
	aiVideoPreset                 =4          # from enum AiDocumentPresetType
	aiWebPreset                   =2          # from enum AiDocumentPresetType
	aiDefaultPreview              =1          # from enum AiDocumentPreviewMode
	aiOverprintPreview            =3          # from enum AiDocumentPreviewMode
	aiPixelPreview                =2          # from enum AiDocumentPreviewMode
	aiHighResolution              =3          # from enum AiDocumentRasterResolution
	aiMediumResolution            =2          # from enum AiDocumentRasterResolution
	aiScreenResolution            =1          # from enum AiDocumentRasterResolution
	aiTransparencyGridBlue        =7          # from enum AiDocumentTransparencyGrid
	aiTransparencyGridDark        =3          # from enum AiDocumentTransparencyGrid
	aiTransparencyGridGreen       =6          # from enum AiDocumentTransparencyGrid
	aiTransparencyGridLight       =1          # from enum AiDocumentTransparencyGrid
	aiTransparencyGridMedium      =2          # from enum AiDocumentTransparencyGrid
	aiTransparencyGridNone        =0          # from enum AiDocumentTransparencyGrid
	aiTransparencyGridOrange      =5          # from enum AiDocumentTransparencyGrid
	aiTransparencyGridPurple      =8          # from enum AiDocumentTransparencyGrid
	aiTransparencyGridRed         =4          # from enum AiDocumentTransparencyGrid
	aiEPS                         =2          # from enum AiDocumentType
	aiFXG                         =4          # from enum AiDocumentType
	aiIllustrator                 =1          # from enum AiDocumentType
	aiPDF                         =3          # from enum AiDocumentType
	aiAverageDownsample           =1          # from enum AiDownsampleMethod
	aiBicubicDownsample           =3          # from enum AiDownsampleMethod
	aiNoDownsample                =0          # from enum AiDownsampleMethod
	aiSubsample                   =2          # from enum AiDownsampleMethod
	aiLevel2                      =2          # from enum AiEPSPostScriptLevelEnum
	aiLevel3                      =3          # from enum AiEPSPostScriptLevelEnum
	aiBWMacintosh                 =2          # from enum AiEPSPreview
	aiBWTIFF                      =4          # from enum AiEPSPreview
	aiColorMacintosh              =3          # from enum AiEPSPreview
	aiColorTIFF                   =6          # from enum AiEPSPreview
	aiNoPreview                   =1          # from enum AiEPSPreview
	aiTransparentColorTIFF        =5          # from enum AiEPSPreview
	aiPlaceAfter                  =4          # from enum AiElementPlacement
	aiPlaceAtBeginning            =1          # from enum AiElementPlacement
	aiPlaceAtEnd                  =2          # from enum AiElementPlacement
	aiPlaceBefore                 =3          # from enum AiElementPlacement
	aiPlaceInside                 =0          # from enum AiElementPlacement
	aiAutoCAD                     =8          # from enum AiExportType
	aiFlash                       =7          # from enum AiExportType
	aiGIF                         =6          # from enum AiExportType
	aiJPEG                        =1          # from enum AiExportType
	aiPNG24                       =5          # from enum AiExportType
	aiPNG8                        =4          # from enum AiExportType
	aiPhotoshop                   =2          # from enum AiExportType
	aiSVG                         =3          # from enum AiExportType
	aiTIFF                        =9          # from enum AiExportType
	aiWOSVG                       =10         # from enum AiExportType
	aiVersion1Pt0                 =1          # from enum AiFXGVersion
	aiVersion2Pt0                 =2          # from enum AiFXGVersion
	aiDefaultFigureStyle          =0          # from enum AiFigureStyleType
	aiProportional                =3          # from enum AiFigureStyleType
	aiProportionalOldStyle        =2          # from enum AiFigureStyleType
	aiTabular                     =1          # from enum AiFigureStyleType
	aiTabularOldStyle             =4          # from enum AiFigureStyleType
	aiExpandFilters               =1          # from enum AiFiltersPreservePolicy
	aiKeepFiltersEditable         =3          # from enum AiFiltersPreservePolicy
	aiRasterizeFilters            =2          # from enum AiFiltersPreservePolicy
	aiBaselineAscent              =0          # from enum AiFirstBaselineType
	aiBaselineCapHeight           =1          # from enum AiFirstBaselineType
	aiBaselineEmBoxHeight         =4          # from enum AiFirstBaselineType
	aiBaselineFixed               =5          # from enum AiFirstBaselineType
	aiBaselineLeading             =2          # from enum AiFirstBaselineType
	aiBaselineLegacy              =6          # from enum AiFirstBaselineType
	aiBaselineXHeight             =3          # from enum AiFirstBaselineType
	aiArtboardsToFiles            =5          # from enum AiFlashExportStyle
	aiAsFlashFile                 =1          # from enum AiFlashExportStyle
	aiLayersAsFiles               =3          # from enum AiFlashExportStyle
	aiLayersAsFrames              =2          # from enum AiFlashExportStyle
	aiLayersAsSymbols             =4          # from enum AiFlashExportStyle
	aiFlashVersion1               =1          # from enum AiFlashExportVersion
	aiFlashVersion2               =2          # from enum AiFlashExportVersion
	aiFlashVersion3               =3          # from enum AiFlashExportVersion
	aiFlashVersion4               =4          # from enum AiFlashExportVersion
	aiFlashVersion5               =5          # from enum AiFlashExportVersion
	aiFlashVersion6               =6          # from enum AiFlashExportVersion
	aiFlashVersion7               =7          # from enum AiFlashExportVersion
	aiFlashVersion8               =8          # from enum AiFlashExportVersion
	aiFlashVersion9               =9          # from enum AiFlashExportVersion
	aiLossless                    =1          # from enum AiFlashImageFormat
	aiLossy                       =2          # from enum AiFlashImageFormat
	aiJPEGOptimized               =2          # from enum AiFlashJPEGMethod
	aiJPEGStandard                =1          # from enum AiFlashJPEGMethod
	aiPlaybackLocal               =1          # from enum AiFlashPlaybackSecurity
	aiPlaybackNetwork             =2          # from enum AiFlashPlaybackSecurity
	aiNormalBaseline              =0          # from enum AiFontBaselineOption
	aiSubScript                   =2          # from enum AiFontBaselineOption
	aiSuperScript                 =1          # from enum AiFontBaselineOption
	aiAllCaps                     =2          # from enum AiFontCapsOption
	aiAllSmallCaps                =3          # from enum AiFontCapsOption
	aiNormalCaps                  =0          # from enum AiFontCapsOption
	aiSmallCaps                   =1          # from enum AiFontCapsOption
	aiDenominator                 =4          # from enum AiFontOpenTypePositionOption
	aiNumerator                   =3          # from enum AiFontOpenTypePositionOption
	aiOpenTypeDefault             =0          # from enum AiFontOpenTypePositionOption
	aiOpenTypeSubScript           =2          # from enum AiFontOpenTypePositionOption
	aiOpenTypeSuperScript         =1          # from enum AiFontOpenTypePositionOption
	aiSubstituteDevice            =2          # from enum AiFontSubstitutionPolicy
	aiSubstituteOblique           =0          # from enum AiFontSubstitutionPolicy
	aiSubstituteTint              =1          # from enum AiFontSubstitutionPolicy
	aiLinearGradient              =1          # from enum AiGradientType
	aiRadialGradient              =2          # from enum AiGradientType
	aiAutomaticallyConvertGradients=4          # from enum AiGradientsPreservePolicy
	aiKeepGradientsEditable       =3          # from enum AiGradientsPreservePolicy
	aiImageCMYK                   =3          # from enum AiImageColorSpace
	aiImageDeviceN                =6          # from enum AiImageColorSpace
	aiImageGrayScale              =1          # from enum AiImageColorSpace
	aiImageIndexed                =7          # from enum AiImageColorSpace
	aiImageLAB                    =4          # from enum AiImageColorSpace
	aiImageRGB                    =2          # from enum AiImageColorSpace
	aiImageSeparation             =5          # from enum AiImageColorSpace
	aiConvertInk                  =2          # from enum AiInkPrintStatus
	aiDisableInk                  =0          # from enum AiInkPrintStatus
	aiEnableInk                   =1          # from enum AiInkPrintStatus
	aiBlackInk                    =3          # from enum AiInkType
	aiCustomInk                   =4          # from enum AiInkType
	aiCyanInk                     =0          # from enum AiInkType
	aiMagentaInk                  =1          # from enum AiInkType
	aiYellowInk                   =2          # from enum AiInkType
	aiBeforeRunning               =3          # from enum AiJavaScriptExecutionMode
	aiDebuggerOnError             =2          # from enum AiJavaScriptExecutionMode
	aiNeverShowDebugger           =1          # from enum AiJavaScriptExecutionMode
	aiCenter                      =2          # from enum AiJustification
	aiFullJustify                 =6          # from enum AiJustification
	aiFullJustifyLastLineCenter   =5          # from enum AiJustification
	aiFullJustifyLastLineLeft     =3          # from enum AiJustification
	aiFullJustifyLastLineRight    =4          # from enum AiJustification
	aiLeft                        =0          # from enum AiJustification
	aiRight                       =1          # from enum AiJustification
	aiPushIn                      =0          # from enum AiKinsokuOrderEnum
	aiPushOutFirst                =1          # from enum AiKinsokuOrderEnum
	aiPushOutOnly                 =2          # from enum AiKinsokuOrderEnum
	aiDisabled                    =0          # from enum AiKnockoutState
	aiEnabled                     =1          # from enum AiKnockoutState
	aiInherited                   =2          # from enum AiKnockoutState
	aiKnockoutUnknown             =-1         # from enum AiKnockoutState
	aiArabic                      =39         # from enum AiLanguageType
	aiBengaliIndia                =51         # from enum AiLanguageType
	aiBokmalNorwegian             =8          # from enum AiLanguageType
	aiBrazillianPortuguese        =11         # from enum AiLanguageType
	aiBulgarian                   =20         # from enum AiLanguageType
	aiCanadianFrench              =3          # from enum AiLanguageType
	aiCatalan                     =17         # from enum AiLanguageType
	aiChinese                     =29         # from enum AiLanguageType
	aiCzech                       =22         # from enum AiLanguageType
	aiDanish                      =16         # from enum AiLanguageType
	aiDutch                       =15         # from enum AiLanguageType
	aiDutch2005Reform             =43         # from enum AiLanguageType
	aiEnglish                     =0          # from enum AiLanguageType
	aiFarsi                       =41         # from enum AiLanguageType
	aiFinnish                     =1          # from enum AiLanguageType
	aiGerman2006Reform            =42         # from enum AiLanguageType
	aiGreek                       =25         # from enum AiLanguageType
	aiGujarati                    =53         # from enum AiLanguageType
	aiHindi                       =49         # from enum AiLanguageType
	aiHungarian                   =28         # from enum AiLanguageType
	aiIcelandic                   =27         # from enum AiLanguageType
	aiItalian                     =7          # from enum AiLanguageType
	aiJapanese                    =30         # from enum AiLanguageType
	aiKannada                     =57         # from enum AiLanguageType
	aiMalayalam                   =58         # from enum AiLanguageType
	aiMarathi                     =50         # from enum AiLanguageType
	aiNynorskNorwegian            =9          # from enum AiLanguageType
	aiOldGerman                   =5          # from enum AiLanguageType
	aiOriya                       =54         # from enum AiLanguageType
	aiPolish                      =23         # from enum AiLanguageType
	aiPunjabi                     =52         # from enum AiLanguageType
	aiRumanian                    =24         # from enum AiLanguageType
	aiRussian                     =18         # from enum AiLanguageType
	aiSerbian                     =21         # from enum AiLanguageType
	aiSpanish                     =12         # from enum AiLanguageType
	aiStandardFrench              =2          # from enum AiLanguageType
	aiStandardGerman              =4          # from enum AiLanguageType
	aiStandardPortuguese          =10         # from enum AiLanguageType
	aiSwedish                     =13         # from enum AiLanguageType
	aiSwissGerman                 =6          # from enum AiLanguageType
	aiSwissGerman2006Reform       =44         # from enum AiLanguageType
	aiTamil                       =55         # from enum AiLanguageType
	aiTelugu                      =56         # from enum AiLanguageType
	aiTurkish                     =26         # from enum AiLanguageType
	aiUKEnglish                   =14         # from enum AiLanguageType
	aiUkranian                    =19         # from enum AiLanguageType
	aiBottomUp                    =1          # from enum AiLayerOrderType
	aiTopDown                     =2          # from enum AiLayerOrderType
	aiBrushes                     =3          # from enum AiLibraryType
	aiGraphicStyles               =4          # from enum AiLibraryType
	aiIllustratorArtwork          =1          # from enum AiLibraryType
	aiSwatches                    =2          # from enum AiLibraryType
	aiSymbols                     =5          # from enum AiLibraryType
	aiCCIT3                       =1          # from enum AiMonochromeCompression
	aiCCIT4                       =2          # from enum AiMonochromeCompression
	aiMonoZIP                     =3          # from enum AiMonochromeCompression
	aiNoMonoCompression           =0          # from enum AiMonochromeCompression
	aiRunLength                   =4          # from enum AiMonochromeCompression
	aiPreserveAppearance          =1          # from enum AiOutputFlattening
	aiPreservePaths               =0          # from enum AiOutputFlattening
	aiPDFArtBox                   =0          # from enum AiPDFBoxType
	aiPDFBleedBox                 =3          # from enum AiPDFBoxType
	aiPDFBoundingBox              =5          # from enum AiPDFBoxType
	aiPDFCropBox                  =1          # from enum AiPDFBoxType
	aiPDFMediaBox                 =4          # from enum AiPDFBoxType
	aiPDFTrimBox                  =2          # from enum AiPDFBoxType
	aiChange128AnyChanges         =5          # from enum AiPDFChangesAllowedEnum
	aiChange128Commenting         =4          # from enum AiPDFChangesAllowedEnum
	aiChange128EditPage           =2          # from enum AiPDFChangesAllowedEnum
	aiChange128FillForm           =3          # from enum AiPDFChangesAllowedEnum
	aiChange128None               =1          # from enum AiPDFChangesAllowedEnum
	aiChange40AnyChanges          =9          # from enum AiPDFChangesAllowedEnum
	aiChange40Commenting          =7          # from enum AiPDFChangesAllowedEnum
	aiChange40None                =6          # from enum AiPDFChangesAllowedEnum
	aiChange40PageLayout          =8          # from enum AiPDFChangesAllowedEnum
	aiAcrobat4                    =4          # from enum AiPDFCompatibility
	aiAcrobat5                    =5          # from enum AiPDFCompatibility
	aiAcrobat6                    =6          # from enum AiPDFCompatibility
	aiAcrobat7                    =7          # from enum AiPDFCompatibility
	aiAcrobat8                    =8          # from enum AiPDFCompatibility
	aiDiscardPDFOverprint         =2          # from enum AiPDFOverprint
	aiPreservePDFOverprint        =1          # from enum AiPDFOverprint
	aiPrint128HighResolution      =3          # from enum AiPDFPrintAllowedEnum
	aiPrint128LowResolution       =2          # from enum AiPDFPrintAllowedEnum
	aiPrint128None                =1          # from enum AiPDFPrintAllowedEnum
	aiPrint40HighResolution       =5          # from enum AiPDFPrintAllowedEnum
	aiPrint40None                 =4          # from enum AiPDFPrintAllowedEnum
	aiTrimMarkWeight0125          =1          # from enum AiPDFTrimMarkWeight
	aiTrimMarkWeight025           =2          # from enum AiPDFTrimMarkWeight
	aiTrimMarkWeight05            =3          # from enum AiPDFTrimMarkWeight
	aiPDFX1a2001                  =2          # from enum AiPDFXStandard
	aiPDFX1a2003                  =3          # from enum AiPDFXStandard
	aiPDFX32001                   =4          # from enum AiPDFXStandard
	aiPDFX32002                   =4          # from enum AiPDFXStandard
	aiPDFX32003                   =5          # from enum AiPDFXStandard
	aiPDFX42007                   =6          # from enum AiPDFXStandard
	aiPDFXNone                    =1          # from enum AiPDFXStandard
	aiCompoundPathItem            =1          # from enum AiPageItemType
	aiEmbeddedItem                =13         # from enum AiPageItemType
	aiGraphItem                   =2          # from enum AiPageItemType
	aiGroupItem                   =3          # from enum AiPageItemType
	aiLegacyTextItem              =11         # from enum AiPageItemType
	aiMeshItem                    =4          # from enum AiPageItemType
	aiNonNativeItem               =12         # from enum AiPageItemType
	aiPathItem                    =5          # from enum AiPageItemType
	aiPlacedItem                  =6          # from enum AiPageItemType
	aiPluginItem                  =7          # from enum AiPageItemType
	aiRasterItem                  =8          # from enum AiPageItemType
	aiSymbolItem                  =9          # from enum AiPageItemType
	aiTextFrame                   =10         # from enum AiPageItemType
	aiPageMarksJapanese           =1          # from enum AiPageMarksTypes
	aiPageMarksRoman              =0          # from enum AiPageMarksTypes
	aiAnchorPoint                 =2          # from enum AiPathPointSelection
	aiLeftDirection               =3          # from enum AiPathPointSelection
	aiLeftRightPoint              =5          # from enum AiPathPointSelection
	aiNoSelection                 =1          # from enum AiPathPointSelection
	aiRightDirection              =4          # from enum AiPathPointSelection
	aiFLOORPLANE                  =3          # from enum AiPerspectiveGridPlaneType
	aiLEFTPLANE                   =1          # from enum AiPerspectiveGridPlaneType
	aiNOPLANE                     =0          # from enum AiPerspectiveGridPlaneType
	aiRIGHTPLANE                  =2          # from enum AiPerspectiveGridPlaneType
	aiPhotoshop6                  =2          # from enum AiPhotoshopCompatibility
	aiPhotoshop8                  =1          # from enum AiPhotoshopCompatibility
	aiCorner                      =2          # from enum AiPointType
	aiSmooth                      =1          # from enum AiPointType
	aiNegative                    =-1         # from enum AiPolarityValues
	aiPositive                    =1          # from enum AiPolarityValues
	aiImageCompressionJPEG        =2          # from enum AiPostScriptImageCompressionType
	aiImageCompressionNone        =0          # from enum AiPostScriptImageCompressionType
	aiImageCompressionRLE         =1          # from enum AiPostScriptImageCompressionType
	aiAllLayers                   =2          # from enum AiPrintArtworkDesignation
	aiVisibleLayers               =1          # from enum AiPrintArtworkDesignation
	aiVisiblePrintableLayers      =0          # from enum AiPrintArtworkDesignation
	aiAbsoluteColorimetric        =3          # from enum AiPrintColorIntent
	aiPerceptualIntent            =0          # from enum AiPrintColorIntent
	aiRelativeColorimetric        =2          # from enum AiPrintColorIntent
	aiSaturationIntent            =1          # from enum AiPrintColorIntent
	aiCustomProfile               =3          # from enum AiPrintColorProfile
	aiOldstyleProfile             =0          # from enum AiPrintColorProfile
	aiPrinterProfile              =2          # from enum AiPrintColorProfile
	aiSourceProfile               =1          # from enum AiPrintColorProfile
	aiComposite                   =0          # from enum AiPrintColorSeparationMode
	aiHostBasedSeparation         =1          # from enum AiPrintColorSeparationMode
	aiInRIPSeparation             =2          # from enum AiPrintColorSeparationMode
	aiDownloadComplete            =2          # from enum AiPrintFontDownloadMode
	aiDownloadNone                =0          # from enum AiPrintFontDownloadMode
	aiDownloadSubset              =1          # from enum AiPrintFontDownloadMode
	aiAutoRotate                  =4          # from enum AiPrintOrientation
	aiLandscape                   =1          # from enum AiPrintOrientation
	aiPortrait                    =0          # from enum AiPrintOrientation
	aiReverseLandscape            =3          # from enum AiPrintOrientation
	aiReversePortrait             =2          # from enum AiPrintOrientation
	aiTranslateBottom             =8          # from enum AiPrintPosition
	aiTranslateBottomLeft         =7          # from enum AiPrintPosition
	aiTranslateBottomRight        =9          # from enum AiPrintPosition
	aiTranslateCenter             =5          # from enum AiPrintPosition
	aiTranslateLeft               =4          # from enum AiPrintPosition
	aiTranslateRight              =6          # from enum AiPrintPosition
	aiTranslateTop                =2          # from enum AiPrintPosition
	aiTranslateTopLeft            =1          # from enum AiPrintPosition
	aiTranslateTopRight           =3          # from enum AiPrintPosition
	aiTileFullPages               =1          # from enum AiPrintTiling
	aiTileImageableAreas          =2          # from enum AiPrintTiling
	aiTileSingleFullPage          =0          # from enum AiPrintTiling
	aiBlackAndWhitePrinter        =2          # from enum AiPrinterColorMode
	aiColorPrinter                =0          # from enum AiPrinterColorMode
	aiGrayscalePrinter            =1          # from enum AiPrinterColorMode
	aiPSLevel1                    =1          # from enum AiPrinterPostScriptLevelEnum
	aiPSLevel2                    =2          # from enum AiPrinterPostScriptLevelEnum
	aiPSLevel3                    =3          # from enum AiPrinterPostScriptLevelEnum
	aiNonPostScriptPrinter        =2          # from enum AiPrinterTypeEnum
	aiPostScriptPrinter           =1          # from enum AiPrinterTypeEnum
	aiUnknownPrinterType          =0          # from enum AiPrinterTypeEnum
	aiArtboardBounds              =0          # from enum AiPrintingBounds
	aiArtworkBounds               =1          # from enum AiPrintingBounds
	aiCropBounds                  =2          # from enum AiPrintingBounds
	aiEmbed                       =0          # from enum AiRasterImageLocation
	aiLink                        =1          # from enum AiRasterImageLocation
	aiPreserve                    =2          # from enum AiRasterImageLocation
	aiDataFromFile                =2          # from enum AiRasterLinkState
	aiDataModified                =3          # from enum AiRasterLinkState
	aiNoData                      =1          # from enum AiRasterLinkState
	aiBitmap                      =3          # from enum AiRasterizationColorModel
	aiDefaultColorModel           =1          # from enum AiRasterizationColorModel
	aiGrayscale                   =2          # from enum AiRasterizationColorModel
	aiUnitsCM                     =3          # from enum AiRulerUnits
	aiUnitsInches                 =2          # from enum AiRulerUnits
	aiUnitsMM                     =6          # from enum AiRulerUnits
	aiUnitsPicas                  =5          # from enum AiRulerUnits
	aiUnitsPixels                 =8          # from enum AiRulerUnits
	aiUnitsPoints                 =4          # from enum AiRulerUnits
	aiUnitsQ                      =7          # from enum AiRulerUnits
	aiUnitsUnknown                =1          # from enum AiRulerUnits
	aiEntities                    =2          # from enum AiSVGCSSPropertyLocation
	aiPresentationAttributes      =4          # from enum AiSVGCSSPropertyLocation
	aiStyleAttributes             =1          # from enum AiSVGCSSPropertyLocation
	aiStyleElements               =3          # from enum AiSVGCSSPropertyLocation
	aiSVG1_0                      =1          # from enum AiSVGDTDVersion
	aiSVG1_1                      =2          # from enum AiSVGDTDVersion
	aiSVGBasic1_1                 =5          # from enum AiSVGDTDVersion
	aiSVGTiny1_1                  =3          # from enum AiSVGDTDVersion
	aiSVGTiny1_1Plus              =4          # from enum AiSVGDTDVersion
	aiSVGTiny1_2                  =6          # from enum AiSVGDTDVersion
	aiASCII                       =1          # from enum AiSVGDocumentEncoding
	aiUTF16                       =3          # from enum AiSVGDocumentEncoding
	aiUTF8                        =2          # from enum AiSVGDocumentEncoding
	aiAllGlyphs                   =7          # from enum AiSVGFontSubsetting
	aiCommonEnglish               =3          # from enum AiSVGFontSubsetting
	aiCommonRoman                 =5          # from enum AiSVGFontSubsetting
	aiGlyphsUsed                  =2          # from enum AiSVGFontSubsetting
	aiGlyphsUsedPlusEnglish       =4          # from enum AiSVGFontSubsetting
	aiGlyphsUsedPlusRoman         =6          # from enum AiSVGFontSubsetting
	aiNoFonts                     =1          # from enum AiSVGFontSubsetting
	aiOutlineFont                 =3          # from enum AiSVGFontType
	aiSVGFont                     =2          # from enum AiSVGFontType
	aiSGIdUnique                  =2          # from enum AiSVGIdType
	aiSVGIdMinimal                =0          # from enum AiSVGIdType
	aiSVGIdRegular                =1          # from enum AiSVGIdType
	aiDoNotSaveChanges            =2          # from enum AiSaveOptions
	aiPromptToSaveChanges         =3          # from enum AiSaveOptions
	aiSaveChanges                 =1          # from enum AiSaveOptions
	aiDesktop                     =2          # from enum AiScreenMode
	aiFullScreen                  =3          # from enum AiScreenMode
	aiMultiWindow                 =1          # from enum AiScreenMode
	aiSpotCMYK                    =0          # from enum AiSpotColorKind
	aiSpotLAB                     =2          # from enum AiSpotColorKind
	aiSpotRGB                     =1          # from enum AiSpotColorKind
	aiButtEndCap                  =1          # from enum AiStrokeCap
	aiProjectingEndCap            =3          # from enum AiStrokeCap
	aiRoundEndCap                 =2          # from enum AiStrokeCap
	aiBevelEndJoin                =3          # from enum AiStrokeJoin
	aiMiterEndJoin                =1          # from enum AiStrokeJoin
	aiRoundEndJoin                =2          # from enum AiStrokeJoin
	aiAlignBottom                 =0          # from enum AiStyleRunAlignmentType
	aiAlignCenter                 =3          # from enum AiStyleRunAlignmentType
	aiAlignTop                    =5          # from enum AiStyleRunAlignmentType
	aiICFBottom                   =1          # from enum AiStyleRunAlignmentType
	aiICFTop                      =4          # from enum AiStyleRunAlignmentType
	aiRomanBaseline               =2          # from enum AiStyleRunAlignmentType
	aiSymbolBottomLeftPoint       =7          # from enum AiSymbolRegistrationPoint
	aiSymbolBottomMiddlePoint     =8          # from enum AiSymbolRegistrationPoint
	aiSymbolBottomRightPoint      =9          # from enum AiSymbolRegistrationPoint
	aiSymbolCenterPoint           =5          # from enum AiSymbolRegistrationPoint
	aiSymbolMiddleLeftPoint       =4          # from enum AiSymbolRegistrationPoint
	aiSymbolMiddleRightPoint      =6          # from enum AiSymbolRegistrationPoint
	aiSymbolTopLeftPoint          =1          # from enum AiSymbolRegistrationPoint
	aiSymbolTopMiddlePoint        =2          # from enum AiSymbolRegistrationPoint
	aiSymbolTopRightPoint         =3          # from enum AiSymbolRegistrationPoint
	aiIBMPC                       =0          # from enum AiTIFFByteOrder
	aiMacintosh                   =1          # from enum AiTIFFByteOrder
	aiCenterTab                   =1          # from enum AiTabStopAlignment
	aiDecimalTab                  =3          # from enum AiTabStopAlignment
	aiLeftTab                     =0          # from enum AiTabStopAlignment
	aiRightTab                    =2          # from enum AiTabStopAlignment
	aiCrisp                       =3          # from enum AiTextAntialias
	aiNone                        =1          # from enum AiTextAntialias
	aiSharp                       =2          # from enum AiTextAntialias
	aiStrong                      =4          # from enum AiTextAntialias
	aiHorizontal                  =0          # from enum AiTextOrientation
	aiVertical                    =1          # from enum AiTextOrientation
	aiAutomaticallyConvertText    =4          # from enum AiTextPreservePolicy
	aiKeepTextEditable            =3          # from enum AiTextPreservePolicy
	aiOutlineText                 =1          # from enum AiTextPreservePolicy
	aiRasterizeText               =2          # from enum AiTextPreservePolicy
	aiAreaText                    =1          # from enum AiTextType
	aiPathText                    =2          # from enum AiTextType
	aiPointText                   =0          # from enum AiTextType
	aiTracingFullColor            =1          # from enum AiTracingColorType
	aiTracingLimitedColor         =0          # from enum AiTracingColorType
	aiTracingMethodAbutting       =0          # from enum AiTracingMethodType
	aiTracingMethodOverlapping    =1          # from enum AiTracingMethodType
	aiTracingModeBlackAndWhite    =2          # from enum AiTracingModeType
	aiTracingModeColor            =0          # from enum AiTracingModeType
	aiTracingModeGray             =1          # from enum AiTracingModeType
	aiTransformBottom             =7          # from enum AiTransformation
	aiTransformBottomLeft         =4          # from enum AiTransformation
	aiTransformBottomRight        =10         # from enum AiTransformation
	aiTransformCenter             =6          # from enum AiTransformation
	aiTransformDocumentOrigin     =1          # from enum AiTransformation
	aiTransformLeft               =3          # from enum AiTransformation
	aiTransformRight              =9          # from enum AiTransformation
	aiTransformTop                =5          # from enum AiTransformation
	aiTransformTopLeft            =2          # from enum AiTransformation
	aiTransformTopRight           =8          # from enum AiTransformation
	aiIgnoreOpaque                =3          # from enum AiTrappingType
	aiNormalTrapping              =0          # from enum AiTrappingType
	aiOpaque                      =2          # from enum AiTrappingType
	aiTransparent                 =1          # from enum AiTrappingType
	aiDisplayAlerts               =2          # from enum AiUserInteractionLevel
	aiDontDisplayAlerts           =-1         # from enum AiUserInteractionLevel
	aiGraph                       =5          # from enum AiVariableKind
	aiImage                       =4          # from enum AiVariableKind
	aiTextual                     =3          # from enum AiVariableKind
	aiUnknownKind                 =1          # from enum AiVariableKind
	aiVisibility                  =2          # from enum AiVariableKind
	aiTracingViewImage            =4          # from enum AiViewType
	aiTracingViewVectorOutlines   =2          # from enum AiViewType
	aiTracingViewVectorOutlinesWithTracing=1          # from enum AiViewType
	aiTracingViewVectorTracingResult=0          # from enum AiViewType
	aiTracingViewVectorWithTransparentImage=3          # from enum AiViewType
	aiWariChuAutoJustify          =7          # from enum AiWariChuJustificationType
	aiWariChuCenter               =2          # from enum AiWariChuJustificationType
	aiWariChuFullJustify          =6          # from enum AiWariChuJustificationType
	aiWariChuFullJustifyLastLineCenter=5          # from enum AiWariChuJustificationType
	aiWariChuFullJustifyLastLineLeft=3          # from enum AiWariChuJustificationType
	aiWariChuFullJustifyLastLineRight=4          # from enum AiWariChuJustificationType
	aiWariChuLeft                 =0          # from enum AiWariChuJustificationType
	aiWariChuRight                =1          # from enum AiWariChuJustificationType
	aiBringForward                =2          # from enum AiZOrderMethod
	aiBringToFront                =1          # from enum AiZOrderMethod
	aiSendBackward                =3          # from enum AiZOrderMethod
	aiSendToBack                  =4          # from enum AiZOrderMethod

from win32com.client import DispatchBaseClass
class Artboard(DispatchBaseClass):
	'an artboard object'
	CLSID = IID('{30557E1D-A243-499D-84B8-6E170B36A1BD}')
	coclass_clsid = None

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtboardRect": (1648454705, 2, (12, 0), (), "ArtboardRect", None),
		"Name": (1648454713, 2, (8, 0), (), "Name", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"RulerOrigin": (1648454712, 2, (12, 0), (), "RulerOrigin", None),
		"RulerPAR": (1648454706, 2, (5, 0), (), "RulerPAR", None),
		"ShowCenter": (1648454708, 2, (11, 0), (), "ShowCenter", None),
		"ShowCrossHairs": (1648454709, 2, (11, 0), (), "ShowCrossHairs", None),
		"ShowSafeAreas": (1648454710, 2, (11, 0), (), "ShowSafeAreas", None),
	}
	_prop_map_put_ = {
		"ArtboardRect": ((1648454705, LCID, 4, 0),()),
		"Name": ((1648454713, LCID, 4, 0),()),
		"RulerOrigin": ((1648454712, LCID, 4, 0),()),
		"RulerPAR": ((1648454706, LCID, 4, 0),()),
		"ShowCenter": ((1648454708, LCID, 4, 0),()),
		"ShowCrossHairs": ((1648454709, LCID, 4, 0),()),
		"ShowSafeAreas": ((1648454710, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Artboards(DispatchBaseClass):
	'A collection of artboards'
	CLSID = IID('{091ADAF8-D422-11DB-8314-0800200C9A66}')
	coclass_clsid = None

	# Result is of type Artboard
	def Add(self, ArtboardRect=defaultNamedNotOptArg):
		'add artboard object'
		ret = self._oleobj_.InvokeTypes(1682533681, LCID, 1, (9, 0), ((12, 1),),ArtboardRect
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{30557E1D-A243-499D-84B8-6E170B36A1BD}')
		return ret

	def GetActiveArtboardIndex(self):
		"Retrieves the index position of the active artboard in the document's list"
		return self._oleobj_.InvokeTypes(1732603698, LCID, 1, (3, 0), (),)

	# Result is of type Artboard
	def GetByName(self, ArtboardName=defaultNamedNotOptArg):
		'Get the first Artboard with specified name'
		ret = self._oleobj_.InvokeTypes(1732603701, LCID, 1, (9, 0), ((8, 1),),ArtboardName
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetByName', '{30557E1D-A243-499D-84B8-6E170B36A1BD}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	def Insert(self, ArtboardRect=defaultNamedNotOptArg, Index=defaultNamedNotOptArg):
		'Insert an Artboard at specified location'
		return self._oleobj_.InvokeTypes(1732603702, LCID, 1, (24, 0), ((12, 1), (3, 1)),ArtboardRect
			, Index)

	# Result is of type Artboard
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{30557E1D-A243-499D-84B8-6E170B36A1BD}')
		return ret

	def Remove(self, Index=defaultNamedNotOptArg):
		'delete artboard object'
		return self._oleobj_.InvokeTypes(1732603697, LCID, 1, (24, 0), ((3, 1),),Index
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	def SetActiveArtboardIndex(self, Index=defaultNamedNotOptArg):
		'Makes a specific artboard active, and makes it current in the iteration order'
		return self._oleobj_.InvokeTypes(1732603699, LCID, 1, (24, 0), ((3, 1),),Index
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{30557E1D-A243-499D-84B8-6E170B36A1BD}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{30557E1D-A243-499D-84B8-6E170B36A1BD}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class AutoCADFileOptions(DispatchBaseClass):
	'Options which may be supplied when opening a AutoCAD file'
	CLSID = IID('{AD865867-DED8-42D6-9BD8-D77533905975}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"CenterArtwork": (1883455863, 2, (11, 0), (), "CenterArtwork", None),
		"GlobalScaleOption": (1883722575, 2, (3, 0), (), "GlobalScaleOption", None),
		"GlobalScalePercent": (1883722576, 2, (5, 0), (), "GlobalScalePercent", None),
		"MergeLayers": (1884114035, 2, (11, 0), (), "MergeLayers", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"ScaleLineweights": (1883327575, 2, (11, 0), (), "ScaleLineweights", None),
		"SelectedLayoutName": (1884507214, 2, (8, 0), (), "SelectedLayoutName", None),
		"Unit": (1883329365, 2, (3, 0), (), "Unit", None),
		"UnitScaleRatio": (1883329362, 2, (5, 0), (), "UnitScaleRatio", None),
	}
	_prop_map_put_ = {
		"CenterArtwork": ((1883455863, LCID, 4, 0),()),
		"GlobalScaleOption": ((1883722575, LCID, 4, 0),()),
		"GlobalScalePercent": ((1883722576, LCID, 4, 0),()),
		"MergeLayers": ((1884114035, LCID, 4, 0),()),
		"ScaleLineweights": ((1883327575, LCID, 4, 0),()),
		"SelectedLayoutName": ((1884507214, LCID, 4, 0),()),
		"Unit": ((1883329365, LCID, 4, 0),()),
		"UnitScaleRatio": ((1883329362, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Brush(DispatchBaseClass):
	'A brush'
	CLSID = IID('{95CD20BA-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def ApplyTo(self, ArtItem=defaultNamedNotOptArg):
		'Apply a brush or art style to object(s)'
		return self._oleobj_.InvokeTypes(1097886841, LCID, 1, (24, 0), ((12, 1),),ArtItem
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"Name": ((1886282093, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Brushes(DispatchBaseClass):
	'A collection of brushes'
	CLSID = IID('{95CD20E8-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	# Result is of type Brush
	def Add(self, BrushDefinition=defaultNamedNotOptArg, BrushName=defaultNamedOptArg):
		'create a brush'
		ret = self._oleobj_.InvokeTypes(1665286500, LCID, 1, (9, 0), ((8, 1), (12, 17)),BrushDefinition
			, BrushName)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{95CD20BA-AD72-11D3-B086-0010A4F5C335}')
		return ret

	# Result is of type Brush
	def AddAndLoad(self, BrushDefinition=defaultNamedNotOptArg):
		'create a brush, select the brush tool and load the created brush in the brush tool'
		ret = self._oleobj_.InvokeTypes(1665286476, LCID, 1, (9, 0), ((8, 1),),BrushDefinition
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddAndLoad', '{95CD20BA-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type Brush
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20BA-AD72-11D3-B086-0010A4F5C335}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20BA-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20BA-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class CharacterAttributes(DispatchBaseClass):
	'properties of a character'
	CLSID = IID('{4C78DFCD-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = None

	def SetFillColor(self, arg0=defaultUnnamedArg):
		'the color of the text fill'
		return self._oleobj_.InvokeTypes(1634289219, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetStrokeColor(self, arg0=defaultUnnamedArg):
		'the color of the text stroke'
		return self._oleobj_.InvokeTypes(1634292547, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		"AkiLeft": (1883451700, 2, (5, 0), (), "AkiLeft", None),
		"AkiRight": (1883451701, 2, (5, 0), (), "AkiRight", None),
		"Alignment": (1416835121, 2, (3, 0), (), "Alignment", None),
		"AlternateGlyphs": (1883451509, 2, (3, 0), (), "AlternateGlyphs", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"AutoKerning": (1884565559, 2, (11, 0), (), "AutoKerning", None),
		"AutoLeading": (1883451443, 2, (11, 0), (), "AutoLeading", None),
		"BaselineDirection": (1883451507, 2, (3, 0), (), "BaselineDirection", None),
		"BaselinePosition": (1883451445, 2, (3, 0), (), "BaselinePosition", None),
		"BaselineShift": (1884565556, 2, (5, 0), (), "BaselineShift", None),
		"Capitalization": (1883451444, 2, (3, 0), (), "Capitalization", None),
		"ConnectionForms": (1883451498, 2, (11, 0), (), "ConnectionForms", None),
		"ContextualLigature": (1883451491, 2, (11, 0), (), "ContextualLigature", None),
		"Direction": (1884565561, 2, (3, 0), (), "Direction", None),
		"DiscretionaryLigature": (1883451490, 2, (11, 0), (), "DiscretionaryLigature", None),
		"FigureStyle": (1883451501, 2, (3, 0), (), "FigureStyle", None),
		"FillColor": (1634289219, 2, (9, 0), (), "FillColor", None),
		"Fractions": (1883451494, 2, (11, 0), (), "Fractions", None),
		"HorizontalScale": (1884510296, 2, (5, 0), (), "HorizontalScale", None),
		"Italics": (1883451506, 2, (11, 0), (), "Italics", None),
		"KerningMethod": (1884566070, 2, (3, 0), (), "KerningMethod", None),
		"Language": (1883451508, 2, (3, 0), (), "Language", None),
		"Leading": (1884565557, 2, (5, 0), (), "Leading", None),
		"Ligature": (1883451489, 2, (11, 0), (), "Ligature", None),
		"NoBreak": (1883451702, 2, (11, 0), (), "NoBreak", None),
		"OpenTypePosition": (1883451446, 2, (3, 0), (), "OpenTypePosition", None),
		"Ordinals": (1883451495, 2, (11, 0), (), "Ordinals", None),
		"Ornaments": (1883451500, 2, (11, 0), (), "Ornaments", None),
		"OverprintFill": (1883451704, 2, (11, 0), (), "OverprintFill", None),
		"OverprintStroke": (1883451703, 2, (11, 0), (), "OverprintStroke", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"ProportionalMetrics": (1883451503, 2, (11, 0), (), "ProportionalMetrics", None),
		"Rotation": (1400394360, 2, (5, 0), (), "Rotation", None),
		"Scaling": (1884565560, 2, (12, 0), (), "Scaling", None),
		"Size": (1886679930, 2, (5, 0), (), "Size", None),
		"StrikeThrough": (1883451448, 2, (11, 0), (), "StrikeThrough", None),
		"StrokeColor": (1634292547, 2, (9, 0), (), "StrokeColor", None),
		"StrokeWeight": (1883451705, 2, (5, 0), (), "StrokeWeight", None),
		"StylisticAlternates": (1883451499, 2, (11, 0), (), "StylisticAlternates", None),
		"Swash": (1883451496, 2, (11, 0), (), "Swash", None),
		"TateChuYokoHorizontal": (1883451699, 2, (3, 0), (), "TateChuYokoHorizontal", None),
		"TateChuYokoVertical": (1883451698, 2, (3, 0), (), "TateChuYokoVertical", None),
		# Method 'TextFont' returns object of type 'TextFont'
		"TextFont": (1666472038, 2, (9, 0), (), "TextFont", '{95CD20BC-AD72-11D3-B086-0010A4F5C335}'),
		"Titling": (1883451497, 2, (11, 0), (), "Titling", None),
		"Tracking": (1884565558, 2, (3, 0), (), "Tracking", None),
		"Tsume": (1883451510, 2, (5, 0), (), "Tsume", None),
		"Underline": (1883451447, 2, (11, 0), (), "Underline", None),
		"VerticalScale": (1884510553, 2, (5, 0), (), "VerticalScale", None),
		"WariChuCharactersAfterBreak": (1883451696, 2, (3, 0), (), "WariChuCharactersAfterBreak", None),
		"WariChuCharactersBeforeBreak": (1883451514, 2, (3, 0), (), "WariChuCharactersBeforeBreak", None),
		"WariChuEnabled": (1883451749, 2, (11, 0), (), "WariChuEnabled", None),
		"WariChuJustification": (1883451697, 2, (3, 0), (), "WariChuJustification", None),
		"WariChuLineGap": (1883451512, 2, (3, 0), (), "WariChuLineGap", None),
		"WariChuLines": (1883451511, 2, (3, 0), (), "WariChuLines", None),
		"WariChuScale": (1883451513, 2, (5, 0), (), "WariChuScale", None),
	}
	_prop_map_put_ = {
		"AkiLeft": ((1883451700, LCID, 4, 0),()),
		"AkiRight": ((1883451701, LCID, 4, 0),()),
		"Alignment": ((1416835121, LCID, 4, 0),()),
		"AlternateGlyphs": ((1883451509, LCID, 4, 0),()),
		"AutoKerning": ((1884565559, LCID, 4, 0),()),
		"AutoLeading": ((1883451443, LCID, 4, 0),()),
		"BaselineDirection": ((1883451507, LCID, 4, 0),()),
		"BaselinePosition": ((1883451445, LCID, 4, 0),()),
		"BaselineShift": ((1884565556, LCID, 4, 0),()),
		"Capitalization": ((1883451444, LCID, 4, 0),()),
		"ConnectionForms": ((1883451498, LCID, 4, 0),()),
		"ContextualLigature": ((1883451491, LCID, 4, 0),()),
		"Direction": ((1884565561, LCID, 4, 0),()),
		"DiscretionaryLigature": ((1883451490, LCID, 4, 0),()),
		"FigureStyle": ((1883451501, LCID, 4, 0),()),
		"FillColor": ((1634289219, LCID, 4, 0),()),
		"Fractions": ((1883451494, LCID, 4, 0),()),
		"HorizontalScale": ((1884510296, LCID, 4, 0),()),
		"Italics": ((1883451506, LCID, 4, 0),()),
		"KerningMethod": ((1884566070, LCID, 4, 0),()),
		"Language": ((1883451508, LCID, 4, 0),()),
		"Leading": ((1884565557, LCID, 4, 0),()),
		"Ligature": ((1883451489, LCID, 4, 0),()),
		"NoBreak": ((1883451702, LCID, 4, 0),()),
		"OpenTypePosition": ((1883451446, LCID, 4, 0),()),
		"Ordinals": ((1883451495, LCID, 4, 0),()),
		"Ornaments": ((1883451500, LCID, 4, 0),()),
		"OverprintFill": ((1883451704, LCID, 4, 0),()),
		"OverprintStroke": ((1883451703, LCID, 4, 0),()),
		"ProportionalMetrics": ((1883451503, LCID, 4, 0),()),
		"Rotation": ((1400394360, LCID, 4, 0),()),
		"Scaling": ((1884565560, LCID, 4, 0),()),
		"Size": ((1886679930, LCID, 4, 0),()),
		"StrikeThrough": ((1883451448, LCID, 4, 0),()),
		"StrokeColor": ((1634292547, LCID, 4, 0),()),
		"StrokeWeight": ((1883451705, LCID, 4, 0),()),
		"StylisticAlternates": ((1883451499, LCID, 4, 0),()),
		"Swash": ((1883451496, LCID, 4, 0),()),
		"TateChuYokoHorizontal": ((1883451699, LCID, 4, 0),()),
		"TateChuYokoVertical": ((1883451698, LCID, 4, 0),()),
		"TextFont": ((1666472038, LCID, 4, 0),()),
		"Titling": ((1883451497, LCID, 4, 0),()),
		"Tracking": ((1884565558, LCID, 4, 0),()),
		"Tsume": ((1883451510, LCID, 4, 0),()),
		"Underline": ((1883451447, LCID, 4, 0),()),
		"VerticalScale": ((1884510553, LCID, 4, 0),()),
		"WariChuCharactersAfterBreak": ((1883451696, LCID, 4, 0),()),
		"WariChuCharactersBeforeBreak": ((1883451514, LCID, 4, 0),()),
		"WariChuEnabled": ((1883451749, LCID, 4, 0),()),
		"WariChuJustification": ((1883451697, LCID, 4, 0),()),
		"WariChuLineGap": ((1883451512, LCID, 4, 0),()),
		"WariChuLines": ((1883451511, LCID, 4, 0),()),
		"WariChuScale": ((1883451513, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class CharacterStyle(DispatchBaseClass):
	'a named style that remembers character attributes'
	CLSID = IID('{7C1FA60D-BF8F-4C43-B14C-77D842034966}')
	coclass_clsid = None

	def ApplyTo(self, TextItem=defaultNamedNotOptArg, ClearingOverrides=defaultNamedOptArg):
		'Apply the character style to text object(s)'
		return self._oleobj_.InvokeTypes(1097876307, LCID, 1, (24, 0), ((12, 1), (12, 17)),TextItem
			, ClearingOverrides)

	def Clear(self):
		'Remove all the attributes from this character style'
		return self._oleobj_.InvokeTypes(1094927187, LCID, 1, (24, 0), (),)

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'CharacterAttributes' returns object of type 'CharacterAttributes'
		"CharacterAttributes": (1130905972, 2, (9, 0), (), "CharacterAttributes", '{4C78DFCD-7A09-11D4-81A0-00C04F60ECCC}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"Name": ((1886282093, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class CharacterStyles(DispatchBaseClass):
	'A collection of character styles'
	CLSID = IID('{255CD590-0FBF-4345-94F5-871C4021D6BF}')
	coclass_clsid = None

	# Result is of type CharacterStyle
	def Add(self, Name=defaultNamedNotOptArg):
		'create a named character style'
		ret = self._oleobj_.InvokeTypes(1665356628, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{7C1FA60D-BF8F-4C43-B14C-77D842034966}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type CharacterStyle
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{7C1FA60D-BF8F-4C43-B14C-77D842034966}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete a character style from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{7C1FA60D-BF8F-4C43-B14C-77D842034966}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{7C1FA60D-BF8F-4C43-B14C-77D842034966}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Characters(DispatchBaseClass):
	'A collection of characters'
	CLSID = IID('{95CD20D5-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	# Result is of type TextRange
	def Add(self, Contents=defaultNamedNotOptArg, RelativeObject=defaultNamedOptArg, InsertionLocation=defaultNamedOptArg):
		'create a character'
		ret = self._oleobj_.InvokeTypes(1667784992, LCID, 1, (9, 0), ((8, 1), (12, 17), (12, 17)),Contents
			, RelativeObject, InsertionLocation)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	# Result is of type TextRange
	def AddBefore(self, Contents=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1131561574, LCID, 1, (9, 0), ((8, 1),),Contents
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddBefore', '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type TextRange
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class CompoundPathItem(DispatchBaseClass):
	'Compound path artwork item'
	CLSID = IID('{95CD20BE-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def ApplyEffect(self, LiveEffectXML=defaultNamedNotOptArg):
		'Apply effect to selected artItem'
		return self._oleobj_.InvokeTypes(1799447892, LCID, 1, (24, 0), ((8, 1),),LiveEffectXML
			)

	def BringInPerspective(self, PositionX=defaultNamedNotOptArg, PositionY=defaultNamedNotOptArg, PerspectiveGridPlane=defaultNamedNotOptArg):
		'Place art object(s)in perspective grid at spedified perspective plane and coordinate'
		return self._oleobj_.InvokeTypes(1685013072, LCID, 1, (24, 0), ((5, 1), (5, 1), (3, 1)),PositionX
			, PositionY, PerspectiveGridPlane)

	def Copy(self):
		'Copy selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668247673, LCID, 1, (24, 0), (),)

	def Cut(self):
		'Cut selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668641824, LCID, 1, (24, 0), (),)

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def Duplicate(self, RelativeObject=defaultNamedOptArg, InsertionLocation=defaultNamedOptArg):
		'create a duplicate of the object'
		ret = self._oleobj_.InvokeTypes(1668050798, LCID, 1, (9, 0), ((12, 17), (12, 17)),RelativeObject
			, InsertionLocation)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', None)
		return ret

	def Move(self, RelativeObject=defaultNamedNotOptArg, InsertionLocation=defaultNamedNotOptArg):
		'move the object'
		return self._oleobj_.InvokeTypes(1836021349, LCID, 1, (24, 0), ((9, 1), (3, 1)),RelativeObject
			, InsertionLocation)

	def MoveAfter(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in behind object'
		return self._oleobj_.InvokeTypes(1299596641, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveBefore(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in front of object'
		return self._oleobj_.InvokeTypes(1299596642, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveToBeginning(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to beginning of container'
		return self._oleobj_.InvokeTypes(1299596646, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def MoveToEnd(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to end of container'
		return self._oleobj_.InvokeTypes(1299596645, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def Resize(self, ScaleX=defaultNamedNotOptArg, ScaleY=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg
			, ChangeFillGradients=defaultNamedOptArg, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, ScaleAbout=defaultNamedOptArg):
		'Scale art object(s)'
		return self._oleobj_.InvokeTypes(1685017421, LCID, 1, (24, 0), ((5, 1), (5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),ScaleX
			, ScaleY, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern
			, ChangeLineWidths, ScaleAbout)

	def Rotate(self, Angle=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, RotateAbout=defaultNamedOptArg):
		'Rotate art object(s)'
		return self._oleobj_.InvokeTypes(1685017165, LCID, 1, (24, 0), ((5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),Angle
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, RotateAbout
			)

	def SendScriptMessage(self, PluginName=defaultNamedNotOptArg, MessageSelector=defaultNamedNotOptArg, InputString=defaultNamedNotOptArg):
		'sends the script message to the required plugin'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1632850765, LCID, 1, (8, 0), ((8, 1), (8, 1), (8, 1)),PluginName
			, MessageSelector, InputString)

	def Transform(self, TransformationMatrix=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, TransformAbout=defaultNamedOptArg):
		'Transform art object(s) using a transformation matrix'
		return self._oleobj_.InvokeTypes(1414676814, LCID, 1, (24, 0), ((9, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),TransformationMatrix
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, ChangeLineWidths
			, TransformAbout)

	def Translate(self, DeltaX=defaultNamedOptArg, DeltaY=defaultNamedOptArg, TransformObjects=defaultNamedOptArg, TransformFillPatterns=defaultNamedOptArg
			, TransformFillGradients=defaultNamedOptArg, TransformStrokePattern=defaultNamedOptArg):
		'Reposition art object(s)'
		return self._oleobj_.InvokeTypes(1685018701, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),DeltaX
			, DeltaY, TransformObjects, TransformFillPatterns, TransformFillGradients, TransformStrokePattern
			)

	def ZOrder(self, ZOrderCmd=defaultNamedNotOptArg):
		'Arranges the art relative to other art in the group or layer'
		return self._oleobj_.InvokeTypes(1515147844, LCID, 1, (24, 0), ((3, 1),),ZOrderCmd
			)

	_prop_map_get_ = {
		"AbsoluteZOrderPosition": (1883331151, 2, (3, 0), (), "AbsoluteZOrderPosition", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtworkKnockout": (1883991659, 2, (3, 0), (), "ArtworkKnockout", None),
		"BlendingMode": (1883401293, 2, (3, 0), (), "BlendingMode", None),
		# Method 'CompoundPathItem' returns object of type 'CompoundPathItem'
		"CompoundPathItem": (1148203057, 2, (9, 0), (), "CompoundPathItem", '{95CD20BE-AD72-11D3-B086-0010A4F5C335}'),
		"ControlBounds": (1634291288, 2, (12, 0), (), "ControlBounds", None),
		"Editable": (1883325796, 2, (11, 0), (), "Editable", None),
		"GeometricBounds": (1634288199, 2, (12, 0), (), "GeometricBounds", None),
		# Method 'GraphItem' returns object of type 'GraphItem'
		"GraphItem": (1148203058, 2, (9, 0), (), "GraphItem", '{4C78DFB7-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'GroupItem' returns object of type 'GroupItem'
		"GroupItem": (1148203059, 2, (9, 0), (), "GroupItem", '{95CD20C6-AD72-11D3-B086-0010A4F5C335}'),
		"Height": (1884506216, 2, (5, 0), (), "Height", None),
		"Hidden": (1634289732, 2, (11, 0), (), "Hidden", None),
		"IsIsolated": (1883861871, 2, (11, 0), (), "IsIsolated", None),
		# Method 'Layer' returns object of type 'Layer'
		"Layer": (1667320921, 2, (9, 0), (), "Layer", '{95CD20AC-AD72-11D3-B086-0010A4F5C335}'),
		"Left": (1279608404, 2, (5, 0), (), "Left", None),
		"Locked": (1634290763, 2, (11, 0), (), "Locked", None),
		# Method 'MeshItem' returns object of type 'MeshItem'
		"MeshItem": (1148203060, 2, (9, 0), (), "MeshItem", '{95CD20C4-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Note": (1634291284, 2, (8, 0), (), "Note", None),
		"Opacity": (1884049264, 2, (5, 0), (), "Opacity", None),
		"PageItem": (1396927603, 2, (9, 0), (), "PageItem", None),
		"PageItemType": (1954115685, 2, (3, 0), (), "PageItemType", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		# Method 'PathItem' returns object of type 'PathItem'
		"PathItem": (1148203061, 2, (9, 0), (), "PathItem", '{95CD20C0-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PathItems' returns object of type 'PathItems'
		"PathItems": (1667321921, 2, (9, 0), (), "PathItems", '{95CD20E1-AD72-11D3-B086-0010A4F5C335}'),
		"PixelAligned": (1884307820, 2, (11, 0), (), "PixelAligned", None),
		# Method 'PlacedItem' returns object of type 'PlacedItem'
		"PlacedItem": (1148203062, 2, (9, 0), (), "PlacedItem", '{95CD20C3-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PluginItem' returns object of type 'PluginItem'
		"PluginItem": (1148203063, 2, (9, 0), (), "PluginItem", '{95CD20C5-AD72-11D3-B086-0010A4F5C335}'),
		"Position": (1885425779, 2, (12, 0), (), "Position", None),
		# Method 'RasterItem' returns object of type 'RasterItem'
		"RasterItem": (1148203064, 2, (9, 0), (), "RasterItem", '{95CD20C2-AD72-11D3-B086-0010A4F5C335}'),
		"Selected": (1936026723, 2, (11, 0), (), "Selected", None),
		"Sliced": (1883329388, 2, (11, 0), (), "Sliced", None),
		# Method 'SymbolItem' returns object of type 'SymbolItem'
		"SymbolItem": (1148203065, 2, (9, 0), (), "SymbolItem", '{4C78DFC3-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'Tags' returns object of type 'Tags'
		"Tags": (1667322951, 2, (9, 0), (), "Tags", '{95CD20EB-AD72-11D3-B086-0010A4F5C335}'),
		"Top": (1414484000, 2, (5, 0), (), "Top", None),
		"URL": (1884639820, 2, (8, 0), (), "URL", None),
		"VisibilityVariable": (1884703062, 2, (12, 0), (), "VisibilityVariable", None),
		"VisibleBounds": (1634293314, 2, (12, 0), (), "VisibleBounds", None),
		"Width": (1884506231, 2, (5, 0), (), "Width", None),
		"WrapInside": (1884583753, 2, (11, 0), (), "WrapInside", None),
		"WrapOffset": (1884583759, 2, (5, 0), (), "WrapOffset", None),
		"Wrapped": (1886672722, 2, (11, 0), (), "Wrapped", None),
		"ZOrderPosition": (1884966736, 2, (3, 0), (), "ZOrderPosition", None),
	}
	_prop_map_put_ = {
		"ArtworkKnockout": ((1883991659, LCID, 4, 0),()),
		"BlendingMode": ((1883401293, LCID, 4, 0),()),
		"Height": ((1884506216, LCID, 4, 0),()),
		"Hidden": ((1634289732, LCID, 4, 0),()),
		"IsIsolated": ((1883861871, LCID, 4, 0),()),
		"Left": ((1279608404, LCID, 4, 0),()),
		"Locked": ((1634290763, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"Note": ((1634291284, LCID, 4, 0),()),
		"Opacity": ((1884049264, LCID, 4, 0),()),
		"PixelAligned": ((1884307820, LCID, 4, 0),()),
		"Position": ((1885425779, LCID, 4, 0),()),
		"Selected": ((1936026723, LCID, 4, 0),()),
		"Sliced": ((1883329388, LCID, 4, 0),()),
		"Top": ((1414484000, LCID, 4, 0),()),
		"URL": ((1884639820, LCID, 4, 0),()),
		"VisibilityVariable": ((1884703062, LCID, 4, 0),()),
		"Width": ((1884506231, LCID, 4, 0),()),
		"WrapInside": ((1884583753, LCID, 4, 0),()),
		"WrapOffset": ((1884583759, LCID, 4, 0),()),
		"Wrapped": ((1886672722, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class CompoundPathItems(DispatchBaseClass):
	'A collection of compound path items'
	CLSID = IID('{95CD20E3-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	# Result is of type CompoundPathItem
	def Add(self):
		'create a compound path item'
		ret = self._oleobj_.InvokeTypes(1667318627, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{95CD20BE-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type CompoundPathItem
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20BE-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20BE-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20BE-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class DataSet(DispatchBaseClass):
	'A set of variables and their associated dynamic data which will be used for dynamic publishing'
	CLSID = IID('{4C78DFA5-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = None

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def Display(self):
		'displays the dynamic data that has been captured in the dataset.'
		return self._oleobj_.InvokeTypes(1833194320, LCID, 1, (24, 0), (),)

	def Update(self):
		're-apply the dynamic data of the active dataset to the artboard'
		return self._oleobj_.InvokeTypes(1883525973, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"Name": ((1886282093, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class DataSets(DispatchBaseClass):
	'A collection of datasets'
	CLSID = IID('{4C78DFAB-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = None

	# Result is of type DataSet
	def Add(self):
		'create a data set'
		ret = self._oleobj_.InvokeTypes(1950634868, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{4C78DFA5-7A09-11D4-81A0-00C04F60ECCC}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type DataSet
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{4C78DFA5-7A09-11D4-81A0-00C04F60ECCC}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{4C78DFA5-7A09-11D4-81A0-00C04F60ECCC}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{4C78DFA5-7A09-11D4-81A0-00C04F60ECCC}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Document(DispatchBaseClass):
	'A document'
	CLSID = IID('{95CD20AB-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def Activate(self):
		'Activate the first window associated with the document'
		return self._oleobj_.InvokeTypes(1633907830, LCID, 1, (24, 0), (),)

	def Close(self, Saving=defaultNamedOptArg):
		'Close the specified document(s)'
		return self._oleobj_.InvokeTypes(1668050803, LCID, 1, (24, 0), ((12, 17),),Saving
			)

	def ConvertCoordinate(self, Coordinate=defaultNamedNotOptArg, Source=defaultNamedNotOptArg, Destination=defaultNamedNotOptArg):
		'Converts the coordinate system of a single point from one coordinate system to another.'
		return self._ApplyTypes_(1130590052, 1, (12, 0), ((12, 1), (3, 1), (3, 1)), 'ConvertCoordinate', None,Coordinate
			, Source, Destination)

	def Copy(self):
		'Copy selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668247673, LCID, 1, (24, 0), (),)

	def Cut(self):
		'Cut selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668641824, LCID, 1, (24, 0), (),)

	def Export(self, ExportFile=defaultNamedNotOptArg, ExportFormat=defaultNamedNotOptArg, Options=defaultNamedOptArg):
		'Export the specified document(s)'
		return self._oleobj_.InvokeTypes(1162112867, LCID, 1, (24, 0), ((8, 1), (3, 1), (12, 17)),ExportFile
			, ExportFormat, Options)

	def ExportPDFPreset(self, File=defaultNamedNotOptArg):
		'save all PDF presets to a file'
		return self._oleobj_.InvokeTypes(1631932755, LCID, 1, (24, 0), ((8, 1),),File
			)

	def ExportPerspectiveGridPreset(self, File=defaultNamedNotOptArg):
		'saves all perspective grid presets to a file'
		return self._oleobj_.InvokeTypes(1348825168, LCID, 1, (24, 0), ((8, 1),),File
			)

	def ExportPrintPreset(self, File=defaultNamedNotOptArg):
		'export the current print setting to the preset file'
		return self._oleobj_.InvokeTypes(1631932499, LCID, 1, (24, 0), ((8, 1),),File
			)

	def ExportSelectedArtwork(self, ExportFile=defaultNamedNotOptArg):
		'Export the selection as Ai file'
		return self._oleobj_.InvokeTypes(1163093313, LCID, 1, (24, 0), ((8, 1),),ExportFile
			)

	def ExportSelectionAsPNG(self, ExportFile=defaultNamedNotOptArg, Options=defaultNamedOptArg):
		'Export the selection as PNG file'
		return self._oleobj_.InvokeTypes(1163093356, LCID, 1, (24, 0), ((8, 1), (12, 17)),ExportFile
			, Options)

	def ExportVariables(self, File=defaultNamedNotOptArg):
		'Save datasets into an XML library. The datasets contain variables and their associated dynamic data'
		return self._oleobj_.InvokeTypes(1634288982, LCID, 1, (24, 0), ((8, 1),),File
			)

	def FitArtboardToSelectedArt(self, Index=defaultNamedOptArg):
		'Change the artboard to selected art bounds.'
		return self._oleobj_.InvokeTypes(1432441665, LCID, 1, (11, 0), ((12, 17),),Index
			)

	def GetPerspectiveActivePlane(self):
		'Gets the active plane of the active perspective grid of the document'
		return self._oleobj_.InvokeTypes(1348952400, LCID, 1, (3, 0), (),)

	def HidePerspectiveGrid(self):
		'Hides the current active perspective grid for the document, if there is visible perspective grid.'
		return self._oleobj_.InvokeTypes(1349021767, LCID, 1, (11, 0), (),)

	def ImageCapture(self, ImageFile=defaultNamedNotOptArg, ClipBounds=defaultNamedOptArg, Options=defaultNamedOptArg):
		'capture the artwork content inside the clip bound as raster image, and write out the captured image data into the target image file.'
		return self._oleobj_.InvokeTypes(1632193859, LCID, 1, (24, 0), ((8, 1), (12, 17), (12, 17)),ImageFile
			, ClipBounds, Options)

	def ImportCharacterStyles(self, FileSpec=defaultNamedNotOptArg):
		'load the character styles from the Illustrator file'
		return self._oleobj_.InvokeTypes(1634289987, LCID, 1, (24, 0), ((8, 1),),FileSpec
			)

	def ImportFileIntoDocument(self, ImportFile=defaultNamedNotOptArg, IsLinked=defaultNamedNotOptArg, LibraryName=defaultNamedOptArg, ItemName=defaultNamedOptArg
			, ElementRef=defaultNamedOptArg, ModifiedTime=defaultNamedOptArg, CreationTime=defaultNamedOptArg, AdobeStockId=defaultNamedOptArg, AdobeStockLicense=defaultNamedOptArg):
		'Import the file into current Ai document'
		return self._oleobj_.InvokeTypes(1229351276, LCID, 1, (24, 0), ((8, 1), (11, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),ImportFile
			, IsLinked, LibraryName, ItemName, ElementRef, ModifiedTime
			, CreationTime, AdobeStockId, AdobeStockLicense)

	def ImportPDFPreset(self, FileSpec=defaultNamedNotOptArg, ReplacingPreset=defaultNamedOptArg):
		'load all PDF presets from a file'
		return self._oleobj_.InvokeTypes(1632194899, LCID, 1, (24, 0), ((8, 1), (12, 17)),FileSpec
			, ReplacingPreset)

	def ImportParagraphStyles(self, FileSpec=defaultNamedNotOptArg):
		'load the paragraph styles from the Illustrator file'
		return self._oleobj_.InvokeTypes(1634290000, LCID, 1, (24, 0), ((8, 1),),FileSpec
			)

	def ImportPerspectiveGridPreset(self, FileSpec=defaultNamedNotOptArg, PerspectivePreset=defaultNamedOptArg):
		'loads mentioned perspective grid preset, if preset name is specified, else loads all(if no preset name is specified) presets, from the specified file'
		return self._oleobj_.InvokeTypes(1349087312, LCID, 1, (24, 0), ((8, 1), (12, 17)),FileSpec
			, PerspectivePreset)

	def ImportPrintPreset(self, PrintPreset=defaultNamedNotOptArg, FileSpec=defaultNamedNotOptArg):
		'apply the named print preset from the file to the current print setting'
		return self._oleobj_.InvokeTypes(1632194643, LCID, 1, (24, 0), ((8, 1), (8, 1)),PrintPreset
			, FileSpec)

	def ImportVariables(self, FileSpec=defaultNamedNotOptArg):
		'Import a library containing datasets, variables and their associated dynamic data. Importing variables will overwrite existing variables and datasets'
		return self._oleobj_.InvokeTypes(1634290006, LCID, 1, (24, 0), ((8, 1),),FileSpec
			)

	def Paste(self):
		'Paste clipboard into the document'
		return self._oleobj_.InvokeTypes(1885434740, LCID, 1, (24, 0), (),)

	def PrintOut(self, Options=defaultNamedOptArg):
		'Print the document'
		return self._oleobj_.InvokeTypes(1097417552, LCID, 1, (24, 0), ((12, 17),),Options
			)

	def ProcessGesture(self, GesturePointsFile=defaultNamedNotOptArg):
		'Process a gesture based on input points'
		return self._oleobj_.InvokeTypes(1346851698, LCID, 1, (24, 0), ((8, 1),),GesturePointsFile
			)

	def Rasterize(self, SourceArt=defaultNamedNotOptArg, ClipBounds=defaultNamedOptArg, Options=defaultNamedOptArg):
		'rasterize the source art(s) within the specified clip bounds. The source art(s) are disposed as a result of the rasterization.'
		ret = self._oleobj_.InvokeTypes(1800552787, LCID, 1, (9, 0), ((12, 1), (12, 17), (12, 17)),SourceArt
			, ClipBounds, Options)
		if ret is not None:
			ret = Dispatch(ret, 'Rasterize', None)
		return ret

	def RearrangeArtboards(self, ArtboardLayout=defaultNamedOptArg, ArtboardRowsOrCols=defaultNamedOptArg, ArtboardSpacing=defaultNamedOptArg, ArtboardMoveArtwork=defaultNamedOptArg):
		'Rearrange Artboards in the document'
		return self._oleobj_.InvokeTypes(1919238498, LCID, 1, (11, 0), ((12, 17), (12, 17), (12, 17), (12, 17)),ArtboardLayout
			, ArtboardRowsOrCols, ArtboardSpacing, ArtboardMoveArtwork)

	def Save(self):
		'Save the document'
		return self._oleobj_.InvokeTypes(1097417555, LCID, 1, (24, 0), (),)

	def SaveAs(self, SaveIn=defaultNamedNotOptArg, Options=defaultNamedOptArg):
		'Save the document with specific save options'
		return self._oleobj_.InvokeTypes(1398161747, LCID, 1, (24, 0), ((8, 1), (12, 17)),SaveIn
			, Options)

	def SelectObjectsOnActiveArtboard(self):
		'Select art objects in active artboard.'
		return self._oleobj_.InvokeTypes(1936671074, LCID, 1, (11, 0), (),)

	def SelectPerspectivePreset(self, PerspectivePreset=defaultNamedNotOptArg):
		'Selects a predefined preset to define grid for the current document.'
		return self._oleobj_.InvokeTypes(1399878224, LCID, 1, (11, 0), ((8, 1),),PerspectivePreset
			)

	def SetDefaultFillColor(self, arg0=defaultUnnamedArg):
		'default fill color'
		return self._oleobj_.InvokeTypes(1147749955, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetDefaultStrokeColor(self, arg0=defaultUnnamedArg):
		'default stroke color'
		return self._oleobj_.InvokeTypes(1147753283, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetPerspectiveActivePlane(self, PerspectiveGridPlane=defaultNamedNotOptArg):
		'Sets the active perspective plane for the active grid of the document.'
		return self._oleobj_.InvokeTypes(1349738832, LCID, 1, (11, 0), ((3, 1),),PerspectiveGridPlane
			)

	def SetRasterEffectSettings(self, arg0=defaultUnnamedArg):
		'The document raster effects settings'
		return self._oleobj_.InvokeTypes(1884439891, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def ShowPerspectiveGrid(self):
		'Shows the current active perspective grid for the document, if no active perspective grid then shows the default perspective grid for the document'
		return self._oleobj_.InvokeTypes(1349742663, LCID, 1, (11, 0), (),)

	def WindowCapture(self, ImageFile=defaultNamedNotOptArg, WindowSize=defaultNamedNotOptArg):
		'capture the current document window to the target TIFF image file.'
		return self._oleobj_.InvokeTypes(1632196419, LCID, 1, (24, 0), ((8, 1), (12, 1)),ImageFile
			, WindowSize)

	_prop_map_get_ = {
		# Method 'ActiveDataSet' returns object of type 'DataSet'
		"ActiveDataSet": (1883521348, 2, (9, 0), (), "ActiveDataSet", '{4C78DFA5-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'ActiveLayer' returns object of type 'Layer'
		"ActiveLayer": (1634288460, 2, (9, 0), (), "ActiveLayer", '{95CD20AC-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'ActiveView' returns object of type 'View'
		"ActiveView": (1634288470, 2, (9, 0), (), "ActiveView", '{95CD20AD-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'Artboards' returns object of type 'Artboards'
		"Artboards": (1682533681, 2, (9, 0), (), "Artboards", '{091ADAF8-D422-11DB-8314-0800200C9A66}'),
		# Method 'Brushes' returns object of type 'Brushes'
		"Brushes": (1667318354, 2, (9, 0), (), "Brushes", '{95CD20E8-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'CharacterStyles' returns object of type 'CharacterStyles'
		"CharacterStyles": (1665356628, 2, (9, 0), (), "CharacterStyles", '{255CD590-0FBF-4345-94F5-871C4021D6BF}'),
		"ColorProfileName": (1883459662, 2, (8, 0), (), "ColorProfileName", None),
		# Method 'CompoundPathItems' returns object of type 'CompoundPathItems'
		"CompoundPathItems": (1667318608, 2, (9, 0), (), "CompoundPathItems", '{95CD20E3-AD72-11D3-B086-0010A4F5C335}'),
		"CropBox": (2021147458, 2, (12, 0), (), "CropBox", None),
		"CropStyle": (2021147475, 2, (3, 0), (), "CropStyle", None),
		# Method 'DataSets' returns object of type 'DataSets'
		"DataSets": (1950634868, 2, (9, 0), (), "DataSets", '{4C78DFAB-7A09-11D4-81A0-00C04F60ECCC}'),
		"DefaultFillColor": (1147749955, 2, (9, 0), (), "DefaultFillColor", None),
		"DefaultFillOverprint": (1147749967, 2, (11, 0), (), "DefaultFillOverprint", None),
		"DefaultFilled": (1147749968, 2, (11, 0), (), "DefaultFilled", None),
		"DefaultStrokeCap": (1147749240, 2, (3, 0), (), "DefaultStrokeCap", None),
		"DefaultStrokeColor": (1147753283, 2, (9, 0), (), "DefaultStrokeColor", None),
		"DefaultStrokeDashOffset": (1147749455, 2, (5, 0), (), "DefaultStrokeDashOffset", None),
		"DefaultStrokeDashes": (1147749459, 2, (12, 0), (), "DefaultStrokeDashes", None),
		"DefaultStrokeJoin": (1147751022, 2, (3, 0), (), "DefaultStrokeJoin", None),
		"DefaultStrokeMiterLimit": (1147751800, 2, (5, 0), (), "DefaultStrokeMiterLimit", None),
		"DefaultStrokeOverprint": (1147753295, 2, (11, 0), (), "DefaultStrokeOverprint", None),
		"DefaultStrokeWidth": (1147753303, 2, (5, 0), (), "DefaultStrokeWidth", None),
		"DefaultStroked": (1147753296, 2, (11, 0), (), "DefaultStroked", None),
		"DocumentColorSpace": (1667318611, 2, (3, 0), (), "DocumentColorSpace", None),
		# Method 'EmbeddedItems' returns object of type 'EmbeddedItems'
		"EmbeddedItems": (1667319116, 2, (9, 0), (), "EmbeddedItems", '{FF327E57-2EDA-4934-B3FD-CF470C62989D}'),
		"FullName": (1634289235, 2, (8, 0), (), "FullName", None),
		"GeometricBounds": (1634288199, 2, (12, 0), (), "GeometricBounds", None),
		# Method 'Gradients' returns object of type 'Gradients'
		"Gradients": (1667319620, 2, (9, 0), (), "Gradients", '{95CD20DD-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'GraphItems' returns object of type 'GraphItems'
		"GraphItems": (1665617992, 2, (9, 0), (), "GraphItems", '{4C78DFB4-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'GraphicStyles' returns object of type 'GraphicStyles'
		"GraphicStyles": (1667318099, 2, (9, 0), (), "GraphicStyles", '{95CD20E9-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'GroupItems' returns object of type 'GroupItems'
		"GroupItems": (1667319632, 2, (9, 0), (), "GroupItems", '{95CD20DF-AD72-11D3-B086-0010A4F5C335}'),
		"Height": (1884506216, 2, (5, 0), (), "Height", None),
		"InkList": (1884309836, 2, (12, 0), (), "InkList", None),
		"KinsokuSet": (1883984719, 2, (12, 0), (), "KinsokuSet", None),
		# Method 'Layers' returns object of type 'Layers'
		"Layers": (1667320921, 2, (9, 0), (), "Layers", '{95CD20DC-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'LegacyTextItems' returns object of type 'LegacyTextItems'
		"LegacyTextItems": (1665946697, 2, (9, 0), (), "LegacyTextItems", '{4C78DFE9-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'MeshItems' returns object of type 'MeshItems'
		"MeshItems": (1666011976, 2, (9, 0), (), "MeshItems", '{95CD20EE-AD72-11D3-B086-0010A4F5C335}'),
		"MojikumiSet": (1884113481, 2, (12, 0), (), "MojikumiSet", None),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		# Method 'NonNativeItems' returns object of type 'NonNativeItems'
		"NonNativeItems": (1665552233, 2, (9, 0), (), "NonNativeItems", '{9157F2B0-D436-4AC6-9769-94DC89E6EC92}'),
		"OutputResolution": (2021150546, 2, (5, 0), (), "OutputResolution", None),
		# Method 'PageItems' returns object of type 'PageItems'
		"PageItems": (1667318100, 2, (9, 0), (), "PageItems", '{95CD20E0-AD72-11D3-B086-0010A4F5C335}'),
		"PageOrigin": (2021150799, 2, (12, 0), (), "PageOrigin", None),
		# Method 'ParagraphStyles' returns object of type 'ParagraphStyles'
		"ParagraphStyles": (1666208596, 2, (9, 0), (), "ParagraphStyles", '{0E3BF58B-A0F2-4776-9CD0-279FCB26009E}'),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"Path": (1883664464, 2, (8, 0), (), "Path", None),
		# Method 'PathItems' returns object of type 'PathItems'
		"PathItems": (1667321921, 2, (9, 0), (), "PathItems", '{95CD20E1-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'Patterns' returns object of type 'Patterns'
		"Patterns": (1667321940, 2, (9, 0), (), "Patterns", '{95CD20E7-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PlacedItems' returns object of type 'PlacedItems'
		"PlacedItems": (1667321932, 2, (9, 0), (), "PlacedItems", '{95CD20ED-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PluginItems' returns object of type 'PluginItems'
		"PluginItems": (1666206791, 2, (9, 0), (), "PluginItems", '{95CD20EF-AD72-11D3-B086-0010A4F5C335}'),
		"PrintTiles": (2021150804, 2, (11, 0), (), "PrintTiles", None),
		# Method 'RasterEffectSettings' returns object of type '_RasterEffectOptions'
		"RasterEffectSettings": (1884439891, 2, (9, 0), (), "RasterEffectSettings", '{246086F4-6F43-4D2B-A0BA-3BFB0E484DDF}'),
		# Method 'RasterItems' returns object of type 'RasterItems'
		"RasterItems": (1667322433, 2, (9, 0), (), "RasterItems", '{95CD20EC-AD72-11D3-B086-0010A4F5C335}'),
		"RulerOrigin": (2021151311, 2, (12, 0), (), "RulerOrigin", None),
		"RulerUnits": (2021151317, 2, (3, 0), (), "RulerUnits", None),
		"Saved": (1883657078, 2, (11, 0), (), "Saved", None),
		"Selection": (1936026725, 2, (12, 0), (), "Selection", None),
		"ShowPlacedImages": (2021151568, 2, (11, 0), (), "ShowPlacedImages", None),
		"SplitLongPaths": (2021151564, 2, (11, 0), (), "SplitLongPaths", None),
		# Method 'Spots' returns object of type 'Spots'
		"Spots": (1667318595, 2, (9, 0), (), "Spots", '{95CD20D9-AD72-11D3-B086-0010A4F5C335}'),
		"Stationery": (1886613604, 2, (11, 0), (), "Stationery", None),
		# Method 'Stories' returns object of type 'Stories'
		"Stories": (1666405455, 2, (9, 0), (), "Stories", '{0E9E7B8C-BF29-4A10-9B1C-9F292FDAB07A}'),
		# Method 'SwatchGroups' returns object of type 'SwatchGroups'
		"SwatchGroups": (1666402162, 2, (9, 0), (), "SwatchGroups", '{558EF46F-A352-4A0D-9B1C-A2F6118FE611}'),
		# Method 'Swatches' returns object of type 'Swatches'
		"Swatches": (1667322711, 2, (9, 0), (), "Swatches", '{95CD20DA-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'SymbolItems' returns object of type 'SymbolItems'
		"SymbolItems": (1667322697, 2, (9, 0), (), "SymbolItems", '{4C78DFC6-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'Symbols' returns object of type 'Symbols'
		"Symbols": (1667322713, 2, (9, 0), (), "Symbols", '{4C78DFC9-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'Tags' returns object of type 'Tags'
		"Tags": (1667322951, 2, (9, 0), (), "Tags", '{95CD20EB-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'TextFrames' returns object of type 'TextFrames'
		"TextFrames": (1666472033, 2, (9, 0), (), "TextFrames", '{3CC63F1C-EA9C-4636-A16C-63808C42691E}'),
		"TileFullPages": (2021151814, 2, (11, 0), (), "TileFullPages", None),
		"UseDefaultScreen": (2021147731, 2, (11, 0), (), "UseDefaultScreen", None),
		# Method 'Variables' returns object of type 'Variables'
		"Variables": (1951818098, 2, (9, 0), (), "Variables", '{4C78DFA8-7A09-11D4-81A0-00C04F60ECCC}'),
		"VariablesLocked": (1883524182, 2, (11, 0), (), "VariablesLocked", None),
		# Method 'Views' returns object of type 'Views'
		"Views": (1667318870, 2, (9, 0), (), "Views", '{95CD20F0-AD72-11D3-B086-0010A4F5C335}'),
		"VisibleBounds": (1634293314, 2, (12, 0), (), "VisibleBounds", None),
		"Width": (1884506231, 2, (5, 0), (), "Width", None),
		"XMPString": (1884835152, 2, (8, 0), (), "XMPString", None),
	}
	_prop_map_put_ = {
		"ActiveDataSet": ((1883521348, LCID, 4, 0),()),
		"ActiveLayer": ((1634288460, LCID, 4, 0),()),
		"CropBox": ((2021147458, LCID, 4, 0),()),
		"CropStyle": ((2021147475, LCID, 4, 0),()),
		"DefaultFillColor": ((1147749955, LCID, 4, 0),()),
		"DefaultFillOverprint": ((1147749967, LCID, 4, 0),()),
		"DefaultFilled": ((1147749968, LCID, 4, 0),()),
		"DefaultStrokeCap": ((1147749240, LCID, 4, 0),()),
		"DefaultStrokeColor": ((1147753283, LCID, 4, 0),()),
		"DefaultStrokeDashOffset": ((1147749455, LCID, 4, 0),()),
		"DefaultStrokeDashes": ((1147749459, LCID, 4, 0),()),
		"DefaultStrokeJoin": ((1147751022, LCID, 4, 0),()),
		"DefaultStrokeMiterLimit": ((1147751800, LCID, 4, 0),()),
		"DefaultStrokeOverprint": ((1147753295, LCID, 4, 0),()),
		"DefaultStrokeWidth": ((1147753303, LCID, 4, 0),()),
		"DefaultStroked": ((1147753296, LCID, 4, 0),()),
		"PageOrigin": ((2021150799, LCID, 4, 0),()),
		"RasterEffectSettings": ((1884439891, LCID, 4, 0),()),
		"RulerOrigin": ((2021151311, LCID, 4, 0),()),
		"Saved": ((1883657078, LCID, 4, 0),()),
		"Selection": ((1936026725, LCID, 4, 0),()),
		"VariablesLocked": ((1883524182, LCID, 4, 0),()),
		"XMPString": ((1884835152, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Documents(DispatchBaseClass):
	'A collection of documents'
	CLSID = IID('{95CD20DB-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	# Result is of type Document
	def Add(self, DocumentColorSpace=defaultNamedOptArg, Width=defaultNamedOptArg, Height=defaultNamedOptArg, NumArtboards=defaultNamedOptArg
			, ArtboardLayout=defaultNamedOptArg, ArtboardSpacing=defaultNamedOptArg, ArtboardRowsOrCols=defaultNamedOptArg):
		'a document'
		ret = self._oleobj_.InvokeTypes(1685021557, LCID, 1, (9, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),DocumentColorSpace
			, Width, Height, NumArtboards, ArtboardLayout, ArtboardSpacing
			, ArtboardRowsOrCols)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{95CD20AB-AD72-11D3-B086-0010A4F5C335}')
		return ret

	# Result is of type Document
	def AddDocument(self, StartupPreset=defaultNamedNotOptArg, PresetSettings=defaultNamedOptArg, ShowOptionsDialog=defaultNamedOptArg):
		'Create a new document from a preset'
		ret = self._oleobj_.InvokeTypes(1665421123, LCID, 1, (9, 0), ((8, 1), (12, 17), (12, 17)),StartupPreset
			, PresetSettings, ShowOptionsDialog)
		if ret is not None:
			ret = Dispatch(ret, 'AddDocument', '{95CD20AB-AD72-11D3-B086-0010A4F5C335}')
		return ret

	# Result is of type Document
	def AddDocumentWithDialogOption(self, StartupPreset=defaultNamedNotOptArg, ShowOptionsDialog=defaultNamedOptArg):
		'create a document from the preset with option to throw dialog to customize present settings'
		ret = self._oleobj_.InvokeTypes(1665226575, LCID, 1, (9, 0), ((8, 1), (12, 17)),StartupPreset
			, ShowOptionsDialog)
		if ret is not None:
			ret = Dispatch(ret, 'AddDocumentWithDialogOption', '{95CD20AB-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Arrange(self, LayoutStyle=defaultNamedNotOptArg):
		'Arranges the documents in the specified style'
		return self._oleobj_.InvokeTypes(1799438660, LCID, 1, (11, 0), ((3, 1),),LayoutStyle
			)

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type Document
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20AB-AD72-11D3-B086-0010A4F5C335}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20AB-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20AB-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class EmbedItem(DispatchBaseClass):
	'Embedded artwork item'
	CLSID = IID('{96C13549-5237-4492-8345-2DB9FB6512BE}')
	coclass_clsid = None

	def ApplyEffect(self, LiveEffectXML=defaultNamedNotOptArg):
		'Apply effect to selected artItem'
		return self._oleobj_.InvokeTypes(1799447892, LCID, 1, (24, 0), ((8, 1),),LiveEffectXML
			)

	def BringInPerspective(self, PositionX=defaultNamedNotOptArg, PositionY=defaultNamedNotOptArg, PerspectiveGridPlane=defaultNamedNotOptArg):
		'Place art object(s)in perspective grid at spedified perspective plane and coordinate'
		return self._oleobj_.InvokeTypes(1685013072, LCID, 1, (24, 0), ((5, 1), (5, 1), (3, 1)),PositionX
			, PositionY, PerspectiveGridPlane)

	def Copy(self):
		'Copy selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668247673, LCID, 1, (24, 0), (),)

	def Cut(self):
		'Cut selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668641824, LCID, 1, (24, 0), (),)

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def Duplicate(self, RelativeObject=defaultNamedOptArg, InsertionLocation=defaultNamedOptArg):
		'create a duplicate of the object'
		ret = self._oleobj_.InvokeTypes(1668050798, LCID, 1, (9, 0), ((12, 17), (12, 17)),RelativeObject
			, InsertionLocation)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', None)
		return ret

	def Move(self, RelativeObject=defaultNamedNotOptArg, InsertionLocation=defaultNamedNotOptArg):
		'move the object'
		return self._oleobj_.InvokeTypes(1836021349, LCID, 1, (24, 0), ((9, 1), (3, 1)),RelativeObject
			, InsertionLocation)

	def MoveAfter(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in behind object'
		return self._oleobj_.InvokeTypes(1299596641, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveBefore(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in front of object'
		return self._oleobj_.InvokeTypes(1299596642, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveToBeginning(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to beginning of container'
		return self._oleobj_.InvokeTypes(1299596646, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def MoveToEnd(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to end of container'
		return self._oleobj_.InvokeTypes(1299596645, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def Resize(self, ScaleX=defaultNamedNotOptArg, ScaleY=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg
			, ChangeFillGradients=defaultNamedOptArg, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, ScaleAbout=defaultNamedOptArg):
		'Scale art object(s)'
		return self._oleobj_.InvokeTypes(1685017421, LCID, 1, (24, 0), ((5, 1), (5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),ScaleX
			, ScaleY, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern
			, ChangeLineWidths, ScaleAbout)

	def Rotate(self, Angle=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, RotateAbout=defaultNamedOptArg):
		'Rotate art object(s)'
		return self._oleobj_.InvokeTypes(1685017165, LCID, 1, (24, 0), ((5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),Angle
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, RotateAbout
			)

	def SendScriptMessage(self, PluginName=defaultNamedNotOptArg, MessageSelector=defaultNamedNotOptArg, InputString=defaultNamedNotOptArg):
		'sends the script message to the required plugin'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1632850765, LCID, 1, (8, 0), ((8, 1), (8, 1), (8, 1)),PluginName
			, MessageSelector, InputString)

	def Transform(self, TransformationMatrix=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, TransformAbout=defaultNamedOptArg):
		'Transform art object(s) using a transformation matrix'
		return self._oleobj_.InvokeTypes(1414676814, LCID, 1, (24, 0), ((9, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),TransformationMatrix
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, ChangeLineWidths
			, TransformAbout)

	def Translate(self, DeltaX=defaultNamedOptArg, DeltaY=defaultNamedOptArg, TransformObjects=defaultNamedOptArg, TransformFillPatterns=defaultNamedOptArg
			, TransformFillGradients=defaultNamedOptArg, TransformStrokePattern=defaultNamedOptArg):
		'Reposition art object(s)'
		return self._oleobj_.InvokeTypes(1685018701, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),DeltaX
			, DeltaY, TransformObjects, TransformFillPatterns, TransformFillGradients, TransformStrokePattern
			)

	def ZOrder(self, ZOrderCmd=defaultNamedNotOptArg):
		'Arranges the art relative to other art in the group or layer'
		return self._oleobj_.InvokeTypes(1515147844, LCID, 1, (24, 0), ((3, 1),),ZOrderCmd
			)

	_prop_map_get_ = {
		"AbsoluteZOrderPosition": (1883331151, 2, (3, 0), (), "AbsoluteZOrderPosition", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtworkKnockout": (1883991659, 2, (3, 0), (), "ArtworkKnockout", None),
		"BlendingMode": (1883401293, 2, (3, 0), (), "BlendingMode", None),
		# Method 'CompoundPathItem' returns object of type 'CompoundPathItem'
		"CompoundPathItem": (1148203057, 2, (9, 0), (), "CompoundPathItem", '{95CD20BE-AD72-11D3-B086-0010A4F5C335}'),
		"ControlBounds": (1634291288, 2, (12, 0), (), "ControlBounds", None),
		"Editable": (1883325796, 2, (11, 0), (), "Editable", None),
		"File": (1634289235, 2, (8, 0), (), "File", None),
		"GeometricBounds": (1634288199, 2, (12, 0), (), "GeometricBounds", None),
		# Method 'GraphItem' returns object of type 'GraphItem'
		"GraphItem": (1148203058, 2, (9, 0), (), "GraphItem", '{4C78DFB7-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'GroupItem' returns object of type 'GroupItem'
		"GroupItem": (1148203059, 2, (9, 0), (), "GroupItem", '{95CD20C6-AD72-11D3-B086-0010A4F5C335}'),
		"Height": (1884506216, 2, (5, 0), (), "Height", None),
		"Hidden": (1634289732, 2, (11, 0), (), "Hidden", None),
		"IsIsolated": (1883861871, 2, (11, 0), (), "IsIsolated", None),
		# Method 'Layer' returns object of type 'Layer'
		"Layer": (1667320921, 2, (9, 0), (), "Layer", '{95CD20AC-AD72-11D3-B086-0010A4F5C335}'),
		"Left": (1279608404, 2, (5, 0), (), "Left", None),
		"Locked": (1634290763, 2, (11, 0), (), "Locked", None),
		# Method 'MeshItem' returns object of type 'MeshItem'
		"MeshItem": (1148203060, 2, (9, 0), (), "MeshItem", '{95CD20C4-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Note": (1634291284, 2, (8, 0), (), "Note", None),
		"Opacity": (1884049264, 2, (5, 0), (), "Opacity", None),
		"PageItem": (1396927603, 2, (9, 0), (), "PageItem", None),
		"PageItemType": (1954115685, 2, (3, 0), (), "PageItemType", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		# Method 'PathItem' returns object of type 'PathItem'
		"PathItem": (1148203061, 2, (9, 0), (), "PathItem", '{95CD20C0-AD72-11D3-B086-0010A4F5C335}'),
		"PixelAligned": (1884307820, 2, (11, 0), (), "PixelAligned", None),
		# Method 'PlacedItem' returns object of type 'PlacedItem'
		"PlacedItem": (1148203062, 2, (9, 0), (), "PlacedItem", '{95CD20C3-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PluginItem' returns object of type 'PluginItem'
		"PluginItem": (1148203063, 2, (9, 0), (), "PluginItem", '{95CD20C5-AD72-11D3-B086-0010A4F5C335}'),
		"Position": (1885425779, 2, (12, 0), (), "Position", None),
		# Method 'RasterItem' returns object of type 'RasterItem'
		"RasterItem": (1148203064, 2, (9, 0), (), "RasterItem", '{95CD20C2-AD72-11D3-B086-0010A4F5C335}'),
		"Selected": (1936026723, 2, (11, 0), (), "Selected", None),
		"Sliced": (1883329388, 2, (11, 0), (), "Sliced", None),
		# Method 'SymbolItem' returns object of type 'SymbolItem'
		"SymbolItem": (1148203065, 2, (9, 0), (), "SymbolItem", '{4C78DFC3-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'Tags' returns object of type 'Tags'
		"Tags": (1667322951, 2, (9, 0), (), "Tags", '{95CD20EB-AD72-11D3-B086-0010A4F5C335}'),
		"Top": (1414484000, 2, (5, 0), (), "Top", None),
		"URL": (1884639820, 2, (8, 0), (), "URL", None),
		"VisibilityVariable": (1884703062, 2, (12, 0), (), "VisibilityVariable", None),
		"VisibleBounds": (1634293314, 2, (12, 0), (), "VisibleBounds", None),
		"Width": (1884506231, 2, (5, 0), (), "Width", None),
		"WrapInside": (1884583753, 2, (11, 0), (), "WrapInside", None),
		"WrapOffset": (1884583759, 2, (5, 0), (), "WrapOffset", None),
		"Wrapped": (1886672722, 2, (11, 0), (), "Wrapped", None),
		"ZOrderPosition": (1884966736, 2, (3, 0), (), "ZOrderPosition", None),
	}
	_prop_map_put_ = {
		"ArtworkKnockout": ((1883991659, LCID, 4, 0),()),
		"BlendingMode": ((1883401293, LCID, 4, 0),()),
		"File": ((1634289235, LCID, 4, 0),()),
		"Height": ((1884506216, LCID, 4, 0),()),
		"Hidden": ((1634289732, LCID, 4, 0),()),
		"IsIsolated": ((1883861871, LCID, 4, 0),()),
		"Left": ((1279608404, LCID, 4, 0),()),
		"Locked": ((1634290763, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"Note": ((1634291284, LCID, 4, 0),()),
		"Opacity": ((1884049264, LCID, 4, 0),()),
		"PixelAligned": ((1884307820, LCID, 4, 0),()),
		"Position": ((1885425779, LCID, 4, 0),()),
		"Selected": ((1936026723, LCID, 4, 0),()),
		"Sliced": ((1883329388, LCID, 4, 0),()),
		"Top": ((1414484000, LCID, 4, 0),()),
		"URL": ((1884639820, LCID, 4, 0),()),
		"VisibilityVariable": ((1884703062, LCID, 4, 0),()),
		"Width": ((1884506231, LCID, 4, 0),()),
		"WrapInside": ((1884583753, LCID, 4, 0),()),
		"WrapOffset": ((1884583759, LCID, 4, 0),()),
		"Wrapped": ((1886672722, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class EmbeddedItems(DispatchBaseClass):
	'EmbeddedItems Collection'
	CLSID = IID('{FF327E57-2EDA-4934-B3FD-CF470C62989D}')
	coclass_clsid = None

	# Result is of type EmbedItem
	def Add(self):
		'create an embedded item'
		ret = self._oleobj_.InvokeTypes(1665486924, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{96C13549-5237-4492-8345-2DB9FB6512BE}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type EmbedItem
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{96C13549-5237-4492-8345-2DB9FB6512BE}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{96C13549-5237-4492-8345-2DB9FB6512BE}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{96C13549-5237-4492-8345-2DB9FB6512BE}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Gradient(DispatchBaseClass):
	'A gradient'
	CLSID = IID('{95CD20AE-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'GradientStops' returns object of type 'GradientStops'
		"GradientStops": (1667319635, 2, (9, 0), (), "GradientStops", '{95CD20DE-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"Type": (1734628473, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Name": ((1886282093, LCID, 4, 0),()),
		"Type": ((1734628473, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class GradientStop(DispatchBaseClass):
	'A gradient stop'
	CLSID = IID('{95CD20AF-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def SetColor(self, arg0=defaultUnnamedArg):
		'the color linked to this gradient stop'
		return self._oleobj_.InvokeTypes(1668246642, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Color": (1668246642, 2, (9, 0), (), "Color", None),
		"MidPoint": (2019642704, 2, (5, 0), (), "MidPoint", None),
		"Opacity": (2017940303, 2, (5, 0), (), "Opacity", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"RampPoint": (2019643984, 2, (5, 0), (), "RampPoint", None),
	}
	_prop_map_put_ = {
		"Color": ((1668246642, LCID, 4, 0),()),
		"MidPoint": ((2019642704, LCID, 4, 0),()),
		"Opacity": ((2017940303, LCID, 4, 0),()),
		"RampPoint": ((2019643984, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class GradientStops(DispatchBaseClass):
	'A collection of gradient stops'
	CLSID = IID('{95CD20DE-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	# Result is of type GradientStop
	def Add(self):
		'create a gradient stop'
		ret = self._oleobj_.InvokeTypes(1667319635, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{95CD20AF-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type GradientStop
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20AF-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20AF-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20AF-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Gradients(DispatchBaseClass):
	'A collection of gradients'
	CLSID = IID('{95CD20DD-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	# Result is of type Gradient
	def Add(self):
		'create a gradient'
		ret = self._oleobj_.InvokeTypes(1667319620, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{95CD20AE-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type Gradient
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20AE-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20AE-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20AE-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class GraphItem(DispatchBaseClass):
	'Graph artwork item'
	CLSID = IID('{4C78DFB7-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = None

	def ApplyEffect(self, LiveEffectXML=defaultNamedNotOptArg):
		'Apply effect to selected artItem'
		return self._oleobj_.InvokeTypes(1799447892, LCID, 1, (24, 0), ((8, 1),),LiveEffectXML
			)

	def BringInPerspective(self, PositionX=defaultNamedNotOptArg, PositionY=defaultNamedNotOptArg, PerspectiveGridPlane=defaultNamedNotOptArg):
		'Place art object(s)in perspective grid at spedified perspective plane and coordinate'
		return self._oleobj_.InvokeTypes(1685013072, LCID, 1, (24, 0), ((5, 1), (5, 1), (3, 1)),PositionX
			, PositionY, PerspectiveGridPlane)

	def Copy(self):
		'Copy selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668247673, LCID, 1, (24, 0), (),)

	def Cut(self):
		'Cut selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668641824, LCID, 1, (24, 0), (),)

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def Duplicate(self, RelativeObject=defaultNamedOptArg, InsertionLocation=defaultNamedOptArg):
		'create a duplicate of the object'
		ret = self._oleobj_.InvokeTypes(1668050798, LCID, 1, (9, 0), ((12, 17), (12, 17)),RelativeObject
			, InsertionLocation)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', None)
		return ret

	def Move(self, RelativeObject=defaultNamedNotOptArg, InsertionLocation=defaultNamedNotOptArg):
		'move the object'
		return self._oleobj_.InvokeTypes(1836021349, LCID, 1, (24, 0), ((9, 1), (3, 1)),RelativeObject
			, InsertionLocation)

	def MoveAfter(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in behind object'
		return self._oleobj_.InvokeTypes(1299596641, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveBefore(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in front of object'
		return self._oleobj_.InvokeTypes(1299596642, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveToBeginning(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to beginning of container'
		return self._oleobj_.InvokeTypes(1299596646, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def MoveToEnd(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to end of container'
		return self._oleobj_.InvokeTypes(1299596645, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def Resize(self, ScaleX=defaultNamedNotOptArg, ScaleY=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg
			, ChangeFillGradients=defaultNamedOptArg, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, ScaleAbout=defaultNamedOptArg):
		'Scale art object(s)'
		return self._oleobj_.InvokeTypes(1685017421, LCID, 1, (24, 0), ((5, 1), (5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),ScaleX
			, ScaleY, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern
			, ChangeLineWidths, ScaleAbout)

	def Rotate(self, Angle=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, RotateAbout=defaultNamedOptArg):
		'Rotate art object(s)'
		return self._oleobj_.InvokeTypes(1685017165, LCID, 1, (24, 0), ((5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),Angle
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, RotateAbout
			)

	def SendScriptMessage(self, PluginName=defaultNamedNotOptArg, MessageSelector=defaultNamedNotOptArg, InputString=defaultNamedNotOptArg):
		'sends the script message to the required plugin'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1632850765, LCID, 1, (8, 0), ((8, 1), (8, 1), (8, 1)),PluginName
			, MessageSelector, InputString)

	def Transform(self, TransformationMatrix=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, TransformAbout=defaultNamedOptArg):
		'Transform art object(s) using a transformation matrix'
		return self._oleobj_.InvokeTypes(1414676814, LCID, 1, (24, 0), ((9, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),TransformationMatrix
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, ChangeLineWidths
			, TransformAbout)

	def Translate(self, DeltaX=defaultNamedOptArg, DeltaY=defaultNamedOptArg, TransformObjects=defaultNamedOptArg, TransformFillPatterns=defaultNamedOptArg
			, TransformFillGradients=defaultNamedOptArg, TransformStrokePattern=defaultNamedOptArg):
		'Reposition art object(s)'
		return self._oleobj_.InvokeTypes(1685018701, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),DeltaX
			, DeltaY, TransformObjects, TransformFillPatterns, TransformFillGradients, TransformStrokePattern
			)

	def ZOrder(self, ZOrderCmd=defaultNamedNotOptArg):
		'Arranges the art relative to other art in the group or layer'
		return self._oleobj_.InvokeTypes(1515147844, LCID, 1, (24, 0), ((3, 1),),ZOrderCmd
			)

	_prop_map_get_ = {
		"AbsoluteZOrderPosition": (1883331151, 2, (3, 0), (), "AbsoluteZOrderPosition", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtworkKnockout": (1883991659, 2, (3, 0), (), "ArtworkKnockout", None),
		"BlendingMode": (1883401293, 2, (3, 0), (), "BlendingMode", None),
		# Method 'CompoundPathItem' returns object of type 'CompoundPathItem'
		"CompoundPathItem": (1148203057, 2, (9, 0), (), "CompoundPathItem", '{95CD20BE-AD72-11D3-B086-0010A4F5C335}'),
		"ContentVariable": (1883459414, 2, (12, 0), (), "ContentVariable", None),
		"ControlBounds": (1634291288, 2, (12, 0), (), "ControlBounds", None),
		"Editable": (1883325796, 2, (11, 0), (), "Editable", None),
		"GeometricBounds": (1634288199, 2, (12, 0), (), "GeometricBounds", None),
		# Method 'GraphItem' returns object of type 'GraphItem'
		"GraphItem": (1148203058, 2, (9, 0), (), "GraphItem", '{4C78DFB7-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'GroupItem' returns object of type 'GroupItem'
		"GroupItem": (1148203059, 2, (9, 0), (), "GroupItem", '{95CD20C6-AD72-11D3-B086-0010A4F5C335}'),
		"Height": (1884506216, 2, (5, 0), (), "Height", None),
		"Hidden": (1634289732, 2, (11, 0), (), "Hidden", None),
		"IsIsolated": (1883861871, 2, (11, 0), (), "IsIsolated", None),
		# Method 'Layer' returns object of type 'Layer'
		"Layer": (1667320921, 2, (9, 0), (), "Layer", '{95CD20AC-AD72-11D3-B086-0010A4F5C335}'),
		"Left": (1279608404, 2, (5, 0), (), "Left", None),
		"Locked": (1634290763, 2, (11, 0), (), "Locked", None),
		# Method 'MeshItem' returns object of type 'MeshItem'
		"MeshItem": (1148203060, 2, (9, 0), (), "MeshItem", '{95CD20C4-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Note": (1634291284, 2, (8, 0), (), "Note", None),
		"Opacity": (1884049264, 2, (5, 0), (), "Opacity", None),
		"PageItem": (1396927603, 2, (9, 0), (), "PageItem", None),
		"PageItemType": (1954115685, 2, (3, 0), (), "PageItemType", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		# Method 'PathItem' returns object of type 'PathItem'
		"PathItem": (1148203061, 2, (9, 0), (), "PathItem", '{95CD20C0-AD72-11D3-B086-0010A4F5C335}'),
		"PixelAligned": (1884307820, 2, (11, 0), (), "PixelAligned", None),
		# Method 'PlacedItem' returns object of type 'PlacedItem'
		"PlacedItem": (1148203062, 2, (9, 0), (), "PlacedItem", '{95CD20C3-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PluginItem' returns object of type 'PluginItem'
		"PluginItem": (1148203063, 2, (9, 0), (), "PluginItem", '{95CD20C5-AD72-11D3-B086-0010A4F5C335}'),
		"Position": (1885425779, 2, (12, 0), (), "Position", None),
		# Method 'RasterItem' returns object of type 'RasterItem'
		"RasterItem": (1148203064, 2, (9, 0), (), "RasterItem", '{95CD20C2-AD72-11D3-B086-0010A4F5C335}'),
		"Selected": (1936026723, 2, (11, 0), (), "Selected", None),
		"Sliced": (1883329388, 2, (11, 0), (), "Sliced", None),
		# Method 'SymbolItem' returns object of type 'SymbolItem'
		"SymbolItem": (1148203065, 2, (9, 0), (), "SymbolItem", '{4C78DFC3-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'Tags' returns object of type 'Tags'
		"Tags": (1667322951, 2, (9, 0), (), "Tags", '{95CD20EB-AD72-11D3-B086-0010A4F5C335}'),
		"Top": (1414484000, 2, (5, 0), (), "Top", None),
		"URL": (1884639820, 2, (8, 0), (), "URL", None),
		"VisibilityVariable": (1884703062, 2, (12, 0), (), "VisibilityVariable", None),
		"VisibleBounds": (1634293314, 2, (12, 0), (), "VisibleBounds", None),
		"Width": (1884506231, 2, (5, 0), (), "Width", None),
		"WrapInside": (1884583753, 2, (11, 0), (), "WrapInside", None),
		"WrapOffset": (1884583759, 2, (5, 0), (), "WrapOffset", None),
		"Wrapped": (1886672722, 2, (11, 0), (), "Wrapped", None),
		"ZOrderPosition": (1884966736, 2, (3, 0), (), "ZOrderPosition", None),
	}
	_prop_map_put_ = {
		"ArtworkKnockout": ((1883991659, LCID, 4, 0),()),
		"BlendingMode": ((1883401293, LCID, 4, 0),()),
		"ContentVariable": ((1883459414, LCID, 4, 0),()),
		"Height": ((1884506216, LCID, 4, 0),()),
		"Hidden": ((1634289732, LCID, 4, 0),()),
		"IsIsolated": ((1883861871, LCID, 4, 0),()),
		"Left": ((1279608404, LCID, 4, 0),()),
		"Locked": ((1634290763, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"Note": ((1634291284, LCID, 4, 0),()),
		"Opacity": ((1884049264, LCID, 4, 0),()),
		"PixelAligned": ((1884307820, LCID, 4, 0),()),
		"Position": ((1885425779, LCID, 4, 0),()),
		"Selected": ((1936026723, LCID, 4, 0),()),
		"Sliced": ((1883329388, LCID, 4, 0),()),
		"Top": ((1414484000, LCID, 4, 0),()),
		"URL": ((1884639820, LCID, 4, 0),()),
		"VisibilityVariable": ((1884703062, LCID, 4, 0),()),
		"Width": ((1884506231, LCID, 4, 0),()),
		"WrapInside": ((1884583753, LCID, 4, 0),()),
		"WrapOffset": ((1884583759, LCID, 4, 0),()),
		"Wrapped": ((1886672722, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class GraphItems(DispatchBaseClass):
	CLSID = IID('{4C78DFB4-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = None

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type GraphItem
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{4C78DFB7-7A09-11D4-81A0-00C04F60ECCC}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{4C78DFB7-7A09-11D4-81A0-00C04F60ECCC}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{4C78DFB7-7A09-11D4-81A0-00C04F60ECCC}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class GraphicStyle(DispatchBaseClass):
	'An art style'
	CLSID = IID('{95CD20BB-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def ApplyTo(self, ArtItem=defaultNamedNotOptArg):
		'Apply a brush or art style to object(s)'
		return self._oleobj_.InvokeTypes(1097886841, LCID, 1, (24, 0), ((12, 1),),ArtItem
			)

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def MergeTo(self, ArtItem=defaultNamedNotOptArg):
		'Merge an art style to object(s) current style(s)'
		return self._oleobj_.InvokeTypes(1298494055, LCID, 1, (24, 0), ((12, 1),),ArtItem
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"Name": ((1886282093, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class GraphicStyles(DispatchBaseClass):
	'A collection of art styles'
	CLSID = IID('{95CD20E9-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type GraphicStyle
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20BB-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20BB-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20BB-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class GroupItem(DispatchBaseClass):
	'An artwork group item'
	CLSID = IID('{95CD20C6-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def ApplyEffect(self, LiveEffectXML=defaultNamedNotOptArg):
		'Apply effect to selected artItem'
		return self._oleobj_.InvokeTypes(1799447892, LCID, 1, (24, 0), ((8, 1),),LiveEffectXML
			)

	def BringInPerspective(self, PositionX=defaultNamedNotOptArg, PositionY=defaultNamedNotOptArg, PerspectiveGridPlane=defaultNamedNotOptArg):
		'Place art object(s)in perspective grid at spedified perspective plane and coordinate'
		return self._oleobj_.InvokeTypes(1685013072, LCID, 1, (24, 0), ((5, 1), (5, 1), (3, 1)),PositionX
			, PositionY, PerspectiveGridPlane)

	def Copy(self):
		'Copy selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668247673, LCID, 1, (24, 0), (),)

	def Cut(self):
		'Cut selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668641824, LCID, 1, (24, 0), (),)

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def Duplicate(self, RelativeObject=defaultNamedOptArg, InsertionLocation=defaultNamedOptArg):
		'create a duplicate of the object'
		ret = self._oleobj_.InvokeTypes(1668050798, LCID, 1, (9, 0), ((12, 17), (12, 17)),RelativeObject
			, InsertionLocation)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', None)
		return ret

	def Move(self, RelativeObject=defaultNamedNotOptArg, InsertionLocation=defaultNamedNotOptArg):
		'move the object'
		return self._oleobj_.InvokeTypes(1836021349, LCID, 1, (24, 0), ((9, 1), (3, 1)),RelativeObject
			, InsertionLocation)

	def MoveAfter(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in behind object'
		return self._oleobj_.InvokeTypes(1299596641, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveBefore(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in front of object'
		return self._oleobj_.InvokeTypes(1299596642, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveToBeginning(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to beginning of container'
		return self._oleobj_.InvokeTypes(1299596646, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def MoveToEnd(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to end of container'
		return self._oleobj_.InvokeTypes(1299596645, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def Paste(self):
		'Paste clipboard into the group'
		return self._oleobj_.InvokeTypes(1885434740, LCID, 1, (24, 0), (),)

	def Resize(self, ScaleX=defaultNamedNotOptArg, ScaleY=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg
			, ChangeFillGradients=defaultNamedOptArg, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, ScaleAbout=defaultNamedOptArg):
		'Scale art object(s)'
		return self._oleobj_.InvokeTypes(1685017421, LCID, 1, (24, 0), ((5, 1), (5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),ScaleX
			, ScaleY, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern
			, ChangeLineWidths, ScaleAbout)

	def Rotate(self, Angle=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, RotateAbout=defaultNamedOptArg):
		'Rotate art object(s)'
		return self._oleobj_.InvokeTypes(1685017165, LCID, 1, (24, 0), ((5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),Angle
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, RotateAbout
			)

	def SendScriptMessage(self, PluginName=defaultNamedNotOptArg, MessageSelector=defaultNamedNotOptArg, InputString=defaultNamedNotOptArg):
		'sends the script message to the required plugin'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1632850765, LCID, 1, (8, 0), ((8, 1), (8, 1), (8, 1)),PluginName
			, MessageSelector, InputString)

	def Transform(self, TransformationMatrix=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, TransformAbout=defaultNamedOptArg):
		'Transform art object(s) using a transformation matrix'
		return self._oleobj_.InvokeTypes(1414676814, LCID, 1, (24, 0), ((9, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),TransformationMatrix
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, ChangeLineWidths
			, TransformAbout)

	def Translate(self, DeltaX=defaultNamedOptArg, DeltaY=defaultNamedOptArg, TransformObjects=defaultNamedOptArg, TransformFillPatterns=defaultNamedOptArg
			, TransformFillGradients=defaultNamedOptArg, TransformStrokePattern=defaultNamedOptArg):
		'Reposition art object(s)'
		return self._oleobj_.InvokeTypes(1685018701, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),DeltaX
			, DeltaY, TransformObjects, TransformFillPatterns, TransformFillGradients, TransformStrokePattern
			)

	def ZOrder(self, ZOrderCmd=defaultNamedNotOptArg):
		'Arranges the art relative to other art in the group or layer'
		return self._oleobj_.InvokeTypes(1515147844, LCID, 1, (24, 0), ((3, 1),),ZOrderCmd
			)

	_prop_map_get_ = {
		"AbsoluteZOrderPosition": (1883331151, 2, (3, 0), (), "AbsoluteZOrderPosition", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtworkKnockout": (1883991659, 2, (3, 0), (), "ArtworkKnockout", None),
		"BlendingMode": (1883401293, 2, (3, 0), (), "BlendingMode", None),
		"Clipped": (1634288496, 2, (11, 0), (), "Clipped", None),
		# Method 'CompoundPathItem' returns object of type 'CompoundPathItem'
		"CompoundPathItem": (1148203057, 2, (9, 0), (), "CompoundPathItem", '{95CD20BE-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'CompoundPathItems' returns object of type 'CompoundPathItems'
		"CompoundPathItems": (1667318608, 2, (9, 0), (), "CompoundPathItems", '{95CD20E3-AD72-11D3-B086-0010A4F5C335}'),
		"ControlBounds": (1634291288, 2, (12, 0), (), "ControlBounds", None),
		"Editable": (1883325796, 2, (11, 0), (), "Editable", None),
		"GeometricBounds": (1634288199, 2, (12, 0), (), "GeometricBounds", None),
		# Method 'GraphItem' returns object of type 'GraphItem'
		"GraphItem": (1148203058, 2, (9, 0), (), "GraphItem", '{4C78DFB7-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'GraphItems' returns object of type 'GraphItems'
		"GraphItems": (1665617992, 2, (9, 0), (), "GraphItems", '{4C78DFB4-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'GroupItem' returns object of type 'GroupItem'
		"GroupItem": (1148203059, 2, (9, 0), (), "GroupItem", '{95CD20C6-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'GroupItems' returns object of type 'GroupItems'
		"GroupItems": (1667319632, 2, (9, 0), (), "GroupItems", '{95CD20DF-AD72-11D3-B086-0010A4F5C335}'),
		"Height": (1884506216, 2, (5, 0), (), "Height", None),
		"Hidden": (1634289732, 2, (11, 0), (), "Hidden", None),
		"IsIsolated": (1883861871, 2, (11, 0), (), "IsIsolated", None),
		# Method 'Layer' returns object of type 'Layer'
		"Layer": (1667320921, 2, (9, 0), (), "Layer", '{95CD20AC-AD72-11D3-B086-0010A4F5C335}'),
		"Left": (1279608404, 2, (5, 0), (), "Left", None),
		# Method 'LegacyTextItems' returns object of type 'LegacyTextItems'
		"LegacyTextItems": (1665946697, 2, (9, 0), (), "LegacyTextItems", '{4C78DFE9-7A09-11D4-81A0-00C04F60ECCC}'),
		"Locked": (1634290763, 2, (11, 0), (), "Locked", None),
		# Method 'MeshItem' returns object of type 'MeshItem'
		"MeshItem": (1148203060, 2, (9, 0), (), "MeshItem", '{95CD20C4-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'MeshItems' returns object of type 'MeshItems'
		"MeshItems": (1666011976, 2, (9, 0), (), "MeshItems", '{95CD20EE-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		# Method 'NonNativeItems' returns object of type 'NonNativeItems'
		"NonNativeItems": (1665552233, 2, (9, 0), (), "NonNativeItems", '{9157F2B0-D436-4AC6-9769-94DC89E6EC92}'),
		"Note": (1634291284, 2, (8, 0), (), "Note", None),
		"Opacity": (1884049264, 2, (5, 0), (), "Opacity", None),
		"PageItem": (1396927603, 2, (9, 0), (), "PageItem", None),
		"PageItemType": (1954115685, 2, (3, 0), (), "PageItemType", None),
		# Method 'PageItems' returns object of type 'PageItems'
		"PageItems": (1667318100, 2, (9, 0), (), "PageItems", '{95CD20E0-AD72-11D3-B086-0010A4F5C335}'),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		# Method 'PathItem' returns object of type 'PathItem'
		"PathItem": (1148203061, 2, (9, 0), (), "PathItem", '{95CD20C0-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PathItems' returns object of type 'PathItems'
		"PathItems": (1667321921, 2, (9, 0), (), "PathItems", '{95CD20E1-AD72-11D3-B086-0010A4F5C335}'),
		"PixelAligned": (1884307820, 2, (11, 0), (), "PixelAligned", None),
		# Method 'PlacedItem' returns object of type 'PlacedItem'
		"PlacedItem": (1148203062, 2, (9, 0), (), "PlacedItem", '{95CD20C3-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PlacedItems' returns object of type 'PlacedItems'
		"PlacedItems": (1667321932, 2, (9, 0), (), "PlacedItems", '{95CD20ED-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PluginItem' returns object of type 'PluginItem'
		"PluginItem": (1148203063, 2, (9, 0), (), "PluginItem", '{95CD20C5-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PluginItems' returns object of type 'PluginItems'
		"PluginItems": (1666206791, 2, (9, 0), (), "PluginItems", '{95CD20EF-AD72-11D3-B086-0010A4F5C335}'),
		"Position": (1885425779, 2, (12, 0), (), "Position", None),
		# Method 'RasterItem' returns object of type 'RasterItem'
		"RasterItem": (1148203064, 2, (9, 0), (), "RasterItem", '{95CD20C2-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'RasterItems' returns object of type 'RasterItems'
		"RasterItems": (1667322433, 2, (9, 0), (), "RasterItems", '{95CD20EC-AD72-11D3-B086-0010A4F5C335}'),
		"Selected": (1936026723, 2, (11, 0), (), "Selected", None),
		"Sliced": (1883329388, 2, (11, 0), (), "Sliced", None),
		# Method 'SymbolItem' returns object of type 'SymbolItem'
		"SymbolItem": (1148203065, 2, (9, 0), (), "SymbolItem", '{4C78DFC3-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'SymbolItems' returns object of type 'SymbolItems'
		"SymbolItems": (1667322697, 2, (9, 0), (), "SymbolItems", '{4C78DFC6-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'Tags' returns object of type 'Tags'
		"Tags": (1667322951, 2, (9, 0), (), "Tags", '{95CD20EB-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'TextFrames' returns object of type 'TextFrames'
		"TextFrames": (1666472033, 2, (9, 0), (), "TextFrames", '{3CC63F1C-EA9C-4636-A16C-63808C42691E}'),
		"Top": (1414484000, 2, (5, 0), (), "Top", None),
		"URL": (1884639820, 2, (8, 0), (), "URL", None),
		"VisibilityVariable": (1884703062, 2, (12, 0), (), "VisibilityVariable", None),
		"VisibleBounds": (1634293314, 2, (12, 0), (), "VisibleBounds", None),
		"Width": (1884506231, 2, (5, 0), (), "Width", None),
		"WrapInside": (1884583753, 2, (11, 0), (), "WrapInside", None),
		"WrapOffset": (1884583759, 2, (5, 0), (), "WrapOffset", None),
		"Wrapped": (1886672722, 2, (11, 0), (), "Wrapped", None),
		"ZOrderPosition": (1884966736, 2, (3, 0), (), "ZOrderPosition", None),
	}
	_prop_map_put_ = {
		"ArtworkKnockout": ((1883991659, LCID, 4, 0),()),
		"BlendingMode": ((1883401293, LCID, 4, 0),()),
		"Clipped": ((1634288496, LCID, 4, 0),()),
		"Height": ((1884506216, LCID, 4, 0),()),
		"Hidden": ((1634289732, LCID, 4, 0),()),
		"IsIsolated": ((1883861871, LCID, 4, 0),()),
		"Left": ((1279608404, LCID, 4, 0),()),
		"Locked": ((1634290763, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"Note": ((1634291284, LCID, 4, 0),()),
		"Opacity": ((1884049264, LCID, 4, 0),()),
		"PixelAligned": ((1884307820, LCID, 4, 0),()),
		"Position": ((1885425779, LCID, 4, 0),()),
		"Selected": ((1936026723, LCID, 4, 0),()),
		"Sliced": ((1883329388, LCID, 4, 0),()),
		"Top": ((1414484000, LCID, 4, 0),()),
		"URL": ((1884639820, LCID, 4, 0),()),
		"VisibilityVariable": ((1884703062, LCID, 4, 0),()),
		"Width": ((1884506231, LCID, 4, 0),()),
		"WrapInside": ((1884583753, LCID, 4, 0),()),
		"WrapOffset": ((1884583759, LCID, 4, 0),()),
		"Wrapped": ((1886672722, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class GroupItems(DispatchBaseClass):
	'A collection of group items'
	CLSID = IID('{95CD20DF-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	# Result is of type GroupItem
	def Add(self):
		'create a group item'
		ret = self._oleobj_.InvokeTypes(1667319651, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{95CD20C6-AD72-11D3-B086-0010A4F5C335}')
		return ret

	# Result is of type GroupItem
	def CreateFromFile(self, ImageFile=defaultNamedNotOptArg):
		'create a group item from a vector graphics file'
		ret = self._oleobj_.InvokeTypes(1164789347, LCID, 1, (9, 0), ((8, 1),),ImageFile
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateFromFile', '{95CD20C6-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type GroupItem
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20C6-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20C6-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20C6-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class InsertionPoint(DispatchBaseClass):
	'a location between characters, used to insert new text objects'
	CLSID = IID('{4C78DFE7-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'Characters' returns object of type 'Characters'
		"Characters": (1667784992, 2, (9, 0), (), "Characters", '{95CD20D5-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'Lines' returns object of type 'Lines'
		"Lines": (1668049262, 2, (9, 0), (), "Lines", '{95CD20D7-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'Paragraphs' returns object of type 'Paragraphs'
		"Paragraphs": (1668309362, 2, (9, 0), (), "Paragraphs", '{95CD20D8-AD72-11D3-B086-0010A4F5C335}'),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		# Method 'Story' returns object of type 'Story'
		"Story": (1666405455, 2, (9, 0), (), "Story", '{8507C961-DE07-440E-A2D8-6D48247ABF79}'),
		# Method 'TextRanges' returns object of type 'TextRanges'
		"TextRanges": (1668577396, 2, (9, 0), (), "TextRanges", '{20899C07-06F0-4803-BD2A-4059F9764852}'),
		# Method 'Words' returns object of type 'Words'
		"Words": (1668771698, 2, (9, 0), (), "Words", '{95CD20D6-AD72-11D3-B086-0010A4F5C335}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class InsertionPoints(DispatchBaseClass):
	'A collection of insertion points'
	CLSID = IID('{20899C08-06F0-4803-BD2A-4059F9764852}')
	coclass_clsid = None

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type InsertionPoint
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{4C78DFE7-7A09-11D4-81A0-00C04F60ECCC}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{4C78DFE7-7A09-11D4-81A0-00C04F60ECCC}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{4C78DFE7-7A09-11D4-81A0-00C04F60ECCC}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Layer(DispatchBaseClass):
	'A layer'
	CLSID = IID('{95CD20AC-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def Move(self, RelativeObject=defaultNamedNotOptArg, InsertionLocation=defaultNamedNotOptArg):
		'move the object'
		return self._oleobj_.InvokeTypes(1836021349, LCID, 1, (24, 0), ((9, 1), (3, 1)),RelativeObject
			, InsertionLocation)

	def MoveAfter(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in behind object'
		return self._oleobj_.InvokeTypes(1299596641, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveBefore(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in front of object'
		return self._oleobj_.InvokeTypes(1299596642, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveToBeginning(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to beginning of container'
		return self._oleobj_.InvokeTypes(1299596646, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def MoveToEnd(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to end of container'
		return self._oleobj_.InvokeTypes(1299596645, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def Paste(self):
		'Paste clipboard into the layer'
		return self._oleobj_.InvokeTypes(1885434740, LCID, 1, (24, 0), (),)

	def SetColor(self, arg0=defaultUnnamedArg):
		'color used when outlining artwork in this layer'
		return self._oleobj_.InvokeTypes(1668246642, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def ZOrder(self, ZOrderCmd=defaultNamedNotOptArg):
		'Arranges the layer relative to other layers'
		return self._oleobj_.InvokeTypes(1515147844, LCID, 1, (24, 0), ((3, 1),),ZOrderCmd
			)

	_prop_map_get_ = {
		"AbsoluteZOrderPosition": (1883331151, 2, (3, 0), (), "AbsoluteZOrderPosition", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtworkKnockout": (1883991659, 2, (3, 0), (), "ArtworkKnockout", None),
		"BlendingMode": (1883401293, 2, (3, 0), (), "BlendingMode", None),
		# Method 'Color' returns object of type '_RGBColor'
		"Color": (1668246642, 2, (9, 0), (), "Color", '{95CD20B1-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'CompoundPathItems' returns object of type 'CompoundPathItems'
		"CompoundPathItems": (1667318608, 2, (9, 0), (), "CompoundPathItems", '{95CD20E3-AD72-11D3-B086-0010A4F5C335}'),
		"DimPlacedImages": (1634288713, 2, (11, 0), (), "DimPlacedImages", None),
		# Method 'GraphItems' returns object of type 'GraphItems'
		"GraphItems": (1665617992, 2, (9, 0), (), "GraphItems", '{4C78DFB4-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'GroupItems' returns object of type 'GroupItems'
		"GroupItems": (1667319632, 2, (9, 0), (), "GroupItems", '{95CD20DF-AD72-11D3-B086-0010A4F5C335}'),
		"HasSelectedArtwork": (1634280484, 2, (11, 0), (), "HasSelectedArtwork", None),
		"IsIsolated": (1883861871, 2, (11, 0), (), "IsIsolated", None),
		# Method 'Layers' returns object of type 'Layers'
		"Layers": (1667320921, 2, (9, 0), (), "Layers", '{95CD20DC-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'LegacyTextItems' returns object of type 'LegacyTextItems'
		"LegacyTextItems": (1665946697, 2, (9, 0), (), "LegacyTextItems", '{4C78DFE9-7A09-11D4-81A0-00C04F60ECCC}'),
		"Locked": (1634290763, 2, (11, 0), (), "Locked", None),
		# Method 'MeshItems' returns object of type 'MeshItems'
		"MeshItems": (1666011976, 2, (9, 0), (), "MeshItems", '{95CD20EE-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		# Method 'NonNativeItems' returns object of type 'NonNativeItems'
		"NonNativeItems": (1665552233, 2, (9, 0), (), "NonNativeItems", '{9157F2B0-D436-4AC6-9769-94DC89E6EC92}'),
		"Opacity": (1884049264, 2, (5, 0), (), "Opacity", None),
		# Method 'PageItems' returns object of type 'PageItems'
		"PageItems": (1667318100, 2, (9, 0), (), "PageItems", '{95CD20E0-AD72-11D3-B086-0010A4F5C335}'),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		# Method 'PathItems' returns object of type 'PathItems'
		"PathItems": (1667321921, 2, (9, 0), (), "PathItems", '{95CD20E1-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PlacedItems' returns object of type 'PlacedItems'
		"PlacedItems": (1667321932, 2, (9, 0), (), "PlacedItems", '{95CD20ED-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PluginItems' returns object of type 'PluginItems'
		"PluginItems": (1666206791, 2, (9, 0), (), "PluginItems", '{95CD20EF-AD72-11D3-B086-0010A4F5C335}'),
		"Preview": (1634291798, 2, (11, 0), (), "Preview", None),
		"Printable": (1634291796, 2, (11, 0), (), "Printable", None),
		# Method 'RasterItems' returns object of type 'RasterItems'
		"RasterItems": (1667322433, 2, (9, 0), (), "RasterItems", '{95CD20EC-AD72-11D3-B086-0010A4F5C335}'),
		"Sliced": (1883329388, 2, (11, 0), (), "Sliced", None),
		# Method 'SymbolItems' returns object of type 'SymbolItems'
		"SymbolItems": (1667322697, 2, (9, 0), (), "SymbolItems", '{4C78DFC6-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'TextFrames' returns object of type 'TextFrames'
		"TextFrames": (1666472033, 2, (9, 0), (), "TextFrames", '{3CC63F1C-EA9C-4636-A16C-63808C42691E}'),
		"Visible": (1886808435, 2, (11, 0), (), "Visible", None),
		"ZOrderPosition": (1884966736, 2, (3, 0), (), "ZOrderPosition", None),
	}
	_prop_map_put_ = {
		"ArtworkKnockout": ((1883991659, LCID, 4, 0),()),
		"BlendingMode": ((1883401293, LCID, 4, 0),()),
		"Color": ((1668246642, LCID, 4, 0),()),
		"DimPlacedImages": ((1634288713, LCID, 4, 0),()),
		"HasSelectedArtwork": ((1634280484, LCID, 4, 0),()),
		"IsIsolated": ((1883861871, LCID, 4, 0),()),
		"Locked": ((1634290763, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"Opacity": ((1884049264, LCID, 4, 0),()),
		"Preview": ((1634291798, LCID, 4, 0),()),
		"Printable": ((1634291796, LCID, 4, 0),()),
		"Sliced": ((1883329388, LCID, 4, 0),()),
		"Visible": ((1886808435, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Layers(DispatchBaseClass):
	'A collection of layers'
	CLSID = IID('{95CD20DC-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	# Result is of type Layer
	def Add(self):
		'create a layer'
		ret = self._oleobj_.InvokeTypes(1667320931, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{95CD20AC-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type Layer
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20AC-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20AC-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20AC-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class LegacyTextItem(DispatchBaseClass):
	'unconverted legacy text items from documents in pre-version 11 formats'
	CLSID = IID('{4C78DFE8-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = None

	def ApplyEffect(self, LiveEffectXML=defaultNamedNotOptArg):
		'Apply effect to selected artItem'
		return self._oleobj_.InvokeTypes(1799447892, LCID, 1, (24, 0), ((8, 1),),LiveEffectXML
			)

	def BringInPerspective(self, PositionX=defaultNamedNotOptArg, PositionY=defaultNamedNotOptArg, PerspectiveGridPlane=defaultNamedNotOptArg):
		'Place art object(s)in perspective grid at spedified perspective plane and coordinate'
		return self._oleobj_.InvokeTypes(1685013072, LCID, 1, (24, 0), ((5, 1), (5, 1), (3, 1)),PositionX
			, PositionY, PerspectiveGridPlane)

	# Result is of type GroupItem
	def ConvertToNative(self):
		'create a native text frame from a legacy text item. The original legacy text item is deleted.'
		ret = self._oleobj_.InvokeTypes(1131695700, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ConvertToNative', '{95CD20C6-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Copy(self):
		'Copy selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668247673, LCID, 1, (24, 0), (),)

	def Cut(self):
		'Cut selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668641824, LCID, 1, (24, 0), (),)

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def Duplicate(self, RelativeObject=defaultNamedOptArg, InsertionLocation=defaultNamedOptArg):
		'create a duplicate of the object'
		ret = self._oleobj_.InvokeTypes(1668050798, LCID, 1, (9, 0), ((12, 17), (12, 17)),RelativeObject
			, InsertionLocation)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', None)
		return ret

	def Move(self, RelativeObject=defaultNamedNotOptArg, InsertionLocation=defaultNamedNotOptArg):
		'move the object'
		return self._oleobj_.InvokeTypes(1836021349, LCID, 1, (24, 0), ((9, 1), (3, 1)),RelativeObject
			, InsertionLocation)

	def MoveAfter(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in behind object'
		return self._oleobj_.InvokeTypes(1299596641, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveBefore(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in front of object'
		return self._oleobj_.InvokeTypes(1299596642, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveToBeginning(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to beginning of container'
		return self._oleobj_.InvokeTypes(1299596646, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def MoveToEnd(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to end of container'
		return self._oleobj_.InvokeTypes(1299596645, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def Resize(self, ScaleX=defaultNamedNotOptArg, ScaleY=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg
			, ChangeFillGradients=defaultNamedOptArg, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, ScaleAbout=defaultNamedOptArg):
		'Scale art object(s)'
		return self._oleobj_.InvokeTypes(1685017421, LCID, 1, (24, 0), ((5, 1), (5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),ScaleX
			, ScaleY, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern
			, ChangeLineWidths, ScaleAbout)

	def Rotate(self, Angle=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, RotateAbout=defaultNamedOptArg):
		'Rotate art object(s)'
		return self._oleobj_.InvokeTypes(1685017165, LCID, 1, (24, 0), ((5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),Angle
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, RotateAbout
			)

	def SendScriptMessage(self, PluginName=defaultNamedNotOptArg, MessageSelector=defaultNamedNotOptArg, InputString=defaultNamedNotOptArg):
		'sends the script message to the required plugin'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1632850765, LCID, 1, (8, 0), ((8, 1), (8, 1), (8, 1)),PluginName
			, MessageSelector, InputString)

	def Transform(self, TransformationMatrix=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, TransformAbout=defaultNamedOptArg):
		'Transform art object(s) using a transformation matrix'
		return self._oleobj_.InvokeTypes(1414676814, LCID, 1, (24, 0), ((9, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),TransformationMatrix
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, ChangeLineWidths
			, TransformAbout)

	def Translate(self, DeltaX=defaultNamedOptArg, DeltaY=defaultNamedOptArg, TransformObjects=defaultNamedOptArg, TransformFillPatterns=defaultNamedOptArg
			, TransformFillGradients=defaultNamedOptArg, TransformStrokePattern=defaultNamedOptArg):
		'Reposition art object(s)'
		return self._oleobj_.InvokeTypes(1685018701, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),DeltaX
			, DeltaY, TransformObjects, TransformFillPatterns, TransformFillGradients, TransformStrokePattern
			)

	def ZOrder(self, ZOrderCmd=defaultNamedNotOptArg):
		'Arranges the art relative to other art in the group or layer'
		return self._oleobj_.InvokeTypes(1515147844, LCID, 1, (24, 0), ((3, 1),),ZOrderCmd
			)

	_prop_map_get_ = {
		"AbsoluteZOrderPosition": (1883331151, 2, (3, 0), (), "AbsoluteZOrderPosition", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtworkKnockout": (1883991659, 2, (3, 0), (), "ArtworkKnockout", None),
		"BlendingMode": (1883401293, 2, (3, 0), (), "BlendingMode", None),
		# Method 'CompoundPathItem' returns object of type 'CompoundPathItem'
		"CompoundPathItem": (1148203057, 2, (9, 0), (), "CompoundPathItem", '{95CD20BE-AD72-11D3-B086-0010A4F5C335}'),
		"ControlBounds": (1634291288, 2, (12, 0), (), "ControlBounds", None),
		"Converted": (1883468878, 2, (11, 0), (), "Converted", None),
		"Editable": (1883325796, 2, (11, 0), (), "Editable", None),
		"GeometricBounds": (1634288199, 2, (12, 0), (), "GeometricBounds", None),
		# Method 'GraphItem' returns object of type 'GraphItem'
		"GraphItem": (1148203058, 2, (9, 0), (), "GraphItem", '{4C78DFB7-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'GroupItem' returns object of type 'GroupItem'
		"GroupItem": (1148203059, 2, (9, 0), (), "GroupItem", '{95CD20C6-AD72-11D3-B086-0010A4F5C335}'),
		"Height": (1884506216, 2, (5, 0), (), "Height", None),
		"Hidden": (1634289732, 2, (11, 0), (), "Hidden", None),
		"IsIsolated": (1883861871, 2, (11, 0), (), "IsIsolated", None),
		# Method 'Layer' returns object of type 'Layer'
		"Layer": (1667320921, 2, (9, 0), (), "Layer", '{95CD20AC-AD72-11D3-B086-0010A4F5C335}'),
		"Left": (1279608404, 2, (5, 0), (), "Left", None),
		"Locked": (1634290763, 2, (11, 0), (), "Locked", None),
		# Method 'MeshItem' returns object of type 'MeshItem'
		"MeshItem": (1148203060, 2, (9, 0), (), "MeshItem", '{95CD20C4-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Note": (1634291284, 2, (8, 0), (), "Note", None),
		"Opacity": (1884049264, 2, (5, 0), (), "Opacity", None),
		"PageItem": (1396927603, 2, (9, 0), (), "PageItem", None),
		"PageItemType": (1954115685, 2, (3, 0), (), "PageItemType", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		# Method 'PathItem' returns object of type 'PathItem'
		"PathItem": (1148203061, 2, (9, 0), (), "PathItem", '{95CD20C0-AD72-11D3-B086-0010A4F5C335}'),
		"PixelAligned": (1884307820, 2, (11, 0), (), "PixelAligned", None),
		# Method 'PlacedItem' returns object of type 'PlacedItem'
		"PlacedItem": (1148203062, 2, (9, 0), (), "PlacedItem", '{95CD20C3-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PluginItem' returns object of type 'PluginItem'
		"PluginItem": (1148203063, 2, (9, 0), (), "PluginItem", '{95CD20C5-AD72-11D3-B086-0010A4F5C335}'),
		"Position": (1885425779, 2, (12, 0), (), "Position", None),
		# Method 'RasterItem' returns object of type 'RasterItem'
		"RasterItem": (1148203064, 2, (9, 0), (), "RasterItem", '{95CD20C2-AD72-11D3-B086-0010A4F5C335}'),
		"Selected": (1936026723, 2, (11, 0), (), "Selected", None),
		"Sliced": (1883329388, 2, (11, 0), (), "Sliced", None),
		# Method 'SymbolItem' returns object of type 'SymbolItem'
		"SymbolItem": (1148203065, 2, (9, 0), (), "SymbolItem", '{4C78DFC3-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'Tags' returns object of type 'Tags'
		"Tags": (1667322951, 2, (9, 0), (), "Tags", '{95CD20EB-AD72-11D3-B086-0010A4F5C335}'),
		"Top": (1414484000, 2, (5, 0), (), "Top", None),
		"URL": (1884639820, 2, (8, 0), (), "URL", None),
		"VisibilityVariable": (1884703062, 2, (12, 0), (), "VisibilityVariable", None),
		"VisibleBounds": (1634293314, 2, (12, 0), (), "VisibleBounds", None),
		"Width": (1884506231, 2, (5, 0), (), "Width", None),
		"WrapInside": (1884583753, 2, (11, 0), (), "WrapInside", None),
		"WrapOffset": (1884583759, 2, (5, 0), (), "WrapOffset", None),
		"Wrapped": (1886672722, 2, (11, 0), (), "Wrapped", None),
		"ZOrderPosition": (1884966736, 2, (3, 0), (), "ZOrderPosition", None),
	}
	_prop_map_put_ = {
		"ArtworkKnockout": ((1883991659, LCID, 4, 0),()),
		"BlendingMode": ((1883401293, LCID, 4, 0),()),
		"Height": ((1884506216, LCID, 4, 0),()),
		"Hidden": ((1634289732, LCID, 4, 0),()),
		"IsIsolated": ((1883861871, LCID, 4, 0),()),
		"Left": ((1279608404, LCID, 4, 0),()),
		"Locked": ((1634290763, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"Note": ((1634291284, LCID, 4, 0),()),
		"Opacity": ((1884049264, LCID, 4, 0),()),
		"PixelAligned": ((1884307820, LCID, 4, 0),()),
		"Position": ((1885425779, LCID, 4, 0),()),
		"Selected": ((1936026723, LCID, 4, 0),()),
		"Sliced": ((1883329388, LCID, 4, 0),()),
		"Top": ((1414484000, LCID, 4, 0),()),
		"URL": ((1884639820, LCID, 4, 0),()),
		"VisibilityVariable": ((1884703062, LCID, 4, 0),()),
		"Width": ((1884506231, LCID, 4, 0),()),
		"WrapInside": ((1884583753, LCID, 4, 0),()),
		"WrapOffset": ((1884583759, LCID, 4, 0),()),
		"Wrapped": ((1886672722, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class LegacyTextItems(DispatchBaseClass):
	'A collection of legacy text items'
	CLSID = IID('{4C78DFE9-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = None

	def ConvertToNative(self):
		'create text frames from all legacy text items. The original legacy text items will be deleted.'
		return self._oleobj_.InvokeTypes(1131695700, LCID, 1, (11, 0), (),)

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type LegacyTextItem
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{4C78DFE8-7A09-11D4-81A0-00C04F60ECCC}')
		return ret

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{4C78DFE8-7A09-11D4-81A0-00C04F60ECCC}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{4C78DFE8-7A09-11D4-81A0-00C04F60ECCC}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Lines(DispatchBaseClass):
	'A collection of lines'
	CLSID = IID('{95CD20D7-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type TextRange
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class MeshItem(DispatchBaseClass):
	'Mesh artwork item'
	CLSID = IID('{95CD20C4-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def ApplyEffect(self, LiveEffectXML=defaultNamedNotOptArg):
		'Apply effect to selected artItem'
		return self._oleobj_.InvokeTypes(1799447892, LCID, 1, (24, 0), ((8, 1),),LiveEffectXML
			)

	def BringInPerspective(self, PositionX=defaultNamedNotOptArg, PositionY=defaultNamedNotOptArg, PerspectiveGridPlane=defaultNamedNotOptArg):
		'Place art object(s)in perspective grid at spedified perspective plane and coordinate'
		return self._oleobj_.InvokeTypes(1685013072, LCID, 1, (24, 0), ((5, 1), (5, 1), (3, 1)),PositionX
			, PositionY, PerspectiveGridPlane)

	def Copy(self):
		'Copy selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668247673, LCID, 1, (24, 0), (),)

	def Cut(self):
		'Cut selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668641824, LCID, 1, (24, 0), (),)

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def Duplicate(self, RelativeObject=defaultNamedOptArg, InsertionLocation=defaultNamedOptArg):
		'create a duplicate of the object'
		ret = self._oleobj_.InvokeTypes(1668050798, LCID, 1, (9, 0), ((12, 17), (12, 17)),RelativeObject
			, InsertionLocation)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', None)
		return ret

	def Move(self, RelativeObject=defaultNamedNotOptArg, InsertionLocation=defaultNamedNotOptArg):
		'move the object'
		return self._oleobj_.InvokeTypes(1836021349, LCID, 1, (24, 0), ((9, 1), (3, 1)),RelativeObject
			, InsertionLocation)

	def MoveAfter(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in behind object'
		return self._oleobj_.InvokeTypes(1299596641, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveBefore(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in front of object'
		return self._oleobj_.InvokeTypes(1299596642, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveToBeginning(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to beginning of container'
		return self._oleobj_.InvokeTypes(1299596646, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def MoveToEnd(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to end of container'
		return self._oleobj_.InvokeTypes(1299596645, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def Resize(self, ScaleX=defaultNamedNotOptArg, ScaleY=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg
			, ChangeFillGradients=defaultNamedOptArg, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, ScaleAbout=defaultNamedOptArg):
		'Scale art object(s)'
		return self._oleobj_.InvokeTypes(1685017421, LCID, 1, (24, 0), ((5, 1), (5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),ScaleX
			, ScaleY, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern
			, ChangeLineWidths, ScaleAbout)

	def Rotate(self, Angle=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, RotateAbout=defaultNamedOptArg):
		'Rotate art object(s)'
		return self._oleobj_.InvokeTypes(1685017165, LCID, 1, (24, 0), ((5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),Angle
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, RotateAbout
			)

	def SendScriptMessage(self, PluginName=defaultNamedNotOptArg, MessageSelector=defaultNamedNotOptArg, InputString=defaultNamedNotOptArg):
		'sends the script message to the required plugin'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1632850765, LCID, 1, (8, 0), ((8, 1), (8, 1), (8, 1)),PluginName
			, MessageSelector, InputString)

	def Transform(self, TransformationMatrix=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, TransformAbout=defaultNamedOptArg):
		'Transform art object(s) using a transformation matrix'
		return self._oleobj_.InvokeTypes(1414676814, LCID, 1, (24, 0), ((9, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),TransformationMatrix
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, ChangeLineWidths
			, TransformAbout)

	def Translate(self, DeltaX=defaultNamedOptArg, DeltaY=defaultNamedOptArg, TransformObjects=defaultNamedOptArg, TransformFillPatterns=defaultNamedOptArg
			, TransformFillGradients=defaultNamedOptArg, TransformStrokePattern=defaultNamedOptArg):
		'Reposition art object(s)'
		return self._oleobj_.InvokeTypes(1685018701, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),DeltaX
			, DeltaY, TransformObjects, TransformFillPatterns, TransformFillGradients, TransformStrokePattern
			)

	def ZOrder(self, ZOrderCmd=defaultNamedNotOptArg):
		'Arranges the art relative to other art in the group or layer'
		return self._oleobj_.InvokeTypes(1515147844, LCID, 1, (24, 0), ((3, 1),),ZOrderCmd
			)

	_prop_map_get_ = {
		"AbsoluteZOrderPosition": (1883331151, 2, (3, 0), (), "AbsoluteZOrderPosition", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtworkKnockout": (1883991659, 2, (3, 0), (), "ArtworkKnockout", None),
		"BlendingMode": (1883401293, 2, (3, 0), (), "BlendingMode", None),
		# Method 'CompoundPathItem' returns object of type 'CompoundPathItem'
		"CompoundPathItem": (1148203057, 2, (9, 0), (), "CompoundPathItem", '{95CD20BE-AD72-11D3-B086-0010A4F5C335}'),
		"ControlBounds": (1634291288, 2, (12, 0), (), "ControlBounds", None),
		"Editable": (1883325796, 2, (11, 0), (), "Editable", None),
		"GeometricBounds": (1634288199, 2, (12, 0), (), "GeometricBounds", None),
		# Method 'GraphItem' returns object of type 'GraphItem'
		"GraphItem": (1148203058, 2, (9, 0), (), "GraphItem", '{4C78DFB7-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'GroupItem' returns object of type 'GroupItem'
		"GroupItem": (1148203059, 2, (9, 0), (), "GroupItem", '{95CD20C6-AD72-11D3-B086-0010A4F5C335}'),
		"Height": (1884506216, 2, (5, 0), (), "Height", None),
		"Hidden": (1634289732, 2, (11, 0), (), "Hidden", None),
		"IsIsolated": (1883861871, 2, (11, 0), (), "IsIsolated", None),
		# Method 'Layer' returns object of type 'Layer'
		"Layer": (1667320921, 2, (9, 0), (), "Layer", '{95CD20AC-AD72-11D3-B086-0010A4F5C335}'),
		"Left": (1279608404, 2, (5, 0), (), "Left", None),
		"Locked": (1634290763, 2, (11, 0), (), "Locked", None),
		# Method 'MeshItem' returns object of type 'MeshItem'
		"MeshItem": (1148203060, 2, (9, 0), (), "MeshItem", '{95CD20C4-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Note": (1634291284, 2, (8, 0), (), "Note", None),
		"Opacity": (1884049264, 2, (5, 0), (), "Opacity", None),
		"PageItem": (1396927603, 2, (9, 0), (), "PageItem", None),
		"PageItemType": (1954115685, 2, (3, 0), (), "PageItemType", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		# Method 'PathItem' returns object of type 'PathItem'
		"PathItem": (1148203061, 2, (9, 0), (), "PathItem", '{95CD20C0-AD72-11D3-B086-0010A4F5C335}'),
		"PixelAligned": (1884307820, 2, (11, 0), (), "PixelAligned", None),
		# Method 'PlacedItem' returns object of type 'PlacedItem'
		"PlacedItem": (1148203062, 2, (9, 0), (), "PlacedItem", '{95CD20C3-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PluginItem' returns object of type 'PluginItem'
		"PluginItem": (1148203063, 2, (9, 0), (), "PluginItem", '{95CD20C5-AD72-11D3-B086-0010A4F5C335}'),
		"Position": (1885425779, 2, (12, 0), (), "Position", None),
		# Method 'RasterItem' returns object of type 'RasterItem'
		"RasterItem": (1148203064, 2, (9, 0), (), "RasterItem", '{95CD20C2-AD72-11D3-B086-0010A4F5C335}'),
		"Selected": (1936026723, 2, (11, 0), (), "Selected", None),
		"Sliced": (1883329388, 2, (11, 0), (), "Sliced", None),
		# Method 'SymbolItem' returns object of type 'SymbolItem'
		"SymbolItem": (1148203065, 2, (9, 0), (), "SymbolItem", '{4C78DFC3-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'Tags' returns object of type 'Tags'
		"Tags": (1667322951, 2, (9, 0), (), "Tags", '{95CD20EB-AD72-11D3-B086-0010A4F5C335}'),
		"Top": (1414484000, 2, (5, 0), (), "Top", None),
		"URL": (1884639820, 2, (8, 0), (), "URL", None),
		"VisibilityVariable": (1884703062, 2, (12, 0), (), "VisibilityVariable", None),
		"VisibleBounds": (1634293314, 2, (12, 0), (), "VisibleBounds", None),
		"Width": (1884506231, 2, (5, 0), (), "Width", None),
		"WrapInside": (1884583753, 2, (11, 0), (), "WrapInside", None),
		"WrapOffset": (1884583759, 2, (5, 0), (), "WrapOffset", None),
		"Wrapped": (1886672722, 2, (11, 0), (), "Wrapped", None),
		"ZOrderPosition": (1884966736, 2, (3, 0), (), "ZOrderPosition", None),
	}
	_prop_map_put_ = {
		"ArtworkKnockout": ((1883991659, LCID, 4, 0),()),
		"BlendingMode": ((1883401293, LCID, 4, 0),()),
		"Height": ((1884506216, LCID, 4, 0),()),
		"Hidden": ((1634289732, LCID, 4, 0),()),
		"IsIsolated": ((1883861871, LCID, 4, 0),()),
		"Left": ((1279608404, LCID, 4, 0),()),
		"Locked": ((1634290763, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"Note": ((1634291284, LCID, 4, 0),()),
		"Opacity": ((1884049264, LCID, 4, 0),()),
		"PixelAligned": ((1884307820, LCID, 4, 0),()),
		"Position": ((1885425779, LCID, 4, 0),()),
		"Selected": ((1936026723, LCID, 4, 0),()),
		"Sliced": ((1883329388, LCID, 4, 0),()),
		"Top": ((1414484000, LCID, 4, 0),()),
		"URL": ((1884639820, LCID, 4, 0),()),
		"VisibilityVariable": ((1884703062, LCID, 4, 0),()),
		"Width": ((1884506231, LCID, 4, 0),()),
		"WrapInside": ((1884583753, LCID, 4, 0),()),
		"WrapOffset": ((1884583759, LCID, 4, 0),()),
		"Wrapped": ((1886672722, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class MeshItems(DispatchBaseClass):
	CLSID = IID('{95CD20EE-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type MeshItem
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20C4-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20C4-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20C4-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class NonNativeItem(DispatchBaseClass):
	'Non-native artwork item'
	CLSID = IID('{FC0A0BD3-5FFB-4301-A44F-F5B3ED181224}')
	coclass_clsid = None

	def ApplyEffect(self, LiveEffectXML=defaultNamedNotOptArg):
		'Apply effect to selected artItem'
		return self._oleobj_.InvokeTypes(1799447892, LCID, 1, (24, 0), ((8, 1),),LiveEffectXML
			)

	def BringInPerspective(self, PositionX=defaultNamedNotOptArg, PositionY=defaultNamedNotOptArg, PerspectiveGridPlane=defaultNamedNotOptArg):
		'Place art object(s)in perspective grid at spedified perspective plane and coordinate'
		return self._oleobj_.InvokeTypes(1685013072, LCID, 1, (24, 0), ((5, 1), (5, 1), (3, 1)),PositionX
			, PositionY, PerspectiveGridPlane)

	def Copy(self):
		'Copy selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668247673, LCID, 1, (24, 0), (),)

	def Cut(self):
		'Cut selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668641824, LCID, 1, (24, 0), (),)

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def Duplicate(self, RelativeObject=defaultNamedOptArg, InsertionLocation=defaultNamedOptArg):
		'create a duplicate of the object'
		ret = self._oleobj_.InvokeTypes(1668050798, LCID, 1, (9, 0), ((12, 17), (12, 17)),RelativeObject
			, InsertionLocation)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', None)
		return ret

	def Move(self, RelativeObject=defaultNamedNotOptArg, InsertionLocation=defaultNamedNotOptArg):
		'move the object'
		return self._oleobj_.InvokeTypes(1836021349, LCID, 1, (24, 0), ((9, 1), (3, 1)),RelativeObject
			, InsertionLocation)

	def MoveAfter(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in behind object'
		return self._oleobj_.InvokeTypes(1299596641, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveBefore(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in front of object'
		return self._oleobj_.InvokeTypes(1299596642, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveToBeginning(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to beginning of container'
		return self._oleobj_.InvokeTypes(1299596646, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def MoveToEnd(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to end of container'
		return self._oleobj_.InvokeTypes(1299596645, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def Resize(self, ScaleX=defaultNamedNotOptArg, ScaleY=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg
			, ChangeFillGradients=defaultNamedOptArg, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, ScaleAbout=defaultNamedOptArg):
		'Scale art object(s)'
		return self._oleobj_.InvokeTypes(1685017421, LCID, 1, (24, 0), ((5, 1), (5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),ScaleX
			, ScaleY, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern
			, ChangeLineWidths, ScaleAbout)

	def Rotate(self, Angle=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, RotateAbout=defaultNamedOptArg):
		'Rotate art object(s)'
		return self._oleobj_.InvokeTypes(1685017165, LCID, 1, (24, 0), ((5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),Angle
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, RotateAbout
			)

	def SendScriptMessage(self, PluginName=defaultNamedNotOptArg, MessageSelector=defaultNamedNotOptArg, InputString=defaultNamedNotOptArg):
		'sends the script message to the required plugin'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1632850765, LCID, 1, (8, 0), ((8, 1), (8, 1), (8, 1)),PluginName
			, MessageSelector, InputString)

	def Transform(self, TransformationMatrix=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, TransformAbout=defaultNamedOptArg):
		'Transform art object(s) using a transformation matrix'
		return self._oleobj_.InvokeTypes(1414676814, LCID, 1, (24, 0), ((9, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),TransformationMatrix
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, ChangeLineWidths
			, TransformAbout)

	def Translate(self, DeltaX=defaultNamedOptArg, DeltaY=defaultNamedOptArg, TransformObjects=defaultNamedOptArg, TransformFillPatterns=defaultNamedOptArg
			, TransformFillGradients=defaultNamedOptArg, TransformStrokePattern=defaultNamedOptArg):
		'Reposition art object(s)'
		return self._oleobj_.InvokeTypes(1685018701, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),DeltaX
			, DeltaY, TransformObjects, TransformFillPatterns, TransformFillGradients, TransformStrokePattern
			)

	def ZOrder(self, ZOrderCmd=defaultNamedNotOptArg):
		'Arranges the art relative to other art in the group or layer'
		return self._oleobj_.InvokeTypes(1515147844, LCID, 1, (24, 0), ((3, 1),),ZOrderCmd
			)

	_prop_map_get_ = {
		"AbsoluteZOrderPosition": (1883331151, 2, (3, 0), (), "AbsoluteZOrderPosition", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtworkKnockout": (1883991659, 2, (3, 0), (), "ArtworkKnockout", None),
		"BlendingMode": (1883401293, 2, (3, 0), (), "BlendingMode", None),
		# Method 'CompoundPathItem' returns object of type 'CompoundPathItem'
		"CompoundPathItem": (1148203057, 2, (9, 0), (), "CompoundPathItem", '{95CD20BE-AD72-11D3-B086-0010A4F5C335}'),
		"ControlBounds": (1634291288, 2, (12, 0), (), "ControlBounds", None),
		"Editable": (1883325796, 2, (11, 0), (), "Editable", None),
		"GeometricBounds": (1634288199, 2, (12, 0), (), "GeometricBounds", None),
		# Method 'GraphItem' returns object of type 'GraphItem'
		"GraphItem": (1148203058, 2, (9, 0), (), "GraphItem", '{4C78DFB7-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'GroupItem' returns object of type 'GroupItem'
		"GroupItem": (1148203059, 2, (9, 0), (), "GroupItem", '{95CD20C6-AD72-11D3-B086-0010A4F5C335}'),
		"Height": (1884506216, 2, (5, 0), (), "Height", None),
		"Hidden": (1634289732, 2, (11, 0), (), "Hidden", None),
		"IsIsolated": (1883861871, 2, (11, 0), (), "IsIsolated", None),
		# Method 'Layer' returns object of type 'Layer'
		"Layer": (1667320921, 2, (9, 0), (), "Layer", '{95CD20AC-AD72-11D3-B086-0010A4F5C335}'),
		"Left": (1279608404, 2, (5, 0), (), "Left", None),
		"Locked": (1634290763, 2, (11, 0), (), "Locked", None),
		# Method 'MeshItem' returns object of type 'MeshItem'
		"MeshItem": (1148203060, 2, (9, 0), (), "MeshItem", '{95CD20C4-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Note": (1634291284, 2, (8, 0), (), "Note", None),
		"Opacity": (1884049264, 2, (5, 0), (), "Opacity", None),
		"PageItem": (1396927603, 2, (9, 0), (), "PageItem", None),
		"PageItemType": (1954115685, 2, (3, 0), (), "PageItemType", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		# Method 'PathItem' returns object of type 'PathItem'
		"PathItem": (1148203061, 2, (9, 0), (), "PathItem", '{95CD20C0-AD72-11D3-B086-0010A4F5C335}'),
		"PixelAligned": (1884307820, 2, (11, 0), (), "PixelAligned", None),
		# Method 'PlacedItem' returns object of type 'PlacedItem'
		"PlacedItem": (1148203062, 2, (9, 0), (), "PlacedItem", '{95CD20C3-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PluginItem' returns object of type 'PluginItem'
		"PluginItem": (1148203063, 2, (9, 0), (), "PluginItem", '{95CD20C5-AD72-11D3-B086-0010A4F5C335}'),
		"Position": (1885425779, 2, (12, 0), (), "Position", None),
		# Method 'RasterItem' returns object of type 'RasterItem'
		"RasterItem": (1148203064, 2, (9, 0), (), "RasterItem", '{95CD20C2-AD72-11D3-B086-0010A4F5C335}'),
		"Selected": (1936026723, 2, (11, 0), (), "Selected", None),
		"Sliced": (1883329388, 2, (11, 0), (), "Sliced", None),
		# Method 'SymbolItem' returns object of type 'SymbolItem'
		"SymbolItem": (1148203065, 2, (9, 0), (), "SymbolItem", '{4C78DFC3-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'Tags' returns object of type 'Tags'
		"Tags": (1667322951, 2, (9, 0), (), "Tags", '{95CD20EB-AD72-11D3-B086-0010A4F5C335}'),
		"Top": (1414484000, 2, (5, 0), (), "Top", None),
		"URL": (1884639820, 2, (8, 0), (), "URL", None),
		"VisibilityVariable": (1884703062, 2, (12, 0), (), "VisibilityVariable", None),
		"VisibleBounds": (1634293314, 2, (12, 0), (), "VisibleBounds", None),
		"Width": (1884506231, 2, (5, 0), (), "Width", None),
		"WrapInside": (1884583753, 2, (11, 0), (), "WrapInside", None),
		"WrapOffset": (1884583759, 2, (5, 0), (), "WrapOffset", None),
		"Wrapped": (1886672722, 2, (11, 0), (), "Wrapped", None),
		"ZOrderPosition": (1884966736, 2, (3, 0), (), "ZOrderPosition", None),
	}
	_prop_map_put_ = {
		"ArtworkKnockout": ((1883991659, LCID, 4, 0),()),
		"BlendingMode": ((1883401293, LCID, 4, 0),()),
		"Height": ((1884506216, LCID, 4, 0),()),
		"Hidden": ((1634289732, LCID, 4, 0),()),
		"IsIsolated": ((1883861871, LCID, 4, 0),()),
		"Left": ((1279608404, LCID, 4, 0),()),
		"Locked": ((1634290763, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"Note": ((1634291284, LCID, 4, 0),()),
		"Opacity": ((1884049264, LCID, 4, 0),()),
		"PixelAligned": ((1884307820, LCID, 4, 0),()),
		"Position": ((1885425779, LCID, 4, 0),()),
		"Selected": ((1936026723, LCID, 4, 0),()),
		"Sliced": ((1883329388, LCID, 4, 0),()),
		"Top": ((1414484000, LCID, 4, 0),()),
		"URL": ((1884639820, LCID, 4, 0),()),
		"VisibilityVariable": ((1884703062, LCID, 4, 0),()),
		"Width": ((1884506231, LCID, 4, 0),()),
		"WrapInside": ((1884583753, LCID, 4, 0),()),
		"WrapOffset": ((1884583759, LCID, 4, 0),()),
		"Wrapped": ((1886672722, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class NonNativeItems(DispatchBaseClass):
	CLSID = IID('{9157F2B0-D436-4AC6-9769-94DC89E6EC92}')
	coclass_clsid = None

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type NonNativeItem
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{FC0A0BD3-5FFB-4301-A44F-F5B3ED181224}')
		return ret

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{FC0A0BD3-5FFB-4301-A44F-F5B3ED181224}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{FC0A0BD3-5FFB-4301-A44F-F5B3ED181224}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class PDFFileOptions(DispatchBaseClass):
	'Options which may be supplied when opening a PDF file'
	CLSID = IID('{4C78DFBD-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"PDFCropToBox": (1884312625, 2, (3, 0), (), "PDFCropToBox", None),
		"PageToOpen": (1884312655, 2, (3, 0), (), "PageToOpen", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"PDFCropToBox": ((1884312625, LCID, 4, 0),()),
		"PageToOpen": ((1884312655, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class PageItems(DispatchBaseClass):
	'A collection of page items'
	CLSID = IID('{95CD20E0-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', None)
		return ret

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', None)
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ParagraphAttributes(DispatchBaseClass):
	'properties of a paragraph'
	CLSID = IID('{4C78DFCE-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"AutoLeadingAmount": (1666204001, 2, (5, 0), (), "AutoLeadingAmount", None),
		"BunriKinshi": (1699760696, 2, (11, 0), (), "BunriKinshi", None),
		"BurasagariType": (1699760697, 2, (3, 0), (), "BurasagariType", None),
		"DesiredGlyphScaling": (1666203961, 2, (5, 0), (), "DesiredGlyphScaling", None),
		"DesiredLetterSpacing": (1884565862, 2, (5, 0), (), "DesiredLetterSpacing", None),
		"DesiredWordSpacing": (1884565859, 2, (5, 0), (), "DesiredWordSpacing", None),
		"EveryLineComposer": (1699760740, 2, (11, 0), (), "EveryLineComposer", None),
		"FirstLineIndent": (1884565811, 2, (5, 0), (), "FirstLineIndent", None),
		"HyphenateCapitalizedWords": (1666203955, 2, (11, 0), (), "HyphenateCapitalizedWords", None),
		"Hyphenation": (1215836209, 2, (11, 0), (), "Hyphenation", None),
		"HyphenationPreference": (1666203956, 2, (5, 0), (), "HyphenationPreference", None),
		"HyphenationZone": (1666203954, 2, (5, 0), (), "HyphenationZone", None),
		"Justification": (1884565814, 2, (3, 0), (), "Justification", None),
		"Kinsoku": (1665880911, 2, (8, 0), (), "Kinsoku", None),
		"KinsokuOrder": (1699760737, 2, (3, 0), (), "KinsokuOrder", None),
		"KurikaeshiMojiShori": (1699760738, 2, (11, 0), (), "KurikaeshiMojiShori", None),
		"LeadingType": (1666203960, 2, (3, 0), (), "LeadingType", None),
		"LeftIndent": (1884565812, 2, (5, 0), (), "LeftIndent", None),
		"MaximumConsecutiveHyphens": (1215836213, 2, (3, 0), (), "MaximumConsecutiveHyphens", None),
		"MaximumGlyphScaling": (1666203957, 2, (5, 0), (), "MaximumGlyphScaling", None),
		"MaximumLetterSpacing": (1884565861, 2, (5, 0), (), "MaximumLetterSpacing", None),
		"MaximumWordSpacing": (1884565858, 2, (5, 0), (), "MaximumWordSpacing", None),
		"MinimumAfterHyphen": (1215836212, 2, (3, 0), (), "MinimumAfterHyphen", None),
		"MinimumBeforeHyphen": (1215836211, 2, (3, 0), (), "MinimumBeforeHyphen", None),
		"MinimumGlyphScaling": (1666203958, 2, (5, 0), (), "MinimumGlyphScaling", None),
		"MinimumHyphenatedWordSize": (1666203953, 2, (3, 0), (), "MinimumHyphenatedWordSize", None),
		"MinimumLetterSpacing": (1884565860, 2, (5, 0), (), "MinimumLetterSpacing", None),
		"MinimumWordSpacing": (1884565857, 2, (5, 0), (), "MinimumWordSpacing", None),
		"Mojikumi": (1666009673, 2, (8, 0), (), "Mojikumi", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"RightIndent": (1884565813, 2, (5, 0), (), "RightIndent", None),
		"RomanHanging": (1699760694, 2, (11, 0), (), "RomanHanging", None),
		"SingleWordJustification": (1666203959, 2, (3, 0), (), "SingleWordJustification", None),
		"SpaceAfter": (1666203952, 2, (5, 0), (), "SpaceAfter", None),
		"SpaceBefore": (1884565808, 2, (5, 0), (), "SpaceBefore", None),
		"TabStops": (1884566067, 2, (12, 0), (), "TabStops", None),
	}
	_prop_map_put_ = {
		"AutoLeadingAmount": ((1666204001, LCID, 4, 0),()),
		"BunriKinshi": ((1699760696, LCID, 4, 0),()),
		"BurasagariType": ((1699760697, LCID, 4, 0),()),
		"DesiredGlyphScaling": ((1666203961, LCID, 4, 0),()),
		"DesiredLetterSpacing": ((1884565862, LCID, 4, 0),()),
		"DesiredWordSpacing": ((1884565859, LCID, 4, 0),()),
		"EveryLineComposer": ((1699760740, LCID, 4, 0),()),
		"FirstLineIndent": ((1884565811, LCID, 4, 0),()),
		"HyphenateCapitalizedWords": ((1666203955, LCID, 4, 0),()),
		"Hyphenation": ((1215836209, LCID, 4, 0),()),
		"HyphenationPreference": ((1666203956, LCID, 4, 0),()),
		"HyphenationZone": ((1666203954, LCID, 4, 0),()),
		"Justification": ((1884565814, LCID, 4, 0),()),
		"Kinsoku": ((1665880911, LCID, 4, 0),()),
		"KinsokuOrder": ((1699760737, LCID, 4, 0),()),
		"KurikaeshiMojiShori": ((1699760738, LCID, 4, 0),()),
		"LeadingType": ((1666203960, LCID, 4, 0),()),
		"LeftIndent": ((1884565812, LCID, 4, 0),()),
		"MaximumConsecutiveHyphens": ((1215836213, LCID, 4, 0),()),
		"MaximumGlyphScaling": ((1666203957, LCID, 4, 0),()),
		"MaximumLetterSpacing": ((1884565861, LCID, 4, 0),()),
		"MaximumWordSpacing": ((1884565858, LCID, 4, 0),()),
		"MinimumAfterHyphen": ((1215836212, LCID, 4, 0),()),
		"MinimumBeforeHyphen": ((1215836211, LCID, 4, 0),()),
		"MinimumGlyphScaling": ((1666203958, LCID, 4, 0),()),
		"MinimumHyphenatedWordSize": ((1666203953, LCID, 4, 0),()),
		"MinimumLetterSpacing": ((1884565860, LCID, 4, 0),()),
		"MinimumWordSpacing": ((1884565857, LCID, 4, 0),()),
		"Mojikumi": ((1666009673, LCID, 4, 0),()),
		"RightIndent": ((1884565813, LCID, 4, 0),()),
		"RomanHanging": ((1699760694, LCID, 4, 0),()),
		"SingleWordJustification": ((1666203959, LCID, 4, 0),()),
		"SpaceAfter": ((1666203952, LCID, 4, 0),()),
		"SpaceBefore": ((1884565808, LCID, 4, 0),()),
		"TabStops": ((1884566067, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ParagraphStyle(DispatchBaseClass):
	'a named style that remembers paragraph attributes'
	CLSID = IID('{2D2A6B70-EA28-49AA-B7C0-3EEC671CBACC}')
	coclass_clsid = None

	def ApplyTo(self, TextItem=defaultNamedNotOptArg, ClearingOverrides=defaultNamedOptArg):
		'Apply the paragraph style to text object(s)'
		return self._oleobj_.InvokeTypes(1097879635, LCID, 1, (24, 0), ((12, 1), (12, 17)),TextItem
			, ClearingOverrides)

	def Clear(self):
		'Remove all the attributes from this paragraph style'
		return self._oleobj_.InvokeTypes(1094930515, LCID, 1, (24, 0), (),)

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'CharacterAttributes' returns object of type 'CharacterAttributes'
		"CharacterAttributes": (1130905972, 2, (9, 0), (), "CharacterAttributes", '{4C78DFCD-7A09-11D4-81A0-00C04F60ECCC}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		# Method 'ParagraphAttributes' returns object of type 'ParagraphAttributes'
		"ParagraphAttributes": (1348944244, 2, (9, 0), (), "ParagraphAttributes", '{4C78DFCE-7A09-11D4-81A0-00C04F60ECCC}'),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"Name": ((1886282093, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ParagraphStyles(DispatchBaseClass):
	'A collection of paragraph styles'
	CLSID = IID('{0E3BF58B-A0F2-4776-9CD0-279FCB26009E}')
	coclass_clsid = None

	# Result is of type ParagraphStyle
	def Add(self, Name=defaultNamedNotOptArg):
		'create a named paragraph style'
		ret = self._oleobj_.InvokeTypes(1666208596, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{2D2A6B70-EA28-49AA-B7C0-3EEC671CBACC}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type ParagraphStyle
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{2D2A6B70-EA28-49AA-B7C0-3EEC671CBACC}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete a paragraph style from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{2D2A6B70-EA28-49AA-B7C0-3EEC671CBACC}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{2D2A6B70-EA28-49AA-B7C0-3EEC671CBACC}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Paragraphs(DispatchBaseClass):
	'A collection of Paragraphs'
	CLSID = IID('{95CD20D8-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	# Result is of type TextRange
	def Add(self, Contents=defaultNamedNotOptArg, RelativeObject=defaultNamedOptArg, InsertionLocation=defaultNamedOptArg):
		'create a text art item'
		ret = self._oleobj_.InvokeTypes(1668309362, LCID, 1, (9, 0), ((8, 1), (12, 17), (12, 17)),Contents
			, RelativeObject, InsertionLocation)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	# Result is of type TextRange
	def AddBefore(self, Contents=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1131561574, LCID, 1, (9, 0), ((8, 1),),Contents
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddBefore', '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type TextRange
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class PathItem(DispatchBaseClass):
	'An artwork path item'
	CLSID = IID('{95CD20C0-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def ApplyEffect(self, LiveEffectXML=defaultNamedNotOptArg):
		'Apply effect to selected artItem'
		return self._oleobj_.InvokeTypes(1799447892, LCID, 1, (24, 0), ((8, 1),),LiveEffectXML
			)

	def BringInPerspective(self, PositionX=defaultNamedNotOptArg, PositionY=defaultNamedNotOptArg, PerspectiveGridPlane=defaultNamedNotOptArg):
		'Place art object(s)in perspective grid at spedified perspective plane and coordinate'
		return self._oleobj_.InvokeTypes(1685013072, LCID, 1, (24, 0), ((5, 1), (5, 1), (3, 1)),PositionX
			, PositionY, PerspectiveGridPlane)

	def Copy(self):
		'Copy selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668247673, LCID, 1, (24, 0), (),)

	def Cut(self):
		'Cut selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668641824, LCID, 1, (24, 0), (),)

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def Duplicate(self, RelativeObject=defaultNamedOptArg, InsertionLocation=defaultNamedOptArg):
		'create a duplicate of the object'
		ret = self._oleobj_.InvokeTypes(1668050798, LCID, 1, (9, 0), ((12, 17), (12, 17)),RelativeObject
			, InsertionLocation)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', None)
		return ret

	def Move(self, RelativeObject=defaultNamedNotOptArg, InsertionLocation=defaultNamedNotOptArg):
		'move the object'
		return self._oleobj_.InvokeTypes(1836021349, LCID, 1, (24, 0), ((9, 1), (3, 1)),RelativeObject
			, InsertionLocation)

	def MoveAfter(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in behind object'
		return self._oleobj_.InvokeTypes(1299596641, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveBefore(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in front of object'
		return self._oleobj_.InvokeTypes(1299596642, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveToBeginning(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to beginning of container'
		return self._oleobj_.InvokeTypes(1299596646, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def MoveToEnd(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to end of container'
		return self._oleobj_.InvokeTypes(1299596645, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def Resize(self, ScaleX=defaultNamedNotOptArg, ScaleY=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg
			, ChangeFillGradients=defaultNamedOptArg, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, ScaleAbout=defaultNamedOptArg):
		'Scale art object(s)'
		return self._oleobj_.InvokeTypes(1685017421, LCID, 1, (24, 0), ((5, 1), (5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),ScaleX
			, ScaleY, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern
			, ChangeLineWidths, ScaleAbout)

	def Rotate(self, Angle=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, RotateAbout=defaultNamedOptArg):
		'Rotate art object(s)'
		return self._oleobj_.InvokeTypes(1685017165, LCID, 1, (24, 0), ((5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),Angle
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, RotateAbout
			)

	def SendScriptMessage(self, PluginName=defaultNamedNotOptArg, MessageSelector=defaultNamedNotOptArg, InputString=defaultNamedNotOptArg):
		'sends the script message to the required plugin'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1632850765, LCID, 1, (8, 0), ((8, 1), (8, 1), (8, 1)),PluginName
			, MessageSelector, InputString)

	def SetEntirePath(self, PathPoints=defaultNamedNotOptArg):
		'Set the path using the provided array of path point (x, y) coordinate pairs'
		return self._oleobj_.InvokeTypes(1397051508, LCID, 1, (24, 0), ((12, 1),),PathPoints
			)

	def SetFillColor(self, arg0=defaultUnnamedArg):
		'fill color'
		return self._oleobj_.InvokeTypes(1634289219, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetStrokeColor(self, arg0=defaultUnnamedArg):
		'stroke color'
		return self._oleobj_.InvokeTypes(1634292547, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def Transform(self, TransformationMatrix=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, TransformAbout=defaultNamedOptArg):
		'Transform art object(s) using a transformation matrix'
		return self._oleobj_.InvokeTypes(1414676814, LCID, 1, (24, 0), ((9, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),TransformationMatrix
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, ChangeLineWidths
			, TransformAbout)

	def Translate(self, DeltaX=defaultNamedOptArg, DeltaY=defaultNamedOptArg, TransformObjects=defaultNamedOptArg, TransformFillPatterns=defaultNamedOptArg
			, TransformFillGradients=defaultNamedOptArg, TransformStrokePattern=defaultNamedOptArg):
		'Reposition art object(s)'
		return self._oleobj_.InvokeTypes(1685018701, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),DeltaX
			, DeltaY, TransformObjects, TransformFillPatterns, TransformFillGradients, TransformStrokePattern
			)

	def ZOrder(self, ZOrderCmd=defaultNamedNotOptArg):
		'Arranges the art relative to other art in the group or layer'
		return self._oleobj_.InvokeTypes(1515147844, LCID, 1, (24, 0), ((3, 1),),ZOrderCmd
			)

	_prop_map_get_ = {
		"AbsoluteZOrderPosition": (1883331151, 2, (3, 0), (), "AbsoluteZOrderPosition", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Area": (1634287954, 2, (5, 0), (), "Area", None),
		"ArtworkKnockout": (1883991659, 2, (3, 0), (), "ArtworkKnockout", None),
		"BlendingMode": (1883401293, 2, (3, 0), (), "BlendingMode", None),
		"Clipping": (1634288464, 2, (11, 0), (), "Clipping", None),
		"Closed": (1634288492, 2, (11, 0), (), "Closed", None),
		# Method 'CompoundPathItem' returns object of type 'CompoundPathItem'
		"CompoundPathItem": (1148203057, 2, (9, 0), (), "CompoundPathItem", '{95CD20BE-AD72-11D3-B086-0010A4F5C335}'),
		"ControlBounds": (1634291288, 2, (12, 0), (), "ControlBounds", None),
		"Editable": (1883325796, 2, (11, 0), (), "Editable", None),
		"Evenodd": (1634288975, 2, (11, 0), (), "Evenodd", None),
		"FillColor": (1634289219, 2, (9, 0), (), "FillColor", None),
		"FillOverprint": (1634289231, 2, (11, 0), (), "FillOverprint", None),
		"Filled": (1634289232, 2, (11, 0), (), "Filled", None),
		"GeometricBounds": (1634288199, 2, (12, 0), (), "GeometricBounds", None),
		# Method 'GraphItem' returns object of type 'GraphItem'
		"GraphItem": (1148203058, 2, (9, 0), (), "GraphItem", '{4C78DFB7-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'GroupItem' returns object of type 'GroupItem'
		"GroupItem": (1148203059, 2, (9, 0), (), "GroupItem", '{95CD20C6-AD72-11D3-B086-0010A4F5C335}'),
		"Guides": (1634289476, 2, (11, 0), (), "Guides", None),
		"Height": (1884506216, 2, (5, 0), (), "Height", None),
		"Hidden": (1634289732, 2, (11, 0), (), "Hidden", None),
		"IsIsolated": (1883861871, 2, (11, 0), (), "IsIsolated", None),
		# Method 'Layer' returns object of type 'Layer'
		"Layer": (1667320921, 2, (9, 0), (), "Layer", '{95CD20AC-AD72-11D3-B086-0010A4F5C335}'),
		"Left": (1279608404, 2, (5, 0), (), "Left", None),
		"Length": (1818586727, 2, (5, 0), (), "Length", None),
		"Locked": (1634290763, 2, (11, 0), (), "Locked", None),
		# Method 'MeshItem' returns object of type 'MeshItem'
		"MeshItem": (1148203060, 2, (9, 0), (), "MeshItem", '{95CD20C4-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Note": (1634291284, 2, (8, 0), (), "Note", None),
		"Opacity": (1884049264, 2, (5, 0), (), "Opacity", None),
		"PageItem": (1396927603, 2, (9, 0), (), "PageItem", None),
		"PageItemType": (1954115685, 2, (3, 0), (), "PageItemType", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		# Method 'PathItem' returns object of type 'PathItem'
		"PathItem": (1148203061, 2, (9, 0), (), "PathItem", '{95CD20C0-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PathPoints' returns object of type 'PathPoints'
		"PathPoints": (1667321939, 2, (9, 0), (), "PathPoints", '{95CD20E2-AD72-11D3-B086-0010A4F5C335}'),
		"PixelAligned": (1884307820, 2, (11, 0), (), "PixelAligned", None),
		# Method 'PlacedItem' returns object of type 'PlacedItem'
		"PlacedItem": (1148203062, 2, (9, 0), (), "PlacedItem", '{95CD20C3-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PluginItem' returns object of type 'PluginItem'
		"PluginItem": (1148203063, 2, (9, 0), (), "PluginItem", '{95CD20C5-AD72-11D3-B086-0010A4F5C335}'),
		"Polarity": (1634291792, 2, (3, 0), (), "Polarity", None),
		"Position": (1885425779, 2, (12, 0), (), "Position", None),
		# Method 'RasterItem' returns object of type 'RasterItem'
		"RasterItem": (1148203064, 2, (9, 0), (), "RasterItem", '{95CD20C2-AD72-11D3-B086-0010A4F5C335}'),
		"Resolution": (1634292314, 2, (5, 0), (), "Resolution", None),
		"Selected": (1936026723, 2, (11, 0), (), "Selected", None),
		"SelectedPathPoints": (1634292600, 2, (12, 0), (), "SelectedPathPoints", None),
		"Sliced": (1883329388, 2, (11, 0), (), "Sliced", None),
		"StrokeCap": (1634288504, 2, (3, 0), (), "StrokeCap", None),
		"StrokeColor": (1634292547, 2, (9, 0), (), "StrokeColor", None),
		"StrokeDashOffset": (1634288719, 2, (5, 0), (), "StrokeDashOffset", None),
		"StrokeDashes": (1634288723, 2, (12, 0), (), "StrokeDashes", None),
		"StrokeJoin": (1634290286, 2, (3, 0), (), "StrokeJoin", None),
		"StrokeMiterLimit": (1634291064, 2, (5, 0), (), "StrokeMiterLimit", None),
		"StrokeOverprint": (1634292559, 2, (11, 0), (), "StrokeOverprint", None),
		"StrokeWidth": (1634292567, 2, (5, 0), (), "StrokeWidth", None),
		"Stroked": (1634292560, 2, (11, 0), (), "Stroked", None),
		# Method 'SymbolItem' returns object of type 'SymbolItem'
		"SymbolItem": (1148203065, 2, (9, 0), (), "SymbolItem", '{4C78DFC3-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'Tags' returns object of type 'Tags'
		"Tags": (1667322951, 2, (9, 0), (), "Tags", '{95CD20EB-AD72-11D3-B086-0010A4F5C335}'),
		"Top": (1414484000, 2, (5, 0), (), "Top", None),
		"URL": (1884639820, 2, (8, 0), (), "URL", None),
		"VisibilityVariable": (1884703062, 2, (12, 0), (), "VisibilityVariable", None),
		"VisibleBounds": (1634293314, 2, (12, 0), (), "VisibleBounds", None),
		"Width": (1884506231, 2, (5, 0), (), "Width", None),
		"WrapInside": (1884583753, 2, (11, 0), (), "WrapInside", None),
		"WrapOffset": (1884583759, 2, (5, 0), (), "WrapOffset", None),
		"Wrapped": (1886672722, 2, (11, 0), (), "Wrapped", None),
		"ZOrderPosition": (1884966736, 2, (3, 0), (), "ZOrderPosition", None),
	}
	_prop_map_put_ = {
		"ArtworkKnockout": ((1883991659, LCID, 4, 0),()),
		"BlendingMode": ((1883401293, LCID, 4, 0),()),
		"Clipping": ((1634288464, LCID, 4, 0),()),
		"Closed": ((1634288492, LCID, 4, 0),()),
		"Evenodd": ((1634288975, LCID, 4, 0),()),
		"FillColor": ((1634289219, LCID, 4, 0),()),
		"FillOverprint": ((1634289231, LCID, 4, 0),()),
		"Filled": ((1634289232, LCID, 4, 0),()),
		"Guides": ((1634289476, LCID, 4, 0),()),
		"Height": ((1884506216, LCID, 4, 0),()),
		"Hidden": ((1634289732, LCID, 4, 0),()),
		"IsIsolated": ((1883861871, LCID, 4, 0),()),
		"Left": ((1279608404, LCID, 4, 0),()),
		"Locked": ((1634290763, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"Note": ((1634291284, LCID, 4, 0),()),
		"Opacity": ((1884049264, LCID, 4, 0),()),
		"PixelAligned": ((1884307820, LCID, 4, 0),()),
		"Polarity": ((1634291792, LCID, 4, 0),()),
		"Position": ((1885425779, LCID, 4, 0),()),
		"Resolution": ((1634292314, LCID, 4, 0),()),
		"Selected": ((1936026723, LCID, 4, 0),()),
		"Sliced": ((1883329388, LCID, 4, 0),()),
		"StrokeCap": ((1634288504, LCID, 4, 0),()),
		"StrokeColor": ((1634292547, LCID, 4, 0),()),
		"StrokeDashOffset": ((1634288719, LCID, 4, 0),()),
		"StrokeDashes": ((1634288723, LCID, 4, 0),()),
		"StrokeJoin": ((1634290286, LCID, 4, 0),()),
		"StrokeMiterLimit": ((1634291064, LCID, 4, 0),()),
		"StrokeOverprint": ((1634292559, LCID, 4, 0),()),
		"StrokeWidth": ((1634292567, LCID, 4, 0),()),
		"Stroked": ((1634292560, LCID, 4, 0),()),
		"Top": ((1414484000, LCID, 4, 0),()),
		"URL": ((1884639820, LCID, 4, 0),()),
		"VisibilityVariable": ((1884703062, LCID, 4, 0),()),
		"Width": ((1884506231, LCID, 4, 0),()),
		"WrapInside": ((1884583753, LCID, 4, 0),()),
		"WrapOffset": ((1884583759, LCID, 4, 0),()),
		"Wrapped": ((1886672722, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class PathItems(DispatchBaseClass):
	'A collection of path items'
	CLSID = IID('{95CD20E1-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	# Result is of type PathItem
	def Add(self):
		'create a path'
		ret = self._oleobj_.InvokeTypes(1667321955, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{95CD20C0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	# Result is of type PathItem
	def Ellipse(self, Top=defaultNamedOptArg, Left=defaultNamedOptArg, Width=defaultNamedOptArg, Height=defaultNamedOptArg
			, Reversed=defaultNamedOptArg, Inscribed=defaultNamedOptArg):
		'Create an elliptical path item.'
		ret = self._oleobj_.InvokeTypes(1935888214, LCID, 1, (9, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),Top
			, Left, Width, Height, Reversed, Inscribed
			)
		if ret is not None:
			ret = Dispatch(ret, 'Ellipse', '{95CD20C0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type PathItem
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20C0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	# Result is of type PathItem
	def Polygon(self, CenterX=defaultNamedOptArg, CenterY=defaultNamedOptArg, Radius=defaultNamedOptArg, Sides=defaultNamedOptArg
			, Reversed=defaultNamedOptArg):
		'Used to create a regular polygon path item. Not for path item access.'
		ret = self._oleobj_.InvokeTypes(1935888455, LCID, 1, (9, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),CenterX
			, CenterY, Radius, Sides, Reversed)
		if ret is not None:
			ret = Dispatch(ret, 'Polygon', '{95CD20C0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	# Result is of type PathItem
	def Rectangle(self, Top=defaultNamedNotOptArg, Left=defaultNamedNotOptArg, Width=defaultNamedNotOptArg, Height=defaultNamedNotOptArg
			, Reversed=defaultNamedOptArg):
		'Used to create a rectangular path item. Not for path item access.'
		ret = self._oleobj_.InvokeTypes(1935888963, LCID, 1, (9, 0), ((5, 1), (5, 1), (5, 1), (5, 1), (12, 17)),Top
			, Left, Width, Height, Reversed)
		if ret is not None:
			ret = Dispatch(ret, 'Rectangle', '{95CD20C0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	# Result is of type PathItem
	def RoundedRectangle(self, Top=defaultNamedNotOptArg, Left=defaultNamedNotOptArg, Width=defaultNamedNotOptArg, Height=defaultNamedNotOptArg
			, HorizontalRadius=defaultNamedOptArg, VerticalRadius=defaultNamedOptArg, Reversed=defaultNamedOptArg):
		'Used to create a rounded-corner rectangular path item. Not for path item access.'
		ret = self._oleobj_.InvokeTypes(1935888978, LCID, 1, (9, 0), ((5, 1), (5, 1), (5, 1), (5, 1), (12, 17), (12, 17), (12, 17)),Top
			, Left, Width, Height, HorizontalRadius, VerticalRadius
			, Reversed)
		if ret is not None:
			ret = Dispatch(ret, 'RoundedRectangle', '{95CD20C0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	# Result is of type PathItem
	def Star(self, CenterX=defaultNamedOptArg, CenterY=defaultNamedOptArg, Radius=defaultNamedOptArg, InnerRadius=defaultNamedOptArg
			, Points=defaultNamedOptArg, Reversed=defaultNamedOptArg):
		'Used to create a star-shaped path item. Not for path item access.'
		ret = self._oleobj_.InvokeTypes(1935889236, LCID, 1, (9, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),CenterX
			, CenterY, Radius, InnerRadius, Points, Reversed
			)
		if ret is not None:
			ret = Dispatch(ret, 'Star', '{95CD20C0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20C0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20C0-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class PathPoint(DispatchBaseClass):
	'A point on a path'
	CLSID = IID('{95CD20C1-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Anchor": (1883336291, 2, (12, 0), (), "Anchor", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"LeftDirection": (1667320142, 2, (12, 0), (), "LeftDirection", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"PointType": (1667318610, 2, (3, 0), (), "PointType", None),
		"RightDirection": (1667321684, 2, (12, 0), (), "RightDirection", None),
		"Selected": (1936026723, 2, (3, 0), (), "Selected", None),
	}
	_prop_map_put_ = {
		"Anchor": ((1883336291, LCID, 4, 0),()),
		"LeftDirection": ((1667320142, LCID, 4, 0),()),
		"PointType": ((1667318610, LCID, 4, 0),()),
		"RightDirection": ((1667321684, LCID, 4, 0),()),
		"Selected": ((1936026723, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class PathPoints(DispatchBaseClass):
	'A collection of path points'
	CLSID = IID('{95CD20E2-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	# Result is of type PathPoint
	def Add(self):
		'create a path point'
		ret = self._oleobj_.InvokeTypes(1667321939, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{95CD20C1-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type PathPoint
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20C1-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20C1-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20C1-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Pattern(DispatchBaseClass):
	'A pattern'
	CLSID = IID('{95CD20B9-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"Name": ((1886282093, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Patterns(DispatchBaseClass):
	'A collection of patterns'
	CLSID = IID('{95CD20E7-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	# Result is of type Pattern
	def Add(self):
		'create a pattern'
		ret = self._oleobj_.InvokeTypes(1667321940, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{95CD20B9-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type Pattern
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20B9-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20B9-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20B9-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class PhotoshopFileOptions(DispatchBaseClass):
	'Options which are applied when opening or placing a Photoshop file'
	CLSID = IID('{4C78DFBA-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"LayerComp": (1884046192, 2, (8, 0), (), "LayerComp", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"PixelAspectRatioCorrection": (1883329091, 2, (11, 0), (), "PixelAspectRatioCorrection", None),
		"PreserveHiddenLayers": (1884309580, 2, (11, 0), (), "PreserveHiddenLayers", None),
		"PreserveImageMaps": (1884309837, 2, (11, 0), (), "PreserveImageMaps", None),
		"PreserveLayers": (1884310649, 2, (11, 0), (), "PreserveLayers", None),
		"PreserveSlices": (1884312419, 2, (11, 0), (), "PreserveSlices", None),
	}
	_prop_map_put_ = {
		"LayerComp": ((1884046192, LCID, 4, 0),()),
		"PixelAspectRatioCorrection": ((1883329091, LCID, 4, 0),()),
		"PreserveHiddenLayers": ((1884309580, LCID, 4, 0),()),
		"PreserveImageMaps": ((1884309837, LCID, 4, 0),()),
		"PreserveLayers": ((1884310649, LCID, 4, 0),()),
		"PreserveSlices": ((1884312419, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class PlacedItem(DispatchBaseClass):
	'Placed artwork item'
	CLSID = IID('{95CD20C3-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def ApplyEffect(self, LiveEffectXML=defaultNamedNotOptArg):
		'Apply effect to selected artItem'
		return self._oleobj_.InvokeTypes(1799447892, LCID, 1, (24, 0), ((8, 1),),LiveEffectXML
			)

	def BringInPerspective(self, PositionX=defaultNamedNotOptArg, PositionY=defaultNamedNotOptArg, PerspectiveGridPlane=defaultNamedNotOptArg):
		'Place art object(s)in perspective grid at spedified perspective plane and coordinate'
		return self._oleobj_.InvokeTypes(1685013072, LCID, 1, (24, 0), ((5, 1), (5, 1), (3, 1)),PositionX
			, PositionY, PerspectiveGridPlane)

	def Copy(self):
		'Copy selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668247673, LCID, 1, (24, 0), (),)

	def Cut(self):
		'Cut selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668641824, LCID, 1, (24, 0), (),)

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def Duplicate(self, RelativeObject=defaultNamedOptArg, InsertionLocation=defaultNamedOptArg):
		'create a duplicate of the object'
		ret = self._oleobj_.InvokeTypes(1668050798, LCID, 1, (9, 0), ((12, 17), (12, 17)),RelativeObject
			, InsertionLocation)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', None)
		return ret

	def Embed(self):
		'Embed the placed art within the illustration'
		return self._oleobj_.InvokeTypes(1883598178, LCID, 1, (24, 0), (),)

	def Move(self, RelativeObject=defaultNamedNotOptArg, InsertionLocation=defaultNamedNotOptArg):
		'move the object'
		return self._oleobj_.InvokeTypes(1836021349, LCID, 1, (24, 0), ((9, 1), (3, 1)),RelativeObject
			, InsertionLocation)

	def MoveAfter(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in behind object'
		return self._oleobj_.InvokeTypes(1299596641, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveBefore(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in front of object'
		return self._oleobj_.InvokeTypes(1299596642, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveToBeginning(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to beginning of container'
		return self._oleobj_.InvokeTypes(1299596646, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def MoveToEnd(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to end of container'
		return self._oleobj_.InvokeTypes(1299596645, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def Relink(self, FileSpec=defaultNamedNotOptArg):
		'Relink the placed art with supplied art from file'
		return self._oleobj_.InvokeTypes(1885426252, LCID, 1, (24, 0), ((8, 1),),FileSpec
			)

	def Resize(self, ScaleX=defaultNamedNotOptArg, ScaleY=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg
			, ChangeFillGradients=defaultNamedOptArg, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, ScaleAbout=defaultNamedOptArg):
		'Scale art object(s)'
		return self._oleobj_.InvokeTypes(1685017421, LCID, 1, (24, 0), ((5, 1), (5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),ScaleX
			, ScaleY, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern
			, ChangeLineWidths, ScaleAbout)

	def Rotate(self, Angle=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, RotateAbout=defaultNamedOptArg):
		'Rotate art object(s)'
		return self._oleobj_.InvokeTypes(1685017165, LCID, 1, (24, 0), ((5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),Angle
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, RotateAbout
			)

	def SendScriptMessage(self, PluginName=defaultNamedNotOptArg, MessageSelector=defaultNamedNotOptArg, InputString=defaultNamedNotOptArg):
		'sends the script message to the required plugin'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1632850765, LCID, 1, (8, 0), ((8, 1), (8, 1), (8, 1)),PluginName
			, MessageSelector, InputString)

	def SetMatrix(self, arg0=defaultUnnamedArg):
		'The transformation matrix of the placed art object'
		return self._oleobj_.InvokeTypes(1950767181, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	# Result is of type PluginItem
	def Trace(self):
		'Trace this raster object using default options.  Reorders this placed to the source art.'
		ret = self._oleobj_.InvokeTypes(1885426802, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Trace', '{95CD20C5-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Transform(self, TransformationMatrix=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, TransformAbout=defaultNamedOptArg):
		'Transform art object(s) using a transformation matrix'
		return self._oleobj_.InvokeTypes(1414676814, LCID, 1, (24, 0), ((9, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),TransformationMatrix
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, ChangeLineWidths
			, TransformAbout)

	def Translate(self, DeltaX=defaultNamedOptArg, DeltaY=defaultNamedOptArg, TransformObjects=defaultNamedOptArg, TransformFillPatterns=defaultNamedOptArg
			, TransformFillGradients=defaultNamedOptArg, TransformStrokePattern=defaultNamedOptArg):
		'Reposition art object(s)'
		return self._oleobj_.InvokeTypes(1685018701, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),DeltaX
			, DeltaY, TransformObjects, TransformFillPatterns, TransformFillGradients, TransformStrokePattern
			)

	def ZOrder(self, ZOrderCmd=defaultNamedNotOptArg):
		'Arranges the art relative to other art in the group or layer'
		return self._oleobj_.InvokeTypes(1515147844, LCID, 1, (24, 0), ((3, 1),),ZOrderCmd
			)

	_prop_map_get_ = {
		"AbsoluteZOrderPosition": (1883331151, 2, (3, 0), (), "AbsoluteZOrderPosition", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtworkKnockout": (1883991659, 2, (3, 0), (), "ArtworkKnockout", None),
		"BlendingMode": (1883401293, 2, (3, 0), (), "BlendingMode", None),
		"BoundingBox": (1634288216, 2, (12, 0), (), "BoundingBox", None),
		# Method 'CompoundPathItem' returns object of type 'CompoundPathItem'
		"CompoundPathItem": (1148203057, 2, (9, 0), (), "CompoundPathItem", '{95CD20BE-AD72-11D3-B086-0010A4F5C335}'),
		"ContentVariable": (1883459414, 2, (12, 0), (), "ContentVariable", None),
		"ControlBounds": (1634291288, 2, (12, 0), (), "ControlBounds", None),
		"Editable": (1883325796, 2, (11, 0), (), "Editable", None),
		"File": (1634289235, 2, (8, 0), (), "File", None),
		"GeometricBounds": (1634288199, 2, (12, 0), (), "GeometricBounds", None),
		# Method 'GraphItem' returns object of type 'GraphItem'
		"GraphItem": (1148203058, 2, (9, 0), (), "GraphItem", '{4C78DFB7-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'GroupItem' returns object of type 'GroupItem'
		"GroupItem": (1148203059, 2, (9, 0), (), "GroupItem", '{95CD20C6-AD72-11D3-B086-0010A4F5C335}'),
		"Height": (1884506216, 2, (5, 0), (), "Height", None),
		"Hidden": (1634289732, 2, (11, 0), (), "Hidden", None),
		"IsIsolated": (1883861871, 2, (11, 0), (), "IsIsolated", None),
		# Method 'Layer' returns object of type 'Layer'
		"Layer": (1667320921, 2, (9, 0), (), "Layer", '{95CD20AC-AD72-11D3-B086-0010A4F5C335}'),
		"Left": (1279608404, 2, (5, 0), (), "Left", None),
		"Locked": (1634290763, 2, (11, 0), (), "Locked", None),
		# Method 'Matrix' returns object of type '_Matrix'
		"Matrix": (1950767181, 2, (9, 0), (), "Matrix", '{95CD20C9-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'MeshItem' returns object of type 'MeshItem'
		"MeshItem": (1148203060, 2, (9, 0), (), "MeshItem", '{95CD20C4-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Note": (1634291284, 2, (8, 0), (), "Note", None),
		"Opacity": (1884049264, 2, (5, 0), (), "Opacity", None),
		"PageItem": (1396927603, 2, (9, 0), (), "PageItem", None),
		"PageItemType": (1954115685, 2, (3, 0), (), "PageItemType", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		# Method 'PathItem' returns object of type 'PathItem'
		"PathItem": (1148203061, 2, (9, 0), (), "PathItem", '{95CD20C0-AD72-11D3-B086-0010A4F5C335}'),
		"PixelAligned": (1884307820, 2, (11, 0), (), "PixelAligned", None),
		# Method 'PlacedItem' returns object of type 'PlacedItem'
		"PlacedItem": (1148203062, 2, (9, 0), (), "PlacedItem", '{95CD20C3-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PluginItem' returns object of type 'PluginItem'
		"PluginItem": (1148203063, 2, (9, 0), (), "PluginItem", '{95CD20C5-AD72-11D3-B086-0010A4F5C335}'),
		"Position": (1885425779, 2, (12, 0), (), "Position", None),
		# Method 'RasterItem' returns object of type 'RasterItem'
		"RasterItem": (1148203064, 2, (9, 0), (), "RasterItem", '{95CD20C2-AD72-11D3-B086-0010A4F5C335}'),
		"Selected": (1936026723, 2, (11, 0), (), "Selected", None),
		"Sliced": (1883329388, 2, (11, 0), (), "Sliced", None),
		# Method 'SymbolItem' returns object of type 'SymbolItem'
		"SymbolItem": (1148203065, 2, (9, 0), (), "SymbolItem", '{4C78DFC3-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'Tags' returns object of type 'Tags'
		"Tags": (1667322951, 2, (9, 0), (), "Tags", '{95CD20EB-AD72-11D3-B086-0010A4F5C335}'),
		"Top": (1414484000, 2, (5, 0), (), "Top", None),
		"URL": (1884639820, 2, (8, 0), (), "URL", None),
		"VisibilityVariable": (1884703062, 2, (12, 0), (), "VisibilityVariable", None),
		"VisibleBounds": (1634293314, 2, (12, 0), (), "VisibleBounds", None),
		"Width": (1884506231, 2, (5, 0), (), "Width", None),
		"WrapInside": (1884583753, 2, (11, 0), (), "WrapInside", None),
		"WrapOffset": (1884583759, 2, (5, 0), (), "WrapOffset", None),
		"Wrapped": (1886672722, 2, (11, 0), (), "Wrapped", None),
		"ZOrderPosition": (1884966736, 2, (3, 0), (), "ZOrderPosition", None),
	}
	_prop_map_put_ = {
		"ArtworkKnockout": ((1883991659, LCID, 4, 0),()),
		"BlendingMode": ((1883401293, LCID, 4, 0),()),
		"ContentVariable": ((1883459414, LCID, 4, 0),()),
		"File": ((1634289235, LCID, 4, 0),()),
		"Height": ((1884506216, LCID, 4, 0),()),
		"Hidden": ((1634289732, LCID, 4, 0),()),
		"IsIsolated": ((1883861871, LCID, 4, 0),()),
		"Left": ((1279608404, LCID, 4, 0),()),
		"Locked": ((1634290763, LCID, 4, 0),()),
		"Matrix": ((1950767181, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"Note": ((1634291284, LCID, 4, 0),()),
		"Opacity": ((1884049264, LCID, 4, 0),()),
		"PixelAligned": ((1884307820, LCID, 4, 0),()),
		"Position": ((1885425779, LCID, 4, 0),()),
		"Selected": ((1936026723, LCID, 4, 0),()),
		"Sliced": ((1883329388, LCID, 4, 0),()),
		"Top": ((1414484000, LCID, 4, 0),()),
		"URL": ((1884639820, LCID, 4, 0),()),
		"VisibilityVariable": ((1884703062, LCID, 4, 0),()),
		"Width": ((1884506231, LCID, 4, 0),()),
		"WrapInside": ((1884583753, LCID, 4, 0),()),
		"WrapOffset": ((1884583759, LCID, 4, 0),()),
		"Wrapped": ((1886672722, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class PlacedItems(DispatchBaseClass):
	CLSID = IID('{95CD20ED-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	# Result is of type PlacedItem
	def Add(self):
		'create a placed item'
		ret = self._oleobj_.InvokeTypes(1666338892, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{95CD20C3-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type PlacedItem
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20C3-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20C3-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20C3-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class PluginItem(DispatchBaseClass):
	'Plugin artwork item'
	CLSID = IID('{95CD20C5-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def ApplyEffect(self, LiveEffectXML=defaultNamedNotOptArg):
		'Apply effect to selected artItem'
		return self._oleobj_.InvokeTypes(1799447892, LCID, 1, (24, 0), ((8, 1),),LiveEffectXML
			)

	def BringInPerspective(self, PositionX=defaultNamedNotOptArg, PositionY=defaultNamedNotOptArg, PerspectiveGridPlane=defaultNamedNotOptArg):
		'Place art object(s)in perspective grid at spedified perspective plane and coordinate'
		return self._oleobj_.InvokeTypes(1685013072, LCID, 1, (24, 0), ((5, 1), (5, 1), (3, 1)),PositionX
			, PositionY, PerspectiveGridPlane)

	def Copy(self):
		'Copy selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668247673, LCID, 1, (24, 0), (),)

	def Cut(self):
		'Cut selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668641824, LCID, 1, (24, 0), (),)

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def Duplicate(self, RelativeObject=defaultNamedOptArg, InsertionLocation=defaultNamedOptArg):
		'create a duplicate of the object'
		ret = self._oleobj_.InvokeTypes(1668050798, LCID, 1, (9, 0), ((12, 17), (12, 17)),RelativeObject
			, InsertionLocation)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', None)
		return ret

	def Move(self, RelativeObject=defaultNamedNotOptArg, InsertionLocation=defaultNamedNotOptArg):
		'move the object'
		return self._oleobj_.InvokeTypes(1836021349, LCID, 1, (24, 0), ((9, 1), (3, 1)),RelativeObject
			, InsertionLocation)

	def MoveAfter(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in behind object'
		return self._oleobj_.InvokeTypes(1299596641, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveBefore(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in front of object'
		return self._oleobj_.InvokeTypes(1299596642, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveToBeginning(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to beginning of container'
		return self._oleobj_.InvokeTypes(1299596646, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def MoveToEnd(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to end of container'
		return self._oleobj_.InvokeTypes(1299596645, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def Resize(self, ScaleX=defaultNamedNotOptArg, ScaleY=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg
			, ChangeFillGradients=defaultNamedOptArg, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, ScaleAbout=defaultNamedOptArg):
		'Scale art object(s)'
		return self._oleobj_.InvokeTypes(1685017421, LCID, 1, (24, 0), ((5, 1), (5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),ScaleX
			, ScaleY, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern
			, ChangeLineWidths, ScaleAbout)

	def Rotate(self, Angle=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, RotateAbout=defaultNamedOptArg):
		'Rotate art object(s)'
		return self._oleobj_.InvokeTypes(1685017165, LCID, 1, (24, 0), ((5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),Angle
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, RotateAbout
			)

	def SendScriptMessage(self, PluginName=defaultNamedNotOptArg, MessageSelector=defaultNamedNotOptArg, InputString=defaultNamedNotOptArg):
		'sends the script message to the required plugin'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1632850765, LCID, 1, (8, 0), ((8, 1), (8, 1), (8, 1)),PluginName
			, MessageSelector, InputString)

	def Transform(self, TransformationMatrix=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, TransformAbout=defaultNamedOptArg):
		'Transform art object(s) using a transformation matrix'
		return self._oleobj_.InvokeTypes(1414676814, LCID, 1, (24, 0), ((9, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),TransformationMatrix
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, ChangeLineWidths
			, TransformAbout)

	def Translate(self, DeltaX=defaultNamedOptArg, DeltaY=defaultNamedOptArg, TransformObjects=defaultNamedOptArg, TransformFillPatterns=defaultNamedOptArg
			, TransformFillGradients=defaultNamedOptArg, TransformStrokePattern=defaultNamedOptArg):
		'Reposition art object(s)'
		return self._oleobj_.InvokeTypes(1685018701, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),DeltaX
			, DeltaY, TransformObjects, TransformFillPatterns, TransformFillGradients, TransformStrokePattern
			)

	def ZOrder(self, ZOrderCmd=defaultNamedNotOptArg):
		'Arranges the art relative to other art in the group or layer'
		return self._oleobj_.InvokeTypes(1515147844, LCID, 1, (24, 0), ((3, 1),),ZOrderCmd
			)

	_prop_map_get_ = {
		"AbsoluteZOrderPosition": (1883331151, 2, (3, 0), (), "AbsoluteZOrderPosition", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtworkKnockout": (1883991659, 2, (3, 0), (), "ArtworkKnockout", None),
		"BlendingMode": (1883401293, 2, (3, 0), (), "BlendingMode", None),
		# Method 'CompoundPathItem' returns object of type 'CompoundPathItem'
		"CompoundPathItem": (1148203057, 2, (9, 0), (), "CompoundPathItem", '{95CD20BE-AD72-11D3-B086-0010A4F5C335}'),
		"ControlBounds": (1634291288, 2, (12, 0), (), "ControlBounds", None),
		"Editable": (1883325796, 2, (11, 0), (), "Editable", None),
		"GeometricBounds": (1634288199, 2, (12, 0), (), "GeometricBounds", None),
		# Method 'GraphItem' returns object of type 'GraphItem'
		"GraphItem": (1148203058, 2, (9, 0), (), "GraphItem", '{4C78DFB7-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'GroupItem' returns object of type 'GroupItem'
		"GroupItem": (1148203059, 2, (9, 0), (), "GroupItem", '{95CD20C6-AD72-11D3-B086-0010A4F5C335}'),
		"Height": (1884506216, 2, (5, 0), (), "Height", None),
		"Hidden": (1634289732, 2, (11, 0), (), "Hidden", None),
		"IsIsolated": (1883861871, 2, (11, 0), (), "IsIsolated", None),
		"IsTracing": (1769165938, 2, (11, 0), (), "IsTracing", None),
		# Method 'Layer' returns object of type 'Layer'
		"Layer": (1667320921, 2, (9, 0), (), "Layer", '{95CD20AC-AD72-11D3-B086-0010A4F5C335}'),
		"Left": (1279608404, 2, (5, 0), (), "Left", None),
		"Locked": (1634290763, 2, (11, 0), (), "Locked", None),
		# Method 'MeshItem' returns object of type 'MeshItem'
		"MeshItem": (1148203060, 2, (9, 0), (), "MeshItem", '{95CD20C4-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Note": (1634291284, 2, (8, 0), (), "Note", None),
		"Opacity": (1884049264, 2, (5, 0), (), "Opacity", None),
		"PageItem": (1396927603, 2, (9, 0), (), "PageItem", None),
		"PageItemType": (1954115685, 2, (3, 0), (), "PageItemType", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		# Method 'PathItem' returns object of type 'PathItem'
		"PathItem": (1148203061, 2, (9, 0), (), "PathItem", '{95CD20C0-AD72-11D3-B086-0010A4F5C335}'),
		"PixelAligned": (1884307820, 2, (11, 0), (), "PixelAligned", None),
		# Method 'PlacedItem' returns object of type 'PlacedItem'
		"PlacedItem": (1148203062, 2, (9, 0), (), "PlacedItem", '{95CD20C3-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PluginItem' returns object of type 'PluginItem'
		"PluginItem": (1148203063, 2, (9, 0), (), "PluginItem", '{95CD20C5-AD72-11D3-B086-0010A4F5C335}'),
		"Position": (1885425779, 2, (12, 0), (), "Position", None),
		# Method 'RasterItem' returns object of type 'RasterItem'
		"RasterItem": (1148203064, 2, (9, 0), (), "RasterItem", '{95CD20C2-AD72-11D3-B086-0010A4F5C335}'),
		"Selected": (1936026723, 2, (11, 0), (), "Selected", None),
		"Sliced": (1883329388, 2, (11, 0), (), "Sliced", None),
		# Method 'SymbolItem' returns object of type 'SymbolItem'
		"SymbolItem": (1148203065, 2, (9, 0), (), "SymbolItem", '{4C78DFC3-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'Tags' returns object of type 'Tags'
		"Tags": (1667322951, 2, (9, 0), (), "Tags", '{95CD20EB-AD72-11D3-B086-0010A4F5C335}'),
		"Top": (1414484000, 2, (5, 0), (), "Top", None),
		# Method 'Tracing' returns object of type 'TracingObject'
		"Tracing": (1735677042, 2, (9, 0), (), "Tracing", '{4C78DFC0-7A09-11D4-81A0-00C04F60ECCE}'),
		"URL": (1884639820, 2, (8, 0), (), "URL", None),
		"VisibilityVariable": (1884703062, 2, (12, 0), (), "VisibilityVariable", None),
		"VisibleBounds": (1634293314, 2, (12, 0), (), "VisibleBounds", None),
		"Width": (1884506231, 2, (5, 0), (), "Width", None),
		"WrapInside": (1884583753, 2, (11, 0), (), "WrapInside", None),
		"WrapOffset": (1884583759, 2, (5, 0), (), "WrapOffset", None),
		"Wrapped": (1886672722, 2, (11, 0), (), "Wrapped", None),
		"ZOrderPosition": (1884966736, 2, (3, 0), (), "ZOrderPosition", None),
	}
	_prop_map_put_ = {
		"ArtworkKnockout": ((1883991659, LCID, 4, 0),()),
		"BlendingMode": ((1883401293, LCID, 4, 0),()),
		"Height": ((1884506216, LCID, 4, 0),()),
		"Hidden": ((1634289732, LCID, 4, 0),()),
		"IsIsolated": ((1883861871, LCID, 4, 0),()),
		"Left": ((1279608404, LCID, 4, 0),()),
		"Locked": ((1634290763, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"Note": ((1634291284, LCID, 4, 0),()),
		"Opacity": ((1884049264, LCID, 4, 0),()),
		"PixelAligned": ((1884307820, LCID, 4, 0),()),
		"Position": ((1885425779, LCID, 4, 0),()),
		"Selected": ((1936026723, LCID, 4, 0),()),
		"Sliced": ((1883329388, LCID, 4, 0),()),
		"Top": ((1414484000, LCID, 4, 0),()),
		"URL": ((1884639820, LCID, 4, 0),()),
		"VisibilityVariable": ((1884703062, LCID, 4, 0),()),
		"Width": ((1884506231, LCID, 4, 0),()),
		"WrapInside": ((1884583753, LCID, 4, 0),()),
		"WrapOffset": ((1884583759, LCID, 4, 0),()),
		"Wrapped": ((1886672722, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class PluginItems(DispatchBaseClass):
	CLSID = IID('{95CD20EF-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type PluginItem
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20C5-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20C5-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20C5-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Preferences(DispatchBaseClass):
	'Preferences for Illustrator'
	CLSID = IID('{4C78DFCC-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = None

	def GetBooleanPreference(self, Key=defaultNamedNotOptArg):
		'retrieve the value of the application preference key as boolean'
		return self._oleobj_.InvokeTypes(1884309043, LCID, 1, (11, 0), ((8, 1),),Key
			)

	def GetIntegerPreference(self, Key=defaultNamedNotOptArg):
		'retrieve the value of the application preference key as integer'
		return self._oleobj_.InvokeTypes(1884309045, LCID, 1, (3, 0), ((8, 1),),Key
			)

	def GetRealPreference(self, Key=defaultNamedNotOptArg):
		'retrieve the value of the application preference key as real number'
		return self._oleobj_.InvokeTypes(1884309047, LCID, 1, (5, 0), ((8, 1),),Key
			)

	def GetStringPreference(self, Key=defaultNamedNotOptArg):
		'retrieve the value of the application preference key as string type'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1884309049, LCID, 1, (8, 0), ((8, 1),),Key
			)

	def RemovePreference(self, Key=defaultNamedNotOptArg):
		'delete the application preference key'
		return self._oleobj_.InvokeTypes(1883525190, LCID, 1, (24, 0), ((8, 1),),Key
			)

	def SetBooleanPreference(self, Key=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		'set the value of the application preference key as boolean'
		return self._oleobj_.InvokeTypes(1884309044, LCID, 1, (24, 0), ((8, 1), (11, 1)),Key
			, Value)

	def SetIntegerPreference(self, Key=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		'set the value of the application preference key as integer'
		return self._oleobj_.InvokeTypes(1884309046, LCID, 1, (24, 0), ((8, 1), (3, 1)),Key
			, Value)

	def SetRealPreference(self, Key=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		'set the value of the application preference key as real number'
		return self._oleobj_.InvokeTypes(1884309048, LCID, 1, (24, 0), ((8, 1), (5, 1)),Key
			, Value)

	def SetStringPreference(self, Key=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		'set the value of the application preference key as string type'
		return self._oleobj_.InvokeTypes(1884309089, LCID, 1, (24, 0), ((8, 1), (8, 1)),Key
			, Value)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'AutoCADFileOptions' returns object of type 'AutoCADFileOptions'
		"AutoCADFileOptions": (1884309042, 2, (9, 0), (), "AutoCADFileOptions", '{AD865867-DED8-42D6-9BD8-D77533905975}'),
		# Method 'PDFFileOptions' returns object of type 'PDFFileOptions'
		"PDFFileOptions": (1884309041, 2, (9, 0), (), "PDFFileOptions", '{4C78DFBD-7A09-11D4-81A0-00C04F60ECCC}'),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		# Method 'PhotoshopFileOptions' returns object of type 'PhotoshopFileOptions'
		"PhotoshopFileOptions": (1884309071, 2, (9, 0), (), "PhotoshopFileOptions", '{4C78DFBA-7A09-11D4-81A0-00C04F60ECCC}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class RasterItem(DispatchBaseClass):
	'Raster artwork item'
	CLSID = IID('{95CD20C2-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def ApplyEffect(self, LiveEffectXML=defaultNamedNotOptArg):
		'Apply effect to selected artItem'
		return self._oleobj_.InvokeTypes(1799447892, LCID, 1, (24, 0), ((8, 1),),LiveEffectXML
			)

	def BringInPerspective(self, PositionX=defaultNamedNotOptArg, PositionY=defaultNamedNotOptArg, PerspectiveGridPlane=defaultNamedNotOptArg):
		'Place art object(s)in perspective grid at spedified perspective plane and coordinate'
		return self._oleobj_.InvokeTypes(1685013072, LCID, 1, (24, 0), ((5, 1), (5, 1), (3, 1)),PositionX
			, PositionY, PerspectiveGridPlane)

	def Colorize(self, RasterColor=defaultNamedNotOptArg):
		'Colorize the RasterItem with a CMYK or RGB Color'
		return self._oleobj_.InvokeTypes(1667318605, LCID, 1, (24, 0), ((9, 1),),RasterColor
			)

	def Copy(self):
		'Copy selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668247673, LCID, 1, (24, 0), (),)

	def Cut(self):
		'Cut selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668641824, LCID, 1, (24, 0), (),)

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def Duplicate(self, RelativeObject=defaultNamedOptArg, InsertionLocation=defaultNamedOptArg):
		'create a duplicate of the object'
		ret = self._oleobj_.InvokeTypes(1668050798, LCID, 1, (9, 0), ((12, 17), (12, 17)),RelativeObject
			, InsertionLocation)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', None)
		return ret

	def Move(self, RelativeObject=defaultNamedNotOptArg, InsertionLocation=defaultNamedNotOptArg):
		'move the object'
		return self._oleobj_.InvokeTypes(1836021349, LCID, 1, (24, 0), ((9, 1), (3, 1)),RelativeObject
			, InsertionLocation)

	def MoveAfter(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in behind object'
		return self._oleobj_.InvokeTypes(1299596641, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveBefore(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in front of object'
		return self._oleobj_.InvokeTypes(1299596642, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveToBeginning(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to beginning of container'
		return self._oleobj_.InvokeTypes(1299596646, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def MoveToEnd(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to end of container'
		return self._oleobj_.InvokeTypes(1299596645, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def Resize(self, ScaleX=defaultNamedNotOptArg, ScaleY=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg
			, ChangeFillGradients=defaultNamedOptArg, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, ScaleAbout=defaultNamedOptArg):
		'Scale art object(s)'
		return self._oleobj_.InvokeTypes(1685017421, LCID, 1, (24, 0), ((5, 1), (5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),ScaleX
			, ScaleY, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern
			, ChangeLineWidths, ScaleAbout)

	def Rotate(self, Angle=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, RotateAbout=defaultNamedOptArg):
		'Rotate art object(s)'
		return self._oleobj_.InvokeTypes(1685017165, LCID, 1, (24, 0), ((5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),Angle
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, RotateAbout
			)

	def SendScriptMessage(self, PluginName=defaultNamedNotOptArg, MessageSelector=defaultNamedNotOptArg, InputString=defaultNamedNotOptArg):
		'sends the script message to the required plugin'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1632850765, LCID, 1, (8, 0), ((8, 1), (8, 1), (8, 1)),PluginName
			, MessageSelector, InputString)

	def SetMatrix(self, arg0=defaultUnnamedArg):
		'The transformation matrix of the raster art object'
		return self._oleobj_.InvokeTypes(1950767181, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	# Result is of type PluginItem
	def Trace(self):
		'Trace this raster object using default options.  Reorders this raster to the source art.'
		ret = self._oleobj_.InvokeTypes(1667322994, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Trace', '{95CD20C5-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Transform(self, TransformationMatrix=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, TransformAbout=defaultNamedOptArg):
		'Transform art object(s) using a transformation matrix'
		return self._oleobj_.InvokeTypes(1414676814, LCID, 1, (24, 0), ((9, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),TransformationMatrix
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, ChangeLineWidths
			, TransformAbout)

	def Translate(self, DeltaX=defaultNamedOptArg, DeltaY=defaultNamedOptArg, TransformObjects=defaultNamedOptArg, TransformFillPatterns=defaultNamedOptArg
			, TransformFillGradients=defaultNamedOptArg, TransformStrokePattern=defaultNamedOptArg):
		'Reposition art object(s)'
		return self._oleobj_.InvokeTypes(1685018701, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),DeltaX
			, DeltaY, TransformObjects, TransformFillPatterns, TransformFillGradients, TransformStrokePattern
			)

	def ZOrder(self, ZOrderCmd=defaultNamedNotOptArg):
		'Arranges the art relative to other art in the group or layer'
		return self._oleobj_.InvokeTypes(1515147844, LCID, 1, (24, 0), ((3, 1),),ZOrderCmd
			)

	_prop_map_get_ = {
		"AbsoluteZOrderPosition": (1883331151, 2, (3, 0), (), "AbsoluteZOrderPosition", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtworkKnockout": (1883991659, 2, (3, 0), (), "ArtworkKnockout", None),
		"BitsPerChannel": (1665290307, 2, (3, 0), (), "BitsPerChannel", None),
		"BlendingMode": (1883401293, 2, (3, 0), (), "BlendingMode", None),
		"BoundingBox": (1634288216, 2, (12, 0), (), "BoundingBox", None),
		"Channels": (1665353806, 2, (3, 0), (), "Channels", None),
		"Colorants": (1666141299, 2, (12, 0), (), "Colorants", None),
		"ColorizedGrayscale": (1665355596, 2, (11, 0), (), "ColorizedGrayscale", None),
		# Method 'CompoundPathItem' returns object of type 'CompoundPathItem'
		"CompoundPathItem": (1148203057, 2, (9, 0), (), "CompoundPathItem", '{95CD20BE-AD72-11D3-B086-0010A4F5C335}'),
		"ContentVariable": (1883459414, 2, (12, 0), (), "ContentVariable", None),
		"ControlBounds": (1634291288, 2, (12, 0), (), "ControlBounds", None),
		"Editable": (1883325796, 2, (11, 0), (), "Editable", None),
		"Embedded": (1667320907, 2, (11, 0), (), "Embedded", None),
		"File": (1634289235, 2, (8, 0), (), "File", None),
		"GeometricBounds": (1634288199, 2, (12, 0), (), "GeometricBounds", None),
		# Method 'GraphItem' returns object of type 'GraphItem'
		"GraphItem": (1148203058, 2, (9, 0), (), "GraphItem", '{4C78DFB7-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'GroupItem' returns object of type 'GroupItem'
		"GroupItem": (1148203059, 2, (9, 0), (), "GroupItem", '{95CD20C6-AD72-11D3-B086-0010A4F5C335}'),
		"Height": (1884506216, 2, (5, 0), (), "Height", None),
		"Hidden": (1634289732, 2, (11, 0), (), "Hidden", None),
		"ImageColorSpace": (1667318611, 2, (3, 0), (), "ImageColorSpace", None),
		"IsIsolated": (1883861871, 2, (11, 0), (), "IsIsolated", None),
		# Method 'Layer' returns object of type 'Layer'
		"Layer": (1667320921, 2, (9, 0), (), "Layer", '{95CD20AC-AD72-11D3-B086-0010A4F5C335}'),
		"Left": (1279608404, 2, (5, 0), (), "Left", None),
		"Locked": (1634290763, 2, (11, 0), (), "Locked", None),
		# Method 'Matrix' returns object of type '_Matrix'
		"Matrix": (1950767181, 2, (9, 0), (), "Matrix", '{95CD20C9-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'MeshItem' returns object of type 'MeshItem'
		"MeshItem": (1148203060, 2, (9, 0), (), "MeshItem", '{95CD20C4-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Note": (1634291284, 2, (8, 0), (), "Note", None),
		"Opacity": (1884049264, 2, (5, 0), (), "Opacity", None),
		"Overprint": (1883131728, 2, (11, 0), (), "Overprint", None),
		"PageItem": (1396927603, 2, (9, 0), (), "PageItem", None),
		"PageItemType": (1954115685, 2, (3, 0), (), "PageItemType", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		# Method 'PathItem' returns object of type 'PathItem'
		"PathItem": (1148203061, 2, (9, 0), (), "PathItem", '{95CD20C0-AD72-11D3-B086-0010A4F5C335}'),
		"PixelAligned": (1884307820, 2, (11, 0), (), "PixelAligned", None),
		# Method 'PlacedItem' returns object of type 'PlacedItem'
		"PlacedItem": (1148203062, 2, (9, 0), (), "PlacedItem", '{95CD20C3-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PluginItem' returns object of type 'PluginItem'
		"PluginItem": (1148203063, 2, (9, 0), (), "PluginItem", '{95CD20C5-AD72-11D3-B086-0010A4F5C335}'),
		"Position": (1885425779, 2, (12, 0), (), "Position", None),
		# Method 'RasterItem' returns object of type 'RasterItem'
		"RasterItem": (1148203064, 2, (9, 0), (), "RasterItem", '{95CD20C2-AD72-11D3-B086-0010A4F5C335}'),
		"Selected": (1936026723, 2, (11, 0), (), "Selected", None),
		"Sliced": (1883329388, 2, (11, 0), (), "Sliced", None),
		"Status": (1667320909, 2, (3, 0), (), "Status", None),
		# Method 'SymbolItem' returns object of type 'SymbolItem'
		"SymbolItem": (1148203065, 2, (9, 0), (), "SymbolItem", '{4C78DFC3-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'Tags' returns object of type 'Tags'
		"Tags": (1667322951, 2, (9, 0), (), "Tags", '{95CD20EB-AD72-11D3-B086-0010A4F5C335}'),
		"Top": (1414484000, 2, (5, 0), (), "Top", None),
		"Transparent": (1697934385, 2, (11, 0), (), "Transparent", None),
		"URL": (1884639820, 2, (8, 0), (), "URL", None),
		"VisibilityVariable": (1884703062, 2, (12, 0), (), "VisibilityVariable", None),
		"VisibleBounds": (1634293314, 2, (12, 0), (), "VisibleBounds", None),
		"Width": (1884506231, 2, (5, 0), (), "Width", None),
		"WrapInside": (1884583753, 2, (11, 0), (), "WrapInside", None),
		"WrapOffset": (1884583759, 2, (5, 0), (), "WrapOffset", None),
		"Wrapped": (1886672722, 2, (11, 0), (), "Wrapped", None),
		"ZOrderPosition": (1884966736, 2, (3, 0), (), "ZOrderPosition", None),
	}
	_prop_map_put_ = {
		"ArtworkKnockout": ((1883991659, LCID, 4, 0),()),
		"BlendingMode": ((1883401293, LCID, 4, 0),()),
		"BoundingBox": ((1634288216, LCID, 4, 0),()),
		"ContentVariable": ((1883459414, LCID, 4, 0),()),
		"Embedded": ((1667320907, LCID, 4, 0),()),
		"Height": ((1884506216, LCID, 4, 0),()),
		"Hidden": ((1634289732, LCID, 4, 0),()),
		"IsIsolated": ((1883861871, LCID, 4, 0),()),
		"Left": ((1279608404, LCID, 4, 0),()),
		"Locked": ((1634290763, LCID, 4, 0),()),
		"Matrix": ((1950767181, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"Note": ((1634291284, LCID, 4, 0),()),
		"Opacity": ((1884049264, LCID, 4, 0),()),
		"Overprint": ((1883131728, LCID, 4, 0),()),
		"PixelAligned": ((1884307820, LCID, 4, 0),()),
		"Position": ((1885425779, LCID, 4, 0),()),
		"Selected": ((1936026723, LCID, 4, 0),()),
		"Sliced": ((1883329388, LCID, 4, 0),()),
		"Top": ((1414484000, LCID, 4, 0),()),
		"URL": ((1884639820, LCID, 4, 0),()),
		"VisibilityVariable": ((1884703062, LCID, 4, 0),()),
		"Width": ((1884506231, LCID, 4, 0),()),
		"WrapInside": ((1884583753, LCID, 4, 0),()),
		"WrapOffset": ((1884583759, LCID, 4, 0),()),
		"Wrapped": ((1886672722, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class RasterItems(DispatchBaseClass):
	CLSID = IID('{95CD20EC-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type RasterItem
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20C2-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20C2-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20C2-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Spot(DispatchBaseClass):
	'A custom color'
	CLSID = IID('{95CD20B5-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def GetInternalColor(self):
		'Gets the internal color of a spot.'
		return self._ApplyTypes_(1799833955, 1, (12, 0), (), 'GetInternalColor', None,)

	def SetColor(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(1668246642, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Color": (1668246642, 2, (9, 0), (), "Color", None),
		"ColorType": (1885422420, 2, (3, 0), (), "ColorType", None),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"SpotKind": (1884504907, 2, (3, 0), (), "SpotKind", None),
	}
	_prop_map_put_ = {
		"Color": ((1668246642, LCID, 4, 0),()),
		"ColorType": ((1885422420, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Spots(DispatchBaseClass):
	'A collection of custom spot colors'
	CLSID = IID('{95CD20D9-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	# Result is of type Spot
	def Add(self):
		'create a spot color'
		ret = self._oleobj_.InvokeTypes(1667318595, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{95CD20B5-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type Spot
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20B5-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20B5-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20B5-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Stories(DispatchBaseClass):
	'A collection of stories'
	CLSID = IID('{0E9E7B8C-BF29-4A10-9B1C-9F292FDAB07A}')
	coclass_clsid = None

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type Story
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{8507C961-DE07-440E-A2D8-6D48247ABF79}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{8507C961-DE07-440E-A2D8-6D48247ABF79}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{8507C961-DE07-440E-A2D8-6D48247ABF79}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Story(DispatchBaseClass):
	'a contiguous block of text'
	CLSID = IID('{8507C961-DE07-440E-A2D8-6D48247ABF79}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'Characters' returns object of type 'Characters'
		"Characters": (1667784992, 2, (9, 0), (), "Characters", '{95CD20D5-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'InsertionPoints' returns object of type 'InsertionPoints'
		"InsertionPoints": (1667853939, 2, (9, 0), (), "InsertionPoints", '{20899C08-06F0-4803-BD2A-4059F9764852}'),
		"Length": (1818586727, 2, (3, 0), (), "Length", None),
		# Method 'Lines' returns object of type 'Lines'
		"Lines": (1668049262, 2, (9, 0), (), "Lines", '{95CD20D7-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'Paragraphs' returns object of type 'Paragraphs'
		"Paragraphs": (1668309362, 2, (9, 0), (), "Paragraphs", '{95CD20D8-AD72-11D3-B086-0010A4F5C335}'),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		# Method 'TextFrames' returns object of type 'TextFrames'
		"TextFrames": (1666472033, 2, (9, 0), (), "TextFrames", '{3CC63F1C-EA9C-4636-A16C-63808C42691E}'),
		# Method 'TextRange' returns object of type 'TextRange'
		"TextRange": (1884509232, 2, (9, 0), (), "TextRange", '{95CD20D0-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'TextRanges' returns object of type 'TextRanges'
		"TextRanges": (1668577396, 2, (9, 0), (), "TextRanges", '{20899C07-06F0-4803-BD2A-4059F9764852}'),
		"TextSelection": (1936026725, 2, (12, 0), (), "TextSelection", None),
		# Method 'Words' returns object of type 'Words'
		"Words": (1668771698, 2, (9, 0), (), "Words", '{95CD20D6-AD72-11D3-B086-0010A4F5C335}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Swatch(DispatchBaseClass):
	'A color swatch'
	CLSID = IID('{95CD20B8-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def SetColor(self, arg0=defaultUnnamedArg):
		'the color information of the swatch'
		return self._oleobj_.InvokeTypes(1668246642, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Color": (1668246642, 2, (9, 0), (), "Color", None),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"Color": ((1668246642, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class SwatchGroup(DispatchBaseClass):
	'A Swatch group'
	CLSID = IID('{75482E9D-B225-419A-8187-EE9EB424138E}')
	coclass_clsid = None

	def AddSpot(self, Spot=defaultNamedNotOptArg):
		'Add a spot swatch to the group'
		return self._oleobj_.InvokeTypes(1799443312, LCID, 1, (24, 0), ((9, 1),),Spot
			)

	def AddSwatch(self, Swatch=defaultNamedNotOptArg):
		'Add a swatch to the group'
		return self._oleobj_.InvokeTypes(1799443304, LCID, 1, (24, 0), ((9, 1),),Swatch
			)

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def GetAllSwatches(self):
		'get all swatches in the swatch group'
		return self._ApplyTypes_(1799831923, 1, (12, 0), (), 'GetAllSwatches', None,)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"Name": ((1886282093, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class SwatchGroups(DispatchBaseClass):
	'A collection of Swatch groups'
	CLSID = IID('{558EF46F-A352-4A0D-9B1C-A2F6118FE611}')
	coclass_clsid = None

	# Result is of type SwatchGroup
	def Add(self):
		'create a Swatch group'
		ret = self._oleobj_.InvokeTypes(1666402162, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{75482E9D-B225-419A-8187-EE9EB424138E}')
		return ret

	def GetSelected(self):
		'get selected swatchGroups in the document'
		return self._ApplyTypes_(1799446899, 1, (12, 0), (), 'GetSelected', None,)

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type SwatchGroup
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{75482E9D-B225-419A-8187-EE9EB424138E}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete a Swatch group from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{75482E9D-B225-419A-8187-EE9EB424138E}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{75482E9D-B225-419A-8187-EE9EB424138E}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Swatches(DispatchBaseClass):
	'A collection of swatches'
	CLSID = IID('{95CD20DA-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	# Result is of type Swatch
	def Add(self):
		'create a swatch'
		ret = self._oleobj_.InvokeTypes(1667322711, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{95CD20B8-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def GetSelected(self, IncludeSwatchInGroup=defaultNamedOptArg):
		'get selected swatches in the document'
		return self._ApplyTypes_(1632064339, 1, (12, 0), ((12, 17),), 'GetSelected', None,IncludeSwatchInGroup
			)

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type Swatch
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20B8-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20B8-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20B8-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Symbol(DispatchBaseClass):
	'A symbol'
	CLSID = IID('{4C78DFC0-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = None

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	# Result is of type Symbol
	def Duplicate(self):
		'create a duplicate of the object'
		ret = self._oleobj_.InvokeTypes(1668050798, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', '{4C78DFC0-7A09-11D4-81A0-00C04F60ECCC}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"Name": ((1886282093, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class SymbolItem(DispatchBaseClass):
	'An instance of a Symbol'
	CLSID = IID('{4C78DFC3-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = None

	def ApplyEffect(self, LiveEffectXML=defaultNamedNotOptArg):
		'Apply effect to selected artItem'
		return self._oleobj_.InvokeTypes(1799447892, LCID, 1, (24, 0), ((8, 1),),LiveEffectXML
			)

	def BreakLink(self):
		'Break link to the symbol'
		return self._oleobj_.InvokeTypes(1801536076, LCID, 1, (24, 0), (),)

	def BringInPerspective(self, PositionX=defaultNamedNotOptArg, PositionY=defaultNamedNotOptArg, PerspectiveGridPlane=defaultNamedNotOptArg):
		'Place art object(s)in perspective grid at spedified perspective plane and coordinate'
		return self._oleobj_.InvokeTypes(1685013072, LCID, 1, (24, 0), ((5, 1), (5, 1), (3, 1)),PositionX
			, PositionY, PerspectiveGridPlane)

	def Copy(self):
		'Copy selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668247673, LCID, 1, (24, 0), (),)

	def Cut(self):
		'Cut selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668641824, LCID, 1, (24, 0), (),)

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def Duplicate(self, RelativeObject=defaultNamedOptArg, InsertionLocation=defaultNamedOptArg):
		'create a duplicate of the object'
		ret = self._oleobj_.InvokeTypes(1668050798, LCID, 1, (9, 0), ((12, 17), (12, 17)),RelativeObject
			, InsertionLocation)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', None)
		return ret

	def Move(self, RelativeObject=defaultNamedNotOptArg, InsertionLocation=defaultNamedNotOptArg):
		'move the object'
		return self._oleobj_.InvokeTypes(1836021349, LCID, 1, (24, 0), ((9, 1), (3, 1)),RelativeObject
			, InsertionLocation)

	def MoveAfter(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in behind object'
		return self._oleobj_.InvokeTypes(1299596641, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveBefore(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in front of object'
		return self._oleobj_.InvokeTypes(1299596642, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveToBeginning(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to beginning of container'
		return self._oleobj_.InvokeTypes(1299596646, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def MoveToEnd(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to end of container'
		return self._oleobj_.InvokeTypes(1299596645, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def Resize(self, ScaleX=defaultNamedNotOptArg, ScaleY=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg
			, ChangeFillGradients=defaultNamedOptArg, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, ScaleAbout=defaultNamedOptArg):
		'Scale art object(s)'
		return self._oleobj_.InvokeTypes(1685017421, LCID, 1, (24, 0), ((5, 1), (5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),ScaleX
			, ScaleY, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern
			, ChangeLineWidths, ScaleAbout)

	def Rotate(self, Angle=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, RotateAbout=defaultNamedOptArg):
		'Rotate art object(s)'
		return self._oleobj_.InvokeTypes(1685017165, LCID, 1, (24, 0), ((5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),Angle
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, RotateAbout
			)

	def SendScriptMessage(self, PluginName=defaultNamedNotOptArg, MessageSelector=defaultNamedNotOptArg, InputString=defaultNamedNotOptArg):
		'sends the script message to the required plugin'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1632850765, LCID, 1, (8, 0), ((8, 1), (8, 1), (8, 1)),PluginName
			, MessageSelector, InputString)

	def Transform(self, TransformationMatrix=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, TransformAbout=defaultNamedOptArg):
		'Transform art object(s) using a transformation matrix'
		return self._oleobj_.InvokeTypes(1414676814, LCID, 1, (24, 0), ((9, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),TransformationMatrix
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, ChangeLineWidths
			, TransformAbout)

	def Translate(self, DeltaX=defaultNamedOptArg, DeltaY=defaultNamedOptArg, TransformObjects=defaultNamedOptArg, TransformFillPatterns=defaultNamedOptArg
			, TransformFillGradients=defaultNamedOptArg, TransformStrokePattern=defaultNamedOptArg):
		'Reposition art object(s)'
		return self._oleobj_.InvokeTypes(1685018701, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),DeltaX
			, DeltaY, TransformObjects, TransformFillPatterns, TransformFillGradients, TransformStrokePattern
			)

	def ZOrder(self, ZOrderCmd=defaultNamedNotOptArg):
		'Arranges the art relative to other art in the group or layer'
		return self._oleobj_.InvokeTypes(1515147844, LCID, 1, (24, 0), ((3, 1),),ZOrderCmd
			)

	_prop_map_get_ = {
		"AbsoluteZOrderPosition": (1883331151, 2, (3, 0), (), "AbsoluteZOrderPosition", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtworkKnockout": (1883991659, 2, (3, 0), (), "ArtworkKnockout", None),
		"BlendingMode": (1883401293, 2, (3, 0), (), "BlendingMode", None),
		# Method 'CompoundPathItem' returns object of type 'CompoundPathItem'
		"CompoundPathItem": (1148203057, 2, (9, 0), (), "CompoundPathItem", '{95CD20BE-AD72-11D3-B086-0010A4F5C335}'),
		"ControlBounds": (1634291288, 2, (12, 0), (), "ControlBounds", None),
		"Editable": (1883325796, 2, (11, 0), (), "Editable", None),
		"GeometricBounds": (1634288199, 2, (12, 0), (), "GeometricBounds", None),
		# Method 'GraphItem' returns object of type 'GraphItem'
		"GraphItem": (1148203058, 2, (9, 0), (), "GraphItem", '{4C78DFB7-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'GroupItem' returns object of type 'GroupItem'
		"GroupItem": (1148203059, 2, (9, 0), (), "GroupItem", '{95CD20C6-AD72-11D3-B086-0010A4F5C335}'),
		"Height": (1884506216, 2, (5, 0), (), "Height", None),
		"Hidden": (1634289732, 2, (11, 0), (), "Hidden", None),
		"IsIsolated": (1883861871, 2, (11, 0), (), "IsIsolated", None),
		# Method 'Layer' returns object of type 'Layer'
		"Layer": (1667320921, 2, (9, 0), (), "Layer", '{95CD20AC-AD72-11D3-B086-0010A4F5C335}'),
		"Left": (1279608404, 2, (5, 0), (), "Left", None),
		"Locked": (1634290763, 2, (11, 0), (), "Locked", None),
		# Method 'MeshItem' returns object of type 'MeshItem'
		"MeshItem": (1148203060, 2, (9, 0), (), "MeshItem", '{95CD20C4-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Note": (1634291284, 2, (8, 0), (), "Note", None),
		"Opacity": (1884049264, 2, (5, 0), (), "Opacity", None),
		"PageItem": (1396927603, 2, (9, 0), (), "PageItem", None),
		"PageItemType": (1954115685, 2, (3, 0), (), "PageItemType", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		# Method 'PathItem' returns object of type 'PathItem'
		"PathItem": (1148203061, 2, (9, 0), (), "PathItem", '{95CD20C0-AD72-11D3-B086-0010A4F5C335}'),
		"PixelAligned": (1884307820, 2, (11, 0), (), "PixelAligned", None),
		# Method 'PlacedItem' returns object of type 'PlacedItem'
		"PlacedItem": (1148203062, 2, (9, 0), (), "PlacedItem", '{95CD20C3-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PluginItem' returns object of type 'PluginItem'
		"PluginItem": (1148203063, 2, (9, 0), (), "PluginItem", '{95CD20C5-AD72-11D3-B086-0010A4F5C335}'),
		"Position": (1885425779, 2, (12, 0), (), "Position", None),
		# Method 'RasterItem' returns object of type 'RasterItem'
		"RasterItem": (1148203064, 2, (9, 0), (), "RasterItem", '{95CD20C2-AD72-11D3-B086-0010A4F5C335}'),
		"Selected": (1936026723, 2, (11, 0), (), "Selected", None),
		"Sliced": (1883329388, 2, (11, 0), (), "Sliced", None),
		# Method 'Symbol' returns object of type 'Symbol'
		"Symbol": (1667322713, 2, (9, 0), (), "Symbol", '{4C78DFC0-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'SymbolItem' returns object of type 'SymbolItem'
		"SymbolItem": (1148203065, 2, (9, 0), (), "SymbolItem", '{4C78DFC3-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'Tags' returns object of type 'Tags'
		"Tags": (1667322951, 2, (9, 0), (), "Tags", '{95CD20EB-AD72-11D3-B086-0010A4F5C335}'),
		"Top": (1414484000, 2, (5, 0), (), "Top", None),
		"URL": (1884639820, 2, (8, 0), (), "URL", None),
		"VisibilityVariable": (1884703062, 2, (12, 0), (), "VisibilityVariable", None),
		"VisibleBounds": (1634293314, 2, (12, 0), (), "VisibleBounds", None),
		"Width": (1884506231, 2, (5, 0), (), "Width", None),
		"WrapInside": (1884583753, 2, (11, 0), (), "WrapInside", None),
		"WrapOffset": (1884583759, 2, (5, 0), (), "WrapOffset", None),
		"Wrapped": (1886672722, 2, (11, 0), (), "Wrapped", None),
		"ZOrderPosition": (1884966736, 2, (3, 0), (), "ZOrderPosition", None),
	}
	_prop_map_put_ = {
		"ArtworkKnockout": ((1883991659, LCID, 4, 0),()),
		"BlendingMode": ((1883401293, LCID, 4, 0),()),
		"Height": ((1884506216, LCID, 4, 0),()),
		"Hidden": ((1634289732, LCID, 4, 0),()),
		"IsIsolated": ((1883861871, LCID, 4, 0),()),
		"Left": ((1279608404, LCID, 4, 0),()),
		"Locked": ((1634290763, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"Note": ((1634291284, LCID, 4, 0),()),
		"Opacity": ((1884049264, LCID, 4, 0),()),
		"PixelAligned": ((1884307820, LCID, 4, 0),()),
		"Position": ((1885425779, LCID, 4, 0),()),
		"Selected": ((1936026723, LCID, 4, 0),()),
		"Sliced": ((1883329388, LCID, 4, 0),()),
		"Symbol": ((1667322713, LCID, 4, 0),()),
		"Top": ((1414484000, LCID, 4, 0),()),
		"URL": ((1884639820, LCID, 4, 0),()),
		"VisibilityVariable": ((1884703062, LCID, 4, 0),()),
		"Width": ((1884506231, LCID, 4, 0),()),
		"WrapInside": ((1884583753, LCID, 4, 0),()),
		"WrapOffset": ((1884583759, LCID, 4, 0),()),
		"Wrapped": ((1886672722, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class SymbolItems(DispatchBaseClass):
	'A collection of symbol items'
	CLSID = IID('{4C78DFC6-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = None

	# Result is of type SymbolItem
	def Add(self, Symbol=defaultNamedNotOptArg):
		'an instance of a symbol item'
		ret = self._oleobj_.InvokeTypes(1666339683, LCID, 1, (9, 0), ((9, 1),),Symbol
			)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{4C78DFC3-7A09-11D4-81A0-00C04F60ECCC}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type SymbolItem
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{4C78DFC3-7A09-11D4-81A0-00C04F60ECCC}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{4C78DFC3-7A09-11D4-81A0-00C04F60ECCC}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{4C78DFC3-7A09-11D4-81A0-00C04F60ECCC}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Symbols(DispatchBaseClass):
	'A collection of symbols'
	CLSID = IID('{4C78DFC9-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = None

	# Result is of type Symbol
	def Add(self, SourceArt=defaultNamedNotOptArg, RegistrationPoint=defaultNamedOptArg):
		'create a symbol'
		ret = self._oleobj_.InvokeTypes(1667322713, LCID, 1, (9, 0), ((9, 1), (12, 17)),SourceArt
			, RegistrationPoint)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{4C78DFC0-7A09-11D4-81A0-00C04F60ECCC}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type Symbol
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{4C78DFC0-7A09-11D4-81A0-00C04F60ECCC}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{4C78DFC0-7A09-11D4-81A0-00C04F60ECCC}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{4C78DFC0-7A09-11D4-81A0-00C04F60ECCC}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Tag(DispatchBaseClass):
	'A tag associated with a piece of artwork'
	CLSID = IID('{95CD20BF-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"Value": (1634292822, 2, (8, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"Name": ((1886282093, LCID, 4, 0),()),
		"Value": ((1634292822, LCID, 4, 0),()),
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(1634292822, 2, (8, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Tags(DispatchBaseClass):
	'The collection of tags associated with a page item'
	CLSID = IID('{95CD20EB-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	# Result is of type Tag
	def Add(self):
		'create a tag'
		ret = self._oleobj_.InvokeTypes(1667322951, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{95CD20BF-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type Tag
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20BF-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20BF-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20BF-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class TextFont(DispatchBaseClass):
	'An installed font'
	CLSID = IID('{95CD20BC-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Family": (1886681190, 2, (8, 0), (), "Family", None),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"Style": (1954050932, 2, (8, 0), (), "Style", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class TextFonts(DispatchBaseClass):
	'A collection of fonts'
	CLSID = IID('{95CD20EA-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def GetCurrentFont(self):
		'Returns the current font name'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1181697859, LCID, 1, (8, 0), (),)

	# Result is of type TextFont
	def GetFontByName(self, FontName=defaultNamedNotOptArg):
		'Get the Text Font with the font name , if not avaiable it will create the substitute font'
		ret = self._oleobj_.InvokeTypes(1181696590, LCID, 1, (9, 0), ((8, 1),),FontName
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetFontByName', '{95CD20BC-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	def IsFontAvailable(self, FontName=defaultNamedNotOptArg):
		'Check if any original font is present with the given name'
		return self._oleobj_.InvokeTypes(1181698381, LCID, 1, (11, 0), ((8, 1),),FontName
			)

	# Result is of type TextFont
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20BC-AD72-11D3-B086-0010A4F5C335}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20BC-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20BC-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class TextFrame(DispatchBaseClass):
	'Text frame item'
	CLSID = IID('{F0692236-A49A-474D-9745-715426856760}')
	coclass_clsid = None

	def ApplyEffect(self, LiveEffectXML=defaultNamedNotOptArg):
		'Apply effect to selected artItem'
		return self._oleobj_.InvokeTypes(1799447892, LCID, 1, (24, 0), ((8, 1),),LiveEffectXML
			)

	def BringInPerspective(self, PositionX=defaultNamedNotOptArg, PositionY=defaultNamedNotOptArg, PerspectiveGridPlane=defaultNamedNotOptArg):
		'Place art object(s)in perspective grid at spedified perspective plane and coordinate'
		return self._oleobj_.InvokeTypes(1685013072, LCID, 1, (24, 0), ((5, 1), (5, 1), (3, 1)),PositionX
			, PositionY, PerspectiveGridPlane)

	# Result is of type TextFrame
	def ConvertAreaObjectToPointObject(self):
		'Convert Area Type Text Object To Point Type Object'
		ret = self._oleobj_.InvokeTypes(1128354896, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ConvertAreaObjectToPointObject', '{F0692236-A49A-474D-9745-715426856760}')
		return ret

	# Result is of type TextFrame
	def ConvertPointObjectToAreaObject(self):
		'Convert Point Type Text Object To Area Type Object'
		ret = self._oleobj_.InvokeTypes(1129337921, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ConvertPointObjectToAreaObject', '{F0692236-A49A-474D-9745-715426856760}')
		return ret

	def Copy(self):
		'Copy selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668247673, LCID, 1, (24, 0), (),)

	# Result is of type GroupItem
	def CreateOutline(self):
		'Convert text item to path items'
		ret = self._oleobj_.InvokeTypes(1163415620, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CreateOutline', '{95CD20C6-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Cut(self):
		'Cut selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668641824, LCID, 1, (24, 0), (),)

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	def Duplicate(self, RelativeObject=defaultNamedOptArg, InsertionLocation=defaultNamedOptArg):
		'create a duplicate of the object'
		ret = self._oleobj_.InvokeTypes(1668050798, LCID, 1, (9, 0), ((12, 17), (12, 17)),RelativeObject
			, InsertionLocation)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', None)
		return ret

	def GenerateThumbnailWithTextFrameProperties(self, TextString=defaultNamedNotOptArg, FontSize=defaultNamedNotOptArg, TextColor=defaultNamedNotOptArg, DestinationPath=defaultNamedNotOptArg):
		'Generates the thumbnail with the properties of first character in the text frame'
		return self._oleobj_.InvokeTypes(1196705360, LCID, 1, (24, 0), ((8, 1), (5, 1), (9, 1), (8, 1)),TextString
			, FontSize, TextColor, DestinationPath)

	def Move(self, RelativeObject=defaultNamedNotOptArg, InsertionLocation=defaultNamedNotOptArg):
		'move the object'
		return self._oleobj_.InvokeTypes(1836021349, LCID, 1, (24, 0), ((9, 1), (3, 1)),RelativeObject
			, InsertionLocation)

	def MoveAfter(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in behind object'
		return self._oleobj_.InvokeTypes(1299596641, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveBefore(self, RelativeObject=defaultNamedNotOptArg):
		'Move the PageItem in front of object'
		return self._oleobj_.InvokeTypes(1299596642, LCID, 1, (24, 0), ((9, 1),),RelativeObject
			)

	def MoveToBeginning(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to beginning of container'
		return self._oleobj_.InvokeTypes(1299596646, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def MoveToEnd(self, Container=defaultNamedNotOptArg):
		'Move the PageItem to end of container'
		return self._oleobj_.InvokeTypes(1299596645, LCID, 1, (24, 0), ((9, 1),),Container
			)

	def Resize(self, ScaleX=defaultNamedNotOptArg, ScaleY=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg
			, ChangeFillGradients=defaultNamedOptArg, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, ScaleAbout=defaultNamedOptArg):
		'Scale art object(s)'
		return self._oleobj_.InvokeTypes(1685017421, LCID, 1, (24, 0), ((5, 1), (5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),ScaleX
			, ScaleY, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern
			, ChangeLineWidths, ScaleAbout)

	def Rotate(self, Angle=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, RotateAbout=defaultNamedOptArg):
		'Rotate art object(s)'
		return self._oleobj_.InvokeTypes(1685017165, LCID, 1, (24, 0), ((5, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),Angle
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, RotateAbout
			)

	def SendScriptMessage(self, PluginName=defaultNamedNotOptArg, MessageSelector=defaultNamedNotOptArg, InputString=defaultNamedNotOptArg):
		'sends the script message to the required plugin'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1632850765, LCID, 1, (8, 0), ((8, 1), (8, 1), (8, 1)),PluginName
			, MessageSelector, InputString)

	def Transform(self, TransformationMatrix=defaultNamedNotOptArg, ChangePositions=defaultNamedOptArg, ChangeFillPatterns=defaultNamedOptArg, ChangeFillGradients=defaultNamedOptArg
			, ChangeStrokePattern=defaultNamedOptArg, ChangeLineWidths=defaultNamedOptArg, TransformAbout=defaultNamedOptArg):
		'Transform art object(s) using a transformation matrix'
		return self._oleobj_.InvokeTypes(1414676814, LCID, 1, (24, 0), ((9, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),TransformationMatrix
			, ChangePositions, ChangeFillPatterns, ChangeFillGradients, ChangeStrokePattern, ChangeLineWidths
			, TransformAbout)

	def Translate(self, DeltaX=defaultNamedOptArg, DeltaY=defaultNamedOptArg, TransformObjects=defaultNamedOptArg, TransformFillPatterns=defaultNamedOptArg
			, TransformFillGradients=defaultNamedOptArg, TransformStrokePattern=defaultNamedOptArg):
		'Reposition art object(s)'
		return self._oleobj_.InvokeTypes(1685018701, LCID, 1, (24, 0), ((12, 17), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),DeltaX
			, DeltaY, TransformObjects, TransformFillPatterns, TransformFillGradients, TransformStrokePattern
			)

	def ZOrder(self, ZOrderCmd=defaultNamedNotOptArg):
		'Arranges the art relative to other art in the group or layer'
		return self._oleobj_.InvokeTypes(1515147844, LCID, 1, (24, 0), ((3, 1),),ZOrderCmd
			)

	_prop_map_get_ = {
		"AbsoluteZOrderPosition": (1883331151, 2, (3, 0), (), "AbsoluteZOrderPosition", None),
		"Anchor": (1883336291, 2, (12, 0), (), "Anchor", None),
		"Antialias": (1884569953, 2, (3, 0), (), "Antialias", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtworkKnockout": (1883991659, 2, (3, 0), (), "ArtworkKnockout", None),
		"BlendingMode": (1883401293, 2, (3, 0), (), "BlendingMode", None),
		# Method 'Characters' returns object of type 'Characters'
		"Characters": (1667784992, 2, (9, 0), (), "Characters", '{95CD20D5-AD72-11D3-B086-0010A4F5C335}'),
		"ColumnCount": (1883458627, 2, (3, 0), (), "ColumnCount", None),
		"ColumnGutter": (1883458631, 2, (5, 0), (), "ColumnGutter", None),
		# Method 'CompoundPathItem' returns object of type 'CompoundPathItem'
		"CompoundPathItem": (1148203057, 2, (9, 0), (), "CompoundPathItem", '{95CD20BE-AD72-11D3-B086-0010A4F5C335}'),
		"ContentVariable": (1883459414, 2, (12, 0), (), "ContentVariable", None),
		"Contents": (1883459156, 2, (8, 0), (), "Contents", None),
		"ControlBounds": (1634291288, 2, (12, 0), (), "ControlBounds", None),
		"Editable": (1883325796, 2, (11, 0), (), "Editable", None),
		"EndTValue": (1884570964, 2, (5, 0), (), "EndTValue", None),
		"FirstBaseline": (1883652716, 2, (3, 0), (), "FirstBaseline", None),
		"FirstBaselineMin": (1883652685, 2, (5, 0), (), "FirstBaselineMin", None),
		"FlowLinksHorizontally": (1884444493, 2, (11, 0), (), "FlowLinksHorizontally", None),
		"GeometricBounds": (1634288199, 2, (12, 0), (), "GeometricBounds", None),
		# Method 'GraphItem' returns object of type 'GraphItem'
		"GraphItem": (1148203058, 2, (9, 0), (), "GraphItem", '{4C78DFB7-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'GroupItem' returns object of type 'GroupItem'
		"GroupItem": (1148203059, 2, (9, 0), (), "GroupItem", '{95CD20C6-AD72-11D3-B086-0010A4F5C335}'),
		"Height": (1884506216, 2, (5, 0), (), "Height", None),
		"Hidden": (1634289732, 2, (11, 0), (), "Hidden", None),
		# Method 'InsertionPoints' returns object of type 'InsertionPoints'
		"InsertionPoints": (1667853939, 2, (9, 0), (), "InsertionPoints", '{20899C08-06F0-4803-BD2A-4059F9764852}'),
		"IsIsolated": (1883861871, 2, (11, 0), (), "IsIsolated", None),
		"Kind": (1668826196, 2, (3, 0), (), "Kind", None),
		# Method 'Layer' returns object of type 'Layer'
		"Layer": (1667320921, 2, (9, 0), (), "Layer", '{95CD20AC-AD72-11D3-B086-0010A4F5C335}'),
		"Left": (1279608404, 2, (5, 0), (), "Left", None),
		# Method 'Lines' returns object of type 'Lines'
		"Lines": (1668049262, 2, (9, 0), (), "Lines", '{95CD20D7-AD72-11D3-B086-0010A4F5C335}'),
		"Locked": (1634290763, 2, (11, 0), (), "Locked", None),
		# Method 'Matrix' returns object of type '_Matrix'
		"Matrix": (1950767181, 2, (9, 0), (), "Matrix", '{95CD20C9-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'MeshItem' returns object of type 'MeshItem'
		"MeshItem": (1148203060, 2, (9, 0), (), "MeshItem", '{95CD20C4-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		# Method 'NextFrame' returns object of type 'TextFrame'
		"NextFrame": (1884178034, 2, (9, 0), (), "NextFrame", '{F0692236-A49A-474D-9745-715426856760}'),
		"Note": (1634291284, 2, (8, 0), (), "Note", None),
		"Opacity": (1884049264, 2, (5, 0), (), "Opacity", None),
		"OpticalAlignment": (1884246081, 2, (11, 0), (), "OpticalAlignment", None),
		"Orientation": (1886670674, 2, (3, 0), (), "Orientation", None),
		"PageItem": (1396927603, 2, (9, 0), (), "PageItem", None),
		"PageItemType": (1954115685, 2, (3, 0), (), "PageItemType", None),
		# Method 'Paragraphs' returns object of type 'Paragraphs'
		"Paragraphs": (1668309362, 2, (9, 0), (), "Paragraphs", '{95CD20D8-AD72-11D3-B086-0010A4F5C335}'),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		# Method 'PathItem' returns object of type 'PathItem'
		"PathItem": (1148203061, 2, (9, 0), (), "PathItem", '{95CD20C0-AD72-11D3-B086-0010A4F5C335}'),
		"PixelAligned": (1884307820, 2, (11, 0), (), "PixelAligned", None),
		# Method 'PlacedItem' returns object of type 'PlacedItem'
		"PlacedItem": (1148203062, 2, (9, 0), (), "PlacedItem", '{95CD20C3-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PluginItem' returns object of type 'PluginItem'
		"PluginItem": (1148203063, 2, (9, 0), (), "PluginItem", '{95CD20C5-AD72-11D3-B086-0010A4F5C335}'),
		"Position": (1885425779, 2, (12, 0), (), "Position", None),
		# Method 'PreviousFrame' returns object of type 'TextFrame'
		"PreviousFrame": (1666205298, 2, (9, 0), (), "PreviousFrame", '{F0692236-A49A-474D-9745-715426856760}'),
		# Method 'RasterItem' returns object of type 'RasterItem'
		"RasterItem": (1148203064, 2, (9, 0), (), "RasterItem", '{95CD20C2-AD72-11D3-B086-0010A4F5C335}'),
		"RowCount": (1884444483, 2, (3, 0), (), "RowCount", None),
		"RowGutter": (1884444487, 2, (5, 0), (), "RowGutter", None),
		"Selected": (1936026723, 2, (11, 0), (), "Selected", None),
		"Sliced": (1883329388, 2, (11, 0), (), "Sliced", None),
		"Spacing": (1884508225, 2, (5, 0), (), "Spacing", None),
		"StartTValue": (1884574548, 2, (5, 0), (), "StartTValue", None),
		# Method 'Story' returns object of type 'Story'
		"Story": (1666405455, 2, (9, 0), (), "Story", '{8507C961-DE07-440E-A2D8-6D48247ABF79}'),
		# Method 'SymbolItem' returns object of type 'SymbolItem'
		"SymbolItem": (1148203065, 2, (9, 0), (), "SymbolItem", '{4C78DFC3-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'Tags' returns object of type 'Tags'
		"Tags": (1667322951, 2, (9, 0), (), "Tags", '{95CD20EB-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'TextPath' returns object of type 'TextPath'
		"TextPath": (1666472048, 2, (9, 0), (), "TextPath", '{95CD20C8-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'TextRange' returns object of type 'TextRange'
		"TextRange": (1884509232, 2, (9, 0), (), "TextRange", '{95CD20D0-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'TextRanges' returns object of type 'TextRanges'
		"TextRanges": (1668577396, 2, (9, 0), (), "TextRanges", '{20899C07-06F0-4803-BD2A-4059F9764852}'),
		"TextSelection": (1936026725, 2, (12, 0), (), "TextSelection", None),
		"Top": (1414484000, 2, (5, 0), (), "Top", None),
		"URL": (1884639820, 2, (8, 0), (), "URL", None),
		"VisibilityVariable": (1884703062, 2, (12, 0), (), "VisibilityVariable", None),
		"VisibleBounds": (1634293314, 2, (12, 0), (), "VisibleBounds", None),
		"Width": (1884506231, 2, (5, 0), (), "Width", None),
		# Method 'Words' returns object of type 'Words'
		"Words": (1668771698, 2, (9, 0), (), "Words", '{95CD20D6-AD72-11D3-B086-0010A4F5C335}'),
		"WrapInside": (1884583753, 2, (11, 0), (), "WrapInside", None),
		"WrapOffset": (1884583759, 2, (5, 0), (), "WrapOffset", None),
		"Wrapped": (1886672722, 2, (11, 0), (), "Wrapped", None),
		"ZOrderPosition": (1884966736, 2, (3, 0), (), "ZOrderPosition", None),
	}
	_prop_map_put_ = {
		"Anchor": ((1883336291, LCID, 4, 0),()),
		"Antialias": ((1884569953, LCID, 4, 0),()),
		"ArtworkKnockout": ((1883991659, LCID, 4, 0),()),
		"BlendingMode": ((1883401293, LCID, 4, 0),()),
		"ColumnCount": ((1883458627, LCID, 4, 0),()),
		"ColumnGutter": ((1883458631, LCID, 4, 0),()),
		"ContentVariable": ((1883459414, LCID, 4, 0),()),
		"Contents": ((1883459156, LCID, 4, 0),()),
		"EndTValue": ((1884570964, LCID, 4, 0),()),
		"FirstBaseline": ((1883652716, LCID, 4, 0),()),
		"FirstBaselineMin": ((1883652685, LCID, 4, 0),()),
		"FlowLinksHorizontally": ((1884444493, LCID, 4, 0),()),
		"Height": ((1884506216, LCID, 4, 0),()),
		"Hidden": ((1634289732, LCID, 4, 0),()),
		"IsIsolated": ((1883861871, LCID, 4, 0),()),
		"Left": ((1279608404, LCID, 4, 0),()),
		"Locked": ((1634290763, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"NextFrame": ((1884178034, LCID, 4, 0),()),
		"Note": ((1634291284, LCID, 4, 0),()),
		"Opacity": ((1884049264, LCID, 4, 0),()),
		"OpticalAlignment": ((1884246081, LCID, 4, 0),()),
		"Orientation": ((1886670674, LCID, 4, 0),()),
		"PixelAligned": ((1884307820, LCID, 4, 0),()),
		"Position": ((1885425779, LCID, 4, 0),()),
		"PreviousFrame": ((1666205298, LCID, 4, 0),()),
		"RowCount": ((1884444483, LCID, 4, 0),()),
		"RowGutter": ((1884444487, LCID, 4, 0),()),
		"Selected": ((1936026723, LCID, 4, 0),()),
		"Sliced": ((1883329388, LCID, 4, 0),()),
		"Spacing": ((1884508225, LCID, 4, 0),()),
		"StartTValue": ((1884574548, LCID, 4, 0),()),
		"Top": ((1414484000, LCID, 4, 0),()),
		"URL": ((1884639820, LCID, 4, 0),()),
		"VisibilityVariable": ((1884703062, LCID, 4, 0),()),
		"Width": ((1884506231, LCID, 4, 0),()),
		"WrapInside": ((1884583753, LCID, 4, 0),()),
		"WrapOffset": ((1884583759, LCID, 4, 0),()),
		"Wrapped": ((1886672722, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class TextFrames(DispatchBaseClass):
	'A collection of text frame items'
	CLSID = IID('{3CC63F1C-EA9C-4636-A16C-63808C42691E}')
	coclass_clsid = None

	# Result is of type TextFrame
	def Add(self):
		'create a point text frame item'
		ret = self._oleobj_.InvokeTypes(1666467434, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{F0692236-A49A-474D-9745-715426856760}')
		return ret

	# Result is of type TextFrame
	def AreaText(self, TextPath=defaultNamedNotOptArg, Orientation=defaultNamedOptArg, BaseFrame=defaultNamedOptArg, PostFix=defaultNamedOptArg):
		'Create an area text frame item.'
		ret = self._oleobj_.InvokeTypes(1665226858, LCID, 1, (9, 0), ((9, 1), (12, 17), (12, 17), (12, 17)),TextPath
			, Orientation, BaseFrame, PostFix)
		if ret is not None:
			ret = Dispatch(ret, 'AreaText', '{F0692236-A49A-474D-9745-715426856760}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type TextFrame
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{F0692236-A49A-474D-9745-715426856760}')
		return ret

	# Result is of type TextFrame
	def PathText(self, TextPath=defaultNamedNotOptArg, StartTValue=defaultNamedOptArg, EndTValue=defaultNamedOptArg, Orientation=defaultNamedOptArg
			, BaseFrame=defaultNamedOptArg, PostFix=defaultNamedOptArg):
		'Create an on-path text frame item.'
		ret = self._oleobj_.InvokeTypes(1666144362, LCID, 1, (9, 0), ((9, 1), (12, 17), (12, 17), (12, 17), (12, 17), (12, 17)),TextPath
			, StartTValue, EndTValue, Orientation, BaseFrame, PostFix
			)
		if ret is not None:
			ret = Dispatch(ret, 'PathText', '{F0692236-A49A-474D-9745-715426856760}')
		return ret

	# Result is of type TextFrame
	def PointText(self, Anchor=defaultNamedNotOptArg, Orientation=defaultNamedOptArg):
		'Create a point text frame item.'
		ret = self._oleobj_.InvokeTypes(1666209898, LCID, 1, (9, 0), ((12, 1), (12, 17)),Anchor
			, Orientation)
		if ret is not None:
			ret = Dispatch(ret, 'PointText', '{F0692236-A49A-474D-9745-715426856760}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete a text frame from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{F0692236-A49A-474D-9745-715426856760}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{F0692236-A49A-474D-9745-715426856760}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class TextPath(DispatchBaseClass):
	'A text path item'
	CLSID = IID('{95CD20C8-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def SetEntirePath(self, PathPoints=defaultNamedNotOptArg):
		'Set the path using the provided array of anchor points'
		return self._oleobj_.InvokeTypes(1397051508, LCID, 1, (24, 0), ((12, 1),),PathPoints
			)

	def SetFillColor(self, arg0=defaultUnnamedArg):
		'fill color'
		return self._oleobj_.InvokeTypes(1634289219, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetStrokeColor(self, arg0=defaultUnnamedArg):
		'stroke color'
		return self._oleobj_.InvokeTypes(1634292547, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Area": (1634287954, 2, (5, 0), (), "Area", None),
		"BlendingMode": (1883401293, 2, (3, 0), (), "BlendingMode", None),
		"Clipping": (1634288464, 2, (11, 0), (), "Clipping", None),
		"Closed": (1634288492, 2, (11, 0), (), "Closed", None),
		"Editable": (1883325796, 2, (11, 0), (), "Editable", None),
		"Evenodd": (1634288975, 2, (11, 0), (), "Evenodd", None),
		"FillColor": (1634289219, 2, (9, 0), (), "FillColor", None),
		"FillOverprint": (1634289231, 2, (11, 0), (), "FillOverprint", None),
		"Filled": (1634289232, 2, (11, 0), (), "Filled", None),
		"Guides": (1634289476, 2, (11, 0), (), "Guides", None),
		"Height": (1884506216, 2, (5, 0), (), "Height", None),
		"Left": (1279608404, 2, (5, 0), (), "Left", None),
		"Note": (1634291284, 2, (8, 0), (), "Note", None),
		"Opacity": (1884049264, 2, (5, 0), (), "Opacity", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		# Method 'PathPoints' returns object of type 'PathPoints'
		"PathPoints": (1667321939, 2, (9, 0), (), "PathPoints", '{95CD20E2-AD72-11D3-B086-0010A4F5C335}'),
		"Polarity": (1634291792, 2, (3, 0), (), "Polarity", None),
		"Position": (1885425779, 2, (12, 0), (), "Position", None),
		"Resolution": (1634292314, 2, (5, 0), (), "Resolution", None),
		"SelectedPathPoints": (1634292600, 2, (12, 0), (), "SelectedPathPoints", None),
		"StrokeCap": (1634288504, 2, (3, 0), (), "StrokeCap", None),
		"StrokeColor": (1634292547, 2, (9, 0), (), "StrokeColor", None),
		"StrokeDashOffset": (1634288719, 2, (5, 0), (), "StrokeDashOffset", None),
		"StrokeDashes": (1634288723, 2, (12, 0), (), "StrokeDashes", None),
		"StrokeJoin": (1634290286, 2, (3, 0), (), "StrokeJoin", None),
		"StrokeMiterLimit": (1634291064, 2, (5, 0), (), "StrokeMiterLimit", None),
		"StrokeOverprint": (1634292559, 2, (11, 0), (), "StrokeOverprint", None),
		"StrokeWidth": (1634292567, 2, (5, 0), (), "StrokeWidth", None),
		"Stroked": (1634292560, 2, (11, 0), (), "Stroked", None),
		"Top": (1414484000, 2, (5, 0), (), "Top", None),
		"Width": (1884506231, 2, (5, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"BlendingMode": ((1883401293, LCID, 4, 0),()),
		"Clipping": ((1634288464, LCID, 4, 0),()),
		"Closed": ((1634288492, LCID, 4, 0),()),
		"Evenodd": ((1634288975, LCID, 4, 0),()),
		"FillColor": ((1634289219, LCID, 4, 0),()),
		"FillOverprint": ((1634289231, LCID, 4, 0),()),
		"Filled": ((1634289232, LCID, 4, 0),()),
		"Guides": ((1634289476, LCID, 4, 0),()),
		"Height": ((1884506216, LCID, 4, 0),()),
		"Left": ((1279608404, LCID, 4, 0),()),
		"Note": ((1634291284, LCID, 4, 0),()),
		"Opacity": ((1884049264, LCID, 4, 0),()),
		"Polarity": ((1634291792, LCID, 4, 0),()),
		"Position": ((1885425779, LCID, 4, 0),()),
		"Resolution": ((1634292314, LCID, 4, 0),()),
		"StrokeCap": ((1634288504, LCID, 4, 0),()),
		"StrokeColor": ((1634292547, LCID, 4, 0),()),
		"StrokeDashOffset": ((1634288719, LCID, 4, 0),()),
		"StrokeDashes": ((1634288723, LCID, 4, 0),()),
		"StrokeJoin": ((1634290286, LCID, 4, 0),()),
		"StrokeMiterLimit": ((1634291064, LCID, 4, 0),()),
		"StrokeOverprint": ((1634292559, LCID, 4, 0),()),
		"StrokeWidth": ((1634292567, LCID, 4, 0),()),
		"Stroked": ((1634292560, LCID, 4, 0),()),
		"Top": ((1414484000, LCID, 4, 0),()),
		"Width": ((1884506231, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class TextRange(DispatchBaseClass):
	'a range of characters from a text item'
	CLSID = IID('{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def ChangeCaseTo(self, Type=defaultNamedNotOptArg):
		'change the capitalization of text'
		return self._oleobj_.InvokeTypes(1884574261, LCID, 1, (24, 0), ((3, 1),),Type
			)

	def DeSelect(self):
		'deselect the text range'
		return self._oleobj_.InvokeTypes(1884574258, LCID, 1, (24, 0), (),)

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	# Result is of type TextRange
	def Duplicate(self, RelativeObject=defaultNamedOptArg, InsertionLocation=defaultNamedOptArg):
		'create a duplicate of the object'
		ret = self._oleobj_.InvokeTypes(1668050798, LCID, 1, (9, 0), ((12, 17), (12, 17)),RelativeObject
			, InsertionLocation)
		if ret is not None:
			ret = Dispatch(ret, 'Duplicate', '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def GetParagraphLength(self):
		'get the length of the first paragraph'
		return self._oleobj_.InvokeTypes(1884574264, LCID, 1, (3, 0), (),)

	def GetTextRunLength(self):
		'get the length of the first text run'
		return self._oleobj_.InvokeTypes(1884574263, LCID, 1, (3, 0), (),)

	def Move(self, RelativeObject=defaultNamedNotOptArg, InsertionLocation=defaultNamedNotOptArg):
		'move the object'
		return self._oleobj_.InvokeTypes(1836021349, LCID, 1, (24, 0), ((9, 1), (3, 1)),RelativeObject
			, InsertionLocation)

	def Select(self, AddToDocument=defaultNamedOptArg):
		'select the text range'
		return self._oleobj_.InvokeTypes(1884574256, LCID, 1, (24, 0), ((12, 17),),AddToDocument
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'CharacterAttributes' returns object of type 'CharacterAttributes'
		"CharacterAttributes": (1130905972, 2, (9, 0), (), "CharacterAttributes", '{4C78DFCD-7A09-11D4-81A0-00C04F60ECCC}'),
		"CharacterOffset": (1884509266, 2, (3, 0), (), "CharacterOffset", None),
		# Method 'CharacterStyles' returns object of type 'CharacterStyles'
		"CharacterStyles": (1665356628, 2, (9, 0), (), "CharacterStyles", '{255CD590-0FBF-4345-94F5-871C4021D6BF}'),
		# Method 'Characters' returns object of type 'Characters'
		"Characters": (1667784992, 2, (9, 0), (), "Characters", '{95CD20D5-AD72-11D3-B086-0010A4F5C335}'),
		"Contents": (1883459156, 2, (8, 0), (), "Contents", None),
		"End": (1883590212, 2, (3, 0), (), "End", None),
		# Method 'InsertionPoints' returns object of type 'InsertionPoints'
		"InsertionPoints": (1667853939, 2, (9, 0), (), "InsertionPoints", '{20899C08-06F0-4803-BD2A-4059F9764852}'),
		"Kerning": (1884566068, 2, (3, 0), (), "Kerning", None),
		"Length": (1818586727, 2, (3, 0), (), "Length", None),
		# Method 'Lines' returns object of type 'Lines'
		"Lines": (1668049262, 2, (9, 0), (), "Lines", '{95CD20D7-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'ParagraphAttributes' returns object of type 'ParagraphAttributes'
		"ParagraphAttributes": (1348944244, 2, (9, 0), (), "ParagraphAttributes", '{4C78DFCE-7A09-11D4-81A0-00C04F60ECCC}'),
		# Method 'ParagraphStyles' returns object of type 'ParagraphStyles'
		"ParagraphStyles": (1666208596, 2, (9, 0), (), "ParagraphStyles", '{0E3BF58B-A0F2-4776-9CD0-279FCB26009E}'),
		# Method 'Paragraphs' returns object of type 'Paragraphs'
		"Paragraphs": (1668309362, 2, (9, 0), (), "Paragraphs", '{95CD20D8-AD72-11D3-B086-0010A4F5C335}'),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"Start": (1883391303, 2, (3, 0), (), "Start", None),
		# Method 'Story' returns object of type 'Story'
		"Story": (1666405455, 2, (9, 0), (), "Story", '{8507C961-DE07-440E-A2D8-6D48247ABF79}'),
		# Method 'TextRanges' returns object of type 'TextRanges'
		"TextRanges": (1668577396, 2, (9, 0), (), "TextRanges", '{20899C07-06F0-4803-BD2A-4059F9764852}'),
		"TextSelection": (1936026725, 2, (12, 0), (), "TextSelection", None),
		# Method 'Words' returns object of type 'Words'
		"Words": (1668771698, 2, (9, 0), (), "Words", '{95CD20D6-AD72-11D3-B086-0010A4F5C335}'),
	}
	_prop_map_put_ = {
		"CharacterOffset": ((1884509266, LCID, 4, 0),()),
		"Contents": ((1883459156, LCID, 4, 0),()),
		"End": ((1883590212, LCID, 4, 0),()),
		"Kerning": ((1884566068, LCID, 4, 0),()),
		"Length": ((1818586727, LCID, 4, 0),()),
		"Start": ((1883391303, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class TextRanges(DispatchBaseClass):
	'A collection of text range items'
	CLSID = IID('{20899C07-06F0-4803-BD2A-4059F9764852}')
	coclass_clsid = None

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type TextRange
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class TracingObject(DispatchBaseClass):
	'A tracing object.'
	CLSID = IID('{4C78DFC0-7A09-11D4-81A0-00C04F60ECCE}')
	coclass_clsid = None

	# Result is of type GroupItem
	def ExpandTracing(self, Viewed=defaultNamedOptArg):
		'Expand the tracing to paths.  Deletes this tracing object.'
		ret = self._oleobj_.InvokeTypes(1953645912, LCID, 1, (9, 0), ((12, 17),),Viewed
			)
		if ret is not None:
			ret = Dispatch(ret, 'ExpandTracing', '{95CD20C6-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def ReleaseTracing(self):
		'Release the source artwork for the tracing object.  Deletes this tracing object.'
		ret = self._oleobj_.InvokeTypes(1953649228, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'ReleaseTracing', None)
		return ret

	_prop_map_get_ = {
		"AnchorCount": (1953644867, 2, (3, 0), (), "AnchorCount", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"PathCount": (1953648707, 2, (3, 0), (), "PathCount", None),
		"SourceArt": (1953649507, 2, (9, 0), (), "SourceArt", None),
		# Method 'TracingOptions' returns object of type 'TracingOptions'
		"TracingOptions": (1953648499, 2, (9, 0), (), "TracingOptions", '{4C78DFC0-7A09-11D4-81A0-00C04F60ECCD}'),
		"UsedColorCount": (1953648195, 2, (3, 0), (), "UsedColorCount", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class TracingOptions(DispatchBaseClass):
	'Tracing options that guide the tracing process.'
	CLSID = IID('{4C78DFC0-7A09-11D4-81A0-00C04F60ECCD}')
	coclass_clsid = None

	def LoadFromPreset(self, PresetName=defaultNamedNotOptArg):
		'Load options from preset.'
		return self._oleobj_.InvokeTypes(1953451088, LCID, 1, (11, 0), ((8, 1),),PresetName
			)

	def StoreToPreset(self, PresetName=defaultNamedNotOptArg):
		'Store options to a preset kAiVectorizeSuite.  Will overwrite an existing (unlocked) preset if names match.'
		return self._oleobj_.InvokeTypes(1953452880, LCID, 1, (11, 0), ((8, 1),),PresetName
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ColorFidelity": (1953451363, 2, (5, 0), (), "ColorFidelity", None),
		"ColorGroup": (1953448807, 2, (8, 0), (), "ColorGroup", None),
		"CornerFidelity": (1953448818, 2, (5, 0), (), "CornerFidelity", None),
		"Fills": (1953449580, 2, (11, 0), (), "Fills", None),
		"GrayLevels": (1953449836, 2, (3, 0), (), "GrayLevels", None),
		"IgnoreWhite": (1953450327, 2, (11, 0), (), "IgnoreWhite", None),
		"MaxStrokeWeight": (1953451384, 2, (5, 0), (), "MaxStrokeWeight", None),
		"NoiseFidelity": (1953451622, 2, (5, 0), (), "NoiseFidelity", None),
		"Palette": (1953452140, 2, (8, 0), (), "Palette", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"PathFidelity": (1953452102, 2, (5, 0), (), "PathFidelity", None),
		"Preset": (1953452146, 2, (8, 0), (), "Preset", None),
		"SnapCurveToLines": (1953452899, 2, (11, 0), (), "SnapCurveToLines", None),
		"Strokes": (1953452916, 2, (11, 0), (), "Strokes", None),
		"Threshold": (1953453160, 2, (3, 0), (), "Threshold", None),
		"TracingColorTypeValue": (1953448788, 2, (3, 0), (), "TracingColorTypeValue", None),
		"TracingColors": (1953448806, 2, (3, 0), (), "TracingColors", None),
		"TracingMethod": (1953451365, 2, (3, 0), (), "TracingMethod", None),
		"TracingMode": (1953451364, 2, (3, 0), (), "TracingMode", None),
		"ViewMode": (1953453686, 2, (3, 0), (), "ViewMode", None),
	}
	_prop_map_put_ = {
		"ColorFidelity": ((1953451363, LCID, 4, 0),()),
		"ColorGroup": ((1953448807, LCID, 4, 0),()),
		"CornerFidelity": ((1953448818, LCID, 4, 0),()),
		"Fills": ((1953449580, LCID, 4, 0),()),
		"GrayLevels": ((1953449836, LCID, 4, 0),()),
		"IgnoreWhite": ((1953450327, LCID, 4, 0),()),
		"MaxStrokeWeight": ((1953451384, LCID, 4, 0),()),
		"NoiseFidelity": ((1953451622, LCID, 4, 0),()),
		"Palette": ((1953452140, LCID, 4, 0),()),
		"PathFidelity": ((1953452102, LCID, 4, 0),()),
		"SnapCurveToLines": ((1953452899, LCID, 4, 0),()),
		"Strokes": ((1953452916, LCID, 4, 0),()),
		"Threshold": ((1953453160, LCID, 4, 0),()),
		"TracingColorTypeValue": ((1953448788, LCID, 4, 0),()),
		"TracingColors": ((1953448806, LCID, 4, 0),()),
		"TracingMethod": ((1953451365, LCID, 4, 0),()),
		"TracingMode": ((1953451364, LCID, 4, 0),()),
		"ViewMode": ((1953453686, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Variable(DispatchBaseClass):
	'Dynamic object used to create data-driven graphics.'
	CLSID = IID('{4C78DFA2-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = None

	def Delete(self):
		'delete the object'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Kind": (1668826196, 2, (3, 0), (), "Kind", None),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		# Method 'PageItems' returns object of type 'PageItems'
		"PageItems": (1667318100, 2, (9, 0), (), "PageItems", '{95CD20E0-AD72-11D3-B086-0010A4F5C335}'),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
		"Kind": ((1668826196, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Variables(DispatchBaseClass):
	'A collection of variables'
	CLSID = IID('{4C78DFA8-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = None

	# Result is of type Variable
	def Add(self):
		'create a variable'
		ret = self._oleobj_.InvokeTypes(1951818098, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{4C78DFA2-7A09-11D4-81A0-00C04F60ECCC}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type Variable
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{4C78DFA2-7A09-11D4-81A0-00C04F60ECCC}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{4C78DFA2-7A09-11D4-81A0-00C04F60ECCC}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{4C78DFA2-7A09-11D4-81A0-00C04F60ECCC}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class View(DispatchBaseClass):
	'A view'
	CLSID = IID('{95CD20AD-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Bounds": (1885498980, 2, (12, 0), (), "Bounds", None),
		"CenterPoint": (1634288468, 2, (12, 0), (), "CenterPoint", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
		"ScreenMode": (1634293325, 2, (3, 0), (), "ScreenMode", None),
		"Zoom": (1634294349, 2, (5, 0), (), "Zoom", None),
	}
	_prop_map_put_ = {
		"CenterPoint": ((1634288468, LCID, 4, 0),()),
		"ScreenMode": ((1634293325, LCID, 4, 0),()),
		"Zoom": ((1634294349, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class Views(DispatchBaseClass):
	'A collection of views'
	CLSID = IID('{95CD20F0-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type View
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20AD-AD72-11D3-B086-0010A4F5C335}')
		return ret

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20AD-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20AD-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class Words(DispatchBaseClass):
	'A collection of words'
	CLSID = IID('{95CD20D6-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = None

	# Result is of type TextRange
	def Add(self, Contents=defaultNamedNotOptArg, RelativeObject=defaultNamedOptArg, InsertionLocation=defaultNamedOptArg):
		'create a word'
		ret = self._oleobj_.InvokeTypes(1668771698, LCID, 1, (9, 0), ((8, 1), (12, 17), (12, 17)),Contents
			, RelativeObject, InsertionLocation)
		if ret is not None:
			ret = Dispatch(ret, 'Add', '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	# Result is of type TextRange
	def AddBefore(self, Contents=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1131561574, LCID, 1, (9, 0), ((8, 1),),Contents
			)
		if ret is not None:
			ret = Dispatch(ret, 'AddBefore', '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Index(self, ItemPtr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1885955192, LCID, 1, (3, 0), ((9, 1),),ItemPtr
			)

	# Result is of type TextRange
	# The method Item is actually a property, but must be used as a method to correctly pass the arguments
	def Item(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Remove(self, Item=defaultNamedNotOptArg):
		'Delete an element from the collection'
		return self._oleobj_.InvokeTypes(1684368495, LCID, 1, (24, 0), ((9, 1),),Item
			)

	def RemoveAll(self):
		return self._oleobj_.InvokeTypes(1380009324, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Count": (1668183141, 2, (3, 0), (), "Count", None),
		"Parent": (1668574834, 2, (9, 0), (), "Parent", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, ItemKey=defaultNamedNotOptArg):
		'get an element from the collection'
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),ItemKey
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95CD20D0-AD72-11D3-B086-0010A4F5C335}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1668183141, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class _Application(DispatchBaseClass):
	'The Adobe Illustrator application'
	CLSID = IID('{95CD20AA-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{0FA36670-F0BC-48C0-AD25-6CF62CAD3A31}')

	# Result is of type _Matrix
	def ConcatenateMatrix(self, Matrix=defaultNamedNotOptArg, SecondMatrix=defaultNamedNotOptArg):
		'Concatenate two transformation matrices'
		ret = self._oleobj_.InvokeTypes(1668566360, LCID, 1, (9, 0), ((9, 1), (9, 1)),Matrix
			, SecondMatrix)
		if ret is not None:
			ret = Dispatch(ret, 'ConcatenateMatrix', '{95CD20C9-AD72-11D3-B086-0010A4F5C335}')
		return ret

	# Result is of type _Matrix
	def ConcatenateRotationMatrix(self, Matrix=defaultNamedNotOptArg, Angle=defaultNamedNotOptArg):
		'Concatenate a rotation matrix to a transformation matrix'
		ret = self._oleobj_.InvokeTypes(1668567629, LCID, 1, (9, 0), ((9, 1), (5, 1)),Matrix
			, Angle)
		if ret is not None:
			ret = Dispatch(ret, 'ConcatenateRotationMatrix', '{95CD20C9-AD72-11D3-B086-0010A4F5C335}')
		return ret

	# Result is of type _Matrix
	def ConcatenateScaleMatrix(self, Matrix=defaultNamedNotOptArg, ScaleX=defaultNamedOptArg, ScaleY=defaultNamedOptArg):
		'Concatenate a scale matrix to a transformation matrix'
		ret = self._oleobj_.InvokeTypes(1668567885, LCID, 1, (9, 0), ((9, 1), (12, 17), (12, 17)),Matrix
			, ScaleX, ScaleY)
		if ret is not None:
			ret = Dispatch(ret, 'ConcatenateScaleMatrix', '{95CD20C9-AD72-11D3-B086-0010A4F5C335}')
		return ret

	# Result is of type _Matrix
	def ConcatenateTranslationMatrix(self, Matrix=defaultNamedNotOptArg, DeltaX=defaultNamedOptArg, DeltaY=defaultNamedOptArg):
		'Concatenate a translation to a transformation matrix'
		ret = self._oleobj_.InvokeTypes(1668569165, LCID, 1, (9, 0), ((9, 1), (12, 17), (12, 17)),Matrix
			, DeltaX, DeltaY)
		if ret is not None:
			ret = Dispatch(ret, 'ConcatenateTranslationMatrix', '{95CD20C9-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def ConvertSampleColor(self, SourceColorSpace=defaultNamedNotOptArg, SourceColor=defaultNamedNotOptArg, DestColorSpace=defaultNamedNotOptArg, ColorConvertPurpose=defaultNamedNotOptArg
			, SourceHasAlpha=defaultNamedOptArg, DestHasAlpha=defaultNamedOptArg):
		'Converts a sample-component color from one color space to another.'
		return self._ApplyTypes_(1631802179, 1, (12, 0), ((3, 1), (12, 1), (3, 1), (3, 1), (12, 17), (12, 17)), 'ConvertSampleColor', None,SourceColorSpace
			, SourceColor, DestColorSpace, ColorConvertPurpose, SourceHasAlpha, DestHasAlpha
			)

	def Copy(self):
		'Copy current selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668247673, LCID, 1, (24, 0), (),)

	def Cut(self):
		'Cut current selection to the clipboard'
		return self._oleobj_.InvokeTypes(1668641824, LCID, 1, (24, 0), (),)

	def DeleteWorkspace(self, WorkspaceName=defaultNamedNotOptArg):
		'Deletes an existing workspace'
		return self._oleobj_.InvokeTypes(1799439447, LCID, 1, (11, 0), ((8, 1),),WorkspaceName
			)

	def DoJavaScript(self, JavaScriptCode=defaultNamedNotOptArg, Arguments=defaultNamedOptArg, ExecutionMode=defaultNamedOptArg):
		'Execute javascript code'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1147828311, LCID, 1, (8, 0), ((8, 1), (12, 17), (12, 17)),JavaScriptCode
			, Arguments, ExecutionMode)

	def DoJavaScriptFile(self, JavaScriptFile=defaultNamedNotOptArg, Arguments=defaultNamedOptArg, ExecutionMode=defaultNamedOptArg):
		'Execute javascript file'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1147823703, LCID, 1, (8, 0), ((8, 1), (12, 17), (12, 17)),JavaScriptFile
			, Arguments, ExecutionMode)

	def DoScript(self, Action=defaultNamedNotOptArg, From=defaultNamedNotOptArg, Dialogs=defaultNamedOptArg):
		'Play an action from the Actions Palette'
		return self._oleobj_.InvokeTypes(1685025635, LCID, 1, (24, 0), ((8, 1), (8, 1), (12, 17)),Action
			, From, Dialogs)

	def ExecuteMenuCommand(self, MenuCommandString=defaultNamedNotOptArg):
		'executes a menu command using the menu shortcut string'
		return self._oleobj_.InvokeTypes(1631931715, LCID, 1, (24, 0), ((8, 1),),MenuCommandString
			)

	# Result is of type _Matrix
	def GetIdentityMatrix(self):
		'Returns an identity matrix'
		ret = self._oleobj_.InvokeTypes(1735674189, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetIdentityMatrix', '{95CD20C9-AD72-11D3-B086-0010A4F5C335}')
		return ret

	# Result is of type _PPDFileInfo
	def GetPPDFileInfo(self, Name=defaultNamedNotOptArg):
		'get detailed info from the specified PPD file'
		ret = self._oleobj_.InvokeTypes(1884308564, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPPDFileInfo', '{95CD2C09-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def GetPresetFileOfType(self, PresetType=defaultNamedNotOptArg):
		"given a preset type, returns the full path to the application's default document profile for the type"
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1632063558, LCID, 1, (8, 0), ((3, 1),),PresetType
			)

	# Result is of type _DocumentPreset
	def GetPresetSettings(self, Preset=defaultNamedNotOptArg):
		'given a preset name, tries and retrieves the settings from the preset template'
		ret = self._oleobj_.InvokeTypes(1632063571, LCID, 1, (9, 0), ((8, 1),),Preset
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPresetSettings', '{B1607D7C-2EA8-41B0-977A-F5B0A36DF932}')
		return ret

	# Result is of type _Matrix
	def GetRotationMatrix(self, Angle=defaultNamedOptArg):
		'Returns a rotation transformation matrix'
		ret = self._oleobj_.InvokeTypes(1734693453, LCID, 1, (9, 0), ((12, 17),),Angle
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetRotationMatrix', '{95CD20C9-AD72-11D3-B086-0010A4F5C335}')
		return ret

	# Result is of type _Matrix
	def GetScaleMatrix(self, ScaleX=defaultNamedOptArg, ScaleY=defaultNamedOptArg):
		'Returns a scale transformation matrix'
		ret = self._oleobj_.InvokeTypes(1734693709, LCID, 1, (9, 0), ((12, 17), (12, 17)),ScaleX
			, ScaleY)
		if ret is not None:
			ret = Dispatch(ret, 'GetScaleMatrix', '{95CD20C9-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def GetScriptableHelpGroup(self):
		'Get the scriptable help group object that represents the search widget in the app bar'
		return self._ApplyTypes_(1632847943, 1, (12, 0), (), 'GetScriptableHelpGroup', None,)

	# Result is of type _Matrix
	def GetTranslationMatrix(self, DeltaX=defaultNamedOptArg, DeltaY=defaultNamedOptArg):
		'Returns a translation matrix'
		ret = self._oleobj_.InvokeTypes(1734694989, LCID, 1, (9, 0), ((12, 17), (12, 17)),DeltaX
			, DeltaY)
		if ret is not None:
			ret = Dispatch(ret, 'GetTranslationMatrix', '{95CD20C9-AD72-11D3-B086-0010A4F5C335}')
		return ret

	# Result is of type _Matrix
	def InvertMatrix(self, Matrix=defaultNamedNotOptArg):
		'Invert a matrix'
		ret = self._oleobj_.InvokeTypes(1229870701, LCID, 1, (9, 0), ((9, 1),),Matrix
			)
		if ret is not None:
			ret = Dispatch(ret, 'InvertMatrix', '{95CD20C9-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def IsEqualMatrix(self, Matrix=defaultNamedNotOptArg, SecondMatrix=defaultNamedNotOptArg):
		'Compares two matrices for equality'
		return self._oleobj_.InvokeTypes(1769162061, LCID, 1, (11, 0), ((9, 1), (9, 1)),Matrix
			, SecondMatrix)

	def IsFillActive(self):
		'Checks if fill is active or not'
		return self._oleobj_.InvokeTypes(1799766371, LCID, 1, (11, 0), (),)

	def IsSingularMatrix(self, Matrix=defaultNamedNotOptArg):
		'Tests if a matrix is singular (cannot be inverted)'
		return self._oleobj_.InvokeTypes(1769165645, LCID, 1, (11, 0), ((9, 1),),Matrix
			)

	def IsStrokeActive(self):
		'Checks if stroke is active or not'
		return self._oleobj_.InvokeTypes(1800618339, LCID, 1, (11, 0), (),)

	def IsTouchWorkspace(self):
		'Is In Touch Workspace'
		return self._oleobj_.InvokeTypes(1799967831, LCID, 1, (11, 0), (),)

	def IsUserSharingAppUsageData(self):
		'Is user sharing the application usage data'
		return self._oleobj_.InvokeTypes(1799443780, LCID, 1, (11, 0), (),)

	def LoadAction(self, ActionFilePath=defaultNamedNotOptArg):
		'Load an action into action palette'
		return self._oleobj_.InvokeTypes(1632387398, LCID, 1, (24, 0), ((8, 1),),ActionFilePath
			)

	def LoadColorSettings(self, FileSpec=defaultNamedNotOptArg):
		'load the color settings from the file. If the file is an empty file spec, the color management will be turned off.'
		return self._oleobj_.InvokeTypes(1632387923, LCID, 1, (24, 0), ((8, 1),),FileSpec
			)

	# Result is of type Document
	def Open(self, File=defaultNamedNotOptArg, DocumentColorSpace=defaultNamedOptArg, Options=defaultNamedOptArg):
		'Open the specified document file'
		ret = self._oleobj_.InvokeTypes(1097417551, LCID, 1, (9, 0), ((8, 1), (12, 17), (12, 17)),File
			, DocumentColorSpace, Options)
		if ret is not None:
			ret = Dispatch(ret, 'Open', '{95CD20AB-AD72-11D3-B086-0010A4F5C335}')
		return ret

	# Result is of type Document
	def OpenCloudLibraryAssetForEditing(self, AssetURL=defaultNamedNotOptArg, ThumbnailURL=defaultNamedNotOptArg, AssetType=defaultNamedNotOptArg, Options=defaultNamedOptArg):
		'For Internal Use'
		ret = self._oleobj_.InvokeTypes(1799439716, LCID, 1, (9, 0), ((8, 1), (8, 1), (8, 1), (12, 17)),AssetURL
			, ThumbnailURL, AssetType, Options)
		if ret is not None:
			ret = Dispatch(ret, 'OpenCloudLibraryAssetForEditing', '{95CD20AB-AD72-11D3-B086-0010A4F5C335}')
		return ret

	def Paste(self):
		'Paste clipboard into the current document'
		return self._oleobj_.InvokeTypes(1885434740, LCID, 1, (24, 0), (),)

	def Quit(self):
		'Quit the application'
		return self._oleobj_.InvokeTypes(1903520116, LCID, 1, (24, 0), (),)

	def Redo(self):
		'Redo the last transaction'
		return self._oleobj_.InvokeTypes(1632781636, LCID, 1, (24, 0), (),)

	def Redraw(self):
		'Force Illustrator to redraw its window(s)'
		return self._oleobj_.InvokeTypes(1380271698, LCID, 1, (24, 0), (),)

	def ReflectCSAW(self, OutputFolder=defaultNamedNotOptArg):
		'generate Creative Suite ActionScript Wrappers in specified directory'
		return self._oleobj_.InvokeTypes(1382433111, LCID, 1, (24, 0), ((8, 1),),OutputFolder
			)

	def ResetWorkspace(self):
		'Resets the current workspace'
		return self._oleobj_.InvokeTypes(1799443031, LCID, 1, (11, 0), (),)

	def SaveWorkspace(self, WorkspaceName=defaultNamedNotOptArg):
		'Saves a new workspace'
		return self._oleobj_.InvokeTypes(1799451479, LCID, 1, (11, 0), ((8, 1),),WorkspaceName
			)

	def SendScriptMessage(self, PluginName=defaultNamedNotOptArg, MessageSelector=defaultNamedNotOptArg, InputString=defaultNamedNotOptArg):
		'sends the script message to the required plugin'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1632850765, LCID, 1, (8, 0), ((8, 1), (8, 1), (8, 1)),PluginName
			, MessageSelector, InputString)

	def SetThumbnailOptionsForCloudLibrary(self, Options=defaultNamedNotOptArg):
		'For Internal Use'
		return self._oleobj_.InvokeTypes(1799443535, LCID, 1, (24, 0), ((12, 1),),Options
			)

	def ShowColorPicker(self, Color=defaultNamedNotOptArg):
		"Invokes application's color picker"
		ret = self._oleobj_.InvokeTypes(1799573611, LCID, 1, (9, 0), ((9, 1),),Color
			)
		if ret is not None:
			ret = Dispatch(ret, 'ShowColorPicker', None)
		return ret

	def ShowPresets(self, FileSpec=defaultNamedNotOptArg):
		'get presets from the file'
		return self._ApplyTypes_(1632850003, 1, (12, 0), ((8, 1),), 'ShowPresets', None,FileSpec
			)

	def SwitchWorkspace(self, WorkspaceName=defaultNamedNotOptArg):
		'Switches between workspaces'
		return self._oleobj_.InvokeTypes(1799443287, LCID, 1, (11, 0), ((8, 1),),WorkspaceName
			)

	def TranslatePlaceholderText(self, Text=defaultNamedNotOptArg):
		'translate the placeholder text to regular text. A method to enter unicode points in hex values.'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1416785492, LCID, 1, (8, 0), ((8, 1),),Text
			)

	def Undo(self):
		'Undo the last transaction'
		return self._oleobj_.InvokeTypes(1632980548, LCID, 1, (24, 0), (),)

	def UnloadAction(self, SetName=defaultNamedNotOptArg, ActionName=defaultNamedNotOptArg):
		'unloads an action into action palette'
		return self._oleobj_.InvokeTypes(1632980033, LCID, 1, (24, 0), ((8, 1), (8, 1)),SetName
			, ActionName)

	def executeAATFile(self, File=defaultNamedNotOptArg):
		'executes the active session in the sequencer'
		return self._oleobj_.InvokeTypes(1181500792, LCID, 1, (24, 0), ((8, 1),),File
			)

	_prop_map_get_ = {
		"ActionIsRunning": (1883326834, 2, (11, 0), (), "ActionIsRunning", None),
		# Method 'ActiveDocument' returns object of type 'Document'
		"ActiveDocument": (1634287940, 2, (9, 0), (), "ActiveDocument", '{95CD20AB-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"BrowserAvailable": (2021212737, 2, (11, 0), (), "BrowserAvailable", None),
		"BuildNumber": (1883324738, 2, (8, 0), (), "BuildNumber", None),
		"ColorSettingsList": (1883460428, 2, (12, 0), (), "ColorSettingsList", None),
		"CoordinateSystem": (1883467603, 2, (3, 0), (), "CoordinateSystem", None),
		"DefaultColorSettings": (1632060243, 2, (8, 0), (), "DefaultColorSettings", None),
		# Method 'Documents' returns object of type 'Documents'
		"Documents": (1685021557, 2, (9, 0), (), "Documents", '{95CD20DB-AD72-11D3-B086-0010A4F5C335}'),
		"FlattenerPresetsList": (1883657036, 2, (12, 0), (), "FlattenerPresetsList", None),
		"FreeMemory": (1634289229, 2, (3, 0), (), "FreeMemory", None),
		"Locale": (1883324748, 2, (8, 0), (), "Locale", None),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"PDFPresetsList": (1883525964, 2, (12, 0), (), "PDFPresetsList", None),
		"PPDFileList": (1884308556, 2, (12, 0), (), "PPDFileList", None),
		"PasteRemembersLayers": (1884448076, 2, (11, 0), (), "PasteRemembersLayers", None),
		"Path": (1883664464, 2, (8, 0), (), "Path", None),
		# Method 'Preferences' returns object of type 'Preferences'
		"Preferences": (1884320358, 2, (9, 0), (), "Preferences", '{4C78DFCC-7A09-11D4-81A0-00C04F60ECCC}'),
		"PrintPresetsList": (1884312396, 2, (12, 0), (), "PrintPresetsList", None),
		"PrinterList": (1884312140, 2, (12, 0), (), "PrinterList", None),
		"ScriptingVersion": (1883331190, 2, (8, 0), (), "ScriptingVersion", None),
		"Selection": (1936026725, 2, (12, 0), (), "Selection", None),
		"StartupPresetsList": (1884508236, 2, (12, 0), (), "StartupPresetsList", None),
		# Method 'TextFonts' returns object of type 'TextFonts'
		"TextFonts": (1666472038, 2, (9, 0), (), "TextFonts", '{95CD20EA-AD72-11D3-B086-0010A4F5C335}'),
		"TracingPresetsList": (1884574540, 2, (12, 0), (), "TracingPresetsList", None),
		"UserAdobeID": (1883326788, 2, (8, 0), (), "UserAdobeID", None),
		"UserGUID": (1883720004, 2, (8, 0), (), "UserGUID", None),
		"UserInteractionLevel": (1883460937, 2, (3, 0), (), "UserInteractionLevel", None),
		"Version": (1986359923, 2, (8, 0), (), "Version", None),
		"Visible": (1886808435, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"ActiveDocument": ((1634287940, LCID, 4, 0),()),
		"CoordinateSystem": ((1883467603, LCID, 4, 0),()),
		"PasteRemembersLayers": ((1884448076, LCID, 4, 0),()),
		"Selection": ((1936026725, LCID, 4, 0),()),
		"UserInteractionLevel": ((1883460937, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _CMYKColor(DispatchBaseClass):
	'A CMYK color specification'
	CLSID = IID('{95CD20B2-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{9AFB43D8-2ABA-4DE9-A3E1-617AAA863C22}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Black": (1112293707, 2, (5, 0), (), "Black", None),
		"Cyan": (1129922894, 2, (5, 0), (), "Cyan", None),
		"Magenta": (1296123726, 2, (5, 0), (), "Magenta", None),
		"Yellow": (1497713740, 2, (5, 0), (), "Yellow", None),
	}
	_prop_map_put_ = {
		"Black": ((1112293707, LCID, 4, 0),()),
		"Cyan": ((1129922894, LCID, 4, 0),()),
		"Magenta": ((1296123726, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Yellow": ((1497713740, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _Dimensions(DispatchBaseClass):
	'Dimensions (height and width)'
	CLSID = IID('{95CD20B1-AD72-11D3-B086-0010A7F5C335}')
	coclass_clsid = IID('{40A7C4A8-EFD2-43A8-806F-5B0CCE61DCE6}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Height": (1145595241, 2, (5, 0), (), "Height", None),
		"Width": (1146578024, 2, (5, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"Height": ((1145595241, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Width": ((1146578024, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _DocumentPreset(DispatchBaseClass):
	'the new document preset to use for creating a new document'
	CLSID = IID('{B1607D7C-2EA8-41B0-977A-F5B0A36DF932}')
	coclass_clsid = IID('{E2D4A432-9E16-41E6-BCA5-062890269CD1}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtboardLayout": (1883327609, 2, (3, 0), (), "ArtboardLayout", None),
		"ArtboardRowsOrCols": (1883329091, 2, (3, 0), (), "ArtboardRowsOrCols", None),
		"ArtboardSpacing": (1883329392, 2, (5, 0), (), "ArtboardSpacing", None),
		"DocumentBleedLink": (1883521612, 2, (11, 0), (), "DocumentBleedLink", None),
		"DocumentBleedOffsetRect": (1883521615, 2, (12, 0), (), "DocumentBleedOffsetRect", None),
		"DocumentColorSpace": (1883521869, 2, (3, 0), (), "DocumentColorSpace", None),
		"DocumentPreviewMode": (1883525202, 2, (3, 0), (), "DocumentPreviewMode", None),
		"DocumentRasterResolution": (1883525714, 2, (3, 0), (), "DocumentRasterResolution", None),
		"DocumentTitle": (1884571988, 2, (8, 0), (), "DocumentTitle", None),
		"DocumentTransparencyGrid": (1883526215, 2, (3, 0), (), "DocumentTransparencyGrid", None),
		"DocumentUnits": (2021147733, 2, (3, 0), (), "DocumentUnits", None),
		"Height": (1884506216, 2, (5, 0), (), "Height", None),
		"NumArtboards": (1884176754, 2, (3, 0), (), "NumArtboards", None),
		"Width": (1884506231, 2, (5, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"ArtboardLayout": ((1883327609, LCID, 4, 0),()),
		"ArtboardRowsOrCols": ((1883329091, LCID, 4, 0),()),
		"ArtboardSpacing": ((1883329392, LCID, 4, 0),()),
		"DocumentBleedLink": ((1883521612, LCID, 4, 0),()),
		"DocumentBleedOffsetRect": ((1883521615, LCID, 4, 0),()),
		"DocumentColorSpace": ((1883521869, LCID, 4, 0),()),
		"DocumentPreviewMode": ((1883525202, LCID, 4, 0),()),
		"DocumentRasterResolution": ((1883525714, LCID, 4, 0),()),
		"DocumentTitle": ((1884571988, LCID, 4, 0),()),
		"DocumentTransparencyGrid": ((1883526215, LCID, 4, 0),()),
		"DocumentUnits": ((2021147733, LCID, 4, 0),()),
		"Height": ((1884506216, LCID, 4, 0),()),
		"NumArtboards": ((1884176754, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Width": ((1884506231, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _EPSSaveOptions(DispatchBaseClass):
	'Options which may be supplied when saving a document as an Illustrator EPS file'
	CLSID = IID('{95CD20A7-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{F07FD4A3-5651-47DA-AC33-91BC06403816}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtboardRange": (1884304483, 2, (8, 0), (), "ArtboardRange", None),
		"CMYKPostScript": (1883459667, 2, (11, 0), (), "CMYKPostScript", None),
		"Compatibility": (1883849584, 2, (3, 0), (), "Compatibility", None),
		"CompatibleGradientPrinting": (1883457360, 2, (11, 0), (), "CompatibleGradientPrinting", None),
		"EmbedAllFonts": (1883586886, 2, (11, 0), (), "EmbedAllFonts", None),
		"EmbedLinkedFiles": (1883861065, 2, (11, 0), (), "EmbedLinkedFiles", None),
		"FlattenOutput": (1884243564, 2, (3, 0), (), "FlattenOutput", None),
		"IncludeDocumentThumbnails": (1883849588, 2, (11, 0), (), "IncludeDocumentThumbnails", None),
		"JapaneseFileFormat": (1883924070, 2, (11, 0), (), "JapaneseFileFormat", None),
		"Overprint": (1883131728, 2, (3, 0), (), "Overprint", None),
		"PostScript": (1884312428, 2, (3, 0), (), "PostScript", None),
		"Preview": (1634291798, 2, (3, 0), (), "Preview", None),
		"SaveMultipleArtboards": (1397571938, 2, (11, 0), (), "SaveMultipleArtboards", None),
	}
	_prop_map_put_ = {
		"ArtboardRange": ((1884304483, LCID, 4, 0),()),
		"CMYKPostScript": ((1883459667, LCID, 4, 0),()),
		"Compatibility": ((1883849584, LCID, 4, 0),()),
		"CompatibleGradientPrinting": ((1883457360, LCID, 4, 0),()),
		"EmbedAllFonts": ((1883586886, LCID, 4, 0),()),
		"EmbedLinkedFiles": ((1883861065, LCID, 4, 0),()),
		"FlattenOutput": ((1884243564, LCID, 4, 0),()),
		"IncludeDocumentThumbnails": ((1883849588, LCID, 4, 0),()),
		"JapaneseFileFormat": ((1883924070, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Overprint": ((1883131728, LCID, 4, 0),()),
		"PostScript": ((1884312428, LCID, 4, 0),()),
		"Preview": ((1634291798, LCID, 4, 0),()),
		"SaveMultipleArtboards": ((1397571938, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _ExportOptionsAutoCAD(DispatchBaseClass):
	'Options which may be supplied when exporting a document to AutoCAD formats (.dwg or .dxf)'
	CLSID = IID('{AD25A97A-80BC-4D6A-9E61-7E288DE977CA}')
	coclass_clsid = IID('{D678C828-971A-4759-8A5D-3FF12C221A22}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		"AlterPathsForAppearance": (1883324752, 2, (11, 0), (), "AlterPathsForAppearance", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Colors": (1883325260, 2, (3, 0), (), "Colors", None),
		"ConvertTextToOutlines": (1884319284, 2, (11, 0), (), "ConvertTextToOutlines", None),
		"ExportFileFormat": (1883326022, 2, (3, 0), (), "ExportFileFormat", None),
		"ExportOption": (1883325775, 2, (3, 0), (), "ExportOption", None),
		"ExportSelectedArtOnly": (1883329345, 2, (11, 0), (), "ExportSelectedArtOnly", None),
		"RasterFormat": (1883329094, 2, (3, 0), (), "RasterFormat", None),
		"ScaleLineweights": (1883327575, 2, (11, 0), (), "ScaleLineweights", None),
		"Unit": (1883329365, 2, (3, 0), (), "Unit", None),
		"UnitScaleRatio": (1883329362, 2, (5, 0), (), "UnitScaleRatio", None),
		"Version": (1883330131, 2, (3, 0), (), "Version", None),
	}
	_prop_map_put_ = {
		"AlterPathsForAppearance": ((1883324752, LCID, 4, 0),()),
		"Colors": ((1883325260, LCID, 4, 0),()),
		"ConvertTextToOutlines": ((1884319284, LCID, 4, 0),()),
		"ExportFileFormat": ((1883326022, LCID, 4, 0),()),
		"ExportOption": ((1883325775, LCID, 4, 0),()),
		"ExportSelectedArtOnly": ((1883329345, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"RasterFormat": ((1883329094, LCID, 4, 0),()),
		"ScaleLineweights": ((1883327575, LCID, 4, 0),()),
		"Unit": ((1883329365, LCID, 4, 0),()),
		"UnitScaleRatio": ((1883329362, LCID, 4, 0),()),
		"Version": ((1883330131, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _ExportOptionsFlash(DispatchBaseClass):
	'Options which may be supplied when exporting a document as an Flash (.SWF) file'
	CLSID = IID('{4C78DF9F-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = IID('{09534ADA-D2A2-45EB-BD90-8E4D391D306B}')

	def SetBackgroundColor(self, arg0=defaultUnnamedArg):
		'the background color'
		return self._oleobj_.InvokeTypes(1883652675, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtClipping": (1883652419, 2, (3, 0), (), "ArtClipping", None),
		"ArtboardRange": (1884304483, 2, (8, 0), (), "ArtboardRange", None),
		# Method 'BackgroundColor' returns object of type '_RGBColor'
		"BackgroundColor": (1883652675, 2, (9, 0), (), "BackgroundColor", '{95CD20B1-AD72-11D3-B086-0010A4F5C335}'),
		"BackgroundLayers": (1883652684, 2, (12, 0), (), "BackgroundLayers", None),
		"BlendAnimation": (1883652673, 2, (3, 0), (), "BlendAnimation", None),
		"Compressed": (1883456611, 2, (11, 0), (), "Compressed", None),
		"ConvertTextToOutlines": (1884319284, 2, (11, 0), (), "ConvertTextToOutlines", None),
		"CurveQuality": (1883652945, 2, (3, 0), (), "CurveQuality", None),
		"ExportAllSymbols": (1883652435, 2, (11, 0), (), "ExportAllSymbols", None),
		"ExportStyle": (1883658323, 2, (3, 0), (), "ExportStyle", None),
		"ExportVersion": (1883658326, 2, (3, 0), (), "ExportVersion", None),
		"FlattenOutput": (1884243564, 2, (3, 0), (), "FlattenOutput", None),
		"FrameRate": (1883653714, 2, (5, 0), (), "FrameRate", None),
		"GenerateHTML": (1883653960, 2, (11, 0), (), "GenerateHTML", None),
		"IgnoreTextKerning": (1883654484, 2, (11, 0), (), "IgnoreTextKerning", None),
		"ImageFormat": (1883654470, 2, (3, 0), (), "ImageFormat", None),
		"IncludeMetadata": (1883852100, 2, (11, 0), (), "IncludeMetadata", None),
		"JPEGMethod": (1883654733, 2, (3, 0), (), "JPEGMethod", None),
		"JPEGQuality": (1883654737, 2, (3, 0), (), "JPEGQuality", None),
		"LayerOrder": (1883655247, 2, (3, 0), (), "LayerOrder", None),
		"Looping": (1883655279, 2, (11, 0), (), "Looping", None),
		"PlaybackAccess": (1883656275, 2, (3, 0), (), "PlaybackAccess", None),
		"PreserveAppearance": (1697919537, 2, (11, 0), (), "PreserveAppearance", None),
		"ReadOnly": (1883656783, 2, (11, 0), (), "ReadOnly", None),
		"Replacing": (1884450924, 2, (3, 0), (), "Replacing", None),
		"Resolution": (1634292314, 2, (5, 0), (), "Resolution", None),
		"SaveMultipleArtboards": (1397571938, 2, (11, 0), (), "SaveMultipleArtboards", None),
	}
	_prop_map_put_ = {
		"ArtClipping": ((1883652419, LCID, 4, 0),()),
		"ArtboardRange": ((1884304483, LCID, 4, 0),()),
		"BackgroundColor": ((1883652675, LCID, 4, 0),()),
		"BackgroundLayers": ((1883652684, LCID, 4, 0),()),
		"BlendAnimation": ((1883652673, LCID, 4, 0),()),
		"Compressed": ((1883456611, LCID, 4, 0),()),
		"ConvertTextToOutlines": ((1884319284, LCID, 4, 0),()),
		"CurveQuality": ((1883652945, LCID, 4, 0),()),
		"ExportAllSymbols": ((1883652435, LCID, 4, 0),()),
		"ExportStyle": ((1883658323, LCID, 4, 0),()),
		"ExportVersion": ((1883658326, LCID, 4, 0),()),
		"FlattenOutput": ((1884243564, LCID, 4, 0),()),
		"FrameRate": ((1883653714, LCID, 4, 0),()),
		"GenerateHTML": ((1883653960, LCID, 4, 0),()),
		"IgnoreTextKerning": ((1883654484, LCID, 4, 0),()),
		"ImageFormat": ((1883654470, LCID, 4, 0),()),
		"IncludeMetadata": ((1883852100, LCID, 4, 0),()),
		"JPEGMethod": ((1883654733, LCID, 4, 0),()),
		"JPEGQuality": ((1883654737, LCID, 4, 0),()),
		"LayerOrder": ((1883655247, LCID, 4, 0),()),
		"Looping": ((1883655279, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"PlaybackAccess": ((1883656275, LCID, 4, 0),()),
		"PreserveAppearance": ((1697919537, LCID, 4, 0),()),
		"ReadOnly": ((1883656783, LCID, 4, 0),()),
		"Replacing": ((1884450924, LCID, 4, 0),()),
		"Resolution": ((1634292314, LCID, 4, 0),()),
		"SaveMultipleArtboards": ((1397571938, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _ExportOptionsGIF(DispatchBaseClass):
	'Options which may be supplied when exporting a document as a GIF file'
	CLSID = IID('{95CD20CD-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{46E4F107-315D-4BDF-BE66-4E33D9596A9A}')

	def SetMatteColor(self, arg0=defaultUnnamedArg):
		'the color to use when matting the artboard (default: white)'
		return self._oleobj_.InvokeTypes(1884111724, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		"AntiAliasing": (1883336257, 2, (11, 0), (), "AntiAliasing", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtBoardClipping": (1883324995, 2, (11, 0), (), "ArtBoardClipping", None),
		"ColorCount": (1883466819, 2, (3, 0), (), "ColorCount", None),
		"ColorDither": (1883456628, 2, (3, 0), (), "ColorDither", None),
		"ColorReduction": (1883460196, 2, (3, 0), (), "ColorReduction", None),
		"DitherPercent": (1883525219, 2, (3, 0), (), "DitherPercent", None),
		"HorizontalScale": (1883798099, 2, (5, 0), (), "HorizontalScale", None),
		"InfoLossPercent": (1883851856, 2, (3, 0), (), "InfoLossPercent", None),
		"Interlaced": (1883860556, 2, (11, 0), (), "Interlaced", None),
		"Matte": (1884111170, 2, (11, 0), (), "Matte", None),
		# Method 'MatteColor' returns object of type '_RGBColor'
		"MatteColor": (1884111724, 2, (9, 0), (), "MatteColor", '{95CD20B1-AD72-11D3-B086-0010A4F5C335}'),
		"SaveAsHTML": (1884506196, 2, (11, 0), (), "SaveAsHTML", None),
		"Transparency": (1884581987, 2, (11, 0), (), "Transparency", None),
		"VerticalScale": (1884714067, 2, (5, 0), (), "VerticalScale", None),
		"WebSnap": (1884770403, 2, (3, 0), (), "WebSnap", None),
	}
	_prop_map_put_ = {
		"AntiAliasing": ((1883336257, LCID, 4, 0),()),
		"ArtBoardClipping": ((1883324995, LCID, 4, 0),()),
		"ColorCount": ((1883466819, LCID, 4, 0),()),
		"ColorDither": ((1883456628, LCID, 4, 0),()),
		"ColorReduction": ((1883460196, LCID, 4, 0),()),
		"DitherPercent": ((1883525219, LCID, 4, 0),()),
		"HorizontalScale": ((1883798099, LCID, 4, 0),()),
		"InfoLossPercent": ((1883851856, LCID, 4, 0),()),
		"Interlaced": ((1883860556, LCID, 4, 0),()),
		"Matte": ((1884111170, LCID, 4, 0),()),
		"MatteColor": ((1884111724, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"SaveAsHTML": ((1884506196, LCID, 4, 0),()),
		"Transparency": ((1884581987, LCID, 4, 0),()),
		"VerticalScale": ((1884714067, LCID, 4, 0),()),
		"WebSnap": ((1884770403, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _ExportOptionsJPEG(DispatchBaseClass):
	'Options which may be supplied when exporting a document as a JPEG file'
	CLSID = IID('{95CD20CA-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{4C1581E0-3BA8-4CE6-83FC-34EF5F2A9F40}')

	def SetMatteColor(self, arg0=defaultUnnamedArg):
		'the color to use when matting the artboard (default: white)'
		return self._oleobj_.InvokeTypes(1884111724, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		"AntiAliasing": (1883336257, 2, (11, 0), (), "AntiAliasing", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtBoardClipping": (1883324995, 2, (11, 0), (), "ArtBoardClipping", None),
		"BlurAmount": (1883401281, 2, (5, 0), (), "BlurAmount", None),
		"HorizontalScale": (1883798099, 2, (5, 0), (), "HorizontalScale", None),
		"Matte": (1884111170, 2, (11, 0), (), "Matte", None),
		# Method 'MatteColor' returns object of type '_RGBColor'
		"MatteColor": (1884111724, 2, (9, 0), (), "MatteColor", '{95CD20B1-AD72-11D3-B086-0010A4F5C335}'),
		"Optimization": (1884254317, 2, (11, 0), (), "Optimization", None),
		"QualitySetting": (1883860305, 2, (3, 0), (), "QualitySetting", None),
		"SaveAsHTML": (1884506196, 2, (11, 0), (), "SaveAsHTML", None),
		"VerticalScale": (1884714067, 2, (5, 0), (), "VerticalScale", None),
	}
	_prop_map_put_ = {
		"AntiAliasing": ((1883336257, LCID, 4, 0),()),
		"ArtBoardClipping": ((1883324995, LCID, 4, 0),()),
		"BlurAmount": ((1883401281, LCID, 4, 0),()),
		"HorizontalScale": ((1883798099, LCID, 4, 0),()),
		"Matte": ((1884111170, LCID, 4, 0),()),
		"MatteColor": ((1884111724, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Optimization": ((1884254317, LCID, 4, 0),()),
		"QualitySetting": ((1883860305, LCID, 4, 0),()),
		"SaveAsHTML": ((1884506196, LCID, 4, 0),()),
		"VerticalScale": ((1884714067, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _ExportOptionsPNG24(DispatchBaseClass):
	'Options which may be supplied when exporting a document as an 24 bit PNG file'
	CLSID = IID('{95CD20CC-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{668E6292-D51A-4628-9800-4817A6762DF3}')

	def SetDimensions(self, arg0=defaultUnnamedArg):
		'Dimensions in which to contain the resulting raster'
		return self._oleobj_.InvokeTypes(1883524430, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetMatteColor(self, arg0=defaultUnnamedArg):
		'the color to use when matting the artboard (default: white)'
		return self._oleobj_.InvokeTypes(1884111724, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		"AntiAliasing": (1883336257, 2, (11, 0), (), "AntiAliasing", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtBoardClipping": (1883324995, 2, (11, 0), (), "ArtBoardClipping", None),
		# Method 'Dimensions' returns object of type '_Dimensions'
		"Dimensions": (1883524430, 2, (9, 0), (), "Dimensions", '{95CD20B1-AD72-11D3-B086-0010A7F5C335}'),
		"HorizontalScale": (1883798099, 2, (5, 0), (), "HorizontalScale", None),
		"Matte": (1884111170, 2, (11, 0), (), "Matte", None),
		# Method 'MatteColor' returns object of type '_RGBColor'
		"MatteColor": (1884111724, 2, (9, 0), (), "MatteColor", '{95CD20B1-AD72-11D3-B086-0010A4F5C335}'),
		"SaveAsHTML": (1884506196, 2, (11, 0), (), "SaveAsHTML", None),
		"Transparency": (1884581987, 2, (11, 0), (), "Transparency", None),
		"VerticalScale": (1884714067, 2, (5, 0), (), "VerticalScale", None),
	}
	_prop_map_put_ = {
		"AntiAliasing": ((1883336257, LCID, 4, 0),()),
		"ArtBoardClipping": ((1883324995, LCID, 4, 0),()),
		"Dimensions": ((1883524430, LCID, 4, 0),()),
		"HorizontalScale": ((1883798099, LCID, 4, 0),()),
		"Matte": ((1884111170, LCID, 4, 0),()),
		"MatteColor": ((1884111724, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"SaveAsHTML": ((1884506196, LCID, 4, 0),()),
		"Transparency": ((1884581987, LCID, 4, 0),()),
		"VerticalScale": ((1884714067, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _ExportOptionsPNG8(DispatchBaseClass):
	'Options which may be supplied when exporting a document as an 8 bit PNG file'
	CLSID = IID('{95CD20CB-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{ECF0C759-F01B-4B3B-8922-541C1C163DF3}')

	def SetMatteColor(self, arg0=defaultUnnamedArg):
		'the color to use when matting the artboard (default: white)'
		return self._oleobj_.InvokeTypes(1884111724, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		"AntiAliasing": (1883336257, 2, (11, 0), (), "AntiAliasing", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtBoardClipping": (1883324995, 2, (11, 0), (), "ArtBoardClipping", None),
		"ColorCount": (1883466819, 2, (3, 0), (), "ColorCount", None),
		"ColorDither": (1883456628, 2, (3, 0), (), "ColorDither", None),
		"ColorReduction": (1883460196, 2, (3, 0), (), "ColorReduction", None),
		"DitherPercent": (1883525219, 2, (3, 0), (), "DitherPercent", None),
		"HorizontalScale": (1883798099, 2, (5, 0), (), "HorizontalScale", None),
		"Interlaced": (1883860556, 2, (11, 0), (), "Interlaced", None),
		"Matte": (1884111170, 2, (11, 0), (), "Matte", None),
		# Method 'MatteColor' returns object of type '_RGBColor'
		"MatteColor": (1884111724, 2, (9, 0), (), "MatteColor", '{95CD20B1-AD72-11D3-B086-0010A4F5C335}'),
		"SaveAsHTML": (1884506196, 2, (11, 0), (), "SaveAsHTML", None),
		"Transparency": (1884581987, 2, (11, 0), (), "Transparency", None),
		"VerticalScale": (1884714067, 2, (5, 0), (), "VerticalScale", None),
		"WebSnap": (1884770403, 2, (3, 0), (), "WebSnap", None),
	}
	_prop_map_put_ = {
		"AntiAliasing": ((1883336257, LCID, 4, 0),()),
		"ArtBoardClipping": ((1883324995, LCID, 4, 0),()),
		"ColorCount": ((1883466819, LCID, 4, 0),()),
		"ColorDither": ((1883456628, LCID, 4, 0),()),
		"ColorReduction": ((1883460196, LCID, 4, 0),()),
		"DitherPercent": ((1883525219, LCID, 4, 0),()),
		"HorizontalScale": ((1883798099, LCID, 4, 0),()),
		"Interlaced": ((1883860556, LCID, 4, 0),()),
		"Matte": ((1884111170, LCID, 4, 0),()),
		"MatteColor": ((1884111724, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"SaveAsHTML": ((1884506196, LCID, 4, 0),()),
		"Transparency": ((1884581987, LCID, 4, 0),()),
		"VerticalScale": ((1884714067, LCID, 4, 0),()),
		"WebSnap": ((1884770403, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _ExportOptionsPhotoshop(DispatchBaseClass):
	'Options which may be supplied when exporting a document as a Photoshop file'
	CLSID = IID('{A07B43A9-0201-4369-A1B5-8A33C8A0BB23}')
	coclass_clsid = IID('{1CC2A29F-5B2C-4359-9728-0D1771BDE2B1}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		"AntiAliasing": (1883336257, 2, (11, 0), (), "AntiAliasing", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtboardRange": (1884304483, 2, (8, 0), (), "ArtboardRange", None),
		"Compatibility": (1883849584, 2, (3, 0), (), "Compatibility", None),
		"CompoundShapes": (1883587411, 2, (11, 0), (), "CompoundShapes", None),
		"EditableText": (1883591800, 2, (11, 0), (), "EditableText", None),
		"EmbedICCProfile": (1883590758, 2, (11, 0), (), "EmbedICCProfile", None),
		"HiddenLayers": (1883792460, 2, (11, 0), (), "HiddenLayers", None),
		"ImageColorSpace": (1667318611, 2, (3, 0), (), "ImageColorSpace", None),
		"ImageMap": (1883588941, 2, (11, 0), (), "ImageMap", None),
		"MaximumEditability": (1884112225, 2, (11, 0), (), "MaximumEditability", None),
		"NestedLayers": (1884179577, 2, (11, 0), (), "NestedLayers", None),
		"Resolution": (1634292314, 2, (5, 0), (), "Resolution", None),
		"SaveMultipleArtboards": (1397571938, 2, (11, 0), (), "SaveMultipleArtboards", None),
		"Slices": (1883591532, 2, (11, 0), (), "Slices", None),
		"Warnings": (1883592562, 2, (11, 0), (), "Warnings", None),
		"WriteLayers": (1884779084, 2, (11, 0), (), "WriteLayers", None),
	}
	_prop_map_put_ = {
		"AntiAliasing": ((1883336257, LCID, 4, 0),()),
		"ArtboardRange": ((1884304483, LCID, 4, 0),()),
		"Compatibility": ((1883849584, LCID, 4, 0),()),
		"CompoundShapes": ((1883587411, LCID, 4, 0),()),
		"EditableText": ((1883591800, LCID, 4, 0),()),
		"EmbedICCProfile": ((1883590758, LCID, 4, 0),()),
		"HiddenLayers": ((1883792460, LCID, 4, 0),()),
		"ImageColorSpace": ((1667318611, LCID, 4, 0),()),
		"ImageMap": ((1883588941, LCID, 4, 0),()),
		"MaximumEditability": ((1884112225, LCID, 4, 0),()),
		"NestedLayers": ((1884179577, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Resolution": ((1634292314, LCID, 4, 0),()),
		"SaveMultipleArtboards": ((1397571938, LCID, 4, 0),()),
		"Slices": ((1883591532, LCID, 4, 0),()),
		"Warnings": ((1883592562, LCID, 4, 0),()),
		"WriteLayers": ((1884779084, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _ExportOptionsSVG(DispatchBaseClass):
	'Options which may be supplied when exporting a document as an SVG file'
	CLSID = IID('{95CD20CF-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{8930E841-DD0D-47EB-ACB1-8A37AFDD5A2A}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtboardRange": (1884304483, 2, (8, 0), (), "ArtboardRange", None),
		"CSSProperties": (1883460435, 2, (3, 0), (), "CSSProperties", None),
		"Compressed": (1883456611, 2, (11, 0), (), "Compressed", None),
		"CoordinatePrecision": (1883530064, 2, (3, 0), (), "CoordinatePrecision", None),
		"DTD": (1883526212, 2, (3, 0), (), "DTD", None),
		"DocumentEncoding": (1883522403, 2, (3, 0), (), "DocumentEncoding", None),
		"EmbedRasterImages": (1884440140, 2, (11, 0), (), "EmbedRasterImages", None),
		"FontSubsetting": (1883657075, 2, (3, 0), (), "FontSubsetting", None),
		"FontType": (1883657305, 2, (3, 0), (), "FontType", None),
		"IncludeFileInfo": (1883851853, 2, (11, 0), (), "IncludeFileInfo", None),
		"IncludeUnusedStyles": (1883854151, 2, (11, 0), (), "IncludeUnusedStyles", None),
		"IncludeVariablesAndDatasets": (1883854404, 2, (11, 0), (), "IncludeVariablesAndDatasets", None),
		"OptimizeForSVGViewer": (1883849038, 2, (11, 0), (), "OptimizeForSVGViewer", None),
		"PreserveEditability": (1883131973, 2, (11, 0), (), "PreserveEditability", None),
		"SVGAutoKerning": (1883329611, 2, (11, 0), (), "SVGAutoKerning", None),
		"SVGTextOnPath": (1884573520, 2, (11, 0), (), "SVGTextOnPath", None),
		"SaveMultipleArtboards": (1397571938, 2, (11, 0), (), "SaveMultipleArtboards", None),
		"Slices": (1883591532, 2, (11, 0), (), "Slices", None),
	}
	_prop_map_put_ = {
		"ArtboardRange": ((1884304483, LCID, 4, 0),()),
		"CSSProperties": ((1883460435, LCID, 4, 0),()),
		"Compressed": ((1883456611, LCID, 4, 0),()),
		"CoordinatePrecision": ((1883530064, LCID, 4, 0),()),
		"DTD": ((1883526212, LCID, 4, 0),()),
		"DocumentEncoding": ((1883522403, LCID, 4, 0),()),
		"EmbedRasterImages": ((1884440140, LCID, 4, 0),()),
		"FontSubsetting": ((1883657075, LCID, 4, 0),()),
		"FontType": ((1883657305, LCID, 4, 0),()),
		"IncludeFileInfo": ((1883851853, LCID, 4, 0),()),
		"IncludeUnusedStyles": ((1883854151, LCID, 4, 0),()),
		"IncludeVariablesAndDatasets": ((1883854404, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"OptimizeForSVGViewer": ((1883849038, LCID, 4, 0),()),
		"PreserveEditability": ((1883131973, LCID, 4, 0),()),
		"SVGAutoKerning": ((1883329611, LCID, 4, 0),()),
		"SVGTextOnPath": ((1884573520, LCID, 4, 0),()),
		"SaveMultipleArtboards": ((1397571938, LCID, 4, 0),()),
		"Slices": ((1883591532, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _ExportOptionsTIFF(DispatchBaseClass):
	'Options which may be supplied when exporting a document as a TIFF file'
	CLSID = IID('{2A8F3C5F-B4E3-45BB-89CB-93F062B4F9F1}')
	coclass_clsid = IID('{A07D1206-AB5A-4BB1-9207-AEBA31A2D652}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		"AntiAliasing": (1951678785, 2, (3, 0), (), "AntiAliasing", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtboardRange": (1884304483, 2, (8, 0), (), "ArtboardRange", None),
		"ByteOrder": (1951679055, 2, (3, 0), (), "ByteOrder", None),
		"EmbedICCProfile": (1883590758, 2, (11, 0), (), "EmbedICCProfile", None),
		"ImageColorSpace": (1667318611, 2, (3, 0), (), "ImageColorSpace", None),
		"LZWCompression": (1951160899, 2, (11, 0), (), "LZWCompression", None),
		"Resolution": (1634292314, 2, (5, 0), (), "Resolution", None),
		"SaveMultipleArtboards": (1397571938, 2, (11, 0), (), "SaveMultipleArtboards", None),
	}
	_prop_map_put_ = {
		"AntiAliasing": ((1951678785, LCID, 4, 0),()),
		"ArtboardRange": ((1884304483, LCID, 4, 0),()),
		"ByteOrder": ((1951679055, LCID, 4, 0),()),
		"EmbedICCProfile": ((1883590758, LCID, 4, 0),()),
		"ImageColorSpace": ((1667318611, LCID, 4, 0),()),
		"LZWCompression": ((1951160899, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Resolution": ((1634292314, LCID, 4, 0),()),
		"SaveMultipleArtboards": ((1397571938, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _ExportOptionsWebOptimizedSVG(DispatchBaseClass):
	'Options which may be supplied when exporting a document as a Web optimized SVG file'
	CLSID = IID('{4C78DF9F-7A09-11D4-81A0-00C04F60ECCE}')
	coclass_clsid = IID('{FCB10B56-8002-46AE-A70D-D02783FFA353}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtboardRange": (1884304483, 2, (8, 0), (), "ArtboardRange", None),
		"CSSProperties": (1883460435, 2, (3, 0), (), "CSSProperties", None),
		"CoordinatePrecision": (1883530064, 2, (3, 0), (), "CoordinatePrecision", None),
		"FontType": (1883657305, 2, (3, 0), (), "FontType", None),
		"RasterImageLocation": (1884440919, 2, (3, 0), (), "RasterImageLocation", None),
		"SVGId": (1883849812, 2, (3, 0), (), "SVGId", None),
		"SVGMinify": (1883329357, 2, (11, 0), (), "SVGMinify", None),
		"SVGResponsive": (1883853395, 2, (11, 0), (), "SVGResponsive", None),
		"SaveMultipleArtboards": (1397571938, 2, (11, 0), (), "SaveMultipleArtboards", None),
	}
	_prop_map_put_ = {
		"ArtboardRange": ((1884304483, LCID, 4, 0),()),
		"CSSProperties": ((1883460435, LCID, 4, 0),()),
		"CoordinatePrecision": ((1883530064, LCID, 4, 0),()),
		"FontType": ((1883657305, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"RasterImageLocation": ((1884440919, LCID, 4, 0),()),
		"SVGId": ((1883849812, LCID, 4, 0),()),
		"SVGMinify": ((1883329357, LCID, 4, 0),()),
		"SVGResponsive": ((1883853395, LCID, 4, 0),()),
		"SaveMultipleArtboards": ((1397571938, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _FXGSaveOptions(DispatchBaseClass):
	'Options which may be supplied when saving a document as an FXG file'
	CLSID = IID('{500C9AF9-AA54-4941-B544-132E4D285938}')
	coclass_clsid = IID('{8DA7F9C4-7E22-46BD-BA1D-5517A9F0CD18}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtboardRange": (1884304483, 2, (8, 0), (), "ArtboardRange", None),
		"BlendsPolicy": (1883660880, 2, (3, 0), (), "BlendsPolicy", None),
		"DownsampleLinkedImages": (1883658092, 2, (11, 0), (), "DownsampleLinkedImages", None),
		"FiltersPolicy": (1883661904, 2, (3, 0), (), "FiltersPolicy", None),
		"GradientsPolicy": (1883662160, 2, (3, 0), (), "GradientsPolicy", None),
		"IncludeMetadata": (1883658349, 2, (11, 0), (), "IncludeMetadata", None),
		"IncludeUnusedSymbols": (1883654517, 2, (11, 0), (), "IncludeUnusedSymbols", None),
		"PreserveEditingCapabilities": (1883656293, 2, (11, 0), (), "PreserveEditingCapabilities", None),
		"SaveMultipleArtboards": (1397571938, 2, (11, 0), (), "SaveMultipleArtboards", None),
		"TextPolicy": (1883665488, 2, (3, 0), (), "TextPolicy", None),
		"Version": (1883652982, 2, (3, 0), (), "Version", None),
	}
	_prop_map_put_ = {
		"ArtboardRange": ((1884304483, LCID, 4, 0),()),
		"BlendsPolicy": ((1883660880, LCID, 4, 0),()),
		"DownsampleLinkedImages": ((1883658092, LCID, 4, 0),()),
		"FiltersPolicy": ((1883661904, LCID, 4, 0),()),
		"GradientsPolicy": ((1883662160, LCID, 4, 0),()),
		"IncludeMetadata": ((1883658349, LCID, 4, 0),()),
		"IncludeUnusedSymbols": ((1883654517, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"PreserveEditingCapabilities": ((1883656293, LCID, 4, 0),()),
		"SaveMultipleArtboards": ((1397571938, LCID, 4, 0),()),
		"TextPolicy": ((1883665488, LCID, 4, 0),()),
		"Version": ((1883652982, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _GradientColor(DispatchBaseClass):
	'A Gradient color specification'
	CLSID = IID('{95CD20B7-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{B2FE80F4-9612-48F9-87AD-B79A905BCBFC}')

	def SetMatrix(self, arg0=defaultUnnamedArg):
		'additional transformation arising from manipulating the path'
		return self._oleobj_.InvokeTypes(1950767181, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		"Angle": (1883326284, 2, (5, 0), (), "Angle", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'Gradient' returns object of type 'Gradient'
		"Gradient": (1667319620, 2, (9, 0), (), "Gradient", '{95CD20AE-AD72-11D3-B086-0010A4F5C335}'),
		"HiliteAngle": (1197753450, 2, (5, 0), (), "HiliteAngle", None),
		"HiliteLength": (1197753464, 2, (5, 0), (), "HiliteLength", None),
		"Length": (1818586727, 2, (5, 0), (), "Length", None),
		# Method 'Matrix' returns object of type '_Matrix'
		"Matrix": (1950767181, 2, (9, 0), (), "Matrix", '{95CD20C9-AD72-11D3-B086-0010A4F5C335}'),
		"Origin": (1197756263, 2, (12, 0), (), "Origin", None),
	}
	_prop_map_put_ = {
		"Angle": ((1883326284, LCID, 4, 0),()),
		"Gradient": ((1667319620, LCID, 4, 0),()),
		"HiliteAngle": ((1197753450, LCID, 4, 0),()),
		"HiliteLength": ((1197753464, LCID, 4, 0),()),
		"Length": ((1818586727, LCID, 4, 0),()),
		"Matrix": ((1950767181, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Origin": ((1197756263, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _GrayColor(DispatchBaseClass):
	'A gray color specification'
	CLSID = IID('{95CD20B3-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{2FEEBDFA-68E5-49AE-BE7B-1A97F09DF8F9}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Gray": (1196573017, 2, (5, 0), (), "Gray", None),
	}
	_prop_map_put_ = {
		"Gray": ((1196573017, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _IllustratorSaveOptions(DispatchBaseClass):
	'Options which may be supplied when saving a document as an Illustrator file'
	CLSID = IID('{95CD20A9-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{5C9DB812-A552-4513-8C6B-3D21EFC42605}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtboardRange": (1884304483, 2, (8, 0), (), "ArtboardRange", None),
		"Compatibility": (1883849584, 2, (3, 0), (), "Compatibility", None),
		"Compressed": (1883456611, 2, (11, 0), (), "Compressed", None),
		"EmbedICCProfile": (1883590758, 2, (11, 0), (), "EmbedICCProfile", None),
		"EmbedLinkedFiles": (1883861065, 2, (11, 0), (), "EmbedLinkedFiles", None),
		"FlattenOutput": (1884243564, 2, (3, 0), (), "FlattenOutput", None),
		"FontSubsetThreshold": (1883657044, 2, (5, 0), (), "FontSubsetThreshold", None),
		"JapaneseFileFormat": (1883924070, 2, (11, 0), (), "JapaneseFileFormat", None),
		"PDFCompatible": (1884308326, 2, (11, 0), (), "PDFCompatible", None),
		"SaveMultipleArtboards": (1397571938, 2, (11, 0), (), "SaveMultipleArtboards", None),
	}
	_prop_map_put_ = {
		"ArtboardRange": ((1884304483, LCID, 4, 0),()),
		"Compatibility": ((1883849584, LCID, 4, 0),()),
		"Compressed": ((1883456611, LCID, 4, 0),()),
		"EmbedICCProfile": ((1883590758, LCID, 4, 0),()),
		"EmbedLinkedFiles": ((1883861065, LCID, 4, 0),()),
		"FlattenOutput": ((1884243564, LCID, 4, 0),()),
		"FontSubsetThreshold": ((1883657044, LCID, 4, 0),()),
		"JapaneseFileFormat": ((1883924070, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"PDFCompatible": ((1884308326, LCID, 4, 0),()),
		"SaveMultipleArtboards": ((1397571938, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _ImageCaptureOptions(DispatchBaseClass):
	'Options which may be supplied when capturing a portion of the artwork as an 24 bit PNG file'
	CLSID = IID('{4C78DFEB-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = IID('{BD1B34AB-D76C-4DA1-A134-086969C4EDEF}')

	def SetMatteColor(self, arg0=defaultUnnamedArg):
		'the color to use when matting the artboard (default: white)'
		return self._oleobj_.InvokeTypes(1884111724, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		"AntiAliasing": (1883336257, 2, (11, 0), (), "AntiAliasing", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Matte": (1884111170, 2, (11, 0), (), "Matte", None),
		# Method 'MatteColor' returns object of type '_RGBColor'
		"MatteColor": (1884111724, 2, (9, 0), (), "MatteColor", '{95CD20B1-AD72-11D3-B086-0010A4F5C335}'),
		"Resolution": (1634292314, 2, (5, 0), (), "Resolution", None),
		"Transparency": (1884581987, 2, (11, 0), (), "Transparency", None),
	}
	_prop_map_put_ = {
		"AntiAliasing": ((1883336257, LCID, 4, 0),()),
		"Matte": ((1884111170, LCID, 4, 0),()),
		"MatteColor": ((1884111724, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Resolution": ((1634292314, LCID, 4, 0),()),
		"Transparency": ((1884581987, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _Ink(DispatchBaseClass):
	"printer's ink"
	CLSID = IID('{95CD2C10-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{E417157D-29E4-408A-B742-0F908DF8C745}')

	def SetInkInfo(self, arg0=defaultUnnamedArg):
		'the ink information'
		return self._oleobj_.InvokeTypes(1883327564, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'InkInfo' returns object of type '_InkInfo'
		"InkInfo": (1883327564, 2, (9, 0), (), "InkInfo", '{95CD2C11-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
	}
	_prop_map_put_ = {
		"InkInfo": ((1883327564, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _InkInfo(DispatchBaseClass):
	'Ink information'
	CLSID = IID('{95CD2C11-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{F4A69A15-7701-4DF4-948D-9E7FBACC0787}')

	def SetCustomColor(self, arg0=defaultUnnamedArg):
		'the color of the custom ink'
		return self._oleobj_.InvokeTypes(1884319030, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		"Angle": (1883326284, 2, (5, 0), (), "Angle", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"CustomColor": (1884319030, 2, (9, 0), (), "CustomColor", None),
		"Density": (1884319028, 2, (5, 0), (), "Density", None),
		"DotShape": (1884319031, 2, (8, 0), (), "DotShape", None),
		"Frequency": (1884316210, 2, (5, 0), (), "Frequency", None),
		"Kind": (1668826196, 2, (3, 0), (), "Kind", None),
		"PrintingStatus": (1884305209, 2, (3, 0), (), "PrintingStatus", None),
		"Trapping": (1884319026, 2, (3, 0), (), "Trapping", None),
		"TrappingOrder": (1884319027, 2, (3, 0), (), "TrappingOrder", None),
	}
	_prop_map_put_ = {
		"Angle": ((1883326284, LCID, 4, 0),()),
		"CustomColor": ((1884319030, LCID, 4, 0),()),
		"Density": ((1884319028, LCID, 4, 0),()),
		"DotShape": ((1884319031, LCID, 4, 0),()),
		"Frequency": ((1884316210, LCID, 4, 0),()),
		"Kind": ((1668826196, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"PrintingStatus": ((1884305209, LCID, 4, 0),()),
		"Trapping": ((1884319026, LCID, 4, 0),()),
		"TrappingOrder": ((1884319027, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _LabColor(DispatchBaseClass):
	'An Lab color specification'
	CLSID = IID('{57EDB0EB-8F86-4898-AA88-5D6F47DEE239}')
	coclass_clsid = IID('{EF57A9D6-A4A8-4136-94C8-8C707F392A92}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		"A": (1281450561, 2, (5, 0), (), "A", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"B": (1281450562, 2, (5, 0), (), "B", None),
		"L": (1281450572, 2, (5, 0), (), "L", None),
	}
	_prop_map_put_ = {
		"A": ((1281450561, LCID, 4, 0),()),
		"B": ((1281450562, LCID, 4, 0),()),
		"L": ((1281450572, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _Matrix(DispatchBaseClass):
	CLSID = IID('{95CD20C9-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{E580BAB8-2188-4312-A007-7449839ACF29}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"MValueA": (1952536172, 2, (5, 0), (), "MValueA", None),
		"MValueB": (1952601708, 2, (5, 0), (), "MValueB", None),
		"MValueC": (1952667244, 2, (5, 0), (), "MValueC", None),
		"MValueD": (1952732780, 2, (5, 0), (), "MValueD", None),
		"MValueTX": (1953790038, 2, (5, 0), (), "MValueTX", None),
		"MValueTY": (1953790294, 2, (5, 0), (), "MValueTY", None),
	}
	_prop_map_put_ = {
		"MValueA": ((1952536172, LCID, 4, 0),()),
		"MValueB": ((1952601708, LCID, 4, 0),()),
		"MValueC": ((1952667244, LCID, 4, 0),()),
		"MValueD": ((1952732780, LCID, 4, 0),()),
		"MValueTX": ((1953790038, LCID, 4, 0),()),
		"MValueTY": ((1953790294, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _NoColor(DispatchBaseClass):
	"represents the 'none' color"
	CLSID = IID('{4C78DFE6-7A09-11D4-81A0-00C04F60ECCC}')
	coclass_clsid = IID('{013C465C-6000-40C3-B7A6-B236B53A672D}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
	}
	_prop_map_put_ = {
		"ObjectValue": ((0, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _OpenOptions(DispatchBaseClass):
	'Options which may be supplied when opening a file'
	CLSID = IID('{60E764BB-CBEE-421F-B706-D228072EBB89}')
	coclass_clsid = IID('{F95B83D1-94FC-4AF6-99B0-9094BE3AB899}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		"AddToRecentFiles": (1883329618, 2, (11, 0), (), "AddToRecentFiles", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ConvertCropAreaToArtboard": (1883456321, 2, (11, 0), (), "ConvertCropAreaToArtboard", None),
		"ConvertTilesToArtboard": (1883460673, 2, (11, 0), (), "ConvertTilesToArtboard", None),
		"CreateArtboardWithArtworkBoundingBox": (1883455810, 2, (11, 0), (), "CreateArtboardWithArtworkBoundingBox", None),
		"OpenAs": (1718383728, 2, (3, 0), (), "OpenAs", None),
		"PreserveLegacyArtboard": (1884310593, 2, (11, 0), (), "PreserveLegacyArtboard", None),
		"UpdateLegacyGradientMesh": (1884047181, 2, (11, 0), (), "UpdateLegacyGradientMesh", None),
		"UpdateLegacyText": (1883458644, 2, (11, 0), (), "UpdateLegacyText", None),
	}
	_prop_map_put_ = {
		"AddToRecentFiles": ((1883329618, LCID, 4, 0),()),
		"ConvertCropAreaToArtboard": ((1883456321, LCID, 4, 0),()),
		"ConvertTilesToArtboard": ((1883460673, LCID, 4, 0),()),
		"CreateArtboardWithArtworkBoundingBox": ((1883455810, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"OpenAs": ((1718383728, LCID, 4, 0),()),
		"PreserveLegacyArtboard": ((1884310593, LCID, 4, 0),()),
		"UpdateLegacyGradientMesh": ((1884047181, LCID, 4, 0),()),
		"UpdateLegacyText": ((1883458644, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _PDFSaveOptions(DispatchBaseClass):
	'Options which may be supplied when saving a document as a PDF file'
	CLSID = IID('{95CD20A8-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{695B5492-AC6A-479A-A2B1-E8AE9DDE5B40}')

	def SetFlattenerOptions(self, arg0=defaultUnnamedArg):
		'the printing flattener options'
		return self._oleobj_.InvokeTypes(1884304227, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		"AcrobatLayers": (1883131980, 2, (11, 0), (), "AcrobatLayers", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtboardRange": (1884304483, 2, (8, 0), (), "ArtboardRange", None),
		"BleedLink": (1883128395, 2, (11, 0), (), "BleedLink", None),
		"BleedOffsetRect": (1884305207, 2, (12, 0), (), "BleedOffsetRect", None),
		"ColorBars": (1884305205, 2, (11, 0), (), "ColorBars", None),
		"ColorCompression": (1883128674, 2, (3, 0), (), "ColorCompression", None),
		"ColorConversionID": (1883128643, 2, (3, 0), (), "ColorConversionID", None),
		"ColorDestinationID": (1883128654, 2, (3, 0), (), "ColorDestinationID", None),
		"ColorDownsampling": (1883128644, 2, (5, 0), (), "ColorDownsampling", None),
		"ColorDownsamplingImageThreshold": (1883128641, 2, (5, 0), (), "ColorDownsamplingImageThreshold", None),
		"ColorDownsamplingMethod": (1883128659, 2, (3, 0), (), "ColorDownsamplingMethod", None),
		"ColorProfileID": (1883128656, 2, (3, 0), (), "ColorProfileID", None),
		"ColorTileSize": (1883128660, 2, (3, 0), (), "ColorTileSize", None),
		"Compatibility": (1883849584, 2, (3, 0), (), "Compatibility", None),
		"CompressArt": (1883133004, 2, (11, 0), (), "CompressArt", None),
		"DocumentPassword": (1883128912, 2, (8, 0), (), "DocumentPassword", None),
		"EnableAccess": (1883129153, 2, (11, 0), (), "EnableAccess", None),
		"EnableCopy": (1883129155, 2, (11, 0), (), "EnableCopy", None),
		"EnableCopyAccess": (1883129154, 2, (11, 0), (), "EnableCopyAccess", None),
		"EnablePlainText": (1883129168, 2, (11, 0), (), "EnablePlainText", None),
		# Method 'FlattenerOptions' returns object of type '_PrintFlattenerOptions'
		"FlattenerOptions": (1884304227, 2, (9, 0), (), "FlattenerOptions", '{95CD2C12-AD72-11D3-B086-0010A4F5C335}'),
		"FlattenerPreset": (1950765908, 2, (8, 0), (), "FlattenerPreset", None),
		"FontSubsetThreshold": (1883657044, 2, (5, 0), (), "FontSubsetThreshold", None),
		"GenerateThumbnails": (1883129684, 2, (11, 0), (), "GenerateThumbnails", None),
		"GrayscaleCompression": (1883129698, 2, (3, 0), (), "GrayscaleCompression", None),
		"GrayscaleDownsampling": (1883129668, 2, (5, 0), (), "GrayscaleDownsampling", None),
		"GrayscaleDownsamplingImageThreshold": (1883129665, 2, (5, 0), (), "GrayscaleDownsamplingImageThreshold", None),
		"GrayscaleDownsamplingMethod": (1883129683, 2, (3, 0), (), "GrayscaleDownsamplingMethod", None),
		"GrayscaleTileSize": (1883129690, 2, (3, 0), (), "GrayscaleTileSize", None),
		"MonochromeCompression": (1883131217, 2, (3, 0), (), "MonochromeCompression", None),
		"MonochromeDownsampling": (1883131204, 2, (5, 0), (), "MonochromeDownsampling", None),
		"MonochromeDownsamplingImageThreshold": (1883131201, 2, (5, 0), (), "MonochromeDownsamplingImageThreshold", None),
		"MonochromeDownsamplingMethod": (1883131219, 2, (3, 0), (), "MonochromeDownsamplingMethod", None),
		"Offset": (1883131713, 2, (5, 0), (), "Offset", None),
		"Optimization": (1884254317, 2, (11, 0), (), "Optimization", None),
		"OutputCondition": (1883128655, 2, (8, 0), (), "OutputCondition", None),
		"OutputConditionID": (1883128661, 2, (8, 0), (), "OutputConditionID", None),
		"OutputIntentProfile": (1883128649, 2, (8, 0), (), "OutputIntentProfile", None),
		"PDFAllowPrinting": (1883131969, 2, (3, 0), (), "PDFAllowPrinting", None),
		"PDFChangesAllowed": (1883128647, 2, (3, 0), (), "PDFChangesAllowed", None),
		"PDFPreset": (1883131731, 2, (8, 0), (), "PDFPreset", None),
		"PDFXStandard": (1883131992, 2, (3, 0), (), "PDFXStandard", None),
		"PDFXStandardDescription": (1883131972, 2, (8, 0), (), "PDFXStandardDescription", None),
		"PageInformation": (1883131977, 2, (11, 0), (), "PageInformation", None),
		"PageMarksType": (1884305201, 2, (3, 0), (), "PageMarksType", None),
		"PermissionPassword": (1883131984, 2, (8, 0), (), "PermissionPassword", None),
		"PreserveEditability": (1883131973, 2, (11, 0), (), "PreserveEditability", None),
		"PrinterResolution": (1883129424, 2, (5, 0), (), "PrinterResolution", None),
		"RegistrationMarks": (1884305204, 2, (11, 0), (), "RegistrationMarks", None),
		"RegistryName": (1883128666, 2, (8, 0), (), "RegistryName", None),
		"RequireDocumentPassword": (1883128914, 2, (11, 0), (), "RequireDocumentPassword", None),
		"RequirePermissionPassword": (1883131986, 2, (11, 0), (), "RequirePermissionPassword", None),
		"Trapped": (1883128658, 2, (11, 0), (), "Trapped", None),
		"TrimMarkWeight": (1883133015, 2, (3, 0), (), "TrimMarkWeight", None),
		"TrimMarks": (1884305203, 2, (11, 0), (), "TrimMarks", None),
		"ViewAfterSaving": (1883133523, 2, (11, 0), (), "ViewAfterSaving", None),
	}
	_prop_map_put_ = {
		"AcrobatLayers": ((1883131980, LCID, 4, 0),()),
		"ArtboardRange": ((1884304483, LCID, 4, 0),()),
		"BleedLink": ((1883128395, LCID, 4, 0),()),
		"BleedOffsetRect": ((1884305207, LCID, 4, 0),()),
		"ColorBars": ((1884305205, LCID, 4, 0),()),
		"ColorCompression": ((1883128674, LCID, 4, 0),()),
		"ColorConversionID": ((1883128643, LCID, 4, 0),()),
		"ColorDestinationID": ((1883128654, LCID, 4, 0),()),
		"ColorDownsampling": ((1883128644, LCID, 4, 0),()),
		"ColorDownsamplingImageThreshold": ((1883128641, LCID, 4, 0),()),
		"ColorDownsamplingMethod": ((1883128659, LCID, 4, 0),()),
		"ColorProfileID": ((1883128656, LCID, 4, 0),()),
		"ColorTileSize": ((1883128660, LCID, 4, 0),()),
		"Compatibility": ((1883849584, LCID, 4, 0),()),
		"CompressArt": ((1883133004, LCID, 4, 0),()),
		"DocumentPassword": ((1883128912, LCID, 4, 0),()),
		"EnableAccess": ((1883129153, LCID, 4, 0),()),
		"EnableCopy": ((1883129155, LCID, 4, 0),()),
		"EnableCopyAccess": ((1883129154, LCID, 4, 0),()),
		"EnablePlainText": ((1883129168, LCID, 4, 0),()),
		"FlattenerOptions": ((1884304227, LCID, 4, 0),()),
		"FlattenerPreset": ((1950765908, LCID, 4, 0),()),
		"FontSubsetThreshold": ((1883657044, LCID, 4, 0),()),
		"GenerateThumbnails": ((1883129684, LCID, 4, 0),()),
		"GrayscaleCompression": ((1883129698, LCID, 4, 0),()),
		"GrayscaleDownsampling": ((1883129668, LCID, 4, 0),()),
		"GrayscaleDownsamplingImageThreshold": ((1883129665, LCID, 4, 0),()),
		"GrayscaleDownsamplingMethod": ((1883129683, LCID, 4, 0),()),
		"GrayscaleTileSize": ((1883129690, LCID, 4, 0),()),
		"MonochromeCompression": ((1883131217, LCID, 4, 0),()),
		"MonochromeDownsampling": ((1883131204, LCID, 4, 0),()),
		"MonochromeDownsamplingImageThreshold": ((1883131201, LCID, 4, 0),()),
		"MonochromeDownsamplingMethod": ((1883131219, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Offset": ((1883131713, LCID, 4, 0),()),
		"Optimization": ((1884254317, LCID, 4, 0),()),
		"OutputCondition": ((1883128655, LCID, 4, 0),()),
		"OutputConditionID": ((1883128661, LCID, 4, 0),()),
		"OutputIntentProfile": ((1883128649, LCID, 4, 0),()),
		"PDFAllowPrinting": ((1883131969, LCID, 4, 0),()),
		"PDFChangesAllowed": ((1883128647, LCID, 4, 0),()),
		"PDFPreset": ((1883131731, LCID, 4, 0),()),
		"PDFXStandard": ((1883131992, LCID, 4, 0),()),
		"PDFXStandardDescription": ((1883131972, LCID, 4, 0),()),
		"PageInformation": ((1883131977, LCID, 4, 0),()),
		"PageMarksType": ((1884305201, LCID, 4, 0),()),
		"PermissionPassword": ((1883131984, LCID, 4, 0),()),
		"PreserveEditability": ((1883131973, LCID, 4, 0),()),
		"PrinterResolution": ((1883129424, LCID, 4, 0),()),
		"RegistrationMarks": ((1884305204, LCID, 4, 0),()),
		"RegistryName": ((1883128666, LCID, 4, 0),()),
		"RequireDocumentPassword": ((1883128914, LCID, 4, 0),()),
		"RequirePermissionPassword": ((1883131986, LCID, 4, 0),()),
		"Trapped": ((1883128658, LCID, 4, 0),()),
		"TrimMarkWeight": ((1883133015, LCID, 4, 0),()),
		"TrimMarks": ((1884305203, LCID, 4, 0),()),
		"ViewAfterSaving": ((1883133523, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _PPDFile(DispatchBaseClass):
	'a PPD file'
	CLSID = IID('{95CD2C0C-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{D2DBC561-0DCE-4141-8FE8-2ECA346CED3E}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetPPDInfo(self, arg0=defaultUnnamedArg):
		'the PPD file information'
		return self._oleobj_.InvokeTypes(1883327564, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		# Method 'PPDInfo' returns object of type '_PPDFileInfo'
		"PPDInfo": (1883327564, 2, (9, 0), (), "PPDInfo", '{95CD2C09-AD72-11D3-B086-0010A4F5C335}'),
	}
	_prop_map_put_ = {
		"Name": ((1886282093, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"PPDInfo": ((1883327564, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _PPDFileInfo(DispatchBaseClass):
	'PPD file information'
	CLSID = IID('{95CD2C09-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{EBE15492-1925-4BA2-A987-8F77CB15FCF0}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"File": (1634289235, 2, (8, 0), (), "File", None),
		"LanguageLevel": (1884303665, 2, (8, 0), (), "LanguageLevel", None),
		"ScreenList": (1884303667, 2, (12, 0), (), "ScreenList", None),
		"ScreenSpotFunctionList": (1884303668, 2, (12, 0), (), "ScreenSpotFunctionList", None),
	}
	_prop_map_put_ = {
		"File": ((1634289235, LCID, 4, 0),()),
		"LanguageLevel": ((1884303665, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"ScreenList": ((1884303667, LCID, 4, 0),()),
		"ScreenSpotFunctionList": ((1884303668, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _Paper(DispatchBaseClass):
	'paper size'
	CLSID = IID('{95CD2C0D-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{99044697-4AD8-4B63-A3D8-BBFE4610C844}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetPaperInfo(self, arg0=defaultUnnamedArg):
		'the paper information'
		return self._oleobj_.InvokeTypes(1883327564, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		# Method 'PaperInfo' returns object of type '_PaperInfo'
		"PaperInfo": (1883327564, 2, (9, 0), (), "PaperInfo", '{95CD2C0A-AD72-11D3-B086-0010A4F5C335}'),
	}
	_prop_map_put_ = {
		"Name": ((1886282093, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"PaperInfo": ((1883327564, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _PaperInfo(DispatchBaseClass):
	'Paper information'
	CLSID = IID('{95CD2C0A-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{2D6EDDEF-62F9-4D38-A0B5-68B576721018}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"CustomPaper": (1884303922, 2, (11, 0), (), "CustomPaper", None),
		"Height": (1884506216, 2, (5, 0), (), "Height", None),
		"ImageableArea": (1884303921, 2, (12, 0), (), "ImageableArea", None),
		"Width": (1884506231, 2, (5, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"CustomPaper": ((1884303922, LCID, 4, 0),()),
		"Height": ((1884506216, LCID, 4, 0),()),
		"ImageableArea": ((1884303921, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Width": ((1884506231, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _PatternColor(DispatchBaseClass):
	'A Pattern color specification'
	CLSID = IID('{95CD20B6-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{F493FD6F-9E65-4AE4-AED9-AFDA9CF7F3ED}')

	def SetMatrix(self, arg0=defaultUnnamedArg):
		'additional transformation arising from manipulating the path'
		return self._oleobj_.InvokeTypes(1950767181, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'Matrix' returns object of type '_Matrix'
		"Matrix": (1950767181, 2, (9, 0), (), "Matrix", '{95CD20C9-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'Pattern' returns object of type 'Pattern'
		"Pattern": (1667321940, 2, (9, 0), (), "Pattern", '{95CD20B9-AD72-11D3-B086-0010A4F5C335}'),
		"Reflect": (1400394342, 2, (11, 0), (), "Reflect", None),
		"ReflectAngle": (1400394337, 2, (5, 0), (), "ReflectAngle", None),
		"Rotation": (1400394360, 2, (5, 0), (), "Rotation", None),
		"ScaleFactor": (1400394595, 2, (12, 0), (), "ScaleFactor", None),
		"ShearAngle": (1400394593, 2, (5, 0), (), "ShearAngle", None),
		"ShearAxis": (1400394616, 2, (5, 0), (), "ShearAxis", None),
		"ShiftAngle": (1400390753, 2, (5, 0), (), "ShiftAngle", None),
		"ShiftDistance": (1400390776, 2, (5, 0), (), "ShiftDistance", None),
	}
	_prop_map_put_ = {
		"Matrix": ((1950767181, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Pattern": ((1667321940, LCID, 4, 0),()),
		"Reflect": ((1400394342, LCID, 4, 0),()),
		"ReflectAngle": ((1400394337, LCID, 4, 0),()),
		"Rotation": ((1400394360, LCID, 4, 0),()),
		"ScaleFactor": ((1400394595, LCID, 4, 0),()),
		"ShearAngle": ((1400394593, LCID, 4, 0),()),
		"ShearAxis": ((1400394616, LCID, 4, 0),()),
		"ShiftAngle": ((1400390753, LCID, 4, 0),()),
		"ShiftDistance": ((1400390776, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _PrintColorManagementOptions(DispatchBaseClass):
	'the color management options'
	CLSID = IID('{95CD2C07-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{EBAD60C2-68F6-4D26-A3A2-0AFD276418AC}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ColorProfileMode": (1884315953, 2, (3, 0), (), "ColorProfileMode", None),
		"Intent": (1884315954, 2, (3, 0), (), "Intent", None),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
	}
	_prop_map_put_ = {
		"ColorProfileMode": ((1884315953, LCID, 4, 0),()),
		"Intent": ((1884315954, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _PrintColorSeparationOptions(DispatchBaseClass):
	'Print color separation options'
	CLSID = IID('{95CD2C02-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{C43D57E6-B94A-4DAD-BEA4-153159D34529}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ColorSeparationMode": (1884304689, 2, (3, 0), (), "ColorSeparationMode", None),
		"ConvertSpotColors": (1884304690, 2, (11, 0), (), "ConvertSpotColors", None),
		"InkList": (1884309836, 2, (12, 0), (), "InkList", None),
		"OverPrintBlack": (1884304691, 2, (11, 0), (), "OverPrintBlack", None),
	}
	_prop_map_put_ = {
		"ColorSeparationMode": ((1884304689, LCID, 4, 0),()),
		"ConvertSpotColors": ((1884304690, LCID, 4, 0),()),
		"InkList": ((1884309836, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"OverPrintBlack": ((1884304691, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _PrintCoordinateOptions(DispatchBaseClass):
	'the print coordinate options'
	CLSID = IID('{95CD2C03-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{42A65455-5260-4F3D-A4FE-33B2C5BF839C}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Emulsion": (1884304946, 2, (11, 0), (), "Emulsion", None),
		"FitToPage": (1884304948, 2, (11, 0), (), "FitToPage", None),
		"HorizontalScale": (1884510296, 2, (5, 0), (), "HorizontalScale", None),
		"Orientation": (1884304945, 2, (3, 0), (), "Orientation", None),
		"Position": (1885425779, 2, (3, 0), (), "Position", None),
		"Tiling": (1884304951, 2, (3, 0), (), "Tiling", None),
		"VerticalScale": (1884510553, 2, (5, 0), (), "VerticalScale", None),
	}
	_prop_map_put_ = {
		"Emulsion": ((1884304946, LCID, 4, 0),()),
		"FitToPage": ((1884304948, LCID, 4, 0),()),
		"HorizontalScale": ((1884510296, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Orientation": ((1884304945, LCID, 4, 0),()),
		"Position": ((1885425779, LCID, 4, 0),()),
		"Tiling": ((1884304951, LCID, 4, 0),()),
		"VerticalScale": ((1884510553, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _PrintFlattenerOptions(DispatchBaseClass):
	'the transparency flattening options'
	CLSID = IID('{95CD2C12-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{C3BF40DE-EDA0-493B-924A-42FD00D36CEB}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ClipComplexRegions": (1884319286, 2, (11, 0), (), "ClipComplexRegions", None),
		"ConvertStrokesToOutlines": (1884319285, 2, (11, 0), (), "ConvertStrokesToOutlines", None),
		"ConvertTextToOutlines": (1884319284, 2, (11, 0), (), "ConvertTextToOutlines", None),
		"FlatteningBalance": (1884319281, 2, (3, 0), (), "FlatteningBalance", None),
		"GradientResolution": (1884319283, 2, (5, 0), (), "GradientResolution", None),
		"Overprint": (1883131728, 2, (3, 0), (), "Overprint", None),
		"RasterizationResolution": (1884319282, 2, (5, 0), (), "RasterizationResolution", None),
	}
	_prop_map_put_ = {
		"ClipComplexRegions": ((1884319286, LCID, 4, 0),()),
		"ConvertStrokesToOutlines": ((1884319285, LCID, 4, 0),()),
		"ConvertTextToOutlines": ((1884319284, LCID, 4, 0),()),
		"FlatteningBalance": ((1884319281, LCID, 4, 0),()),
		"GradientResolution": ((1884319283, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Overprint": ((1883131728, LCID, 4, 0),()),
		"RasterizationResolution": ((1884319282, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _PrintFontOptions(DispatchBaseClass):
	'the font options for printing'
	CLSID = IID('{95CD2C05-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{FDB1EDFA-8339-4630-A515-6ACFD4102EDD}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"DownloadFonts": (1884305457, 2, (3, 0), (), "DownloadFonts", None),
		"FontSubstitution": (1884305460, 2, (3, 0), (), "FontSubstitution", None),
	}
	_prop_map_put_ = {
		"DownloadFonts": ((1884305457, LCID, 4, 0),()),
		"FontSubstitution": ((1884305460, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _PrintJobOptions(DispatchBaseClass):
	'the print job options'
	CLSID = IID('{95CD2C01-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{A816141F-0C6E-4F89-846A-0F596AEDAF9F}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ArtboardRange": (1884304483, 2, (8, 0), (), "ArtboardRange", None),
		"BitmapResolution": (1884304481, 2, (5, 0), (), "BitmapResolution", None),
		"Collate": (1884304439, 2, (11, 0), (), "Collate", None),
		"Copies": (1884304435, 2, (3, 0), (), "Copies", None),
		"Designation": (1884304433, 2, (3, 0), (), "Designation", None),
		"File": (1634289235, 2, (8, 0), (), "File", None),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"PrintAllArtboards": (1884304482, 2, (11, 0), (), "PrintAllArtboards", None),
		"PrintArea": (1884304434, 2, (3, 0), (), "PrintArea", None),
		"PrintAsBitmap": (1884304441, 2, (11, 0), (), "PrintAsBitmap", None),
		"ReversePages": (1884304438, 2, (11, 0), (), "ReversePages", None),
	}
	_prop_map_put_ = {
		"ArtboardRange": ((1884304483, LCID, 4, 0),()),
		"BitmapResolution": ((1884304481, LCID, 4, 0),()),
		"Collate": ((1884304439, LCID, 4, 0),()),
		"Copies": ((1884304435, LCID, 4, 0),()),
		"Designation": ((1884304433, LCID, 4, 0),()),
		"File": ((1634289235, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"PrintAllArtboards": ((1884304482, LCID, 4, 0),()),
		"PrintArea": ((1884304434, LCID, 4, 0),()),
		"PrintAsBitmap": ((1884304441, LCID, 4, 0),()),
		"ReversePages": ((1884304438, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _PrintOptions(DispatchBaseClass):
	'the print options'
	CLSID = IID('{95CD2C00-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{76543789-87FE-43E4-B70C-17089F44F447}')

	def SetColorManagementOptions(self, arg0=defaultUnnamedArg):
		'the printing color management options'
		return self._oleobj_.InvokeTypes(1884304226, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetColorSeparationOptions(self, arg0=defaultUnnamedArg):
		'the printing color separation options'
		return self._oleobj_.InvokeTypes(1884304182, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetCoordinateOptions(self, arg0=defaultUnnamedArg):
		'the printing coordinate options'
		return self._oleobj_.InvokeTypes(1884304183, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetFlattenerOptions(self, arg0=defaultUnnamedArg):
		'the printing flattener options'
		return self._oleobj_.InvokeTypes(1884304227, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetFontOptions(self, arg0=defaultUnnamedArg):
		'the printing font options'
		return self._oleobj_.InvokeTypes(1884304185, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetJobOptions(self, arg0=defaultUnnamedArg):
		'the printing job options'
		return self._oleobj_.InvokeTypes(1884304181, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetPageMarksOptions(self, arg0=defaultUnnamedArg):
		'the printing page marks options'
		return self._oleobj_.InvokeTypes(1884304184, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetPaperOptions(self, arg0=defaultUnnamedArg):
		'the paper options'
		return self._oleobj_.InvokeTypes(1884304179, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetPostScriptOptions(self, arg0=defaultUnnamedArg):
		'the printing PostScript options'
		return self._oleobj_.InvokeTypes(1884304225, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'ColorManagementOptions' returns object of type '_PrintColorManagementOptions'
		"ColorManagementOptions": (1884304226, 2, (9, 0), (), "ColorManagementOptions", '{95CD2C07-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'ColorSeparationOptions' returns object of type '_PrintColorSeparationOptions'
		"ColorSeparationOptions": (1884304182, 2, (9, 0), (), "ColorSeparationOptions", '{95CD2C02-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'CoordinateOptions' returns object of type '_PrintCoordinateOptions'
		"CoordinateOptions": (1884304183, 2, (9, 0), (), "CoordinateOptions", '{95CD2C03-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'FlattenerOptions' returns object of type '_PrintFlattenerOptions'
		"FlattenerOptions": (1884304227, 2, (9, 0), (), "FlattenerOptions", '{95CD2C12-AD72-11D3-B086-0010A4F5C335}'),
		"FlattenerPreset": (1950765908, 2, (8, 0), (), "FlattenerPreset", None),
		# Method 'FontOptions' returns object of type '_PrintFontOptions'
		"FontOptions": (1884304185, 2, (9, 0), (), "FontOptions", '{95CD2C05-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'JobOptions' returns object of type '_PrintJobOptions'
		"JobOptions": (1884304181, 2, (9, 0), (), "JobOptions", '{95CD2C01-AD72-11D3-B086-0010A4F5C335}'),
		"PPDName": (1884304178, 2, (8, 0), (), "PPDName", None),
		# Method 'PageMarksOptions' returns object of type '_PrintPageMarksOptions'
		"PageMarksOptions": (1884304184, 2, (9, 0), (), "PageMarksOptions", '{95CD2C04-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PaperOptions' returns object of type '_PrintPaperOptions'
		"PaperOptions": (1884304179, 2, (9, 0), (), "PaperOptions", '{95CD2C15-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'PostScriptOptions' returns object of type '_PrintPostScriptOptions'
		"PostScriptOptions": (1884304225, 2, (9, 0), (), "PostScriptOptions", '{95CD2C06-AD72-11D3-B086-0010A4F5C335}'),
		"PrintPreset": (1951421268, 2, (8, 0), (), "PrintPreset", None),
		"PrinterName": (1884304177, 2, (8, 0), (), "PrinterName", None),
	}
	_prop_map_put_ = {
		"ColorManagementOptions": ((1884304226, LCID, 4, 0),()),
		"ColorSeparationOptions": ((1884304182, LCID, 4, 0),()),
		"CoordinateOptions": ((1884304183, LCID, 4, 0),()),
		"FlattenerOptions": ((1884304227, LCID, 4, 0),()),
		"FlattenerPreset": ((1950765908, LCID, 4, 0),()),
		"FontOptions": ((1884304185, LCID, 4, 0),()),
		"JobOptions": ((1884304181, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"PPDName": ((1884304178, LCID, 4, 0),()),
		"PageMarksOptions": ((1884304184, LCID, 4, 0),()),
		"PaperOptions": ((1884304179, LCID, 4, 0),()),
		"PostScriptOptions": ((1884304225, LCID, 4, 0),()),
		"PrintPreset": ((1951421268, LCID, 4, 0),()),
		"PrinterName": ((1884304177, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _PrintPageMarksOptions(DispatchBaseClass):
	'the page marks options'
	CLSID = IID('{95CD2C04-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{D41CD84C-C090-4B8F-A7CD-44CCF26C254E}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"BleedOffsetRect": (1884305207, 2, (12, 0), (), "BleedOffsetRect", None),
		"ColorBars": (1884305205, 2, (11, 0), (), "ColorBars", None),
		"MarksOffsetRect": (1884305208, 2, (12, 0), (), "MarksOffsetRect", None),
		"PageInfoMarks": (1884305206, 2, (11, 0), (), "PageInfoMarks", None),
		"PageMarksType": (1884305201, 2, (3, 0), (), "PageMarksType", None),
		"RegistrationMarks": (1884305204, 2, (11, 0), (), "RegistrationMarks", None),
		"TrimMarks": (1884305203, 2, (11, 0), (), "TrimMarks", None),
		"TrimMarksWeight": (1884305202, 2, (5, 0), (), "TrimMarksWeight", None),
	}
	_prop_map_put_ = {
		"BleedOffsetRect": ((1884305207, LCID, 4, 0),()),
		"ColorBars": ((1884305205, LCID, 4, 0),()),
		"MarksOffsetRect": ((1884305208, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"PageInfoMarks": ((1884305206, LCID, 4, 0),()),
		"PageMarksType": ((1884305201, LCID, 4, 0),()),
		"RegistrationMarks": ((1884305204, LCID, 4, 0),()),
		"TrimMarks": ((1884305203, LCID, 4, 0),()),
		"TrimMarksWeight": ((1884305202, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _PrintPaperOptions(DispatchBaseClass):
	'the paper options'
	CLSID = IID('{95CD2C15-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{297CFCE2-7884-400D-AEB1-BAB1BB3CC897}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Height": (1884506216, 2, (5, 0), (), "Height", None),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"Offset": (1883131713, 2, (5, 0), (), "Offset", None),
		"Transverse": (1884319793, 2, (11, 0), (), "Transverse", None),
		"Width": (1884506231, 2, (5, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"Height": ((1884506216, LCID, 4, 0),()),
		"Name": ((1886282093, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Offset": ((1883131713, LCID, 4, 0),()),
		"Transverse": ((1884319793, LCID, 4, 0),()),
		"Width": ((1884506231, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _PrintPostScriptOptions(DispatchBaseClass):
	'the PostScript options'
	CLSID = IID('{95CD2C06-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{F58B5314-DC1D-4283-90C4-2248F6E60C6C}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"BinaryPrinting": (1884303417, 2, (11, 0), (), "BinaryPrinting", None),
		"CompatibleShading": (1884305717, 2, (11, 0), (), "CompatibleShading", None),
		"ForceContinuousTone": (1884305716, 2, (11, 0), (), "ForceContinuousTone", None),
		"ImageCompression": (1884305715, 2, (3, 0), (), "ImageCompression", None),
		"NegativePrinting": (1884305714, 2, (11, 0), (), "NegativePrinting", None),
		"PostScriptLevel": (1884312428, 2, (3, 0), (), "PostScriptLevel", None),
		"ShadingResolution": (1884305718, 2, (5, 0), (), "ShadingResolution", None),
	}
	_prop_map_put_ = {
		"BinaryPrinting": ((1884303417, LCID, 4, 0),()),
		"CompatibleShading": ((1884305717, LCID, 4, 0),()),
		"ForceContinuousTone": ((1884305716, LCID, 4, 0),()),
		"ImageCompression": ((1884305715, LCID, 4, 0),()),
		"NegativePrinting": ((1884305714, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"PostScriptLevel": ((1884312428, LCID, 4, 0),()),
		"ShadingResolution": ((1884305718, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _Printer(DispatchBaseClass):
	'an installed printer'
	CLSID = IID('{95CD2C0B-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{081252CB-D855-48B9-9D85-FA9A9981DF81}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetPrinterInfo(self, arg0=defaultUnnamedArg):
		'the printer information'
		return self._oleobj_.InvokeTypes(1883327564, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		# Method 'PrinterInfo' returns object of type '_PrinterInfo'
		"PrinterInfo": (1883327564, 2, (9, 0), (), "PrinterInfo", '{95CD2C08-AD72-11D3-B086-0010A4F5C335}'),
	}
	_prop_map_put_ = {
		"Name": ((1886282093, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"PrinterInfo": ((1883327564, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _PrinterInfo(DispatchBaseClass):
	'printer information'
	CLSID = IID('{95CD2C08-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{29FEE1EA-CD21-41A6-9340-6219E3E57BB7}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"BinaryPrintingSupport": (1884303417, 2, (11, 0), (), "BinaryPrintingSupport", None),
		"ColorSupport": (1884303411, 2, (3, 0), (), "ColorSupport", None),
		"CustomPaperSupport": (1884303414, 2, (11, 0), (), "CustomPaperSupport", None),
		"CustomPaperTransverseSupport": (1884303415, 2, (11, 0), (), "CustomPaperTransverseSupport", None),
		"DeviceResolution": (1884303412, 2, (5, 0), (), "DeviceResolution", None),
		"InRIPSeparationSupport": (1884303416, 2, (11, 0), (), "InRIPSeparationSupport", None),
		"MaxDeviceResolution": (1884303413, 2, (5, 0), (), "MaxDeviceResolution", None),
		"MaxPaperHeight": (1884303461, 2, (5, 0), (), "MaxPaperHeight", None),
		"MaxPaperHeightOffset": (1884303466, 2, (5, 0), (), "MaxPaperHeightOffset", None),
		"MaxPaperWidth": (1884303459, 2, (5, 0), (), "MaxPaperWidth", None),
		"MaxPaperWidthOffset": (1884303464, 2, (5, 0), (), "MaxPaperWidthOffset", None),
		"MinPaperHeight": (1884303460, 2, (5, 0), (), "MinPaperHeight", None),
		"MinPaperHeightOffset": (1884303465, 2, (5, 0), (), "MinPaperHeightOffset", None),
		"MinPaperWidth": (1884303458, 2, (5, 0), (), "MinPaperWidth", None),
		"MinPaperWidthOffset": (1884303462, 2, (5, 0), (), "MinPaperWidthOffset", None),
		"PaperSizes": (1884303457, 2, (12, 0), (), "PaperSizes", None),
		"PostScriptLevel": (1884312428, 2, (3, 0), (), "PostScriptLevel", None),
		"PrinterType": (1884303409, 2, (3, 0), (), "PrinterType", None),
	}
	_prop_map_put_ = {
		"BinaryPrintingSupport": ((1884303417, LCID, 4, 0),()),
		"ColorSupport": ((1884303411, LCID, 4, 0),()),
		"CustomPaperSupport": ((1884303414, LCID, 4, 0),()),
		"CustomPaperTransverseSupport": ((1884303415, LCID, 4, 0),()),
		"DeviceResolution": ((1884303412, LCID, 4, 0),()),
		"InRIPSeparationSupport": ((1884303416, LCID, 4, 0),()),
		"MaxDeviceResolution": ((1884303413, LCID, 4, 0),()),
		"MaxPaperHeight": ((1884303461, LCID, 4, 0),()),
		"MaxPaperHeightOffset": ((1884303466, LCID, 4, 0),()),
		"MaxPaperWidth": ((1884303459, LCID, 4, 0),()),
		"MaxPaperWidthOffset": ((1884303464, LCID, 4, 0),()),
		"MinPaperHeight": ((1884303460, LCID, 4, 0),()),
		"MinPaperHeightOffset": ((1884303465, LCID, 4, 0),()),
		"MinPaperWidth": ((1884303458, LCID, 4, 0),()),
		"MinPaperWidthOffset": ((1884303462, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"PaperSizes": ((1884303457, LCID, 4, 0),()),
		"PostScriptLevel": ((1884312428, LCID, 4, 0),()),
		"PrinterType": ((1884303409, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _RGBColor(DispatchBaseClass):
	'An RGB color specification'
	CLSID = IID('{95CD20B1-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{6707D262-70F2-423D-88E1-ADCE85B359CE}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Blue": (1112298821, 2, (5, 0), (), "Blue", None),
		"Green": (1196574030, 2, (5, 0), (), "Green", None),
		"Red": (1380271136, 2, (5, 0), (), "Red", None),
	}
	_prop_map_put_ = {
		"Blue": ((1112298821, LCID, 4, 0),()),
		"Green": ((1196574030, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Red": ((1380271136, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _RasterEffectOptions(DispatchBaseClass):
	'The document raster effects settings'
	CLSID = IID('{246086F4-6F43-4D2B-A0BA-3BFB0E484DDF}')
	coclass_clsid = IID('{F4FCC1A9-2D0B-4555-B48D-ADE421F10F54}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		"AntiAliasing": (1883336257, 2, (11, 0), (), "AntiAliasing", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"ClippingMask": (1884115787, 2, (11, 0), (), "ClippingMask", None),
		"ColorModel": (1698909540, 2, (3, 0), (), "ColorModel", None),
		"ConvertSpotColors": (1884304690, 2, (11, 0), (), "ConvertSpotColors", None),
		"Padding": (1884307780, 2, (5, 0), (), "Padding", None),
		"Resolution": (1634292314, 2, (5, 0), (), "Resolution", None),
		"Transparency": (1884581987, 2, (11, 0), (), "Transparency", None),
	}
	_prop_map_put_ = {
		"AntiAliasing": ((1883336257, LCID, 4, 0),()),
		"ClippingMask": ((1884115787, LCID, 4, 0),()),
		"ColorModel": ((1698909540, LCID, 4, 0),()),
		"ConvertSpotColors": ((1884304690, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Padding": ((1884307780, LCID, 4, 0),()),
		"Resolution": ((1634292314, LCID, 4, 0),()),
		"Transparency": ((1884581987, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _RasterizeOptions(DispatchBaseClass):
	'Options which may be supplied when rasterizing the artwork'
	CLSID = IID('{196F9F57-2023-4C2F-8662-9C20F9D6DE7A}')
	coclass_clsid = IID('{FA4BF28E-9A94-4EE8-A050-74C8A54B107F}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		"AntiAliasingMethod": (1698778195, 2, (3, 0), (), "AntiAliasingMethod", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"BackgroundBlack": (1883390539, 2, (11, 0), (), "BackgroundBlack", None),
		"ClippingMask": (1884115787, 2, (11, 0), (), "ClippingMask", None),
		"ColorModel": (1698909540, 2, (3, 0), (), "ColorModel", None),
		"ConvertSpotColors": (1884304690, 2, (11, 0), (), "ConvertSpotColors", None),
		"ConvertTextToOutlines": (1884319284, 2, (11, 0), (), "ConvertTextToOutlines", None),
		"IncludeLayers": (1883851865, 2, (11, 0), (), "IncludeLayers", None),
		"Padding": (1884307780, 2, (5, 0), (), "Padding", None),
		"Resolution": (1634292314, 2, (5, 0), (), "Resolution", None),
		"Transparency": (1884581987, 2, (11, 0), (), "Transparency", None),
	}
	_prop_map_put_ = {
		"AntiAliasingMethod": ((1698778195, LCID, 4, 0),()),
		"BackgroundBlack": ((1883390539, LCID, 4, 0),()),
		"ClippingMask": ((1884115787, LCID, 4, 0),()),
		"ColorModel": ((1698909540, LCID, 4, 0),()),
		"ConvertSpotColors": ((1884304690, LCID, 4, 0),()),
		"ConvertTextToOutlines": ((1884319284, LCID, 4, 0),()),
		"IncludeLayers": ((1883851865, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Padding": ((1884307780, LCID, 4, 0),()),
		"Resolution": ((1634292314, LCID, 4, 0),()),
		"Transparency": ((1884581987, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _Screen(DispatchBaseClass):
	'color separation screen'
	CLSID = IID('{95CD2C0E-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{162B9894-C6F9-4E55-A6D9-BFD86B8BF4F5}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def SetScreenInfo(self, arg0=defaultUnnamedArg):
		'the color separation screen information'
		return self._oleobj_.InvokeTypes(1883327564, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		# Method 'ScreenInfo' returns object of type '_ScreenInfo'
		"ScreenInfo": (1883327564, 2, (9, 0), (), "ScreenInfo", '{95CD2C0F-AD72-11D3-B086-0010A4F5C335}'),
	}
	_prop_map_put_ = {
		"Name": ((1886282093, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"ScreenInfo": ((1883327564, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _ScreenInfo(DispatchBaseClass):
	'Screen information'
	CLSID = IID('{95CD2C0F-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{FB23AEC3-074E-4CE4-8FC7-2391BBF14140}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		"Angle": (1883326284, 2, (5, 0), (), "Angle", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"DefaultScreen": (1884316209, 2, (11, 0), (), "DefaultScreen", None),
		"Frequency": (1884316210, 2, (5, 0), (), "Frequency", None),
	}
	_prop_map_put_ = {
		"Angle": ((1883326284, LCID, 4, 0),()),
		"DefaultScreen": ((1884316209, LCID, 4, 0),()),
		"Frequency": ((1884316210, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _ScreenSpotFunction(DispatchBaseClass):
	'color separation screen spot function'
	CLSID = IID('{95CD2C14-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{0D7F382B-98D9-4834-AE8D-6A03017CB774}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"Name": (1886282093, 2, (8, 0), (), "Name", None),
		"SpotFunction": (1884316211, 2, (8, 0), (), "SpotFunction", None),
	}
	_prop_map_put_ = {
		"Name": ((1886282093, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"SpotFunction": ((1884316211, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _SpotColor(DispatchBaseClass):
	'Information about the spot color'
	CLSID = IID('{95CD20B4-AD72-11D3-B086-0010A4F5C335}')
	coclass_clsid = IID('{00BAC15D-DEEB-47CE-B207-C0C72BC7718C}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		# Method 'Spot' returns object of type 'Spot'
		"Spot": (1667318595, 2, (9, 0), (), "Spot", '{95CD20B5-AD72-11D3-B086-0010A4F5C335}'),
		"Tint": (1414090324, 2, (5, 0), (), "Tint", None),
	}
	_prop_map_put_ = {
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Spot": ((1667318595, LCID, 4, 0),()),
		"Tint": ((1414090324, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _TabStopInfo(DispatchBaseClass):
	'Tab stop information (returned by tab stops from a paragraph object)'
	CLSID = IID('{E380AAF5-61BF-44C2-B3D2-00D631CE879D}')
	coclass_clsid = IID('{F26D5AB0-8B1D-4BF2-87A7-4EC6B74B03EF}')

	def SetObjectValue(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	_prop_map_get_ = {
		"Alignment": (1416835121, 2, (3, 0), (), "Alignment", None),
		# Method 'Application' returns object of type '_Application'
		"Application": (1667330160, 2, (9, 0), (), "Application", '{95CD20AA-AD72-11D3-B086-0010A4F5C335}'),
		"DecimalCharacter": (1416835122, 2, (8, 0), (), "DecimalCharacter", None),
		"Leader": (1416835123, 2, (8, 0), (), "Leader", None),
		"Position": (1885425779, 2, (5, 0), (), "Position", None),
	}
	_prop_map_put_ = {
		"Alignment": ((1416835121, LCID, 4, 0),()),
		"DecimalCharacter": ((1416835122, LCID, 4, 0),()),
		"Leader": ((1416835123, LCID, 4, 0),()),
		"ObjectValue": ((0, LCID, 4, 0),()),
		"Position": ((1885425779, LCID, 4, 0),()),
	}
	# Default method for this class is 'ObjectValue'
	def __call__(self, arg0=defaultUnnamedArg):
		return self._oleobj_.InvokeTypes(0, LCID, 8, (24, 0), ((9, 0),),arg0
			)

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'Illustrator.Application.CC.2017'
class Application(CoClassBaseClass): # A CoClass
	# The Adobe Illustrator application
	CLSID = IID('{0FA36670-F0BC-48C0-AD25-6CF62CAD3A31}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Application,
	]
	default_interface = _Application

# This CoClass is known by the name 'Illustrator.CMYKColor.CC.2017'
class CMYKColor(CoClassBaseClass): # A CoClass
	# A CMYK color specification
	CLSID = IID('{9AFB43D8-2ABA-4DE9-A3E1-617AAA863C22}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_CMYKColor,
	]
	default_interface = _CMYKColor

class Dimensions(CoClassBaseClass): # A CoClass
	# Dimensions (height and width)
	CLSID = IID('{40A7C4A8-EFD2-43A8-806F-5B0CCE61DCE6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Dimensions,
	]
	default_interface = _Dimensions

# This CoClass is known by the name 'Illustrator.DocumentPreset.CC.2017'
class DocumentPreset(CoClassBaseClass): # A CoClass
	# the new document preset to use for creating a new document
	CLSID = IID('{E2D4A432-9E16-41E6-BCA5-062890269CD1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_DocumentPreset,
	]
	default_interface = _DocumentPreset

# This CoClass is known by the name 'Illustrator.EPSSaveOptions.CC.2017'
class EPSSaveOptions(CoClassBaseClass): # A CoClass
	# Options which may be supplied when saving a document as an Illustrator EPS file
	CLSID = IID('{F07FD4A3-5651-47DA-AC33-91BC06403816}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_EPSSaveOptions,
	]
	default_interface = _EPSSaveOptions

# This CoClass is known by the name 'Illustrator.ExportOptionsAutoCAD.CC.2017'
class ExportOptionsAutoCAD(CoClassBaseClass): # A CoClass
	# Options which may be supplied when exporting a document to AutoCAD formats (.dwg or .dxf)
	CLSID = IID('{D678C828-971A-4759-8A5D-3FF12C221A22}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_ExportOptionsAutoCAD,
	]
	default_interface = _ExportOptionsAutoCAD

# This CoClass is known by the name 'Illustrator.ExportOptionsFlash.CC.2017'
class ExportOptionsFlash(CoClassBaseClass): # A CoClass
	# Options which may be supplied when exporting a document as an Flash (.SWF) file
	CLSID = IID('{09534ADA-D2A2-45EB-BD90-8E4D391D306B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_ExportOptionsFlash,
	]
	default_interface = _ExportOptionsFlash

# This CoClass is known by the name 'Illustrator.ExportOptionsGIF.CC.2017'
class ExportOptionsGIF(CoClassBaseClass): # A CoClass
	# Options which may be supplied when exporting a document as a GIF file
	CLSID = IID('{46E4F107-315D-4BDF-BE66-4E33D9596A9A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_ExportOptionsGIF,
	]
	default_interface = _ExportOptionsGIF

# This CoClass is known by the name 'Illustrator.ExportOptionsJPEG.CC.2017'
class ExportOptionsJPEG(CoClassBaseClass): # A CoClass
	# Options which may be supplied when exporting a document as a JPEG file
	CLSID = IID('{4C1581E0-3BA8-4CE6-83FC-34EF5F2A9F40}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_ExportOptionsJPEG,
	]
	default_interface = _ExportOptionsJPEG

# This CoClass is known by the name 'Illustrator.ExportOptionsPNG24.CC.2017'
class ExportOptionsPNG24(CoClassBaseClass): # A CoClass
	# Options which may be supplied when exporting a document as an 24 bit PNG file
	CLSID = IID('{668E6292-D51A-4628-9800-4817A6762DF3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_ExportOptionsPNG24,
	]
	default_interface = _ExportOptionsPNG24

# This CoClass is known by the name 'Illustrator.ExportOptionsPNG8.CC.2017'
class ExportOptionsPNG8(CoClassBaseClass): # A CoClass
	# Options which may be supplied when exporting a document as an 8 bit PNG file
	CLSID = IID('{ECF0C759-F01B-4B3B-8922-541C1C163DF3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_ExportOptionsPNG8,
	]
	default_interface = _ExportOptionsPNG8

# This CoClass is known by the name 'Illustrator.ExportOptionsPhotoshop.CC.2017'
class ExportOptionsPhotoshop(CoClassBaseClass): # A CoClass
	# Options which may be supplied when exporting a document as a Photoshop file
	CLSID = IID('{1CC2A29F-5B2C-4359-9728-0D1771BDE2B1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_ExportOptionsPhotoshop,
	]
	default_interface = _ExportOptionsPhotoshop

# This CoClass is known by the name 'Illustrator.ExportOptionsSVG.CC.2017'
class ExportOptionsSVG(CoClassBaseClass): # A CoClass
	# Options which may be supplied when exporting a document as an SVG file
	CLSID = IID('{8930E841-DD0D-47EB-ACB1-8A37AFDD5A2A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_ExportOptionsSVG,
	]
	default_interface = _ExportOptionsSVG

class ExportOptionsTIFF(CoClassBaseClass): # A CoClass
	# Options which may be supplied when exporting a document as a TIFF file
	CLSID = IID('{A07D1206-AB5A-4BB1-9207-AEBA31A2D652}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_ExportOptionsTIFF,
	]
	default_interface = _ExportOptionsTIFF

class ExportOptionsWebOptimizedSVG(CoClassBaseClass): # A CoClass
	# Options which may be supplied when exporting a document as a Web optimized SVG file
	CLSID = IID('{FCB10B56-8002-46AE-A70D-D02783FFA353}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_ExportOptionsWebOptimizedSVG,
	]
	default_interface = _ExportOptionsWebOptimizedSVG

# This CoClass is known by the name 'Illustrator.FXGSaveOptions.CC.2017'
class FXGSaveOptions(CoClassBaseClass): # A CoClass
	# Options which may be supplied when saving a document as an FXG file
	CLSID = IID('{8DA7F9C4-7E22-46BD-BA1D-5517A9F0CD18}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_FXGSaveOptions,
	]
	default_interface = _FXGSaveOptions

# This CoClass is known by the name 'Illustrator.GradientColor.CC.2017'
class GradientColor(CoClassBaseClass): # A CoClass
	# A Gradient color specification
	CLSID = IID('{B2FE80F4-9612-48F9-87AD-B79A905BCBFC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_GradientColor,
	]
	default_interface = _GradientColor

class GrayColor(CoClassBaseClass): # A CoClass
	# A gray color specification
	CLSID = IID('{2FEEBDFA-68E5-49AE-BE7B-1A97F09DF8F9}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_GrayColor,
	]
	default_interface = _GrayColor

# This CoClass is known by the name 'Illustrator.IllustratorSaveOptions.CC.2017'
class IllustratorSaveOptions(CoClassBaseClass): # A CoClass
	# Options which may be supplied when saving a document as an Illustrator file
	CLSID = IID('{5C9DB812-A552-4513-8C6B-3D21EFC42605}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_IllustratorSaveOptions,
	]
	default_interface = _IllustratorSaveOptions

# This CoClass is known by the name 'Illustrator.ImageCaptureOptions.CC.2017'
class ImageCaptureOptions(CoClassBaseClass): # A CoClass
	# Options which may be supplied when capturing a portion of the artwork as an 24 bit PNG file
	CLSID = IID('{BD1B34AB-D76C-4DA1-A134-086969C4EDEF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_ImageCaptureOptions,
	]
	default_interface = _ImageCaptureOptions

# This CoClass is known by the name 'Illustrator.Ink.CC.2017'
class Ink(CoClassBaseClass): # A CoClass
	# printer's ink
	CLSID = IID('{E417157D-29E4-408A-B742-0F908DF8C745}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Ink,
	]
	default_interface = _Ink

# This CoClass is known by the name 'Illustrator.InkInfo.CC.2017'
class InkInfo(CoClassBaseClass): # A CoClass
	# Ink information
	CLSID = IID('{F4A69A15-7701-4DF4-948D-9E7FBACC0787}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_InkInfo,
	]
	default_interface = _InkInfo

# This CoClass is known by the name 'Illustrator.LabColor.CC.2017'
class LabColor(CoClassBaseClass): # A CoClass
	# An Lab color specification
	CLSID = IID('{EF57A9D6-A4A8-4136-94C8-8C707F392A92}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_LabColor,
	]
	default_interface = _LabColor

# This CoClass is known by the name 'Illustrator.Matrix.CC.2017'
class Matrix(CoClassBaseClass): # A CoClass
	CLSID = IID('{E580BAB8-2188-4312-A007-7449839ACF29}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Matrix,
	]
	default_interface = _Matrix

# This CoClass is known by the name 'Illustrator.NoColor.CC.2017'
class NoColor(CoClassBaseClass): # A CoClass
	# represents the 'none' color
	CLSID = IID('{013C465C-6000-40C3-B7A6-B236B53A672D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_NoColor,
	]
	default_interface = _NoColor

# This CoClass is known by the name 'Illustrator.OpenOptions.CC.2017'
class OpenOptions(CoClassBaseClass): # A CoClass
	# Options which may be supplied when opening a file
	CLSID = IID('{F95B83D1-94FC-4AF6-99B0-9094BE3AB899}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_OpenOptions,
	]
	default_interface = _OpenOptions

# This CoClass is known by the name 'Illustrator.PDFSaveOptions.CC.2017'
class PDFSaveOptions(CoClassBaseClass): # A CoClass
	# Options which may be supplied when saving a document as a PDF file
	CLSID = IID('{695B5492-AC6A-479A-A2B1-E8AE9DDE5B40}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PDFSaveOptions,
	]
	default_interface = _PDFSaveOptions

# This CoClass is known by the name 'Illustrator.PPDFile.CC.2017'
class PPDFile(CoClassBaseClass): # A CoClass
	# a PPD file
	CLSID = IID('{D2DBC561-0DCE-4141-8FE8-2ECA346CED3E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PPDFile,
	]
	default_interface = _PPDFile

# This CoClass is known by the name 'Illustrator.PPDFileInfo.CC.2017'
class PPDFileInfo(CoClassBaseClass): # A CoClass
	# PPD file information
	CLSID = IID('{EBE15492-1925-4BA2-A987-8F77CB15FCF0}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PPDFileInfo,
	]
	default_interface = _PPDFileInfo

# This CoClass is known by the name 'Illustrator.Paper.CC.2017'
class Paper(CoClassBaseClass): # A CoClass
	# paper size
	CLSID = IID('{99044697-4AD8-4B63-A3D8-BBFE4610C844}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Paper,
	]
	default_interface = _Paper

# This CoClass is known by the name 'Illustrator.PaperInfo.CC.2017'
class PaperInfo(CoClassBaseClass): # A CoClass
	# Paper information
	CLSID = IID('{2D6EDDEF-62F9-4D38-A0B5-68B576721018}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PaperInfo,
	]
	default_interface = _PaperInfo

# This CoClass is known by the name 'Illustrator.PatternColor.CC.2017'
class PatternColor(CoClassBaseClass): # A CoClass
	# A Pattern color specification
	CLSID = IID('{F493FD6F-9E65-4AE4-AED9-AFDA9CF7F3ED}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PatternColor,
	]
	default_interface = _PatternColor

# This CoClass is known by the name 'Illustrator.PrintColorManagementOptions.CC.2017'
class PrintColorManagementOptions(CoClassBaseClass): # A CoClass
	# the color management options
	CLSID = IID('{EBAD60C2-68F6-4D26-A3A2-0AFD276418AC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PrintColorManagementOptions,
	]
	default_interface = _PrintColorManagementOptions

# This CoClass is known by the name 'Illustrator.PrintColorSeparationOptions.CC.2017'
class PrintColorSeparationOptions(CoClassBaseClass): # A CoClass
	# Print color separation options
	CLSID = IID('{C43D57E6-B94A-4DAD-BEA4-153159D34529}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PrintColorSeparationOptions,
	]
	default_interface = _PrintColorSeparationOptions

class PrintCoordinateOptions(CoClassBaseClass): # A CoClass
	# the print coordinate options
	CLSID = IID('{42A65455-5260-4F3D-A4FE-33B2C5BF839C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PrintCoordinateOptions,
	]
	default_interface = _PrintCoordinateOptions

# This CoClass is known by the name 'Illustrator.PrintFlattenerOptions.CC.2017'
class PrintFlattenerOptions(CoClassBaseClass): # A CoClass
	# the transparency flattening options
	CLSID = IID('{C3BF40DE-EDA0-493B-924A-42FD00D36CEB}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PrintFlattenerOptions,
	]
	default_interface = _PrintFlattenerOptions

# This CoClass is known by the name 'Illustrator.PrintFontOptions.CC.2017'
class PrintFontOptions(CoClassBaseClass): # A CoClass
	# the font options for printing
	CLSID = IID('{FDB1EDFA-8339-4630-A515-6ACFD4102EDD}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PrintFontOptions,
	]
	default_interface = _PrintFontOptions

# This CoClass is known by the name 'Illustrator.PrintJobOptions.CC.2017'
class PrintJobOptions(CoClassBaseClass): # A CoClass
	# the print job options
	CLSID = IID('{A816141F-0C6E-4F89-846A-0F596AEDAF9F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PrintJobOptions,
	]
	default_interface = _PrintJobOptions

# This CoClass is known by the name 'Illustrator.PrintOptions.CC.2017'
class PrintOptions(CoClassBaseClass): # A CoClass
	# the print options
	CLSID = IID('{76543789-87FE-43E4-B70C-17089F44F447}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PrintOptions,
	]
	default_interface = _PrintOptions

# This CoClass is known by the name 'Illustrator.PrintPageMarksOptions.CC.2017'
class PrintPageMarksOptions(CoClassBaseClass): # A CoClass
	# the page marks options
	CLSID = IID('{D41CD84C-C090-4B8F-A7CD-44CCF26C254E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PrintPageMarksOptions,
	]
	default_interface = _PrintPageMarksOptions

# This CoClass is known by the name 'Illustrator.PrintPaperOptions.CC.2017'
class PrintPaperOptions(CoClassBaseClass): # A CoClass
	# the paper options
	CLSID = IID('{297CFCE2-7884-400D-AEB1-BAB1BB3CC897}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PrintPaperOptions,
	]
	default_interface = _PrintPaperOptions

# This CoClass is known by the name 'Illustrator.PrintPostScriptOptions.CC.2017'
class PrintPostScriptOptions(CoClassBaseClass): # A CoClass
	# the PostScript options
	CLSID = IID('{F58B5314-DC1D-4283-90C4-2248F6E60C6C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PrintPostScriptOptions,
	]
	default_interface = _PrintPostScriptOptions

# This CoClass is known by the name 'Illustrator.Printer.CC.2017'
class Printer(CoClassBaseClass): # A CoClass
	# an installed printer
	CLSID = IID('{081252CB-D855-48B9-9D85-FA9A9981DF81}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Printer,
	]
	default_interface = _Printer

# This CoClass is known by the name 'Illustrator.PrinterInfo.CC.2017'
class PrinterInfo(CoClassBaseClass): # A CoClass
	# printer information
	CLSID = IID('{29FEE1EA-CD21-41A6-9340-6219E3E57BB7}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_PrinterInfo,
	]
	default_interface = _PrinterInfo

# This CoClass is known by the name 'Illustrator.RGBColor.CC.2017'
class RGBColor(CoClassBaseClass): # A CoClass
	# An RGB color specification
	CLSID = IID('{6707D262-70F2-423D-88E1-ADCE85B359CE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_RGBColor,
	]
	default_interface = _RGBColor

# This CoClass is known by the name 'Illustrator.RasterEffectOptions.CC.2017'
class RasterEffectOptions(CoClassBaseClass): # A CoClass
	# The document raster effects settings
	CLSID = IID('{F4FCC1A9-2D0B-4555-B48D-ADE421F10F54}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_RasterEffectOptions,
	]
	default_interface = _RasterEffectOptions

# This CoClass is known by the name 'Illustrator.RasterizeOptions.CC.2017'
class RasterizeOptions(CoClassBaseClass): # A CoClass
	# Options which may be supplied when rasterizing the artwork
	CLSID = IID('{FA4BF28E-9A94-4EE8-A050-74C8A54B107F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_RasterizeOptions,
	]
	default_interface = _RasterizeOptions

# This CoClass is known by the name 'Illustrator.Screen.CC.2017'
class Screen(CoClassBaseClass): # A CoClass
	# color separation screen
	CLSID = IID('{162B9894-C6F9-4E55-A6D9-BFD86B8BF4F5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_Screen,
	]
	default_interface = _Screen

# This CoClass is known by the name 'Illustrator.ScreenInfo.CC.2017'
class ScreenInfo(CoClassBaseClass): # A CoClass
	# Screen information
	CLSID = IID('{FB23AEC3-074E-4CE4-8FC7-2391BBF14140}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_ScreenInfo,
	]
	default_interface = _ScreenInfo

# This CoClass is known by the name 'Illustrator.ScreenSpotFunction.CC.2017'
class ScreenSpotFunction(CoClassBaseClass): # A CoClass
	# color separation screen spot function
	CLSID = IID('{0D7F382B-98D9-4834-AE8D-6A03017CB774}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_ScreenSpotFunction,
	]
	default_interface = _ScreenSpotFunction

# This CoClass is known by the name 'Illustrator.SpotColor.CC.2017'
class SpotColor(CoClassBaseClass): # A CoClass
	# Information about the spot color
	CLSID = IID('{00BAC15D-DEEB-47CE-B207-C0C72BC7718C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_SpotColor,
	]
	default_interface = _SpotColor

# This CoClass is known by the name 'Illustrator.TabStopInfo.CC.2017'
class TabStopInfo(CoClassBaseClass): # A CoClass
	# Tab stop information (returned by tab stops from a paragraph object)
	CLSID = IID('{F26D5AB0-8B1D-4BF2-87A7-4EC6B74B03EF}')
	coclass_sources = [
	]
	coclass_interfaces = [
		_TabStopInfo,
	]
	default_interface = _TabStopInfo

RecordMap = {
}

CLSIDToClassMap = {
	'{95CD20AA-AD72-11D3-B086-0010A4F5C335}' : _Application,
	'{95CD20AB-AD72-11D3-B086-0010A4F5C335}' : Document,
	'{95CD20AC-AD72-11D3-B086-0010A4F5C335}' : Layer,
	'{95CD20B1-AD72-11D3-B086-0010A4F5C335}' : _RGBColor,
	'{95CD20E3-AD72-11D3-B086-0010A4F5C335}' : CompoundPathItems,
	'{95CD20BE-AD72-11D3-B086-0010A4F5C335}' : CompoundPathItem,
	'{95CD20E1-AD72-11D3-B086-0010A4F5C335}' : PathItems,
	'{95CD20C0-AD72-11D3-B086-0010A4F5C335}' : PathItem,
	'{95CD20E2-AD72-11D3-B086-0010A4F5C335}' : PathPoints,
	'{95CD20C1-AD72-11D3-B086-0010A4F5C335}' : PathPoint,
	'{95CD20EB-AD72-11D3-B086-0010A4F5C335}' : Tags,
	'{95CD20BF-AD72-11D3-B086-0010A4F5C335}' : Tag,
	'{4C78DFB7-7A09-11D4-81A0-00C04F60ECCC}' : GraphItem,
	'{95CD20C6-AD72-11D3-B086-0010A4F5C335}' : GroupItem,
	'{95CD20DF-AD72-11D3-B086-0010A4F5C335}' : GroupItems,
	'{95CD20E0-AD72-11D3-B086-0010A4F5C335}' : PageItems,
	'{95CD20EC-AD72-11D3-B086-0010A4F5C335}' : RasterItems,
	'{95CD20C2-AD72-11D3-B086-0010A4F5C335}' : RasterItem,
	'{95CD20C9-AD72-11D3-B086-0010A4F5C335}' : _Matrix,
	'{95CD20C4-AD72-11D3-B086-0010A4F5C335}' : MeshItem,
	'{95CD20C3-AD72-11D3-B086-0010A4F5C335}' : PlacedItem,
	'{95CD20C5-AD72-11D3-B086-0010A4F5C335}' : PluginItem,
	'{4C78DFC0-7A09-11D4-81A0-00C04F60ECCE}' : TracingObject,
	'{4C78DFC0-7A09-11D4-81A0-00C04F60ECCD}' : TracingOptions,
	'{4C78DFC3-7A09-11D4-81A0-00C04F60ECCC}' : SymbolItem,
	'{4C78DFC0-7A09-11D4-81A0-00C04F60ECCC}' : Symbol,
	'{95CD20ED-AD72-11D3-B086-0010A4F5C335}' : PlacedItems,
	'{95CD20EE-AD72-11D3-B086-0010A4F5C335}' : MeshItems,
	'{95CD20EF-AD72-11D3-B086-0010A4F5C335}' : PluginItems,
	'{4C78DFB4-7A09-11D4-81A0-00C04F60ECCC}' : GraphItems,
	'{9157F2B0-D436-4AC6-9769-94DC89E6EC92}' : NonNativeItems,
	'{FC0A0BD3-5FFB-4301-A44F-F5B3ED181224}' : NonNativeItem,
	'{3CC63F1C-EA9C-4636-A16C-63808C42691E}' : TextFrames,
	'{F0692236-A49A-474D-9745-715426856760}' : TextFrame,
	'{8507C961-DE07-440E-A2D8-6D48247ABF79}' : Story,
	'{95CD20D0-AD72-11D3-B086-0010A4F5C335}' : TextRange,
	'{95CD20D5-AD72-11D3-B086-0010A4F5C335}' : Characters,
	'{95CD20D6-AD72-11D3-B086-0010A4F5C335}' : Words,
	'{95CD20D7-AD72-11D3-B086-0010A4F5C335}' : Lines,
	'{95CD20D8-AD72-11D3-B086-0010A4F5C335}' : Paragraphs,
	'{20899C07-06F0-4803-BD2A-4059F9764852}' : TextRanges,
	'{20899C08-06F0-4803-BD2A-4059F9764852}' : InsertionPoints,
	'{4C78DFE7-7A09-11D4-81A0-00C04F60ECCC}' : InsertionPoint,
	'{255CD590-0FBF-4345-94F5-871C4021D6BF}' : CharacterStyles,
	'{7C1FA60D-BF8F-4C43-B14C-77D842034966}' : CharacterStyle,
	'{4C78DFCD-7A09-11D4-81A0-00C04F60ECCC}' : CharacterAttributes,
	'{95CD20BC-AD72-11D3-B086-0010A4F5C335}' : TextFont,
	'{0E3BF58B-A0F2-4776-9CD0-279FCB26009E}' : ParagraphStyles,
	'{2D2A6B70-EA28-49AA-B7C0-3EEC671CBACC}' : ParagraphStyle,
	'{4C78DFCE-7A09-11D4-81A0-00C04F60ECCC}' : ParagraphAttributes,
	'{95CD20C8-AD72-11D3-B086-0010A4F5C335}' : TextPath,
	'{4C78DFC6-7A09-11D4-81A0-00C04F60ECCC}' : SymbolItems,
	'{4C78DFE9-7A09-11D4-81A0-00C04F60ECCC}' : LegacyTextItems,
	'{4C78DFE8-7A09-11D4-81A0-00C04F60ECCC}' : LegacyTextItem,
	'{95CD20DC-AD72-11D3-B086-0010A4F5C335}' : Layers,
	'{95CD20AD-AD72-11D3-B086-0010A4F5C335}' : View,
	'{4C78DFA5-7A09-11D4-81A0-00C04F60ECCC}' : DataSet,
	'{246086F4-6F43-4D2B-A0BA-3BFB0E484DDF}' : _RasterEffectOptions,
	'{091ADAF8-D422-11DB-8314-0800200C9A66}' : Artboards,
	'{30557E1D-A243-499D-84B8-6E170B36A1BD}' : Artboard,
	'{95CD20F0-AD72-11D3-B086-0010A4F5C335}' : Views,
	'{FF327E57-2EDA-4934-B3FD-CF470C62989D}' : EmbeddedItems,
	'{96C13549-5237-4492-8345-2DB9FB6512BE}' : EmbedItem,
	'{0E9E7B8C-BF29-4A10-9B1C-9F292FDAB07A}' : Stories,
	'{95CD20DA-AD72-11D3-B086-0010A4F5C335}' : Swatches,
	'{95CD20B8-AD72-11D3-B086-0010A4F5C335}' : Swatch,
	'{558EF46F-A352-4A0D-9B1C-A2F6118FE611}' : SwatchGroups,
	'{75482E9D-B225-419A-8187-EE9EB424138E}' : SwatchGroup,
	'{95CD20B5-AD72-11D3-B086-0010A4F5C335}' : Spot,
	'{95CD20DD-AD72-11D3-B086-0010A4F5C335}' : Gradients,
	'{95CD20AE-AD72-11D3-B086-0010A4F5C335}' : Gradient,
	'{95CD20DE-AD72-11D3-B086-0010A4F5C335}' : GradientStops,
	'{95CD20AF-AD72-11D3-B086-0010A4F5C335}' : GradientStop,
	'{95CD20E7-AD72-11D3-B086-0010A4F5C335}' : Patterns,
	'{95CD20B9-AD72-11D3-B086-0010A4F5C335}' : Pattern,
	'{95CD20D9-AD72-11D3-B086-0010A4F5C335}' : Spots,
	'{4C78DFC9-7A09-11D4-81A0-00C04F60ECCC}' : Symbols,
	'{95CD20E8-AD72-11D3-B086-0010A4F5C335}' : Brushes,
	'{95CD20BA-AD72-11D3-B086-0010A4F5C335}' : Brush,
	'{95CD20E9-AD72-11D3-B086-0010A4F5C335}' : GraphicStyles,
	'{95CD20BB-AD72-11D3-B086-0010A4F5C335}' : GraphicStyle,
	'{4C78DFA8-7A09-11D4-81A0-00C04F60ECCC}' : Variables,
	'{4C78DFA2-7A09-11D4-81A0-00C04F60ECCC}' : Variable,
	'{4C78DFAB-7A09-11D4-81A0-00C04F60ECCC}' : DataSets,
	'{4C78DFCC-7A09-11D4-81A0-00C04F60ECCC}' : Preferences,
	'{4C78DFBA-7A09-11D4-81A0-00C04F60ECCC}' : PhotoshopFileOptions,
	'{4C78DFBD-7A09-11D4-81A0-00C04F60ECCC}' : PDFFileOptions,
	'{AD865867-DED8-42D6-9BD8-D77533905975}' : AutoCADFileOptions,
	'{95CD20DB-AD72-11D3-B086-0010A4F5C335}' : Documents,
	'{95CD20EA-AD72-11D3-B086-0010A4F5C335}' : TextFonts,
	'{B1607D7C-2EA8-41B0-977A-F5B0A36DF932}' : _DocumentPreset,
	'{95CD2C09-AD72-11D3-B086-0010A4F5C335}' : _PPDFileInfo,
	'{60E764BB-CBEE-421F-B706-D228072EBB89}' : _OpenOptions,
	'{500C9AF9-AA54-4941-B544-132E4D285938}' : _FXGSaveOptions,
	'{95CD20A7-AD72-11D3-B086-0010A4F5C335}' : _EPSSaveOptions,
	'{95CD20A8-AD72-11D3-B086-0010A4F5C335}' : _PDFSaveOptions,
	'{95CD2C12-AD72-11D3-B086-0010A4F5C335}' : _PrintFlattenerOptions,
	'{95CD20A9-AD72-11D3-B086-0010A4F5C335}' : _IllustratorSaveOptions,
	'{95CD20CA-AD72-11D3-B086-0010A4F5C335}' : _ExportOptionsJPEG,
	'{95CD20CB-AD72-11D3-B086-0010A4F5C335}' : _ExportOptionsPNG8,
	'{95CD20CC-AD72-11D3-B086-0010A4F5C335}' : _ExportOptionsPNG24,
	'{95CD20B1-AD72-11D3-B086-0010A7F5C335}' : _Dimensions,
	'{95CD20CD-AD72-11D3-B086-0010A4F5C335}' : _ExportOptionsGIF,
	'{A07B43A9-0201-4369-A1B5-8A33C8A0BB23}' : _ExportOptionsPhotoshop,
	'{95CD20CF-AD72-11D3-B086-0010A4F5C335}' : _ExportOptionsSVG,
	'{4C78DF9F-7A09-11D4-81A0-00C04F60ECCE}' : _ExportOptionsWebOptimizedSVG,
	'{4C78DF9F-7A09-11D4-81A0-00C04F60ECCC}' : _ExportOptionsFlash,
	'{AD25A97A-80BC-4D6A-9E61-7E288DE977CA}' : _ExportOptionsAutoCAD,
	'{2A8F3C5F-B4E3-45BB-89CB-93F062B4F9F1}' : _ExportOptionsTIFF,
	'{57EDB0EB-8F86-4898-AA88-5D6F47DEE239}' : _LabColor,
	'{95CD20B2-AD72-11D3-B086-0010A4F5C335}' : _CMYKColor,
	'{95CD20B3-AD72-11D3-B086-0010A4F5C335}' : _GrayColor,
	'{4C78DFE6-7A09-11D4-81A0-00C04F60ECCC}' : _NoColor,
	'{95CD20B4-AD72-11D3-B086-0010A4F5C335}' : _SpotColor,
	'{95CD20B6-AD72-11D3-B086-0010A4F5C335}' : _PatternColor,
	'{95CD20B7-AD72-11D3-B086-0010A4F5C335}' : _GradientColor,
	'{E380AAF5-61BF-44C2-B3D2-00D631CE879D}' : _TabStopInfo,
	'{95CD2C0B-AD72-11D3-B086-0010A4F5C335}' : _Printer,
	'{95CD2C08-AD72-11D3-B086-0010A4F5C335}' : _PrinterInfo,
	'{95CD2C0C-AD72-11D3-B086-0010A4F5C335}' : _PPDFile,
	'{95CD2C0D-AD72-11D3-B086-0010A4F5C335}' : _Paper,
	'{95CD2C0A-AD72-11D3-B086-0010A4F5C335}' : _PaperInfo,
	'{95CD2C0E-AD72-11D3-B086-0010A4F5C335}' : _Screen,
	'{95CD2C0F-AD72-11D3-B086-0010A4F5C335}' : _ScreenInfo,
	'{95CD2C14-AD72-11D3-B086-0010A4F5C335}' : _ScreenSpotFunction,
	'{95CD2C10-AD72-11D3-B086-0010A4F5C335}' : _Ink,
	'{95CD2C11-AD72-11D3-B086-0010A4F5C335}' : _InkInfo,
	'{95CD2C00-AD72-11D3-B086-0010A4F5C335}' : _PrintOptions,
	'{95CD2C15-AD72-11D3-B086-0010A4F5C335}' : _PrintPaperOptions,
	'{95CD2C01-AD72-11D3-B086-0010A4F5C335}' : _PrintJobOptions,
	'{95CD2C02-AD72-11D3-B086-0010A4F5C335}' : _PrintColorSeparationOptions,
	'{95CD2C03-AD72-11D3-B086-0010A4F5C335}' : _PrintCoordinateOptions,
	'{95CD2C04-AD72-11D3-B086-0010A4F5C335}' : _PrintPageMarksOptions,
	'{95CD2C05-AD72-11D3-B086-0010A4F5C335}' : _PrintFontOptions,
	'{95CD2C06-AD72-11D3-B086-0010A4F5C335}' : _PrintPostScriptOptions,
	'{95CD2C07-AD72-11D3-B086-0010A4F5C335}' : _PrintColorManagementOptions,
	'{4C78DFEB-7A09-11D4-81A0-00C04F60ECCC}' : _ImageCaptureOptions,
	'{196F9F57-2023-4C2F-8662-9C20F9D6DE7A}' : _RasterizeOptions,
	'{0FA36670-F0BC-48C0-AD25-6CF62CAD3A31}' : Application,
	'{F95B83D1-94FC-4AF6-99B0-9094BE3AB899}' : OpenOptions,
	'{8DA7F9C4-7E22-46BD-BA1D-5517A9F0CD18}' : FXGSaveOptions,
	'{F07FD4A3-5651-47DA-AC33-91BC06403816}' : EPSSaveOptions,
	'{695B5492-AC6A-479A-A2B1-E8AE9DDE5B40}' : PDFSaveOptions,
	'{5C9DB812-A552-4513-8C6B-3D21EFC42605}' : IllustratorSaveOptions,
	'{E580BAB8-2188-4312-A007-7449839ACF29}' : Matrix,
	'{4C1581E0-3BA8-4CE6-83FC-34EF5F2A9F40}' : ExportOptionsJPEG,
	'{ECF0C759-F01B-4B3B-8922-541C1C163DF3}' : ExportOptionsPNG8,
	'{668E6292-D51A-4628-9800-4817A6762DF3}' : ExportOptionsPNG24,
	'{46E4F107-315D-4BDF-BE66-4E33D9596A9A}' : ExportOptionsGIF,
	'{1CC2A29F-5B2C-4359-9728-0D1771BDE2B1}' : ExportOptionsPhotoshop,
	'{8930E841-DD0D-47EB-ACB1-8A37AFDD5A2A}' : ExportOptionsSVG,
	'{FCB10B56-8002-46AE-A70D-D02783FFA353}' : ExportOptionsWebOptimizedSVG,
	'{09534ADA-D2A2-45EB-BD90-8E4D391D306B}' : ExportOptionsFlash,
	'{D678C828-971A-4759-8A5D-3FF12C221A22}' : ExportOptionsAutoCAD,
	'{A07D1206-AB5A-4BB1-9207-AEBA31A2D652}' : ExportOptionsTIFF,
	'{EF57A9D6-A4A8-4136-94C8-8C707F392A92}' : LabColor,
	'{40A7C4A8-EFD2-43A8-806F-5B0CCE61DCE6}' : Dimensions,
	'{6707D262-70F2-423D-88E1-ADCE85B359CE}' : RGBColor,
	'{9AFB43D8-2ABA-4DE9-A3E1-617AAA863C22}' : CMYKColor,
	'{2FEEBDFA-68E5-49AE-BE7B-1A97F09DF8F9}' : GrayColor,
	'{013C465C-6000-40C3-B7A6-B236B53A672D}' : NoColor,
	'{00BAC15D-DEEB-47CE-B207-C0C72BC7718C}' : SpotColor,
	'{F493FD6F-9E65-4AE4-AED9-AFDA9CF7F3ED}' : PatternColor,
	'{B2FE80F4-9612-48F9-87AD-B79A905BCBFC}' : GradientColor,
	'{F26D5AB0-8B1D-4BF2-87A7-4EC6B74B03EF}' : TabStopInfo,
	'{081252CB-D855-48B9-9D85-FA9A9981DF81}' : Printer,
	'{29FEE1EA-CD21-41A6-9340-6219E3E57BB7}' : PrinterInfo,
	'{D2DBC561-0DCE-4141-8FE8-2ECA346CED3E}' : PPDFile,
	'{EBE15492-1925-4BA2-A987-8F77CB15FCF0}' : PPDFileInfo,
	'{99044697-4AD8-4B63-A3D8-BBFE4610C844}' : Paper,
	'{2D6EDDEF-62F9-4D38-A0B5-68B576721018}' : PaperInfo,
	'{162B9894-C6F9-4E55-A6D9-BFD86B8BF4F5}' : Screen,
	'{FB23AEC3-074E-4CE4-8FC7-2391BBF14140}' : ScreenInfo,
	'{0D7F382B-98D9-4834-AE8D-6A03017CB774}' : ScreenSpotFunction,
	'{E417157D-29E4-408A-B742-0F908DF8C745}' : Ink,
	'{F4A69A15-7701-4DF4-948D-9E7FBACC0787}' : InkInfo,
	'{E2D4A432-9E16-41E6-BCA5-062890269CD1}' : DocumentPreset,
	'{76543789-87FE-43E4-B70C-17089F44F447}' : PrintOptions,
	'{297CFCE2-7884-400D-AEB1-BAB1BB3CC897}' : PrintPaperOptions,
	'{A816141F-0C6E-4F89-846A-0F596AEDAF9F}' : PrintJobOptions,
	'{C43D57E6-B94A-4DAD-BEA4-153159D34529}' : PrintColorSeparationOptions,
	'{42A65455-5260-4F3D-A4FE-33B2C5BF839C}' : PrintCoordinateOptions,
	'{D41CD84C-C090-4B8F-A7CD-44CCF26C254E}' : PrintPageMarksOptions,
	'{FDB1EDFA-8339-4630-A515-6ACFD4102EDD}' : PrintFontOptions,
	'{F58B5314-DC1D-4283-90C4-2248F6E60C6C}' : PrintPostScriptOptions,
	'{EBAD60C2-68F6-4D26-A3A2-0AFD276418AC}' : PrintColorManagementOptions,
	'{C3BF40DE-EDA0-493B-924A-42FD00D36CEB}' : PrintFlattenerOptions,
	'{BD1B34AB-D76C-4DA1-A134-086969C4EDEF}' : ImageCaptureOptions,
	'{F4FCC1A9-2D0B-4555-B48D-ADE421F10F54}' : RasterEffectOptions,
	'{FA4BF28E-9A94-4EE8-A050-74C8A54B107F}' : RasterizeOptions,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
}


NamesToIIDMap = {
	'_Application' : '{95CD20AA-AD72-11D3-B086-0010A4F5C335}',
	'Document' : '{95CD20AB-AD72-11D3-B086-0010A4F5C335}',
	'Layer' : '{95CD20AC-AD72-11D3-B086-0010A4F5C335}',
	'_RGBColor' : '{95CD20B1-AD72-11D3-B086-0010A4F5C335}',
	'CompoundPathItems' : '{95CD20E3-AD72-11D3-B086-0010A4F5C335}',
	'CompoundPathItem' : '{95CD20BE-AD72-11D3-B086-0010A4F5C335}',
	'PathItems' : '{95CD20E1-AD72-11D3-B086-0010A4F5C335}',
	'PathItem' : '{95CD20C0-AD72-11D3-B086-0010A4F5C335}',
	'PathPoints' : '{95CD20E2-AD72-11D3-B086-0010A4F5C335}',
	'PathPoint' : '{95CD20C1-AD72-11D3-B086-0010A4F5C335}',
	'Tags' : '{95CD20EB-AD72-11D3-B086-0010A4F5C335}',
	'Tag' : '{95CD20BF-AD72-11D3-B086-0010A4F5C335}',
	'GraphItem' : '{4C78DFB7-7A09-11D4-81A0-00C04F60ECCC}',
	'GroupItem' : '{95CD20C6-AD72-11D3-B086-0010A4F5C335}',
	'GroupItems' : '{95CD20DF-AD72-11D3-B086-0010A4F5C335}',
	'PageItems' : '{95CD20E0-AD72-11D3-B086-0010A4F5C335}',
	'RasterItems' : '{95CD20EC-AD72-11D3-B086-0010A4F5C335}',
	'RasterItem' : '{95CD20C2-AD72-11D3-B086-0010A4F5C335}',
	'_Matrix' : '{95CD20C9-AD72-11D3-B086-0010A4F5C335}',
	'MeshItem' : '{95CD20C4-AD72-11D3-B086-0010A4F5C335}',
	'PlacedItem' : '{95CD20C3-AD72-11D3-B086-0010A4F5C335}',
	'PluginItem' : '{95CD20C5-AD72-11D3-B086-0010A4F5C335}',
	'TracingObject' : '{4C78DFC0-7A09-11D4-81A0-00C04F60ECCE}',
	'TracingOptions' : '{4C78DFC0-7A09-11D4-81A0-00C04F60ECCD}',
	'SymbolItem' : '{4C78DFC3-7A09-11D4-81A0-00C04F60ECCC}',
	'Symbol' : '{4C78DFC0-7A09-11D4-81A0-00C04F60ECCC}',
	'PlacedItems' : '{95CD20ED-AD72-11D3-B086-0010A4F5C335}',
	'MeshItems' : '{95CD20EE-AD72-11D3-B086-0010A4F5C335}',
	'PluginItems' : '{95CD20EF-AD72-11D3-B086-0010A4F5C335}',
	'GraphItems' : '{4C78DFB4-7A09-11D4-81A0-00C04F60ECCC}',
	'NonNativeItems' : '{9157F2B0-D436-4AC6-9769-94DC89E6EC92}',
	'NonNativeItem' : '{FC0A0BD3-5FFB-4301-A44F-F5B3ED181224}',
	'TextFrames' : '{3CC63F1C-EA9C-4636-A16C-63808C42691E}',
	'TextFrame' : '{F0692236-A49A-474D-9745-715426856760}',
	'Story' : '{8507C961-DE07-440E-A2D8-6D48247ABF79}',
	'TextRange' : '{95CD20D0-AD72-11D3-B086-0010A4F5C335}',
	'Characters' : '{95CD20D5-AD72-11D3-B086-0010A4F5C335}',
	'Words' : '{95CD20D6-AD72-11D3-B086-0010A4F5C335}',
	'Lines' : '{95CD20D7-AD72-11D3-B086-0010A4F5C335}',
	'Paragraphs' : '{95CD20D8-AD72-11D3-B086-0010A4F5C335}',
	'TextRanges' : '{20899C07-06F0-4803-BD2A-4059F9764852}',
	'InsertionPoints' : '{20899C08-06F0-4803-BD2A-4059F9764852}',
	'InsertionPoint' : '{4C78DFE7-7A09-11D4-81A0-00C04F60ECCC}',
	'CharacterStyles' : '{255CD590-0FBF-4345-94F5-871C4021D6BF}',
	'CharacterStyle' : '{7C1FA60D-BF8F-4C43-B14C-77D842034966}',
	'CharacterAttributes' : '{4C78DFCD-7A09-11D4-81A0-00C04F60ECCC}',
	'TextFont' : '{95CD20BC-AD72-11D3-B086-0010A4F5C335}',
	'ParagraphStyles' : '{0E3BF58B-A0F2-4776-9CD0-279FCB26009E}',
	'ParagraphStyle' : '{2D2A6B70-EA28-49AA-B7C0-3EEC671CBACC}',
	'ParagraphAttributes' : '{4C78DFCE-7A09-11D4-81A0-00C04F60ECCC}',
	'TextPath' : '{95CD20C8-AD72-11D3-B086-0010A4F5C335}',
	'SymbolItems' : '{4C78DFC6-7A09-11D4-81A0-00C04F60ECCC}',
	'LegacyTextItems' : '{4C78DFE9-7A09-11D4-81A0-00C04F60ECCC}',
	'LegacyTextItem' : '{4C78DFE8-7A09-11D4-81A0-00C04F60ECCC}',
	'Layers' : '{95CD20DC-AD72-11D3-B086-0010A4F5C335}',
	'View' : '{95CD20AD-AD72-11D3-B086-0010A4F5C335}',
	'DataSet' : '{4C78DFA5-7A09-11D4-81A0-00C04F60ECCC}',
	'_RasterEffectOptions' : '{246086F4-6F43-4D2B-A0BA-3BFB0E484DDF}',
	'Artboards' : '{091ADAF8-D422-11DB-8314-0800200C9A66}',
	'Artboard' : '{30557E1D-A243-499D-84B8-6E170B36A1BD}',
	'Views' : '{95CD20F0-AD72-11D3-B086-0010A4F5C335}',
	'EmbeddedItems' : '{FF327E57-2EDA-4934-B3FD-CF470C62989D}',
	'EmbedItem' : '{96C13549-5237-4492-8345-2DB9FB6512BE}',
	'Stories' : '{0E9E7B8C-BF29-4A10-9B1C-9F292FDAB07A}',
	'Swatches' : '{95CD20DA-AD72-11D3-B086-0010A4F5C335}',
	'Swatch' : '{95CD20B8-AD72-11D3-B086-0010A4F5C335}',
	'SwatchGroups' : '{558EF46F-A352-4A0D-9B1C-A2F6118FE611}',
	'SwatchGroup' : '{75482E9D-B225-419A-8187-EE9EB424138E}',
	'Spot' : '{95CD20B5-AD72-11D3-B086-0010A4F5C335}',
	'Gradients' : '{95CD20DD-AD72-11D3-B086-0010A4F5C335}',
	'Gradient' : '{95CD20AE-AD72-11D3-B086-0010A4F5C335}',
	'GradientStops' : '{95CD20DE-AD72-11D3-B086-0010A4F5C335}',
	'GradientStop' : '{95CD20AF-AD72-11D3-B086-0010A4F5C335}',
	'Patterns' : '{95CD20E7-AD72-11D3-B086-0010A4F5C335}',
	'Pattern' : '{95CD20B9-AD72-11D3-B086-0010A4F5C335}',
	'Spots' : '{95CD20D9-AD72-11D3-B086-0010A4F5C335}',
	'Symbols' : '{4C78DFC9-7A09-11D4-81A0-00C04F60ECCC}',
	'Brushes' : '{95CD20E8-AD72-11D3-B086-0010A4F5C335}',
	'Brush' : '{95CD20BA-AD72-11D3-B086-0010A4F5C335}',
	'GraphicStyles' : '{95CD20E9-AD72-11D3-B086-0010A4F5C335}',
	'GraphicStyle' : '{95CD20BB-AD72-11D3-B086-0010A4F5C335}',
	'Variables' : '{4C78DFA8-7A09-11D4-81A0-00C04F60ECCC}',
	'Variable' : '{4C78DFA2-7A09-11D4-81A0-00C04F60ECCC}',
	'DataSets' : '{4C78DFAB-7A09-11D4-81A0-00C04F60ECCC}',
	'Preferences' : '{4C78DFCC-7A09-11D4-81A0-00C04F60ECCC}',
	'PhotoshopFileOptions' : '{4C78DFBA-7A09-11D4-81A0-00C04F60ECCC}',
	'PDFFileOptions' : '{4C78DFBD-7A09-11D4-81A0-00C04F60ECCC}',
	'AutoCADFileOptions' : '{AD865867-DED8-42D6-9BD8-D77533905975}',
	'Documents' : '{95CD20DB-AD72-11D3-B086-0010A4F5C335}',
	'TextFonts' : '{95CD20EA-AD72-11D3-B086-0010A4F5C335}',
	'_DocumentPreset' : '{B1607D7C-2EA8-41B0-977A-F5B0A36DF932}',
	'_PPDFileInfo' : '{95CD2C09-AD72-11D3-B086-0010A4F5C335}',
	'_OpenOptions' : '{60E764BB-CBEE-421F-B706-D228072EBB89}',
	'_FXGSaveOptions' : '{500C9AF9-AA54-4941-B544-132E4D285938}',
	'_EPSSaveOptions' : '{95CD20A7-AD72-11D3-B086-0010A4F5C335}',
	'_PDFSaveOptions' : '{95CD20A8-AD72-11D3-B086-0010A4F5C335}',
	'_PrintFlattenerOptions' : '{95CD2C12-AD72-11D3-B086-0010A4F5C335}',
	'_IllustratorSaveOptions' : '{95CD20A9-AD72-11D3-B086-0010A4F5C335}',
	'_ExportOptionsJPEG' : '{95CD20CA-AD72-11D3-B086-0010A4F5C335}',
	'_ExportOptionsPNG8' : '{95CD20CB-AD72-11D3-B086-0010A4F5C335}',
	'_ExportOptionsPNG24' : '{95CD20CC-AD72-11D3-B086-0010A4F5C335}',
	'_Dimensions' : '{95CD20B1-AD72-11D3-B086-0010A7F5C335}',
	'_ExportOptionsGIF' : '{95CD20CD-AD72-11D3-B086-0010A4F5C335}',
	'_ExportOptionsPhotoshop' : '{A07B43A9-0201-4369-A1B5-8A33C8A0BB23}',
	'_ExportOptionsSVG' : '{95CD20CF-AD72-11D3-B086-0010A4F5C335}',
	'_ExportOptionsWebOptimizedSVG' : '{4C78DF9F-7A09-11D4-81A0-00C04F60ECCE}',
	'_ExportOptionsFlash' : '{4C78DF9F-7A09-11D4-81A0-00C04F60ECCC}',
	'_ExportOptionsAutoCAD' : '{AD25A97A-80BC-4D6A-9E61-7E288DE977CA}',
	'_ExportOptionsTIFF' : '{2A8F3C5F-B4E3-45BB-89CB-93F062B4F9F1}',
	'_LabColor' : '{57EDB0EB-8F86-4898-AA88-5D6F47DEE239}',
	'_CMYKColor' : '{95CD20B2-AD72-11D3-B086-0010A4F5C335}',
	'_GrayColor' : '{95CD20B3-AD72-11D3-B086-0010A4F5C335}',
	'_NoColor' : '{4C78DFE6-7A09-11D4-81A0-00C04F60ECCC}',
	'_SpotColor' : '{95CD20B4-AD72-11D3-B086-0010A4F5C335}',
	'_PatternColor' : '{95CD20B6-AD72-11D3-B086-0010A4F5C335}',
	'_GradientColor' : '{95CD20B7-AD72-11D3-B086-0010A4F5C335}',
	'_TabStopInfo' : '{E380AAF5-61BF-44C2-B3D2-00D631CE879D}',
	'_Printer' : '{95CD2C0B-AD72-11D3-B086-0010A4F5C335}',
	'_PrinterInfo' : '{95CD2C08-AD72-11D3-B086-0010A4F5C335}',
	'_PPDFile' : '{95CD2C0C-AD72-11D3-B086-0010A4F5C335}',
	'_Paper' : '{95CD2C0D-AD72-11D3-B086-0010A4F5C335}',
	'_PaperInfo' : '{95CD2C0A-AD72-11D3-B086-0010A4F5C335}',
	'_Screen' : '{95CD2C0E-AD72-11D3-B086-0010A4F5C335}',
	'_ScreenInfo' : '{95CD2C0F-AD72-11D3-B086-0010A4F5C335}',
	'_ScreenSpotFunction' : '{95CD2C14-AD72-11D3-B086-0010A4F5C335}',
	'_Ink' : '{95CD2C10-AD72-11D3-B086-0010A4F5C335}',
	'_InkInfo' : '{95CD2C11-AD72-11D3-B086-0010A4F5C335}',
	'_PrintOptions' : '{95CD2C00-AD72-11D3-B086-0010A4F5C335}',
	'_PrintPaperOptions' : '{95CD2C15-AD72-11D3-B086-0010A4F5C335}',
	'_PrintJobOptions' : '{95CD2C01-AD72-11D3-B086-0010A4F5C335}',
	'_PrintColorSeparationOptions' : '{95CD2C02-AD72-11D3-B086-0010A4F5C335}',
	'_PrintCoordinateOptions' : '{95CD2C03-AD72-11D3-B086-0010A4F5C335}',
	'_PrintPageMarksOptions' : '{95CD2C04-AD72-11D3-B086-0010A4F5C335}',
	'_PrintFontOptions' : '{95CD2C05-AD72-11D3-B086-0010A4F5C335}',
	'_PrintPostScriptOptions' : '{95CD2C06-AD72-11D3-B086-0010A4F5C335}',
	'_PrintColorManagementOptions' : '{95CD2C07-AD72-11D3-B086-0010A4F5C335}',
	'_ImageCaptureOptions' : '{4C78DFEB-7A09-11D4-81A0-00C04F60ECCC}',
	'_RasterizeOptions' : '{196F9F57-2023-4C2F-8662-9C20F9D6DE7A}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

