import asyncio
from sync_vs_async_agent_execution.sync_main import sync_main
from sync_vs_async_agent_execution.async_main import async_main
from sync_vs_async_agent_execution.sync_main_demo import sync_main_demo
from sync_vs_async_agent_execution.async_main_demo import async_main_demo


def run_sync():
    sync_main()


def run_async():
    asyncio.run(async_main())


def run_sync_demo():
    sync_main_demo()


def run_async_demo():
    asyncio.run(async_main_demo())
