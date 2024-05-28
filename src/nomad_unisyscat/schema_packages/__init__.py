from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class MySchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_unisyscat.schema_packages.mypackage import m_package

        return m_package


mypackage = MySchemaPackageEntryPoint(
    name='MyPackage',
    description='Schema package defined using the new plugin mechanism.',
)


class SpectroscopyEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_unisyscat.schema_packages.mypackage import m_package

        return m_package


unisyscatpackage = SpectroscopyEntryPoint(
    name='UniSysCat',
    description="""
    Schema package for unisyscat example data defined using the new plugin mechanism.
    """,
)
