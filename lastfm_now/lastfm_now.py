#!/usr/bin/env python3

import pylast
import os
import click
import logging
import sys

@click.command()
@click.option('-a', '--apikey', default=None, help='Lastfm API key')
@click.option('--log', default='INFO', help='Minimum log level to display [debug, info, warning, error, critical]')
@click.option('--latch/--no-latch', default=False, help='Show most recently played track, even if not currently playing')
@click.option('--prechars', default='', help='Characters to be displayed before the output')
@click.option('--postchars', default='', help='Characters to be displayed after the output')
@click.argument('username', default=None)
def run(apikey, log, username, latch, prechars, postchars):
    """ Get the current playing song for user """

    logger = logging.getLogger(__name__)
    log_handler = logging.StreamHandler(sys.stderr)
    logger.setLevel(getattr(logging, log.upper()))
    logger.addHandler(log_handler)
    logger.debug('Debug logging enabled')

    if apikey:
        API_KEY = apikey
    else:
        try:
            API_KEY = os.environ['LASTFM_API_KEY']
        except KeyError as e:
            logger.error(f'Error reading environment variable: {e}')
            sys.exit(1)
    try:
        network = pylast.LastFMNetwork(API_KEY)
    except WSError as e:
        logger.error(f'Error connecting to lastfm: {e}')
        sys.exit(1)

    user = network.get_user(username)
    playing = user.get_now_playing()
    most_recent = user.get_recent_tracks()[0].track

    if playing:
        build_output(prechars, postchars, playing)
    elif not playing and latch:
        build_output(prechars, postchars, most_recent)

def build_output(prechars, postchars, track):

    click.echo(f'{prechars}{track}{postchars}')

if __name__ == '__main__':
    run()
