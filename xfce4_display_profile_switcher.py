#!/usr/bin/env python3
import argparse
import subprocess
import re

parser = argparse.ArgumentParser()
parser.add_argument(
    "-s", "--set-profile", help="set profile with given id", type=str, metavar='PROFILE_ID'
)
parser.add_argument(
    "-l", "--list-profiles", help="list profiles", action="store_true"
)


class XconfQuery:
    def __init__(self):
        self.xconf_query_command = "xfconf-query"

    def run_xconf_query(self, *arguments):
        return subprocess.check_output([self.xconf_query_command, *arguments])

    def get_values(self, channel):
        raw_values = self.run_xconf_query('-l', '-v', '-c', channel)
        values = {}

        for value in raw_values.split(b'\n'):
            result = re.search(r'(^[^\s]*)\s+([\w\d\-\._]+.*)', value.decode('utf8'))
            if not result:
                continue
            try:
                values[result.group(1)] = result.group(2)
            except IndexError:
                pass
        return values


class DisplayProfiles:
    def __init__(self):
        self.xq = XconfQuery()

    def get_profiles(self):
        displays = self.xq.get_values('displays')
        profiles = {}
        regexp = r'^/[\d\w]+/.*/EDID$'
        profile_ids = set([
            k.split('/')[1] for (k, v) in displays.items()
            if re.search(regexp, k, re.IGNORECASE) and not (k.startswith('/Default') or k.startswith('/Fallback'))
        ])
        active = displays.get('/ActiveProfile')

        for profile_id in profile_ids:
            profiles[profile_id] = {
                'name': displays.get(f'/{profile_id}'),
                'active': profile_id == active
            }

        return profiles

    def print_profiles(self):
        profiles = self.get_profiles()
        for profile_id, values in profiles.items():
            print(f"id: {profile_id}, name: {values['name']}" + (" (active)" if values.get('active') else ''))

    def set_profile(self, profile_id):
        self.xq.run_xconf_query(
            "--create", '-c', 'displays', '-p', '/Schemes/Apply', '-t', 'string', '-s', profile_id
        )


if __name__ == "__main__":
    dp = DisplayProfiles()
    args = parser.parse_args()

    if args.list_profiles:
        dp.print_profiles()
    elif args.set_profile:
        dp.set_profile(args.set_profile)
    else:
        parser.print_help()
