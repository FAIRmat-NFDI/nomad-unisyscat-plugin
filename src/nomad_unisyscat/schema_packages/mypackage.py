import os
from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

from nomad.config import config
from nomad.datamodel.data import Schema, EntryData
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import Quantity, SchemaPackage
from nomad.datamodel.metainfo.basesections import Measurement

from nomad.datamodel.metainfo.plot import PlotSection, PlotlyFigure
import plotly.express as px

configuration = config.get_plugin_entry_point(
    'nomad_unisyscat.schema_packages:mypackage'
)

m_package = SchemaPackage()

class NVRSpectroscopy(Measurement, PlotSection, EntryData):
    measurements_data_file = Quantity(
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
            default='Nuclear resonance vibrational spectroscopy',
        ),
    )

    def normalize(self, archive, logger):
        super(NVRSpectroscopy, self).normalize(archive, logger)
        if self.measurements_data_file is None:
            return

        if (self.measurements_data_file is not None) and (
            os.path.splitext(self.measurement_data_file)[-1] != '.dat'
        ):
            raise ValueError('Unsupported file format. Only .dat file')

        if self.measurement_data_file.endswith('.dat'):
            with archive.m_context.raw_file(self.measurement_data_file) as f:
                import pandas as pd

                col_names = ['wavenumber, cm-1', '57Fe PVDOS']
                data = pd.read_csv(f.name, header=None, names=col_names)

        self.figures = []
        fig = px.line(x=data['wavenumber, cm-1'], y=data['57Fe PVDOS'])
        fig.update_xaxes(title_text=col_names[0])
        fig.update_yaxes(title_text=col_names[1])
        self.figures.append(PlotlyFigure(label='NVPS', figure=fig.to_plotly_json()))


class MySchema(Schema):
    name = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    message = Quantity(type=str)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        logger.info('MySchema.normalize', parameter=configuration.parameter)
        self.message = f'Hello {self.name}!'


m_package.__init_metainfo__()