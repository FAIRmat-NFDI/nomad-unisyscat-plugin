import os.path

from nomad.client import normalize_all, parse


def test_ir_schema():
    test_file = os.path.join('tests', 'data', 'ir_test.archive.yaml')
    entry_archive = parse(test_file)[0]
    normalize_all(entry_archive)

    assert entry_archive.data.results[0].wavenumber is not None


def test_epr_schema():
    test_file = os.path.join('tests', 'data', 'epr_test.archive.yaml')
    entry_archive = parse(test_file)[0]
    normalize_all(entry_archive)

    assert entry_archive.data.results[0].intensity is not None
