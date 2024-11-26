# vpngate-pick

A command-line tool to fetch and decode a random OpenVPN configuration from [VPN Gate](https://www.vpngate.net/ja/).

## Description

`vpngate-pick` retrieves VPN server information from VPN Gate's public CSV, randomly selects one server, and outputs its OpenVPN configuration. This tool can be used to quickly get a working OpenVPN configuration without visiting the VPN Gate website.

## Usage

Save the OpenVPN configuration:

```bash
$ ./vpngate-pick > client.ovpn
```

The script will:

1. Fetch the server list from VPN Gate
2. Randomly select one server
3. Decode its OpenVPN configuration
4. Output the configuration to stdout

If successful, the configuration will be saved to `client.ovpn` (or any filename you specify). If an error occurs, the script will exit with status code 1.

Connect to the OpenVPN server:

```bash
$ sudo openvpn --config client.ovpn
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) for details.
