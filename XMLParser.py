import xml.etree.ElementTree as ET

def XMLParser(root):

    body = root.find(".//body")
    items = body.find(".//items")
    item = body.find(".//item")
    lunDayTag = item.find('.//lunDay')

    lunDay = lunDayTag.text

    return lunDay