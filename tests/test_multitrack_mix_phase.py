import pytest
import media.multitrack_mix_phase as mod

CASES = [
    ("resample_phase", (1)),
    ("solo_ramp", (1)),
    ("sidechain_order", (1)),
    ("timebase_norm", (1)),
    ("offline_path", (1)),
    ("quantize", (1)),
    ("bus_sum", (1)),
    ("validation", (1)),
    ("audit", (1)),
    ("fallback", (1)),
    ("latency_comp", (1)),
    ("metrics", (1)),
    ("long_project", (1)),
    ("monitor_match", (1)),
    ("determinism", (1)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
