# Copyright 2025 stawwik <stawwik@gmail.com>
# MIT License


import re


def validate(email_str: str) -> str:
    """
    Uses regex to validate passed string as email address.
    Regex has been tested here: https://regex101.com/r/Ft7l0d/1
    
    Parameters
    ----------
    email_str: str
        String to be validated.

    Returns
    -------
    msg: str
        String stating whether validation was successful or not.
    """""
    # Variables with messages to be returned.
    msg_valid = 'Email is valid.'
    msg_invalid = 'Email is invalid!'
    regex_str = (r"^(?![.-])"  # Before next group there is no [.-].
                 r"([\w.-]*)"  # Local part.
                 r"((?<![.-])@(?![.-])[a-zA-Z0-9.-]+)"  # Domain. Before or 
                 # after @ sign, there is no [.-].
                 r"((?<![.-])\.[a-zA-Z0-9]{2,})$")  # Top-level domain. Before
                 # it there is no [.-] (no double dots). At least 2 chars. No
                 # special character at the end of string.

    # Fast workaround for double dots or hyphens in local part or domain.
    if ('..' in email_str) or ('--' in email_str):
        return msg_invalid

    pattern = re.compile(regex_str)
    match = pattern.match(email_str)

    if match:
        return msg_valid
    else:
        return msg_invalid


if __name__ == '__main__':
    print('Pass email address for validation.')
    email = input('>')

    print(validate(email))
