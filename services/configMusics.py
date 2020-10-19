import json

def updateWakeUpValue(value, config):
    config['wakeupMusic'] = value.get()
    with open('.\\.\\config.json', 'w') as data:
        json.dump(config, data)
        data.close()

def updateStartUpValue(value, config):
    config['startupMusic'] = value.get()
    with open('.\\.\\config.json', 'w') as data:
        json.dump(config, data)
        data.close()