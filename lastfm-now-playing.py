#!/usr/bin/env python3

import pylast
import os
import click
import logging
import sys

@click.command()
@click.option('--apikey', default=None)
@click.option('--secret', default=None)
@click.option('--log', default='INFO')
@click.argument('username', default=None)


def run(apikey, secret, log, username):
    """ Get the current playing song for user """

    logger = logging.getLogger(__name__)
    log_handler = logging.StreamHandler(sys.stderr)
    logger.setLevel(getattr(logging, log.upper()))
    logger.addHandler(log_handler)
    logger.debug('Debug logging enabled')

    if secret:
        SECRET = secret
    else:
        try:
            SECRET = os.environ['LASTFM_SECRET']
        except KeyError as e:
            logger.error(f'Error reading environment variable: {e}')
            sys.exit(1)
            click.clear
    if apikey:
        API_KEY = apikey
    else:
        try:
            API_KEY = os.environ['LASTFM_API_KEY']
        except KeyError as e:
            logger.error(f'Error reading environment variable: {e}')
            sys.exit(1)
    try:
        network = pylast.LastFMNetwork(API_KEY, SECRET)
    except WSError as e:
        logger.error(f'Error connecting to lastfm: {e}')
        sys.exit(1)

    user = network.get_user(username)

    click.echo(user.get_now_playing())

if __name__ == '__main__':
    run()
