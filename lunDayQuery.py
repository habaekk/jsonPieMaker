import xml.etree.ElementTree as ET

from urlHelper import urlHelper
from request import request
from XMLParser import XMLParser

class LunDayQuery():
    def __init__(self):
        pass
    
    def fetchLunDay(self, month, day, year):
        url = self.getUrl(month, day, year)
        xml = self.getXML(url)
        lunDay = self.parse(xml)
        
        return lunDay
    
    def parse(self, xmlRoot):
        lunD = XMLParser(xmlRoot)
        return lunD
    
    def getXML(self, url):
        xml = request(url)
        return xml
    
    def getUrl(self, month, day, year): # fetch 랑 get 이랑 차이가 뭐냐?
        url = urlHelper(month, day, year)
        return url