import requests
import os
import pathlib

url = 'https://cloud.bluestacks.com/api/getdownloadnow?platform=win&win_version=10&mac_version=&client_uuid=75aa6930-e177-4f78-93a2-04ceafb91b89&app_pkg=&platform_cloud=%257B%2522description%2522%253A%2522Chrome%252091.0.4472.77%2520on%2520Windows%252010%252064-bit%2522%252C%2522layout%2522%253A%2522Blink%2522%252C%2522manufacturer%2522%253Anull%252C%2522name%2522%253A%2522Chrome%2522%252C%2522prerelease%2522%253Anull%252C%2522product%2522%253Anull%252C%2522ua%2522%253A%2522Mozilla%252F5.0%2520(Windows%2520NT%252010.0%253B%2520Win64%253B%2520x64)%2520AppleWebKit%252F537.36%2520(KHTML%252C%2520like%2520Gecko)%2520Chrome%252F91.0.4472.77%2520Safari%252F537.36%2522%252C%2522version%2522%253A%252291.0.4472.77%2522%252C%2522os%2522%253A%257B%2522architecture%2522%253A64%252C%2522family%2522%253A%2522Windows%2522%252C%2522version%2522%253A%252210%2522%257D%257D&preferred_lang=en&utm_source=&utm_medium=&gaCookie=GA1.2.1483974032.1623500083&gclid=&clickid=&msclkid=&affiliateId=&offerId=&transaction_id=&aff_sub=&first_landing_page=https%253A%252F%252Fwww.bluestacks.com%252F&referrer=https%253A%252F%252Fgithub.com%252Fnilanshu-bst%252FQA-Automation-Lead-assignment%252Fblob%252Fmain%252FREADME.md&download_page_referrer=&utm_campaign=homepage-dl-button-en&exit_utm_campaign=homepage-dl-button-en&incompatible=false&bluestacks_version=bs5'
filename = 'BlueStacksInstaller_5.0.220.1003.exe'
response = requests.get(url, stream=True)
with open(filename, 'wb') as f:
    f.write(response.content)

path = pathlib.Path().absolute()
stringPath = str(path)
os.system(stringPath + '/' + filename)