# chatty: a container that writes to stdout

## Usage

```
$ docker run -t heldroe/chatty
```

## Options

```
$ docker run heldroe/chatty --help
    usage: chatty.py [-h] [--json] [-f FREQUENCY]

    optional arguments:
      -h, --help            show this help message and exit
      --json                log in JSON format
      -f FREQUENCY, --frequency FREQUENCY
                            log line frequency (log lines per second)
```

## Example

```
$ docker run -t heldroe/chatty --json --frequency=2
{"Hello": "World!"}
{"Hello": "World!"}
{"Hello": "World!"}
{"Hello": "World!"}
...
```

## Running without Docker

Without Docker you'll need Python to run chatty:

```
$ git clone git@github.com:Heldroe/chatty.git
$ cd chatty
$ ./chatty.py
```

## Possible improvements

* Write to `stderr`
* Make sure the frequency is within reasonable bounds (i.e. `> 0`)
* Customizable output (not just "Hello, World!")
