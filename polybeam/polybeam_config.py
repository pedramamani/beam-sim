from pathlib import Path
from os import path

c = 2.9979E8
i = complex(0, 1)
π = 3.1416
μ0 = 1.2566E-6

fν = 16
fx = 16
DEFAULT_Nν = 2 ** 8
DEFAULT_Nx = 2 ** 16
DEFAULT_I0 = 1E12

ASSETS_DIR = Path(path.dirname(__file__)) / 'polybeam_assets'
WISDOM_FILE = 'pyfftw_wisdom_{}'


class ERROR:
    TRANSFORM = 'Transform failed since some of the cross-sections are not planar.'
    SECTION = 'Cannot plot since some of the cross-sections are not planar.'
    DISPERSION = 'Some frequency components don\'t have a first-order diffraction for these grating parameters.'


class PLOT:
    POSITION_LABEL = 'x (mm)'
    POSITION_SCALE = 1E3

    FREQUENCY_LABEL = 'ν (THz)'
    FREQUENCY_SCALE = 1E-12

    TIME_LABEL = 't (fs)'
    TIME_SCALE = 1E15

    PHASE_TITLE = 'Phase Profile'
    PHASE_LABEL = 'φ (rad)'

    AMPLITUDE_TITLE = 'Amplitude Profile'
    AMPLITUDE_LABEL = 'A (V/m)'
    AMPLITUDE_SCALE = 1E0

    INTENSITY_TITLE = 'Intensity Profile'
    INTENSITY_LABEL = 'I (GW/m²)'
    INTENSITY_SCALE = 1E-9

    @staticmethod
    def SAVE_TIME(title): return '-'.join(title.lower().split() + ['time'])

    @staticmethod
    def SAVE_FREQ(title): return '-'.join(title.lower().split() + ['freq'])
