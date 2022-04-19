_base_ = [
    '../_base_/models/deeplabv3plus_r50-d8_RTKClassBalanced.py',
    '../_base_/datasets/rtk.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_700k_rtk.py'
]
