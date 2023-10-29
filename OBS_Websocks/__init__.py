'''OBS Actions'''

OBS_IP = 'localhost'
OBS_Port = '4455'
OBS_Password = ''

import logging
logger = logging.getLogger(__name__)
from eventmanager import Evt
from EventActions import ActionEffect
from RHUI import UIField, UIFieldType, UIFieldSelectOption
import simpleobsws
import asyncio
import asyncio_gevent

asyncio.set_event_loop_policy(asyncio_gevent.EventLoopPolicy())
loop = asyncio.get_event_loop()
ws = simpleobsws.WebSocketClient(url = 'ws://' + OBS_IP + ':' + OBS_Port, password = OBS_Password)

async def OBSConnect():
    try:
        await ws.connect()
        await ws.wait_until_identified()
        if simpleobsws.WebSocketClient.is_identified(ws):
            print("OBS Connected")
        else:
            print("*** OBS failed to connect ***")
    except:
        print("*** OBS Server is not active ***")

async def OBSDisconnect():
    try:
        if simpleobsws.WebSocketClient.is_identified(ws):
            await ws.disconnect()
            print("OBS Disconnected")
    except:
        pass
    
async def OBSRecord(recMode):  
    if recMode == '1':
        await ws.emit(simpleobsws.Request('StartRecord'))
    elif recMode == '2':
        await ws.emit(simpleobsws.Request('StopRecord'))

async def OBSScene(Scene_Select):
    if Scene_Select != '':
        await ws.emit(simpleobsws.Request('SetCurrentProgramScene', { 'sceneName': Scene_Select }))

class OBS_Actions():
    def __init__(self, rhapi):
        self._rhapi = rhapi

    def connectToOBS(self, args):
        loop.run_until_complete(OBSConnect())

    def disconnectFromOBS(self, args):
        loop.run_until_complete(OBSDisconnect())
    
    def obsMessageEffect(self, action, args):

        try:
            OBS_scene = action['scene']
        except:
            OBS_scene = ''
        try:
            OBS_record = action['record']
        except:
            OBS_record = 0
        try:
            OBS_Connect = action['connect']
        except:
            OBS_Connect = 0

        is_identified = simpleobsws.WebSocketClient.is_identified(ws)

        if (OBS_Connect != '0' and OBS_Connect != '') and not is_identified:
            print("OBS trying to connect...")
            loop.run_until_complete(OBSConnect())

        if is_identified:
            loop.run_until_complete(OBSScene(OBS_scene))
            loop.run_until_complete(OBSRecord(OBS_record))
            logger.debug("OBS scene changed to: {}, recording: {}". format(OBS_scene, OBS_record))

    def register_handlers(self, args):
        if 'register_fn' in args:
            for effect in [
                ActionEffect(
                    'OBS Actions',
                    self.obsMessageEffect,
                    [
                        UIField('scene', "OBS Scene", UIFieldType.TEXT),
                        UIField('record', "OBS Record", UIFieldType.SELECT, options=[
                            UIFieldSelectOption(0, "No change"),
                            UIFieldSelectOption(1, "Start recording"),
                            UIFieldSelectOption(2, "Stop recording"),
                        ], value=0),
                        UIField('connect', "OBS Connect", UIFieldType.SELECT, options=[
                            UIFieldSelectOption(0, "No action"),
                            UIFieldSelectOption(1, "Connect to OBS if not already connected"),
                        ], value=0),
                    ]
                )
            ]:
                args['register_fn'](effect)

def initialize(rhapi):
    obs = OBS_Actions(rhapi)
    rhapi.events.on(Evt.STARTUP, obs.connectToOBS)
    rhapi.events.on(Evt.SHUTDOWN, obs.disconnectFromOBS)
    rhapi.events.on(Evt.ACTIONS_INITIALIZE, obs.register_handlers)
  