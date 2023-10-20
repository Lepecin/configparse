from .types import Config
from .abstract import ConfigLoader


class TestConfigLoader(ConfigLoader):
    def load(self, path: str) -> Config:
        print(f"Load config from {path}")

        test_config = {
            "hello": {
                "hey": 2,
                "ho": 3,
                "yeet": {
                    "halo": 9,
                },
            },
            "sup": 5,
        }

        return test_config

    def save(self, path: str, config: Config):
        print(f"Saved config to {path}")
        print(config)
