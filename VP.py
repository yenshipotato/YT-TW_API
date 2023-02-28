import asyncio
import asyncore
import json
import websockets

req = {
    "apiName": "VTubeStudioPublicAPI",
    "apiVersion": "1.0",
    "requestID": "SomeID",
    "messageType": "AuthenticationRequest",
    "data": {
        "pluginName": "My Cool Plugin",
        "pluginDeveloper": "My Name",
        "authenticationToken": "TOKEN"
    }
}

req2 = {
    "apiName": "VTubeStudioPublicAPI",
    "apiVersion": "1.0",
    "requestID": "SomeID",
    "messageType": "HotkeyTriggerRequest",
    "data": {
        "hotkeyID": "hand"
    }
}

tint = {
    "apiName": "VTubeStudioPublicAPI",
    "apiVersion": "1.0",
    "requestID": "SomeID",
    "messageType": "ColorTintRequest",
    "data": {
        "colorTint": {
            "colorR": 64,
            "colorG": 210,
            "colorB": 230,
            "colorA": 255,
            "mixWithSceneLightingColor": 1
        },
        "artMeshMatcher": {
            "tintAll": False,
            "nameExact": ["BODY2", "ArtMesh1", "ArtMesh0"]
        }
    }
}
authenticationToken = "TOKEN"
reqS = str(req)


async def head(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps(req, indent=2).encode('utf-8'))
        name = await websocket.recv()

        await websocket.send(json.dumps(req2, indent=2).encode('utf-8'))
        name = await websocket.recv()
        print(f"(client) recv from server {name}")
        await asyncio.sleep(3)


async def color(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps(req, indent=2).encode('utf-8'))
        name = await websocket.recv()

        await websocket.send(json.dumps(tint, indent=2).encode('utf-8'))
        name = await websocket.recv()
        print(f"(client) recv from server {name}")
        await asyncio.sleep(3)
