Hamstr
======

Tool for gathering and aggregating data from decentralized streams.


.. code-block:: shell

    $ hamstr startproject <name>

This will create a directory with <name> and the following contents::

    <name>/
        deploy.cfg
        <name>/
            __init__.py
            models.py
            settings.py
            collectors/
                __init__.py


To run collectors 1 time and terminate afterwards

.. code-block:: shell

    $ hamstr collect <project_path>


To run project, which executes collectors when scheduled

.. code-block:: shell

    $ hamstr run <project_path>
