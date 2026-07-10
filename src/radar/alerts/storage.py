"""
Alert storage system
"""

import json
from pathlib import Path


class AlertStorage:


    def __init__(self):

        self.file = Path(
            "logs/alerts.json"
        )

        self.file.parent.mkdir(
            exist_ok=True
        )


    def save(
        self,
        alerts
    ):

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                alerts,
                f,
                indent=4
            )


    def load(self):

        if not self.file.exists():

            return []


        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)