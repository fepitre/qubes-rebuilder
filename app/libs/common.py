DEBIAN = {
    "buster": "10",
    "bullseye": "11",
    "bookworm": "12",
    "unstable": ""
}

DEBIAN_ARCHES = {
    "x86_64": "amd64",
    "noarch": "all"
}


def is_qubes(dist):
    return dist.startswith("qubes")


def is_fedora(dist):
    return dist.startswith("fedora") or dist.startswith("fc")


def is_debian(dist):
    dist, package_sets = "{}+".format(dist).split('+', 1)
    return DEBIAN.get(dist, None) is not None
