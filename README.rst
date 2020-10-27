Hamstr
======

Tool for automatically collecting your data that is spread out among different APIs.

Simplest example
----------------

.. code-block:: python

    from hamstr import Hamstr

    app = Hamstr()
    app.add_collector(url='https://api.example.com/examples', interval=3600)

    if __name__ == '__main__':
        app.run()

This will call the (nonexistent) https://api.example.com/examples endpoint every
3600 seconds (1 hour) and, by default, write the response to a file with the timestamp
of the collection as name.
