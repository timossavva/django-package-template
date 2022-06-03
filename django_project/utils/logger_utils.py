def log_message_to_logger(type_of_log, logger_name, log_msg):
    import logging
    logger = logging.getLogger(logger_name)
    log_msg = "{} | {}".format(logger_name, log_msg)
    if type_of_log == 'debug':
        logger.debug(log_msg)
    if type_of_log == 'info':
        logger.info(log_msg)
    if type_of_log == 'warning':
        logger.warning(log_msg)
    if type_of_log == 'error':
        logger.error(log_msg)
    if type_of_log == 'critical':
        logger.critical(log_msg)
