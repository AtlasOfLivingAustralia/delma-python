import delma
import pytest
import shutil
import os
import pandas as pd

# ------------------------------------
# prep for tests
# ------------------------------------
if os.path.isdir('testing'):
    shutil.rmtree('testing',ignore_errors=True)
if os.path.exists('metadata.md'):
    os.remove('metadata.md')
if os.path.exists('testing.md'):
    os.remove('testing.md')
os.mkdir('testing')

# ------------------------------------
# create_md.py
# ------------------------------------
def test_default_markdown():
    delma.create_md()
    assert os.path.isfile('metadata.md')

def test_rename_markdown():
    delma.create_md(metadata_md='testing.md')
    assert os.path.isfile('testing.md')

def test_directory():
    delma.create_md(working_dir='testing')
    assert os.path.isfile('testing/metadata.md')

def test_directory_rename_markdown():
    delma.create_md(metadata_md='testing.md',working_dir='testing')
    assert os.path.isfile('testing/testing.md')

def test_xml():
    if os.path.isfile('metadata.md'):
        os.remove('metadata.md')
    delma.create_md(xml_url="https://collections.ala.org.au/ws/eml/dr368")
    assert os.path.isfile('metadata.md')

def test_xml_rename():
    if os.path.isfile('testing.md'):
        os.remove('testing.md')
    delma.create_md(xml_url="https://collections.ala.org.au/ws/eml/dr368",metadata_md='testing.md')
    assert os.path.isfile('testing.md')

