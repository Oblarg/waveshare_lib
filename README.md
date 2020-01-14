# RPI Waveshare Lib

This is a simple library for using the WaveShare L76x GPS hat for the Raspberry Pi.

The library turns on sensing and runs a background thread that parses the incoming serial messages and pushes them into a queue, from which the most recent message of a given type can be queried synchronously without blocking.

The API exposes the following methods:

## Importing the Library

```python
import waveshare
```

## Start Serial Stream

```python
start()
```

This starts the stream of serial data from the device.  Prior to running this method, all getters will return `None`.

## Stop Serial Stream

```python
stop()
```

This stops the stream of serial data from the device.  Until it is re-started, all getters will return the last value published by the device.

## Read Data Packets

```python
get_gga()
```

```python
get_gsa()
```

```python
get_gsv()
```

```python
get_rmc()
```

For a description of the contents of each packet type, see: http://aprs.gids.nl/nmea/