import requests
import json

headers = {
    'authority': 'api.av.by',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://av.by',
    'referer': 'https://av.by/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-api-key': '5f76cde7ebefc9.04631320',
    'x-device-type': 'web.desktop',
}

response = requests.get('https://api.av.by/home/filters/home/init', headers=headers)

blocks = json.loads( response.content )["blocks"]
filters_ierarchy = {}


"""fi = {
    "model":{
        "rows":[
            
        ]
    },
    "summary":{},
    "extended":{
        "primary_extended":{
                "transmission_type":{
                    "fallbackType": "select",
                    "valueFormat": "value",
                    "id": 13,
                    "name": "transmission_type",
                    "nested": [],
                    "label": "Коробка передач",
                    "disabled": false,
                    "options": [
                        {
                            "id": 1,
                            "label": "автомат",
                            "intValue": 1
                        },
                        {
                            "id": 2,
                            "label": "механика",
                            "intValue": 2
                        }
                    ],
                    "constraints": [],
                    "visible": true,
                    "metadata": [],
                    "hasRelations": false,
                    "widget": "inline_select"
                },
                                {
                                    "fallbackType": "select",
                                    "valueFormat": "array",
                                    "id": 14,
                                    "name": "body_type",
                                    "nested": [],
                                    "label": "Кузов",
                                    "disabled": false,
                                    "options": [
                                        {
                                            "id": 23,
                                            "label": "внедорожник 3 дв.",
                                            "intValue": 23
                                        },
                                        {
                                            "id": 6,
                                            "label": "внедорожник 5 дв.",
                                            "intValue": 6
                                        },
                                        {
                                            "id": 7,
                                            "label": "кабриолет",
                                            "intValue": 7
                                        },
                                        {
                                            "id": 1,
                                            "label": "купе",
                                            "intValue": 1
                                        },
                                        {
                                            "id": 20,
                                            "label": "легковой фургон",
                                            "intValue": 20
                                        },
                                        {
                                            "id": 22,
                                            "label": "лимузин",
                                            "intValue": 22
                                        },
                                        {
                                            "id": 26,
                                            "label": "лифтбек",
                                            "intValue": 26
                                        },
                                        {
                                            "id": 21,
                                            "label": "микроавтобус грузопассажирский",
                                            "intValue": 21
                                        },
                                        {
                                            "id": 11,
                                            "label": "микроавтобус пассажирский",
                                            "intValue": 11
                                        },
                                        {
                                            "id": 4,
                                            "label": "минивэн",
                                            "intValue": 4
                                        },
                                        {
                                            "id": 8,
                                            "label": "пикап",
                                            "intValue": 8
                                        },
                                        {
                                            "id": 18,
                                            "label": "родстер",
                                            "intValue": 18
                                        },
                                        {
                                            "id": 5,
                                            "label": "седан",
                                            "intValue": 5
                                        },
                                        {
                                            "id": 2,
                                            "label": "универсал",
                                            "intValue": 2
                                        },
                                        {
                                            "id": 24,
                                            "label": "хэтчбек 3 дв.",
                                            "intValue": 24
                                        },
                                        {
                                            "id": 3,
                                            "label": "хэтчбек 5 дв.",
                                            "intValue": 3
                                        },
                                        {
                                            "id": 19,
                                            "label": "другой",
                                            "intValue": 19
                                        }
                                    ],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "select",
                                    "valueFormat": "array",
                                    "id": 15,
                                    "name": "engine_type",
                                    "nested": [],
                                    "label": "Тип двигателя",
                                    "disabled": false,
                                    "options": [
                                        {
                                            "id": 1,
                                            "name": "gasoline",
                                            "label": "бензин",
                                            "intValue": 1
                                        },
                                        {
                                            "id": 2,
                                            "name": "gasoline_propane_butane",
                                            "label": "бензин (пропан-бутан)",
                                            "intValue": 2
                                        },
                                        {
                                            "id": 3,
                                            "name": "gasoline_methane",
                                            "label": "бензин (метан)",
                                            "intValue": 3
                                        },
                                        {
                                            "id": 4,
                                            "name": "gasoline_hybrid",
                                            "label": "бензин (гибрид)",
                                            "intValue": 4
                                        },
                                        {
                                            "id": 5,
                                            "name": "diesel",
                                            "label": "дизель",
                                            "intValue": 5
                                        },
                                        {
                                            "id": 6,
                                            "name": "diesel_hybrid",
                                            "label": "дизель (гибрид)",
                                            "intValue": 6
                                        },
                                        {
                                            "id": 7,
                                            "name": "electro",
                                            "label": "электро",
                                            "intValue": 7
                                        }
                                    ],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "select",
                                    "valueFormat": "array",
                                    "id": 16,
                                    "name": "drive_type",
                                    "nested": [],
                                    "label": "Привод",
                                    "disabled": false,
                                    "options": [
                                        {
                                            "id": 1,
                                            "label": "передний привод",
                                            "intValue": 1
                                        },
                                        {
                                            "id": 2,
                                            "label": "задний привод",
                                            "intValue": 2
                                        },
                                        {
                                            "id": 3,
                                            "label": "подключаемый полный привод",
                                            "intValue": 3
                                        },
                                        {
                                            "id": 4,
                                            "label": "постоянный полный привод",
                                            "intValue": 4
                                        }
                                    ],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                }
                            ]
                        }
                    ]
                },
                {
                    "id": 87,
                    "type": "description_search",
                    "label": "",
                    "order": 1,
                    "propertyGroups": [
                        {
                            "id": 88,
                            "label": "",
                            "order": 1,
                            "properties": [
                                {
                                    "fallbackType": "string",
                                    "valueFormat": "value",
                                    "id": 35,
                                    "name": "description",
                                    "nested": [],
                                    "label": "Поиск по словам в описании к объявлению",
                                    "hint": "Например, «техосмотр» или «снята с учёта»",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [
                                        {
                                            "type": "str_len_max",
                                            "max": 100,
                                            "errorMessage": "Слишком длинный текст поиска"
                                        }
                                    ],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false,
                                    "widget": "description_search"
                                }
                            ]
                        }
                    ]
                },
                {
                    "id": 89,
                    "type": "default",
                    "label": "",
                    "order": 2,
                    "propertyGroups": [
                        {
                            "id": 90,
                            "label": "Продавец",
                            "order": 1,
                            "properties": [
                                {
                                    "fallbackType": "select",
                                    "valueFormat": "array",
                                    "id": 18,
                                    "name": "place_region",
                                    "nested": [],
                                    "label": "Область",
                                    "disabled": false,
                                    "options": [
                                        {
                                            "id": 1001,
                                            "name": "brest",
                                            "label": "Брестская обл.",
                                            "intValue": 1001
                                        },
                                        {
                                            "id": 1002,
                                            "name": "vitebsk",
                                            "label": "Витебская обл.",
                                            "intValue": 1002
                                        },
                                        {
                                            "id": 1003,
                                            "name": "gomel",
                                            "label": "Гомельская обл.",
                                            "intValue": 1003
                                        },
                                        {
                                            "id": 1004,
                                            "name": "grodno",
                                            "label": "Гродненская обл.",
                                            "intValue": 1004
                                        },
                                        {
                                            "id": 1005,
                                            "name": "minsk",
                                            "label": "Минская обл.",
                                            "intValue": 1005
                                        },
                                        {
                                            "id": 1006,
                                            "name": "mogilev",
                                            "label": "Могилевская обл.",
                                            "intValue": 1006
                                        }
                                    ],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "select",
                                    "valueFormat": "array",
                                    "id": 19,
                                    "name": "place_city",
                                    "nested": [],
                                    "label": "Город",
                                    "disabled": true,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "select",
                                    "valueFormat": "array",
                                    "id": 21,
                                    "name": "seller_type",
                                    "nested": [],
                                    "label": "",
                                    "disabled": false,
                                    "options": [
                                        {
                                            "id": 1,
                                            "label": "Частное лицо",
                                            "metadata": {
                                                "saved_filter_label": "частное лицо"
                                            },
                                            "intValue": 1
                                        },
                                        {
                                            "id": 2,
                                            "label": "Компания",
                                            "metadata": {
                                                "saved_filter_label": "компания"
                                            },
                                            "intValue": 2
                                        }
                                    ],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false,
                                    "widget": "checkbox_select"
                                }
                            ]
                        },
                        {
                            "id": 91,
                            "label": "Состояние",
                            "order": 2,
                            "properties": [
                                {
                                    "fallbackType": "select",
                                    "valueFormat": "array",
                                    "id": 20,
                                    "name": "condition",
                                    "nested": [],
                                    "label": "Состояние",
                                    "disabled": false,
                                    "options": [
                                        {
                                            "id": 1,
                                            "label": "новый",
                                            "intValue": 1
                                        },
                                        {
                                            "id": 2,
                                            "label": "с пробегом",
                                            "intValue": 2
                                        },
                                        {
                                            "id": 3,
                                            "label": "аварийный",
                                            "intValue": 3
                                        },
                                        {
                                            "id": 4,
                                            "label": "на запчасти",
                                            "intValue": 4
                                        }
                                    ],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "select",
                                    "valueFormat": "range",
                                    "id": 22,
                                    "name": "mileage_km",
                                    "nested": [],
                                    "label": "Пробег, км",
                                    "disabled": false,
                                    "options": [
                                        {
                                            "id": 10000,
                                            "label": "до 10 тыс.",
                                            "intValue": 10000
                                        },
                                        {
                                            "id": 20000,
                                            "label": "до 20 тыс.",
                                            "intValue": 20000
                                        },
                                        {
                                            "id": 30000,
                                            "label": "до 30 тыс.",
                                            "intValue": 30000
                                        },
                                        {
                                            "id": 40000,
                                            "label": "до 40 тыс.",
                                            "intValue": 40000
                                        },
                                        {
                                            "id": 50000,
                                            "label": "до 50 тыс.",
                                            "intValue": 50000
                                        },
                                        {
                                            "id": 60000,
                                            "label": "до 60 тыс.",
                                            "intValue": 60000
                                        },
                                        {
                                            "id": 70000,
                                            "label": "до 70 тыс.",
                                            "intValue": 70000
                                        },
                                        {
                                            "id": 80000,
                                            "label": "до 80 тыс.",
                                            "intValue": 80000
                                        },
                                        {
                                            "id": 90000,
                                            "label": "до 90 тыс.",
                                            "intValue": 90000
                                        },
                                        {
                                            "id": 100000,
                                            "label": "до 100 тыс.",
                                            "intValue": 100000
                                        },
                                        {
                                            "id": 110000,
                                            "label": "до 110 тыс.",
                                            "intValue": 110000
                                        },
                                        {
                                            "id": 120000,
                                            "label": "до 120 тыс.",
                                            "intValue": 120000
                                        },
                                        {
                                            "id": 130000,
                                            "label": "до 130 тыс.",
                                            "intValue": 130000
                                        },
                                        {
                                            "id": 140000,
                                            "label": "до 140 тыс.",
                                            "intValue": 140000
                                        },
                                        {
                                            "id": 150000,
                                            "label": "до 150 тыс.",
                                            "intValue": 150000
                                        },
                                        {
                                            "id": 160000,
                                            "label": "до 160 тыс.",
                                            "intValue": 160000
                                        },
                                        {
                                            "id": 170000,
                                            "label": "до 170 тыс.",
                                            "intValue": 170000
                                        },
                                        {
                                            "id": 180000,
                                            "label": "до 180 тыс.",
                                            "intValue": 180000
                                        },
                                        {
                                            "id": 190000,
                                            "label": "до 190 тыс.",
                                            "intValue": 190000
                                        },
                                        {
                                            "id": 200000,
                                            "label": "до 200 тыс.",
                                            "intValue": 200000
                                        },
                                        {
                                            "id": 210000,
                                            "label": "до 210 тыс.",
                                            "intValue": 210000
                                        },
                                        {
                                            "id": 220000,
                                            "label": "до 220 тыс.",
                                            "intValue": 220000
                                        },
                                        {
                                            "id": 230000,
                                            "label": "до 230 тыс.",
                                            "intValue": 230000
                                        },
                                        {
                                            "id": 240000,
                                            "label": "до 240 тыс.",
                                            "intValue": 240000
                                        },
                                        {
                                            "id": 250000,
                                            "label": "до 250 тыс.",
                                            "intValue": 250000
                                        },
                                        {
                                            "id": 260000,
                                            "label": "до 260 тыс.",
                                            "intValue": 260000
                                        },
                                        {
                                            "id": 270000,
                                            "label": "до 270 тыс.",
                                            "intValue": 270000
                                        },
                                        {
                                            "id": 280000,
                                            "label": "до 280 тыс.",
                                            "intValue": 280000
                                        },
                                        {
                                            "id": 290000,
                                            "label": "до 290 тыс.",
                                            "intValue": 290000
                                        },
                                        {
                                            "id": 300000,
                                            "label": "до 300 тыс.",
                                            "intValue": 300000
                                        },
                                        {
                                            "id": 350000,
                                            "label": "до 350 тыс.",
                                            "intValue": 350000
                                        },
                                        {
                                            "id": 400000,
                                            "label": "до 400 тыс.",
                                            "intValue": 400000
                                        },
                                        {
                                            "id": 450000,
                                            "label": "до 450 тыс.",
                                            "intValue": 450000
                                        },
                                        {
                                            "id": 500000,
                                            "label": "до 500 тыс.",
                                            "intValue": 500000
                                        }
                                    ],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": {
                                        "saved_filter_to_range_label": ""
                                    },
                                    "hasRelations": false,
                                    "widget": "range_max"
                                }
                            ]
                        },
                        {
                            "id": 92,
                            "label": "Объявления",
                            "order": 3,
                            "properties": [
                                {
                                    "fallbackType": "select",
                                    "valueFormat": "value",
                                    "id": 23,
                                    "name": "creation_date",
                                    "nested": [],
                                    "label": "Период публикации",
                                    "disabled": false,
                                    "options": [
                                        {
                                            "id": 10,
                                            "label": "за сегодня",
                                            "intValue": 10
                                        },
                                        {
                                            "id": 11,
                                            "label": "за 2 дня",
                                            "intValue": 11
                                        },
                                        {
                                            "id": 12,
                                            "label": "за 3 дня",
                                            "intValue": 12
                                        },
                                        {
                                            "id": 13,
                                            "label": "за 4 дня",
                                            "intValue": 13
                                        },
                                        {
                                            "id": 16,
                                            "label": "за неделю",
                                            "intValue": 16
                                        }
                                    ],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 24,
                                    "name": "video_url",
                                    "nested": [],
                                    "label": "С видео",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 26,
                                    "name": "has_nds",
                                    "nested": [],
                                    "label": "Цена с НДС",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": {
                                        "saved_filter_label": "цена с НДС"
                                    },
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 25,
                                    "name": "has_exchange",
                                    "nested": [],
                                    "label": "Возможен обмен",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 32,
                                    "name": "vin_checked",
                                    "nested": [],
                                    "label": "VIN проверен",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": {
                                        "saved_filter_label": "VIN проверен"
                                    },
                                    "hasRelations": false,
                                    "widget": "vin_checked"
                                }
                            ]
                        }
                    ]
                },
                {
                    "id": 93,
                    "type": "default",
                    "label": "",
                    "order": 3,
                    "propertyGroups": [
                        {
                            "id": 94,
                            "label": "Экстерьер",
                            "order": 1,
                            "properties": [
                                {
                                    "fallbackType": "select",
                                    "valueFormat": "array",
                                    "id": 17,
                                    "name": "color",
                                    "nested": [],
                                    "label": "Цвет кузова",
                                    "disabled": false,
                                    "options": [
                                        {
                                            "id": 1,
                                            "label": "белый",
                                            "intValue": 1
                                        },
                                        {
                                            "id": 2,
                                            "label": "бордовый",
                                            "intValue": 2
                                        },
                                        {
                                            "id": 3,
                                            "label": "жёлтый",
                                            "intValue": 3
                                        },
                                        {
                                            "id": 4,
                                            "label": "зелёный",
                                            "intValue": 4
                                        },
                                        {
                                            "id": 5,
                                            "label": "коричневый",
                                            "intValue": 5
                                        },
                                        {
                                            "id": 6,
                                            "label": "красный",
                                            "intValue": 6
                                        },
                                        {
                                            "id": 7,
                                            "label": "оранжевый",
                                            "intValue": 7
                                        },
                                        {
                                            "id": 8,
                                            "label": "серебристый",
                                            "intValue": 8
                                        },
                                        {
                                            "id": 9,
                                            "label": "серый",
                                            "intValue": 9
                                        },
                                        {
                                            "id": 10,
                                            "label": "синий",
                                            "intValue": 10
                                        },
                                        {
                                            "id": 11,
                                            "label": "фиолетовый",
                                            "intValue": 11
                                        },
                                        {
                                            "id": 12,
                                            "label": "чёрный",
                                            "intValue": 12
                                        },
                                        {
                                            "id": 13,
                                            "label": "другой",
                                            "intValue": 13
                                        }
                                    ],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 67,
                                    "name": "alloy_wheels",
                                    "nested": [],
                                    "label": "Легкосплавные диски",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 68,
                                    "name": "railings",
                                    "nested": [],
                                    "label": "Рейлинги на крыше",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 69,
                                    "name": "hitch",
                                    "nested": [],
                                    "label": "Фаркоп",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                }
                            ]
                        },
                        {
                            "id": 95,
                            "label": "Системы безопасности",
                            "order": 2,
                            "properties": [
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 37,
                                    "name": "abs",
                                    "nested": [],
                                    "label": "ABS",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 38,
                                    "name": "esp",
                                    "nested": [],
                                    "label": "ESP",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 39,
                                    "name": "anti_slip_system",
                                    "nested": [],
                                    "label": "Антипробуксовочная",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 40,
                                    "name": "immobilizer",
                                    "nested": [],
                                    "label": "Иммобилайзер",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 41,
                                    "name": "alarm",
                                    "nested": [],
                                    "label": "Сигнализация",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                }
                            ]
                        },
                        {
                            "id": 96,
                            "label": "Системы помощи",
                            "order": 3,
                            "properties": [
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 45,
                                    "name": "rain_detector",
                                    "nested": [],
                                    "label": "Датчик дождя",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 46,
                                    "name": "rear_view_camera",
                                    "nested": [],
                                    "label": "Камера заднего вида",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 47,
                                    "name": "parktronics",
                                    "nested": [],
                                    "label": "Парктроники",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 48,
                                    "name": "mirror_dead_zone_control",
                                    "nested": [],
                                    "label": "Контроль мертвых зон на зеркалах",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                }
                            ]
                        },
                        {
                            "id": 97,
                            "label": "Подушки",
                            "order": 4,
                            "properties": [
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 42,
                                    "name": "front_safebags",
                                    "nested": [],
                                    "label": "Передние",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 43,
                                    "name": "side_safebags",
                                    "nested": [],
                                    "label": "Боковые",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 44,
                                    "name": "rear_safebags",
                                    "nested": [],
                                    "label": "Задние",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                }
                            ]
                        }
                    ]
                },
                {
                    "id": 98,
                    "type": "default",
                    "label": "",
                    "order": 4,
                    "propertyGroups": [
                        {
                            "id": 99,
                            "label": "Интерьер",
                            "order": 1,
                            "properties": [
                                {
                                    "fallbackType": "select",
                                    "valueFormat": "array",
                                    "id": 29,
                                    "name": "interior_color",
                                    "nested": [],
                                    "label": "Цвет салона",
                                    "disabled": false,
                                    "options": [
                                        {
                                            "id": 1,
                                            "label": "светлый",
                                            "intValue": 1
                                        },
                                        {
                                            "id": 3,
                                            "label": "комби",
                                            "intValue": 3
                                        },
                                        {
                                            "id": 2,
                                            "label": "тёмный",
                                            "intValue": 2
                                        }
                                    ],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "select",
                                    "valueFormat": "array",
                                    "id": 28,
                                    "name": "interior_material",
                                    "nested": [],
                                    "label": "Материал салона",
                                    "disabled": false,
                                    "options": [
                                        {
                                            "id": 1,
                                            "label": "натуральная кожа",
                                            "intValue": 1
                                        },
                                        {
                                            "id": 2,
                                            "label": "искусственная кожа",
                                            "intValue": 2
                                        },
                                        {
                                            "id": 3,
                                            "label": "ткань",
                                            "intValue": 3
                                        },
                                        {
                                            "id": 4,
                                            "label": "велюр",
                                            "intValue": 4
                                        },
                                        {
                                            "id": 5,
                                            "label": "алькантара",
                                            "intValue": 5
                                        },
                                        {
                                            "id": 6,
                                            "label": "комбинированные материалы",
                                            "intValue": 6
                                        }
                                    ],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 50,
                                    "name": "panoramic_roof",
                                    "nested": [],
                                    "label": "Панорамная крыша",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 49,
                                    "name": "hatch",
                                    "nested": [],
                                    "label": "Люк",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 36,
                                    "name": "seven_seats",
                                    "nested": [],
                                    "label": "7 местная версия",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                }
                            ]
                        },
                        {
                            "id": 100,
                            "label": "Комфорт",
                            "order": 2,
                            "properties": [
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 61,
                                    "name": "drive_auto_start",
                                    "nested": [],
                                    "label": "Автозапуск двигателя",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 62,
                                    "name": "cruise_control",
                                    "nested": [],
                                    "label": "Круиз-контроль",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 63,
                                    "name": "steering_wheel_media_control",
                                    "nested": [],
                                    "label": "Управление мультимедиа с руля",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 64,
                                    "name": "electro_seat_adjustment",
                                    "nested": [],
                                    "label": "Электрорегулировка сидений",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 65,
                                    "name": "front_glass_lift",
                                    "nested": [],
                                    "label": "Передние электро-стеклоподъёмники",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 66,
                                    "name": "rear_glass_lift",
                                    "nested": [],
                                    "label": "Задние электро-стеклоподъёмники",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                }
                            ]
                        },
                        {
                            "id": 101,
                            "label": "Обогрев",
                            "order": 3,
                            "properties": [
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 51,
                                    "name": "seat_heating",
                                    "nested": [],
                                    "label": "Сидений",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 52,
                                    "name": "front_glass_heating",
                                    "nested": [],
                                    "label": "Лобового стекла",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 53,
                                    "name": "mirror_heating",
                                    "nested": [],
                                    "label": "Зеркал",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 54,
                                    "name": "steering_wheel_heating",
                                    "nested": [],
                                    "label": "Руля",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 55,
                                    "name": "autonomous_heater",
                                    "nested": [],
                                    "label": "Автономный отопитель",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                }
                            ]
                        },
                        {
                            "id": 102,
                            "label": "Климат",
                            "order": 4,
                            "properties": [
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 56,
                                    "name": "climate_control",
                                    "nested": [],
                                    "label": "Климат-контроль",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 57,
                                    "name": "conditioner",
                                    "nested": [],
                                    "label": "Кондиционер",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                }
                            ]
                        }
                    ]
                },
                {
                    "id": 103,
                    "type": "default",
                    "label": "",
                    "order": 5,
                    "propertyGroups": [
                        {
                            "id": 104,
                            "label": "Мультимедиа",
                            "order": 1,
                            "properties": [
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 70,
                                    "name": "aux_ipod",
                                    "nested": [],
                                    "label": "AUX или iPod",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 71,
                                    "name": "bluetooth",
                                    "nested": [],
                                    "label": "Bluetooth",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 72,
                                    "name": "cd_mp3_player",
                                    "nested": [],
                                    "label": "CD или MP3",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 73,
                                    "name": "usb",
                                    "nested": [],
                                    "label": "USB",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 74,
                                    "name": "media_screen",
                                    "nested": [],
                                    "label": "Мультимедийный экран",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 75,
                                    "name": "navigator",
                                    "nested": [],
                                    "label": "Штатная навигация",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                }
                            ]
                        },
                        {
                            "id": 105,
                            "label": "Фары",
                            "order": 2,
                            "properties": [
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 58,
                                    "name": "xenon_lights",
                                    "nested": [],
                                    "label": "Ксеноновые",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 59,
                                    "name": "fog_lights",
                                    "nested": [],
                                    "label": "Противотуманные",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                },
                                {
                                    "fallbackType": "boolean",
                                    "valueFormat": "value",
                                    "id": 60,
                                    "name": "led_lights",
                                    "nested": [],
                                    "label": "Светодиодные",
                                    "disabled": false,
                                    "options": [],
                                    "constraints": [],
                                    "visible": true,
                                    "metadata": [],
                                    "hasRelations": false
                                }
                            ]
                        }
                    ]
                }
            ]
        ]
    }
}"""


