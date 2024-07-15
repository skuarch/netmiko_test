from netmiko import SSHDetect, ConnectHandler
from getpass import getpass


def main():
    device = {
        "host": "localhost",
        "username": "skuarch",
        "password": "dragon3s12",
        "device_type": "autodetect",
    }

    with ConnectHandler(**device) as connection:
        connection.establish_connection()
        output = connection.send_command('ll')
        print(output)
        connection.disconnect()


if __name__ == '__main__':
    main()
