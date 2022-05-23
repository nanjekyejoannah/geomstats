"""Unit tests for the Grassmannian."""

import geomstats.backend as gs
from geomstats.tests import np_backend
from tests.conftest import Parametrizer
from tests.data.grassmannian_data import (
    GrassmannianCanonicalMetricTestData,
    GrassmannianTestData,
)
from tests.geometry_test_cases import LevelSetTestCase, RiemannianMetricTestCase


class TestGrassmannian(LevelSetTestCase, metaclass=Parametrizer):
    skip_test_intrinsic_after_extrinsic = True
    skip_test_extrinsic_after_intrinsic = True

    testing_data = GrassmannianTestData()
    space = testing_data.space

    def test_belongs(self, n, k, point, expected):
        self.assertAllClose(self.space(n, k).belongs(point), gs.array(expected))


class TestGrassmannianCanonicalMetric(RiemannianMetricTestCase, metaclass=Parametrizer):
    skip_test_log_after_exp = True
    skip_test_exp_geodesic_ivp = True
    skip_test_log_is_tangent = not np_backend()

    testing_data = GrassmannianCanonicalMetricTestData()
    Metric = Connection = testing_data.Metric

    def test_exp(self, n, k, tangent_vec, base_point, expected):
        self.assertAllClose(
            self.Metric(n, k).exp(gs.array(tangent_vec), gs.array(base_point)),
            gs.array(expected),
        )
