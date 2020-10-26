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

API OPTIONS

depends on goal of hamstr

OPTION 1
pros: clean, simple, callbacks
cons: will always get all objects at endpoint (how to smart limit?)

.. code-block:: python

    from hamstr import Hamstr, Service, Model, paginators

    app = Hamstr()

    mollie = Service(
        'https://api.mollie.com/v2/',
        api_key='123',
        paginator=paginators.SeekPaginator
    )

    mollie.add_collector(endpoint='payments', model=Model, interval=5, callbacks=[])

    app.register_service(mollie)

    app.run()

OPTION 2
pros:
cons: verbose project structure

structure::

    project/
        settings.py
        services/
            mollie/
                conf.py
                collectors.py
                models.py

# conf.py

.. code-block:: python

    BASE_URL = 'https://api.mollie.com/v2/'
    API_KEY = '123'

# collectors.py

.. code-block:: python

    from hamstr.collectors import Collector

    from .models import Payment

    # class-based collector option 1
    class PaymentsCollector(Collector):
        endpoint = 'payments'
        model = Payment
        interval = 5  # seconds

        def collect(self, response):
            ...
            # extract 'Payment' objects from response
            return objects
    
    # class-based collector option 1
    class PaymentsCollector(Collector):
        model = Payment
        interval = 5  # seconds

        def collect(self):
            # call api
            return objects

# models.py

.. code-block:: python

    from hamstr import Model

    class Payments(Model):
        id: str
        createdAt: datetime
        # ...

OPTION 3

pros: no code
cons: no callbacks, limited customisability

# hamstr.yml::

    name: project
    services:  # list of api providers
        mollie:
            base_url: https://api.mollie.com/v2
            api_key: "123"
            paginator: SeekPaginator  # always calls list endpoint and paginates with paginator (so, only new objects)
            collectors:
                /payments:  # endoint
                    interval:  # when to run collector
                        days: 1
                    model:  # return model of single object returned by get request
                    resource: string
                    id: string

Running hamstr

.. code-block:: shell

    $ hamstr run hamstr.yml
