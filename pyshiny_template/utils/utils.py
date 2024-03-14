from loguru import logger


@logger.catch(reraise=True)
def divide(x, y):
    return x / y
