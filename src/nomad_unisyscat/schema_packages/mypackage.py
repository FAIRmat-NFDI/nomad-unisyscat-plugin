import os
from typing import (
    TYPE_CHECKING,
)

import numpy as np

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

import plotly.express as px
from nomad.config import config
from nomad.datamodel.data import Schema
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.datamodel.metainfo.basesections import Measurement, MeasurementResult
from nomad.datamodel.metainfo.plot import PlotlyFigure, PlotSection
from nomad.metainfo import Quantity, SchemaPackage, Section

configuration = config.get_plugin_entry_point(
    'nomad_unisyscat.schema_packages:mypackage'
)

m_package = SchemaPackage()


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
        description='The count at each wavenumber value, dimensionless',
        a_plot={'x': 'array_index', 'y': 'intensity'},
    )
    wavenumber = Quantity(
        type=np.float64,
        shape=['*'],
        unit='1/cm',
        description='The wavenumber range of the sprectrum',
        a_plot={'x': 'array_index', 'y': 'wavenumber'},
    )


class NRVSpectroscopy(Measurement, PlotSection, Schema):
    measurement_data_file = Quantity(
        type=str,
        description="""
            experimental tab data file
            """,
        a_eln=dict(component='FileEditQuantity'),
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
        a_eln=dict(
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

        self.results.wavenumber = data['wavenumber, cm-1']
        self.results.intensity = data['57Fe PVDOS']

        self.figures = []

        fig = px.line(x=data['wavenumber, cm-1'], y=data['57Fe PVDOS'])
        fig.update_xaxes(title_text=col_names[0])
        fig.update_yaxes(title_text=col_names[1])
        self.figures.append(PlotlyFigure(label='NRVS', figure=fig.to_plotly_json()))

m_package.__init_metainfo__()