for filter_group in blocks:

    if type( filter_group ) == dict :
        #filters_ierarchy[ filter_group["name"] ]  = filter_group["rows"]
        filters_ierarchy[ filter_group["name"] ] = {}

        for row in filter_group["rows"] :
            #filters_ierarchy[ filter_group["name"] ][ f"""{row["id"]}.{row["type"]}.{row["label"]}""" ] = row["propertyGroups"]
            filters_ierarchy[ filter_group["name"] ][ f"""{row["id"]}.{row["type"]}.{row["label"]}""" ] = {}

            for pG in row["propertyGroups"]:
                #filters_ierarchy[ filter_group["name"] ][ f"""{row["id"]}.{row["type"]}.{row["label"]}""" ][ f"""{row["id"]}.{row["label"]}""" ] = pG["properties"]
                filters_ierarchy[ filter_group["name"] ][ f"""{row["id"]}.{row["type"]}.{row["label"]}""" ][ f"""{row["id"]}.{row["label"]}""" ] = {}

                for prop in pG["properties"] :
                    filters_ierarchy[ filter_group["name"] ][ f"""{row["id"]}.{row["type"]}.{row["label"]}""" ][ f"""{row["id"]}.{row["label"]}""" ][ prop["name"] ] = prop




with open( "blacksheet\\complete_filters\\filters_ierarchy\\filters.json", "w", encoding="utf-8" ) as f :
    json.dump( filters_ierarchy, f, indent=4, ensure_ascii=False )        