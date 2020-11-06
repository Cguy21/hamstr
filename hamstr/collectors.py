from copy import copy
from datetime import timedelta

from pydantic import BaseModel


class CollectorMeta(type):

    def __new__(mcs, name, bases, namespace, **kwargs):
        """
        Removes Model class definition from collector class
        and creates actual pydantic BaseModel from it. Model
        is not accessible as model attribute. Also, collects
        all settings and stores them in settings dict attr.
        """
        model = namespace.get('Model')
        if model:
            # creates pydantic model subclass
            d = {k: v for k, v in model.__dict__.items() if k != '__dict__'}
            model = type('Model', (BaseModel,), d)

        ignore = ['Model']

        settings = {}
        if bases:
            possible = bases[0].default_settings
            for k, v in namespace.items():
                k = k.upper()
                if k in possible:
                    settings[k] = v
            for k in possible:
                ignore.append(k.lower())

        new_namespace = {
            'model': model,
            'settings': settings,
            **{k: v for k, v in namespace.items() if k not in ignore},
        }
        cls = super().__new__(mcs, name, bases, new_namespace, **kwargs)
        return cls


class Collector(metaclass=CollectorMeta):

    default_settings = {
        'INTERVAL': timedelta(days=1),
    }

    def __init__(
        self,
        cli_settings: dict = None,
        project_settings: dict = None,
    ):
        self._resolve_settings(cli_settings or {}, project_settings or {})

    def _resolve_settings(self, cli_settings: dict, project_settings: dict) -> dict:
        """
        Setting resolution order lowest to highest priority.

            1. Default settings
            2. (Possible) project settings
            3. Collector class settings
            4. (possible) CLI variables
        """
        settings = copy(self.default_settings)
        # project = overwrite_settings(default, project_settings)
        settings.update(project_settings)
        settings.update(self.settings)
        settings.update(cli_settings)
        self.settings = settings

    def parse_json_response(self, json: dict):
        """
        Extracts the model(s) from the json response of the list API call.
        """
        # if not self.model:
        #     return json

    def export_item(self, item: any):
        """
        Sends the item to storage backend.
        """
