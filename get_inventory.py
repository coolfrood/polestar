#!/usr/bin/env python3

import json
import requests
import csv
import update_sheet

URL = 'https://pc-api.polestar.com/eu-north-1/preconfigured-cars/'
DEALERS = json.loads('''
[
  {
    "code": "USMJI0012",
    "name": "Polestar South Coast"
  },
  {
    "code": "USVNY0011",
    "name": "Polestar Los Angeles"
  },
  {
    "code": "USSTZ0014",
    "name": "Polestar Scottsdale"
  },
  {
    "code": "USPAO0013",
    "name": "Polestar San Jose"
  },
  {
    "code": "USSRF0013",
    "name": "Polestar Marin"
  },
  {
    "code": "USLTO0013",
    "name": "Polestar Denver"
  },
  {
    "code": "USBVW0012",
    "name": "Polestar Portland"
  },
  {
    "code": "USTUK0012",
    "name": "Polestar Bellevue"
  },
  {
    "code": "USAUS0020",
    "name": "Polestar Austin"
  },
  {
    "code": "USGPV0011",
    "name": "Polestar Grapevine"
  },
  {
    "code": "USGVY0011",
    "name": "Polestar Minneapolis"
  },
  {
    "code": "USTPA0024",
    "name": "Polestar Tampa"
  },
  {
    "code": "USCLT0024",
    "name": "Polestar Charlotte"
  },
  {
    "code": "USFHI0012",
    "name": "Polestar Detroit"
  },
  {
    "code": "USRKV0016",
    "name": "Polestar Washington DC"
  },
  {
    "code": "USBOS0018",
    "name": "Polestar Boston"
  },
  {
    "code": "USWPR0011",
    "name": "Polestar Westport"
  },
  {
    "code": "USNYC0031",
    "name": "Polestar Manhattan"
  },
  {
    "code": "USEHA0011",
    "name": "Polestar Short Hills"
  },
  {
    "code": "USLRV0011",
    "name": "Polestar Princeton"
  }
]
''')

