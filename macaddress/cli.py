#!/usr/bin/env python3

import click

from macaddress import api


def display_info(device_info):
    if device_info["vendorDetails"]["companyName"]:
        print("Company Name : {}".format(device_info["vendorDetails"]["companyName"]))
    else:
        print("Device information not found")


def get_device_info(server, token, address):
    """Fetch device information from macaddress server"""

    if not server:
        raise SystemExit(
            "Error: Mac Address Server URI is not present. Add '--server' flag or MAC_ADDRESS_SERVER variable in your environment"
        )

    if not token:
        raise SystemExit(
            "Error: Mac Address Token is not present. Add '--token' flag or MAC_ADDRESS_TOKEN variable in your environment"
        )

    return api.get_device_info(server, token, address)


@click.group()
def cli():
    pass


@cli.command("search")
@click.option("--server", default="https://api.macaddress.io", help="Server address")
@click.option("--token", help="API token")
@click.option("--address", help="MAC address")
def search(server, token, address):
    """Run a command to get the device information"""
    device_info = get_device_info(server, token, address)
    display_info(device_info)


if __name__ == "__main__":
    cli()
