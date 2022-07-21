from HomePage import *
from TableVersions import *
from TableReleases import *
from robot.libraries.BuiltIn import BuiltIn

class DownloadsPage(HomePage, TableReleases, TableVersions):
    
    @staticmethod
    def check_existing_releases(rls):
        if rls is not None:
            message =  f'Exista {len(rls)} release-uri pentru ultima versiune'
            BuiltIn().log(message)
        else:
            BuiltIn().fail('Nu exista release pentru ultima versiune')
            
    @staticmethod
    def compare_dates(older, newer):
        print(older, newer)
        if older > newer:
            message = f'Gresit - data primului release este {older} si a ultimului {newer}'
            BuiltIn().fail(message)
        else:
            message = f'Corect - data primului release este {older} si a ultimului {newer}'
            BuiltIn().pass_execution(message) 
    


