Hamstr
======

Tool for gathering and aggregating data from decentralized streams.

.. For example, say you have take away restaurant that allows people to
.. order online as well as in the shop. This way you will have 2 seperate
.. streams of order data. STOORD allows you to hook into both events and
.. extract certain data from them and store this data in the same place.

Constraints:
    1. Storage backend independent (Abstract Base Model)
    2. API independent
    3. Data independent

Like Scrapy project has a project template

project/
    deploy.cfg
    project/
        __init__.py
        models.py
        settings.py
        collectors/
            __init__.py

