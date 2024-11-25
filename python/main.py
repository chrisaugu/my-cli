#!/usr/bin/env python
import json
import os
import click
from myssh import run_command_on_device

@click.group()
def cli():
    pass

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.argument('name')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

@click.command()
def initdb():
    click.echo('Initialized the database')

@click.command()
def dropdb():
    click.echo('Dropped the database')

@click.command()
@click.option(
    "--hostname", prompt=True,
    help='Your hostname',
    default='172.30.4.54'
)
@click.option(
    "--username", prompt='Enter username',
    default=lambda: os.environ.get("USER", "")
)
@click.password_option(
    "--password", prompt=True,
    help='Enter password',
    confirmation_prompt=False
)
def remote_connect(hostname, username, password):
    # hostname = click.prompt('Enter hostname', default='172.30.4.54')
    # username = click.prompt('Enter username')
    # password = click.prompt('Enter password')
    click.echo('Initiating connection')
    click.echo(f'connecting to {username}@{hostname} ...')

    router_output = run_command_on_device(hostname, username, password, "df -h")

    # Use perplexity to serialized this
    # Initialize an empty list to hold the parsed entries
    filesystems = []

    # Parse the data
    for line in router_output[1:]: # Skip the header
        parts = line.split()
        
        # Create a dictionary for each filesystem entry
        if len(parts) >= 6:
            filesystem_entry = {
                "Filesystem": parts[0],
                "Size": parts[1],
                "Used": parts[2],
                "Avail": parts[3],
                "Use%": parts[4],
                "Mounted on": parts[5]
            }
            filesystems.append(filesystem_entry)

    # Serialize to JSON
    json_output = json.dumps(filesystems, indent=4)

    # Print the resulting JSON
    click.echo(json_output)
    # if router_output != None:
    #     for line in router_output:
    #         if "/dev/sda2" in line:
    #             click.echo("Found default route:")
    #             s = line.split('\n')
    #             click.echo(s)

cli.add_command(initdb)
cli.add_command(dropdb)
cli.add_command(remote_connect)

if __name__ == '__main__':
    # hello()
    cli()