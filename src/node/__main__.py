# Copyright (C) 2016-2021 Ben Cordero <bencord0@condi.me>
#
# This file is part of blog.condi.me.
#
# blog.condi.me is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# blog.condi.me is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with blog.condi.me.  If not, see <http://www.gnu.org/licenses/>.

# Run the `nodejs` binary, driven by python code
#
#   Start an interpreter
#
#   $ python -m node
#
import subprocess


def main():
    # Synchronous blocking call, wait for an exit code
    exit = subprocess.run(['node'])

    # Raises CalledProcessError if returncode != 0
    exit.check_returncode()


if __name__ == '__main__':
    main()
