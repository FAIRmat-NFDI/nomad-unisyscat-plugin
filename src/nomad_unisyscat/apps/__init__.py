from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import App, Column, Columns, FilterMenu, FilterMenus


myapp = AppEntryPoint(
    name='UniSysCatApp',
    description='Explore UniSysCat example data.',
    app=App(
        label='UniSysCatApp',
        path='unisyscatapp',
        category='Use Cases',
        columns=Columns(
            selected=[
                'entry_id',
                'data.method#nomad_unisyscat.schema_packages.mypackage.NRVSpectroscopy'
            ],
            options={
                'entry_id': Column(),
                'data.method#nomad_unisyscat.schema_packages.mypackage.NRVSpectroscopy': Column()
            },
        ),

        filter_menus=FilterMenus(
            options={
                'material': FilterMenu(label='Material'),
            }
        ),
        filters=Filters(
            include=['*#nomad_unisyscat.schema_packages.mypackage'],
        ),
    ),
)
