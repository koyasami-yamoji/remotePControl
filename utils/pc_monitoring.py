import datetime
import time
from typing import Dict, List
from collections import namedtuple

import psutil

THRESHOLD = 100 * 1024 * 1024  # 100 mb


def get_cpu_information():
	cpu_percent = psutil.cpu_percent(interval=1)
	load_avg_1_5_15_min = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
	return {'cpu_percent': cpu_percent,
			'system_load': load_avg_1_5_15_min}


def get_time_pc_word():
	now = time.time()
	total_work_time = psutil.boot_time()
	result = datetime.datetime.fromtimestamp(now - total_work_time).strftime("%H:%M:%S")
	return {'time': result}


def get_memory_info():
	virtual_memory = psutil.virtual_memory().available
	result = f"{virtual_memory}"
	if virtual_memory <= THRESHOLD:
		result += "⚠ Warning"
	return {'virtual_memory': result}


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
	most_load_memory = {}

	process = [
		(p.pid, p.name(), p.memory_info().rss)
		for p in psutil.process_iter(['name', 'memory_info'])
		if p.memory_info().rss > 500 * 1024 * 1024
	]

	for proc in process:
		most_load_memory[proc[1]] = {
			'pid': proc[0],
			'used_memory': f"{round(proc[2] / 1024 / 1024, 1)} MB",
		}

	return most_load_memory


def kill_process(pid: int) -> str:
	if not psutil.pid_exists(pid):
		return 'Такого процесса не существует'
