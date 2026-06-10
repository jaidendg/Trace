import inspect
import asyncio


class Executor:

    def run(self, module, *args):
        result = module.run(*args)

        if inspect.iscoroutine(result):
            return asyncio.run(result)

        return result