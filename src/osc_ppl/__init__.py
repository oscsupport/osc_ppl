import logging
import pathlib
import logging.handlers

_time_fmt = '%Y-%m-%d %H:%M'
_fmt = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s::%(funcName)s:%(lineno)d) - %(message)s"


def _get_file_handler(logfile, formatter):
    handler = logging.handlers.RotatingFileHandler(
        logfile,
        maxBytes=0.5e7, 
        backupCount=1
    )

    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)
    return handler


def _get_stream_handler(formatter, level):
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    handler.setLevel(level)
    return handler


def get_logger(logfile, level):
    print(__name__)
    if not logfile is pathlib.Path:
        logfile = pathlib.Path(logfile)

    if not logfile.parent.is_dir():
        logfile.parent.mkdir()

    if not logfile.is_file():
        logfile.touch()

    logger = logging.getLogger(__name__)
    logger.setLevel(level)

    formatter = logging.Formatter(
        datefmt=_time_fmt, 
        fmt=_fmt
    )
    
    file_handler = _get_file_handler(logfile, formatter)
    stream_handler = _get_stream_handler(formatter, level)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger