# rileylink\_lights

This is a quick hack to hook up my cheap RF remote LED lights
(FCC ID N9STY-16F and N9STY-R-434) to HomeKit. The script runs on a
Raspberry Pi and uses a [RileyLink](https://github.com/ps2/rileylink)
to bridge to the 433MHz that the lights speak. [HomeBridge](https://github.com/nfarina/homebridge)
and [homebridge-http-lightbulb](https://github.com/Supereg/homebridge-http-lightbulb) complete
the setup.

Here's the relevant part of my HomeBridge config.json:

```
    {
      "accessory": "HTTP-LIGHTBULB",
      "name": "Christmas Lights",
      "onUrl": "http://localhost:8999/on",
      "offUrl": "http://localhost:8999/off",
      "statusUrl": "http://localhost:8999/state",
      "statusPattern": "on"
    }
```

