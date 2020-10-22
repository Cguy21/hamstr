Hamstr
======

Tool for gathering and aggregating data from decentralized streams.


.. code-block:: shell

    $ hamstr startproject <name>

project/
    deploy.cfg
    project/
        __init__.py
        models.py
        settings.py
        collectors/
            __init__.py


To run collectors 1 time and terminating afterwards

.. code-block:: shell

    $ hamstr collect <project_path>


To run project, which executes collectors when scheduled

.. code-block:: shell

    $ hamstr run <project_path>
