# SPDX-FileCopyrightText: 2021 Aaron Dewes <aaron.dewes@protonmail.com>
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import os
import subprocess

scriptDir = os.path.dirname(os.path.realpath(__file__))
nodeRoot = os.path.join(scriptDir, "..", "..")

def deriveEntropy(identifier: str):
    seedFile = os.path.join(nodeRoot, "db", "citadel-seed", "seed")
    alternativeSeedFile = os.path.join(nodeRoot, "db", "citadel-seed", "seed")
    if not os.path.isfile(seedFile):
        if os.path.isfile(alternativeSeedFile):
            seedFile = alternativeSeedFile
        else:
            print("No seed file found, exiting...")
            exit(1)
    with open(seedFile, "r") as f:
        node_seed = f.read().strip()
    entropy = subprocess.check_output(
        'printf "%s" "{}" | openssl dgst -sha256 -binary -hmac "{}" | xxd -p | tr --delete "\n"'.format(identifier, node_seed), shell=True)
    return entropy.decode("utf-8")
