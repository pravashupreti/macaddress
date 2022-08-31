# MACADDRESS

MACADDRESS is a simple CLI tool to fetch device info using its MAC address/OUI/IAB.

## Installation

`macaddress` requires `docker` installed.

```sh
$ docker build -t macaddress .
```

Create alias

```sh
$ alias macaddress="docker run macaddress"
```

## Usage

### Search mac address

```
$ macaddress search  --token=<MAC_ADDRESS_TOKEN> --address=<MAC_ADDRESS_VALUE>
```

### Example

```sh
$ macaddress search --token=<YOUR_API_TOKEN> --address=44:38:39:ff:ef:57
Company Name : Cumulus Networks, Inc
```

### Security

The tool uses the rest api endpoint to fetch the device information. The api token is passed on HTTPS header for authentication.
