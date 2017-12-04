
import ConfigParser

def parseConfig(configfile, section):
    config = ConfigParser.ConfigParser()
    config.read(configfile)
    return { x[0] : x[1] for x in config.items(section) }

