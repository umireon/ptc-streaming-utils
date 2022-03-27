from configparser import ConfigParser
from os import chdir, getcwd
from os.path import abspath, dirname, exists, join
from dataclasses import dataclass
import re

@dataclass
class AppConfig:
    path: str

basedir = dirname(__file__)

def read_ini(name: str, basedir = basedir, config_path = join(basedir, 'config.ini')) -> AppConfig:
    config = ConfigParser()
    config.read(config_path)
    oldcwd = getcwd()
    chdir(basedir)
    path=abspath(config[name]['path'])
    chdir(oldcwd)
    return AppConfig(path=path)

def increment(config: AppConfig) -> None:
    if not exists(config.path):
        with open(config.path, 'w') as fp:
            pass

    with open(config.path, 'r+') as fp:
        input_text = fp.read()
        m = re.match('^(.*)(\d+)(.*)$', input_text)
        if m is None:
            output_text = "1"
        else:
            value = int(m[2])
            if value < 6:
                value += 1
            output_text = m[1] + str(value) + m[3]
        fp.seek(0)
        fp.write(output_text)

def decrement(config: AppConfig) -> None:
    if not exists(config.path):
        with open(config.path, 'w') as fp:
            pass

    with open(config.path, 'r+') as fp:
        input_text = fp.read()
        m = re.match('^(.*)(\d+)(.*)$', input_text)
        if m is None:
            output_text = "0"
        else:
            value = int(m[2])
            if value > 0:
                value -= 1
            output_text = m[1] + str(value) + m[3]
        fp.seek(0)
        fp.write(output_text)
