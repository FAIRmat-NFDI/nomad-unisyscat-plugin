import os
from typing import (
    TYPE_CHECKING,
)

import numpy as np
from nomad.metainfo.metainfo import SubSection

if TYPE_CHECKING:
    pass

import plotly.express as px
from nomad.config import config
from nomad.datamodel.data import ArchiveSection, Schema
from nomad.datamodel.metainfo.annotations import ELNAnnotation
from nomad.datamodel.metainfo.basesections import Measurement, MeasurementResult
from nomad.datamodel.metainfo.plot import PlotlyFigure, PlotSection
from nomad.metainfo import Quantity, SchemaPackage, Section

configuration = config.get_plugin_entry_point(
    'nomad_unisyscat.schema_packages:mypackage'
)

m_package = SchemaPackage()


class EPRSettings(ArchiveSection):
    metal_ions_defined = Quantity(type=bool)
    organic_radicals_defined = Quantity(type=bool)
    allegro_mode = Quantity(type=bool)
    center_field = Quantity(type=float, unit='G')
    delay_time = Quantity(type=float, unit='s')
    field_flyback = Quantity(type=str)
    field_wait = Quantity(type=str)
    g_factor = Quantity(type=float)
    measuring_hall = Quantity(type=bool)
    set_to_sample_g = Quantity(type=bool)
    static_field_monitor = Quantity(type=float, unit='G')
    sweep_direction = Quantity(type=str)
    sweep_width = Quantity(type=float, unit='G')
    frequency_monitor = Quantity(type=float, unit='GHz')
    q_monitor_bridge = Quantity(type=bool)
    acquisition_fine_tuning = Quantity(type=str)
    acquisition_scan_fine_tuning = Quantity(type=str)
    acquisition_slice_fine_tuning = Quantity(type=str)
    bridge_calibration = Quantity(type=float)
    power_level = Quantity(type=float, unit='mW')
    power_attenuation = Quantity(type=float, unit='dB')
    q_value = Quantity(type=int)
    baseline_correction = Quantity(type=bool)
    number_of_scans_accumulated = Quantity(type=int)
    number_of_scans_done = Quantity(type=int)
    number_of_scans_to_do = Quantity(type=int)
    replace_mode = Quantity(type=str)
    smoothing_mode = Quantity(type=str)
    smoothing_points = Quantity(type=int)
    afc_trap = Quantity(type=bool)
    allow_short_circuit = Quantity(type=bool)
    calibrated = Quantity(type=bool)
    conversion_time = Quantity(type=float, unit='ms')
    demodulation_detection_sct = Quantity(type=str)
    dual_detection = Quantity(type=str)
    eliptical_delay = Quantity(type=float, unit='us')
    enable_imaginary = Quantity(type=str)
    external_lock_in = Quantity(type=bool)
    external_trigger = Quantity(type=bool)
    gain_level = Quantity(type=float, unit='dB')
    harmonic_level = Quantity(type=int)
    high_pass_filter = Quantity(type=bool)
    integrator_enabled = Quantity(type=bool)
    is_calibrated_experiment = Quantity(type=bool)
    modulation_amplitude = Quantity(type=float, unit='G')
    modulation_frequency = Quantity(type=float, unit='kHz')
    modulation_phase = Quantity(type=float)
    modulation_resolution = Quantity(type=int)
    offset_percentage = Quantity(type=float)
    quad_mode = Quantity(type=bool)
    resolution_value = Quantity(type=int)
    resonator_number = Quantity(type=int)
    sct_normalization = Quantity(type=bool)
    sct_revision = Quantity(type=str)
    spu_extension = Quantity(type=bool)
    sweep_time = Quantity(type=float, unit='s')
    time_constant = Quantity(type=float, unit='ms')
    time_exponential = Quantity(type=bool)
    tuning_capacitance = Quantity(type=int)

    def normalize(self, archive, logger) -> None:
        super().normalize(archive, logger)

        logger.info('Settings.normalize', parameter=configuration.parameter)


