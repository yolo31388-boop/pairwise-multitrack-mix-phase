# pairwise-multitrack-mix-phase

## 领域

游戏、图形与多媒体

## 主题

多轨混音相位

## 说明

重采样相位补偿、增益斜坡与离线一致。

初始状态下 `media/multitrack_mix_phase.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
