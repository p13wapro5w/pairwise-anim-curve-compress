import pytest
from animation import curve_compress as mod

CASES = [
    ("error_true", 'm.error_ok(0.1, 0.2) is True'),
    ("error_false", 'm.error_ok(0.3, 0.2) is False'),
    ("quat_x", 'm.normalize_quat((2.0, 0.0, 0.0, 0.0)) == approx((1.0, 0.0, 0.0, 0.0))'),
    ("quat_y", 'm.normalize_quat((0.0, 2.0, 0.0, 0.0)) == approx((0.0, 1.0, 0.0, 0.0))'),
    ("loop_match", 'm.loop_ok(1.0, 1.0) is True'),
    ("loop_mismatch", 'm.loop_ok(1.0, 2.0) is False'),
    ("phase_half", 'm.phase_diff(0.5, 0.2) == approx(0.3)'),
    ("root_fine", 'm.root_precision(1.234, 0.001) == approx(1.234)'),
    ("root_coarse", 'm.root_precision(1.234, 1.0) == approx(1.0)'),
    ("event_lock", 'm.lock_event(0.11, 0.10, 0.05) == approx(0.10)'),
    ("event_keep", 'm.lock_event(0.20, 0.10, 0.05) == approx(0.20)'),
    ("fps_up", 'm.sample_rate_scale(30, 60) == approx(2.0)'),
    ("fps_down", 'm.sample_rate_scale(60, 30) == approx(0.5)'),
    ("bounds", 'm.recompute_bounds(1.0, 3.0, 0.5) == approx((0.5, 3.5))'),
    ("mirror", 'm.mirror_curve([1, 2, 3]) == [3, 2, 1]')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
