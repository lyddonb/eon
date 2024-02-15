# https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py
# https://docs.gunicorn.org/en/latest/settings.html#settings

bind = 'localhost:9999'
raw_env = [
    'FIREBASE_AUTH_EMULATOR_HOST=localhost:9099',
    'FIRESTORE_EMULATOR_HOST=localhost:8081',
    'GOOGLE_CLOUD_PROJECT=local'
]

#
#   Logging
#
#   logfile - The path to a log file to write to.
#
#       A path string. "-" means log to stdout.
#
#   loglevel - The granularity of log output
#
#       A string of "debug", "info", "warning", "error", "critical"
#
errorlog = '-'
loglevel = 'debug'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

#
#   spew - Install a trace function that spews every line of Python
#       that is executed when running the server. This is the
#       nuclear option.
#
#       True or False
#
spew = False

reload = True

