# https://iptc.atlassian.net/wiki/spaces/PMD/pages/649592833/Reading+and+writing+IPTC+metadata+in+Python+using+pyexiftool
# https://smarnach.github.io/pyexiftool/
# python -m pip install -U pyexiftool


import os

from exiftool import ExifToolHelper


def get_exif_key(file, key):
    if not os.path.exists(file):
        print(f"ERROR: file not found: {file}")
        return None

    try:
        with ExifToolHelper() as et:
            d = et.get_metadata(file)
            # pprint.pp(d[0][key])
            return d[0][key]

    except KeyError:
        raise


def print_all_exif(file):
    if not os.path.exists(file):
        print(f"ERROR: file not found: {file}")
        return None

    try:
        with ExifToolHelper() as et:
            for d in et.get_metadata(file):
                for k, v in d.items():
                    print(f"{k} = {v}")
    except KeyError:
        raise


def update_exif_keys(file, keys):
    if not os.path.exists(file):
        print(f"ERROR: file not found: {file}")
        return None

    try:
        with ExifToolHelper() as et:
            et.execute(*keys, "-m", file)
    except Exception as e:
        print(f"ERROR: {e}")
        return None


def update_exif_for_adobestock(title, description, keywords, file):
    if not os.path.exists(file):
        print(f"ERROR: file not found: {file}")
        return None

    key1 = f"-IPTC:Caption-Abstract={description}"
    key2 = f"-IPTC:ObjectName={title}"
    key3 = f"-IPTC:Keywords={keywords}"
    with ExifToolHelper() as et:
        et.execute(key1, key2, key3, "-m", file)


def clear_exif_for_midjourney(file):
    if not os.path.exists(file):
        print(f"ERROR: file not found: {file}")
        return None

    key1 = "-PNG:Author="
    key2 = "-PNG:Description="
    key3 = "-XMP:DigitalImageGUID="
    key4 = "-XMP:DigitalSourceType="
    with ExifToolHelper() as et:
        et.execute(key1, key2, key3, key4, file)


def get_exif_for_midjourney(file):
    if not os.path.exists(file):
        print(f"ERROR: file not found: {file}")
        return None

    key1 = "PNG:Description"
    key2 = "XMP:DigitalImageGUID"

    prompt = ""
    jobid = ""

    with ExifToolHelper() as et:
        d = et.get_metadata(file)

        if key1 in d[0]:
            prompt = d[0][key1]

        if key2 in d[0]:
            jobid = d[0][key2]

    return (prompt, jobid)


# these are the keys that Adobe Stock are looking for
# IPTC:Caption-Abstract
# IPTC:ObjectName
# IPTC:Keywords

# these are the keys that Midjourney sets
# PNG:Author: 'aardvark_fike',
# PNG:Description: 'zombie | in the style of black and white spiroglyphic --ar 1:1 --v 6 Job ID: f75d5778-5022-41d7-868b-79383372873a',
# XMP:DigitalImageGUID: 'f75d5778-5022-41d7-868b-79383372873a',
# XMP:DigitalSourceType: 'http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia',

# exiftool command to remove all metadata
# exiftool -all= -CommonIFD0= --icc_profile:all 'full path to file or folder'

# iptcHeaders = [
#     'title' => '2#005',
#     'headline' => '2#105',
#     'keywords' => '2#025'
# ];
