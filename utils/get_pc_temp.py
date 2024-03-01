import clr
import os

hwtypes = ['Mainboard', 'SuperIO', 'CPU', 'RAM', 'GpuNvidia', 'GpuAti', 'TBalancer', 'Heatmaster', 'HDD']


def initialize_openhardwaremonitor():
	file = rf'{os.getcwd()}\OpenHardwareMonitorLib.dll'
	clr.AddReference(file)

	from OpenHardwareMonitor import Hardware

	handle = Hardware.Computer()
	handle.MainboardEnabled = True
	handle.CPUEnabled = True
	handle.RAMEnabled = True
	handle.GPUEnabled = True
	handle.HDDEnabled = True
	handle.Open()
	return handle


def fetch_stats(handle):
	sensors_data = []
	for i in handle.Hardware:
		i.Update()
		for sensor in i.Sensors:
			data = parse_sensor(sensor)
			if data:
				sensors_data.append(data)
		for j in i.SubHardware:
			j.Update()
			for subsensor in j.Sensors:
				data = parse_sensor(subsensor)
				if data:
					sensors_data.append(data)
	return sensors_data


def parse_sensor(sensor):
	if sensor.Value:
		if str(sensor.SensorType) == 'Temperature':
			type_name = hwtypes[sensor.Hardware.HardwareType]
			return [(f"{type_name}. {sensor.Hardware.Name!r} "
				  f"#{sensor.Index} - {sensor.Value}°C")]


async def get_sensor_data(**kwargs):
	hardware_handle = initialize_openhardwaremonitor()
	data = fetch_stats(hardware_handle)
	return {'sensor_data': data}