class EPRResults(MeasurementResult):
    field = Quantity(type=float, shape=['*'], unit='G')
    frequency = Quantity(type=float, unit='GHz')
    intensity = Quantity(type=float, shape=['*'])
    signal = Quantity(type=float)
    signal_error = Quantity(type=float)
    time = Quantity(type=float, unit='s')

    def normalize(self, archive, logger) -> None:
        super().normalize(archive, logger)

        logger.info('EPRResults.normalize', parameter=configuration.parameter)


class EPR(Measurement):
    method = Quantity(
        type=str,
        description='The method of the measurement.',
        default='Electron paramagnetic resonance (EPR)',
    )

    dsc_file = Quantity(
        type=str,
        description='The path to the DSC file.',
        shape=[],
        a_eln=dict(component='FileEditQuantity'),
    )
    dta_file = Quantity(
        type=str,
        description='The path to the DTA file.',
        shape=[],
        a_eln=dict(component='FileEditQuantity'),
    )
    settings = SubSection(
        section_def=EPRSettings,
        description="""
        The settings used for the EPR measurement.
        """,
    )
    results = Measurement.results.m_copy()
    results.section_def = EPRResults

    def normalize(self, archive, logger) -> None:
        super().normalize(archive, logger)
        if self.dsc_file is not None and self.dta_file is not None:
            from .epr_reader import parse_dta_dsc

            with archive.m_context.raw_file(self.dsc_file) as f:
                with archive.m_context.raw_file(self.dta_file) as g:
                    temp_dict = parse_dta_dsc(g.name, f.name)
            result = EPRResults()
            result.intensity = temp_dict['y_values']
            result.field = temp_dict['x_values']
            results = []
            results.append(result)
            self.results = results

            self.figures = []

            fig = px.line(x=temp_dict['x_values'], y=temp_dict['y_values'])
            fig.update_xaxes(title_text='Field (G)')
            fig.update_yaxes(title_text='Intensity')
            self.figures.append(PlotlyFigure(label='EPR', figure=fig.to_plotly_json()))

        logger.info('EPR.normalize', parameter=configuration.parameter)


class NRVSResult(MeasurementResult):
    m_def = Section()

    array_index = Quantity(
        type=np.float64,
        shape=['*'],
        description=(
            'A placeholder for the indices of vectorial quantities. '
            'Used as x-axis for plots within quantities.'
        ),
        a_display={'visible': False},
    )
    intensity = Quantity(
        type=np.float64,
        shape=['*'],
        unit='dimensionless',
        description='The 57Fe PVDOS count at each wavenumber value, dimensionless',
        a_plot={'x': 'array_index', 'y': 'intensity'},
    )
    wavenumber = Quantity(
        type=np.float64,
        shape=['*'],
        unit='1/cm',
        description='The wavenumber range of the spectrum',
        a_eln=ELNAnnotation(defaultDisplayUnit='1/cm'),
        a_plot={'x': 'array_index', 'y': 'wavenumber'},
    )


