from ConfigParser import SafeConfigParser

def config_parser():
    """get config section"""
    parser = SafeConfigParser()
    parser.read('config.ini')
    return parser

sched_configs = config_parser()
