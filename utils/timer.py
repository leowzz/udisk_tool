#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author LeoWang
# @date 2023/1/10
# @file timer.py
import time
import functools
from utils.setting import setting__
from utils.log import get_logger
logger = get_logger("timer", setting__.get_log_level())


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()  # 2
        run_time = end_time - start_time  # 3
        logger.info(f"Finished {func.__name__!r} in {run_time:.4f} secs.")
        return value

    return wrapper_timer


def timer_ns(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter_ns()  # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter_ns()  # 2
        run_time = end_time - start_time  # 3
        logger.info(f"Finished {func.__name__!r} in {run_time:.4f} ns, {run_time/1e9:.5f} s.")
        return value

    return wrapper_timer
