import logging

#logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")


def add(a, b):
    res = a+b
    logger.debug(f"Adding {a} and {b} = {res}")
    return res

def subtract(a, b):
    res = a-b
    logger.debug(f"Subtracting {a} and {b} = {res}")
    return res

def multiply(a, b):
    res = a*b
    logger.debug(f"Multiplying {a} and {b} = {res}")
    return res

def divide(a, b):
    if b == 0:
        logger.error("Division by zero error")
        return None
    res = a/b
    logger.debug(f"Dividing {a} and {b} = {res}")
    return res

add(10, 5)
subtract(10, 5)
multiply(10, 5)
divide(10, 50)
