import os

from bs4 import BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://www.pythonforbeginners.com/beautifulsoup/python-beautifulsoup-basic


def get_file_tags(tags, file_name):
    [base_name, ext] = os.path.splitext(file_name)
    ext = ext.replace(".", "")

    found_tags = []
    tag_string = ""

    for tag in tags:
        if f"_{tag}" in base_name:
            found_tags.append(tag)
            base_name = base_name.replace(f"_{tag}", "")

    if found_tags:
        tag_string = ", ".join(found_tags)
    else:
        tag_string = ext

    return [base_name, tag_string]



def metadata_from_log(html, imgfile):
    soup = BeautifulSoup(html, "html.parser")
    id = imgfile.replace(".", "_")
    # print(f"id = {id}")
    d = soup.find("div", attrs={"id": id})
    result = {}

    if d:
        metadata_tables = d.find_all("table", class_="metadata")

        # print(f"table = {metadata_tables}")

        for table in metadata_tables:
            labels = [
                label.text for label in table.find_all("td", class_=["label", "key"])
            ]
            values = [
                value.text.strip() for value in table.find_all("td", class_="value")
            ]
            metadata = dict(zip(labels, values))
            result.update(metadata)

    return result


def metadata_from_oldlog(html, imgfile):
    soup = BeautifulSoup(html, "html.parser")
    id = imgfile.replace(".", "_")
    # print(f"id = {id}")
    d = soup.find("div", attrs={"id": id})

    if d:
        return str(d)
