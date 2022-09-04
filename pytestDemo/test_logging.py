import logging

def test_loggingDmeo():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # filehandler object

    # logger.setLevel(logging.CRITICAL)
    logger.debug("A debug statement is executed")
    logger.info("Information Statement")
    logger.debug("A debug statement is executed")   # This will not printed if we setLevel to the lower lavel
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happend")
    logger.critical("Critical issue")