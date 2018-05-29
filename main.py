#!/usr/bin/env python
 
import sys
import logging
import logging.config
import solution

def get_log_level(log_args):
    # Numeric levels 10, 20, 30, 40
    valid_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR']
    proposed_level = log_args[0].split("=", 1)[1].upper()
    if not proposed_level in valid_levels:
        raise ValueError('Invalid log level: %s' % proposed_level)
    return proposed_level

def main():
    """
    Note: Manually override the lowest-severity log message level
    that the logger will handle from the command line by executing with flags:
    i.e. python main.py --log=WARNING

    Sample usage:
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warn message')
        logger.error('error message')
    """

    # Load logger config
    logging.config.fileConfig('logging.conf')

    # Create logger
    logger = logging.getLogger('Recogniser logger')

    # Specify lowest-severity log message a logger will handle
    logger.setLevel('ERROR')
    if len(sys.argv):
        log_args = [arg for arg in sys.argv if '--log=' in arg]
        if len(log_args) > 0:
            logger.setLevel(get_log_level(log_args))

    # Get current logging level
    numeric_level = logging.getLogger().getEffectiveLevel()
    logging.info('Starting Recogniser')
    solution.run()
    logging.info('Finished Recogniser')

if __name__ == '__main__':
    main()
