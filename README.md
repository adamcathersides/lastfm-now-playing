# lastfm-now

Show what a user is currently playing.

# Basic Usage

In order for this to work you will require a lastfm api key and secret.  Grab one [here](https://www.last.fm/api/account/create)

## Install

```
cd lastfm-now-playing
pip3 install .
```

## Run

`lastfm-now` will read the api key from `LASTFM_API_KEY` environment variables. It can also be specified on the command line.

### Environment variables - example

```
export LASTFM_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxx 
lastfm-now <username> 

```

### Command line options - example

```
lastfm-now --apikey xxxxxxxxxxxxxxxxxxxxxxxx <username> 

```

## CLI options

```
  -a, --apikey TEXT     Lastfm API key
  --log TEXT            Minimum log level to display [debug, info, warning, error, critical]
  --latch / --no-latch  Show most recently played track, even if not currently playing
  --prechars TEXT       Characters to be displayed before the output
  --postchars TEXT      Characters to be displayed after the output
  --help                Show this message and exit.
```
