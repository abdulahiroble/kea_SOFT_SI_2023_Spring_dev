import os
import csv
import json
import xml.etree.ElementTree as ET
from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

routes = APIRouter()

routes.get("/")

def _():
    return {"message": "First FastAPI route"}


# From JSON to CSV
@routes.get("/csv", status_code=200)
async def read_csv(response: Response):
    file_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "../../files/me.json"))
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        data = []
        for row in csvreader:
            data.append(row)
    return JSONResponse(content=data, status_code=200)


# From CSV to JSON
@routes.get('/json', status_code=200)
async def read_csv():
    file_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "../../files/me.csv"))
    with open(file_path, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        rows = [row for row in csvreader]
    return rows

# From JSON to XML
@routes.get('/xml', status_code=200)
async def read_json():
    file_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "../../files/me.json"))
    with open(file_path, 'r') as f:
        json_data = json.load(f)

    # Convert the JSON data to an ElementTree object
    root = ET.Element('root')
    for key, value in json_data.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    # Convert the ElementTree object to an XML string
    xml_string = ET.tostring(root)

    # Return the XML response
    return Response(content=xml_string, media_type='application/xml')