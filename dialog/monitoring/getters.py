import datetime
import time
from os import environ, path

import psutil
from platform import uname, win32_edition
import GPUtil

THRESHOLD = 100 * 1024 * 1024  # 100 mb


async def get_pc_load_info(**kwargs):
	virtual_ram_info = get_memory_info()
	cpu_percent = get_cpu_information()
	gpu_info = get_gpu_info()
	return {'virtual_ram_info': virtual_ram_info,
			'cpu_percent': cpu_percent,
			'gpu_info': gpu_info}


async def platform_os(**kwargs):
	time_work_pc = get_time_pc_work()
	os_info = dict()
	if uname().system and uname().release:
		os_info.update({"Caption": f'{uname().system} {uname().release}'})
	elif uname().system and not uname().release:
		os_info.update({"Caption": f'{uname().system}'})
	elif uname().release and not uname().system:
		os_info.update({"Caption": f'{uname().release}'})
	if win32_edition():
		os_info.update({"EditionID": win32_edition()})
	if uname().version:
		os_info.update({"Version": uname().version})
	if environ['WINDIR']:
		os_info.update({"WindowsDirectory": environ['WINDIR']})
	if environ['USERNAME']:
		os_info.update({"UserName": environ['USERNAME']})
	if environ['USERPROFILE']:
		os_info.update({"InstallDate":
							datetime.datetime.fromtimestamp(path.getctime(environ['USERPROFILE'])).strftime(
								'%d.%m.%Y, %H:%M:%S')})
	os_info["time_work_pc"] = time_work_pc
	return os_info if os_info else False


def get_cpu_information():
	cpu_percent = psutil.cpu_percent(interval=1)
	return cpu_percent


def get_time_pc_work():
	now = time.time()
	total_work_time = psutil.boot_time()
	work_time = datetime.datetime.fromtimestamp(now - total_work_time).strftime("%H:%M:%S")
	return work_time


def get_memory_info():
	virtual_memory = psutil.virtual_memory().available
	result = f"{round(virtual_memory / 1024 / 1024)}"
	if virtual_memory <= THRESHOLD:
		result += "⚠ Warning"
	return result


async def get_disk_info(**kwargs):
	all_disc = psutil.disk_partitions(all=False)
	all_disc_result_info = []
	for i, disc in enumerate(all_disc):
		disc_usage = psutil.disk_usage(disc.device)
		disc_info = (
			i + 1,
			disc.device,
			round(disc_usage.total / 1024 / 1024 / 1024),
			round(disc_usage.used / 1024 / 1024 / 1024),
			round(disc_usage.free / 1024 / 1024 / 1024),
			disc_usage.percent
		)
		all_disc_result_info.append(disc_info)
	return {"discs": all_disc_result_info}


def get_all_process():
	process = {}
	for proc in psutil.process_iter(['pid', 'name']):
		process[proc.name()] = {
			'pid': proc.pid,
			'name': proc.name()
		}
	return process


def get_most_load_memory():
	process = [
		(p.pid, p.name(), round(p.memory_info().rss / 1024 / 1024, 1))
		for p in psutil.process_iter(['name', 'memory_info'])
		if p.memory_info().rss > 500 * 1024 * 1024
	]

	return {"most_load": process}


def kill_process(pid: int) -> str:
	if not psutil.pid_exists(pid):
		return 'Такого процесса не существует'


def get_gpu_info():
	gpu_info = [(gpu.name, gpu.temperature, gpu.driver, gpu.memoryTotal,
				 gpu.memoryUsed, gpu.memoryFree)
				for gpu in GPUtil.getGPUs()]
	return gpu_info[0]