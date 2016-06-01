import os.path
import os
import subprocess


def run_rpmdeplint(args, **kwargs):
    env = os.environ
    env['PYTHONBUFFERED'] = '1'

    p = subprocess.Popen(args,
                         stdout=subprocess.PIPE,
                         stdin=open('/dev/null'),
                         stderr=subprocess.PIPE,
                         env=env,
                         **kwargs)

    max_output = 10240
    out = p.stdout.read(max_output)
    if len(out) == max_output:
        raise RuntimeError('Output size limit exceeded when invoking {}:\n{}'.format(args, out))
    err = p.stderr.read(max_output)
    if len(err) == max_output:
        raise RuntimeError('Stderr size limit exceeded when invoking {}:\n{}'.format(args, out))
    p.wait()
    return (p.returncode, out, err)
