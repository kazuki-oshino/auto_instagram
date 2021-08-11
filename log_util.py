from logging import getLogger, StreamHandler, Formatter, FileHandler, DEBUG


def setup_logger(log_folder, modname=__name__):
    logger = getLogger(modname)
    logger.setLevel(DEBUG)

    sh = StreamHandler()
    sh.setLevel(DEBUG)
    formatter = Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    fh = FileHandler(log_folder)
    fh.setLevel(DEBUG)
    fh_formatter = Formatter('%(asctime)s - %(filename)s - %(name)s - %(lineno)d - %(levelname)s - %(message)s')
    fh.setFormatter(fh_formatter)
    logger.addHandler(fh)
    return logger
