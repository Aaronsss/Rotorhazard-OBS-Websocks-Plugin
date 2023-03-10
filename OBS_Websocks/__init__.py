'''OBS Interface'''

OBS_IP = 'localhost'
OBS_Port = '4455'
OBS_Password = ''

import logging
logger = logging.getLogger(__name__)
from eventmanager import Evt
from EventActions import ActionEffect
import simpleobsws
import asyncio
import asyncio_gevent

asyncio.set_event_loop_policy(asyncio_gevent.EventLoopPolicy())
loop = asyncio.get_event_loop()

ws = simpleobsws.WebSocketClient(url = 'ws://' + OBS_IP + ':' + OBS_Port, password = OBS_Password) 

def connectToOBS(args):
    loop.run_until_complete(OBSConnect())

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

def disconnectFromOBS(args):
    loop.run_until_complete(OBSDisconnect())

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
    
def registerHandlers(args):
    if 'registerFn' in args:
        for effect in obsdiscover():
            args['registerFn'](effect)

def initialize(**kwargs):
    if 'Events' in kwargs:
        kwargs['Events'].on(Evt.STARTUP, 'OBS_Websocks_Interface', connectToOBS, {}, 75)
        kwargs['Events'].on(Evt.SHUTDOWN, 'OBS_Websocks_Interface', disconnectFromOBS, {}, 75)
        kwargs['Events'].on('actionsInitialize', 'OBS_Websocks_Interface', registerHandlers, {}, 120, True)
        
def obsMessageEffect(action, args):

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

def obsdiscover():
    return [
        ActionEffect(
            'obsmessage',
            'OBS Message',
            obsMessageEffect,
            [
                {
                    'id': 'scene',
                    'name': 'OBS Scene',
                    'type': 'text',
                },
                {
                    'id': 'record',
                    'name': 'OBS Record (0 - no change, 1 - record, 2 - stop)',
                    'type': 'text',
                },                
                {
                    'id': 'connect',
                    'name': 'OBS Connect (Try to connet to OBS)',
                    'type': 'text',
                }
            ]
        )
    ]
