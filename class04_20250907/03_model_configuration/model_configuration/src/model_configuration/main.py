"""
CLI entry wiring for the model configuration demos.

Exposes four commands via pyproject.toml:
 - run-global-config  -> global_config_main()
 - run-agent-config   -> agent_config_main()
 - run-runner-config  -> runner_config_main()
 - run-debug-mode     -> debug_mode_main()

Each function simply delegates to its respective module.
"""

from model_configuration.global_config_main import global_config_main
from model_configuration.agent_config_main import agent_config_main
from model_configuration.runner_config_main import runner_config_main
from model_configuration.debug_mode_main import debug_mode_main


def run_global_config():
    """Demonstrate app-wide defaults (single provider/model for all agents)."""
    global_config_main()


def run_agent_config():
    """Demonstrate per-agent model configuration via a concrete model object."""
    agent_config_main()


def run_runner_config():
    """Demonstrate per-run overrides using RunConfig (AB tests, canaries, etc.)."""
    runner_config_main()
    
def run_debug_mode():
    """Demonstrate .env-based credentials + verbose logging for debugging."""
    debug_mode_main()
