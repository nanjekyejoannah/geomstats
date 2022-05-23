import random

import geomstats.backend as gs
from geomstats.information_geometry.beta import BetaDistributions, BetaMetric
from tests.data_generation import _OpenSetTestData, _RiemannianMetricTestData


class BetaDistributionsTestsData(_OpenSetTestData):
    space = BetaDistributions
    space_args_list = [()]
    shape_list = [(2,)]
    n_samples_list = random.sample(range(2, 5), 2)
    n_points_list = random.sample(range(1, 5), 2)
    n_vecs_list = random.sample(range(2, 5), 2)

    def belongs_test_data(self):
        smoke_data = [
            dict(dim=3, vec=[0.1, 1.0, 0.3], expected=True),
            dict(dim=3, vec=[0.1, 1.0], expected=False),
            dict(dim=3, vec=[0.0, 1.0, 0.3], expected=False),
            dict(dim=2, vec=[-1.0, 0.3], expected=False),
        ]
        return self.generate_tests(smoke_data)

    def random_point_test_data(self):
        random_data = [
            dict(point=self.space(2).random_point(1), expected=(2,)),
            dict(point=self.space(3).random_point(5), expected=(5, 3)),
        ]
        return self.generate_tests([], random_data)

    def point_to_pdf_test_data(self):
        smoke_data = [dict(x=gs.linspace(0.0, 1.0, 10))]
        return self.generate_tests(smoke_data)

    def point_to_pdf_vectorization_test_data(self):
        smoke_data = [dict(x=gs.linspace(0.0, 1.0, 10))]
        return self.generate_tests(smoke_data)


class BetaMetricTestData(_RiemannianMetricTestData):

    metric_args_list = [()]
    shape_list = [(2,)]
    space_list = [BetaDistributions()]
    n_samples_list = random.sample(range(2, 5), 2)
    n_points_a_list = n_points_b_list = n_points_list = random.sample(range(1, 5), 2)
    n_tangent_vecs_list = n_vecs_list = random.sample(range(2, 5), 2)

    Space = BetaDistributions
    Metric = BetaMetric

    def metric_matrix_test_data(self):
        smoke_data = [
            dict(
                point=gs.array([1.0, 1.0]),
                expected=gs.array([[1.0, -0.644934066], [-0.644934066, 1.0]]),
            )
        ]
        return self.generate_tests(smoke_data)

    def exp_test_data(self):
        smoke_data = [dict(n_samples=10)]
        return self.generate_tests(smoke_data)

    def christoffels_shape_test_data(self):
        smoke_data = [dict(n_samples=10)]
        return self.generate_tests(smoke_data)
