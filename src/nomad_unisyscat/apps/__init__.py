from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Column,
    Columns,
    FilterMenu,
    FilterMenus,
    Filters,
)

schema = 'nomad_unisyscat.schema_packages.*'

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
                'results.eln.lab_ids',
                'data.method#nomad_unisyscat.schema_packages.mypackage.NRVSpectroscopy',
            ],
            options={
                'entry_name': Column(),
                'entry_id': Column(),
                'results.eln.lab_ids': Column(),
                'results.eln.methods': Column(),
                'results.eln.instruments': Column(),
                'data.name#nomad_unisyscat.schema_packages.mypackage.NRVSpectroscopy':
                    Column(),
                'data.method#nomad_unisyscat.schema_packages.mypackage.NRVSpectroscopy':
                    Column(),
                'authors.name': Column(),
                'results.method.simulation.program_name': Column(),
            },
        ),

        filter_menus=FilterMenus(
            options={
                'material': FilterMenu(label='Material'),
                'elements': FilterMenu(label='Elements / Formula', level=1, size='xl'),
                'eln': FilterMenu(label='Electronic Lab Notebook'),
                'custom_quantities': FilterMenu(label='User Defined Quantities'),
                'author': FilterMenu(label='Author / Origin / Dataset'),
                'metadata': FilterMenu(label='Visibility / IDs / Schema'),
            }
        ),
        filters=Filters(
            include=['*#nomad_unisyscat.schema_packages.mypackage.*'],
        ),
        filters_locked={'upload_name': 'UniSysCat Test Data'}, #schema},
        dashboard={
            'widgets': [
                {
                    'type': 'terms',
                    'scale': 'linear',
                    'quantity': 'results.eln.methods',
                    'layout': {
                        'xxl': {
                            'minH': 3,
                            'minW': 3,
                            'h': 5,
                            'w': 6,
                            'y': 0,
                            'x': 0,
                        },
                        'xl': {
                            'minH': 3,
                            'minW': 3,
                            'h': 5,
                            'w': 6,
                            'y': 0,
                            'x': 0,
                        },
                        'lg': {'minH': 3, 'minW': 3, 'h': 5, 'w': 6, 'y': 0, 'x': 0},
                        'md': {
                            'minH': 3,
                            'minW': 3,
                            'h': 5,
                            'w': 6,
                            'y': 0,
                            'x': 0,
                        },
                        'sm': {
                            'minH': 3,
                            'minW': 3,
                            'h': 4,
                            'w': 6,
                            'y': 0,
                            'x': 0,  #'.inf',
                        },
                    },
                },
                {
                    'type': 'terms',
                    'scale': 'linear',
                    'quantity': 'results.eln.instruments',
                    'layout': {
                        'xxl': {
                            'minH': 3,
                            'minW': 3,
                            'h': 5,
                            'w': 6,
                            'y': 0,
                            'x': 6,
                        },
                        'xl': {
                            'minH': 3,
                            'minW': 3,
                            'h': 5,
                            'w': 6,
                            'y': 0,
                            'x': 6,
                        },
                        'lg': {'minH': 3, 'minW': 3, 'h': 5, 'w': 6, 'y': 0, 'x': 6},
                        'md': {
                            'minH': 3,
                            'minW': 3,
                            'h': 5,
                            'w': 6,
                            'y': 0,
                            'x': 6,
                        },
                        'sm': {
                            'minH': 3,
                            'minW': 3,
                            'h': 4,
                            'w': 6,
                            'y': 0,
                            'x': 6,
                        },
                    },
                },
                {
                    'type': 'terms',
                    'scale': 'linear',
                    'quantity': 'authors.name',
                    'layout': {
                        'xxl': {
                            'minH': 3,
                            'minW': 3,
                            'h': 5,
                            'w': 6,
                            'y': 0,
                            'x': 12,
                        },
                        'xl': {
                            'minH': 3,
                            'minW': 3,
                            'h': 5,
                            'w': 6,
                            'y': 0,
                            'x': 12,
                        },
                        'lg': {'minH': 3, 'minW': 3, 'h': 5, 'w': 6, 'y': 0, 'x': 12},
                        'md': {
                            'minH': 3,
                            'minW': 3,
                            'h': 5,
                            'w': 6,
                            'y': 0,
                            'x': 12,
                        },
                        'sm': {
                            'minH': 3,
                            'minW': 3,
                            'h': 4,
                            'w': 6,
                            'y': 4,
                            'x': 0,
                        },
                    },
                },
                {
                    'type': 'terms',
                    'scale': 'linear',
                    'quantity': 'results.method.simulation.program_name',
                    'layout': {
                        'xxl': {
                            'minH': 3,
                            'minW': 3,
                            'h': 5,
                            'w': 6,
                            'y': 0,
                            'x': 18,
                        },
                        'xl': {
                            'minH': 3,
                            'minW': 3,
                            'h': 5,
                            'w': 6,
                            'y': 0,
                            'x': 18,
                        },
                        'lg': {'minH': 3, 'minW': 3, 'h': 5, 'w': 6, 'y': 0, 'x': 18},
                        'md': {
                            'minH': 3,
                            'minW': 3,
                            'h': 5,
                            'w': 6,
                            'y': 5,
                            'x': 0,
                        },
                        'sm': {
                            'minH': 3,
                            'minW': 3,
                            'h': 4,
                            'w': 6,
                            'y': 4,
                            'x': 6,
                        },
                    },
                },
                {
                    'type': 'histogram',
                    'showinput': 'true',
                    'autorange': 'true',
                    'nbins': 30,
                    'scale': 'linear',
                    'quantity': 'entry_create_time',
                    'layout': {
                        'xxl': {
                            'minH': 3,
                            'minW': 3,
                            'h': 6,
                            'w': 12,
                            'y': 5,
                            'x': 0,
                        },
                        'xl': {
                            'minH': 3,
                            'minW': 3,
                            'h': 5,
                            'w': 12,
                            'y': 5,
                            'x': 0,
                        },
                        'lg': {'minH': 3, 'minW': 3, 'h': 5, 'w': 12, 'y': 5, 'x': 0},
                        'md': {
                            'minH': 3,
                            'minW': 3,
                            'h': 5,
                            'w': 12,
                            'y': 8,
                            'x': 0,
                        },
                        'sm': {
                            'minH': 3,
                            'minW': 3,
                            'h': 5,
                            'w': 12,
                            'y': 8,
                            'x': 0,
                        },
                    },
                },
                # {
                #     'type': 'scatterplot',
                #     'autorange': 'true',
                #     'size': 1000,
                #     'scale': 'linear',
                #     'y':
                #         'quantity': 'data.results[0].frequency'
                #             '#nomad_unisyscat.schema_packages.mypackage.EPR',
                #     'x':
                #         'quantity': 'data.results[0].signal'
                #             '#nomad_unisyscat.schema_packages.mypackage.EPR',
                #     'layout': {
                #         'xxl': {
                #             'minH': 3,
                #             'minW': 3,
                #             'h': 6,
                #             'w': 12,
                #             'y': 5,
                #             'x': 12,
                #         },
                #         'xl': {
                #             'minH': 3,
                #             'minW': 3,
                #             'h': 5,
                #             'w': 12,
                #             'y': 5,
                #             'x': 12,
                #         },
                #         'lg': {
                #             'minH': 3, 'minW': 3,
                #             'h': 5, 'w': 12, 'y': 5, 'x': 12},
                #         'md': {
                #             'minH': 3,
                #             'minW': 3,
                #             'h': 6,
                #             'w': 12,
                #             'y': 10,
                #             'x': 0,
                #         },
                #         'sm': {
                #             'minH': 3,
                #             'minW': 3,
                #             'h': 6,
                #             'w': 12,
                #             'y': 13,
                #             'x': 0,
                #         },
                #     },
                # }
            ],
        }
    ),
)
