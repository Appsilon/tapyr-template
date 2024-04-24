from loguru import logger


@logger.catch(reraise=True)
def divide(x: int, y: int) -> float:
    """
    The purpose of this function is to illustrate where to put functions in the template.
    Additionally it shows how to use loguru to catch exceptions and log them.
    """

    return x / y
