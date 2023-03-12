import configparser
import getpass

def init():

    global config

    global urls 
    
    global config_file_path

    config_file_path="/home/"+getpass.getuser()+"/.go2/urls"

    config = configparser.ConfigParser()

    config.read(config_file_path)

    default_profile=config['SETTINGS']['DEFAULT_PROFILE']

    urls=config[default_profile]