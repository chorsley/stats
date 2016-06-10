import subprocess

def deploy():
    '''Builds the site, puts in gh-pages'''
    content = 'content'
    outputfp = 'output'
    remote = 'origin'
    config = 'config_default.py'

    _generate = ['pelican', content, '-o', outputfp, '-s', config]
    _copy = ['ghp-import', '-m', 'New site build', outputfp]
    _push = ['git', 'push', remote, 'gh-pages', '--force']

    print('Generating the static site')
    subprocess.call(_generate)
    print('Copying the generated site to the gh-pages branch')
    subprocess.call(_copy)

    print('')
    print('You can now push gh-pages branch live using the following command')
    print(' '.join(_push))
    # click.echo('Pushing gh-pages branch to the deploy remote')
    # subprocess.call(_push)

deploy()