class NRVSpectroscopy(Measurement, PlotSection, Schema):
    measurement_data_file = Quantity(
        type=str,
        description="""
            experimental tab data file
            """,
        a_eln=ELNAnnotation(component='FileEditQuantity'),
        a_browser=dict(adaptor='RawFileAdaptor'),
    )

    # simulation_data_file = Quantity(
    #     type=str,
    #     description="""
    #         simulated tab data file
    #         """,
    #     a_eln=dict(component='FileEditQuantity'),
    #     a_browser=dict(adaptor='RawFileAdaptor')
    # )

    method = Quantity(
        type=str,
        description="""
            name of the method
            """,
        a_eln=ELNAnnotation(
            component='StringEditQuantity',
            default='nuclear resonance vibrational spectroscopy',
            props=dict(
                suggestions=[
                    'experimental nuclear resonance vibrational spectroscopy',
                    'simulated nuclear resonance vibrational spectroscopy',
                ]
            ),
        ),
    )

    results = Measurement.results.m_copy()
    results.section_def = NRVSResult

    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        if self.measurement_data_file is None:
            return

        if (self.measurement_data_file is not None) and (
            os.path.splitext(self.measurement_data_file)[-1] != '.dat'
        ):
            raise ValueError('Unsupported file format. Only .dat file')

        if self.measurement_data_file.endswith('.dat'):
            with archive.m_context.raw_file(self.measurement_data_file) as f:
                import pandas as pd

                col_names = ['wavenumber, cm-1', '57Fe PVDOS']
                data = pd.read_csv(f.name, header=None, names=col_names)
        result = NRVSResult()
        result.wavenumber = data['wavenumber, cm-1']
        result.intensity = data['57Fe PVDOS']
        results = []
        results.append(result)
        self.results = results

        self.figures = []

        fig = px.line(x=data['wavenumber, cm-1'], y=data['57Fe PVDOS'])
        fig.update_xaxes(title_text=col_names[0])
        fig.update_yaxes(title_text=col_names[1])
        self.figures.append(PlotlyFigure(label='NRVS', figure=fig.to_plotly_json()))


class IRResult(MeasurementResult):
    m_def = Section()

    array_index = Quantity(
        type=np.float64,
        shape=['*'],
        description=(
            'A placeholder for the indices of vectorial quantities. '
            'Used as x-axis for plots within quantities.'
        ),
        a_display={'visible': False},
    )
    intensity = Quantity(
        type=np.float64,
        shape=['*'],
        unit='dimensionless',
        description='The absorbance at each wavenumber value, dimensionless',
        a_plot={'x': 'array_index', 'y': 'intensity'},
    )
    wavenumber = Quantity(
        type=np.float64,
        shape=['*'],
        unit='1/cm',
        description='The wavenumber range of the spectrum',
        a_eln=ELNAnnotation(defaultDisplayUnit='1/cm'),
        a_plot={'x': 'array_index', 'y': 'wavenumber'},
    )


class IRSpectroscopy(Measurement, PlotSection, Schema):
    data_file = Quantity(
        type=str,
        description="""
            csv data file ending .dat
            """,
        a_eln=ELNAnnotation(component='FileEditQuantity'),
        a_browser=dict(adaptor='RawFileAdaptor'),
    )

    method = Quantity(
        type=str,
        description="""
            name of the method
            """,
        a_eln=ELNAnnotation(
            component='StringEditQuantity',
            default='infra red vibrational spectroscopy',
            props=dict(
                suggestions=[
                    'experimental IR vibrational spectroscopy',
                    'simulated IR vibrational spectroscopy',
                ]
            ),
        ),
    )

    results = Measurement.results.m_copy()
    results.section_def = IRResult

    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        if self.data_file is None:
            return

        if (self.data_file is not None) and (
            os.path.splitext(self.data_file)[-1] != '.dat'
        ):
            raise ValueError('Unsupported file format. Only .dat file')

        if self.data_file.endswith('.dat'):
            with archive.m_context.raw_file(self.data_file) as f:
                import pandas as pd

                col_names = ['wavenumber, cm-1', 'Absorbance']
                data = pd.read_csv(f.name, header=None, names=col_names)

        result = IRResult()
        result.wavenumber = data['wavenumber, cm-1']
        result.intensity = data['Absorbance']
        results = []
        results.append(result)
        self.results = results

        self.figures = []

        fig = px.line(x=data['wavenumber, cm-1'], y=data['Absorbance'])
        fig.update_xaxes(title_text=col_names[0])
        fig.update_yaxes(title_text=col_names[1])
        self.figures.append(PlotlyFigure(label='IR', figure=fig.to_plotly_json()))


m_package.__init_metainfo__()