CARS = {
    "operationName":"LoadResultsQuery",
    "variables":{"market":"us","includeValidFilters":True,"debug":False,"filters":[{"filterTypeId":"4","filterValues":[{"value":"534","featureCode":"534","isB2B":False}]},{"filterTypeId":"10","filterValues":[{"value":"2021","featureCode":"2021","isB2B":False},{"value":"2022","featureCode":"2022","isB2B":False}]}]},
    "query":"query LoadResultsQuery($market: String!, $includeValidFilters: Boolean!, $filters: [FilterValueGroupInput], $dealerCode: String, $debug: Boolean!, $stateCode: String) {\n  filterFunction(\n    market: $market\n    includeValidFilters: $includeValidFilters\n    filters: $filters\n    dealerCode: $dealerCode\n    debug: $debug\n    stateCode: $stateCode\n  ) {\n    debugInfo\n    b2b\n    timestamp\n    market\n    validFilters {\n      filterTypeId\n      featureType\n      filterValues {\n        value\n        featureCode\n        isB2B\n        thumbnailUrl\n      }\n      filterRanges {\n        upper\n        lower\n        featureCode\n        isB2B\n      }\n    }\n    filterResults {\n      pno34\n      modelYear\n      structureWeek\n      description\n      earliestDeliveryDate\n      visualizations {\n        name\n        views {\n          name\n          parameters {\n            urlTemplate\n            parameters {\n              required\n              values\n            }\n          }\n        }\n      }\n      cashPriceData {\n        totals {\n          car {\n            carTotalPrice {\n              id\n              label\n              value\n            }\n            carTotalBasicPrice {\n              id\n              label\n              value\n            }\n            carTotalTaxes {\n              id\n              label\n              value\n            }\n            carTotalVAT {\n              id\n              label\n              value\n            }\n            carTotalPriceExclVAT {\n              id\n              label\n              value\n            }\n            taxes {\n              name\n              amount\n              vatRate\n              vatPosition\n            }\n          }\n          extras {\n            extrasTotalPrice {\n              id\n              label\n              value\n            }\n            extrasBasicPrice {\n              id\n              label\n              value\n            }\n            extrasTotalVAT {\n              id\n              label\n              value\n            }\n            extrasTotalPriceExclVAT {\n              id\n              label\n              value\n            }\n          }\n          delivery {\n            deliveryChargePrice {\n              id\n              label\n              value\n            }\n            deliveryChargeBasicPrice {\n              id\n              label\n              value\n            }\n            deliveryChargeVAT {\n              id\n              label\n              value\n            }\n          }\n          grandTotal {\n            grandTotalCarExtras {\n              grandTotalCarExtrasPrice {\n                id\n                label\n                value\n              }\n              grandTotalCarExtrasBasicPrice {\n                id\n                label\n                value\n              }\n              grandTotalCarExtrasBeforeVAT {\n                id\n                label\n                value\n              }\n              grandTotalCarExtrasTax {\n                id\n                label\n                value\n              }\n              grandTotalCarExtrasVAT {\n                id\n                label\n                value\n              }\n            }\n          }\n        }\n        car {\n          type\n          code\n          price\n          vat\n          priceIncVat\n        }\n        extras {\n          id\n          price\n          vat\n          priceIncVat\n        }\n      }\n      fspPrices {\n        price\n        description\n        financeType\n        priceIsB2B\n      }\n      images {\n        icons {\n          rims\n          color\n          upholstery\n        }\n        location {\n          url\n          angles\n          resolutions\n        }\n        studio {\n          url\n          angles\n          resolutions\n        }\n      }\n      content {\n        excluded\n        filterTypeId\n        featureType\n        code\n        name\n        description\n        numericValue\n        dateValue\n        stringValue\n        images {\n          url\n          alt\n        }\n        thumbnail {\n          url\n          alt\n        }\n        isB2B\n        learnMore {\n          href\n          label\n        }\n        tyreLinks {\n          url\n          label\n        }\n      }\n      towbar {\n        excluded\n        filterTypeId\n        featureType\n        code\n        name\n        description\n        numericValue\n        dateValue\n        stringValue\n        cardTitle\n        labelForInfo\n        images {\n          url\n          alt\n        }\n        thumbnail {\n          url\n          alt\n        }\n        isB2B\n      }\n      wltpNedcSummary {\n        items {\n          redaName\n          name\n          description\n          value\n          unit\n        }\n      }\n      techData {\n        engineBev_LabelForPower\n        engineBev_TotalHp\n        engineBev_TotalKw\n        engineBev_LabelForTorque\n        engineBev_TotalTorqueNm\n        engineBev_LabelForBattery\n        engineBev_Batteries\n        engineHybrid_Batteries\n        labelForPerformanceRange\n        performance\n        engineBev_ElectricRange\n        engineBev_LabelForElectricMotors\n        engineBev_ElectricMotors\n        engineBev_ElectricRangeEpaMiles\n        labelForDivider\n        productFeatures {\n          excluded\n          featureType\n          code\n          name\n          description\n          images {\n            url\n            alt\n          }\n          thumbnail {\n            url\n            alt\n          }\n          isStandard\n          isDefault\n          isAccessory\n        }\n        engineBev_LabelForTrunkCapacityTotal\n        engineBev_TrunkCapacityTotal\n        seats\n        seatsLabel\n        driveTrain\n        seeAllFeatures {\n          href\n          label\n        }\n      }\n      dimensionsMetric {\n        wheelbaseLabel\n        wheelbaseValue\n        dimensions\n        dimensionsLabel\n      }\n      dimensionsImperial {\n        wheelbaseLabel\n        wheelbaseValue\n      }\n      interior360BaseUrl\n      exterior360BaseUrl\n      exteriorImageCount\n      environmentalImpactDetails {\n        label\n        linkUrl\n        isIncluded\n      }\n      packages {\n        filterTypeId\n        featureType\n        name\n        code\n        cardTitle\n        labelForInfo\n        description\n        numericValue\n        dateValue\n        stringValue\n        isB2B\n        images {\n          url\n          alt\n        }\n        thumbnail {\n          url\n          alt\n        }\n        excluded\n        totalSalesPrice\n        learnMore {\n          href\n          label\n        }\n      }\n    }\n    filters {\n      filterTypeId\n      featureType\n      filterValues {\n        value\n        featureCode\n        isB2B\n      }\n      filterRanges {\n        upper\n        lower\n        featureCode\n        isB2B\n      }\n    }\n  }\n}\n"
}

def to_row(space, car_data):
    packs = [x['name'] for x in car_data['content'] if x['featureType']=='Packages']
    return {
        'Space': space,
        'Configuration': car_data['pno34'],
        'Delivery Date': car_data['earliestDeliveryDate'],
        'Price': car_data['cashPriceData']['totals']['car']['carTotalPrice']['value'],
        'Exterior': next(x['name'] for x in car_data['content'] if x['featureType'] == 'Color'),
        'Interior': next(x['name'] for x in car_data['content'] if x['featureType'] == 'Upholstery'),
        'Wheels': next(x['name'] for x in car_data['content'] if x['featureType'] == 'Rims'),
        'Packs': '|'.join(packs),
        'Engine': next(x['name'] for x in car_data['content'] if x['featureType'] == 'Engine'),
        'Year': next(x['name'] for x in car_data['content'] if x['featureType'] == 'ModelYear')
    }


def fetch_data():
    fields = ['Space', 'Configuration', 'Delivery Date', 'Price', 'Exterior', 'Interior', 'Wheels', 'Packs', 'Engine', 'Year']
    with open('cars.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fields)
        writer.writeheader()
        for x in DEALERS:
            print(f'Looking for dealer {x["name"]}')
            CARS['variables']['dealerCode'] = x['code']
            resp = requests.post(URL, json=CARS)
            resp_data = json.loads(resp.text)
            for want in resp_data['data']['filterFunction']['filterResults']:
                writer.writerow(to_row(x['name'], want))

        
if __name__ == '__main__':
    fetch_data()
    update_sheet.update_sheet()
