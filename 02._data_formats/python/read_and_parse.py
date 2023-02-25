import csv
import json
import xml.etree.ElementTree as ET
import yaml

# CSV
with open('../me.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

# JSON
with open('../me.json') as jsonfile:
    data = json.load(jsonfile)
    print(data)
    
# XML
tree = ET.parse('../me.xml')
root = tree.getroot()

name = root.find('name').text
age = root.find('age').text

hobbies = []
for hobby in root.find('hobbies').iter('hobby'):
    hobbies.append(hobby.text)

print(f"Name: {name}")
print(f"Age: {age}")
print("Hobbies: ")
for hobby in hobbies:
    print(f" - {hobby}")

# YAML
with open('../me.yaml', 'r') as file:
    data = yaml.safe_load(file)

name = data['name']
age = data['age']
hobbies = data['hobbies']

print(f"Name: {name}")
print(f"Age: {age}")
print("Hobbies: ")
for hobby in hobbies:
    print(f" - {hobby}")

# TXT
with open('../me.txt', 'r') as file:
    data = file.read()
    print(data)