def test_xml_change_working_dir():
    if os.path.isfile('testing/metadata.md'):
        os.remove('testing/metadata.md')
    delma.create_md(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing')
    assert os.path.isfile('testing/metadata.md')

def test_xml_rename_change_working_dir():
    if os.path.isfile('testing/testing.md'):
        os.remove('testing/testing.md')
    delma.create_md(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing',metadata_md='testing.md')
    assert os.path.isfile('testing/testing.md')

# ------------------------------------
# display_as_dataframe.py
# ------------------------------------
def test_display_as_dataframe_default():
    delma.create_md()
    df = delma.display_as_dataframe()
    assert type(df) is pd.core.frame.DataFrame

def test_display_as_dataframe_specify_markdown():
    delma.create_md('testing.md')
    df = delma.display_as_dataframe(metadata_md='testing.md')
    assert type(df) is pd.core.frame.DataFrame

def test_display_as_dataframe_specify_directory():
    delma.create_md(working_dir='testing')
    df = delma.display_as_dataframe(working_dir='testing')
    assert type(df) is pd.core.frame.DataFrame

def test_display_as_dataframe_both_markdown_directory():
    delma.create_md(working_dir='testing',metadata_md='testing.md')
    df = delma.display_as_dataframe(working_dir='testing',metadata_md='testing.md')
    assert type(df) is pd.core.frame.DataFrame

def test_display_as_dataframe_xml():
    if os.path.isfile('metadata.md'):
        os.remove('metadata.md')
    delma.create_md(xml_url="https://collections.ala.org.au/ws/eml/dr368")
    df = delma.display_as_dataframe()
    assert type(df) is pd.core.frame.DataFrame

def test_display_as_dataframe_xml_rename():
    if os.path.isfile('testing.md'):
        os.remove('testing.md')
    delma.create_md(xml_url="https://collections.ala.org.au/ws/eml/dr368",metadata_md='testing.md')
    df = delma.display_as_dataframe(metadata_md='testing.md')
    assert type(df) is pd.core.frame.DataFrame

def test_display_as_dataframe_xml_change_working_dir():
    if os.path.isfile('testing/metadata.md'):
        os.remove('testing/metadata.md')
    delma.create_md(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing')
    df = delma.display_as_dataframe(working_dir='testing')
    assert type(df) is pd.core.frame.DataFrame

def test_display_as_dataframe_xml_rename_change_working_dir():
    if os.path.isfile('testing/testing.md'):
        os.remove('testing/testing.md')
    delma.create_md(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing',metadata_md='testing.md')
    df = delma.display_as_dataframe(working_dir='testing',metadata_md='testing.md')
    assert type(df) is pd.core.frame.DataFrame

# ------------------------------------
# write_eml.py
# ------------------------------------
def test_write_eml_default():
    if os.path.exists('metadata.md'):
        os.remove('metadata.md')
    delma.create_md()
    delma.write_eml()
    assert os.path.isfile('eml.xml')

def test_write_eml_markdown():
    if os.path.exists('eml.xml'):
        os.remove('eml.xml')
    if os.path.exists('testing.md'):
        os.remove('testing.md')
    delma.create_md(metadata_md='testing.md')
    delma.write_eml(metadata_md='testing.md')
    assert os.path.isfile('eml.xml')

def test_write_eml_directory():
    if os.path.exists('testing/metadata.md'):
        os.remove('testing/metadata.md')
    if os.path.exists('testing/eml.xml'):
        os.remove('testing/eml.xml')
    delma.create_md(working_dir='testing')
    delma.write_eml(working_dir='testing')
    assert os.path.isfile('testing/eml.xml')

def test_write_eml_markdown_directory():
    if os.path.exists('testing/testing.md'):
        os.remove('testing/testing.md')
    if os.path.exists('testing/eml.xml'):
        os.remove('testing/eml.xml')
    delma.create_md(working_dir='testing',metadata_md='testing.md')
    delma.write_eml(working_dir='testing',metadata_md='testing.md')
    assert os.path.isfile('testing/eml.xml')

def test_write_eml_directory_eml_xml():
    if os.path.exists('testing/metadata.md'):
        os.remove('testing/metadata.md')
    if os.path.exists('testing/testing.xml'):
        os.remove('testing/testing.xml')
    delma.create_md(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing')
    delma.write_eml(working_dir='testing',eml_xml='testing.xml')
    assert os.path.isfile('testing/testing.xml')

def test_write_eml_markdown_eml_xml():
    if os.path.exists('testing.md'):
        os.remove('testing.md')
    if os.path.exists('testing.xml'):
        os.remove('testing.xml')
    delma.create_md(xml_url="https://collections.ala.org.au/ws/eml/dr368",metadata_md='testing.md')
    delma.write_eml(metadata_md='testing.md',eml_xml='testing.xml')
    assert os.path.isfile('testing.xml')

def test_write_eml_markdown_directory_xml_rename():
    if os.path.exists('testing/testing.md'):
        os.remove('testing/testing.md')
    if os.path.exists('testing/testing.xml'):
        os.remove('testing/testing.xml')
    delma.create_md(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing',metadata_md='testing.md')
    delma.write_eml(working_dir='testing',metadata_md='testing.md',eml_xml='testing.xml')
    assert os.path.isfile('testing/testing.xml')

# ------------------------------------
# check_metadata.py
# ------------------------------------
def test_check_metadata_default():
    if os.path.exists('metadata.md'):
        os.remove('metadata.md')
    delma.create_md()
    delma.write_eml()
    check = delma.check_metadata()
    assert check is None

def test_check_metadata_markdown():
    if os.path.exists('eml.xml'):
        os.remove('eml.xml')
    if os.path.exists('testing.md'):
        os.remove('testing.md')
    delma.create_md(metadata_md='testing.md')
    delma.write_eml(metadata_md='testing.md')
    check = delma.check_metadata()
    assert check is None

def test_check_metadata_directory():
    if os.path.exists('testing/metadata.md'):
        os.remove('testing/metadata.md')
    if os.path.exists('testing/eml.xml'):
        os.remove('testing/eml.xml')
    delma.create_md(working_dir='testing')
    delma.write_eml(working_dir='testing')
    check = delma.check_metadata(working_dir='testing')
    assert check is None

def test_check_metadata_markdown_directory():
    if os.path.exists('testing/testing.md'):
        os.remove('testing/testing.md')
    if os.path.exists('testing/eml.xml'):
        os.remove('testing/eml.xml')
    delma.create_md(working_dir='testing',metadata_md='testing.md')
    delma.write_eml(working_dir='testing',metadata_md='testing.md')
    check = delma.check_metadata(working_dir='testing')
    assert check is None

def test_check_metadata_directory_eml_xml():
    if os.path.exists('testing/metadata.md'):
        os.remove('testing/metadata.md')
    if os.path.exists('testing/testing.xml'):
        os.remove('testing/testing.xml')
    delma.create_md(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing')
    delma.write_eml(working_dir='testing',eml_xml='testing.xml')
    check = delma.check_metadata(working_dir='testing',eml_xml='testing.xml')
    assert check is None

def test_check_metadata_markdown_eml_xml():
    if os.path.exists('testing.md'):
        os.remove('testing.md')
    if os.path.exists('testing.xml'):
        os.remove('testing.xml')
    delma.create_md(xml_url="https://collections.ala.org.au/ws/eml/dr368",metadata_md='testing.md')
    delma.write_eml(metadata_md='testing.md',eml_xml='testing.xml')
    check = delma.check_metadata(eml_xml='testing.xml')
    assert check is None

def test_check_metadata_markdown_directory_xml_rename():
    if os.path.exists('testing/testing.md'):
        os.remove('testing/testing.md')
    if os.path.exists('testing/testing.xml'):
        os.remove('testing/testing.xml')
    delma.create_md(xml_url="https://collections.ala.org.au/ws/eml/dr368",working_dir='testing',metadata_md='testing.md')
    delma.write_eml(working_dir='testing',metadata_md='testing.md',eml_xml='testing.xml')
    check = delma.check_metadata(working_dir='testing',eml_xml='testing.xml')
    assert check is None