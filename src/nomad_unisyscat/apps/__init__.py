from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Column,
    Columns,
    FilterMenu,
    FilterMenus,
    Filters,
)

myapp = AppEntryPoint(
    name='UniSysCatApp',
    description='Explore UniSysCat example data.',
    app=App(
        label='UniSysCatApp',
        path='unisyscatapp',
        category='Use Cases',
        columns=Columns(
            selected=[
                'entry_name',
                'data.name#nomad_unisyscat.schema_packages.mypackage.NRVSpectroscopy',
                'data.method#nomad_unisyscat.schema_packages.mypackage.NRVSpectroscopy'
            ],
            options={
                'entry_name': Column(),
                'entry_id': Column(),
                'results.eln.lab_ids': Column,
                'results.eln.methods': Column,
                'data.name#nomad_unisyscat.schema_packages.mypackage.NRVSpectroscopy':
                    Column(),
                'data.method#nomad_unisyscat.schema_packages.mypackage.NRVSpectroscopy':
                    Column(),
                
            },
        ),

        filter_menus=FilterMenus(
            options={
                'material': FilterMenu(label='Material'),
                'eln': FilterMenu(label='Electronic Lab Notebook'),
                'custom_quantities': FilterMenu(label='User Defined Quantities'),
                'author': FilterMenu(label='Author / Origin / Dataset'),
                'metadata': FilterMenu(label='Visibility / IDs / Schema'),
            }
        ),
        filters=Filters(
            include=['*#nomad_unisyscat.schema_packages.mypackage.NRVSpectroscopy'],
        ),
        # dashboard={
        #     'widgets': [
        #         {
        #             'type': 'terms',
        #             'scale': 'linear',
        #             'quantity': 'data.method',
        #             'layout': {
        #                 'xxl': {
        #                     'minH': 3,
        #                     'minW': 3,
        #                     'h': 9,
        #                     'w': 6,
        #                     'y': 0,
        #                     'x': 10,
        #                 },
        #                 'xl': {
        #                     'minH': 3,
        #                     'minW': 3,
        #                     'h': 9,
        #                     'w': 6,
        #                     'y': 0,
        #                     'x': 10,  #'.inf',
        #                 },
        #                 'lg': {'minH': 3, 'minW': 3, 'h': 4, 'w': 5, 'y': 0, 'x': 0},
        #                 'md': {
        #                     'minH': 3,
        #                     'minW': 3,
        #                     'h': 9,
        #                     'w': 6,
        #                     'y': 0,
        #                     'x': 10,  #'.inf',
        #                 },
        #                 'sm': {
        #                     'minH': 3,
        #                     'minW': 3,
        #                     'h': 9,
        #                     'w': 6,
        #                     'y': 0,
        #                     'x': 10,  #'.inf',
        #                 },
        #             },
        #         },
        #     ],
        # }
    ),
)
