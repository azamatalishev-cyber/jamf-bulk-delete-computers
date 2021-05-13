import jss
import pandas as pd
import click

jss_prefs = jss.JSSPrefs()
j = jss.JSS(jss_prefs)


def csv_to_list_conversion(csv):
    data = pd.read_csv(csv).values.tolist()
    return [''.join(ele) for ele in data]


def delete_computer(computer_name):
    try:
        j.Computer(computer_name).delete()
    except jss.exceptions.GetError:
        print('Could not find computer: {} '.format(computer_name))


def delete_mobile_device(device_name):
    try:
        j.MobileDevice(device_name).delete()
    except jss.exceptions.GetError:
        print('Could not find mobile device: {} '.format(computer_name))


def bulk_delete_mobile_devices(mobile_csv):
    for i in csv_to_list_conversion(mobile_csv):
        delete_mobile_device(i)


@click.command()
@click.option('--csv', prompt='Path to csv',
              help='Path to the csv with the objects you '
                   'would like to delete in Jamf')
def bulk_delete_computers(csv):
    for i in csv_to_list_conversion(csv):
        delete_computer(i)


if __name__ == '__main__':
    bulk_delete_computers()
