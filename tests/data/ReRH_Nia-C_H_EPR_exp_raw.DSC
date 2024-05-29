#DESC	1.2 * DESCRIPTOR INFORMATION ***********************
*
*	Dataset Type and Format:
*
DSRC	MAN
BSEQ	BIG
IKKF	REAL
XTYP	IDX
YTYP	NODATA
ZTYP	NODATA
*
*	Item Formats:
*
IRFMT	D
*
*	Data Ranges and Resolutions:
*
XPTS	800
XMIN	2400.000000
XWID	1598.000000
*
*	Documentational Text:
*
TITL	'RHStop lyo H2red NRVS 500uM pH 8, 80K, Mod 10G, 1mW, 4sc, 1600:1'
IRNAM	'Intensity'
XNAM	'Field'
IRUNI	''
XUNI	'G'
*
************************************************************
*
#SPL	1.2 * STANDARD PARAMETER LAYER
*
OPER    xuser
DATE    05/19/17
TIME    16:46:53
CMNT    
SAMP    
SFOR    
STAG    C
EXPT    CW
OXS1    IADC
AXS1    B0VL
AXS2    NONE
AXS3    
A1CT    0.32
A1SW    0.16
MWFQ    9.300992e+09
MWPW    0.001002
AVGS    4
SPTP    0.08128
RCAG    60
RCHM    1
B0MA    0.001
B0MF    100000
RCPH    0.0
RCOF    0.0
A1RS    800
RCTC    0.08192
*
************************************************************
*
#DSL	1.0 * DEVICE SPECIFIC LAYER
*
.DVC     acqStart, 1.0
.DVC     ezcw, 1.0
MetalIonsDef       False
OrgRadicalsDef     False
.DVC     fieldCtrl, 1.0
AllegroMode        True
CenterField        3200.00 G
Delay              0.0 s
FieldFlyback       On
FieldWait          Wait LED off
GFactor            2.000000
MeasuringHall      False
SetToSampleG       False
StaticFieldMon     2400.000 G
SweepDirection     Up
SweepWidth         1600.0 G
.DVC     fieldSweep, 1.0
.DVC     freqCounter, 1.0
FrequencyMon       9.300992 GHz
QMonitBridge       On
.DVC     mwBridge, 1.0
AcqFineTuning      Never
AcqScanFTuning     Off
AcqSliceFTuning    Off
BridgeCalib        60.6
Power              1.002 mW
PowerAtten         23.0 dB
QValue             6600
.DVC     recorder, 1.0
BaselineCorr       On
NbScansAcc         4
NbScansDone        4
NbScansToDo        4
ReplaceMode        Off
SmoothMode         Manual
SmoothPoints       0
.DVC     scanEnd, 1.0
.DVC     signalChannel, 1.0
AFCTrap            True
AllegroMode        True
AllowShortCt       False
Calibrated         True
ConvTime           81.28 ms
DModDetectSCT      First
DualDetect         OFF
EliDelay           1.0 us
EnableImag         Disable
ExtLockIn          False
ExtTrigger         False
Gain               60 dB
Harmonic           1
HighPass           True
Integrator         False
IsCalibExp         False
ModAmp             10.000 G
ModFreq            100.00 kHz
ModPhase           0.0
ModResol           5
Offset             0.0 %
QuadMode           False
Resolution         800
Resonator          1
SctNorm            False
SctRevision        Allegro
SpuExtension       False
SweepTime          65.02 s
TimeConst          81.92 ms
TimeExp            False
TuneCaps           40
*
************************************************************
*
#MHL	1.0 * MANIPULATION HISTORY LAYER by BRUKER
*
*
*       Input Dataset:
*
SOURCE_PRIM
'RHStop lyo H2red NRVS 500uM pH 8, 80K, Mod 10G, 1mW, 4sc, 1600'
END_SOURCE_PRIM
*
*       Input Dataset:
*
SOURCE_SCND
  *
  SOURCE
  'RHStop lyo H2red NRVS 500uM pH 8, 80K, Mod 10G, 1mW, 4sc, 1600'
  END_SOURCE
  SELECT  'qualiRegions'
  'qualiRegions'
  END_SELECT
  PROCESS 'prFit9thOrder'
  REPORT
                  a = -2.32463e-19
                  b = 6.67438e-15 
                  c = -8.47992e-11
                  d = 6.25714e-07 
                  e = -0.0029549  
                  f = 9.26139     
                  g = -19265      
                  h = 2.56464e+07 
                  i = -1.98269e+10
                  j = 6.78213e+12 
  reduced chi-square = 6.469e+09
  END_REPORT
END_SOURCE_SCND
*
*       Selection:
*
SELECT  'qualiRegions'
'qualiRegions'
END_SELECT
*
*       Process:
*
PROCESS 'prDiff'
*
*       Parameter:
*
PAR_VAL Gain(Sec.) =  1.000e+00
PAR_VAL x-Shift(Sec.) =  0.000e+00
PAR_VAL x-Stretch(Sec.) =  1.000e+00
MDATE   06/15/17 08:50:45
*
************************************************************
