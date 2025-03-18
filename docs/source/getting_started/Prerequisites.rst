.. _Prerequisites:

Prerequisites
=================================

You will need the following packages to be able to run ``delma``:

- `pandas <https://pandas.pydata.org/>`_
- `beautifulsoup4 <https://beautiful-soup-4.readthedocs.io/en/latest/>`_
- `configparser <https://pypi.org/project/configparser/>`_
- `pytest <https://pypi.org/project/pytest/>`_
- `requests <https://requests.readthedocs.io/en/latest/>`_
- `shutils <https://pypi.org/project/shutils/>`_
- `metapype <https://pypi.org/project/metapype/>`_
- `xmltodict <https://pypi.org/project/xmltodict/>`_

To install all of these at once, run

.. prompt:: 

    pip install pandas beautifulsoup4 configparser pytest requests shutils metapype xmltodict

WARNING: If you're installing all of the packages in one go, make sure you check that the installation ran successfully.  If one package doesnt work, the rest following wont install...