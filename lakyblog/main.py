import sys, os
sys.path.append(os.path.abspath('..'))
from optparse import OptionParser
from lakyblog.config import parse_config_file

def parser():
    parser = OptionParser()
    parser.add_option('-d', '--debug',
                      action='store_true', dest='debug',
                      help='run on debug mode', default=False)
    parser.add_option('-c', '--config',
                      action='store', dest='config_file_path',
                      help='config file path', default='config.yaml')
    return parser

def main():
    # parse options
    (options, args) = parser().parse_args()

    # parse config file into setting.setting
    parse_config_file(options.config_file_path)

    # run blog
    from lakyblog.app import app
    app.debug = options.debug
    app.run()

if __name__ == '__main__':
    main()
