import random

import geomstats.backend as gs
from geomstats.geometry.euclidean import Euclidean
from geomstats.geometry.hypersphere import Hypersphere
from geomstats.geometry.landmarks import L2Metric, Landmarks
from tests.data_generation import _ManifoldTestData, _RiemannianMetricTestData


class LandmarksTestData(_ManifoldTestData):
    dim_list = random.sample(range(2, 4), 2)
    n_landmarks_list = random.sample(range(1, 5), 2)
    space_args_list = [
        (Hypersphere(dim), n_landmarks)
        for dim, n_landmarks in zip(dim_list, n_landmarks_list)
    ] + [
        (Euclidean(dim + 1), n_landmarks)
        for dim, n_landmarks in zip(dim_list, n_landmarks_list)
    ]
    shape_list = [
        (n_landmark, dim + 1) for dim, n_landmark in zip(dim_list, n_landmarks_list)
    ] * 2
    n_points_list = random.sample(range(1, 5), 4)
    n_vecs_list = random.sample(range(2, 5), 2)

    space = Landmarks

    def random_point_belongs_test_data(self):
        smoke_space_args_list = [(Hypersphere(2), 2), (Euclidean(2 + 1), 2)]
        smoke_n_points_list = [1, 2]
        return self._random_point_belongs_test_data(
            smoke_space_args_list,
            smoke_n_points_list,
            self.space_args_list,
            self.n_points_list,
        )


class TestDataL2Metric(_RiemannianMetricTestData):

    dim_list = random.sample(range(2, 4), 2)
    n_landmarks_list = random.sample(range(2, 5), 2)
    metric_args_list = [
        (Hypersphere(dim), n_landmarks)
        for dim, n_landmarks in zip(dim_list, n_landmarks_list)
    ] + [
        (Euclidean(dim + 1), n_landmarks)
        for dim, n_landmarks in zip(dim_list, n_landmarks_list)
    ]
    space_list = [Landmarks(*metric_arg) for metric_arg in metric_args_list]
    shape_list = [
        (n_landmark, dim + 1) for dim, n_landmark in zip(dim_list, n_landmarks_list)
    ] * 2
    n_points_list = random.sample(range(2, 5), 2)
    n_tangent_vecs_list = random.sample(range(2, 5), 2)
    n_points_a_list = random.sample(range(2, 5), 2)
    n_points_b_list = [1]
    alpha_list = [1] * 4
    n_rungs_list = [1] * 4
    scheme_list = ["pole"] * 4

    s2 = Hypersphere(dim=2)
    r3 = s2.embedding_space

    initial_point = [0.0, 0.0, 1.0]
    initial_tangent_vec_a = [1.0, 0.0, 0.0]
    initial_tangent_vec_b = [0.0, 1.0, 0.0]
    initial_tangent_vec_c = [-1.0, 0.0, 0.0]

    landmarks_a = s2.metric.geodesic(
        initial_point=initial_point, initial_tangent_vec=initial_tangent_vec_a
    )
    landmarks_b = s2.metric.geodesic(
        initial_point=initial_point, initial_tangent_vec=initial_tangent_vec_b
    )
    landmarks_c = s2.metric.geodesic(
        initial_point=initial_point, initial_tangent_vec=initial_tangent_vec_c
    )

    n_sampling_points = 10
    sampling_times = gs.linspace(0.0, 1.0, n_sampling_points)
    landmark_set_a = landmarks_a(sampling_times)
    landmark_set_b = landmarks_b(sampling_times)
    landmark_set_c = landmarks_c(sampling_times)

    n_landmark_sets = 5
    times = gs.linspace(0.0, 1.0, n_landmark_sets)
    space_landmarks_in_sphere_2d = Landmarks(
        ambient_manifold=s2, k_landmarks=n_sampling_points
    )
    l2_metric_s2 = space_landmarks_in_sphere_2d.metric

    Metric = L2Metric

    def log_after_exp_test_data(self):
        return super().log_after_exp_test_data(amplitude=30)

    def l2_metric_inner_product_vectorization_test_data(self):
        smoke_data = [
            dict(
                l2_metric_s2=self.l2_metric_s2,
                times=self.times,
                n_landmark_sets=self.n_landmark_sets,
                landmarks_a=self.landmark_set_a,
                landmarks_b=self.landmark_set_b,
                landmarks_c=self.landmark_set_c,
            )
        ]
        return self.generate_tests(smoke_data)

    def l2_metric_exp_vectorization_test_data(self):
        smoke_data = [
            dict(
                l2_metric_s2=self.l2_metric_s2,
                times=self.times,
                landmarks_a=self.landmark_set_a,
                landmarks_b=self.landmark_set_b,
                landmarks_c=self.landmark_set_c,
            )
        ]
        return self.generate_tests(smoke_data)

    def l2_metric_log_vectorization_test_data(self):
        smoke_data = [
            dict(
                l2_metric_s2=self.l2_metric_s2,
                times=self.times,
                landmarks_a=self.landmark_set_a,
                landmarks_b=self.landmark_set_b,
                landmarks_c=self.landmark_set_c,
            )
        ]
        return self.generate_tests(smoke_data)

    def l2_metric_geodesic_test_data(self):
        smoke_data = [
            dict(
                l2_metric_s2=self.l2_metric_s2,
                times=self.times,
                n_sampling_points=self.n_sampling_points,
                landmarks_a=self.landmark_set_a,
                landmarks_b=self.landmark_set_b,
            )
        ]
        return self.generate_tests(smoke_data)
