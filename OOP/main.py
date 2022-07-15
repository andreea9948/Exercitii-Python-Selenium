import json
from CloudCtx import *
from HealthInst import *
import argparse


def sort_func_health(e):
    return e.health_inst.current_health


def sort_last_modif(e):
    return e.last_modif

#Add argument and parse
my_parser = argparse.ArgumentParser()
my_parser.add_argument('--file', action='store', type=str, required=True)

args = my_parser.parse_args()
print(f'Nume fisier:{args.file}')


#Open file
with open(args.file) as json_file:
    data = json.load(json_file)

cloudCtxs = []
N = len(data['imdata'])

#Get data from json
for entry in data['imdata']:
    entry = entry['hcloudCtx']

    #If not healthInst
    try:
        healthInstEntry = entry['children'][0]['healthInst']['attributes']
        healthInst = HealthInst(healthInstEntry['cur'], healthInstEntry['maxSev'])
    except IndexError:
        healthInst = HealthInst('0', '')

    cloudCtxEntry = entry['attributes']
    cloudCtxs.append(CloudCtx(cloudCtxEntry['name'], cloudCtxEntry['tenantName'], cloudCtxEntry['description'],
                     cloudCtxEntry['nameAlias'], cloudCtxEntry['ctxProfileName'], healthInst, cloudCtxEntry['modTs']))


#Display health for 3 entries
for i in range(3):
    cloudCtxs[i].display_health()

#Sort - health
cloudCtxs.sort(key=sort_func_health)
print()
for i in range(N):
    cloudCtxs[i].display()

#Count instances
print(f'Nr instante CloudCtx: {CloudCtx.countInstances}')

#Sort - last modif
cloudCtxs.sort(key=sort_last_modif, reverse=True)

print()
for i in range(N):
    cloudCtxs[i].display()
