# ============================================================================#
# ============================ARCANE CALCULATOR===============================#
# ============================================================================#

import hashlib
import sys

from fernet import Fernet
import base64

# GLOBALS --v
arcane_loop_trial = True
jump_into_full = False
full_version_code = ""

username_trial = "MORTON"
bUsername_trial = b"MORTON"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"  # 75fc1081
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial


def get_hash(username_trial):
    ans = ''
    ans += hashlib.sha256(username_trial).hexdigest()[4]
    ans += hashlib.sha256(username_trial).hexdigest()[5]
    ans += hashlib.sha256(username_trial).hexdigest()[3]
    ans += hashlib.sha256(username_trial).hexdigest()[6]
    ans += hashlib.sha256(username_trial).hexdigest()[2]
    ans += hashlib.sha256(username_trial).hexdigest()[7]
    ans += hashlib.sha256(username_trial).hexdigest()[1]
    ans += hashlib.sha256(username_trial).hexdigest()[8]
    return ans


print(f'{key_part_static1_trial}{get_hash(bUsername_trial)}{key_part_static2_trial}')
