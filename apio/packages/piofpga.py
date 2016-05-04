# PioFPGA icestorm class

import click
import requests
requests.packages.urllib3.disable_warnings()

from os.path import join, expanduser

from ..installer import Installer


class PioFPGAInstaller(Installer):

    def __init__(self):
        self.packages_dir = join(expanduser('~'), '.platformio')

        self.package = 'pio-fpga'
        self.version = self._get_version()
        self.extension = 'zip'

    def install(self):
        click.secho("Installing FPGA support for platformio...")
        super(PioFPGAInstaller, self).install()
        click.secho("Now execute the following command:", fg='green')
        click.secho("   pio platforms install lattice_ice40", fg='green')

    def _get_download_url(self):
        url = '{0}/v0.{1}/{2}'.format(
            'https://github.com/FPGAwars/Platformio-FPGA/releases/download',
            self.version,
            self._get_package_name())
        return url

    def _get_package_name(self):
        name = '{0}-{1}.{2}'.format(
            self.package,
            self.version,
            self.extension)
        return name

    def _get_version(self):
        releases_url = 'https://api.github.com/repos/FPGAwars/Platformio-FPGA/releases/latest'
        response = requests.get(releases_url)
        releases = response.json()
        version = releases['tag_name'].split('.')[1]  # 0.X -> X
        return version
