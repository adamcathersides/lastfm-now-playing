#!/usr/bin/env python3

import pylast
import os
import click


API_SECRET = os.environ.get('LASTFM_API_SECRET')

@click.command()
@click.option('--api_key', default=None)
@click.option('--secret', default=None)
@click.option('--user', default=None)

def run(api_key, secret, user):
    """ Get the current playing song for user """

    if api_key:
        API_KEY = api_key
    else:
        try:
            os.environ.get('LASTFM_API_KEY')
        except:
            print('No API key envvar')

if __name__ == '__main__':
    run()
