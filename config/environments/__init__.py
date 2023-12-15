from .local.api import ApiConfig as LocalApiConfig
from .local.react import ReactConfig as LocalReactConfig
from .local.angular import AngularConfig as LocalAngularConfig
from .dev.api import ApiConfig as DevApiConfig
from .dev.react import ReactConfig as DevReactConfig
from .dev.angular import AngularConfig as DevAngularConfig
from .prod.api import ApiConfig as ProdApiConfig
from .prod.react import ReactConfig as ProdReactConfig
from .prod.angular import AngularConfig as ProdAngularConfig


def get_config(env):
    """Get Config Environment"""
    if env == "local":
        return {
            "angular": LocalAngularConfig().BASE_URL,
            "react": LocalReactConfig().BASE_URL,
            "api": LocalApiConfig().BASE_URL,
        }
    elif env == "dev":
        return {
            "angular": DevAngularConfig().BASE_URL,
            "react": DevReactConfig().BASE_URL,
            "api": DevApiConfig().BASE_URL,
        }
    elif env == "prod":
        return {
            "angular": ProdAngularConfig().BASE_URL,
            "react": ProdReactConfig().BASE_URL,
            "api": ProdApiConfig().BASE_URL,
        }
    else:
        raise ValueError(f"Unsupported environment: {env}")
