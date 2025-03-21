import argparse
import textwrap
from datetime import datetime

from SSR import define
from SSR import storagespace
from SSR import reconstructor


class StorageSpaceReconstructorTool():
    """
    StorageSpaceReconstructor Tool

    """
    NAME = 'Storage Space Reconstructor(SSR)'
    VERSION = '1.0'
    DESCRIPTION = textwrap.dedent('\n'.join([
        '',
        'Storage Space Reconstructor(SSR)',
        '',
        'More information can be gathered from here:',
        '    https://github.com/KimVegetable/StorageSpaceReconstructor',
        '    RAID level list: simple, 2mirror, 3mirror, parity, 2parity',
        '    Windows version list: win8, win8.1, win10, winserver2012, winserver2016, winserver2019'
        '']))
    EPILOG = textwrap.dedent('\n'.join([
        '',
        'Example usage:',
        '',
        'Enter image full path with RAID level, windows version',
        '-inputs C:\\10GB.001 C:\\20GB.001 C:\\30GB.001 C:\\40GB.001 -level simple -win win10 -output C:\\result',
        '']))

    def __init__(self):
        """Initializes a StorageSpaceReconstructorTool.

        Args:
            input:

        """
        super(StorageSpaceReconstructorTool, self).__init__()

        self.show_info = False

    def ParseArguments(self, arguments):
        """Parses the command line arguments.

        Args:
            arguments (list[str]): command line arguments.

        """

        argument_parser = argparse.ArgumentParser(
            description=self.DESCRIPTION, epilog=self.EPILOG, add_help=False,
            formatter_class=argparse.RawDescriptionHelpFormatter)

        self.AddBasicOptions(argument_parser)

        ### Info argument group
        info_group = argument_parser.add_argument_group('informational arguments')

        self.AddInformationalOptions(info_group)

        date = datetime.now().strftime('%Y-%m-%d')

        argument_parser.add_argument(
            '-win', '--windows_version', action='store', dest='windows_version', type=str, help='Enter an windows version of the target.')

        argument_parser.add_argument(
            '-level', '--raid_level', action='store', dest='raid_level', type=str, help='Enter a RAID level of the target.')

        ### source
        argument_parser.add_argument(
            '-inputs', action='store', dest='inputs', nargs='+', type=str, help='Enter sources for RAID reconstruction.')

        ### source
        argument_parser.add_argument(
            '-output', action='store', dest='output',
            default=None, type=str, help=(
                'Enter an output path.'))

        try:
            options = argument_parser.parse_args(arguments)
        except UnicodeEncodeError:
            return False

        if options.inputs == None or options.windows_version == None or options.raid_level == None:
            return False
        #try:
        self.ParseOptions(options)
        # except Exception:
        #     return False

        return True

    def ParseOptions(self, options):
        """Parses the options.

        Args:
            options (argparse.Namespace): command line arguments.

        Raises:
            BadConfigOption: if the options are invalid.
        """
        # Check the list options first otherwise required options will raise.

        self.inputs = getattr(options, 'inputs', None)
        self.output = getattr(options, 'output', None)

        self.windows_version = getattr(options, 'windows_version', False)
        self.raid_level = getattr(options, 'raid_level', False)

    def GetVersionInformation(self):
        return '{0:s} v{1:s}'.format(self.NAME, self.VERSION)

    def AddBasicOptions(self, argument_group):
        version_string = self.GetVersionInformation()

        argument_group.add_argument(
            '-h', '--help', action='help',
            help='Show this help message and exit.')

        argument_group.add_argument(
            '--troubles', dest='show_troubleshooting', action='store_true',
            default=False, help='Show troubleshooting information.')

        argument_group.add_argument(
            '-V', '--version', dest='version', action='version',
            version=version_string, help='Show the version information.')

    def AddInformationalOptions(self, argument_group):
        argument_group.add_argument(
            '-d', '--debug', dest='debug', action='store_true', default=False,
            help='Enable debug output.')

        argument_group.add_argument(
            '-q', '--quiet', dest='quiet', action='store_true', default=False,
            help='Disable informational output.')

        argument_group.add_argument(
            '--info', dest='show_info', action='store_true', default=False,
            help='Print out information about supported plugins and parsers.')

        argument_group.add_argument(
            '--no_dependencies_check', '--no-dependencies-check',
            dest='dependencies_check', action='store_false', default=True,
            help='Disable the dependencies check.')

    def ReconstructVirtualDisk(self):
        raid_level = None
        windows_version = None
        if self.raid_level.lower() == 'simple':
            raid_level = define.Define.RAID_LEVEL_SIMPLE
        elif self.raid_level.lower() == '2mirror':
            raid_level = define.Define.RAID_LEVEL_2MIRROR
        elif self.raid_level.lower() == '3mirror':
            raid_level = define.Define.RAID_LEVEL_3MIRROR
        elif self.raid_level.lower() == 'parity':
            raid_level = define.Define.RAID_LEVEL_PARITY
        elif self.raid_level.lower() == '2parity':
            raid_level = define.Define.RAID_LEVEL_2PARITY
        else:
            print("Wrong RAID Level.")
            return False

        if self.windows_version.lower() == 'win8' or self.windows_version.lower() == 'win8.1':
            windows_version = define.Define.WINDOWS_8
        elif self.windows_version.lower() == 'win10':
            windows_version = define.Define.WINDOWS_10
        elif self.windows_version.lower() == 'winserver2012':
            windows_version = define.Define.WINDOWS_SERVER_2012
        elif self.windows_version.lower() == 'winserver2016':
            windows_version = define.Define.WINDOWS_SERVER_2016
        elif self.windows_version.lower() == 'winserver2019':
            windows_version = define.Define.WINDOWS_SERVER_2019
        elif self.windows_version.lower() == 'win11':
            windows_version = define.Define.WINDOWS_11
        else:
            print("Wrong Windows Version.")
            return False

        disk_list = list()
        for input in self.inputs:
            disk = storagespace.StorageSpace(windows_version, raid_level)

            if disk.open_disk(input):
                if disk.parse_disk():
                    pass
                else:
                    print("[Error] parse_disk (" + input + ")")
                    return False
            else:
                print("[Error] open_disk (" + input + ")")
                return False

            print("")
            disk_list.append(disk)


        recon = reconstructor.Reconstructor(windows_version, raid_level)
        for disk in disk_list:
            recon.add_disk(disk)

        print("")
        recon.parse_metadata()

        recon.restore_virtual_disk(output_path=self.output)

    def ShowInfo(self):
        print(self.NAME, self.VERSION, self.DESCRIPTION, self.EPILOG)