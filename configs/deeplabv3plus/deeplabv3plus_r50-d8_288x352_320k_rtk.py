_base_ = [
    '../_base_/models/deeplabv3plus_r50-d8.py',
    '../_base_/datasets/rtk.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_320k_rtk.py'
]
