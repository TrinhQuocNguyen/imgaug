"""
Automatically run tests for this library.
Simply execute
    python test.py
or execute
    nosetests --verbose
from within tests/
or add @attr("now") in front of a test and then execute
    nosetests --verbose -a now
to only execute a specific test.
"""
from __future__ import print_function, division
import imgaug as ia
from imgaug import augmenters as iaa
from imgaug import parameters as iap
import numpy as np
import random
import six
import six.moves as sm
from scipy import misc
import skimage
from skimage import data, color
import cv2
import time
import scipy

#from nose.plugins.attrib import attr


def main():
    time_start = time.time()

    # ----------------------
    # imgaug
    # ----------------------
    is_np_array()
    test_is_single_integer()
    test_is_single_float()
    test_is_single_number()
    test_is_iterable()
    test_is_string()
    test_is_integer_array()
    test_is_callable()
    test_seed()
    test_current_random_state()
    test_new_random_state()
    test_dummy_random_state()
    test_copy_random_state()
    test_derive_random_state()
    test_derive_random_states()
    test_forward_random_state()
    # test_quokka()
    # test_quokka_square()
    # test_angle_between_vectors()
    # test_draw_text()
    # test_imresize_many_images()
    # test_imresize_single_image()
    # test_draw_grid()
    # test_show_grid()
    # test_do_assert()
    # test_HooksImages_is_activated()
    # test_HooksImages_is_propagating()
    # test_HooksImages_preprocess()
    # test_HooksImages_postprocess()
    # test_Keypoint_x_int()
    # test_Keypoint_y_int()
    # test_Keypoint_project()
    # test_Keypoint_shift()
    # test_Keypoint_repr()
    # test_Keypoint_str()
    # test_KeypointsOnImage_height()
    # test_KeypointsOnImage_width()
    # test_KeypointsOnImage_on()
    # test_KeypointsOnImage_draw_on_image()
    # test_KeypointsOnImage_shift()
    # test_KeypointsOnImage_get_coords_array()
    # test_KeypointsOnImage_from_coords_array()
    # test_KeypointsOnImage_to_keypoint_image()
    # test_KeypointsOnImage_from_keypoint_image()
    # test_KeypointsOnImage_copy()
    # test_KeypointsOnImage_deepcopy()
    test_BoundingBox()
    # test_BoundingBoxesOnImage_height()
    # test_BoundingBoxesOnImage_width()
    # test_BoundingBoxesOnImage_on()
    # test_BoundingBoxesOnImage_draw_on_image()
    # test_BoundingBoxesOnImage_remove_out_of_image()
    # test_BoundingBoxesOnImage_cut_out_of_image()
    # test_BoundingBoxesOnImage_shift()
    # test_BoundingBoxesOnImage_copy()
    # test_BoundingBoxesOnImage_deepcopy()
    # test_BoundingBoxesOnImage_repr()
    # test_BoundingBoxesOnImage_str()
    # test_Batch()
    # test_BatchLoader.all_finished()
    # test_BatchLoader._load_batches()
    # test_BatchLoader.terminate()
    # test_BackgroundAugmenter.get_batch()
    # test_BackgroundAugmenter._augment_images_worker()
    # test_BackgroundAugmenter.terminate()

    # ----------------------
    # augmenters
    # ----------------------
    test_find()
    test_remove()
    test_hooks()

    # arithmetic
    test_Add()
    test_AddElementwise()
    test_AdditiveGaussianNoise()
    test_Multiply()
    test_MultiplyElementwise()
    test_Dropout()
    test_CoarseDropout()
    # TODO SaltAndPepper
    # TODO CoarseSaltAndPepper
    # TODO Salt
    # TODO CoarseSalt
    # TODO Pepper
    # TODO CoarsePepper
    test_ReplaceElementwise()
    test_Invert()
    test_ContrastNormalization()

    # blur
    test_GaussianBlur()
    test_AverageBlur()
    test_MedianBlur()
    # TODO BilateralBlur

    # color
    # TODO WithColorspace
    test_AddToHueAndSaturation()
    # TODO ChangeColorspace
    test_Grayscale()

    # convolutional
    # TODO Convolve
    test_Sharpen()
    # TODO Emboss
    # TODO EdgeDetect
    # TODO DirectedEdgeDetect

    # flip
    test_Fliplr()
    test_Flipud()

    # geometric
    test_Affine()
    # TODO AffineCv2
    # TODO PiecewiseAffine
    # TODO PerspectiveTransform
    # TODO ElasticTransformation

    # meta
    # TODO copy_dtypes_for_restore()
    # TODO restore_augmented_images_dtypes_()
    # TODO restore_augmented_images_dtypes()
    # TODO clip_augmented_images_()
    # TODO clip_augmented_images()
    # TODO Augmenter
    test_Sequential()
    test_SomeOf()
    test_OneOf()
    test_Sometimes()
    test_WithChannels()
    test_Noop()
    test_Lambda()
    test_AssertLambda()
    test_AssertShape()

    # overlay
    test_Alpha()
    test_AlphaElementwise()
    # TODO SimplexNoiseAlpha
    # TODO FrequencyNoiseAlpha

    # segmentation
    test_Superpixels()

    # size
    test_Scale()
    # TODO CropAndPad
    test_Pad()
    test_Crop()

    # these functions use various augmenters, so test them last
    test_2d_inputs()
    test_background_augmentation()
    test_determinism()
    test_keypoint_augmentation()
    test_unusual_channel_numbers()
    test_dtype_preservation()
    test_copy_random_state()

    # ----------------------
    # parameters
    # ----------------------
    test_parameters_Biomial()
    test_parameters_Choice()
    test_parameters_DiscreteUniform()
    test_parameters_Poisson()
    test_parameters_Normal()
    test_parameters_Laplace()
    test_parameters_ChiSquare()
    test_parameters_Weibull()
    test_parameters_Uniform()
    test_parameters_Beta()
    test_parameters_Deterministic()
    test_parameters_FromLowerResolution()
    test_parameters_Clip()
    test_parameters_Discretize()
    test_parameters_Multiply()
    test_parameters_Divide()
    test_parameters_Add()
    test_parameters_Subtract()
    test_parameters_Power()
    test_parameters_Absolute()
    test_parameters_RandomSign()
    test_parameters_ForceSign()
    test_parameters_Positive()
    test_parameters_Negative()
    test_parameters_IterativeNoiseAggregator()
    test_parameters_Sigmoid()
    #test_parameters_SimplexNoise()
    #test_parameters_FrequencyNoise()
    test_parameters_operators()

    time_end = time.time()
    print("Finished without errors in %.4fs." % (time_end - time_start,))


def is_np_array():
    class _Dummy(object):
        pass
    values_true = [
        np.zeros((1, 2), dtype=np.uint8),
        np.zeros((64, 64, 3), dtype=np.uint8),
        np.zeros((1, 2), dtype=np.float32),
        np.zeros((100,), dtype=np.float64)
    ]
    values_false = [
        "A", "BC", "1", True, False, (1.0, 2.0), [1.0, 2.0], _Dummy(),
        -100, 1, 0, 1, 100, -1.2, -0.001, 0.0, 0.001, 1.2, 1e-4
    ]
    for value in values_true:
        assert ia.is_np_array(value) == True
    for value in values_false:
        assert ia.is_np_array(value) == False


def test_is_single_integer():
    assert ia.is_single_integer("A") == False
    assert ia.is_single_integer(None) == False
    assert ia.is_single_integer(1.2) == False
    assert ia.is_single_integer(1.0) == False
    assert ia.is_single_integer(np.ones((1,), dtype=np.float32)[0]) == False
    assert ia.is_single_integer(1) == True
    assert ia.is_single_integer(1234) == True
    assert ia.is_single_integer(np.ones((1,), dtype=np.uint8)[0]) == True
    assert ia.is_single_integer(np.ones((1,), dtype=np.int32)[0]) == True


def test_is_single_float():
    assert ia.is_single_float("A") == False
    assert ia.is_single_float(None) == False
    assert ia.is_single_float(1.2) == True
    assert ia.is_single_float(1.0) == True
    assert ia.is_single_float(np.ones((1,), dtype=np.float32)[0]) == True
    assert ia.is_single_float(1) == False
    assert ia.is_single_float(1234) == False
    assert ia.is_single_float(np.ones((1,), dtype=np.uint8)[0]) == False
    assert ia.is_single_float(np.ones((1,), dtype=np.int32)[0]) == False


def test_is_single_number():
    class _Dummy(object):
        pass
    values_true = [-100, 1, 0, 1, 100, -1.2, -0.001, 0.0, 0.001, 1.2, 1e-4]
    values_false = ["A", "BC", "1", True, False, (1.0, 2.0), [1.0, 2.0], _Dummy(), np.zeros((1, 2), dtype=np.uint8)]
    for value in values_true:
        assert ia.is_single_number(value) == True
    for value in values_false:
        assert ia.is_single_number(value) == False


def test_is_iterable():
    class _Dummy(object):
        pass
    values_true = [
        [0, 1, 2],
        ["A", "X"],
        [[123], [456, 789]],
        [],
        (1, 2, 3),
        (1,),
        tuple(),
        "A",
        "ABC",
        "",
        np.zeros((100,), dtype=np.uint8)
    ]
    values_false = [1, 100, 0, -100, -1, 1.2, -1.2, True, False, _Dummy()]
    for value in values_true:
        assert ia.is_iterable(value) == True, value
    for value in values_false:
        assert ia.is_iterable(value) == False


def test_is_string():
    class _Dummy(object):
        pass
    values_true = ["A", "BC", "1", ""]
    values_false = [-100, 1, 0, 1, 100, -1.2, -0.001, 0.0, 0.001, 1.2, 1e-4, True, False, (1.0, 2.0), [1.0, 2.0], _Dummy(), np.zeros((1, 2), dtype=np.uint8)]
    for value in values_true:
        assert ia.is_string(value) == True
    for value in values_false:
        assert ia.is_string(value) == False


def test_is_integer_array():
    class _Dummy(object):
        pass
    values_true = [
        np.zeros((1, 2), dtype=np.uint8),
        np.zeros((100,), dtype=np.uint8),
        np.zeros((1, 2), dtype=np.uint16),
        np.zeros((1, 2), dtype=np.int32),
        np.zeros((1, 2), dtype=np.int64)
    ]
    values_false = [
        "A", "BC", "1", "", -100, 1, 0, 1, 100, -1.2, -0.001, 0.0, 0.001, 1.2, 1e-4, True, False,
        (1.0, 2.0), [1.0, 2.0], _Dummy(),
        np.zeros((1, 2), dtype=np.float16),
        np.zeros((100,), dtype=np.float32),
        np.zeros((1, 2), dtype=np.float64),
        np.zeros((1, 2), dtype=np.bool)
    ]
    for value in values_true:
        assert ia.is_integer_array(value) == True
    for value in values_false:
        assert ia.is_integer_array(value) == False


def test_is_callable():
    def _dummy_func():
        pass
    _dummy_func2 = lambda x: x
    class _Dummy1(object):
        pass
    class _Dummy2(object):
        def __call__(self):
            pass
    values_true = [_dummy_func, _dummy_func2, _Dummy2()]
    values_false = ["A", "BC", "1", "", -100, 1, 0, 1, 100, -1.2, -0.001, 0.0, 0.001, 1.2, 1e-4, True, False, (1.0, 2.0), [1.0, 2.0], _Dummy1(), np.zeros((1, 2), dtype=np.uint8)]
    for value in values_true:
        assert ia.is_callable(value) == True
    for value in values_false:
        assert ia.is_callable(value) == False


def test_seed():
    ia.seed(10017)
    rs = np.random.RandomState(10017)
    assert ia.CURRENT_RANDOM_STATE.randint(0, 1000*1000) == rs.randint(0, 1000*1000)
    reseed()


def test_current_random_state():
    assert ia.current_random_state() == ia.CURRENT_RANDOM_STATE


def test_new_random_state():
    seed = 1000
    ia.seed(seed)

    rs_observed = ia.new_random_state(seed=None, fully_random=False)
    rs_expected = np.random.RandomState(np.random.RandomState(seed).randint(0, 10**6, 1)[0])
    assert rs_observed.randint(0, 10**6) == rs_expected.randint(0, 10**6)
    rs_observed1 = ia.new_random_state(seed=None, fully_random=False)
    rs_observed2 = ia.new_random_state(seed=None, fully_random=False)
    assert rs_observed1.randint(0, 10**6) != rs_observed2.randint(0, 10**6)

    ia.seed(seed)
    np.random.seed(seed)
    rs_observed = ia.new_random_state(seed=None, fully_random=True)
    rs_not_expected = np.random.RandomState(np.random.RandomState(seed).randint(0, 10**6, 1)[0])
    assert rs_observed.randint(0, 10**6) != rs_not_expected.randint(0, 10**6)

    rs_observed1 = ia.new_random_state(seed=None, fully_random=True)
    rs_observed2 = ia.new_random_state(seed=None, fully_random=True)
    assert rs_observed1.randint(0, 10**6) != rs_observed2.randint(0, 10**6)

    rs_observed1 = ia.new_random_state(seed=1234)
    rs_observed2 = ia.new_random_state(seed=1234)
    rs_expected = np.random.RandomState(1234)
    assert rs_observed1.randint(0, 10**6) == rs_observed2.randint(0, 10**6) == rs_expected.randint(0, 10**6)


def test_dummy_random_state():
    assert ia.dummy_random_state().randint(0, 10**6) == np.random.RandomState(1).randint(0, 10**6)


def test_copy_random_state():
    rs = np.random.RandomState(1017)
    rs_copy = ia.copy_random_state(rs)
    assert rs != rs_copy
    assert rs.randint(0, 10**6) == rs_copy.randint(0, 10**6)

    assert ia.copy_random_state(np.random) == np.random
    assert ia.copy_random_state(np.random, force_copy=True) != np.random


def test_derive_random_state():
    rs = np.random.RandomState(1017)
    rs_observed = ia.derive_random_state(np.random.RandomState(1017))
    rs_expected = np.random.RandomState(np.random.RandomState(1017).randint(0, 10**6))
    assert rs_observed.randint(0, 10**6) == rs_expected.randint(0, 10**6)


def test_derive_random_states():
    rs = np.random.RandomState(1017)
    rs_observed1, rs_observed2 = ia.derive_random_states(np.random.RandomState(1017), n=2)
    seed = np.random.RandomState(1017).randint(0, 10**6)
    rs_expected1 = np.random.RandomState(seed+0)
    rs_expected2 = np.random.RandomState(seed+1)
    assert rs_observed1.randint(0, 10**6) == rs_expected1.randint(0, 10**6)
    assert rs_observed2.randint(0, 10**6) == rs_expected2.randint(0, 10**6)


def test_forward_random_state():
    rs1 = np.random.RandomState(1017)
    rs2 = np.random.RandomState(1017)
    ia.forward_random_state(rs1)
    rs2.uniform()
    assert rs1.randint(0, 10**6) == rs2.randint(0, 10**6)


def test_BoundingBox():
    eps = 1e-8

    # properties with ints
    bb = ia.BoundingBox(y1=10, x1=20, y2=30, x2=40, label=None)
    assert bb.y1_int == 10
    assert bb.x1_int == 20
    assert bb.y2_int == 30
    assert bb.x2_int == 40
    assert bb.width == 40 - 20
    assert bb.height == 30 - 10
    center_x = bb.x1 + (bb.x2 - bb.x1)/2
    center_y = bb.y1 + (bb.y2 - bb.y1)/2
    assert center_x - eps < bb.center_x < center_x + eps
    assert center_y - eps < bb.center_y < center_y + eps

    # properties with floats
    bb = ia.BoundingBox(y1=10.1, x1=20.1, y2=30.9, x2=40.9, label=None)
    assert bb.y1_int == 10
    assert bb.x1_int == 20
    assert bb.y2_int == 31
    assert bb.x2_int == 41
    assert bb.width == 40.9 - 20.1
    assert bb.height == 30.9 - 10.1
    center_x = bb.x1 + (bb.x2 - bb.x1)/2
    center_y = bb.y1 + (bb.y2 - bb.y1)/2
    assert center_x - eps < bb.center_x < center_x + eps
    assert center_y - eps < bb.center_y < center_y + eps

    # area
    bb = ia.BoundingBox(y1=10, x1=20, y2=30, x2=40, label=None)
    assert bb.area == (30-10) * (40-20)

    # project
    bb = ia.BoundingBox(y1=10, x1=20, y2=30, x2=40, label=None)
    bb2 = bb.project((10, 10), (20, 20))
    assert 10*2 - eps < bb2.y1 < 10*2 + eps
    assert 20*2 - eps < bb2.x1 < 20*2 + eps
    assert 30*2 - eps < bb2.y2 < 30*2 + eps
    assert 40*2 - eps < bb2.x2 < 40*2 + eps

    bb2 = bb.project((10, 10), (5, 5))
    assert 10*0.5 - eps < bb2.y1 < 10*0.5 + eps
    assert 20*0.5 - eps < bb2.x1 < 20*0.5 + eps
    assert 30*0.5 - eps < bb2.y2 < 30*0.5 + eps
    assert 40*0.5 - eps < bb2.x2 < 40*0.5 + eps

    bb2 = bb.project((10, 10), (10, 20))
    assert 10*1 - eps < bb2.y1 < 10*1 + eps
    assert 20*2 - eps < bb2.x1 < 20*2 + eps
    assert 30*1 - eps < bb2.y2 < 30*1 + eps
    assert 40*2 - eps < bb2.x2 < 40*2 + eps

    bb2 = bb.project((10, 10), (20, 10))
    assert 10*2 - eps < bb2.y1 < 10*2 + eps
    assert 20*1 - eps < bb2.x1 < 20*1 + eps
    assert 30*2 - eps < bb2.y2 < 30*2 + eps
    assert 40*1 - eps < bb2.x2 < 40*1 + eps

    # extend
    bb = ia.BoundingBox(y1=10, x1=20, y2=30, x2=40, label=None)
    bb2 = bb.extend(all_sides=1)
    assert bb2.y1 == 10-1
    assert bb2.y2 == 30+1
    assert bb2.x1 == 20-1
    assert bb2.x2 == 40+1

    bb2 = bb.extend(all_sides=-1)
    assert bb2.y1 == 10-(-1)
    assert bb2.y2 == 30+(-1)
    assert bb2.x1 == 20-(-1)
    assert bb2.x2 == 40+(-1)

    bb2 = bb.extend(top=1)
    assert bb2.y1 == 10-1
    assert bb2.y2 == 30+0
    assert bb2.x1 == 20-0
    assert bb2.x2 == 40+0

    bb2 = bb.extend(right=1)
    assert bb2.y1 == 10-0
    assert bb2.y2 == 30+0
    assert bb2.x1 == 20-0
    assert bb2.x2 == 40+1

    bb2 = bb.extend(bottom=1)
    assert bb2.y1 == 10-0
    assert bb2.y2 == 30+1
    assert bb2.x1 == 20-0
    assert bb2.x2 == 40+0

    bb2 = bb.extend(left=1)
    assert bb2.y1 == 10-0
    assert bb2.y2 == 30+0
    assert bb2.x1 == 20-1
    assert bb2.x2 == 40+0

    # intersection
    bb1 = ia.BoundingBox(y1=10, x1=20, y2=30, x2=40, label=None)
    bb2 = ia.BoundingBox(y1=10, x1=39, y2=30, x2=59, label=None)
    bb_inter = bb1.intersection(bb2)
    assert bb_inter.x1 == 39
    assert bb_inter.x2 == 40
    assert bb_inter.y1 == 10
    assert bb_inter.y2 == 30

    bb1 = ia.BoundingBox(y1=10, x1=20, y2=30, x2=40, label=None)
    bb2 = ia.BoundingBox(y1=10, x1=41, y2=30, x2=61, label=None)
    bb_inter = bb1.intersection(bb2, default=False)
    assert bb_inter == False

    # union
    bb1 = ia.BoundingBox(y1=10, x1=20, y2=30, x2=40, label=None)
    bb2 = ia.BoundingBox(y1=10, x1=39, y2=30, x2=59, label=None)
    bb_union = bb1.union(bb2)
    assert bb_union.x1 == 20
    assert bb_union.x2 == 59
    assert bb_union.y1 == 10
    assert bb_union.y2 == 30

    # iou
    bb1 = ia.BoundingBox(y1=10, x1=20, y2=30, x2=40, label=None)
    bb2 = ia.BoundingBox(y1=10, x1=20, y2=30, x2=40, label=None)
    iou = bb1.iou(bb2)
    assert 1.0 - eps < iou < 1.0 + eps

    bb1 = ia.BoundingBox(y1=10, x1=20, y2=30, x2=40, label=None)
    bb2 = ia.BoundingBox(y1=10, x1=41, y2=30, x2=61, label=None)
    iou = bb1.iou(bb2)
    assert 0.0 - eps < iou < 0.0 + eps

    bb1 = ia.BoundingBox(y1=10, x1=10, y2=20, x2=20, label=None)
    bb2 = ia.BoundingBox(y1=15, x1=15, y2=25, x2=25, label=None)
    iou = bb1.iou(bb2)
    area_union = 15 * 15
    area_intersection = 5 * 5
    iou_expected = area_intersection / area_union
    assert iou_expected - eps < iou < iou_expected + eps

    # is_fully_within_image
    bb = ia.BoundingBox(y1=10, x1=20, y2=30, x2=40, label=None)
    assert bb.is_fully_within_image((100, 100, 3)) == True
    assert bb.is_fully_within_image((20, 100, 3)) == False
    assert bb.is_fully_within_image((100, 30, 3)) == False
    assert bb.is_fully_within_image((1, 1, 3)) == False

    # is_partly_within_image
    bb = ia.BoundingBox(y1=10, x1=20, y2=30, x2=40, label=None)
    assert bb.is_partly_within_image((100, 100, 3)) == True
    assert bb.is_partly_within_image((20, 100, 3)) == True
    assert bb.is_partly_within_image((100, 30, 3)) == True
    assert bb.is_partly_within_image((1, 1, 3)) == False

    # test_BoundingBox_is_out_of_image()
    bb = ia.BoundingBox(y1=10, x1=20, y2=30, x2=40, label=None)
    assert bb.is_out_of_image((100, 100, 3), partly=True, fully=True) == False
    assert bb.is_out_of_image((100, 100, 3), partly=False, fully=True) == False
    assert bb.is_out_of_image((100, 100, 3), partly=True, fully=False) == False
    assert bb.is_out_of_image((20, 100, 3), partly=True, fully=True) == True
    assert bb.is_out_of_image((20, 100, 3), partly=False, fully=True) == False
    assert bb.is_out_of_image((20, 100, 3), partly=True, fully=False) == True
    assert bb.is_out_of_image((100, 30, 3), partly=True, fully=True) == True
    assert bb.is_out_of_image((100, 30, 3), partly=False, fully=True) == False
    assert bb.is_out_of_image((100, 30, 3), partly=True, fully=False) == True
    assert bb.is_out_of_image((1, 1, 3), partly=True, fully=True) == True
    assert bb.is_out_of_image((1, 1, 3), partly=False, fully=True) == True
    assert bb.is_out_of_image((1, 1, 3), partly=True, fully=False) == False

    # cut_out_of_image
    bb = ia.BoundingBox(y1=10, x1=20, y2=30, x2=40, label=None)
    bb_cut = bb.cut_out_of_image((100, 100, 3))
    assert bb_cut.y1 == 10
    assert bb_cut.x1 == 20
    assert bb_cut.y2 == 30
    assert bb_cut.x2 == 40
    bb_cut = bb.cut_out_of_image((20, 100, 3))
    assert bb_cut.y1 == 10
    assert bb_cut.x1 == 20
    assert bb_cut.y2 == 20
    assert bb_cut.x2 == 40
    bb_cut = bb.cut_out_of_image((100, 30, 3))
    assert bb_cut.y1 == 10
    assert bb_cut.x1 == 20
    assert bb_cut.y2 == 30
    assert bb_cut.x2 == 30

    # shift
    bb = ia.BoundingBox(y1=10, x1=20, y2=30, x2=40, label=None)
    bb_top = bb.shift(top=0)
    bb_right = bb.shift(right=0)
    bb_bottom = bb.shift(bottom=0)
    bb_left = bb.shift(left=0)
    assert bb_top.y1 == 10
    assert bb_top.x1 == 20
    assert bb_top.y2 == 30
    assert bb_top.x2 == 40
    assert bb_right.y1 == 10
    assert bb_right.x1 == 20
    assert bb_right.y2 == 30
    assert bb_right.x2 == 40
    assert bb_bottom.y1 == 10
    assert bb_bottom.x1 == 20
    assert bb_bottom.y2 == 30
    assert bb_bottom.x2 == 40
    assert bb_left.y1 == 10
    assert bb_left.x1 == 20
    assert bb_left.y2 == 30
    assert bb_left.x2 == 40
    bb_top = bb.shift(top=1)
    bb_right = bb.shift(right=1)
    bb_bottom = bb.shift(bottom=1)
    bb_left = bb.shift(left=1)
    assert bb_top.y1 == 10+1
    assert bb_top.x1 == 20
    assert bb_top.y2 == 30+1
    assert bb_top.x2 == 40
    assert bb_right.y1 == 10
    assert bb_right.x1 == 20-1
    assert bb_right.y2 == 30
    assert bb_right.x2 == 40-1
    assert bb_bottom.y1 == 10-1
    assert bb_bottom.x1 == 20
    assert bb_bottom.y2 == 30-1
    assert bb_bottom.x2 == 40
    assert bb_left.y1 == 10
    assert bb_left.x1 == 20+1
    assert bb_left.y2 == 30
    assert bb_left.x2 == 40+1
    bb_top = bb.shift(top=-1)
    bb_right = bb.shift(right=-1)
    bb_bottom = bb.shift(bottom=-1)
    bb_left = bb.shift(left=-1)
    assert bb_top.y1 == 10-1
    assert bb_top.x1 == 20
    assert bb_top.y2 == 30-1
    assert bb_top.x2 == 40
    assert bb_right.y1 == 10
    assert bb_right.x1 == 20+1
    assert bb_right.y2 == 30
    assert bb_right.x2 == 40+1
    assert bb_bottom.y1 == 10+1
    assert bb_bottom.x1 == 20
    assert bb_bottom.y2 == 30+1
    assert bb_bottom.x2 == 40
    assert bb_left.y1 == 10
    assert bb_left.x1 == 20-1
    assert bb_left.y2 == 30
    assert bb_left.x2 == 40-1
    bb_mix = bb.shift(top=1, bottom=2, left=3, right=4)
    assert bb_mix.y1 == 10+1-2
    assert bb_mix.x1 == 20+3-4
    assert bb_mix.y2 == 30+3-4
    assert bb_mix.x2 == 40+1-2

    # draw_on_image()
    image = np.zeros((10, 10, 3), dtype=np.uint8)
    bb = ia.BoundingBox(y1=1, x1=1, y2=3, x2=3, label=None)
    bb_mask = np.zeros(image.shape[0:2], dtype=np.bool)
    bb_mask[1:3+1, 1] = True
    bb_mask[1:3+1, 3] = True
    bb_mask[1, 1:3+1] = True
    bb_mask[3, 1:3+1] = True
    image_bb = bb.draw_on_image(image, color=[255, 255, 255], alpha=1.0, thickness=1, copy=True, raise_if_out_of_image=False)
    assert np.all(image_bb[bb_mask] == [255, 255, 255])
    assert np.all(image_bb[~bb_mask] == [0, 0, 0])
    assert np.all(image == 0)

    image_bb = bb.draw_on_image(image, color=[255, 0, 0], alpha=1.0, thickness=1, copy=True, raise_if_out_of_image=False)
    assert np.all(image_bb[bb_mask] == [255, 0, 0])
    assert np.all(image_bb[~bb_mask] == [0, 0, 0])

    image_bb = bb.draw_on_image(image, color=128, alpha=1.0, thickness=1, copy=True, raise_if_out_of_image=False)
    assert np.all(image_bb[bb_mask] == [128, 128, 128])
    assert np.all(image_bb[~bb_mask] == [0, 0, 0])

    image_bb = bb.draw_on_image(image+100, color=[200, 200, 200], alpha=0.5, thickness=1, copy=True, raise_if_out_of_image=False)
    assert np.all(image_bb[bb_mask] == [150, 150, 150])
    assert np.all(image_bb[~bb_mask] == [100, 100, 100])

    image_bb = bb.draw_on_image(image, color=[255, 255, 255], alpha=1.0, thickness=1, copy=False, raise_if_out_of_image=False)
    assert np.all(image_bb[bb_mask] == [255, 255, 255])
    assert np.all(image_bb[~bb_mask] == [0, 0, 0])
    assert np.all(image[bb_mask] == [255, 255, 255])
    assert np.all(image[~bb_mask] == [0, 0, 0])

    image = np.zeros_like(image)
    bb = ia.BoundingBox(y1=-1, x1=-1, y2=2, x2=2, label=None)
    bb_mask = np.zeros(image.shape[0:2], dtype=np.bool)
    bb_mask[2, 0:3] = True
    bb_mask[0:3, 2] = True
    image_bb = bb.draw_on_image(image, color=[255, 255, 255], alpha=1.0, thickness=1, copy=True, raise_if_out_of_image=False)
    assert np.all(image_bb[bb_mask] == [255, 255, 255])
    assert np.all(image_bb[~bb_mask] == [0, 0, 0])

    bb = ia.BoundingBox(y1=1, x1=1, y2=3, x2=3, label=None)
    bb_mask = np.zeros(image.shape[0:2], dtype=np.bool)
    bb_mask[0:5, 0:5] = True
    bb_mask[2, 2] = False
    image_bb = bb.draw_on_image(image, color=[255, 255, 255], alpha=1.0, thickness=2, copy=True, raise_if_out_of_image=False)
    assert np.all(image_bb[bb_mask] == [255, 255, 255])
    assert np.all(image_bb[~bb_mask] == [0, 0, 0])

    bb = ia.BoundingBox(y1=-1, x1=-1, y2=1, x2=1, label=None)
    bb_mask = np.zeros(image.shape[0:2], dtype=np.bool)
    bb_mask[0:1+1, 1] = True
    bb_mask[1, 0:1+1] = True
    image_bb = bb.draw_on_image(image, color=[255, 255, 255], alpha=1.0, thickness=1, copy=True, raise_if_out_of_image=False)
    assert np.all(image_bb[bb_mask] == [255, 255, 255])
    assert np.all(image_bb[~bb_mask] == [0, 0, 0])

    bb = ia.BoundingBox(y1=-1, x1=-1, y2=1, x2=1, label=None)
    got_exception = False
    try:
        image_bb = bb.draw_on_image(image, color=[255, 255, 255], alpha=1.0, thickness=1, copy=True, raise_if_out_of_image=True)
    except Exception as e:
        got_exception = True
    assert got_exception == False

    bb = ia.BoundingBox(y1=-5, x1=-5, y2=-1, x2=-1, label=None)
    got_exception = False
    try:
        image_bb = bb.draw_on_image(image, color=[255, 255, 255], alpha=1.0, thickness=1, copy=True, raise_if_out_of_image=True)
    except Exception as e:
        got_exception = True
    assert got_exception == True

    # extract_from_image()
    image = np.random.RandomState(1234).randint(0, 255, size=(10, 10, 3))
    bb = ia.BoundingBox(y1=1, y2=3, x1=1, x2=3, label=None)
    image_sub = bb.extract_from_image(image)
    assert np.array_equal(image_sub, image[1:3, 1:3, :])

    image = np.random.RandomState(1234).randint(0, 255, size=(10, 10, 3))
    image_pad = np.pad(image, ((0, 1), (0, 1), (0, 0)), mode="constant", constant_values=0)
    bb = ia.BoundingBox(y1=8, y2=11, x1=8, x2=11, label=None)
    image_sub = bb.extract_from_image(image)
    assert np.array_equal(image_sub, image_pad[8:11, 8:11, :])

    # to_keypoints()
    bb = ia.BoundingBox(y1=1, y2=3, x1=1, x2=3, label=None)
    kps = bb.to_keypoints()
    assert kps[0].y == 1
    assert kps[0].x == 1
    assert kps[1].y == 1
    assert kps[1].x == 3
    assert kps[2].y == 3
    assert kps[2].x == 3
    assert kps[3].y == 3
    assert kps[3].x == 1

    # copy()
    bb = ia.BoundingBox(y1=1, y2=3, x1=1, x2=3, label="test")
    bb2 = bb.copy()
    assert bb2.y1 == 1
    assert bb2.y2 == 3
    assert bb2.x1 == 1
    assert bb2.x2 == 3
    assert bb2.label == "test"

    bb2 = bb.copy(y1=10, x1=20, y2=30, x2=40, label="test2")
    assert bb2.y1 == 10
    assert bb2.x1 == 20
    assert bb2.y2 == 30
    assert bb2.x2 == 40
    assert bb2.label == "test2"

    # deepcopy()
    bb = ia.BoundingBox(y1=1, y2=3, x1=1, x2=3, label=["test"])
    bb2 = bb.deepcopy()
    assert bb2.y1 == 1
    assert bb2.y2 == 3
    assert bb2.x1 == 1
    assert bb2.x2 == 3
    assert bb2.label[0] == "test"

    # BoundingBox_repr()
    bb = ia.BoundingBox(y1=1, y2=3, x1=1, x2=3, label=None)
    assert bb.__repr__() == "BoundingBox(x1=1.0000, y1=1.0000, x2=3.0000, y2=3.0000, label=None)"

    # test_BoundingBox_str()
    bb = ia.BoundingBox(y1=1, y2=3, x1=1, x2=3, label=None)
    assert bb.__str__() == "BoundingBox(x1=1.0000, y1=1.0000, x2=3.0000, y2=3.0000, label=None)"


def test_find():
    reseed()

    noop1 = iaa.Noop(name="Noop")
    fliplr = iaa.Fliplr(name="Fliplr")
    flipud = iaa.Flipud(name="Flipud")
    noop2 = iaa.Noop(name="Noop2")
    seq2 = iaa.Sequential([flipud, noop2], name="Seq2")
    seq1 = iaa.Sequential([noop1, fliplr, seq2], name="Seq")

    augs = seq1.find_augmenters_by_name("Seq")
    assert len(augs) == 1
    assert augs[0] == seq1

    augs = seq1.find_augmenters_by_name("Seq2")
    assert len(augs) == 1
    assert augs[0] == seq2

    augs = seq1.find_augmenters_by_names(["Seq", "Seq2"])
    assert len(augs) == 2
    assert augs[0] == seq1
    assert augs[1] == seq2

    augs = seq1.find_augmenters_by_name(r"Seq.*", regex=True)
    assert len(augs) == 2
    assert augs[0] == seq1
    assert augs[1] == seq2

    augs = seq1.find_augmenters(lambda aug, parents: aug.name in ["Seq", "Seq2"])
    assert len(augs) == 2
    assert augs[0] == seq1
    assert augs[1] == seq2

    augs = seq1.find_augmenters(lambda aug, parents: aug.name in ["Seq", "Seq2"] and len(parents) > 0)
    assert len(augs) == 1
    assert augs[0] == seq2

    augs = seq1.find_augmenters(lambda aug, parents: aug.name in ["Seq", "Seq2"], flat=False)
    assert len(augs) == 2
    assert augs[0] == seq1
    assert augs[1] == [seq2]


def test_remove():
    reseed()

    def get_seq():
        noop1 = iaa.Noop(name="Noop")
        fliplr = iaa.Fliplr(name="Fliplr")
        flipud = iaa.Flipud(name="Flipud")
        noop2 = iaa.Noop(name="Noop2")
        seq2 = iaa.Sequential([flipud, noop2], name="Seq2")
        seq1 = iaa.Sequential([noop1, fliplr, seq2], name="Seq")
        return seq1

    augs = get_seq()
    augs = augs.remove_augmenters(lambda aug, parents: aug.name == "Seq2")
    seqs = augs.find_augmenters_by_name(r"Seq.*", regex=True)
    assert len(seqs) == 1
    assert seqs[0].name == "Seq"

    augs = get_seq()
    augs = augs.remove_augmenters(lambda aug, parents: aug.name == "Seq2" and len(parents) == 0)
    seqs = augs.find_augmenters_by_name(r"Seq.*", regex=True)
    assert len(seqs) == 2
    assert seqs[0].name == "Seq"
    assert seqs[1].name == "Seq2"

    augs = get_seq()
    augs = augs.remove_augmenters(lambda aug, parents: True)
    assert augs is not None
    assert isinstance(augs, iaa.Noop)

    augs = get_seq()
    augs = augs.remove_augmenters(lambda aug, parents: True, noop_if_topmost=False)
    assert augs is None


def test_hooks():
    reseed()

    image = np.array([[0, 0, 1],
                      [0, 0, 1],
                      [0, 1, 1]], dtype=np.uint8)
    image_lr = np.array([[1, 0, 0],
                         [1, 0, 0],
                         [1, 1, 0]], dtype=np.uint8)
    image_ud = np.array([[0, 1, 1],
                         [0, 0, 1],
                         [0, 0, 1]], dtype=np.uint8)
    image_lrud = np.array([[1, 1, 0],
                           [1, 0, 0],
                           [1, 0, 0]], dtype=np.uint8)
    image = image[:, :, np.newaxis]
    image_lr = image_lr[:, :, np.newaxis]
    image_ud = image_ud[:, :, np.newaxis]
    image_lrud = image_lrud[:, :, np.newaxis]

    seq = iaa.Sequential([iaa.Fliplr(1.0), iaa.Flipud(1.0)])

    # preprocessing
    def preprocessor(images, augmenter, parents):
        img = np.copy(images)
        img[0][1, 1, 0] += 1
        return img
    hooks = ia.HooksImages(preprocessor=preprocessor)
    images_aug = seq.augment_images([image], hooks=hooks)
    expected = np.copy(image_lrud)
    expected[1, 1, 0] = 3
    assert np.array_equal(images_aug[0], expected)

    # postprocessing
    def postprocessor(images, augmenter, parents):
        img = np.copy(images)
        img[0][1, 1, 0] += 1
        return img
    hooks = ia.HooksImages(postprocessor=postprocessor)
    images_aug = seq.augment_images([image], hooks=hooks)
    expected = np.copy(image_lrud)
    expected[1, 1, 0] = 3
    assert np.array_equal(images_aug[0], expected)

    # propagating
    def propagator(images, augmenter, parents, default):
        if "Seq" in augmenter.name:
            return False
        else:
            return default
    hooks = ia.HooksImages(propagator=propagator)
    images_aug = seq.augment_images([image], hooks=hooks)
    assert np.array_equal(images_aug[0], image)

    # activation
    def activator(images, augmenter, parents, default):
        if "Flipud" in augmenter.name:
            return False
        else:
            return default
    hooks = ia.HooksImages(activator=activator)
    images_aug = seq.augment_images([image], hooks=hooks)
    assert np.array_equal(images_aug[0], image_lr)


def test_Noop():
    reseed()

    images = create_random_images((16, 70, 50, 3))
    keypoints = create_random_keypoints((16, 70, 50, 3), 4)
    aug = iaa.Noop()
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    expected = images
    assert np.array_equal(observed, expected)

    observed = aug_det.augment_images(images)
    expected = images
    assert np.array_equal(observed, expected)

    observed = aug.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    observed = aug_det.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)


def test_Lambda():
    reseed()

    base_img = np.array([[0, 0, 1],
                         [0, 0, 1],
                         [0, 1, 1]], dtype=np.uint8)
    base_img = base_img[:, :, np.newaxis]
    images = np.array([base_img])
    images_list = [base_img]

    images_aug = images + 1
    images_aug_list = [image + 1 for image in images_list]

    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=2)], shape=base_img.shape)]
    keypoints_aug = [ia.KeypointsOnImage([ia.Keypoint(x=1, y=0), ia.Keypoint(x=2, y=1),
                                          ia.Keypoint(x=0, y=2)], shape=base_img.shape)]

    def func_images(images, random_state, parents, hooks):
        if isinstance(images, list):
            images = [image + 1 for image in images]
        else:
            images = images + 1
        return images

    def func_keypoints(keypoints_on_images, random_state, parents, hooks):
        for keypoints_on_image in keypoints_on_images:
            for kp in keypoints_on_image.keypoints:
                kp.x = (kp.x + 1) % 3
        return keypoints_on_images

    aug = iaa.Lambda(func_images, func_keypoints)
    aug_det = aug.to_deterministic()

    # check once that the augmenter can handle lists correctly
    observed = aug.augment_images(images_list)
    expected = images_aug_list
    assert array_equal_lists(observed, expected)

    observed = aug_det.augment_images(images_list)
    expected = images_aug_list
    assert array_equal_lists(observed, expected)

    for _ in sm.xrange(10):
        observed = aug.augment_images(images)
        expected = images_aug
        assert np.array_equal(observed, expected)

        observed = aug_det.augment_images(images)
        expected = images_aug
        assert np.array_equal(observed, expected)

        observed = aug.augment_keypoints(keypoints)
        expected = keypoints_aug
        assert keypoints_equal(observed, expected)

        observed = aug_det.augment_keypoints(keypoints)
        expected = keypoints_aug
        assert keypoints_equal(observed, expected)


def test_AssertLambda():
    reseed()

    base_img = np.array([[0, 0, 1],
                         [0, 0, 1],
                         [0, 1, 1]], dtype=np.uint8)
    base_img = base_img[:, :, np.newaxis]
    images = np.array([base_img])
    images_list = [base_img]

    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=2)], shape=base_img.shape)]

    def func_images_succeeds(images, random_state, parents, hooks):
        return images[0][0, 0] == 0 and images[0][2, 2] == 1

    def func_images_fails(images, random_state, parents, hooks):
        return images[0][0, 0] == 1

    def func_keypoints_succeeds(keypoints_on_images, random_state, parents, hooks):
        return keypoints_on_images[0].keypoints[0].x == 0 and keypoints_on_images[0].keypoints[2].x == 2

    def func_keypoints_fails(keypoints_on_images, random_state, parents, hooks):
        return keypoints_on_images[0].keypoints[0].x == 2

    aug_succeeds = iaa.AssertLambda(func_images_succeeds, func_keypoints_succeeds)
    aug_succeeds_det = aug_succeeds.to_deterministic()
    aug_fails = iaa.AssertLambda(func_images_fails, func_keypoints_fails)
    aug_fails_det = aug_fails.to_deterministic()

    # images as numpy array
    observed = aug_succeeds.augment_images(images)
    expected = images
    assert np.array_equal(observed, expected)

    try:
        observed = aug_fails.augment_images(images)
        errored = False
    except AssertionError as e:
        errored = True
    assert errored

    observed = aug_succeeds_det.augment_images(images)
    expected = images
    assert np.array_equal(observed, expected)

    try:
        observed = aug_fails.augment_images(images)
        errored = False
    except AssertionError as e:
        errored = True
    assert errored

    # Lists of images
    observed = aug_succeeds.augment_images(images_list)
    expected = images_list
    assert array_equal_lists(observed, expected)

    try:
        observed = aug_fails.augment_images(images_list)
        errored = False
    except AssertionError as e:
        errored = True
    assert errored

    observed = aug_succeeds_det.augment_images(images_list)
    expected = images_list
    assert array_equal_lists(observed, expected)

    try:
        observed = aug_fails.augment_images(images_list)
        errored = False
    except AssertionError as e:
        errored = True
    assert errored

    # keypoints
    observed = aug_succeeds.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    try:
        observed = aug_fails.augment_keypoints(keypoints)
        errored = False
    except AssertionError as e:
        errored = True
    assert errored

    observed = aug_succeeds_det.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    try:
        observed = aug_fails.augment_keypoints(keypoints)
        errored = False
    except AssertionError as e:
        errored = True
    assert errored


def test_AssertShape():
    reseed()

    base_img = np.array([[0, 0, 1, 0],
                         [0, 0, 1, 0],
                         [0, 1, 1, 0]], dtype=np.uint8)
    base_img = base_img[:, :, np.newaxis]
    images = np.array([base_img])
    images_list = [base_img]
    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=2)], shape=base_img.shape)]

    base_img_h4 = np.array([[0, 0, 1, 0],
                            [0, 0, 1, 0],
                            [0, 1, 1, 0],
                            [1, 0, 1, 0]], dtype=np.uint8)
    base_img_h4 = base_img_h4[:, :, np.newaxis]
    images_h4 = np.array([base_img_h4])
    keypoints_h4 = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                         ia.Keypoint(x=2, y=2)], shape=base_img_h4.shape)]

    # image must have exactly shape (1, 3, 4, 1)
    aug = iaa.AssertShape((1, 3, 4, 1))
    aug_det = aug.to_deterministic()

    # check once that the augmenter can handle lists correctly
    observed = aug.augment_images(images_list)
    expected = images_list
    assert array_equal_lists(observed, expected)

    observed = aug_det.augment_images(images_list)
    expected = images_list
    assert array_equal_lists(observed, expected)

    for _ in sm.xrange(10):
        observed = aug.augment_images(images)
        expected = images
        assert np.array_equal(observed, expected)

        observed = aug_det.augment_images(images)
        expected = images
        assert np.array_equal(observed, expected)

        observed = aug.augment_keypoints(keypoints)
        expected = keypoints
        assert keypoints_equal(observed, expected)

        observed = aug_det.augment_keypoints(keypoints)
        expected = keypoints
        assert keypoints_equal(observed, expected)

        try:
            observed = aug.augment_images(images_h4)
            errored = False
        except AssertionError as e:
            errored = True
        assert errored

        try:
            observed = aug.augment_keypoints(keypoints_h4)
            errored = False
        except AssertionError as e:
            errored = True
        assert errored

    # any value for number of images allowed (None)
    aug = iaa.AssertShape((None, 3, 4, 1))
    aug_det = aug.to_deterministic()
    for _ in sm.xrange(10):
        observed = aug.augment_images(images)
        expected = images
        assert np.array_equal(observed, expected)

        observed = aug_det.augment_images(images)
        expected = images
        assert np.array_equal(observed, expected)

        observed = aug.augment_keypoints(keypoints)
        expected = keypoints
        assert keypoints_equal(observed, expected)

        observed = aug_det.augment_keypoints(keypoints)
        expected = keypoints
        assert keypoints_equal(observed, expected)

        try:
            observed = aug.augment_images(images_h4)
            errored = False
        except AssertionError as e:
            errored = True
        assert errored

        try:
            observed = aug.augment_keypoints(keypoints_h4)
            errored = False
        except AssertionError as e:
            errored = True
        assert errored

    # list of possible choices [1, 3, 5] for height
    aug = iaa.AssertShape((1, [1, 3, 5], 4, 1))
    aug_det = aug.to_deterministic()
    for _ in sm.xrange(10):
        observed = aug.augment_images(images)
        expected = images
        assert np.array_equal(observed, expected)

        observed = aug_det.augment_images(images)
        expected = images
        assert np.array_equal(observed, expected)

        observed = aug.augment_keypoints(keypoints)
        expected = keypoints
        assert keypoints_equal(observed, expected)

        observed = aug_det.augment_keypoints(keypoints)
        expected = keypoints
        assert keypoints_equal(observed, expected)

        try:
            observed = aug.augment_images(images_h4)
            errored = False
        except AssertionError as e:
            errored = True
        assert errored

        try:
            observed = aug.augment_keypoints(keypoints_h4)
            errored = False
        except AssertionError as e:
            errored = True
        assert errored

    # range of 1-3 for height (tuple comparison is a <= x < b, so we use (1,4) here)
    aug = iaa.AssertShape((1, (1, 4), 4, 1))
    aug_det = aug.to_deterministic()
    for _ in sm.xrange(10):
        observed = aug.augment_images(images)
        expected = images
        assert np.array_equal(observed, expected)

        observed = aug_det.augment_images(images)
        expected = images
        assert np.array_equal(observed, expected)

        observed = aug.augment_keypoints(keypoints)
        expected = keypoints
        assert keypoints_equal(observed, expected)

        observed = aug_det.augment_keypoints(keypoints)
        expected = keypoints
        assert keypoints_equal(observed, expected)

        try:
            observed = aug.augment_images(images_h4)
            errored = False
        except AssertionError as e:
            errored = True
        assert errored

        try:
            observed = aug.augment_keypoints(keypoints_h4)
            errored = False
        except AssertionError as e:
            errored = True
        assert errored


def test_Alpha():
    reseed()

    base_img = np.zeros((3, 3, 1), dtype=np.uint8)

    aug = iaa.Alpha(1, iaa.Add(10), iaa.Add(20))
    observed = aug.augment_image(base_img)
    expected = (base_img + 10).astype(np.uint8)
    assert np.allclose(observed, expected)

    aug = iaa.Alpha(0, iaa.Add(10), iaa.Add(20))
    observed = aug.augment_image(base_img)
    expected = (base_img + 20).astype(np.uint8)
    assert np.allclose(observed, expected)

    aug = iaa.Alpha(0.75, iaa.Add(10), iaa.Add(20))
    observed = aug.augment_image(base_img)
    expected = (base_img + 0.75 * 10 + 0.25 * 20).astype(np.uint8)
    assert np.allclose(observed, expected)

    aug = iaa.Alpha(0.75, None, iaa.Add(20))
    observed = aug.augment_image(base_img + 10)
    expected = (base_img + 0.75 * 10 + 0.25 * (10 + 20)).astype(np.uint8)
    assert np.allclose(observed, expected)

    aug = iaa.Alpha(0.75, iaa.Add(10), None)
    observed = aug.augment_image(base_img + 10)
    expected = (base_img + 0.75 * (10 + 10) + 0.25 * 10).astype(np.uint8)
    assert np.allclose(observed, expected)

    base_img = np.zeros((1, 2, 1), dtype=np.uint8)
    nb_iterations = 1000
    aug = iaa.Alpha((0.0, 1.0), iaa.Add(10), iaa.Add(110))
    values = []
    for _ in sm.xrange(nb_iterations):
        observed = aug.augment_image(base_img)
        observed_val = np.round(np.average(observed)) - 10
        values.append(observed_val / 100)

    nb_bins = 5
    hist, _ = np.histogram(values, bins=nb_bins, range=(0.0, 1.0), density=False)
    density_expected = 1.0/nb_bins
    density_tolerance = 0.05
    for nb_samples in hist:
        density = nb_samples / nb_iterations
        assert density_expected - density_tolerance < density < density_expected + density_tolerance


def test_AlphaElementwise():
    reseed()

    base_img = np.zeros((3, 3, 1), dtype=np.uint8)

    aug = iaa.AlphaElementwise(1, iaa.Add(10), iaa.Add(20))
    observed = aug.augment_image(base_img)
    expected = base_img + 10
    assert np.allclose(observed, expected)

    aug = iaa.AlphaElementwise(0, iaa.Add(10), iaa.Add(20))
    observed = aug.augment_image(base_img)
    expected = base_img + 20
    assert np.allclose(observed, expected)

    aug = iaa.AlphaElementwise(0.75, iaa.Add(10), iaa.Add(20))
    observed = aug.augment_image(base_img)
    expected = (base_img + 0.75 * 10 + 0.25 * 20).astype(np.uint8)
    assert np.allclose(observed, expected)

    aug = iaa.AlphaElementwise(0.75, None, iaa.Add(20))
    observed = aug.augment_image(base_img + 10)
    expected = (base_img + 0.75 * 10 + 0.25 * (10 + 20)).astype(np.uint8)
    assert np.allclose(observed, expected)

    aug = iaa.AlphaElementwise(0.75, iaa.Add(10), None)
    observed = aug.augment_image(base_img + 10)
    expected = (base_img + 0.75 * (10 + 10) + 0.25 * 10).astype(np.uint8)
    assert np.allclose(observed, expected)

    base_img = np.zeros((100, 100), dtype=np.uint8)
    aug = iaa.AlphaElementwise((0.0, 1.0), iaa.Add(10), iaa.Add(110))
    observed = (aug.augment_image(base_img) - 10) / 100
    nb_bins = 10
    hist, _ = np.histogram(observed.flatten(),  bins=nb_bins, range=(0.0, 1.0), density=False)
    density_expected = 1.0/nb_bins
    density_tolerance = 0.05
    for nb_samples in hist:
        density = nb_samples / observed.size
        assert density_expected - density_tolerance < density < density_expected + density_tolerance

    base_img = np.zeros((1, 1, 100), dtype=np.uint8)
    aug = iaa.AlphaElementwise((0.0, 1.0), iaa.Add(10), iaa.Add(110), per_channel=True)
    observed = aug.augment_image(base_img)
    assert len(set(observed.flatten())) > 1

def test_Superpixels():
    reseed()

    def _array_equals_tolerant(a, b, tolerance):
        diff = np.abs(a.astype(np.int32) - b.astype(np.int32))
        return np.all(diff <= tolerance)

    base_img = [
        [255, 255, 255, 0, 0, 0],
        [255, 235, 255, 0, 20, 0],
        [250, 250, 250, 5, 5, 5]
    ]
    base_img = np.tile(np.array(base_img, dtype=np.uint8)[..., np.newaxis], (1, 1, 3))

    base_img_superpixels = [
        [251, 251, 251, 4, 4, 4],
        [251, 251, 251, 4, 4, 4],
        [251, 251, 251, 4, 4, 4]
    ]
    base_img_superpixels = np.tile(np.array(base_img_superpixels, dtype=np.uint8)[..., np.newaxis], (1, 1, 3))

    base_img_superpixels_left = np.copy(base_img_superpixels)
    base_img_superpixels_left[:, 3:, :] = base_img[:, 3:, :]

    base_img_superpixels_right = np.copy(base_img_superpixels)
    base_img_superpixels_right[:, :3, :] = base_img[:, :3, :]

    aug = iaa.Superpixels(p_replace=0, n_segments=2)
    observed = aug.augment_image(base_img)
    expected = base_img
    assert np.allclose(observed, expected)

    aug = iaa.Superpixels(p_replace=1.0, n_segments=2)
    observed = aug.augment_image(base_img)
    expected = base_img_superpixels
    assert _array_equals_tolerant(observed, expected, 2)

    aug = iaa.Superpixels(p_replace=0.5, n_segments=2)
    seen = {"none": False, "left": False, "right": False, "both": False}
    for _ in sm.xrange(100):
        observed = aug.augment_image(base_img)
        if _array_equals_tolerant(observed, base_img, 2):
            seen["none"] = True
        elif _array_equals_tolerant(observed, base_img_superpixels_left, 2):
            seen["left"] = True
        elif _array_equals_tolerant(observed, base_img_superpixels_right, 2):
            seen["right"] = True
        elif _array_equals_tolerant(observed, base_img_superpixels, 2):
            seen["both"] = True
        else:
            raise Exception("Generated superpixels image does not match any expected image.")
        if all(seen.values()):
            break
    assert all(seen.values())


def test_Scale():
    reseed()

    base_img2d = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 255, 255, 255, 255, 255, 255, 0],
        [0, 255, 255, 255, 255, 255, 255, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    base_img2d = np.array(base_img2d, dtype=np.uint8)
    base_img3d = np.tile(base_img2d[..., np.newaxis], (1, 1, 3))

    intensity_avg = np.average(base_img2d)
    intensity_low = intensity_avg - 0.2 * np.abs(intensity_avg - 128)
    intensity_high = intensity_avg + 0.2 * np.abs(intensity_avg - 128)

    aspect_ratio2d = base_img2d.shape[1] / base_img2d.shape[0]
    aspect_ratio3d = base_img3d.shape[1] / base_img3d.shape[0]

    aug = iaa.Scale(12)
    observed2d = aug.augment_image(base_img2d)
    observed3d = aug.augment_image(base_img3d)
    assert observed2d.shape == (12, 12)
    assert observed3d.shape == (12, 12, 3)
    assert 50 < np.average(observed2d) < 205
    assert 50 < np.average(observed3d) < 205

    aug = iaa.Scale([12, 14])
    seen2d = [False, False]
    seen3d = [False, False]
    for _ in sm.xrange(100):
        observed2d = aug.augment_image(base_img2d)
        observed3d = aug.augment_image(base_img3d)
        assert observed2d.shape in [(12, 12), (14, 14)]
        assert observed3d.shape in [(12, 12, 3), (14, 14, 3)]
        if observed2d.shape == (12, 12):
            seen2d[0] = True
        else:
            seen2d[1] = True
        if observed3d.shape == (12, 12, 3):
            seen3d[0] = True
        else:
            seen3d[1] = True
        if all(seen2d) and all(seen3d):
            break
    assert all(seen2d)
    assert all(seen3d)

    aug = iaa.Scale((12, 14))
    seen2d = [False, False, False]
    seen3d = [False, False, False]
    for _ in sm.xrange(100):
        observed2d = aug.augment_image(base_img2d)
        observed3d = aug.augment_image(base_img3d)
        assert observed2d.shape in [(12, 12), (13, 13), (14, 14)]
        assert observed3d.shape in [(12, 12, 3), (13, 13, 3), (14, 14, 3)]
        if observed2d.shape == (12, 12):
            seen2d[0] = True
        elif observed2d.shape == (13, 13):
            seen2d[1] = True
        else:
            seen2d[2] = True
        if observed3d.shape == (12, 12, 3):
            seen3d[0] = True
        elif observed3d.shape == (13, 13, 3):
            seen3d[1] = True
        else:
            seen3d[2] = True
        if all(seen2d) and all(seen3d):
            break
    assert all(seen2d)
    assert all(seen3d)

    aug = iaa.Scale({"height": 12, "width": 13})
    observed2d = aug.augment_image(base_img2d)
    observed3d = aug.augment_image(base_img3d)
    assert observed2d.shape == (12, 13)
    assert observed3d.shape == (12, 13, 3)

    aug = iaa.Scale({"height": 12, "width": "keep"})
    observed2d = aug.augment_image(base_img2d)
    observed3d = aug.augment_image(base_img3d)
    assert observed2d.shape == (12, base_img2d.shape[1])
    assert observed3d.shape == (12, base_img3d.shape[1], 3)

    aug = iaa.Scale({"height": "keep", "width": 12})
    observed2d = aug.augment_image(base_img2d)
    observed3d = aug.augment_image(base_img3d)
    assert observed2d.shape == (base_img2d.shape[0], 12)
    assert observed3d.shape == (base_img3d.shape[0], 12, 3)

    aug = iaa.Scale({"height": 12, "width": "keep-aspect-ratio"})
    observed2d = aug.augment_image(base_img2d)
    observed3d = aug.augment_image(base_img3d)
    assert observed2d.shape == (12, int(12 * aspect_ratio2d))
    assert observed3d.shape == (12, int(12 * aspect_ratio3d), 3)

    aug = iaa.Scale({"height": "keep-aspect-ratio", "width": 12})
    observed2d = aug.augment_image(base_img2d)
    observed3d = aug.augment_image(base_img3d)
    assert observed2d.shape == (int(12 * (1/aspect_ratio2d)), 12)
    assert observed3d.shape == (int(12 * (1/aspect_ratio3d)), 12, 3)

    aug = iaa.Scale({"height": [12, 14], "width": 12})
    seen2d = [False, False]
    seen3d = [False, False]
    for _ in sm.xrange(100):
        observed2d = aug.augment_image(base_img2d)
        observed3d = aug.augment_image(base_img3d)
        assert observed2d.shape in [(12, 12), (14, 12)]
        assert observed3d.shape in [(12, 12, 3), (14, 12, 3)]
        if observed2d.shape == (12, 12):
            seen2d[0] = True
        else:
            seen2d[1] = True
        if observed3d.shape == (12, 12, 3):
            seen3d[0] = True
        else:
            seen3d[1] = True
        if all(seen2d) and all(seen3d):
            break
    assert all(seen2d)
    assert all(seen3d)

    aug = iaa.Scale({"height": 12, "width": [12, 14]})
    seen2d = [False, False]
    seen3d = [False, False]
    for _ in sm.xrange(100):
        observed2d = aug.augment_image(base_img2d)
        observed3d = aug.augment_image(base_img3d)
        assert observed2d.shape in [(12, 12), (12, 14)]
        assert observed3d.shape in [(12, 12, 3), (12, 14, 3)]
        if observed2d.shape == (12, 12):
            seen2d[0] = True
        else:
            seen2d[1] = True
        if observed3d.shape == (12, 12, 3):
            seen3d[0] = True
        else:
            seen3d[1] = True
        if all(seen2d) and all(seen3d):
            break
    assert all(seen2d)
    assert all(seen3d)

    aug = iaa.Scale({"height": (12, 14), "width": 12})
    seen2d = [False, False, False]
    seen3d = [False, False, False]
    for _ in sm.xrange(100):
        observed2d = aug.augment_image(base_img2d)
        observed3d = aug.augment_image(base_img3d)
        assert observed2d.shape in [(12, 12), (13, 12), (14, 12)]
        assert observed3d.shape in [(12, 12, 3), (13, 12, 3), (14, 12, 3)]
        if observed2d.shape == (12, 12):
            seen2d[0] = True
        elif observed2d.shape == (13, 12):
            seen2d[1] = True
        else:
            seen2d[2] = True
        if observed3d.shape == (12, 12, 3):
            seen3d[0] = True
        elif observed3d.shape == (13, 12, 3):
            seen3d[1] = True
        else:
            seen3d[2] = True
        if all(seen2d) and all(seen3d):
            break
    assert all(seen2d)
    assert all(seen3d)

    aug = iaa.Scale(2.0)
    observed2d = aug.augment_image(base_img2d)
    observed3d = aug.augment_image(base_img3d)
    assert observed2d.shape == (base_img2d.shape[0]*2, base_img2d.shape[1]*2)
    assert observed3d.shape == (base_img3d.shape[0]*2, base_img3d.shape[1]*2, 3)
    assert intensity_low < np.average(observed2d) < intensity_high
    assert intensity_low < np.average(observed3d) < intensity_high

    aug = iaa.Scale([2.0, 4.0])
    seen2d = [False, False]
    seen3d = [False, False]
    for _ in sm.xrange(100):
        observed2d = aug.augment_image(base_img2d)
        observed3d = aug.augment_image(base_img3d)
        assert observed2d.shape in [(base_img2d.shape[0]*2, base_img2d.shape[1]*2), (base_img2d.shape[0]*4, base_img2d.shape[1]*4)]
        assert observed3d.shape in [(base_img3d.shape[0]*2, base_img3d.shape[1]*2, 3), (base_img3d.shape[0]*4, base_img3d.shape[1]*4, 3)]
        if observed2d.shape == (base_img2d.shape[0]*2, base_img2d.shape[1]*2):
            seen2d[0] = True
        else:
            seen2d[1] = True
        if observed3d.shape == (base_img3d.shape[0]*2, base_img3d.shape[1]*2, 3):
            seen3d[0] = True
        else:
            seen3d[1] = True
        if all(seen2d) and all(seen3d):
            break
    assert all(seen2d)
    assert all(seen3d)

    base_img2d = base_img2d[0:4, 0:4]
    base_img3d = base_img3d[0:4, 0:4, :]
    aug = iaa.Scale((0.76, 1.0))
    not_seen2d = set()
    not_seen3d = set()
    for size in sm.xrange(3, 4+1):
        not_seen2d.add((size, size))
    for size in sm.xrange(3, 4+1):
        not_seen3d.add((size, size, 3))
    possible2d = set(list(not_seen2d))
    possible3d = set(list(not_seen3d))
    for _ in sm.xrange(100):
        observed2d = aug.augment_image(base_img2d)
        observed3d = aug.augment_image(base_img3d)
        assert observed2d.shape in possible2d
        assert observed3d.shape in possible3d
        if observed2d.shape in not_seen2d:
            not_seen2d.remove(observed2d.shape)
        if observed3d.shape in not_seen3d:
            not_seen3d.remove(observed3d.shape)
        if not not_seen2d and not not_seen3d:
            break
    assert not not_seen2d
    assert not not_seen3d

    base_img2d = base_img2d[0:4, 0:4]
    base_img3d = base_img3d[0:4, 0:4, :]
    aug = iaa.Scale({"height": (0.76, 1.0), "width": (0.76, 1.0)})
    not_seen2d = set()
    not_seen3d = set()
    for hsize in sm.xrange(3, 4+1):
        for wsize in sm.xrange(3, 4+1):
            not_seen2d.add((hsize, wsize))
    #print(base_img3d.shape[0]//2, base_img3d.shape[1]+1)
    for hsize in sm.xrange(3, 4+1):
        for wsize in sm.xrange(3, 4+1):
            not_seen3d.add((hsize, wsize, 3))
    possible2d = set(list(not_seen2d))
    possible3d = set(list(not_seen3d))
    for _ in sm.xrange(100):
        observed2d = aug.augment_image(base_img2d)
        observed3d = aug.augment_image(base_img3d)
        assert observed2d.shape in possible2d
        assert observed3d.shape in possible3d
        if observed2d.shape in not_seen2d:
            not_seen2d.remove(observed2d.shape)
        if observed3d.shape in not_seen3d:
            not_seen3d.remove(observed3d.shape)
        if not not_seen2d and not not_seen3d:
            break
    assert not not_seen2d
    assert not not_seen3d


def test_Pad():
    reseed()

    base_img = np.array([[0, 0, 0],
                         [0, 1, 0],
                         [0, 0, 0]], dtype=np.uint8)
    base_img = base_img[:, :, np.newaxis]

    images = np.array([base_img])
    images_list = [base_img]

    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=2)], shape=base_img.shape)]

    # test pad by 1 pixel on each side
    pads = [
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1),
    ]
    for pad in pads:
        top, right, bottom, left = pad
        height, width = base_img.shape[0:2]
        aug = iaa.Pad(px=pad, keep_size=False)
        base_img_padded = np.pad(base_img, ((top, bottom), (left, right), (0, 0)),
                                 mode="constant",
                                 constant_values=0)
        observed = aug.augment_images(images)
        assert np.array_equal(observed, np.array([base_img_padded]))

        observed = aug.augment_images(images_list)
        assert array_equal_lists(observed, [base_img_padded])

        keypoints_moved = [keypoints[0].shift(x=left, y=top)]
        observed = aug.augment_keypoints(keypoints)
        assert keypoints_equal(observed, keypoints_moved)

    # test pad by range of pixels
    pads = [
        ((0, 2), 0, 0, 0),
        (0, (0, 2), 0, 0),
        (0, 0, (0, 2), 0),
        (0, 0, 0, (0, 2)),
    ]
    for pad in pads:
        top, right, bottom, left = pad
        height, width = base_img.shape[0:2]
        aug = iaa.Pad(px=pad, keep_size=False)
        aug_det = aug.to_deterministic()

        images_padded = []
        keypoints_padded = []
        top_range = top if isinstance(top, tuple) else (top, top)
        right_range = right if isinstance(right, tuple) else (right, right)
        bottom_range = bottom if isinstance(bottom, tuple) else (bottom, bottom)
        left_range = left if isinstance(left, tuple) else (left, left)
        for top_val in sm.xrange(top_range[0], top_range[1]+1):
            for right_val in sm.xrange(right_range[0], right_range[1]+1):
                for bottom_val in sm.xrange(bottom_range[0], bottom_range[1]+1):
                    for left_val in sm.xrange(left_range[0], left_range[1]+1):
                        images_padded.append(np.pad(base_img, ((top_val, bottom_val), (left_val, right_val), (0, 0)), mode="constant", constant_values=0))
                        keypoints_padded.append(keypoints[0].shift(x=left_val, y=top_val))

        movements = []
        movements_det = []
        for i in sm.xrange(100):
            observed = aug.augment_images(images)

            matches = [1 if np.array_equal(observed, np.array([base_img_padded])) else 0
                       for base_img_padded in images_padded]
            movements.append(np.argmax(np.array(matches)))
            assert any([val == 1 for val in matches])

            observed = aug_det.augment_images(images)
            matches = [1 if np.array_equal(observed, np.array([base_img_padded])) else 0
                       for base_img_padded in images_padded]
            movements_det.append(np.argmax(np.array(matches)))
            assert any([val == 1 for val in matches])

            observed = aug.augment_images(images_list)
            assert any([array_equal_lists(observed, [base_img_padded])
                        for base_img_padded in images_padded])

            observed = aug.augment_keypoints(keypoints)
            assert any([keypoints_equal(observed, [kp]) for kp in keypoints_padded])

        assert len(set(movements)) == 3
        assert len(set(movements_det)) == 1

    # test pad by list of exact pixel values
    pads = [
        ([0, 2], 0, 0, 0),
        (0, [0, 2], 0, 0),
        (0, 0, [0, 2], 0),
        (0, 0, 0, [0, 2]),
    ]
    for pad in pads:
        top, right, bottom, left = pad
        height, width = base_img.shape[0:2]
        aug = iaa.Pad(px=pad, keep_size=False)
        aug_det = aug.to_deterministic()

        images_padded = []
        keypoints_padded = []
        top_range = top if isinstance(top, list) else [top]
        right_range = right if isinstance(right, list) else [right]
        bottom_range = bottom if isinstance(bottom, list) else [bottom]
        left_range = left if isinstance(left, list) else [left]
        for top_val in top_range:
            for right_val in right_range:
                for bottom_val in bottom_range:
                    for left_val in left_range:
                        images_padded.append(np.pad(base_img, ((top_val, bottom_val), (left_val, right_val), (0, 0)), mode="constant", constant_values=0))
                        keypoints_padded.append(keypoints[0].shift(x=left_val, y=top_val))

        movements = []
        movements_det = []
        for i in sm.xrange(100):
            observed = aug.augment_images(images)
            matches = [1 if np.array_equal(observed, np.array([base_img_padded])) else 0
                       for base_img_padded in images_padded]
            movements.append(np.argmax(np.array(matches)))
            assert any([val == 1 for val in matches])

            observed = aug_det.augment_images(images)
            matches = [1 if np.array_equal(observed, np.array([base_img_padded])) else 0
                       for base_img_padded in images_padded]
            movements_det.append(np.argmax(np.array(matches)))
            assert any([val == 1 for val in matches])

            observed = aug.augment_images(images_list)
            assert any([array_equal_lists(observed, [base_img_padded])
                        for base_img_padded in images_padded])

            observed = aug.augment_keypoints(keypoints)
            assert any([keypoints_equal(observed, [kp]) for kp in keypoints_padded])

        assert len(set(movements)) == 2
        assert len(set(movements_det)) == 1

    # TODO
    #print("[Note] Pad by percentages is currently not tested.")
    #print("[Note] Landmark projection after pad with resize is currently not tested.")


def test_Crop():
    reseed()

    base_img = np.array([[0, 0, 0],
                         [0, 1, 0],
                         [0, 0, 0]], dtype=np.uint8)
    base_img = base_img[:, :, np.newaxis]

    images = np.array([base_img])
    images_list = [base_img]

    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=2)], shape=base_img.shape)]

    # test crop by 1 pixel on each side
    crops = [
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1),
    ]
    for crop in crops:
        top, right, bottom, left = crop
        height, width = base_img.shape[0:2]
        aug = iaa.Crop(px=crop, keep_size=False)
        base_img_cropped = base_img[top:height-bottom, left:width-right, :]
        observed = aug.augment_images(images)
        assert np.array_equal(observed, np.array([base_img_cropped]))

        observed = aug.augment_images(images_list)
        assert array_equal_lists(observed, [base_img_cropped])

        keypoints_moved = [keypoints[0].shift(x=-left, y=-top)]
        observed = aug.augment_keypoints(keypoints)
        assert keypoints_equal(observed, keypoints_moved)

    # test crop by range of pixels
    crops = [
        ((0, 2), 0, 0, 0),
        (0, (0, 2), 0, 0),
        (0, 0, (0, 2), 0),
        (0, 0, 0, (0, 2)),
    ]
    for crop in crops:
        top, right, bottom, left = crop
        height, width = base_img.shape[0:2]
        aug = iaa.Crop(px=crop, keep_size=False)
        aug_det = aug.to_deterministic()

        images_cropped = []
        keypoints_cropped = []
        top_range = top if isinstance(top, tuple) else (top, top)
        right_range = right if isinstance(right, tuple) else (right, right)
        bottom_range = bottom if isinstance(bottom, tuple) else (bottom, bottom)
        left_range = left if isinstance(left, tuple) else (left, left)
        for top_val in sm.xrange(top_range[0], top_range[1]+1):
            for right_val in sm.xrange(right_range[0], right_range[1]+1):
                for bottom_val in sm.xrange(bottom_range[0], bottom_range[1]+1):
                    for left_val in sm.xrange(left_range[0], left_range[1]+1):

                        images_cropped.append(base_img[top_val:height-bottom_val, left_val:width-right_val, :])
                        keypoints_cropped.append(keypoints[0].shift(x=-left_val, y=-top_val))

        movements = []
        movements_det = []
        for i in sm.xrange(100):
            observed = aug.augment_images(images)

            matches = [1 if np.array_equal(observed, np.array([base_img_cropped])) else 0
                       for base_img_cropped in images_cropped]
            movements.append(np.argmax(np.array(matches)))
            assert any([val == 1 for val in matches])

            observed = aug_det.augment_images(images)
            matches = [1 if np.array_equal(observed, np.array([base_img_cropped])) else 0
                       for base_img_cropped in images_cropped]
            movements_det.append(np.argmax(np.array(matches)))
            assert any([val == 1 for val in matches])

            observed = aug.augment_images(images_list)
            assert any([array_equal_lists(observed, [base_img_cropped])
                        for base_img_cropped in images_cropped])

            observed = aug.augment_keypoints(keypoints)
            assert any([keypoints_equal(observed, [kp]) for kp in keypoints_cropped])

        assert len(set(movements)) == 3
        assert len(set(movements_det)) == 1

    # test crop by list of exact pixel values
    crops = [
        ([0, 2], 0, 0, 0),
        (0, [0, 2], 0, 0),
        (0, 0, [0, 2], 0),
        (0, 0, 0, [0, 2]),
    ]
    for crop in crops:
        top, right, bottom, left = crop
        height, width = base_img.shape[0:2]
        aug = iaa.Crop(px=crop, keep_size=False)
        aug_det = aug.to_deterministic()

        images_cropped = []
        keypoints_cropped = []
        top_range = top if isinstance(top, list) else [top]
        right_range = right if isinstance(right, list) else [right]
        bottom_range = bottom if isinstance(bottom, list) else [bottom]
        left_range = left if isinstance(left, list) else [left]
        for top_val in top_range:
            for right_val in right_range:
                for bottom_val in bottom_range:
                    for left_val in left_range:
                        images_cropped.append(base_img[top_val:height-bottom_val, left_val:width-right_val, :])
                        keypoints_cropped.append(keypoints[0].shift(x=-left_val, y=-top_val))

        movements = []
        movements_det = []
        for i in sm.xrange(100):
            observed = aug.augment_images(images)
            matches = [1 if np.array_equal(observed, np.array([base_img_cropped])) else 0
                       for base_img_cropped in images_cropped]
            movements.append(np.argmax(np.array(matches)))
            assert any([val == 1 for val in matches])

            observed = aug_det.augment_images(images)
            matches = [1 if np.array_equal(observed, np.array([base_img_cropped])) else 0
                       for base_img_cropped in images_cropped]
            movements_det.append(np.argmax(np.array(matches)))
            assert any([val == 1 for val in matches])

            observed = aug.augment_images(images_list)
            assert any([array_equal_lists(observed, [base_img_cropped])
                        for base_img_cropped in images_cropped])

            observed = aug.augment_keypoints(keypoints)
            assert any([keypoints_equal(observed, [kp]) for kp in keypoints_cropped])

        assert len(set(movements)) == 2
        assert len(set(movements_det)) == 1

    # TODO
    #print("[Note] Crop by percentages is currently not tested.")
    #print("[Note] Landmark projection after crop with resize is currently not tested.")


def test_Fliplr():
    reseed()

    base_img = np.array([[0, 0, 1],
                         [0, 0, 1],
                         [0, 1, 1]], dtype=np.uint8)
    base_img = base_img[:, :, np.newaxis]

    base_img_flipped = np.array([[1, 0, 0],
                                 [1, 0, 0],
                                 [1, 1, 0]], dtype=np.uint8)
    base_img_flipped = base_img_flipped[:, :, np.newaxis]

    images = np.array([base_img])
    images_flipped = np.array([base_img_flipped])

    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=2)], shape=base_img.shape)]
    keypoints_flipped = [ia.KeypointsOnImage([ia.Keypoint(x=2, y=0), ia.Keypoint(x=1, y=1),
                                              ia.Keypoint(x=0, y=2)], shape=base_img.shape)]

    # 0% chance of flip
    aug = iaa.Fliplr(0)
    aug_det = aug.to_deterministic()

    for _ in sm.xrange(10):
        observed = aug.augment_images(images)
        expected = images
        assert np.array_equal(observed, expected)

        observed = aug_det.augment_images(images)
        expected = images
        assert np.array_equal(observed, expected)

        observed = aug.augment_keypoints(keypoints)
        expected = keypoints
        assert keypoints_equal(observed, expected)

        observed = aug_det.augment_keypoints(keypoints)
        expected = keypoints
        assert keypoints_equal(observed, expected)

    # 100% chance of flip
    aug = iaa.Fliplr(1.0)
    aug_det = aug.to_deterministic()

    for _ in sm.xrange(10):
        observed = aug.augment_images(images)
        expected = images_flipped
        assert np.array_equal(observed, expected)

        observed = aug_det.augment_images(images)
        expected = images_flipped
        assert np.array_equal(observed, expected)

        observed = aug.augment_keypoints(keypoints)
        expected = keypoints_flipped
        assert keypoints_equal(observed, expected)

        observed = aug_det.augment_keypoints(keypoints)
        expected = keypoints_flipped
        assert keypoints_equal(observed, expected)

    # 50% chance of flip
    aug = iaa.Fliplr(0.5)
    aug_det = aug.to_deterministic()

    nb_iterations = 1000
    nb_images_flipped = 0
    nb_images_flipped_det = 0
    nb_keypoints_flipped = 0
    nb_keypoints_flipped_det = 0
    for _ in sm.xrange(nb_iterations):
        observed = aug.augment_images(images)
        if np.array_equal(observed, images_flipped):
            nb_images_flipped += 1

        observed = aug_det.augment_images(images)
        if np.array_equal(observed, images_flipped):
            nb_images_flipped_det += 1

        observed = aug.augment_keypoints(keypoints)
        if keypoints_equal(observed, keypoints_flipped):
            nb_keypoints_flipped += 1

        observed = aug_det.augment_keypoints(keypoints)
        if keypoints_equal(observed, keypoints_flipped):
            nb_keypoints_flipped_det += 1

    assert int(nb_iterations * 0.3) <= nb_images_flipped <= int(nb_iterations * 0.7)
    assert int(nb_iterations * 0.3) <= nb_keypoints_flipped <= int(nb_iterations * 0.7)
    assert nb_images_flipped_det in [0, nb_iterations]
    assert nb_keypoints_flipped_det in [0, nb_iterations]

    # 50% chance of flipped, multiple images, list as input
    images_multi = [base_img, base_img]
    aug = iaa.Fliplr(0.5)
    aug_det = aug.to_deterministic()
    nb_iterations = 1000
    nb_flipped_by_pos = [0] * len(images_multi)
    nb_flipped_by_pos_det = [0] * len(images_multi)
    for _ in sm.xrange(nb_iterations):
        observed = aug.augment_images(images_multi)
        for i in sm.xrange(len(images_multi)):
            if np.array_equal(observed[i], base_img_flipped):
                nb_flipped_by_pos[i] += 1

        observed = aug_det.augment_images(images_multi)
        for i in sm.xrange(len(images_multi)):
            if np.array_equal(observed[i], base_img_flipped):
                nb_flipped_by_pos_det[i] += 1

    for val in nb_flipped_by_pos:
        assert int(nb_iterations * 0.3) <= val <= int(nb_iterations * 0.7)

    for val in nb_flipped_by_pos_det:
        assert val in [0, nb_iterations]


def test_Flipud():
    reseed()

    base_img = np.array([[0, 0, 1],
                         [0, 0, 1],
                         [0, 1, 1]], dtype=np.uint8)
    base_img = base_img[:, :, np.newaxis]

    base_img_flipped = np.array([[0, 1, 1],
                                 [0, 0, 1],
                                 [0, 0, 1]], dtype=np.uint8)
    base_img_flipped = base_img_flipped[:, :, np.newaxis]

    images = np.array([base_img])
    images_flipped = np.array([base_img_flipped])

    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=2)], shape=base_img.shape)]
    keypoints_flipped = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=2), ia.Keypoint(x=1, y=1),
                                              ia.Keypoint(x=2, y=0)], shape=base_img.shape)]

    # 0% chance of flip
    aug = iaa.Flipud(0)
    aug_det = aug.to_deterministic()

    for _ in sm.xrange(10):
        observed = aug.augment_images(images)
        expected = images
        assert np.array_equal(observed, expected)

        observed = aug_det.augment_images(images)
        expected = images
        assert np.array_equal(observed, expected)

        observed = aug.augment_keypoints(keypoints)
        expected = keypoints
        assert keypoints_equal(observed, expected)

        observed = aug_det.augment_keypoints(keypoints)
        expected = keypoints
        assert keypoints_equal(observed, expected)

    # 100% chance of flip
    aug = iaa.Flipud(1.0)
    aug_det = aug.to_deterministic()

    for _ in sm.xrange(10):
        observed = aug.augment_images(images)
        expected = images_flipped
        assert np.array_equal(observed, expected)

        observed = aug_det.augment_images(images)
        expected = images_flipped
        assert np.array_equal(observed, expected)

        observed = aug.augment_keypoints(keypoints)
        expected = keypoints_flipped
        assert keypoints_equal(observed, expected)

        observed = aug_det.augment_keypoints(keypoints)
        expected = keypoints_flipped
        assert keypoints_equal(observed, expected)

    # 50% chance of flip
    aug = iaa.Flipud(0.5)
    aug_det = aug.to_deterministic()

    nb_iterations = 1000
    nb_images_flipped = 0
    nb_images_flipped_det = 0
    nb_keypoints_flipped = 0
    nb_keypoints_flipped_det = 0
    for _ in sm.xrange(nb_iterations):
        observed = aug.augment_images(images)
        if np.array_equal(observed, images_flipped):
            nb_images_flipped += 1

        observed = aug_det.augment_images(images)
        if np.array_equal(observed, images_flipped):
            nb_images_flipped_det += 1

        observed = aug.augment_keypoints(keypoints)
        if keypoints_equal(observed, keypoints_flipped):
            nb_keypoints_flipped += 1

        observed = aug_det.augment_keypoints(keypoints)
        if keypoints_equal(observed, keypoints_flipped):
            nb_keypoints_flipped_det += 1

    assert int(nb_iterations * 0.3) <= nb_images_flipped <= int(nb_iterations * 0.7)
    assert int(nb_iterations * 0.3) <= nb_keypoints_flipped <= int(nb_iterations * 0.7)
    assert nb_images_flipped_det in [0, nb_iterations]
    assert nb_keypoints_flipped_det in [0, nb_iterations]

    # 50% chance of flipped, multiple images, list as input
    images_multi = [base_img, base_img]
    aug = iaa.Flipud(0.5)
    aug_det = aug.to_deterministic()
    nb_iterations = 1000
    nb_flipped_by_pos = [0] * len(images_multi)
    nb_flipped_by_pos_det = [0] * len(images_multi)
    for _ in sm.xrange(nb_iterations):
        observed = aug.augment_images(images_multi)
        for i in sm.xrange(len(images_multi)):
            if np.array_equal(observed[i], base_img_flipped):
                nb_flipped_by_pos[i] += 1

        observed = aug_det.augment_images(images_multi)
        for i in sm.xrange(len(images_multi)):
            if np.array_equal(observed[i], base_img_flipped):
                nb_flipped_by_pos_det[i] += 1

    for val in nb_flipped_by_pos:
        assert int(nb_iterations * 0.3) <= val <= int(nb_iterations * 0.7)

    for val in nb_flipped_by_pos_det:
        assert val in [0, nb_iterations]


def test_GaussianBlur():
    reseed()

    base_img = np.array([[0, 0, 0],
                         [0, 255, 0],
                         [0, 0, 0]], dtype=np.uint8)
    base_img = base_img[:, :, np.newaxis]

    images = np.array([base_img])
    images_list = [base_img]
    outer_pixels = ([], [])
    for i in sm.xrange(base_img.shape[0]):
        for j in sm.xrange(base_img.shape[1]):
            if i != j:
                outer_pixels[0].append(i)
                outer_pixels[1].append(j)

    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=2)], shape=base_img.shape)]

    # no blur, shouldnt change anything
    aug = iaa.GaussianBlur(sigma=0)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    expected = images
    assert np.array_equal(observed, expected)

    # weak blur of center pixel
    aug = iaa.GaussianBlur(sigma=0.5)
    aug_det = aug.to_deterministic()

    #np.set_printoptions(formatter={'float_kind': lambda x: "%.6f" % x})
    #from scipy import ndimage
    #images2 = np.copy(images).astype(np.float32)
    #images2[0, ...] = ndimage.gaussian_filter(images2[0, ...], 0.4)
    #print(images2)

    # images as numpy array
    observed = aug.augment_images(images)
    assert 100 < observed[0][1, 1] < 255
    assert (observed[0][outer_pixels[0], outer_pixels[1]] > 0).all()
    assert (observed[0][outer_pixels[0], outer_pixels[1]] < 50).all()

    observed = aug_det.augment_images(images)
    assert 100 < observed[0][1, 1] < 255
    assert (observed[0][outer_pixels[0], outer_pixels[1]] > 0).all()
    assert (observed[0][outer_pixels[0], outer_pixels[1]] < 50).all()

    # images as list
    observed = aug.augment_images(images_list)
    assert 100 < observed[0][1, 1] < 255
    assert (observed[0][outer_pixels[0], outer_pixels[1]] > 0).all()
    assert (observed[0][outer_pixels[0], outer_pixels[1]] < 50).all()

    observed = aug_det.augment_images(images_list)
    assert 100 < observed[0][1, 1] < 255
    assert (observed[0][outer_pixels[0], outer_pixels[1]] > 0).all()
    assert (observed[0][outer_pixels[0], outer_pixels[1]] < 50).all()

    # keypoints shouldnt be changed
    observed = aug.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    observed = aug_det.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    # varying blur sigmas
    aug = iaa.GaussianBlur(sigma=(0, 1))
    aug_det = aug.to_deterministic()

    last_aug = None
    last_aug_det = None
    nb_changed_aug = 0
    nb_changed_aug_det = 0
    nb_iterations = 1000
    for i in sm.xrange(nb_iterations):
        observed_aug = aug.augment_images(images)
        observed_aug_det = aug_det.augment_images(images)
        if i == 0:
            last_aug = observed_aug
            last_aug_det = observed_aug_det
        else:
            if not np.array_equal(observed_aug, last_aug):
                nb_changed_aug += 1
            if not np.array_equal(observed_aug_det, last_aug_det):
                nb_changed_aug_det += 1
            last_aug = observed_aug
            last_aug_det = observed_aug_det
    assert nb_changed_aug >= int(nb_iterations * 0.8)
    assert nb_changed_aug_det == 0


def test_AverageBlur():
    reseed()

    base_img = np.zeros((11, 11, 1), dtype=np.uint8)
    base_img[5, 5, 0] = 200
    base_img[4, 5, 0] = 100
    base_img[6, 5, 0] = 100
    base_img[5, 4, 0] = 100
    base_img[5, 6, 0] = 100

    blur3x3 = np.copy(base_img)
    blur3x3 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 11, 11, 11, 0, 0, 0, 0],
        [0, 0, 0, 11, 44, 56, 44, 11, 0, 0, 0],
        [0, 0, 0, 11, 56, 67, 56, 11, 0, 0, 0],
        [0, 0, 0, 11, 44, 56, 44, 11, 0, 0, 0],
        [0, 0, 0, 0, 11, 11, 11, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    blur3x3 = np.array(blur3x3, dtype=np.uint8)[..., np.newaxis]

    blur4x4 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 6, 6, 6, 0, 0, 0],
        [0, 0, 0, 6, 25, 31, 31, 25, 6, 0, 0],
        [0, 0, 0, 6, 31, 38, 38, 31, 6, 0, 0],
        [0, 0, 0, 6, 31, 38, 38, 31, 6, 0, 0],
        [0, 0, 0, 6, 25, 31, 31, 25, 6, 0, 0],
        [0, 0, 0, 0, 6, 6, 6, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    blur4x4 = np.array(blur4x4, dtype=np.uint8)[..., np.newaxis]

    blur5x5 = np.copy(base_img)
    blur5x5 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0],
        [0, 0, 4, 16, 20, 20, 20, 16, 4, 0, 0],
        [0, 0, 4, 20, 24, 24, 24, 20, 4, 0, 0],
        [0, 0, 4, 20, 24, 24, 24, 20, 4, 0, 0],
        [0, 0, 4, 20, 24, 24, 24, 20, 4, 0, 0],
        [0, 0, 4, 16, 20, 20, 20, 16, 4, 0, 0],
        [0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    blur5x5 = np.array(blur5x5, dtype=np.uint8)[..., np.newaxis]

    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=2)], shape=base_img.shape)]

    # no blur, shouldnt change anything
    aug = iaa.AverageBlur(k=0)
    observed = aug.augment_image(base_img)
    assert np.array_equal(observed, base_img)

    # k=3
    aug = iaa.AverageBlur(k=3)
    observed = aug.augment_image(base_img)
    assert np.array_equal(observed, blur3x3)

    # k=5
    aug = iaa.AverageBlur(k=5)
    observed = aug.augment_image(base_img)
    assert np.array_equal(observed, blur5x5)

    # k as (3, 4)
    aug = iaa.AverageBlur(k=(3, 4))
    nb_iterations = 100
    nb_seen = [0, 0]
    for i in sm.xrange(nb_iterations):
        observed = aug.augment_image(base_img)
        if np.array_equal(observed, blur3x3):
            nb_seen[0] += 1
        elif np.array_equal(observed, blur4x4):
            nb_seen[1] += 1
        else:
            raise Exception("Unexpected result in AverageBlur@1")
    p_seen = [v/nb_iterations for v in nb_seen]
    assert 0.4 <= p_seen[0] <= 0.6
    assert 0.4 <= p_seen[1] <= 0.6

    # k as (3, 5)
    aug = iaa.AverageBlur(k=(3, 5))
    nb_iterations = 100
    nb_seen = [0, 0, 0]
    for i in sm.xrange(nb_iterations):
        observed = aug.augment_image(base_img)
        if np.array_equal(observed, blur3x3):
            nb_seen[0] += 1
        elif np.array_equal(observed, blur4x4):
            nb_seen[1] += 1
        elif np.array_equal(observed, blur5x5):
            nb_seen[2] += 1
        else:
            raise Exception("Unexpected result in AverageBlur@2")
    p_seen = [v/nb_iterations for v in nb_seen]
    assert 0.23 <= p_seen[0] <= 0.43
    assert 0.23 <= p_seen[1] <= 0.43
    assert 0.23 <= p_seen[2] <= 0.43

    # k as stochastic parameter
    aug = iaa.AverageBlur(k=iap.Choice([3, 5]))
    nb_iterations = 100
    nb_seen = [0, 0]
    for i in sm.xrange(nb_iterations):
        observed = aug.augment_image(base_img)
        if np.array_equal(observed, blur3x3):
            nb_seen[0] += 1
        elif np.array_equal(observed, blur5x5):
            nb_seen[1] += 1
        else:
            raise Exception("Unexpected result in AverageBlur@3")
    p_seen = [v/nb_iterations for v in nb_seen]
    assert 0.4 <= p_seen[0] <= 0.6
    assert 0.4 <= p_seen[1] <= 0.6

    # k as ((3, 5), (3, 5))
    aug = iaa.AverageBlur(k=((3, 5), (3, 5)))

    possible = dict()
    for kh in [3, 4, 5]:
        for kw in [3, 4, 5]:
            key = (kh, kw)
            if kh == 0 or kw == 0:
                possible[key] = np.copy(base_img)
            else:
                possible[key] = cv2.blur(base_img, (kh, kw))[..., np.newaxis]

    nb_iterations = 250
    #nb_seen = [0] * len(possible.keys())
    nb_seen = dict([(key, 0) for key, val in possible.items()])
    for i in sm.xrange(nb_iterations):
        observed = aug.augment_image(base_img)
        for key, img_aug in possible.items():
            if np.array_equal(observed, img_aug):
                nb_seen[key] += 1
    # dont check sum here, because 0xX and Xx0 are all the same, i.e. much
    # higher sum than nb_iterations
    assert all([v > 0 for v in nb_seen.values()])

    # keypoints shouldnt be changed
    aug = iaa.AverageBlur(k=3)
    aug_det = aug.to_deterministic()
    observed = aug.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    observed = aug_det.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)


def test_MedianBlur():
    reseed()

    base_img = np.zeros((11, 11, 1), dtype=np.uint8)
    base_img[3:8, 3:8, 0] = 1
    base_img[4:7, 4:7, 0] = 2
    base_img[5:6, 5:6, 0] = 3

    blur3x3 = np.zeros_like(base_img)
    blur3x3[3:8, 3:8, 0] = 1
    blur3x3[4:7, 4:7, 0] = 2
    blur3x3[4, 4, 0] = 1
    blur3x3[4, 6, 0] = 1
    blur3x3[6, 4, 0] = 1
    blur3x3[6, 6, 0] = 1
    blur3x3[3, 3, 0] = 0
    blur3x3[3, 7, 0] = 0
    blur3x3[7, 3, 0] = 0
    blur3x3[7, 7, 0] = 0

    blur5x5 = np.copy(blur3x3)
    blur5x5[4, 3, 0] = 0
    blur5x5[3, 4, 0] = 0
    blur5x5[6, 3, 0] = 0
    blur5x5[7, 4, 0] = 0
    blur5x5[4, 7, 0] = 0
    blur5x5[3, 6, 0] = 0
    blur5x5[6, 7, 0] = 0
    blur5x5[7, 6, 0] = 0
    blur5x5[blur5x5 > 1] = 1
    #blur5x5 = np.zeros_like(base_img)
    #blur5x5[2:9, 2:9, 0] = 1
    #blur5x5[3:8, 3:8, 0] = 1
    #blur5x5[4:7, 4:7, 0] = 1
    #blur5x5[5:6, 5:6, 0] = 1

    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=2)], shape=base_img.shape)]

    # no blur, shouldnt change anything
    aug = iaa.MedianBlur(k=1)
    observed = aug.augment_image(base_img)
    assert np.array_equal(observed, base_img)

    # k=3
    aug = iaa.MedianBlur(k=3)
    observed = aug.augment_image(base_img)
    assert np.array_equal(observed, blur3x3)

    # k=5
    aug = iaa.MedianBlur(k=5)
    observed = aug.augment_image(base_img)
    assert np.array_equal(observed, blur5x5)

    # k as (3, 5)
    aug = iaa.MedianBlur(k=(3, 5))
    seen = [False, False]
    for i in sm.xrange(100):
        observed = aug.augment_image(base_img)
        if np.array_equal(observed, blur3x3):
            seen[0] = True
        elif np.array_equal(observed, blur5x5):
            seen[1] = True
        else:
            raise Exception("Unexpected result in MedianBlur@1")
        if all(seen):
            break
    assert all(seen)

    # k as stochastic parameter
    aug = iaa.MedianBlur(k=iap.Choice([3, 5]))
    seen = [False, False]
    for i in sm.xrange(100):
        observed = aug.augment_image(base_img)
        if np.array_equal(observed, blur3x3):
            seen[0] += True
        elif np.array_equal(observed, blur5x5):
            seen[1] += True
        else:
            raise Exception("Unexpected result in MedianBlur@2")
        if all(seen):
            break
    assert all(seen)

    # keypoints shouldnt be changed
    aug = iaa.MedianBlur(k=3)
    aug_det = aug.to_deterministic()
    observed = aug.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    observed = aug_det.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)


def test_AddToHueAndSaturation():
    reseed()

    # interestingly, when using this RGB2HSV and HSV2RGB conversion from skimage, the results
    # differ quite a bit from the cv2 ones
    """
    def _add_hue_saturation(img, value):
        img_hsv = color.rgb2hsv(img / 255.0)
        img_hsv[..., 0:2] += (value / 255.0)
        return color.hsv2rgb(img_hsv) * 255
    """

    def _add_hue_saturation(img, value):
        img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        img_hsv[..., 0:2] += value
        return cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)

    base_img = np.zeros((2, 2, 3), dtype=np.uint8)
    base_img[..., 0] += 20
    base_img[..., 1] += 40
    base_img[..., 2] += 60

    aug = iaa.AddToHueAndSaturation(0)
    observed = aug.augment_image(base_img)
    expected = base_img
    assert np.allclose(observed, expected)

    aug = iaa.AddToHueAndSaturation(30)
    observed = aug.augment_image(base_img)
    expected = _add_hue_saturation(base_img, 30)
    diff = np.abs(observed.astype(np.float32) - expected)
    assert np.all(diff <= 3)

    aug = iaa.AddToHueAndSaturation((0, 2))
    base_img = base_img[0:1, 0:1, :]
    expected_imgs = [
        iaa.AddToHueAndSaturation(0).augment_image(base_img),
        iaa.AddToHueAndSaturation(1).augment_image(base_img),
        iaa.AddToHueAndSaturation(2).augment_image(base_img)
    ]
    assert not np.array_equal(expected_imgs[0], expected_imgs[1])
    assert not np.array_equal(expected_imgs[1], expected_imgs[2])
    assert not np.array_equal(expected_imgs[0], expected_imgs[2])
    nb_iterations = 300
    seen = dict([(i, 0) for i, _ in enumerate(expected_imgs)])
    for _ in sm.xrange(nb_iterations):
        observed = aug.augment_image(base_img)
        for i, expected_img in enumerate(expected_imgs):
            if np.allclose(observed, expected_img):
                seen[i] += 1
    assert np.sum(list(seen.values())) == nb_iterations
    n_exp = nb_iterations / 3
    n_exp_tol = nb_iterations * 0.1
    assert all([n_exp - n_exp_tol < v < n_exp + n_exp_tol for v in seen.values()])


def test_Grayscale():
    reseed()

    def _compute_luminosity(r, g, b):
        return 0.21 * r + 0.72 * g + 0.07 * b

    base_img = np.zeros((4, 4, 3), dtype=np.uint8)
    base_img[..., 0] += 10
    base_img[..., 1] += 20
    base_img[..., 2] += 30

    aug = iaa.Grayscale(0.0)
    observed = aug.augment_image(base_img)
    expected = np.copy(base_img)
    assert np.allclose(observed, expected)

    aug = iaa.Grayscale(1.0)
    observed = aug.augment_image(base_img)
    luminosity = _compute_luminosity(10, 20, 30)
    expected = np.zeros_like(base_img) + luminosity
    assert np.allclose(observed, expected.astype(np.uint8))

    aug = iaa.Grayscale(0.5)
    observed = aug.augment_image(base_img)
    luminosity = _compute_luminosity(10, 20, 30)
    expected = 0.5 * base_img + 0.5 * luminosity
    assert np.allclose(observed, expected.astype(np.uint8))

    aug = iaa.Grayscale((0.0, 1.0))
    base_img = base_img[0:1, 0:1, :]
    base_img_gray = iaa.Grayscale(1.0).augment_image(base_img)
    distance_max = np.average(np.abs(base_img_gray.astype(np.int32) - base_img.astype(np.int32)))
    nb_iterations = 1000
    distances = []
    for _ in sm.xrange(nb_iterations):
        observed = aug.augment_image(base_img)
        distance = np.average(np.abs(observed.astype(np.int32) - base_img.astype(np.int32))) / distance_max
        distances.append(distance)

    assert 0 - 1e-4 < min(distances) < 0.1
    assert 0.4 < np.average(distances) < 0.6
    assert 0.9 < max(distances) < 1.0 + 1e-4

    nb_bins = 5
    hist, _ = np.histogram(distances, bins=nb_bins, range=(0.0, 1.0), density=False)
    density_expected = 1.0/nb_bins
    density_tolerance = 0.05
    for nb_samples in hist:
        density = nb_samples / nb_iterations
        assert density_expected - density_tolerance < density < density_expected + density_tolerance


def test_Sharpen():
    reseed()

    def _compute_sharpened_base_img(lightness, m):
        base_img_sharpened = np.zeros((3, 3), dtype=np.float32)
        k = 1
        # note that cv2 uses reflection padding by default
        base_img_sharpened[0, 0] = (m[1, 1] + lightness)/k * 10 + 4 * (m[0, 0]/k) * 10 + 4 * (m[2, 2]/k) * 20
        base_img_sharpened[0, 2] = base_img_sharpened[0, 0]
        base_img_sharpened[2, 0] = base_img_sharpened[0, 0]
        base_img_sharpened[2, 2] = base_img_sharpened[0, 0]
        base_img_sharpened[0, 1] = (m[1, 1] + lightness)/k * 10 + 6 * (m[0, 1]/k) * 10 + 2 * (m[2, 2]/k) * 20
        base_img_sharpened[1, 0] = base_img_sharpened[0, 1]
        base_img_sharpened[1, 2] = base_img_sharpened[0, 1]
        base_img_sharpened[2, 1] = base_img_sharpened[0, 1]
        base_img_sharpened[1, 1] = (m[1, 1] + lightness)/k * 20 + 8 * (m[0, 1]/k) * 10

        #print("A", base_img_sharpened, "Am", m)
        base_img_sharpened = np.clip(base_img_sharpened, 0, 255).astype(np.uint8)

        return base_img_sharpened

    base_img = [[10, 10, 10],
                [10, 20, 10],
                [10, 10, 10]]
    base_img = np.uint8(base_img)
    m = np.float32([[-1, -1, -1],
                    [-1, 8, -1],
                    [-1, -1, -1]])
    m_noop = np.float32([[0, 0, 0],
                         [0, 1, 0],
                         [0, 0, 0]])
    base_img_sharpened = _compute_sharpened_base_img(1, m)

    aug = iaa.Sharpen(alpha=0, lightness=1)
    observed = aug.augment_image(base_img)
    expected = base_img
    assert np.allclose(observed, expected)

    aug = iaa.Sharpen(alpha=1.0, lightness=1)
    observed = aug.augment_image(base_img)
    expected = base_img_sharpened
    assert np.allclose(observed, expected)

    aug = iaa.Sharpen(alpha=0.5, lightness=1)
    observed = aug.augment_image(base_img)
    expected = _compute_sharpened_base_img(0.5*1, 0.5 * m_noop + 0.5 * m)
    assert np.allclose(observed, expected.astype(np.uint8))

    aug = iaa.Sharpen(alpha=0.75, lightness=1)
    observed = aug.augment_image(base_img)
    expected = _compute_sharpened_base_img(0.75*1, 0.25 * m_noop + 0.75 * m)
    assert np.allclose(observed, expected)

    aug = iaa.Sharpen(alpha=1.0, lightness=2)
    observed = aug.augment_image(base_img)
    expected = _compute_sharpened_base_img(1.0*2, m)
    assert np.allclose(observed, expected)

    aug = iaa.Sharpen(alpha=1.0, lightness=3)
    observed = aug.augment_image(base_img)
    expected = _compute_sharpened_base_img(1.0*3, m)
    assert np.allclose(observed, expected)

    # this part doesnt really work so far due to nonlinearities resulting from clipping to uint8
    """
    # alpha range
    aug = iaa.Sharpen(alpha=(0.0, 1.0), lightness=1)
    base_img = np.copy(base_img)
    base_img_sharpened_min = _compute_sharpened_base_img(0.0*1, 1.0 * m_noop + 0.0 * m)
    base_img_sharpened_max = _compute_sharpened_base_img(1.0*1, 0.0 * m_noop + 1.0 * m)
    #distance_max = np.average(np.abs(base_img_sharpened.astype(np.float32) - base_img.astype(np.float32)))
    distance_max = np.average(np.abs(base_img_sharpened_max - base_img_sharpened_min))
    nb_iterations = 250
    distances = []
    for _ in sm.xrange(nb_iterations):
        observed = aug.augment_image(base_img)
        distance = np.average(np.abs(observed.astype(np.float32) - base_img_sharpened_max.astype(np.float32))) / distance_max
        distances.append(distance)

    print(distances)
    print(min(distances), np.average(distances), max(distances))
    assert 0 - 1e-4 < min(distances) < 0.1
    assert 0.4 < np.average(distances) < 0.6
    assert 0.9 < max(distances) < 1.0 + 1e-4

    nb_bins = 5
    hist, _ = np.histogram(distances, bins=nb_bins, range=(0.0, 1.0), density=False)
    density_expected = 1.0/nb_bins
    density_tolerance = 0.05
    for nb_samples in hist:
        density = nb_samples / nb_iterations
        assert density_expected - density_tolerance < density < density_expected + density_tolerance

    # lightness range
    aug = iaa.Sharpen(alpha=1.0, lightness=(0.5, 2.0))
    base_img = np.copy(base_img)
    base_img_sharpened = _compute_sharpened_base_img(1.0*2.0, m)
    distance_max = np.average(np.abs(base_img_sharpened.astype(np.int32) - base_img.astype(np.int32)))
    nb_iterations = 250
    distances = []
    for _ in sm.xrange(nb_iterations):
        observed = aug.augment_image(base_img)
        distance = np.average(np.abs(observed.astype(np.int32) - base_img.astype(np.int32))) / distance_max
        distances.append(distance)

    assert 0 - 1e-4 < min(distances) < 0.1
    assert 0.4 < np.average(distances) < 0.6
    assert 0.9 < max(distances) < 1.0 + 1e-4

    nb_bins = 5
    hist, _ = np.histogram(distances, bins=nb_bins, range=(0.0, 1.0), density=False)
    density_expected = 1.0/nb_bins
    density_tolerance = 0.05
    for nb_samples in hist:
        density = nb_samples / nb_iterations
        assert density_expected - density_tolerance < density < density_expected + density_tolerance
    """


def test_AdditiveGaussianNoise():
    reseed()

    #base_img = np.array([[128, 128, 128],
    #                     [128, 128, 128],
    #                     [128, 128, 128]], dtype=np.uint8)
    base_img = np.ones((16, 16, 1), dtype=np.uint8) * 128
    #base_img = base_img[:, :, np.newaxis]

    images = np.array([base_img])
    images_list = [base_img]

    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=2)], shape=base_img.shape)]

    # no noise, shouldnt change anything
    aug = iaa.AdditiveGaussianNoise(loc=0, scale=0)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    expected = images
    assert np.array_equal(observed, expected)

    # zero-centered noise
    aug = iaa.AdditiveGaussianNoise(loc=0, scale=0.2 * 255)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    assert not np.array_equal(observed, images)

    observed = aug_det.augment_images(images)
    assert not np.array_equal(observed, images)

    observed = aug.augment_images(images_list)
    assert not array_equal_lists(observed, images_list)

    observed = aug_det.augment_images(images_list)
    assert not array_equal_lists(observed, images_list)

    observed = aug.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints)

    observed = aug_det.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints)

    # std correct?
    aug = iaa.AdditiveGaussianNoise(loc=0, scale=0.2 * 255)
    aug_det = aug.to_deterministic()
    images = np.ones((1, 1, 1, 1), dtype=np.uint8) * 128
    nb_iterations = 1000
    values = []
    for i in sm.xrange(nb_iterations):
        images_aug = aug.augment_images(images)
        values.append(images_aug[0, 0, 0, 0])
    values = np.array(values)
    assert np.min(values) == 0
    assert 0.1 < np.std(values) / 255.0 < 0.4

    # non-zero loc
    aug = iaa.AdditiveGaussianNoise(loc=0.25 * 255, scale=0.01 * 255)
    aug_det = aug.to_deterministic()
    images = np.ones((1, 1, 1, 1), dtype=np.uint8) * 128
    nb_iterations = 1000
    values = []
    for i in sm.xrange(nb_iterations):
        images_aug = aug.augment_images(images)
        values.append(images_aug[0, 0, 0, 0] - 128)
    values = np.array(values)
    assert 54 < np.average(values) < 74 # loc=0.25 should be around 255*0.25=64 average

    # varying locs
    aug = iaa.AdditiveGaussianNoise(loc=(0, 0.5 * 255), scale=0.0001 * 255)
    aug_det = aug.to_deterministic()
    images = np.ones((1, 1, 1, 1), dtype=np.uint8) * 128
    last_aug = None
    last_aug_det = None
    nb_changed_aug = 0
    nb_changed_aug_det = 0
    nb_iterations = 1000
    for i in sm.xrange(nb_iterations):
        observed_aug = aug.augment_images(images)
        observed_aug_det = aug_det.augment_images(images)
        if i == 0:
            last_aug = observed_aug
            last_aug_det = observed_aug_det
        else:
            if not np.array_equal(observed_aug, last_aug):
                nb_changed_aug += 1
            if not np.array_equal(observed_aug_det, last_aug_det):
                nb_changed_aug_det += 1
            last_aug = observed_aug
            last_aug_det = observed_aug_det
    assert nb_changed_aug >= int(nb_iterations * 0.95)
    assert nb_changed_aug_det == 0

    # varying stds
    aug = iaa.AdditiveGaussianNoise(loc=0, scale=(0.01 * 255, 0.2 * 255))
    aug_det = aug.to_deterministic()
    images = np.ones((1, 1, 1, 1), dtype=np.uint8) * 128
    last_aug = None
    last_aug_det = None
    nb_changed_aug = 0
    nb_changed_aug_det = 0
    nb_iterations = 1000
    for i in sm.xrange(nb_iterations):
        observed_aug = aug.augment_images(images)
        observed_aug_det = aug_det.augment_images(images)
        if i == 0:
            last_aug = observed_aug
            last_aug_det = observed_aug_det
        else:
            if not np.array_equal(observed_aug, last_aug):
                nb_changed_aug += 1
            if not np.array_equal(observed_aug_det, last_aug_det):
                nb_changed_aug_det += 1
            last_aug = observed_aug
            last_aug_det = observed_aug_det
    assert nb_changed_aug >= int(nb_iterations * 0.95)
    assert nb_changed_aug_det == 0


#def test_MultiplicativeGaussianNoise():
#    pass

#def test_ReplacingGaussianNoise():
#    pass


def test_Dropout():
    reseed()

    base_img = np.ones((512, 512, 1), dtype=np.uint8) * 255

    images = np.array([base_img])
    images_list = [base_img]

    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=2)], shape=base_img.shape)]

    # no dropout, shouldnt change anything
    aug = iaa.Dropout(p=0)
    observed = aug.augment_images(images)
    expected = images
    assert np.array_equal(observed, expected)

    observed = aug.augment_images(images_list)
    expected = images_list
    assert array_equal_lists(observed, expected)

    # 100% dropout, should drop everything
    aug = iaa.Dropout(p=1.0)
    observed = aug.augment_images(images)
    expected = np.zeros((1, 512, 512, 1), dtype=np.uint8)
    assert np.array_equal(observed, expected)

    observed = aug.augment_images(images_list)
    expected = [np.zeros((512, 512, 1), dtype=np.uint8)]
    assert array_equal_lists(observed, expected)

    # 50% dropout
    aug = iaa.Dropout(p=0.5)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    assert not np.array_equal(observed, images)
    percent_nonzero = len(observed.flatten().nonzero()[0]) \
                      / (base_img.shape[0] * base_img.shape[1] * base_img.shape[2])
    assert 0.35 <= (1 - percent_nonzero) <= 0.65

    observed = aug_det.augment_images(images)
    assert not np.array_equal(observed, images)
    percent_nonzero = len(observed.flatten().nonzero()[0]) \
                      / (base_img.shape[0] * base_img.shape[1] * base_img.shape[2])
    assert 0.35 <= (1 - percent_nonzero) <= 0.65

    observed = aug.augment_images(images_list)
    assert not array_equal_lists(observed, images_list)
    percent_nonzero = len(observed[0].flatten().nonzero()[0]) \
                      / (base_img.shape[0] * base_img.shape[1] * base_img.shape[2])
    assert 0.35 <= (1 - percent_nonzero) <= 0.65

    observed = aug_det.augment_images(images_list)
    assert not array_equal_lists(observed, images_list)
    percent_nonzero = len(observed[0].flatten().nonzero()[0]) \
                      / (base_img.shape[0] * base_img.shape[1] * base_img.shape[2])
    assert 0.35 <= (1 - percent_nonzero) <= 0.65

    observed = aug.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints)

    observed = aug_det.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints)

    # varying p
    aug = iaa.Dropout(p=(0.0, 1.0))
    aug_det = aug.to_deterministic()
    images = np.ones((1, 8, 8, 1), dtype=np.uint8) * 255
    last_aug = None
    last_aug_det = None
    nb_changed_aug = 0
    nb_changed_aug_det = 0
    nb_iterations = 1000
    for i in sm.xrange(nb_iterations):
        observed_aug = aug.augment_images(images)
        observed_aug_det = aug_det.augment_images(images)
        if i == 0:
            last_aug = observed_aug
            last_aug_det = observed_aug_det
        else:
            if not np.array_equal(observed_aug, last_aug):
                nb_changed_aug += 1
            if not np.array_equal(observed_aug_det, last_aug_det):
                nb_changed_aug_det += 1
            last_aug = observed_aug
            last_aug_det = observed_aug_det
    assert nb_changed_aug >= int(nb_iterations * 0.95)
    assert nb_changed_aug_det == 0


def test_CoarseDropout():
    reseed()

    base_img = np.ones((16, 16, 1), dtype=np.uint8) * 100

    aug = iaa.CoarseDropout(p=0, size_px=4, size_percent=None, per_channel=False, min_size=4)
    observed = aug.augment_image(base_img)
    expected = base_img
    assert np.array_equal(observed, expected)

    aug = iaa.CoarseDropout(p=1.0, size_px=4, size_percent=None, per_channel=False, min_size=4)
    observed = aug.augment_image(base_img)
    expected = np.zeros_like(base_img)
    assert np.array_equal(observed, expected)

    aug = iaa.CoarseDropout(p=0.5, size_px=1, size_percent=None, per_channel=False, min_size=1)
    averages = []
    for _ in sm.xrange(50):
        observed = aug.augment_image(base_img)
        averages.append(np.average(observed))
    assert all([v in [0, 100] for v in averages])
    assert 50 - 20 < np.average(averages) < 50 + 20

    aug = iaa.CoarseDropout(p=0.5, size_px=None, size_percent=0.001, per_channel=False, min_size=1)
    averages = []
    for _ in sm.xrange(50):
        observed = aug.augment_image(base_img)
        averages.append(np.average(observed))
    assert all([v in [0, 100] for v in averages])
    assert 50 - 20 < np.average(averages) < 50 + 20

    aug = iaa.CoarseDropout(p=0.5, size_px=1, size_percent=None, per_channel=True, min_size=1)
    base_img = np.ones((4, 4, 3), dtype=np.uint8) * 100
    found = False
    for _ in sm.xrange(100):
        observed = aug.augment_image(base_img)
        avgs = np.average(observed, axis=(0, 1))
        if len(set(avgs)) >= 2:
            found = True
            break
    assert found


def test_Multiply():
    reseed()

    base_img = np.ones((3, 3, 1), dtype=np.uint8) * 100
    images = np.array([base_img])
    images_list = [base_img]
    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=2)], shape=base_img.shape)]

    # no multiply, shouldnt change anything
    aug = iaa.Multiply(mul=1.0)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    expected = images
    assert np.array_equal(observed, expected)

    observed = aug.augment_images(images_list)
    expected = images_list
    assert array_equal_lists(observed, expected)

    observed = aug_det.augment_images(images)
    expected = images
    assert np.array_equal(observed, expected)

    observed = aug_det.augment_images(images_list)
    expected = images_list
    assert array_equal_lists(observed, expected)

    # multiply >1.0
    aug = iaa.Multiply(mul=1.2)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    expected = np.ones((1, 3, 3, 1), dtype=np.uint8) * 120
    assert np.array_equal(observed, expected)

    observed = aug.augment_images(images_list)
    expected = [np.ones((3, 3, 1), dtype=np.uint8) * 120]
    assert array_equal_lists(observed, expected)

    observed = aug_det.augment_images(images)
    expected = np.ones((1, 3, 3, 1), dtype=np.uint8) * 120
    assert np.array_equal(observed, expected)

    observed = aug_det.augment_images(images_list)
    expected = [np.ones((3, 3, 1), dtype=np.uint8) * 120]
    assert array_equal_lists(observed, expected)

    # multiply <1.0
    aug = iaa.Multiply(mul=0.8)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    expected = np.ones((1, 3, 3, 1), dtype=np.uint8) * 80
    assert np.array_equal(observed, expected)

    observed = aug.augment_images(images_list)
    expected = [np.ones((3, 3, 1), dtype=np.uint8) * 80]
    assert array_equal_lists(observed, expected)

    observed = aug_det.augment_images(images)
    expected = np.ones((1, 3, 3, 1), dtype=np.uint8) * 80
    assert np.array_equal(observed, expected)

    observed = aug_det.augment_images(images_list)
    expected = [np.ones((3, 3, 1), dtype=np.uint8) * 80]
    assert array_equal_lists(observed, expected)

    # keypoints shouldnt be changed
    aug = iaa.Multiply(mul=1.2)
    aug_det = iaa.Multiply(mul=1.2).to_deterministic()
    observed = aug.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    observed = aug_det.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    # varying multiply factors
    aug = iaa.Multiply(mul=(0, 2.0))
    aug_det = aug.to_deterministic()

    last_aug = None
    last_aug_det = None
    nb_changed_aug = 0
    nb_changed_aug_det = 0
    nb_iterations = 1000
    for i in sm.xrange(nb_iterations):
        observed_aug = aug.augment_images(images)
        observed_aug_det = aug_det.augment_images(images)
        if i == 0:
            last_aug = observed_aug
            last_aug_det = observed_aug_det
        else:
            if not np.array_equal(observed_aug, last_aug):
                nb_changed_aug += 1
            if not np.array_equal(observed_aug_det, last_aug_det):
                nb_changed_aug_det += 1
            last_aug = observed_aug
            last_aug_det = observed_aug_det
    assert nb_changed_aug >= int(nb_iterations * 0.95)
    assert nb_changed_aug_det == 0

def test_MultiplyElementwise():
    reseed()

    base_img = np.ones((3, 3, 1), dtype=np.uint8) * 100
    images = np.array([base_img])
    images_list = [base_img]
    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=2)], shape=base_img.shape)]

    # no multiply, shouldnt change anything
    aug = iaa.MultiplyElementwise(mul=1.0)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    expected = images
    assert np.array_equal(observed, expected)

    observed = aug.augment_images(images_list)
    expected = images_list
    assert array_equal_lists(observed, expected)

    observed = aug_det.augment_images(images)
    expected = images
    assert np.array_equal(observed, expected)

    observed = aug_det.augment_images(images_list)
    expected = images_list
    assert array_equal_lists(observed, expected)

    # multiply >1.0
    aug = iaa.MultiplyElementwise(mul=1.2)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    expected = np.ones((1, 3, 3, 1), dtype=np.uint8) * 120
    assert np.array_equal(observed, expected)

    observed = aug.augment_images(images_list)
    expected = [np.ones((3, 3, 1), dtype=np.uint8) * 120]
    assert array_equal_lists(observed, expected)

    observed = aug_det.augment_images(images)
    expected = np.ones((1, 3, 3, 1), dtype=np.uint8) * 120
    assert np.array_equal(observed, expected)

    observed = aug_det.augment_images(images_list)
    expected = [np.ones((3, 3, 1), dtype=np.uint8) * 120]
    assert array_equal_lists(observed, expected)

    # multiply <1.0
    aug = iaa.MultiplyElementwise(mul=0.8)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    expected = np.ones((1, 3, 3, 1), dtype=np.uint8) * 80
    assert np.array_equal(observed, expected)

    observed = aug.augment_images(images_list)
    expected = [np.ones((3, 3, 1), dtype=np.uint8) * 80]
    assert array_equal_lists(observed, expected)

    observed = aug_det.augment_images(images)
    expected = np.ones((1, 3, 3, 1), dtype=np.uint8) * 80
    assert np.array_equal(observed, expected)

    observed = aug_det.augment_images(images_list)
    expected = [np.ones((3, 3, 1), dtype=np.uint8) * 80]
    assert array_equal_lists(observed, expected)

    # keypoints shouldnt be changed
    aug = iaa.MultiplyElementwise(mul=1.2)
    aug_det = iaa.Multiply(mul=1.2).to_deterministic()
    observed = aug.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    observed = aug_det.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    # varying multiply factors
    aug = iaa.MultiplyElementwise(mul=(0, 2.0))
    aug_det = aug.to_deterministic()

    last_aug = None
    last_aug_det = None
    nb_changed_aug = 0
    nb_changed_aug_det = 0
    nb_iterations = 1000
    for i in sm.xrange(nb_iterations):
        observed_aug = aug.augment_images(images)
        observed_aug_det = aug_det.augment_images(images)
        if i == 0:
            last_aug = observed_aug
            last_aug_det = observed_aug_det
        else:
            if not np.array_equal(observed_aug, last_aug):
                nb_changed_aug += 1
            if not np.array_equal(observed_aug_det, last_aug_det):
                nb_changed_aug_det += 1
            last_aug = observed_aug
            last_aug_det = observed_aug_det
    assert nb_changed_aug >= int(nb_iterations * 0.95)
    assert nb_changed_aug_det == 0

    # values should change between pixels
    aug = iaa.MultiplyElementwise(mul=(0.5, 1.5))

    nb_same = 0
    nb_different = 0
    nb_iterations = 1000
    for i in sm.xrange(nb_iterations):
        observed_aug = aug.augment_images(images)
        observed_aug_flat = observed_aug.flatten()
        last = None
        for j in sm.xrange(observed_aug_flat.size):
            if last is not None:
                v = observed_aug_flat[j]
                if v - 0.0001 <= last <= v + 0.0001:
                    nb_same += 1
                else:
                    nb_different += 1
            last = observed_aug_flat[j]
    assert nb_different > 0.95 * (nb_different + nb_same)

def test_ReplaceElementwise():
    reseed()

    base_img = np.ones((3, 3, 1), dtype=np.uint8) + 99
    images = np.array([base_img])
    images_list = [base_img]
    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=2)], shape=base_img.shape)]

    # no replace, shouldnt change anything
    aug = iaa.ReplaceElementwise(mask=0, replacement=0)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    expected = images
    assert np.array_equal(observed, expected)

    observed = aug.augment_images(images_list)
    expected = images_list
    assert array_equal_lists(observed, expected)

    observed = aug_det.augment_images(images)
    expected = images
    assert np.array_equal(observed, expected)

    observed = aug_det.augment_images(images_list)
    expected = images_list
    assert array_equal_lists(observed, expected)

    # replace at 100 percent prob., should change everything
    aug = iaa.ReplaceElementwise(mask=1, replacement=0)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    expected = np.zeros((1, 3, 3, 1), dtype=np.uint8)
    assert np.array_equal(observed, expected)

    observed = aug.augment_images(images_list)
    expected = [np.zeros((3, 3, 1), dtype=np.uint8)]
    assert array_equal_lists(observed, expected)

    observed = aug_det.augment_images(images)
    expected = np.zeros((1, 3, 3, 1), dtype=np.uint8)
    assert np.array_equal(observed, expected)

    observed = aug_det.augment_images(images_list)
    expected = [np.zeros((3, 3, 1), dtype=np.uint8)]
    assert array_equal_lists(observed, expected)

    # replace half
    aug = iaa.ReplaceElementwise(mask=iap.Binomial(p=0.5), replacement=0)

    nb_iterations = 100
    nb_diff_all = 0
    for i in sm.xrange(nb_iterations):
        img = np.ones((100, 100, 1), dtype=np.uint8)
        observed = aug.augment_image(img)
        nb_diff = np.sum(img != observed)
        nb_diff_all += nb_diff
    p = nb_diff_all / (nb_iterations * 100 * 100)
    assert 0.45 <= p <= 0.55

    """
    observed = aug.augment_images(images)
    expected = np.ones((1, 3, 3, 1), dtype=np.uint8) * 80
    assert np.array_equal(observed, expected)

    observed = aug.augment_images(images_list)
    expected = [np.ones((3, 3, 1), dtype=np.uint8) * 80]
    assert array_equal_lists(observed, expected)

    observed = aug_det.augment_images(images)
    expected = np.ones((1, 3, 3, 1), dtype=np.uint8) * 80
    assert np.array_equal(observed, expected)

    observed = aug_det.augment_images(images_list)
    expected = [np.ones((3, 3, 1), dtype=np.uint8) * 80]
    assert array_equal_lists(observed, expected)
    """

    # keypoints shouldnt be changed
    aug = iaa.ReplaceElementwise(mask=iap.Binomial(p=0.5), replacement=0)
    aug_det = iaa.ReplaceElementwise(mask=iap.Binomial(p=0.5), replacement=0).to_deterministic()
    observed = aug.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    observed = aug_det.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    # different replacements
    aug = iaa.ReplaceElementwise(mask=1, replacement=iap.Choice([100, 200]))
    img = np.zeros((1000, 1000, 1), dtype=np.uint8)
    img100 = img + 100
    img200 = img + 200
    observed = aug.augment_image(img)
    nb_diff_100 = np.sum(img100 != observed)
    nb_diff_200 = np.sum(img200 != observed)
    p100 = nb_diff_100 / (1000 * 1000)
    p200 = nb_diff_200 / (1000 * 1000)
    assert 0.45 <= p100 <= 0.55
    assert 0.45 <= p200 <= 0.55

def test_Add():
    reseed()

    base_img = np.ones((3, 3, 1), dtype=np.uint8) * 100
    images = np.array([base_img])
    images_list = [base_img]
    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=2)], shape=base_img.shape)]

    # no add, shouldnt change anything
    aug = iaa.Add(value=0)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    expected = images
    assert np.array_equal(observed, expected)

    observed = aug.augment_images(images_list)
    expected = images_list
    assert array_equal_lists(observed, expected)

    observed = aug_det.augment_images(images)
    expected = images
    assert np.array_equal(observed, expected)

    observed = aug_det.augment_images(images_list)
    expected = images_list
    assert array_equal_lists(observed, expected)

    # add > 0
    aug = iaa.Add(value=1)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    expected = images + 1
    assert np.array_equal(observed, expected)

    observed = aug.augment_images(images_list)
    expected = [images_list[0] + 1]
    assert array_equal_lists(observed, expected)

    observed = aug_det.augment_images(images)
    expected = images + 1
    assert np.array_equal(observed, expected)

    observed = aug_det.augment_images(images_list)
    expected = [images_list[0] + 1]
    assert array_equal_lists(observed, expected)

    # add < 0
    aug = iaa.Add(value=-1)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    expected = images - 1
    assert np.array_equal(observed, expected)

    observed = aug.augment_images(images_list)
    expected = [images_list[0] - 1]
    assert array_equal_lists(observed, expected)

    observed = aug_det.augment_images(images)
    expected = images - 1
    assert np.array_equal(observed, expected)

    observed = aug_det.augment_images(images_list)
    expected = [images_list[0] - 1]
    assert array_equal_lists(observed, expected)

    # test other parameters
    aug = iaa.Add(value=iap.DiscreteUniform(1, 10))
    observed = aug.augment_images(images)
    assert 100 + 1 <= np.average(observed) <= 100 + 10

    aug = iaa.Add(value=iap.Uniform(1, 10))
    observed = aug.augment_images(images)
    assert 100 + 1 <= np.average(observed) <= 100 + 10

    aug = iaa.Add(value=iap.Clip(iap.Normal(1, 1), -3, 3))
    observed = aug.augment_images(images)
    assert 100 - 3 <= np.average(observed) <= 100 + 3

    aug = iaa.Add(value=iap.Discretize(iap.Clip(iap.Normal(1, 1), -3, 3)))
    observed = aug.augment_images(images)
    assert 100 - 3 <= np.average(observed) <= 100 + 3

    # keypoints shouldnt be changed
    aug = iaa.Add(value=1)
    aug_det = iaa.Add(value=1).to_deterministic()
    observed = aug.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    observed = aug_det.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    # varying values
    aug = iaa.Add(value=(0, 10))
    aug_det = aug.to_deterministic()

    last_aug = None
    last_aug_det = None
    nb_changed_aug = 0
    nb_changed_aug_det = 0
    nb_iterations = 1000
    for i in sm.xrange(nb_iterations):
        observed_aug = aug.augment_images(images)
        observed_aug_det = aug_det.augment_images(images)
        if i == 0:
            last_aug = observed_aug
            last_aug_det = observed_aug_det
        else:
            if not np.array_equal(observed_aug, last_aug):
                nb_changed_aug += 1
            if not np.array_equal(observed_aug_det, last_aug_det):
                nb_changed_aug_det += 1
            last_aug = observed_aug
            last_aug_det = observed_aug_det
    assert nb_changed_aug >= int(nb_iterations * 0.7)
    assert nb_changed_aug_det == 0

def test_AddElementwise():
    reseed()

    base_img = np.ones((3, 3, 1), dtype=np.uint8) * 100
    images = np.array([base_img])
    images_list = [base_img]
    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=2)], shape=base_img.shape)]

    # no add, shouldnt change anything
    aug = iaa.AddElementwise(value=0)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    expected = images
    assert np.array_equal(observed, expected)

    observed = aug.augment_images(images_list)
    expected = images_list
    assert array_equal_lists(observed, expected)

    observed = aug_det.augment_images(images)
    expected = images
    assert np.array_equal(observed, expected)

    observed = aug_det.augment_images(images_list)
    expected = images_list
    assert array_equal_lists(observed, expected)

    # add > 0
    aug = iaa.AddElementwise(value=1)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    expected = images + 1
    assert np.array_equal(observed, expected)

    observed = aug.augment_images(images_list)
    expected = [images_list[0] + 1]
    assert array_equal_lists(observed, expected)

    observed = aug_det.augment_images(images)
    expected = images + 1
    assert np.array_equal(observed, expected)

    observed = aug_det.augment_images(images_list)
    expected = [images_list[0] + 1]
    assert array_equal_lists(observed, expected)

    # add < 0
    aug = iaa.AddElementwise(value=-1)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    expected = images - 1
    assert np.array_equal(observed, expected)

    observed = aug.augment_images(images_list)
    expected = [images_list[0] - 1]
    assert array_equal_lists(observed, expected)

    observed = aug_det.augment_images(images)
    expected = images - 1
    assert np.array_equal(observed, expected)

    observed = aug_det.augment_images(images_list)
    expected = [images_list[0] - 1]
    assert array_equal_lists(observed, expected)

    # test other parameters
    aug = iaa.AddElementwise(value=iap.DiscreteUniform(1, 10))
    observed = aug.augment_images(images)
    assert np.min(observed) >= 100 + 1
    assert np.max(observed) <= 100 + 10

    aug = iaa.AddElementwise(value=iap.Uniform(1, 10))
    observed = aug.augment_images(images)
    assert np.min(observed) >= 100 + 1
    assert np.max(observed) <= 100 + 10

    aug = iaa.AddElementwise(value=iap.Clip(iap.Normal(1, 1), -3, 3))
    observed = aug.augment_images(images)
    assert np.min(observed) >= 100 - 3
    assert np.max(observed) <= 100 + 3

    aug = iaa.AddElementwise(value=iap.Discretize(iap.Clip(iap.Normal(1, 1), -3, 3)))
    observed = aug.augment_images(images)
    assert np.min(observed) >= 100 - 3
    assert np.max(observed) <= 100 + 3

    # keypoints shouldnt be changed
    aug = iaa.AddElementwise(value=1)
    aug_det = iaa.AddElementwise(value=1).to_deterministic()
    observed = aug.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    observed = aug_det.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    # varying values
    aug = iaa.AddElementwise(value=(0, 10))
    aug_det = aug.to_deterministic()

    last_aug = None
    last_aug_det = None
    nb_changed_aug = 0
    nb_changed_aug_det = 0
    nb_iterations = 1000
    for i in sm.xrange(nb_iterations):
        observed_aug = aug.augment_images(images)
        observed_aug_det = aug_det.augment_images(images)
        if i == 0:
            last_aug = observed_aug
            last_aug_det = observed_aug_det
        else:
            if not np.array_equal(observed_aug, last_aug):
                nb_changed_aug += 1
            if not np.array_equal(observed_aug_det, last_aug_det):
                nb_changed_aug_det += 1
            last_aug = observed_aug
            last_aug_det = observed_aug_det
    assert nb_changed_aug >= int(nb_iterations * 0.7)
    assert nb_changed_aug_det == 0

    # values should change between pixels
    aug = iaa.AddElementwise(value=(-50, 50))

    nb_same = 0
    nb_different = 0
    nb_iterations = 1000
    for i in sm.xrange(nb_iterations):
        observed_aug = aug.augment_images(images)
        observed_aug_flat = observed_aug.flatten()
        last = None
        for j in sm.xrange(observed_aug_flat.size):
            if last is not None:
                v = observed_aug_flat[j]
                if v - 0.0001 <= last <= v + 0.0001:
                    nb_same += 1
                else:
                    nb_different += 1
            last = observed_aug_flat[j]
    assert nb_different > 0.9 * (nb_different + nb_same)

def test_Invert():
    reseed()

    zeros = np.zeros((4, 4, 3), dtype=np.uint8)
    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=2)], shape=zeros.shape)]

    observed = iaa.Invert(p=1.0).augment_image(zeros + 255)
    expected = zeros
    assert np.array_equal(observed, expected)

    observed = iaa.Invert(p=0.0).augment_image(zeros + 255)
    expected = zeros + 255
    assert np.array_equal(observed, expected)

    observed = iaa.Invert(p=1.0, max_value=200).augment_image(zeros + 200)
    expected = zeros
    assert np.array_equal(observed, expected)

    observed = iaa.Invert(p=1.0, max_value=200, min_value=100).augment_image(zeros + 200)
    expected = zeros + 100
    assert np.array_equal(observed, expected)

    observed = iaa.Invert(p=1.0, max_value=200, min_value=100).augment_image(zeros + 100)
    expected = zeros + 200
    assert np.array_equal(observed, expected)

    nb_iterations = 1000
    nb_inverted = 0
    for i in sm.xrange(nb_iterations):
        observed = iaa.Invert(p=0.5).augment_image(zeros + 256)
        if np.array_equal(observed, zeros):
            nb_inverted += 1
    pinv = nb_inverted / nb_iterations
    assert 0.4 <= pinv <= 0.6

    # keypoints shouldnt be changed
    aug = iaa.Invert(p=1.0)
    aug_det = iaa.Invert(p=1.0).to_deterministic()
    observed = aug.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    observed = aug_det.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

def test_ContrastNormalization():
    reseed()

    zeros = np.zeros((4, 4, 3), dtype=np.uint8)
    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=2)], shape=zeros.shape)]

    # contrast stays the same
    observed = iaa.ContrastNormalization(alpha=1.0).augment_image(zeros + 50)
    expected = zeros + 50
    assert np.array_equal(observed, expected)

    # image with mean intensity (ie 128), contrast cannot be changed
    observed = iaa.ContrastNormalization(alpha=2.0).augment_image(zeros + 128)
    expected = zeros + 128
    assert np.array_equal(observed, expected)

    # increase contrast
    observed = iaa.ContrastNormalization(alpha=2.0).augment_image(zeros + 128 + 10)
    expected = zeros + 128 + 20
    assert np.array_equal(observed, expected)

    observed = iaa.ContrastNormalization(alpha=2.0).augment_image(zeros + 128 - 10)
    expected = zeros + 128 - 20
    assert np.array_equal(observed, expected)

    # decrease contrast
    observed = iaa.ContrastNormalization(alpha=0.5).augment_image(zeros + 128 + 10)
    expected = zeros + 128 + 5
    assert np.array_equal(observed, expected)

    observed = iaa.ContrastNormalization(alpha=0.5).augment_image(zeros + 128 - 10)
    expected = zeros + 128 - 5
    assert np.array_equal(observed, expected)

    # increase contrast by stochastic parameter
    observed = iaa.ContrastNormalization(alpha=iap.Choice([2.0, 3.0])).augment_image(zeros + 128 + 10)
    expected1 = zeros + 128 + 20
    expected2 = zeros + 128 + 30
    assert np.array_equal(observed, expected1) or np.array_equal(observed, expected2)

    # change contrast by tuple
    nb_iterations = 1000
    nb_changed = 0
    last = None
    for i in sm.xrange(nb_iterations):
        observed = iaa.ContrastNormalization(alpha=(0.5, 2.0)).augment_image(zeros + 128 + 40)
        if last is None:
            last = observed
        else:
            if not np.array_equal(observed, last):
                nb_changed += 1
    p_changed = nb_changed / (nb_iterations-1)
    assert p_changed > 0.5

    # keypoints shouldnt be changed
    aug = iaa.ContrastNormalization(alpha=2.0)
    aug_det = iaa.ContrastNormalization(alpha=2.0).to_deterministic()
    observed = aug.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    observed = aug_det.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

def test_Affine():
    reseed()

    base_img = np.array([[0, 0, 0],
                         [0, 255, 0],
                         [0, 0, 0]], dtype=np.uint8)
    base_img = base_img[:, :, np.newaxis]

    images = np.array([base_img])
    images_list = [base_img]
    outer_pixels = ([], [])
    for i in sm.xrange(base_img.shape[0]):
        for j in sm.xrange(base_img.shape[1]):
            if i != j:
                outer_pixels[0].append(i)
                outer_pixels[1].append(j)

    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=2)], shape=base_img.shape)]

    # no translation/scale/rotate/shear, shouldnt change nothing
    aug = iaa.Affine(scale=1.0, translate_px=0, rotate=0, shear=0)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    expected = images
    assert np.array_equal(observed, expected)

    observed = aug_det.augment_images(images)
    expected = images
    assert np.array_equal(observed, expected)

    observed = aug.augment_images(images_list)
    expected = images_list
    assert array_equal_lists(observed, expected)

    observed = aug_det.augment_images(images_list)
    expected = images_list
    assert array_equal_lists(observed, expected)

    observed = aug.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    observed = aug_det.augment_keypoints(keypoints)
    expected = keypoints
    assert keypoints_equal(observed, expected)

    # ---------------------
    # scale
    # ---------------------
    # zoom in
    aug = iaa.Affine(scale=1.75, translate_px=0, rotate=0, shear=0)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    #exit()
    assert observed[0][1, 1] > 250
    assert (observed[0][outer_pixels[0], outer_pixels[1]] > 20).all()
    assert (observed[0][outer_pixels[0], outer_pixels[1]] < 150).all()

    observed = aug_det.augment_images(images)
    assert observed[0][1, 1] > 250
    assert (observed[0][outer_pixels[0], outer_pixels[1]] > 20).all()
    assert (observed[0][outer_pixels[0], outer_pixels[1]] < 150).all()

    observed = aug.augment_images(images_list)
    assert observed[0][1, 1] > 250
    assert (observed[0][outer_pixels[0], outer_pixels[1]] > 20).all()
    assert (observed[0][outer_pixels[0], outer_pixels[1]] < 150).all()

    observed = aug_det.augment_images(images_list)
    assert observed[0][1, 1] > 250
    assert (observed[0][outer_pixels[0], outer_pixels[1]] > 20).all()
    assert (observed[0][outer_pixels[0], outer_pixels[1]] < 150).all()

    observed = aug.augment_keypoints(keypoints)
    assert observed[0].keypoints[0].x < 0
    assert observed[0].keypoints[0].y < 0
    assert observed[0].keypoints[1].x == 1
    assert observed[0].keypoints[1].y == 1
    assert observed[0].keypoints[2].x > 2
    assert observed[0].keypoints[2].y > 2

    observed = aug_det.augment_keypoints(keypoints)
    assert observed[0].keypoints[0].x < 0
    assert observed[0].keypoints[0].y < 0
    assert observed[0].keypoints[1].x == 1
    assert observed[0].keypoints[1].y == 1
    assert observed[0].keypoints[2].x > 2
    assert observed[0].keypoints[2].y > 2

    # zoom in only on x axis
    aug = iaa.Affine(scale={"x": 1.75, "y": 1.0}, translate_px=0, rotate=0, shear=0)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    assert observed[0][1, 1] > 250
    assert (observed[0][[1, 1], [0, 2]] > 20).all()
    assert (observed[0][[1, 1], [0, 2]] < 150).all()
    assert (observed[0][0, :] < 5).all()
    assert (observed[0][2, :] < 5).all()

    observed = aug_det.augment_images(images)
    assert observed[0][1, 1] > 250
    assert (observed[0][[1, 1], [0, 2]] > 20).all()
    assert (observed[0][[1, 1], [0, 2]] < 150).all()
    assert (observed[0][0, :] < 5).all()
    assert (observed[0][2, :] < 5).all()

    observed = aug.augment_images(images_list)
    assert observed[0][1, 1] > 250
    assert (observed[0][[1, 1], [0, 2]] > 20).all()
    assert (observed[0][[1, 1], [0, 2]] < 150).all()
    assert (observed[0][0, :] < 5).all()
    assert (observed[0][2, :] < 5).all()

    observed = aug_det.augment_images(images_list)
    assert observed[0][1, 1] > 250
    assert (observed[0][[1, 1], [0, 2]] > 20).all()
    assert (observed[0][[1, 1], [0, 2]] < 150).all()
    assert (observed[0][0, :] < 5).all()
    assert (observed[0][2, :] < 5).all()

    observed = aug.augment_keypoints(keypoints)
    assert observed[0].keypoints[0].x < 0
    assert observed[0].keypoints[0].y == 0
    assert observed[0].keypoints[1].x == 1
    assert observed[0].keypoints[1].y == 1
    assert observed[0].keypoints[2].x > 2
    assert observed[0].keypoints[2].y == 2

    observed = aug_det.augment_keypoints(keypoints)
    assert observed[0].keypoints[0].x < 0
    assert observed[0].keypoints[0].y == 0
    assert observed[0].keypoints[1].x == 1
    assert observed[0].keypoints[1].y == 1
    assert observed[0].keypoints[2].x > 2
    assert observed[0].keypoints[2].y == 2

    # zoom in only on y axis
    aug = iaa.Affine(scale={"x": 1.0, "y": 1.75}, translate_px=0, rotate=0, shear=0)
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    assert observed[0][1, 1] > 250
    assert (observed[0][[0, 2], [1, 1]] > 20).all()
    assert (observed[0][[0, 2], [1, 1]] < 150).all()
    assert (observed[0][:, 0] < 5).all()
    assert (observed[0][:, 2] < 5).all()

    observed = aug_det.augment_images(images)
    assert observed[0][1, 1] > 250
    assert (observed[0][[0, 2], [1, 1]] > 20).all()
    assert (observed[0][[0, 2], [1, 1]] < 150).all()
    assert (observed[0][:, 0] < 5).all()
    assert (observed[0][:, 2] < 5).all()

    observed = aug.augment_images(images_list)
    assert observed[0][1, 1] > 250
    assert (observed[0][[0, 2], [1, 1]] > 20).all()
    assert (observed[0][[0, 2], [1, 1]] < 150).all()
    assert (observed[0][:, 0] < 5).all()
    assert (observed[0][:, 2] < 5).all()

    observed = aug_det.augment_images(images_list)
    assert observed[0][1, 1] > 250
    assert (observed[0][[0, 2], [1, 1]] > 20).all()
    assert (observed[0][[0, 2], [1, 1]] < 150).all()
    assert (observed[0][:, 0] < 5).all()
    assert (observed[0][:, 2] < 5).all()

    observed = aug.augment_keypoints(keypoints)
    assert observed[0].keypoints[0].x == 0
    assert observed[0].keypoints[0].y < 0
    assert observed[0].keypoints[1].x == 1
    assert observed[0].keypoints[1].y == 1
    assert observed[0].keypoints[2].x == 2
    assert observed[0].keypoints[2].y > 2

    observed = aug_det.augment_keypoints(keypoints)
    assert observed[0].keypoints[0].x == 0
    assert observed[0].keypoints[0].y < 0
    assert observed[0].keypoints[1].x == 1
    assert observed[0].keypoints[1].y == 1
    assert observed[0].keypoints[2].x == 2
    assert observed[0].keypoints[2].y > 2

    # zoom out
    # this one uses a 4x4 area of all 255, which is zoomed out to a 4x4 area
    # in which the center 2x2 area is 255
    # zoom in should probably be adapted to this style
    # no separate tests here for x/y axis, should work fine if zoom in works with that
    aug = iaa.Affine(scale=0.49, translate_px=0, rotate=0, shear=0)
    aug_det = aug.to_deterministic()

    image = np.ones((4, 4, 1), dtype=np.uint8) * 255
    images = np.array([image])
    images_list = [image]
    outer_pixels = ([], [])
    for y in sm.xrange(4):
        xs = sm.xrange(4) if y in [0, 3] else [0, 3]
        for x in xs:
            outer_pixels[0].append(y)
            outer_pixels[1].append(x)
    inner_pixels = ([1, 1, 2, 2], [1, 2, 1, 2])
    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0), ia.Keypoint(x=3, y=0),
                                      ia.Keypoint(x=0, y=3), ia.Keypoint(x=3, y=3)],
                                     shape=image.shape)]
    keypoints_aug = [ia.KeypointsOnImage([ia.Keypoint(x=0.765, y=0.765), ia.Keypoint(x=2.235, y=0.765),
                                          ia.Keypoint(x=0.765, y=2.235), ia.Keypoint(x=2.235, y=2.235)],
                                         shape=image.shape)]

    observed = aug.augment_images(images)
    assert (observed[0][outer_pixels] < 25).all()
    assert (observed[0][inner_pixels] > 200).all()

    observed = aug_det.augment_images(images)
    assert (observed[0][outer_pixels] < 25).all()
    assert (observed[0][inner_pixels] > 200).all()

    observed = aug.augment_images(images_list)
    assert (observed[0][outer_pixels] < 25).all()
    assert (observed[0][inner_pixels] > 200).all()

    observed = aug_det.augment_images(images_list)
    assert (observed[0][outer_pixels] < 25).all()
    assert (observed[0][inner_pixels] > 200).all()

    observed = aug.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints_aug)

    observed = aug_det.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints_aug)

    # varying scales
    aug = iaa.Affine(scale={"x": (0.5, 1.5), "y": (0.5, 1.5)}, translate_px=0,
                     rotate=0, shear=0)
    aug_det = aug.to_deterministic()

    image = np.array([[0, 0, 0, 0, 0],
                      [0, 1, 1, 1, 0],
                      [0, 1, 2, 1, 0],
                      [0, 1, 1, 1, 0],
                      [0, 0, 0, 0, 0]], dtype=np.uint8) * 100
    image = image[:, :, np.newaxis]
    images_list = [image]
    images = np.array([image])

    last_aug = None
    last_aug_det = None
    nb_changed_aug = 0
    nb_changed_aug_det = 0
    nb_iterations = 1000
    for i in sm.xrange(nb_iterations):
        observed_aug = aug.augment_images(images)
        observed_aug_det = aug_det.augment_images(images)
        if i == 0:
            last_aug = observed_aug
            last_aug_det = observed_aug_det
        else:
            if not np.array_equal(observed_aug, last_aug):
                nb_changed_aug += 1
            if not np.array_equal(observed_aug_det, last_aug_det):
                nb_changed_aug_det += 1
            last_aug = observed_aug
            last_aug_det = observed_aug_det
    assert nb_changed_aug >= int(nb_iterations * 0.8)
    assert nb_changed_aug_det == 0

    # ---------------------
    # translate
    # ---------------------
    # move one pixel to the right
    aug = iaa.Affine(scale=1.0, translate_px={"x": 1, "y": 0}, rotate=0, shear=0)
    aug_det = aug.to_deterministic()

    image = np.zeros((3, 3, 1), dtype=np.uint8)
    image_aug = np.copy(image)
    image[1, 1] = 255
    image_aug[1, 2] = 255
    images = np.array([image])
    images_aug = np.array([image_aug])
    images_list = [image]
    images_aug_list = [image_aug]
    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=1, y=1)], shape=base_img.shape)]
    keypoints_aug = [ia.KeypointsOnImage([ia.Keypoint(x=2, y=1)], shape=base_img.shape)]

    observed = aug.augment_images(images)
    assert np.array_equal(observed, images_aug)

    observed = aug_det.augment_images(images)
    assert np.array_equal(observed, images_aug)

    observed = aug.augment_images(images_list)
    assert array_equal_lists(observed, images_aug_list)

    observed = aug_det.augment_images(images_list)
    assert array_equal_lists(observed, images_aug_list)

    observed = aug.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints_aug)

    observed = aug_det.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints_aug)

    # move one pixel to the bottom
    aug = iaa.Affine(scale=1.0, translate_px={"x": 0, "y": 1}, rotate=0, shear=0)
    aug_det = aug.to_deterministic()

    image = np.zeros((3, 3, 1), dtype=np.uint8)
    image_aug = np.copy(image)
    image[1, 1] = 255
    image_aug[2, 1] = 255
    images = np.array([image])
    images_aug = np.array([image_aug])
    images_list = [image]
    images_aug_list = [image_aug]
    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=1, y=1)], shape=base_img.shape)]
    keypoints_aug = [ia.KeypointsOnImage([ia.Keypoint(x=1, y=2)], shape=base_img.shape)]

    observed = aug.augment_images(images)
    assert np.array_equal(observed, images_aug)

    observed = aug_det.augment_images(images)
    assert np.array_equal(observed, images_aug)

    observed = aug.augment_images(images_list)
    assert array_equal_lists(observed, images_aug_list)

    observed = aug_det.augment_images(images_list)
    assert array_equal_lists(observed, images_aug_list)

    observed = aug.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints_aug)

    observed = aug_det.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints_aug)

    # move 33% (one pixel) to the right
    aug = iaa.Affine(scale=1.0, translate_percent={"x": 0.3333, "y": 0}, rotate=0, shear=0)
    aug_det = aug.to_deterministic()

    image = np.zeros((3, 3, 1), dtype=np.uint8)
    image_aug = np.copy(image)
    image[1, 1] = 255
    image_aug[1, 2] = 255
    images = np.array([image])
    images_aug = np.array([image_aug])
    images_list = [image]
    images_aug_list = [image_aug]
    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=1, y=1)], shape=base_img.shape)]
    keypoints_aug = [ia.KeypointsOnImage([ia.Keypoint(x=2, y=1)], shape=base_img.shape)]

    observed = aug.augment_images(images)
    assert np.array_equal(observed, images_aug)

    observed = aug_det.augment_images(images)
    assert np.array_equal(observed, images_aug)

    observed = aug.augment_images(images_list)
    assert array_equal_lists(observed, images_aug_list)

    observed = aug_det.augment_images(images_list)
    assert array_equal_lists(observed, images_aug_list)

    observed = aug.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints_aug)

    observed = aug_det.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints_aug)

    # move 33% (one pixel) to the bottom
    aug = iaa.Affine(scale=1.0, translate_percent={"x": 0, "y": 0.3333}, rotate=0, shear=0)
    aug_det = aug.to_deterministic()

    image = np.zeros((3, 3, 1), dtype=np.uint8)
    image_aug = np.copy(image)
    image[1, 1] = 255
    image_aug[2, 1] = 255
    images = np.array([image])
    images_aug = np.array([image_aug])
    images_list = [image]
    images_aug_list = [image_aug]
    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=1, y=1)], shape=base_img.shape)]
    keypoints_aug = [ia.KeypointsOnImage([ia.Keypoint(x=1, y=2)], shape=base_img.shape)]

    observed = aug.augment_images(images)
    assert np.array_equal(observed, images_aug)

    observed = aug_det.augment_images(images)
    assert np.array_equal(observed, images_aug)

    observed = aug.augment_images(images_list)
    assert array_equal_lists(observed, images_aug_list)

    observed = aug_det.augment_images(images_list)
    assert array_equal_lists(observed, images_aug_list)

    observed = aug.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints_aug)

    observed = aug_det.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints_aug)

    # 0-1px to left/right and 0-1px to top/bottom
    aug = iaa.Affine(scale=1.0, translate_px={"x": (-1, 1), "y": (-1, 1)}, rotate=0, shear=0)
    aug_det = aug.to_deterministic()
    last_aug = None
    last_aug_det = None
    nb_changed_aug = 0
    nb_changed_aug_det = 0
    nb_iterations = 1000
    centers_aug = np.copy(image).astype(np.int32) * 0
    centers_aug_det = np.copy(image).astype(np.int32) * 0
    for i in sm.xrange(nb_iterations):
        observed_aug = aug.augment_images(images)
        observed_aug_det = aug_det.augment_images(images)
        if i == 0:
            last_aug = observed_aug
            last_aug_det = observed_aug_det
        else:
            if not np.array_equal(observed_aug, last_aug):
                nb_changed_aug += 1
            if not np.array_equal(observed_aug_det, last_aug_det):
                nb_changed_aug_det += 1
            last_aug = observed_aug
            last_aug_det = observed_aug_det

        assert len(observed_aug[0].nonzero()[0]) == 1
        assert len(observed_aug_det[0].nonzero()[0]) == 1
        centers_aug += (observed_aug[0] > 0)
        centers_aug_det += (observed_aug_det[0] > 0)

    assert nb_changed_aug >= int(nb_iterations * 0.7)
    assert nb_changed_aug_det == 0
    assert (centers_aug > int(nb_iterations * (1/9 * 0.6))).all()
    assert (centers_aug < int(nb_iterations * (1/9 * 1.4))).all()

    # ---------------------
    # rotate
    # ---------------------
    # rotate by 45 degrees
    aug = iaa.Affine(scale=1.0, translate_px=0, rotate=90, shear=0)
    aug_det = aug.to_deterministic()

    image = np.zeros((3, 3, 1), dtype=np.uint8)
    image_aug = np.copy(image)
    image[1, :] = 255
    image_aug[0, 1] = 255
    image_aug[1, 1] = 255
    image_aug[2, 1] = 255
    images = np.array([image])
    images_aug = np.array([image_aug])
    images_list = [image]
    images_aug_list = [image_aug]
    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=1), ia.Keypoint(x=1, y=1),
                                      ia.Keypoint(x=2, y=1)], shape=base_img.shape)]
    keypoints_aug = [ia.KeypointsOnImage([ia.Keypoint(x=1, y=0), ia.Keypoint(x=1, y=1),
                                          ia.Keypoint(x=1, y=2)], shape=base_img.shape)]

    observed = aug.augment_images(images)
    observed[observed >= 100] = 255
    observed[observed < 100] = 0
    assert np.array_equal(observed, images_aug)

    observed = aug_det.augment_images(images)
    observed[observed >= 100] = 255
    observed[observed < 100] = 0
    assert np.array_equal(observed, images_aug)

    observed = aug.augment_images(images_list)
    observed[0][observed[0] >= 100] = 255
    observed[0][observed[0] < 100] = 0
    assert array_equal_lists(observed, images_aug_list)

    observed = aug_det.augment_images(images_list)
    observed[0][observed[0] >= 100] = 255
    observed[0][observed[0] < 100] = 0
    assert array_equal_lists(observed, images_aug_list)

    observed = aug.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints_aug)

    observed = aug_det.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints_aug)

    # random rotation 0-364 degrees
    aug = iaa.Affine(scale=1.0, translate_px=0, rotate=(0, 364), shear=0)
    aug_det = aug.to_deterministic()
    last_aug = None
    last_aug_det = None
    nb_changed_aug = 0
    nb_changed_aug_det = 0
    nb_iterations = 1000
    pixels_sums_aug = np.copy(image).astype(np.int32) * 0
    pixels_sums_aug_det = np.copy(image).astype(np.int32) * 0
    for i in sm.xrange(nb_iterations):
        observed_aug = aug.augment_images(images)
        observed_aug_det = aug_det.augment_images(images)
        if i == 0:
            last_aug = observed_aug
            last_aug_det = observed_aug_det
        else:
            if not np.array_equal(observed_aug, last_aug):
                nb_changed_aug += 1
            if not np.array_equal(observed_aug_det, last_aug_det):
                nb_changed_aug_det += 1
            last_aug = observed_aug
            last_aug_det = observed_aug_det

        #assert len(observed_aug[0].nonzero()[0]) == 1
        #assert len(observed_aug_det[0].nonzero()[0]) == 1
        pixels_sums_aug += (observed_aug[0] > 100)
        pixels_sums_aug_det += (observed_aug_det[0] > 100)

    assert nb_changed_aug >= int(nb_iterations * 0.9)
    assert nb_changed_aug_det == 0
    # center pixel, should always be white when rotating line around center
    assert pixels_sums_aug[1, 1] > (nb_iterations * 0.98)
    assert pixels_sums_aug[1, 1] < (nb_iterations * 1.02)

    # outer pixels, should sometimes be white
    # the values here had to be set quite tolerant, the middle pixels at top/left/bottom/right get more activation than expected
    outer_pixels = ([0, 0, 0, 1, 1, 2, 2, 2], [0, 1, 2, 0, 2, 0, 1, 2])
    assert (pixels_sums_aug[outer_pixels] > int(nb_iterations * (2/8 * 0.4))).all()
    assert (pixels_sums_aug[outer_pixels] < int(nb_iterations * (2/8 * 2.0))).all()

    # ---------------------
    # shear
    # ---------------------
    # TODO
    #print("[Note] There is currently no test for shear in test_Affine().")

    # ---------------------
    # cval
    # ---------------------
    aug = iaa.Affine(scale=1.0, translate_px=100, rotate=0, shear=0, cval=128)
    aug_det = aug.to_deterministic()

    image = np.ones((3, 3, 1), dtype=np.uint8) * 255
    image_aug = np.copy(image)
    images = np.array([image])
    images_list = [image]

    observed = aug.augment_images(images)
    assert (observed[0] > 128 - 30).all()
    assert (observed[0] < 128 + 30).all()

    observed = aug_det.augment_images(images)
    assert (observed[0] > 128 - 30).all()
    assert (observed[0] < 128 + 30).all()

    observed = aug.augment_images(images_list)
    assert (observed[0] > 128 - 30).all()
    assert (observed[0] < 128 + 30).all()

    observed = aug_det.augment_images(images_list)
    assert (observed[0] > 128 - 30).all()
    assert (observed[0] < 128 + 30).all()

    # random cvals
    aug = iaa.Affine(scale=1.0, translate_px=100, rotate=0, shear=0, cval=(0, 255))
    aug_det = aug.to_deterministic()
    last_aug = None
    last_aug_det = None
    nb_changed_aug = 0
    nb_changed_aug_det = 0
    nb_iterations = 1000
    averages = []
    for i in sm.xrange(nb_iterations):
        observed_aug = aug.augment_images(images)
        observed_aug_det = aug_det.augment_images(images)
        if i == 0:
            last_aug = observed_aug
            last_aug_det = observed_aug_det
        else:
            if not np.array_equal(observed_aug, last_aug):
                nb_changed_aug += 1
            if not np.array_equal(observed_aug_det, last_aug_det):
                nb_changed_aug_det += 1
            last_aug = observed_aug
            last_aug_det = observed_aug_det

        averages.append(int(np.average(observed_aug)))

    assert nb_changed_aug >= int(nb_iterations * 0.9)
    assert nb_changed_aug_det == 0
    # center pixel, should always be white when rotating line around center
    assert pixels_sums_aug[1, 1] > (nb_iterations * 0.98)
    assert pixels_sums_aug[1, 1] < (nb_iterations * 1.02)
    assert len(set(averages)) > 200

    # ---------------------
    # order
    # ---------------------
    # TODO
    #print("[Note] There is currently no test for (interpolation) order in test_Affine().")


def test_Sequential():
    reseed()

    image = np.array([[0, 1, 1],
                      [0, 0, 1],
                      [0, 0, 1]], dtype=np.uint8) * 255
    image = image[:, :, np.newaxis]
    images_list = [image]
    images = np.array([image])

    image_lr = np.array([[1, 1, 0],
                         [1, 0, 0],
                         [1, 0, 0]], dtype=np.uint8) * 255
    image_lr = image_lr[:, :, np.newaxis]
    images_lr = np.array([image_lr])

    image_ud = np.array([[0, 0, 1],
                         [0, 0, 1],
                         [0, 1, 1]], dtype=np.uint8) * 255
    image_ud = image_ud[:, :, np.newaxis]
    images_ud = np.array([image_ud])

    image_lr_ud = np.array([[1, 0, 0],
                            [1, 0, 0],
                            [1, 1, 0]], dtype=np.uint8) * 255
    image_lr_ud = image_lr_ud[:, :, np.newaxis]
    images_lr_ud_list = [image_lr_ud]
    images_lr_ud = np.array([image_lr_ud])

    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=1, y=0), ia.Keypoint(x=2, y=0),
                                      ia.Keypoint(x=2, y=1)], shape=image.shape)]
    keypoints_aug = [ia.KeypointsOnImage([ia.Keypoint(x=1, y=2), ia.Keypoint(x=0, y=2),
                                          ia.Keypoint(x=0, y=1)], shape=image.shape)]

    aug = iaa.Sequential([
        iaa.Fliplr(1.0),
        iaa.Flipud(1.0)
    ])
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    assert np.array_equal(observed, images_lr_ud)

    observed = aug_det.augment_images(images)
    assert np.array_equal(observed, images_lr_ud)

    observed = aug.augment_images(images_list)
    assert array_equal_lists(observed, images_lr_ud_list)

    observed = aug_det.augment_images(images_list)
    assert array_equal_lists(observed, images_lr_ud_list)

    observed = aug.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints_aug)

    observed = aug_det.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints_aug)

    # 50% horizontal flip, 50% vertical flip
    aug = iaa.Sequential([
        iaa.Fliplr(0.5),
        iaa.Flipud(0.5)
    ])
    aug_det = aug.to_deterministic()
    last_aug = None
    last_aug_det = None
    nb_changed_aug = 0
    nb_changed_aug_det = 0
    nb_iterations = 200
    for i in sm.xrange(nb_iterations):
        observed_aug = aug.augment_images(images)
        observed_aug_det = aug_det.augment_images(images)
        if i == 0:
            last_aug = observed_aug
            last_aug_det = observed_aug_det
        else:
            if not np.array_equal(observed_aug, last_aug):
                nb_changed_aug += 1
            if not np.array_equal(observed_aug_det, last_aug_det):
                nb_changed_aug_det += 1
            last_aug = observed_aug
            last_aug_det = observed_aug_det

        assert np.array_equal(observed_aug, images) \
               or np.array_equal(observed_aug, images_lr) \
               or np.array_equal(observed_aug, images_ud) \
               or np.array_equal(observed_aug, images_lr_ud)
        assert np.array_equal(observed_aug_det, images) \
               or np.array_equal(observed_aug_det, images_lr) \
               or np.array_equal(observed_aug_det, images_ud) \
               or np.array_equal(observed_aug_det, images_lr_ud)

    assert (0.25 - 0.10) <= (1 - (nb_changed_aug / nb_iterations)) <= (0.25 + 0.10) # should be the same in roughly 25% of all cases
    assert nb_changed_aug_det == 0

    # random order
    image = np.array([[0, 1, 1],
                      [0, 0, 1],
                      [0, 0, 1]], dtype=np.uint8)
    image = image[:, :, np.newaxis]
    images = np.array([image])

    images_first_second = (images + 10) * 10
    images_second_first = (images * 10) + 10

    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=0, y=0)], shape=image.shape)]
    keypoints_first_second = [ia.KeypointsOnImage([ia.Keypoint(x=1, y=1)], shape=image.shape)]
    keypoints_second_first = [ia.KeypointsOnImage([ia.Keypoint(x=1, y=0)], shape=image.shape)]

    def images_first(images, random_state, parents, hooks):
        return images + 10

    def images_second(images, random_state, parents, hooks):
        return images * 10

    def keypoints_first(keypoints_on_images, random_state, parents, hooks):
        for keypoints_on_image in keypoints_on_images:
            for keypoint in keypoints_on_image.keypoints:
                keypoint.x = keypoint.x + 1
        return keypoints_on_images

    def keypoints_second(keypoints_on_images, random_state, parents, hooks):
        for keypoints_on_image in keypoints_on_images:
            for keypoint in keypoints_on_image.keypoints:
                keypoint.y = keypoint.y + keypoint.x
        return keypoints_on_images

    aug_unrandom = iaa.Sequential([
        iaa.Lambda(images_first, keypoints_first),
        iaa.Lambda(images_second, keypoints_second)
    ], random_order=False)
    aug_unrandom_det = aug.to_deterministic()
    aug_random = iaa.Sequential([
        iaa.Lambda(images_first, keypoints_first),
        iaa.Lambda(images_second, keypoints_second)
    ], random_order=True)
    aug_random_det = aug.to_deterministic()

    last_aug = None
    last_aug_det = None
    nb_changed_aug = 0
    nb_changed_aug_det = 0
    nb_iterations = 200

    nb_images_first_second_unrandom = 0
    nb_images_second_first_unrandom = 0
    nb_images_first_second_random = 0
    nb_images_second_first_random = 0
    nb_keypoints_first_second_unrandom = 0
    nb_keypoints_second_first_unrandom = 0
    nb_keypoints_first_second_random = 0
    nb_keypoints_second_first_random = 0

    for i in sm.xrange(nb_iterations):
        observed_aug_unrandom = aug_unrandom.augment_images(images)
        observed_aug_unrandom_det = aug_unrandom_det.augment_images(images)
        observed_aug_random = aug_random.augment_images(images)
        observed_aug_random_det = aug_random_det.augment_images(images)

        keypoints_aug_unrandom = aug_unrandom.augment_keypoints(keypoints)
        keypoints_aug_unrandom_det = aug_unrandom_det.augment_keypoints(keypoints)
        keypoints_aug_random = aug_random.augment_keypoints(keypoints)
        keypoints_aug_random_det = aug_random_det.augment_keypoints(keypoints)

        if i == 0:
            last_aug = observed_aug
            last_aug_det = observed_aug_det
        else:
            if not np.array_equal(observed_aug, last_aug):
                nb_changed_aug += 1
            if not np.array_equal(observed_aug_det, last_aug_det):
                nb_changed_aug_det += 1
            last_aug = observed_aug
            last_aug_det = observed_aug_det

        if np.array_equal(observed_aug_unrandom, images_first_second):
            nb_images_first_second_unrandom += 1
        elif np.array_equal(observed_aug_unrandom, images_second_first):
            nb_images_second_first_unrandom += 1
        else:
            raise Exception("Received output doesnt match any expected output.")

        if np.array_equal(observed_aug_random, images_first_second):
            nb_images_first_second_random += 1
        elif np.array_equal(observed_aug_random, images_second_first):
            nb_images_second_first_random += 1
        else:
            raise Exception("Received output doesnt match any expected output.")

        if keypoints_equal(keypoints_aug_unrandom, keypoints_first_second):
            nb_keypoints_first_second_unrandom += 1
        elif keypoints_equal(keypoints_aug_unrandom, keypoints_second_first):
            nb_keypoints_second_first_unrandom += 1
        else:
            raise Exception("Received output doesnt match any expected output.")

        if keypoints_equal(keypoints_aug_random, keypoints_first_second):
            nb_keypoints_first_second_random += 1
        elif keypoints_equal(keypoints_aug_random, keypoints_second_first):
            nb_keypoints_second_first_random += 1
        else:
            raise Exception("Received output doesnt match any expected output.")

    assert nb_changed_aug == 0
    assert nb_changed_aug_det == 0
    assert nb_images_first_second_unrandom == nb_iterations
    assert nb_images_second_first_unrandom == 0
    assert nb_keypoints_first_second_unrandom == nb_iterations
    assert nb_keypoints_second_first_unrandom == 0
    assert (0.50 - 0.1) <= nb_images_first_second_random / nb_iterations <= (0.50 + 0.1)
    assert (0.50 - 0.1) <= nb_images_second_first_random / nb_iterations <= (0.50 + 0.1)
    assert (0.50 - 0.1) <= nb_keypoints_first_second_random / nb_iterations <= (0.50 + 0.1)
    assert (0.50 - 0.1) <= nb_keypoints_second_first_random / nb_iterations <= (0.50 + 0.1)


def test_SomeOf():
    reseed()

    zeros = np.zeros((3, 3, 1), dtype=np.uint8)

    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=1, y=0), ia.Keypoint(x=2, y=0),
                                      ia.Keypoint(x=2, y=1)], shape=zeros.shape)]

    # no child augmenters
    observed = iaa.SomeOf(n=0, children=[]).augment_image(zeros)
    assert np.array_equal(observed, zeros)

    observed = iaa.SomeOf(n=0).augment_image(zeros)
    assert np.array_equal(observed, zeros)

    # up to three child augmenters
    augs = [iaa.Add(1), iaa.Add(2), iaa.Add(3)]

    observed = iaa.SomeOf(n=0, children=augs).augment_image(zeros)
    assert np.array_equal(observed, zeros)

    observed = iaa.SomeOf(n=1, children=augs).augment_image(zeros)
    assert np.sum(observed) in [9*1, 9*2, 9*3]

    observed = iaa.SomeOf(n=2, children=augs).augment_image(zeros)
    assert np.sum(observed) in [9*1+9*2, 9*1+9*3, 9*2+9*3]

    observed = iaa.SomeOf(n=3, children=augs).augment_image(zeros)
    assert np.sum(observed) in [9*1+9*2+9*3]

    observed = iaa.SomeOf(n=4, children=augs).augment_image(zeros)
    assert np.sum(observed) in [9*1+9*2+9*3]

    # n as tuple
    augs = [iaa.Add(1), iaa.Add(2), iaa.Add(4)]
    nb_iterations = 1000
    nb_observed = [0, 0, 0, 0]
    for i in sm.xrange(nb_iterations):
        observed = iaa.SomeOf(n=(0, 3), children=augs).augment_image(zeros)
        s = observed[0, 0, 0]
        if s == 0:
            nb_observed[0] += 1
        if s & 1 > 0:
            nb_observed[1] += 1
        if s & 2 > 0:
            nb_observed[2] += 1
        if s & 4 > 0:
            nb_observed[3] += 1
    p_observed = [n/nb_iterations for n in nb_observed]
    assert 0.25-0.1 <= p_observed[0] <= 0.25+0.1
    assert 0.5-0.1 <= p_observed[1] <= 0.5+0.1
    assert 0.5-0.1 <= p_observed[2] <= 0.5+0.1
    assert 0.5-0.1 <= p_observed[3] <= 0.5+0.1

    # in-order vs random order
    augs = [iaa.Multiply(2.0), iaa.Add(100)]
    observed = iaa.SomeOf(n=2, children=augs, random_order=False).augment_image(zeros)
    assert np.sum(observed) == 9*100

    nb_iterations = 1000
    nb_observed = [0, 0]
    for i in sm.xrange(nb_iterations):
        augs = [iaa.Multiply(2.0), iaa.Add(100)]
        observed = iaa.SomeOf(n=2, children=augs, random_order=True).augment_image(zeros)
        s = np.sum(observed)
        if s == 9*100:
            nb_observed[0] += 1
        elif s == 9*200:
            nb_observed[1] += 1
        else:
            raise Exception("Unexpected sum: %.8f (@2)" % (s,))
    p_observed = [n/nb_iterations for n in nb_observed]
    assert 0.5-0.1 <= p_observed[0] <= 0.5+0.1
    assert 0.5-0.1 <= p_observed[1] <= 0.5+0.1

def test_OneOf():
    reseed()

    zeros = np.zeros((3, 3, 1), dtype=np.uint8)

    # one child augmenter
    observed = iaa.OneOf(children=iaa.Add(1)).augment_image(zeros)
    assert np.array_equal(observed, zeros + 1)
    observed = iaa.OneOf(children=iaa.Sequential([iaa.Add(1)])).augment_image(zeros)
    assert np.array_equal(observed, zeros + 1)
    observed = iaa.OneOf(children=[iaa.Add(1)]).augment_image(zeros)
    assert np.array_equal(observed, zeros + 1)

    # up to three child augmenters
    augs = [iaa.Add(1), iaa.Add(2), iaa.Add(3)]
    aug = iaa.OneOf(augs)

    results = {9*1: 0, 9*2: 0, 9*3: 0}
    nb_iterations = 1000
    for _ in sm.xrange(nb_iterations):
        result = aug.augment_image(zeros)
        s = np.sum(result)
        results[s] += 1
    expected = int(nb_iterations / len(augs))
    expected_tolerance = int(nb_iterations * 0.05)
    for key, val in results.items():
        assert expected - expected_tolerance < val < expected + expected_tolerance

def test_Sometimes():
    reseed()

    image = np.array([[0, 1, 1],
                      [0, 0, 1],
                      [0, 0, 1]], dtype=np.uint8) * 255
    image = image[:, :, np.newaxis]
    images_list = [image]
    images = np.array([image])

    image_lr = np.array([[1, 1, 0],
                         [1, 0, 0],
                         [1, 0, 0]], dtype=np.uint8) * 255
    image_lr = image_lr[:, :, np.newaxis]
    images_lr_list = [image_lr]
    images_lr = np.array([image_lr])

    image_ud = np.array([[0, 0, 1],
                         [0, 0, 1],
                         [0, 1, 1]], dtype=np.uint8) * 255
    image_ud = image_ud[:, :, np.newaxis]
    images_ud_list = [image_ud]
    images_ud = np.array([image_ud])

    keypoints = [ia.KeypointsOnImage([ia.Keypoint(x=1, y=0), ia.Keypoint(x=2, y=0),
                                      ia.Keypoint(x=2, y=1)], shape=image.shape)]
    keypoints_lr = [ia.KeypointsOnImage([ia.Keypoint(x=1, y=0), ia.Keypoint(x=0, y=0),
                                         ia.Keypoint(x=0, y=1)], shape=image.shape)]
    keypoints_ud = [ia.KeypointsOnImage([ia.Keypoint(x=1, y=2), ia.Keypoint(x=2, y=2),
                                         ia.Keypoint(x=2, y=1)], shape=image.shape)]

    # 100% chance of if-branch
    aug = iaa.Sometimes(1.0, [iaa.Fliplr(1.0)], [iaa.Flipud(1.0)])
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    assert np.array_equal(observed, images_lr)

    observed = aug_det.augment_images(images)
    assert np.array_equal(observed, images_lr)

    observed = aug.augment_images(images_list)
    assert array_equal_lists(observed, images_lr_list)

    observed = aug_det.augment_images(images_list)
    assert array_equal_lists(observed, images_lr_list)

    observed = aug.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints_lr)

    observed = aug_det.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints_lr)

    # 100% chance of else-branch
    aug = iaa.Sometimes(0.0, [iaa.Fliplr(1.0)], [iaa.Flipud(1.0)])
    aug_det = aug.to_deterministic()

    observed = aug.augment_images(images)
    assert np.array_equal(observed, images_ud)

    observed = aug_det.augment_images(images)
    assert np.array_equal(observed, images_ud)

    observed = aug.augment_images(images_list)
    assert array_equal_lists(observed, images_ud_list)

    observed = aug_det.augment_images(images_list)
    assert array_equal_lists(observed, images_ud_list)

    observed = aug.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints_ud)

    observed = aug_det.augment_keypoints(keypoints)
    assert keypoints_equal(observed, keypoints_ud)

    # 50% if branch, 50% else branch
    aug = iaa.Sometimes(0.5, [iaa.Fliplr(1.0)], [iaa.Flipud(1.0)])
    aug_det = aug.to_deterministic()
    last_aug = None
    last_aug_det = None
    nb_changed_aug = 0
    nb_changed_aug_det = 0
    nb_iterations = 1000
    nb_images_if_branch = 0
    nb_images_else_branch = 0
    nb_keypoints_if_branch = 0
    nb_keypoints_else_branch = 0
    for i in sm.xrange(nb_iterations):
        observed_aug = aug.augment_images(images)
        observed_aug_det = aug_det.augment_images(images)
        keypoints_aug = aug.augment_keypoints(keypoints)
        keypoints_aug_det = aug.augment_keypoints(keypoints)
        if i == 0:
            last_aug = observed_aug
            last_aug_det = observed_aug_det
        else:
            if not np.array_equal(observed_aug, last_aug):
                nb_changed_aug += 1
            if not np.array_equal(observed_aug_det, last_aug_det):
                nb_changed_aug_det += 1
            last_aug = observed_aug
            last_aug_det = observed_aug_det

        if np.array_equal(observed_aug, images_lr):
            nb_images_if_branch += 1
        elif np.array_equal(observed_aug, images_ud):
            nb_images_else_branch += 1
        else:
            raise Exception("Received output doesnt match any expected output.")

        if keypoints_equal(keypoints_aug, keypoints_lr):
            nb_keypoints_if_branch += 1
        elif keypoints_equal(keypoints_aug, keypoints_ud):
            nb_keypoints_else_branch += 1
        else:
            raise Exception("Received output doesnt match any expected output.")

    assert (0.50 - 0.10) <= nb_images_if_branch / nb_iterations <= (0.50 + 0.10)
    assert (0.50 - 0.10) <= nb_images_else_branch / nb_iterations <= (0.50 + 0.10)
    assert (0.50 - 0.10) <= nb_keypoints_if_branch / nb_iterations <= (0.50 + 0.10)
    assert (0.50 - 0.10) <= nb_keypoints_else_branch / nb_iterations <= (0.50 + 0.10)
    assert (0.50 - 0.10) <= (1 - (nb_changed_aug / nb_iterations)) <= (0.50 + 0.10) # should be the same in roughly 50% of all cases
    assert nb_changed_aug_det == 0

    # 50% if branch, otherwise no change
    aug = iaa.Sometimes(0.5, iaa.Fliplr(1.0))
    aug_det = aug.to_deterministic()
    last_aug = None
    last_aug_det = None
    nb_changed_aug = 0
    nb_changed_aug_det = 0
    nb_iterations = 1000
    nb_images_if_branch = 0
    nb_images_else_branch = 0
    nb_keypoints_if_branch = 0
    nb_keypoints_else_branch = 0
    for i in sm.xrange(nb_iterations):
        observed_aug = aug.augment_images(images)
        observed_aug_det = aug_det.augment_images(images)
        keypoints_aug = aug.augment_keypoints(keypoints)
        keypoints_aug_det = aug.augment_keypoints(keypoints)
        if i == 0:
            last_aug = observed_aug
            last_aug_det = observed_aug_det
        else:
            if not np.array_equal(observed_aug, last_aug):
                nb_changed_aug += 1
            if not np.array_equal(observed_aug_det, last_aug_det):
                nb_changed_aug_det += 1
            last_aug = observed_aug
            last_aug_det = observed_aug_det

        if np.array_equal(observed_aug, images_lr):
            nb_images_if_branch += 1
        elif np.array_equal(observed_aug, images):
            nb_images_else_branch += 1
        else:
            raise Exception("Received output doesnt match any expected output.")

        if keypoints_equal(keypoints_aug, keypoints_lr):
            nb_keypoints_if_branch += 1
        elif keypoints_equal(keypoints_aug, keypoints):
            nb_keypoints_else_branch += 1
        else:
            raise Exception("Received output doesnt match any expected output.")

    assert (0.50 - 0.10) <= nb_images_if_branch / nb_iterations <= (0.50 + 0.10)
    assert (0.50 - 0.10) <= nb_images_else_branch / nb_iterations <= (0.50 + 0.10)
    assert (0.50 - 0.10) <= nb_keypoints_if_branch / nb_iterations <= (0.50 + 0.10)
    assert (0.50 - 0.10) <= nb_keypoints_else_branch / nb_iterations <= (0.50 + 0.10)
    assert (0.50 - 0.10) <= (1 - (nb_changed_aug / nb_iterations)) <= (0.50 + 0.10) # should be the same in roughly 50% of all cases
    assert nb_changed_aug_det == 0


def test_WithChannels():
    base_img = np.zeros((3, 3, 2), dtype=np.uint8)
    base_img[..., 0] += 100
    base_img[..., 1] += 200

    aug = iaa.WithChannels(None, iaa.Add(10))
    observed = aug.augment_image(base_img)
    expected = base_img + 10
    assert np.allclose(observed, expected)

    aug = iaa.WithChannels(0, iaa.Add(10))
    observed = aug.augment_image(base_img)
    expected = np.copy(base_img)
    expected[..., 0] += 10
    assert np.allclose(observed, expected)

    aug = iaa.WithChannels(1, iaa.Add(10))
    observed = aug.augment_image(base_img)
    expected = np.copy(base_img)
    expected[..., 1] += 10
    assert np.allclose(observed, expected)

    base_img = np.zeros((3, 3, 2), dtype=np.uint8)
    base_img[..., 0] += 5
    base_img[..., 1] += 10
    aug = iaa.WithChannels(1, [iaa.Add(10), iaa.Multiply(2.0)])
    observed = aug.augment_image(base_img)
    expected = np.copy(base_img)
    expected[..., 1] += 10
    expected[..., 1] *= 2
    assert np.allclose(observed, expected)


def test_2d_inputs():
    """Test whether inputs of 2D-images (i.e. (H, W) instead of (H, W, C)) work.
    """
    reseed()

    base_img1 = np.array([[0, 0, 1, 1],
                          [0, 0, 1, 1],
                          [0, 1, 1, 1]], dtype=np.uint8)
    base_img2 = np.array([[0, 0, 1, 1],
                          [0, 1, 1, 1],
                          [0, 1, 0, 0]], dtype=np.uint8)

    base_img1_flipped = np.array([[1, 1, 0, 0],
                                  [1, 1, 0, 0],
                                  [1, 1, 1, 0]], dtype=np.uint8)
    base_img2_flipped = np.array([[1, 1, 0, 0],
                                  [1, 1, 1, 0],
                                  [0, 0, 1, 0]], dtype=np.uint8)

    images = np.array([base_img1, base_img2])
    images_flipped = np.array([base_img1_flipped, base_img2_flipped])
    images_list = [base_img1, base_img2]
    images_flipped_list = [base_img1_flipped, base_img2_flipped]
    images_list2d3d = [base_img1, base_img2[:, :, np.newaxis]]
    images_flipped_list2d3d = [base_img1_flipped, base_img2_flipped[:, :, np.newaxis]]

    aug = iaa.Fliplr(1.0)
    noaug = iaa.Fliplr(0.0)

    # one numpy array as input
    observed = aug.augment_images(images)
    assert np.array_equal(observed, images_flipped)

    observed = noaug.augment_images(images)
    assert np.array_equal(observed, images)

    # list of 2d images
    observed = aug.augment_images(images_list)
    assert array_equal_lists(observed, images_flipped_list)

    observed = noaug.augment_images(images_list)
    assert array_equal_lists(observed, images_list)

    # list of images, one 2d and one 3d
    observed = aug.augment_images(images_list2d3d)
    assert array_equal_lists(observed, images_flipped_list2d3d)

    observed = noaug.augment_images(images_list2d3d)
    assert array_equal_lists(observed, images_list2d3d)


def test_background_augmentation():
    reseed()

    image = np.array([[0, 0, 1, 1],
                      [0, 0, 1, 1],
                      [0, 1, 1, 1]], dtype=np.uint8)
    image_flipped = np.fliplr(image)
    keypoint = ia.Keypoint(x=2, y=1)
    keypoints = [ia.KeypointsOnImage([keypoint], shape=image.shape + (1,))]
    kp_flipped = ia.Keypoint(
        x=image.shape[1]-1-keypoint.x,
        y=keypoint.y
    )

    seq = iaa.Fliplr(0.5)

    # with images as list, background=False
    nb_flipped_images = 0
    nb_flipped_keypoints = 0
    nb_iterations = 1000
    batches = [ia.Batch(images=[np.copy(image)], keypoints=[keypoints[0].deepcopy()]) for _ in sm.xrange(nb_iterations)]
    batches_aug = list(seq.augment_batches(batches, background=False))
    for batch_aug in batches_aug:
        image_aug = batch_aug.images_aug[0]
        keypoint_aug = batch_aug.keypoints_aug[0].keypoints[0]
        assert np.array_equal(image_aug, image) or np.array_equal(image_aug, image_flipped)
        if np.array_equal(image_aug, image_flipped):
            nb_flipped_images += 1

        assert (keypoint_aug.x == keypoint.x and keypoint_aug.y == keypoint.y) \
               or (keypoint_aug.x == kp_flipped.x and keypoint_aug.y == kp_flipped.y)
        if keypoint_aug.x == kp_flipped.x and keypoint_aug.y == kp_flipped.y:
            nb_flipped_keypoints += 1
    assert 0.4*nb_iterations <= nb_flipped_images <= 0.6*nb_iterations
    assert nb_flipped_images == nb_flipped_keypoints

    # with images as list
    nb_flipped_images = 0
    nb_flipped_keypoints = 0
    nb_iterations = 1000
    batches = [ia.Batch(images=[np.copy(image)], keypoints=[keypoints[0].deepcopy()]) for _ in sm.xrange(nb_iterations)]
    batches_aug = list(seq.augment_batches(batches, background=True))
    for batch_aug in batches_aug:
        image_aug = batch_aug.images_aug[0]
        keypoint_aug = batch_aug.keypoints_aug[0].keypoints[0]
        assert np.array_equal(image_aug, image) or np.array_equal(image_aug, image_flipped)
        if np.array_equal(image_aug, image_flipped):
            nb_flipped_images += 1

        assert (keypoint_aug.x == keypoint.x and keypoint_aug.y == keypoint.y) \
               or (keypoint_aug.x == kp_flipped.x and keypoint_aug.y == kp_flipped.y)
        if keypoint_aug.x == kp_flipped.x and keypoint_aug.y == kp_flipped.y:
            nb_flipped_keypoints += 1
    assert 0.4*nb_iterations <= nb_flipped_images <= 0.6*nb_iterations
    assert nb_flipped_images == nb_flipped_keypoints

    # with images as array
    nb_flipped_images = 0
    nb_flipped_keypoints = 0
    nb_iterations = 1000
    batches = [ia.Batch(images=np.array([np.copy(image)], dtype=np.uint8), keypoints=None) for _ in sm.xrange(nb_iterations)]
    batches_aug = list(seq.augment_batches(batches, background=True))
    for batch_aug in batches_aug:
        #batch = ia.Batch(images=np.array([image], dtype=np.uint8), keypoints=keypoints)
        #batches_aug = list(seq.augment_batches([batch], background=True))
        #batch_aug = batches_aug[0]
        image_aug = batch_aug.images_aug[0]
        assert np.array_equal(image_aug, image) or np.array_equal(image_aug, image_flipped)
        if np.array_equal(image_aug, image_flipped):
            nb_flipped_images += 1
    assert 0.4*nb_iterations <= nb_flipped_images <= 0.6*nb_iterations

    # array (N, H, W) as input
    nb_flipped_images = 0
    nb_iterations = 1000
    batches = [np.array([np.copy(image)], dtype=np.uint8) for _ in sm.xrange(nb_iterations)]
    batches_aug = list(seq.augment_batches(batches, background=True))
    for batch_aug in batches_aug:
        #batch = np.array([image], dtype=np.uint8)
        #batches_aug = list(seq.augment_batches([batch], background=True))
        #image_aug = batches_aug[0][0]
        image_aug = batch_aug[0]
        assert np.array_equal(image_aug, image) or np.array_equal(image_aug, image_flipped)
        if np.array_equal(image_aug, image_flipped):
            nb_flipped_images += 1
    assert 0.4*nb_iterations <= nb_flipped_images <= 0.6*nb_iterations

    # list of list of KeypointsOnImage as input
    nb_flipped_keypoints = 0
    nb_iterations = 1000
    #batches = [ia.Batch(images=[np.copy(image)], keypoints=None) for _ in sm.xrange(nb_iterations)]
    batches = [[keypoints[0].deepcopy()] for _ in sm.xrange(nb_iterations)]
    batches_aug = list(seq.augment_batches(batches, background=True))
    for batch_aug in batches_aug:
        #batch = [keypoints]
        #batches_aug = list(seq.augment_batches([batch], background=True))
        #batch_aug = batches_aug[0]
        #keypoint_aug = batches_aug[0].keypoints[0].keypoints[0]
        keypoint_aug = batch_aug[0].keypoints[0]

        assert (keypoint_aug.x == keypoint.x and keypoint_aug.y == keypoint.y) \
               or (keypoint_aug.x == kp_flipped.x and keypoint_aug.y == kp_flipped.y)
        if keypoint_aug.x == kp_flipped.x and keypoint_aug.y == kp_flipped.y:
            nb_flipped_keypoints += 1
    assert 0.4*nb_iterations <= nb_flipped_keypoints <= 0.6*nb_iterations

    # test all augmenters
    # this test is currently skipped by default as it takes around 40s on its own,
    # probably because of having to start background processes
    """
    augs = [
        iaa.Sequential([iaa.Fliplr(1.0), iaa.Flipud(1.0)]),
        iaa.SomeOf(1, [iaa.Fliplr(1.0), iaa.Flipud(1.0)]),
        iaa.OneOf([iaa.Fliplr(1.0), iaa.Flipud(1.0)]),
        iaa.Sometimes(1.0, iaa.Fliplr(1)),
        iaa.WithColorspace("HSV", children=iaa.Add((-50, 50))),
        iaa.WithChannels([0], iaa.Add((-50, 50))),
        iaa.Noop(name="Noop-nochange"),
        iaa.Lambda(
            func_images=lambda images, random_state, parents, hooks: images,
            func_keypoints=lambda keypoints_on_images, random_state, parents, hooks: keypoints_on_images,
            name="Lambda-nochange"
        ),
        iaa.AssertLambda(
            func_images=lambda images, random_state, parents, hooks: True,
            func_keypoints=lambda keypoints_on_images, random_state, parents, hooks: True,
            name="AssertLambda-nochange"
        ),
        iaa.AssertShape(
            (None, 64, 64, 3),
            check_keypoints=False,
            name="AssertShape-nochange"
        ),
        iaa.Scale((0.5, 0.9)),
        iaa.CropAndPad(px=(-50, 50)),
        iaa.Pad(px=(1, 50)),
        iaa.Crop(px=(1, 50)),
        iaa.Fliplr(1.0),
        iaa.Flipud(1.0),
        iaa.Superpixels(p_replace=(0.25, 1.0), n_segments=(16, 128)),
        iaa.ChangeColorspace(to_colorspace="GRAY"),
        iaa.Grayscale(alpha=(0.1, 1.0)),
        iaa.GaussianBlur(1.0),
        iaa.AverageBlur(5),
        iaa.MedianBlur(5),
        iaa.Convolve(np.array([[0, 1, 0],
                               [1, -4, 1],
                               [0, 1, 0]])),
        iaa.Sharpen(alpha=(0.1, 1.0), lightness=(0.8, 1.2)),
        iaa.Emboss(alpha=(0.1, 1.0), strength=(0.8, 1.2)),
        iaa.EdgeDetect(alpha=(0.1, 1.0)),
        iaa.DirectedEdgeDetect(alpha=(0.1, 1.0), direction=(0.0, 1.0)),
        iaa.Add((-50, 50)),
        iaa.AddElementwise((-50, 50)),
        iaa.AdditiveGaussianNoise(scale=(0.1, 1.0)),
        iaa.Multiply((0.6, 1.4)),
        iaa.MultiplyElementwise((0.6, 1.4)),
        iaa.Dropout((0.3, 0.5)),
        iaa.CoarseDropout((0.3, 0.5), size_percent=(0.05, 0.2)),
        iaa.Invert(0.5),
        iaa.ContrastNormalization((0.6, 1.4)),
        iaa.Affine(scale=(0.7, 1.3), translate_percent=(-0.1, 0.1), rotate=(-20, 20),
                   shear=(-20, 20), order=ia.ALL, mode=ia.ALL, cval=(0, 255)),
        iaa.PiecewiseAffine(scale=(0.1, 0.3)),
        iaa.ElasticTransformation(alpha=0.5)
    ]

    nb_iterations = 100
    image = ia.quokka(size=(64, 64))
    batch = ia.Batch(images=np.array([image]), keypoints=keypoints)
    batches = [ia.Batch(images=[np.copy(image)], keypoints=[keypoints[0].deepcopy()])
               for _ in sm.xrange(nb_iterations)]
    for aug in augs:
        nb_changed = 0
        batches_aug = list(aug.augment_batches(batches, background=True))
        for batch_aug in batches_aug:
            image_aug = batch_aug.images_aug[0]
            if image.shape != image_aug.shape or not np.array_equal(image, image_aug):
                nb_changed += 1
                if nb_changed > 10:
                    break
        if "-nochange" not in aug.name:
            assert nb_changed > 0
        else:
            assert nb_changed == 0
    """


def test_determinism():
    reseed()

    images = [
        ia.quokka(size=(128, 128)),
        ia.quokka(size=(64, 64)),
        misc.imresize(data.astronaut(), (128, 256))
    ]
    keypoints = [
        ia.KeypointsOnImage([
            ia.Keypoint(x=20, y=10), ia.Keypoint(x=5, y=5), ia.Keypoint(x=10, y=43)
            ], shape=(50, 60, 3))
    ]

    augs = [
        iaa.Sequential([iaa.Fliplr(1.0), iaa.Flipud(1.0)]),
        iaa.SomeOf(1, [iaa.Fliplr(1.0), iaa.Flipud(1.0)]),
        iaa.OneOf([iaa.Fliplr(1.0), iaa.Flipud(1.0)]),
        iaa.Sometimes(1.0, iaa.Fliplr(1)),
        iaa.WithColorspace("HSV", children=iaa.Add((-50, 50))),
        iaa.WithChannels([0], iaa.Add((-50, 50))),
        iaa.Noop(name="Noop-nochange"),
        iaa.Lambda(
            func_images=lambda images, random_state, parents, hooks: images,
            func_keypoints=lambda keypoints_on_images, random_state, parents, hooks: keypoints_on_images,
            name="Lambda-nochange"
        ),
        iaa.AssertLambda(
            func_images=lambda images, random_state, parents, hooks: True,
            func_keypoints=lambda keypoints_on_images, random_state, parents, hooks: True,
            name="AssertLambda-nochange"
        ),
        iaa.AssertShape(
            (None, None, None, 3),
            check_keypoints=False,
            name="AssertShape-nochange"
        ),
        iaa.Scale((0.5, 0.9)),
        iaa.CropAndPad(px=(-50, 50)),
        iaa.Pad(px=(1, 50)),
        iaa.Crop(px=(1, 50)),
        iaa.Fliplr(1.0),
        iaa.Flipud(1.0),
        iaa.Superpixels(p_replace=(0.25, 1.0), n_segments=(16, 128)),
        iaa.ChangeColorspace(to_colorspace="GRAY"),
        iaa.Grayscale(alpha=(0.1, 1.0)),
        iaa.GaussianBlur(1.0),
        iaa.AverageBlur(5),
        iaa.MedianBlur(5),
        iaa.Convolve(np.array([[0, 1, 0],
                               [1, -4, 1],
                               [0, 1, 0]])),
        iaa.Sharpen(alpha=(0.1, 1.0), lightness=(0.8, 1.2)),
        iaa.Emboss(alpha=(0.1, 1.0), strength=(0.8, 1.2)),
        iaa.EdgeDetect(alpha=(0.1, 1.0)),
        iaa.DirectedEdgeDetect(alpha=(0.1, 1.0), direction=(0.0, 1.0)),
        iaa.Add((-50, 50)),
        iaa.AddElementwise((-50, 50)),
        iaa.AdditiveGaussianNoise(scale=(0.1, 1.0)),
        iaa.Multiply((0.6, 1.4)),
        iaa.MultiplyElementwise((0.6, 1.4)),
        iaa.Dropout((0.3, 0.5)),
        iaa.CoarseDropout((0.3, 0.5), size_percent=(0.05, 0.2)),
        iaa.Invert(0.5),
        iaa.ContrastNormalization((0.6, 1.4)),
        iaa.Affine(scale=(0.7, 1.3), translate_percent=(-0.1, 0.1),
                   rotate=(-20, 20), shear=(-20, 20), order=ia.ALL,
                   mode=ia.ALL, cval=(0, 255)),
        iaa.PiecewiseAffine(scale=(0.1, 0.3)),
        iaa.ElasticTransformation(alpha=0.5)
    ]

    for aug in augs:
        aug_det = aug.to_deterministic()
        images_aug1 = aug_det.augment_images(images)
        images_aug2 = aug_det.augment_images(images)
        kps_aug1 = aug_det.augment_keypoints(keypoints)
        kps_aug2 = aug_det.augment_keypoints(keypoints)
        assert array_equal_lists(images_aug1, images_aug2), \
            "Images not identical for %s" % (aug.name,)
        assert keypoints_equal(kps_aug1, kps_aug2), \
            "Keypoints not identical for %s" % (aug.name,)


def test_keypoint_augmentation():
    ia.seed(1)

    keypoints = []
    for y in range(40//5):
        for x in range(60//5):
            keypoints.append(ia.Keypoint(y=y*5, x=x*5))

    keypoints_oi = ia.KeypointsOnImage(keypoints, shape=(40, 60, 3))
    augs = [
        iaa.Add((-5, 5), name="Add"),
        iaa.AddElementwise((-5, 5), name="AddElementwise"),
        iaa.AdditiveGaussianNoise(0.01*255, name="AdditiveGaussianNoise"),
        iaa.Multiply((0.95, 1.05), name="Multiply"),
        iaa.Dropout(0.01, name="Dropout"),
        iaa.CoarseDropout(0.01, size_px=6, name="CoarseDropout"),
        iaa.Invert(0.01, per_channel=True, name="Invert"),
        iaa.ContrastNormalization((0.95, 1.05), name="ContrastNormalization"),
        iaa.GaussianBlur(sigma=(0.95, 1.05), name="GaussianBlur"),
        iaa.AverageBlur((3, 5), name="AverageBlur"),
        iaa.MedianBlur((3, 5), name="MedianBlur"),
        #iaa.BilateralBlur((3, 5), name="BilateralBlur"),
        # WithColorspace ?
        #iaa.AddToHueAndSaturation((-5, 5), name="AddToHueAndSaturation"),
        # ChangeColorspace ?
        # Grayscale cannot be tested, input not RGB
        # Convolve ?
        iaa.Sharpen((0.0, 0.1), lightness=(1.0, 1.2), name="Sharpen"),
        iaa.Emboss(alpha=(0.0, 0.1), strength=(0.5, 1.5), name="Emboss"),
        iaa.EdgeDetect(alpha=(0.0, 0.1), name="EdgeDetect"),
        iaa.DirectedEdgeDetect(alpha=(0.0, 0.1), direction=0, name="DirectedEdgeDetect"),
        iaa.Fliplr(0.5, name="Fliplr"),
        iaa.Flipud(0.5, name="Flipud"),
        iaa.Affine(translate_px=(-5, 5), name="Affine-translate-px"),
        iaa.Affine(translate_percent=(-0.05, 0.05), name="Affine-translate-percent"),
        iaa.Affine(rotate=(-20, 20), name="Affine-rotate"),
        iaa.Affine(shear=(-20, 20), name="Affine-shear"),
        iaa.Affine(scale=(0.9, 1.1), name="Affine-scale"),
        iaa.PiecewiseAffine(scale=(0.001, 0.005), name="PiecewiseAffine"),
        #iaa.PerspectiveTransform(scale=(0.01, 0.10), name="PerspectiveTransform"),
        iaa.ElasticTransformation(alpha=(0.1, 0.2), sigma=(0.1, 0.2), name="ElasticTransformation"),
        # Sequential
        # SomeOf
        # OneOf
        # Sometimes
        # WithChannels
        # Noop
        # Lambda
        # AssertLambda
        # AssertShape
        iaa.Alpha((0.0, 0.1), iaa.Add(10), name="Alpha"),
        iaa.AlphaElementwise((0.0, 0.1), iaa.Add(10), name="AlphaElementwise"),
        iaa.SimplexNoiseAlpha(iaa.Add(10), name="SimplexNoiseAlpha"),
        iaa.FrequencyNoiseAlpha(exponent=(-2, 2), first=iaa.Add(10),
                                name="SimplexNoiseAlpha"),
        iaa.Superpixels(p_replace=0.01, n_segments=64),
        iaa.Scale(0.5, name="Scale"),
        iaa.CropAndPad(px=(-10, 10), name="CropAndPad"),
        iaa.Pad(px=(0, 10), name="Pad"),
        iaa.Crop(px=(0, 10), name="Crop")
    ]

    for aug in augs:
        #if aug.name != "PiecewiseAffine":
        #    continue
        dss = []
        for i in range(10):
            aug_det = aug.to_deterministic()
            kp_image = keypoints_oi.to_keypoint_image(size=5)
            kp_image_aug = aug_det.augment_image(kp_image)
            kp_image_aug_rev = ia.KeypointsOnImage.from_keypoint_image(
                kp_image_aug,
                if_not_found_coords={"x": -9999, "y": -9999},
                nb_channels=1
            )
            kp_aug = aug_det.augment_keypoints([keypoints_oi])[0]
            ds = []
            assert len(kp_image_aug_rev.keypoints) == len(kp_aug.keypoints),\
                "Lost keypoints for '%s' (%d vs expected %d)" \
                % (aug.name, len(kp_aug.keypoints), len(kp_image_aug_rev.keypoints))
            for kp_pred, kp_pred_img in zip(kp_aug.keypoints, kp_image_aug_rev.keypoints):
                kp_pred_lost = (kp_pred.x == -9999 and kp_pred.y == -9999)
                kp_pred_img_lost = (kp_pred_img.x == -9999 and kp_pred_img.y == -9999)
                #if kp_pred_lost and not kp_pred_img_lost:
                #    print("lost kp_pred", kp_pred_img)
                #elif not kp_pred_lost and kp_pred_img_lost:
                #    print("lost kp_pred_img", kp_pred)
                #elif kp_pred_lost and kp_pred_img_lost:
                #    print("lost both keypoints")

                if not kp_pred_lost and not kp_pred_img_lost:
                    d = np.sqrt((kp_pred.x - kp_pred_img.x) ** 2
                                + (kp_pred.y - kp_pred_img.y) ** 2)
                    ds.append(d)
            #print(aug.name, np.average(ds), ds)
            dss.extend(ds)
            if len(ds) == 0:
                print("[INFO] No valid keypoints found for '%s' "
                      "in test_keypoint_augmentation()" % (str(aug),))
        assert np.average(dss) < 5.0, \
            "Average distance too high (%.2f, with ds: %s)" \
            % (np.average(dss), str(dss))


def test_unusual_channel_numbers():
    ia.seed(1)

    images = [
        (0, create_random_images((4, 16, 16))),
        (1, create_random_images((4, 16, 16, 1))),
        (2, create_random_images((4, 16, 16, 2))),
        (4, create_random_images((4, 16, 16, 4))),
        (5, create_random_images((4, 16, 16, 5))),
        (10, create_random_images((4, 16, 16, 10))),
        (20, create_random_images((4, 16, 16, 20)))
    ]

    augs = [
        iaa.Add((-5, 5), name="Add"),
        iaa.AddElementwise((-5, 5), name="AddElementwise"),
        iaa.AdditiveGaussianNoise(0.01*255, name="AdditiveGaussianNoise"),
        iaa.Multiply((0.95, 1.05), name="Multiply"),
        iaa.Dropout(0.01, name="Dropout"),
        iaa.CoarseDropout(0.01, size_px=6, name="CoarseDropout"),
        iaa.Invert(0.01, per_channel=True, name="Invert"),
        iaa.ContrastNormalization((0.95, 1.05), name="ContrastNormalization"),
        iaa.GaussianBlur(sigma=(0.95, 1.05), name="GaussianBlur"),
        iaa.AverageBlur((3, 5), name="AverageBlur"),
        iaa.MedianBlur((3, 5), name="MedianBlur"),
        #iaa.BilateralBlur((3, 5), name="BilateralBlur"), # works only with 3/RGB channels
        # WithColorspace ?
        #iaa.AddToHueAndSaturation((-5, 5), name="AddToHueAndSaturation"), # works only with 3/RGB channels
        # ChangeColorspace ?
        #iaa.Grayscale((0.0, 0.1), name="Grayscale"), # works only with 3 channels
        # Convolve ?
        iaa.Sharpen((0.0, 0.1), lightness=(1.0, 1.2), name="Sharpen"),
        iaa.Emboss(alpha=(0.0, 0.1), strength=(0.5, 1.5), name="Emboss"),
        iaa.EdgeDetect(alpha=(0.0, 0.1), name="EdgeDetect"),
        iaa.DirectedEdgeDetect(alpha=(0.0, 0.1), direction=0,
                               name="DirectedEdgeDetect"),
        iaa.Fliplr(0.5, name="Fliplr"),
        iaa.Flipud(0.5, name="Flipud"),
        iaa.Affine(translate_px=(-5, 5), name="Affine-translate-px"),
        iaa.Affine(translate_percent=(-0.05, 0.05), name="Affine-translate-percent"),
        iaa.Affine(rotate=(-20, 20), name="Affine-rotate"),
        iaa.Affine(shear=(-20, 20), name="Affine-shear"),
        iaa.Affine(scale=(0.9, 1.1), name="Affine-scale"),
        iaa.PiecewiseAffine(scale=(0.001, 0.005), name="PiecewiseAffine"),
        iaa.PerspectiveTransform(scale=(0.01, 0.10), name="PerspectiveTransform"),
        iaa.ElasticTransformation(alpha=(0.1, 0.2), sigma=(0.1, 0.2),
                                  name="ElasticTransformation"),
        iaa.Sequential([iaa.Add((-5, 5)), iaa.AddElementwise((-5, 5))]),
        iaa.SomeOf(1, [iaa.Add((-5, 5)), iaa.AddElementwise((-5, 5))]),
        iaa.OneOf(iaa.Add((-5, 5)), iaa.AddElementwise((-5, 5))),
        iaa.Sometimes(0.5, iaa.Add((-5, 5)), name="Sometimes"),
        # WithChannels
        iaa.Noop(name="Noop"),
        # Lambda
        # AssertLambda
        # AssertShape
        iaa.Alpha((0.0, 0.1), iaa.Add(10), name="Alpha"),
        iaa.AlphaElementwise((0.0, 0.1), iaa.Add(10), name="AlphaElementwise"),
        iaa.SimplexNoiseAlpha(iaa.Add(10), name="SimplexNoiseAlpha"),
        iaa.FrequencyNoiseAlpha(exponent=(-2, 2), first=iaa.Add(10),
                                name="SimplexNoiseAlpha"),
        iaa.Superpixels(p_replace=0.01, n_segments=64),
        iaa.Scale({"height": 4, "width": 4}, name="Scale"),
        iaa.CropAndPad(px=(-10, 10), name="CropAndPad"),
        iaa.Pad(px=(0, 10), name="Pad"),
        iaa.Crop(px=(0, 10), name="Crop")
    ]

    for aug in augs:
        for (nb_channels, images_c) in images:
            #print("shape", images_c.shape, aug.name)
            if aug.name != "Scale":
                images_aug = aug.augment_images(images_c)
                assert images_aug.shape == images_c.shape
                image_aug = aug.augment_image(images_c[0])
                assert image_aug.shape == images_c[0].shape
            else:
                images_aug = aug.augment_images(images_c)
                image_aug = aug.augment_image(images_c[0])
                if images_c.ndim == 3:
                    assert images_aug.shape == (4, 4, 4)
                    assert image_aug.shape == (4, 4)
                else:
                    assert images_aug.shape == (4, 4, 4, images_c.shape[3])
                    assert image_aug.shape == (4, 4, images_c.shape[3])


#@attr("now")
def test_dtype_preservation():
    ia.seed(1)

    size = (4, 16, 16, 3)
    images = [
        np.random.uniform(0, 255, size).astype(np.uint8),
        np.random.uniform(0, 65535, size).astype(np.uint16),
        np.random.uniform(0, 4294967295, size).astype(np.uint32), # not supported by cv2.blur in AverageBlur
        np.random.uniform(-128, 127, size).astype(np.int16),
        np.random.uniform(-32768, 32767, size).astype(np.int32),
        np.random.uniform(0.0, 1.0, size).astype(np.float32),
        np.random.uniform(-1000.0, 1000.0, size).astype(np.float16), # not supported by scipy.ndimage.filter in GaussianBlur
        np.random.uniform(-1000.0, 1000.0, size).astype(np.float32),
        np.random.uniform(-1000.0, 1000.0, size).astype(np.float64)
    ]

    default_dtypes = set([arr.dtype for arr in images])
    # Some dtypes are here removed per augmenter, because the respective
    # augmenter does not support them. This test currently only checks whether
    # dtypes are preserved from in- to output for all dtypes that are supported
    # per augmenter.
    # dtypes are here removed via list comprehension instead of
    # `default_dtypes - set([dtype])`, because the latter one simply never
    # removed the dtype(s) for some reason?!
    augs = [
        (iaa.Add((-5, 5), name="Add"), default_dtypes),
        (iaa.AddElementwise((-5, 5), name="AddElementwise"), default_dtypes),
        (iaa.AdditiveGaussianNoise(0.01*255, name="AdditiveGaussianNoise"), default_dtypes),
        (iaa.Multiply((0.95, 1.05), name="Multiply"), default_dtypes),
        (iaa.Dropout(0.01, name="Dropout"), default_dtypes),
        (iaa.CoarseDropout(0.01, size_px=6, name="CoarseDropout"), default_dtypes),
        (iaa.Invert(0.01, per_channel=True, name="Invert"), default_dtypes),
        (iaa.ContrastNormalization((0.95, 1.05), name="ContrastNormalization"), default_dtypes),
        (iaa.GaussianBlur(sigma=(0.95, 1.05), name="GaussianBlur"), [dt for dt in default_dtypes if dt not in [np.float16]]),
        (iaa.AverageBlur((3, 5), name="AverageBlur"), [dt for dt in default_dtypes if dt not in [np.uint32, np.float16]]),
        (iaa.MedianBlur((3, 5), name="MedianBlur"), [dt for dt in default_dtypes if dt not in [np.uint32, np.int32, np.float16, np.float64]]),
        (iaa.BilateralBlur((3, 5), name="BilateralBlur"), [dt for dt in default_dtypes if dt not in [np.uint16, np.uint32, np.int16, np.int32, np.float16, np.float64]]),
        # WithColorspace ?
        #iaa.AddToHueAndSaturation((-5, 5), name="AddToHueAndSaturation"), # works only with RGB/uint8
        # ChangeColorspace ?
        #iaa.Grayscale((0.0, 0.1), name="Grayscale"), # works only with RGB/uint8
        # Convolve ?
        (iaa.Sharpen((0.0, 0.1), lightness=(1.0, 1.2), name="Sharpen"), [dt for dt in default_dtypes if dt not in [np.uint32, np.int32, np.float16, np.uint32]]),
        (iaa.Emboss(alpha=(0.0, 0.1), strength=(0.5, 1.5), name="Emboss"), [dt for dt in default_dtypes if dt not in [np.uint32, np.int32, np.float16, np.uint32]]),
        (iaa.EdgeDetect(alpha=(0.0, 0.1), name="EdgeDetect"), [dt for dt in default_dtypes if dt not in [np.uint32, np.int32, np.float16, np.uint32]]),
        (iaa.DirectedEdgeDetect(alpha=(0.0, 0.1), direction=0, name="DirectedEdgeDetect"), [dt for dt in default_dtypes if dt not in [np.uint32, np.int32, np.float16, np.uint32]]),
        (iaa.Fliplr(0.5, name="Fliplr"), default_dtypes),
        (iaa.Flipud(0.5, name="Flipud"), default_dtypes),
        (iaa.Affine(translate_px=(-5, 5), name="Affine-translate-px"), default_dtypes),
        (iaa.Affine(translate_percent=(-0.05, 0.05), name="Affine-translate-percent"), default_dtypes),
        (iaa.Affine(rotate=(-20, 20), name="Affine-rotate"), default_dtypes),
        (iaa.Affine(shear=(-20, 20), name="Affine-shear"), default_dtypes),
        (iaa.Affine(scale=(0.9, 1.1), name="Affine-scale"), default_dtypes),
        (iaa.PiecewiseAffine(scale=(0.001, 0.005), name="PiecewiseAffine"), default_dtypes),
        #(iaa.PerspectiveTransform(scale=(0.01, 0.10), name="PerspectiveTransform"), [dt for dt in default_dtypes if dt not in [np.uint32]]),
        (iaa.ElasticTransformation(alpha=(0.1, 0.2), sigma=(0.1, 0.2), name="ElasticTransformation"), [dt for dt in default_dtypes if dt not in [np.float16]]),
        (iaa.Sequential([iaa.Add((-5, 5)), iaa.AddElementwise((-5, 5))]), default_dtypes),
        (iaa.SomeOf(1, [iaa.Add((-5, 5)), iaa.AddElementwise((-5, 5))]), default_dtypes),
        (iaa.OneOf(iaa.Add((-5, 5)), iaa.AddElementwise((-5, 5))), default_dtypes),
        (iaa.Sometimes(0.5, iaa.Add((-5, 5)), name="Sometimes"), default_dtypes),
        # WithChannels
        (iaa.Noop(name="Noop"), default_dtypes),
        # Lambda
        # AssertLambda
        # AssertShape
        (iaa.Alpha((0.0, 0.1), iaa.Add(10), name="Alpha"), default_dtypes),
        (iaa.AlphaElementwise((0.0, 0.1), iaa.Add(10), name="AlphaElementwise"), default_dtypes),
        (iaa.SimplexNoiseAlpha(iaa.Add(10), name="SimplexNoiseAlpha"), default_dtypes),
        (iaa.FrequencyNoiseAlpha(exponent=(-2, 2), first=iaa.Add(10), name="SimplexNoiseAlpha"), default_dtypes),
        (iaa.Superpixels(p_replace=0.01, n_segments=64), [dt for dt in default_dtypes if dt not in [np.float16, np.float32]]),
        (iaa.Scale({"height": 4, "width": 4}, name="Scale"), [dt for dt in default_dtypes if dt not in [np.uint16, np.uint32, np.int16, np.int32, np.float32, np.float16, np.float64]]),
        (iaa.CropAndPad(px=(-10, 10), name="CropAndPad"), [dt for dt in default_dtypes if dt not in [np.uint16, np.uint32, np.int16, np.int32, np.float32, np.float16, np.float64]]),
        (iaa.Pad(px=(0, 10), name="Pad"), [dt for dt in default_dtypes if dt not in [np.uint16, np.uint32, np.int16, np.int32, np.float32, np.float16, np.float64]]),
        (iaa.Crop(px=(0, 10), name="Crop"), [dt for dt in default_dtypes if dt not in [np.uint16, np.uint32, np.int16, np.int32, np.float32, np.float16, np.float64]])
    ]

    for (aug, allowed_dtypes) in augs:
        #print(aug.name, allowed_dtypes)
        for images_i in images:
            if images_i.dtype in allowed_dtypes:
                #print("shape", images_i.shape, images_i.dtype, aug.name)
                images_aug = aug.augment_images(images_i)
                #assert images_aug.shape == images_i.shape
                assert images_aug.dtype == images_i.dtype
            else:
                #print("Skipped dtype %s for augmenter %s" % (images_i.dtype, aug.name))
                pass

def test_copy_random_state():
    image = ia.quokka_square(size=(128, 128))
    images = np.array([image] * 64, dtype=np.uint8)

    source = iaa.Sequential([
        iaa.Fliplr(0.5, name="hflip"),
        iaa.Dropout(0.05, name="dropout"),
        iaa.Affine(translate_px=(-10, 10), name="translate", random_state=3),
        iaa.GaussianBlur(1.0, name="blur", random_state=4)
    ], random_state=5)
    target = iaa.Sequential([
        iaa.Fliplr(0.5, name="hflip"),
        iaa.Dropout(0.05, name="dropout"),
        iaa.Affine(translate_px=(-10, 10), name="translate")
    ])

    source.localize_random_state_()

    target_cprs = target.copy_random_state(source, matching="position")
    source_alt = source.remove_augmenters(lambda aug, parents: aug.name == "blur")
    images_aug_source = source_alt.augment_images(images)
    images_aug_target = target_cprs.augment_images(images)
    #misc.imshow(np.hstack([images_aug_source[0], images_aug_source[1], images_aug_target[0], images_aug_target[1]]))
    assert np.array_equal(images_aug_source, images_aug_target)

    target_cprs = target.copy_random_state(source, matching="name")
    source_alt = source.remove_augmenters(lambda aug, parents: aug.name == "blur")
    images_aug_source = source_alt.augment_images(images)
    images_aug_target = target_cprs.augment_images(images)
    assert np.array_equal(images_aug_source, images_aug_target)

    source_alt = source.remove_augmenters(lambda aug, parents: aug.name == "blur")
    source_det = source_alt.to_deterministic()
    target_cprs_det = target.copy_random_state(source_det, matching="name",
                                               copy_determinism=True)
    images_aug_source1 = source_det.augment_images(images)
    images_aug_target1 = target_cprs_det.augment_images(images)
    images_aug_source2 = source_det.augment_images(images)
    images_aug_target2 = target_cprs_det.augment_images(images)
    assert np.array_equal(images_aug_source1, images_aug_source2)
    assert np.array_equal(images_aug_target1, images_aug_target2)
    assert np.array_equal(images_aug_source1, images_aug_target1)
    assert np.array_equal(images_aug_source2, images_aug_target2)


def test_parameters_Biomial():
    reseed()
    eps = np.finfo(np.float32).eps

    param = iap.Binomial(0)
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert sample == 0
    assert np.all(samples == 0)

    param = iap.Binomial(1.0)
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert sample == 1
    assert np.all(samples == 1)

    param = iap.Binomial(0.5)
    sample = param.draw_sample()
    samples = param.draw_samples((10000))
    assert sample.shape == tuple()
    assert samples.shape == (10000,)
    assert sample in [0, 1]
    unique, counts = np.unique(samples, return_counts=True)
    assert len(unique) == 2
    for val, count in zip(unique, counts):
        if val == 0:
            assert 5000 - 500 < count < 5000 + 500
        elif val == 1:
            assert 5000 - 500 < count < 5000 + 500
        else:
            assert False

    param = iap.Binomial(iap.Choice([0.25, 0.75]))
    for _ in sm.xrange(10):
        samples = param.draw_samples((1000,))
        p = np.sum(samples) / samples.size
        assert (0.25 - 0.05 < p < 0.25 + 0.05) or (0.75 - 0.05 < p < 0.75 + 0.05)

    param = iap.Binomial((0.0, 1.0))
    last_p = 0.5
    diffs = []
    for _ in sm.xrange(30):
        samples = param.draw_samples((1000,))
        p = np.sum(samples).astype(np.float32) / samples.size
        diffs.append(abs(p - last_p))
        last_p = p
    nb_p_changed = sum([diff > 0.05 for diff in diffs])
    assert nb_p_changed > 15

    param = iap.Binomial(0.5)
    samples1 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    samples2 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    assert np.array_equal(samples1, samples2)


def test_parameters_Choice():
    reseed()
    eps = np.finfo(np.float32).eps

    param = iap.Choice([0, 1, 2])
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert sample in [0, 1, 2]
    assert np.all(np.logical_or(np.logical_or(samples == 0, samples == 1), samples==2))

    samples = param.draw_samples((10000,))
    expected = 10000/3
    expected_tolerance = expected * 0.05
    for v in [0, 1, 2]:
        count = np.sum(samples == v)
        assert expected - expected_tolerance < count < expected + expected_tolerance

    param = iap.Choice([-1, 1])
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert sample in [-1, 1]
    assert np.all(np.logical_or(samples == -1, samples == 1))

    param = iap.Choice([-1.2, 1.7])
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert -1.2 - eps < sample < -1.2 + eps or 1.7 - eps < sample < 1.7 + eps
    assert np.all(
        np.logical_or(
            np.logical_or(-1.2 - eps < samples, samples < -1.2 + eps),
            np.logical_or(1.7 - eps < samples, samples < 1.7 + eps)
        )
    )

    param = iap.Choice(["first", "second", "third"])
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert sample in ["first", "second", "third"]
    assert np.all(
        np.logical_or(
            np.logical_or(
                samples == "first",
                samples == "second"
            ),
            samples == "third"
        )
    )

    param = iap.Choice([1+i for i in sm.xrange(100)], replace=False)
    samples = param.draw_samples((50,))
    seen = [0 for _ in sm.xrange(100)]
    for sample in samples:
        seen[sample-1] += 1
    assert all([count in [0, 1] for count in seen])

    param = iap.Choice([0, 1], p=[0.25, 0.75])
    samples = param.draw_samples((10000,))
    unique, counts = np.unique(samples, return_counts=True)
    assert len(unique) == 2
    for val, count in zip(unique, counts):
        if val == 0:
            assert 2500 - 500 < count < 2500 + 500
        elif val == 1:
            assert 7500 - 500 < count < 7500 + 500
        else:
            assert False

    param = iap.Choice([iap.Choice([0, 1]), 2])
    samples = param.draw_samples((10000,))
    unique, counts = np.unique(samples, return_counts=True)
    assert len(unique) == 3
    for val, count in zip(unique, counts):
        if val in [0, 1]:
            assert 2500 - 500 < count < 2500 + 500
        elif val == 2:
            assert 5000 - 500 < count < 5000 + 500
        else:
            assert False

    param = iap.Choice([-1, 0, 1, 2, 3])
    samples1 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    samples2 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    assert np.array_equal(samples1, samples2)


def test_parameters_DiscreteUniform():
    reseed()
    eps = np.finfo(np.float32).eps

    param = iap.DiscreteUniform(0, 2)
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert sample in [0, 1, 2]
    assert np.all(np.logical_or(np.logical_or(samples == 0, samples == 1), samples==2))

    samples = param.draw_samples((10000,))
    expected = 10000/3
    expected_tolerance = expected * 0.05
    for v in [0, 1, 2]:
        count = np.sum(samples == v)
        assert expected - expected_tolerance < count < expected + expected_tolerance

    param = iap.DiscreteUniform(-1, 1)
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert sample in [-1, 0, 1]
    assert np.all(np.logical_or(np.logical_or(samples == -1, samples == 0), samples==1))

    param = iap.DiscreteUniform(-1.2, 1.2)
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert sample in [-1, 0, 1]
    assert np.all(np.logical_or(np.logical_or(samples == -1, samples == 0), samples==1))

    param = iap.DiscreteUniform(1, -1)
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert sample in [-1, 0, 1]
    assert np.all(np.logical_or(np.logical_or(samples == -1, samples == 0), samples==1))

    param = iap.Uniform(-1, 1)
    samples1 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    samples2 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    assert np.array_equal(samples1, samples2)


def test_parameters_Poisson():
    reseed()
    eps = np.finfo(np.float32).eps

    param = iap.Poisson(1)
    sample = param.draw_sample()
    samples = param.draw_samples((100, 1000))
    samples_direct = np.random.RandomState(1234).poisson(lam=1, size=(100, 1000))
    assert sample.shape == tuple()
    assert samples.shape == (100, 1000)
    assert 0 < sample

    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        count_direct = np.sum(samples_direct == i)
        count = np.sum(samples == i)
        tolerance = max(count_direct * 0.1, 250)
        assert count_direct - tolerance < count < count_direct + tolerance

    param = iap.Poisson(1)
    samples1 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    samples2 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    assert np.array_equal(samples1, samples2)


def test_parameters_Normal():
    reseed()

    param = iap.Normal(0, 1)
    sample = param.draw_sample()
    samples = param.draw_samples((100, 1000))
    samples_direct = np.random.RandomState(1234).normal(loc=0, scale=1, size=(100, 1000))
    assert sample.shape == tuple()
    assert samples.shape == (100, 1000)

    samples = np.clip(samples, -1, 1)
    samples_direct = np.clip(samples_direct, -1, 1)
    nb_bins = 10
    hist, _ = np.histogram(samples, bins=nb_bins, range=(-1.0, 1.0), density=False)
    hist_direct, _ = np.histogram(samples_direct, bins=nb_bins, range=(-1.0, 1.0), density=False)
    tolerance = 0.05
    for nb_samples, nb_samples_direct in zip(hist, hist_direct):
        density = nb_samples / samples.size
        density_direct = nb_samples_direct / samples_direct.size
        assert density_direct - tolerance < density < density_direct + tolerance

    param = iap.Normal(iap.Choice([-100, 100]), 1)
    seen = [0, 0]
    for _ in sm.xrange(1000):
        samples = param.draw_samples((100,))
        exp = np.mean(samples)

        if -100 - 10 < exp < -100 + 10:
            seen[0] += 1
        elif 100 - 10 < exp < 100 + 10:
            seen[1] += 1
        else:
            assert False

    assert 500 - 100 < seen[0] < 500 + 100
    assert 500 - 100 < seen[1] < 500 + 100

    param1 = iap.Normal(0, 1)
    param2 = iap.Normal(0, 100)
    samples1 = param1.draw_samples((1000,))
    samples2 = param2.draw_samples((1000,))
    assert np.std(samples1) < np.std(samples2)
    assert 100 - 10 < np.std(samples2) < 100 + 10

    param = iap.Normal(0, 1)
    samples1 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    samples2 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    assert np.allclose(samples1, samples2)


def test_parameters_Laplace():
    reseed()

    param = iap.Laplace(0, 1)
    sample = param.draw_sample()
    samples = param.draw_samples((100, 1000))
    samples_direct = np.random.RandomState(1234).laplace(loc=0, scale=1, size=(100, 1000))
    assert sample.shape == tuple()
    assert samples.shape == (100, 1000)

    samples = np.clip(samples, -1, 1)
    samples_direct = np.clip(samples_direct, -1, 1)
    nb_bins = 10
    hist, _ = np.histogram(samples, bins=nb_bins, range=(-1.0, 1.0), density=False)
    hist_direct, _ = np.histogram(samples_direct, bins=nb_bins, range=(-1.0, 1.0), density=False)
    tolerance = 0.05
    for nb_samples, nb_samples_direct in zip(hist, hist_direct):
        density = nb_samples / samples.size
        density_direct = nb_samples_direct / samples_direct.size
        assert density_direct - tolerance < density < density_direct + tolerance

    param = iap.Laplace(iap.Choice([-100, 100]), 1)
    seen = [0, 0]
    for _ in sm.xrange(1000):
        samples = param.draw_samples((100,))
        exp = np.mean(samples)

        if -100 - 10 < exp < -100 + 10:
            seen[0] += 1
        elif 100 - 10 < exp < 100 + 10:
            seen[1] += 1
        else:
            assert False

    assert 500 - 100 < seen[0] < 500 + 100
    assert 500 - 100 < seen[1] < 500 + 100

    param1 = iap.Laplace(0, 1)
    param2 = iap.Laplace(0, 100)
    samples1 = param1.draw_samples((1000,))
    samples2 = param2.draw_samples((1000,))
    assert np.var(samples1) < np.var(samples2)

    param = iap.Laplace(0, 1)
    samples1 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    samples2 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    assert np.allclose(samples1, samples2)


def test_parameters_ChiSquare():
    reseed()

    param = iap.ChiSquare(1)
    sample = param.draw_sample()
    samples = param.draw_samples((100, 1000))
    samples_direct = np.random.RandomState(1234).chisquare(df=1, size=(100, 1000))
    assert sample.shape == tuple()
    assert samples.shape == (100, 1000)
    assert 0 <= sample
    assert np.all(0 <= samples)

    samples = np.clip(samples, 0, 3)
    samples_direct = np.clip(samples_direct, 0, 3)
    nb_bins = 10
    hist, _ = np.histogram(samples, bins=nb_bins, range=(0, 3.0), density=False)
    hist_direct, _ = np.histogram(samples_direct, bins=nb_bins, range=(0, 3.0), density=False)
    tolerance = 0.05
    for nb_samples, nb_samples_direct in zip(hist, hist_direct):
        density = nb_samples / samples.size
        density_direct = nb_samples_direct / samples_direct.size
        assert density_direct - tolerance < density < density_direct + tolerance

    param = iap.ChiSquare(iap.Choice([1, 10]))
    seen = [0, 0]
    for _ in sm.xrange(1000):
        samples = param.draw_samples((100,))
        exp = np.mean(samples)

        if 1 - 1.0 < exp < 1 + 1.0:
            seen[0] += 1
        elif 10 - 4.0 < exp < 10 + 4.0:
            seen[1] += 1
        else:
            assert False

    assert 500 - 100 < seen[0] < 500 + 100
    assert 500 - 100 < seen[1] < 500 + 100

    param1 = iap.ChiSquare(1)
    param2 = iap.ChiSquare(10)
    samples1 = param1.draw_samples((1000,))
    samples2 = param2.draw_samples((1000,))
    assert np.var(samples1) < np.var(samples2)
    assert 2*1 - 1.0 < np.var(samples1) < 2*1 + 1.0
    assert 2*10 - 5.0 < np.var(samples2) < 2*10 + 5.0

    param = iap.ChiSquare(1)
    samples1 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    samples2 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    assert np.allclose(samples1, samples2)


def test_parameters_Weibull():
    reseed()

    param = iap.Weibull(1)
    sample = param.draw_sample()
    samples = param.draw_samples((100, 1000))
    samples_direct = np.random.RandomState(1234).weibull(a=1, size=(100, 1000))
    assert sample.shape == tuple()
    assert samples.shape == (100, 1000)
    assert 0 <= sample
    assert np.all(0 <= samples)

    samples = np.clip(samples, 0, 2)
    samples_direct = np.clip(samples_direct, 0, 2)
    nb_bins = 10
    hist, _ = np.histogram(samples, bins=nb_bins, range=(0, 2.0), density=False)
    hist_direct, _ = np.histogram(samples_direct, bins=nb_bins, range=(0, 2.0), density=False)
    tolerance = 0.05
    for nb_samples, nb_samples_direct in zip(hist, hist_direct):
        density = nb_samples / samples.size
        density_direct = nb_samples_direct / samples_direct.size
        assert density_direct - tolerance < density < density_direct + tolerance

    param = iap.Weibull(iap.Choice([1, 0.5]))
    expected_first = scipy.special.gamma(1 + 1/1)
    expected_second = scipy.special.gamma(1 + 1/0.5)
    seen = [0, 0]
    for _ in sm.xrange(100):
        samples = param.draw_samples((50000,))
        observed = np.mean(samples)

        if expected_first - 0.2 * expected_first < observed < expected_first + 0.2 * expected_first:
            seen[0] += 1
        elif expected_second - 0.2 * expected_second < observed < expected_second + 0.2 * expected_second:
            seen[1] += 1
        else:
            assert False

    assert 50 - 25 < seen[0] < 50 + 25
    assert 50 - 25 < seen[1] < 50 + 25

    param1 = iap.Weibull(1)
    param2 = iap.Weibull(0.5)
    samples1 = param1.draw_samples((10000,))
    samples2 = param2.draw_samples((10000,))
    assert np.var(samples1) < np.var(samples2)
    expected_first = scipy.special.gamma(1 + 2/1) - (scipy.special.gamma(1 + 1/1))**2
    expected_second = scipy.special.gamma(1 + 2/0.5) - (scipy.special.gamma(1 + 1/0.5))**2
    assert expected_first - 0.2 * expected_first < np.var(samples1) < expected_first + 0.2 * expected_first
    assert expected_second - 0.2 * expected_second < np.var(samples2) < expected_second + 0.2 * expected_second

    param = iap.Weibull(1)
    samples1 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    samples2 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    assert np.allclose(samples1, samples2)


def test_parameters_Uniform():
    reseed()
    eps = np.finfo(np.float32).eps

    param = iap.Uniform(0, 1.0)
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert 0 - eps < sample < 1.0 + eps
    assert np.all(np.logical_or(0 - eps < samples, samples < 1.0 + eps))

    samples = param.draw_samples((10000,))
    nb_bins = 10
    hist, _ = np.histogram(samples, bins=nb_bins, range=(0.0, 1.0), density=False)
    density_expected = 1.0/nb_bins
    density_tolerance = 0.05
    for nb_samples in hist:
        density = nb_samples / samples.size
        assert density_expected - density_tolerance < density < density_expected + density_tolerance

    param = iap.Uniform(-1.0, 1.0)
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert -1.0 - eps < sample < 1.0 + eps
    assert np.all(np.logical_or(-1.0 - eps < samples, samples < 1.0 + eps))

    param = iap.Uniform(1.0, -1.0)
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert -1.0 - eps < sample < 1.0 + eps
    assert np.all(np.logical_or(-1.0 - eps < samples, samples < 1.0 + eps))

    param = iap.Uniform(-1, 1)
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert -1.0 - eps < sample < 1.0 + eps
    assert np.all(np.logical_or(0 - eps < samples, samples < 1.0 + eps))

    param = iap.Uniform(-1.0, 1.0)
    samples1 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    samples2 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    assert np.allclose(samples1, samples2)


def test_parameters_Beta():
    def _mean(alpha, beta):
        return alpha / (alpha + beta)

    def _var(alpha, beta):
        return (alpha * beta) / ((alpha + beta)**2 * (alpha + beta + 1))

    reseed()
    eps = np.finfo(np.float32).eps

    param = iap.Beta(0.5, 0.5)
    sample = param.draw_sample()
    samples = param.draw_samples((100, 1000))
    samples_direct = np.random.RandomState(1234).beta(a=0.5, b=0.5, size=(100, 1000))
    assert sample.shape == tuple()
    assert samples.shape == (100, 1000)
    assert 0 - eps < sample < 1.0 + eps
    assert np.all(np.logical_or(0 - eps <= samples, samples <= 1.0 + eps))

    nb_bins = 10
    hist, _ = np.histogram(samples, bins=nb_bins, range=(0, 1.0), density=False)
    hist_direct, _ = np.histogram(samples_direct, bins=nb_bins, range=(0, 1.0), density=False)
    tolerance = 0.05
    for nb_samples, nb_samples_direct in zip(hist, hist_direct):
        density = nb_samples / samples.size
        density_direct = nb_samples_direct / samples_direct.size
        assert density_direct - tolerance < density < density_direct + tolerance

    param = iap.Beta(iap.Choice([0.5, 2]), 0.5)
    expected_first = _mean(0.5, 0.5)
    expected_second = _mean(2, 0.5)
    seen = [0, 0]
    for _ in sm.xrange(100):
        samples = param.draw_samples((10000,))
        observed = np.mean(samples)

        if expected_first - 0.05 < observed < expected_first + 0.05:
            seen[0] += 1
        elif expected_second - 0.05 < observed < expected_second + 0.05:
            seen[1] += 1
        else:
            assert False

    assert 50 - 25 < seen[0] < 50 + 25
    assert 50 - 25 < seen[1] < 50 + 25

    param1 = iap.Beta(2, 2)
    param2 = iap.Beta(0.5, 0.5)
    samples1 = param1.draw_samples((10000,))
    samples2 = param2.draw_samples((10000,))
    assert np.var(samples1) < np.var(samples2)
    expected_first = _var(2, 2)
    expected_second = _var(0.5, 0.5)
    assert expected_first - 0.1 * expected_first < np.var(samples1) < expected_first + 0.1 * expected_first
    assert expected_second - 0.1 * expected_second < np.var(samples2) < expected_second + 0.1 * expected_second

    param = iap.Beta(0.5, 0.5)
    samples1 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    samples2 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    assert np.allclose(samples1, samples2)


def test_parameters_Deterministic():
    reseed()
    eps = np.finfo(np.float32).eps

    values_int = [-100, -54, -1, 0, 1, 54, 100]
    values_float = [-100.0, -54.3, -1.0, 0.1, 0.0, 0.1, 1.0, 54.4, 100.0]

    for value in values_int:
        param = iap.Deterministic(value)

        sample1 = param.draw_sample()
        sample2 = param.draw_sample()
        assert sample1.shape == tuple()
        assert sample1 == sample2

        samples1 = param.draw_samples(10)
        samples2 = param.draw_samples(10)
        samples3 = param.draw_samples((5, 3))
        samples4 = param.draw_samples((5, 3))
        samples5 = param.draw_samples((4, 5, 3))
        samples6 = param.draw_samples((4, 5, 3))

        samples1_unique = np.unique(samples1)
        samples2_unique = np.unique(samples2)
        samples3_unique = np.unique(samples3)
        samples4_unique = np.unique(samples4)
        samples5_unique = np.unique(samples5)
        samples6_unique = np.unique(samples6)

        assert samples1.shape == (10,)
        assert samples2.shape == (10,)
        assert samples3.shape == (5, 3)
        assert samples4.shape == (5, 3)
        assert samples5.shape == (4, 5, 3)
        assert samples6.shape == (4, 5, 3)
        assert len(samples1_unique) == 1 and samples1_unique[0] == value
        assert len(samples2_unique) == 1 and samples2_unique[0] == value
        assert len(samples3_unique) == 1 and samples3_unique[0] == value
        assert len(samples4_unique) == 1 and samples4_unique[0] == value
        assert len(samples5_unique) == 1 and samples5_unique[0] == value
        assert len(samples6_unique) == 1 and samples6_unique[0] == value

        rs1 = np.random.RandomState(123456)
        rs2 = np.random.RandomState(123456)
        assert np.array_equal(
            param.draw_samples(20, random_state=rs1),
            param.draw_samples(20, random_state=rs2)
        )

    for value in values_float:
        param = iap.Deterministic(value)

        sample1 = param.draw_sample()
        sample2 = param.draw_sample()
        assert sample1.shape == tuple()
        assert sample1 - eps < sample2 < sample1 + eps

        samples1 = param.draw_samples(10)
        samples2 = param.draw_samples(10)
        samples3 = param.draw_samples((5, 3))
        samples4 = param.draw_samples((5, 3))
        samples5 = param.draw_samples((4, 5, 3))
        samples6 = param.draw_samples((4, 5, 3))

        samples1_sorted = np.sort(samples1)
        samples2_sorted = np.sort(samples2)
        samples3_sorted = np.sort(samples3.flatten())
        samples4_sorted = np.sort(samples4.flatten())
        samples5_sorted = np.sort(samples5.flatten())
        samples6_sorted = np.sort(samples6.flatten())

        assert samples1.shape == (10,)
        assert samples2.shape == (10,)
        assert samples3.shape == (5, 3)
        assert samples4.shape == (5, 3)
        assert samples5.shape == (4, 5, 3)
        assert samples6.shape == (4, 5, 3)
        assert samples1_sorted[0] - eps < samples1_sorted[-1] < samples1_sorted[0] + eps
        assert samples2_sorted[0] - eps < samples2_sorted[-1] < samples2_sorted[0] + eps
        assert samples3_sorted[0] - eps < samples3_sorted[-1] < samples3_sorted[0] + eps
        assert samples4_sorted[0] - eps < samples4_sorted[-1] < samples4_sorted[0] + eps
        assert samples5_sorted[0] - eps < samples5_sorted[-1] < samples5_sorted[0] + eps
        assert samples6_sorted[0] - eps < samples6_sorted[-1] < samples6_sorted[0] + eps

        rs1 = np.random.RandomState(123456)
        rs2 = np.random.RandomState(123456)
        assert np.allclose(
            param.draw_samples(20, random_state=rs1),
            param.draw_samples(20, random_state=rs2)
        )


def test_parameters_FromLowerResolution():
    reseed()
    eps = np.finfo(np.float32).eps

    param = iap.FromLowerResolution(iap.Binomial(0.5), size_px=8)
    samples = param.draw_samples((8, 8, 1))
    assert samples.shape == (8, 8, 1)
    uq = np.unique(samples)
    assert len(uq) == 2 and (0 in uq or 1 in uq)

    param = iap.FromLowerResolution(iap.Binomial(0.5), size_px=8)
    samples = param.draw_samples((8, 8, 3))
    assert samples.shape == (8, 8, 3)
    uq = np.unique(samples)
    assert len(uq) == 2 and (0 in uq or 1 in uq)

    param1 = iap.FromLowerResolution(iap.Binomial(0.5), size_px=2)
    param2 = iap.FromLowerResolution(iap.Binomial(0.5), size_px=16)
    seen_components = [0, 0]
    seen_pixels = [0, 0]
    for _ in sm.xrange(100):
        samples1 = param1.draw_samples((16, 16, 1))
        samples2 = param2.draw_samples((16, 16, 1))
        _, num1 = skimage.morphology.label(samples1, neighbors=4, background=0, return_num=True)
        _, num2 = skimage.morphology.label(samples2, neighbors=4, background=0, return_num=True)
        seen_components[0] += num1
        seen_components[1] += num2
        seen_pixels[0] += np.sum(samples1 == 1)
        seen_pixels[1] += np.sum(samples2 == 1)

    assert seen_components[0] < seen_components[1]
    assert seen_pixels[0] / seen_components[0] > seen_pixels[1] / seen_components[1]

    param1 = iap.FromLowerResolution(iap.Binomial(0.5), size_px=2)
    param2 = iap.FromLowerResolution(iap.Binomial(0.5), size_px=1, min_size=16)
    seen_components = [0, 0]
    seen_pixels = [0, 0]
    for _ in sm.xrange(100):
        samples1 = param1.draw_samples((16, 16, 1))
        samples2 = param2.draw_samples((16, 16, 1))
        _, num1 = skimage.morphology.label(samples1, neighbors=4, background=0, return_num=True)
        _, num2 = skimage.morphology.label(samples2, neighbors=4, background=0, return_num=True)
        seen_components[0] += num1
        seen_components[1] += num2
        seen_pixels[0] += np.sum(samples1 == 1)
        seen_pixels[1] += np.sum(samples2 == 1)

    assert seen_components[0] < seen_components[1]
    assert seen_pixels[0] / seen_components[0] > seen_pixels[1] / seen_components[1]

    param1 = iap.FromLowerResolution(iap.Binomial(0.5), size_percent=0.01)
    param2 = iap.FromLowerResolution(iap.Binomial(0.5), size_percent=0.8)
    seen_components = [0, 0]
    seen_pixels = [0, 0]
    for _ in sm.xrange(100):
        samples1 = param1.draw_samples((16, 16, 1))
        samples2 = param2.draw_samples((16, 16, 1))
        _, num1 = skimage.morphology.label(samples1, neighbors=4, background=0, return_num=True)
        _, num2 = skimage.morphology.label(samples2, neighbors=4, background=0, return_num=True)
        seen_components[0] += num1
        seen_components[1] += num2
        seen_pixels[0] += np.sum(samples1 == 1)
        seen_pixels[1] += np.sum(samples2 == 1)

    assert seen_components[0] < seen_components[1]
    assert seen_pixels[0] / seen_components[0] > seen_pixels[1] / seen_components[1]

    param = iap.FromLowerResolution(iap.Binomial(0.5), size_px=2)
    samples1 = param.draw_samples((10, 5, 1), random_state=np.random.RandomState(1234))
    samples2 = param.draw_samples((10, 5, 1), random_state=np.random.RandomState(1234))
    assert np.allclose(samples1, samples2)


def test_parameters_Clip():
    reseed()
    eps = np.finfo(np.float32).eps

    param = iap.Clip(iap.Deterministic(0), -1, 1)
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert sample == 0
    assert np.all(samples == 0)

    param = iap.Clip(iap.Deterministic(1), -1, 1)
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert sample == 1
    assert np.all(samples == 1)

    param = iap.Clip(iap.Deterministic(-1), -1, 1)
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert sample == -1
    assert np.all(samples == -1)

    param = iap.Clip(iap.Deterministic(0.5), -1, 1)
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert 0.5 - eps < sample < 0.5 + eps
    assert np.all(np.logical_or(0.5 - eps < samples, samples < 0.5 + eps))

    param = iap.Clip(iap.Deterministic(2), -1, 1)
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert sample == 1
    assert np.all(samples == 1)

    param = iap.Clip(iap.Deterministic(-2), -1, 1)
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert sample == -1
    assert np.all(samples == -1)

    param = iap.Clip(iap.Choice([0, 2]), -1, 1)
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert sample in [0, 1]
    assert np.all(np.logical_or(samples == 0, samples == 1))

    samples1 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    samples2 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    assert np.array_equal(samples1, samples2)


def test_parameters_Discretize():
    reseed()
    eps = np.finfo(np.float32).eps

    values = [-100.2, -54.3, -1.0, -1, -0.7, -0.00043, 0, 0.00043, 0.7, 1.0, 1, 54.3, 100.2]
    for value in values:
        value_expected = np.round(np.float64([value])).astype(np.int32)[0]
        param = iap.Discretize(iap.Deterministic(value))
        sample = param.draw_sample()
        samples = param.draw_samples((10, 5))
        assert sample.shape == tuple()
        assert samples.shape == (10, 5)
        assert sample == value_expected
        assert np.all(samples == value_expected)

    param_orig = iap.DiscreteUniform(0, 1)
    param = iap.Discretize(param_orig)
    sample = param.draw_sample()
    samples = param.draw_samples((10, 5))
    assert sample.shape == tuple()
    assert samples.shape == (10, 5)
    assert sample in [0, 1]
    assert np.all(np.logical_or(samples == 0, samples == 1))

    param_orig = iap.DiscreteUniform(0, 2)
    param = iap.Discretize(param_orig)
    samples1 = param_orig.draw_samples((10000,))
    samples2 = param.draw_samples((10000,))
    assert np.all(np.abs(samples1 - samples2) < 0.2*(10000/3))

    param_orig = iap.DiscreteUniform(0, 2)
    param = iap.Discretize(param_orig)
    samples1 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    samples2 = param.draw_samples((10, 5), random_state=np.random.RandomState(1234))
    assert np.array_equal(samples1, samples2)


def test_parameters_Multiply():
    reseed()
    eps = np.finfo(np.float32).eps

    values_int = [-100, -54, -1, 0, 1, 54, 100]
    values_float = [-100.0, -54.3, -1.0, 0.1, 0.0, 0.1, 1.0, 54.4, 100.0]

    for v1 in values_int:
        for v2 in values_int:
            p = iap.Multiply(iap.Deterministic(v1), v2)
            assert p.draw_sample() == v1 * v2
            samples = p.draw_samples((2, 3))
            assert samples.dtype == np.int64
            assert np.array_equal(samples, np.zeros((2, 3), dtype=np.int64) + v1 * v2)

            p = iap.Multiply(iap.Deterministic(v1), iap.Deterministic(v2))
            assert p.draw_sample() == v1 * v2
            samples = p.draw_samples((2, 3))
            assert samples.dtype == np.int64
            assert np.array_equal(samples, np.zeros((2, 3), dtype=np.int64) + v1 * v2)

    for v1 in values_float:
        for v2 in values_float:
            p = iap.Multiply(iap.Deterministic(v1), v2)
            assert v1 * v2 - eps < p.draw_sample() < v1 * v2 + eps
            samples = p.draw_samples((2, 3))
            assert samples.dtype == np.float64
            assert np.allclose(samples, np.zeros((2, 3), dtype=np.float64) + v1 * v2)

            p = iap.Multiply(iap.Deterministic(v1), iap.Deterministic(v2))
            assert v1 * v2 - eps < p.draw_sample() < v1 * v2 + eps
            samples = p.draw_samples((2, 3))
            assert samples.dtype == np.float64
            assert np.allclose(samples, np.zeros((2, 3), dtype=np.float64) + v1 * v2)

    param = iap.Multiply(iap.Deterministic(1.0), (1.0, 2.0), elementwise=False)
    samples = param.draw_samples((10, 20))
    assert samples.shape == (10, 20)
    assert np.all(samples > 1.0 * 1.0 - eps)
    assert np.all(samples < 1.0 * 2.0 + eps)
    samples_sorted = np.sort(samples.flatten())
    assert samples_sorted[0] - eps < samples_sorted[-1] < samples_sorted[0] + eps

    param = iap.Multiply(iap.Deterministic(1.0), (1.0, 2.0), elementwise=True)
    samples = param.draw_samples((10, 20))
    assert samples.shape == (10, 20)
    assert np.all(samples > 1.0 * 1.0 - eps)
    assert np.all(samples < 1.0 * 2.0 + eps)
    samples_sorted = np.sort(samples.flatten())
    assert not (samples_sorted[0] - eps < samples_sorted[-1] < samples_sorted[0] + eps)

    param = iap.Multiply(iap.Uniform(1.0, 2.0), 1.0, elementwise=False)
    samples = param.draw_samples((10, 20))
    assert samples.shape == (10, 20)
    assert np.all(samples > 1.0 * 1.0 - eps)
    assert np.all(samples < 2.0 * 1.0 + eps)
    samples_sorted = np.sort(samples.flatten())
    assert not (samples_sorted[0] - eps < samples_sorted[-1] < samples_sorted[0] + eps)

    param = iap.Multiply(iap.Uniform(1.0, 2.0), 1.0, elementwise=True)
    samples = param.draw_samples((10, 20))
    assert samples.shape == (10, 20)
    assert np.all(samples > 1.0 * 1.0 - eps)
    assert np.all(samples < 2.0 * 1.0 + eps)
    samples_sorted = np.sort(samples.flatten())
    assert not (samples_sorted[0] - eps < samples_sorted[-1] < samples_sorted[0] + eps)


def test_parameters_Divide():
    reseed()
    eps = np.finfo(np.float32).eps

    values_int = [-100, -54, -1, 0, 1, 54, 100]
    values_float = [-100.0, -54.3, -1.0, 0.1, 0.0, 0.1, 1.0, 54.4, 100.0]

    for v1 in values_int:
        for v2 in values_int:
            if v2 == 0:
                v2 = 1

            p = iap.Divide(iap.Deterministic(v1), v2)
            assert p.draw_sample() == v1 / v2
            samples = p.draw_samples((2, 3))
            assert samples.dtype == np.float64
            assert np.array_equal(samples, np.zeros((2, 3), dtype=np.float64) + v1 / v2)

            p = iap.Divide(iap.Deterministic(v1), iap.Deterministic(v2))
            assert p.draw_sample() == v1 / v2
            samples = p.draw_samples((2, 3))
            assert samples.dtype == np.float64
            assert np.array_equal(samples, np.zeros((2, 3), dtype=np.float64) + v1 / v2)

    for v1 in values_float:
        for v2 in values_float:
            if v2 == 0:
                v2 = 1

            p = iap.Divide(iap.Deterministic(v1), v2)
            assert v1 / v2 - eps < p.draw_sample() < v1 / v2 + eps
            samples = p.draw_samples((2, 3))
            assert samples.dtype == np.float64
            assert np.allclose(samples, np.zeros((2, 3), dtype=np.float64) + v1 / v2)

            p = iap.Divide(iap.Deterministic(v1), iap.Deterministic(v2))
            assert v1 / v2 - eps < p.draw_sample() < v1 / v2 + eps
            samples = p.draw_samples((2, 3))
            assert samples.dtype == np.float64
            assert np.allclose(samples, np.zeros((2, 3), dtype=np.float64) + v1 / v2)

    param = iap.Divide(iap.Deterministic(1.0), (1.0, 2.0), elementwise=False)
    samples = param.draw_samples((10, 20))
    assert samples.shape == (10, 20)
    assert np.all(samples > 1.0 / 2.0 - eps)
    assert np.all(samples < 1.0 / 1.0 + eps)
    samples_sorted = np.sort(samples.flatten())
    assert samples_sorted[0] - eps < samples_sorted[-1] < samples_sorted[0] + eps

    param = iap.Divide(iap.Deterministic(1.0), (1.0, 2.0), elementwise=True)
    samples = param.draw_samples((10, 20))
    assert samples.shape == (10, 20)
    assert np.all(samples > 1.0 / 2.0 - eps)
    assert np.all(samples < 1.0 / 1.0 + eps)
    samples_sorted = np.sort(samples.flatten())
    assert not (samples_sorted[0] - eps < samples_sorted[-1] < samples_sorted[0] + eps)

    param = iap.Divide(iap.Uniform(1.0, 2.0), 1.0, elementwise=False)
    samples = param.draw_samples((10, 20))
    assert samples.shape == (10, 20)
    assert np.all(samples > 1.0 / 1.0 - eps)
    assert np.all(samples < 2.0 / 1.0 + eps)
    samples_sorted = np.sort(samples.flatten())
    assert not (samples_sorted[0] - eps < samples_sorted[-1] < samples_sorted[0] + eps)

    param = iap.Divide(iap.Uniform(1.0, 2.0), 1.0, elementwise=True)
    samples = param.draw_samples((10, 20))
    assert samples.shape == (10, 20)
    assert np.all(samples > 1.0 / 1.0 - eps)
    assert np.all(samples < 2.0 / 1.0 + eps)
    samples_sorted = np.sort(samples.flatten())
    assert not (samples_sorted[0] - eps < samples_sorted[-1] < samples_sorted[0] + eps)

    # test division by zero automatically being converted to division by 1
    param = iap.Divide(2, iap.Choice([0, 2]), elementwise=True)
    samples = param.draw_samples((10, 20))
    samples_unique = np.sort(np.unique(samples.flatten()))
    assert samples_unique[0] == 1 and samples_unique[1] == 2


def test_parameters_Add():
    reseed()
    eps = np.finfo(np.float32).eps

    values_int = [-100, -54, -1, 0, 1, 54, 100]
    values_float = [-100.0, -54.3, -1.0, 0.1, 0.0, 0.1, 1.0, 54.4, 100.0]

    for v1 in values_int:
        for v2 in values_int:
            p = iap.Add(iap.Deterministic(v1), v2)
            assert p.draw_sample() == v1 + v2
            samples = p.draw_samples((2, 3))
            assert samples.dtype == np.int64
            assert np.array_equal(samples, np.zeros((2, 3), dtype=np.int64) + v1 + v2)

            p = iap.Add(iap.Deterministic(v1), iap.Deterministic(v2))
            assert p.draw_sample() == v1 + v2
            samples = p.draw_samples((2, 3))
            assert samples.dtype == np.int64
            assert np.array_equal(samples, np.zeros((2, 3), dtype=np.int64) + v1 + v2)

    for v1 in values_float:
        for v2 in values_float:
            p = iap.Add(iap.Deterministic(v1), v2)
            assert v1 + v2 - eps < p.draw_sample() < v1 + v2 + eps
            samples = p.draw_samples((2, 3))
            assert samples.dtype == np.float64
            assert np.allclose(samples, np.zeros((2, 3), dtype=np.float64) + v1 + v2)

            p = iap.Add(iap.Deterministic(v1), iap.Deterministic(v2))
            assert v1 + v2 - eps < p.draw_sample() < v1 + v2 + eps
            samples = p.draw_samples((2, 3))
            assert samples.dtype == np.float64
            assert np.allclose(samples, np.zeros((2, 3), dtype=np.float64) + v1 + v2)

    param = iap.Add(iap.Deterministic(1.0), (1.0, 2.0), elementwise=False)
    samples = param.draw_samples((10, 20))
    assert samples.shape == (10, 20)
    assert np.all(samples > 1.0 + 1.0 - eps)
    assert np.all(samples < 1.0 + 2.0 + eps)
    samples_sorted = np.sort(samples.flatten())
    assert samples_sorted[0] - eps < samples_sorted[-1] < samples_sorted[0] + eps

    param = iap.Add(iap.Deterministic(1.0), (1.0, 2.0), elementwise=True)
    samples = param.draw_samples((10, 20))
    assert samples.shape == (10, 20)
    assert np.all(samples > 1.0 + 1.0 - eps)
    assert np.all(samples < 1.0 + 2.0 + eps)
    samples_sorted = np.sort(samples.flatten())
    assert not (samples_sorted[0] - eps < samples_sorted[-1] < samples_sorted[0] + eps)

    param = iap.Add(iap.Uniform(1.0, 2.0), 1.0, elementwise=False)
    samples = param.draw_samples((10, 20))
    assert samples.shape == (10, 20)
    assert np.all(samples > 1.0 + 1.0 - eps)
    assert np.all(samples < 2.0 + 1.0 + eps)
    samples_sorted = np.sort(samples.flatten())
    assert not (samples_sorted[0] - eps < samples_sorted[-1] < samples_sorted[0] + eps)

    param = iap.Add(iap.Uniform(1.0, 2.0), 1.0, elementwise=True)
    samples = param.draw_samples((10, 20))
    assert samples.shape == (10, 20)
    assert np.all(samples > 1.0 + 1.0 - eps)
    assert np.all(samples < 2.0 + 1.0 + eps)
    samples_sorted = np.sort(samples.flatten())
    assert not (samples_sorted[0] - eps < samples_sorted[-1] < samples_sorted[0] + eps)


def test_parameters_Subtract():
    reseed()
    eps = np.finfo(np.float32).eps

    values_int = [-100, -54, -1, 0, 1, 54, 100]
    values_float = [-100.0, -54.3, -1.0, 0.1, 0.0, 0.1, 1.0, 54.4, 100.0]

    for v1 in values_int:
        for v2 in values_int:
            p = iap.Subtract(iap.Deterministic(v1), v2)
            assert p.draw_sample() == v1 - v2
            samples = p.draw_samples((2, 3))
            assert samples.dtype == np.int64
            assert np.array_equal(samples, np.zeros((2, 3), dtype=np.int64) + v1 - v2)

            p = iap.Subtract(iap.Deterministic(v1), iap.Deterministic(v2))
            assert p.draw_sample() == v1 - v2
            samples = p.draw_samples((2, 3))
            assert samples.dtype == np.int64
            assert np.array_equal(samples, np.zeros((2, 3), dtype=np.int64) + v1 - v2)

    for v1 in values_float:
        for v2 in values_float:
            p = iap.Subtract(iap.Deterministic(v1), v2)
            assert v1 - v2 - eps < p.draw_sample() < v1 - v2 + eps
            samples = p.draw_samples((2, 3))
            assert samples.dtype == np.float64
            assert np.allclose(samples, np.zeros((2, 3), dtype=np.float64) + v1 - v2)

            p = iap.Subtract(iap.Deterministic(v1), iap.Deterministic(v2))
            assert v1 - v2 - eps < p.draw_sample() < v1 - v2 + eps
            samples = p.draw_samples((2, 3))
            assert samples.dtype == np.float64
            assert np.allclose(samples, np.zeros((2, 3), dtype=np.float64) + v1 - v2)

    param = iap.Subtract(iap.Deterministic(1.0), (1.0, 2.0), elementwise=False)
    samples = param.draw_samples((10, 20))
    assert samples.shape == (10, 20)
    assert np.all(samples > 1.0 - 2.0 - eps)
    assert np.all(samples < 1.0 - 1.0 + eps)
    samples_sorted = np.sort(samples.flatten())
    assert samples_sorted[0] - eps < samples_sorted[-1] < samples_sorted[0] + eps

    param = iap.Subtract(iap.Deterministic(1.0), (1.0, 2.0), elementwise=True)
    samples = param.draw_samples((10, 20))
    assert samples.shape == (10, 20)
    assert np.all(samples > 1.0 - 2.0 - eps)
    assert np.all(samples < 1.0 - 1.0 + eps)
    samples_sorted = np.sort(samples.flatten())
    assert not (samples_sorted[0] - eps < samples_sorted[-1] < samples_sorted[0] + eps)

    param = iap.Subtract(iap.Uniform(1.0, 2.0), 1.0, elementwise=False)
    samples = param.draw_samples((10, 20))
    assert samples.shape == (10, 20)
    assert np.all(samples > 1.0 - 1.0 - eps)
    assert np.all(samples < 2.0 - 1.0 + eps)
    samples_sorted = np.sort(samples.flatten())
    assert not (samples_sorted[0] - eps < samples_sorted[-1] < samples_sorted[0] + eps)

    param = iap.Subtract(iap.Uniform(1.0, 2.0), 1.0, elementwise=True)
    samples = param.draw_samples((10, 20))
    assert samples.shape == (10, 20)
    assert np.all(samples > 1.0 - 1.0 - eps)
    assert np.all(samples < 2.0 - 1.0 + eps)
    samples_sorted = np.sort(samples.flatten())
    assert not (samples_sorted[0] - eps < samples_sorted[-1] < samples_sorted[0] + eps)


def test_parameters_Power():
    reseed()
    eps = np.finfo(np.float32).eps

    values = [-100, -54, -1, 0, 1, 54, 100]
    values = values + [float(v) for v in values]
    exponents = [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]

    for v1 in values:
        for v2 in exponents:
            if v1 < 0 and ia.is_single_float(v2):
                continue
            if v1 == 0 and v2 < 0:
                continue
            p = iap.Power(iap.Deterministic(v1), v2)
            assert v1 ** v2 - eps < p.draw_sample() < v1 ** v2 + eps
            samples = p.draw_samples((2, 3))
            assert samples.dtype == np.float64
            assert np.allclose(samples, np.zeros((2, 3), dtype=np.float64) + v1 ** v2)

            p = iap.Power(iap.Deterministic(v1), iap.Deterministic(v2))
            assert v1 ** v2 - eps < p.draw_sample() < v1 ** v2 + eps
            samples = p.draw_samples((2, 3))
            assert samples.dtype == np.float64
            assert np.allclose(samples, np.zeros((2, 3), dtype=np.float64) + v1 ** v2)

    param = iap.Power(iap.Deterministic(1.5), (1.0, 2.0), elementwise=False)
    samples = param.draw_samples((10, 20))
    assert samples.shape == (10, 20)
    assert np.all(samples > 1.5 ** 1.0 - eps)
    assert np.all(samples < 1.5 ** 2.0 + eps)
    samples_sorted = np.sort(samples.flatten())
    assert samples_sorted[0] - eps < samples_sorted[-1] < samples_sorted[0] + eps

    param = iap.Power(iap.Deterministic(1.5), (1.0, 2.0), elementwise=True)
    samples = param.draw_samples((10, 20))
    assert samples.shape == (10, 20)
    assert np.all(samples > 1.5 ** 1.0 - eps)
    assert np.all(samples < 1.5 ** 2.0 + eps)
    samples_sorted = np.sort(samples.flatten())
    assert not (samples_sorted[0] - eps < samples_sorted[-1] < samples_sorted[0] + eps)

    param = iap.Power(iap.Uniform(1.0, 2.0), 1.0, elementwise=False)
    samples = param.draw_samples((10, 20))
    assert samples.shape == (10, 20)
    assert np.all(samples > 1.0 ** 1.0 - eps)
    assert np.all(samples < 2.0 ** 1.0 + eps)
    samples_sorted = np.sort(samples.flatten())
    assert not (samples_sorted[0] - eps < samples_sorted[-1] < samples_sorted[0] + eps)

    param = iap.Power(iap.Uniform(1.0, 2.0), 1.0, elementwise=True)
    samples = param.draw_samples((10, 20))
    assert samples.shape == (10, 20)
    assert np.all(samples > 1.0 ** 1.0 - eps)
    assert np.all(samples < 2.0 ** 1.0 + eps)
    samples_sorted = np.sort(samples.flatten())
    assert not (samples_sorted[0] - eps < samples_sorted[-1] < samples_sorted[0] + eps)


def test_parameters_Absolute():
    reseed()
    eps = np.finfo(np.float32).eps

    simple_values = [-1.5, -1, -1.0, -0.1, 0, 0.0, 0.1, 1, 1.0, 1.5]

    for value in simple_values:
        param = iap.Absolute(iap.Deterministic(value))
        sample = param.draw_sample()
        samples = param.draw_samples((10, 5))
        assert sample.shape == tuple()
        assert samples.shape == (10, 5)
        if ia.is_single_float(value):
            assert abs(value) - eps < sample < abs(value) + eps
            assert np.all(abs(value) - eps < samples)
            assert np.all(samples < abs(value) + eps)
        else:
            assert sample == abs(value)
            assert np.all(samples == abs(value))

    param = iap.Absolute(iap.Choice([-3, -1, 1, 3]))
    sample = param.draw_sample()
    samples = param.draw_samples((10, 10))
    samples_uq = np.sort(np.unique(samples))
    assert sample.shape == tuple()
    assert sample in [3, 1]
    assert samples.shape == (10, 10)
    assert len(samples_uq) == 2
    assert samples_uq[0] == 1 and samples_uq[1] == 3


def test_parameters_RandomSign():
    reseed()

    param = iap.RandomSign(iap.Deterministic(1))
    samples = param.draw_samples((1000,))
    n_positive = np.sum(samples == 1)
    n_negative = np.sum(samples == -1)
    assert samples.shape == (1000,)
    assert n_positive + n_negative == 1000
    assert 350 < n_positive < 750

    seen = [0, 0]
    for _ in sm.xrange(1000):
        sample = param.draw_sample()
        assert sample.shape == tuple()
        if sample == 1:
            seen[1] += 1
        else:
            seen[0] += 1
    n_negative, n_positive = seen
    assert n_positive + n_negative == 1000
    assert 350 < n_positive < 750

    param = iap.RandomSign(iap.Choice([1, 2]))
    samples = param.draw_samples((4000,))
    seen = [0, 0, 0, 0]
    seen[0] = np.sum(samples == -2)
    seen[1] = np.sum(samples == -1)
    seen[2] = np.sum(samples == 1)
    seen[3] = np.sum(samples == 2)
    assert np.sum(seen) == 4000
    assert all([700 < v < 1300 for v in seen])

    param = iap.RandomSign(iap.Choice([1, 2]))
    samples1 = param.draw_samples((100, 10), random_state=np.random.RandomState(1234))
    samples2 = param.draw_samples((100, 10), random_state=np.random.RandomState(1234))
    assert samples1.shape == (100, 10)
    assert samples2.shape == (100, 10)
    assert np.array_equal(samples1, samples2)
    assert np.sum(samples == -2) > 50
    assert np.sum(samples == -1) > 50
    assert np.sum(samples == 1) > 50
    assert np.sum(samples == 2) > 50


def test_parameters_ForceSign():
    reseed()

    param = iap.ForceSign(iap.Deterministic(1), positive=True, mode="invert")
    sample = param.draw_sample()
    assert sample.shape == tuple()
    assert sample == 1

    param = iap.ForceSign(iap.Deterministic(1), positive=False, mode="invert")
    sample = param.draw_sample()
    assert sample.shape == tuple()
    assert sample == -1

    param = iap.ForceSign(iap.Deterministic(1), positive=True, mode="invert")
    samples = param.draw_samples(100)
    assert samples.shape == (100,)
    assert np.all(samples == 1)

    param = iap.ForceSign(iap.Deterministic(1), positive=False, mode="invert")
    samples = param.draw_samples(100)
    assert samples.shape == (100,)
    assert np.all(samples == -1)

    param = iap.ForceSign(iap.Deterministic(-1), positive=True, mode="invert")
    samples = param.draw_samples(100)
    assert samples.shape == (100,)
    assert np.all(samples == 1)

    param = iap.ForceSign(iap.Deterministic(-1), positive=False, mode="invert")
    samples = param.draw_samples(100)
    assert samples.shape == (100,)
    assert np.all(samples == -1)

    param = iap.ForceSign(iap.Choice([-2, 1]), positive=True, mode="invert")
    samples = param.draw_samples(1000)
    assert samples.shape == (1000,)
    n_twos = np.sum(samples == 2)
    n_ones = np.sum(samples == 1)
    assert n_twos + n_ones == 1000
    assert 200 < n_twos < 700
    assert 200 < n_ones < 700

    param = iap.ForceSign(iap.Choice([-2, 1]), positive=True, mode="reroll")
    samples = param.draw_samples(1000)
    assert samples.shape == (1000,)
    n_twos = np.sum(samples == 2)
    n_ones = np.sum(samples == 1)
    assert n_twos + n_ones == 1000
    assert n_twos > 0
    assert n_ones > 0

    param = iap.ForceSign(iap.Choice([-2, 1]), positive=True, mode="reroll", reroll_count_max=100)
    samples = param.draw_samples(100)
    assert samples.shape == (100,)
    n_twos = np.sum(samples == 2)
    n_ones = np.sum(samples == 1)
    assert n_twos + n_ones == 100
    assert n_twos < 5

    param = iap.ForceSign(iap.Choice([-2, 1]), positive=True, mode="invert")
    samples1 = param.draw_samples((100, 10), random_state=np.random.RandomState(1234))
    samples2 = param.draw_samples((100, 10), random_state=np.random.RandomState(1234))
    assert samples1.shape == (100, 10)
    assert samples2.shape == (100, 10)
    assert np.array_equal(samples1, samples2)


def test_parameters_Positive():
    reseed()

    param = iap.Positive(iap.Deterministic(-1), mode="reroll", reroll_count_max=1)
    samples = param.draw_samples((100,))
    assert samples.shape == (100,)
    assert np.all(samples == 1)


def test_parameters_Negative():
    reseed()

    param = iap.Negative(iap.Deterministic(1), mode="reroll", reroll_count_max=1)
    samples = param.draw_samples((100,))
    assert samples.shape == (100,)
    assert np.all(samples == -1)


def test_parameters_IterativeNoiseAggregator():
    reseed()
    eps = np.finfo(np.float32).eps

    param = iap.IterativeNoiseAggregator(iap.Deterministic(1), iterations=1, aggregation_method="max")
    sample = param.draw_sample()
    samples = param.draw_samples((2, 4))
    assert sample.shape == tuple()
    assert samples.shape == (2, 4)
    assert sample == 1
    assert np.all(samples == 1)

    param = iap.IterativeNoiseAggregator(iap.Choice([0, 50]), iterations=100, aggregation_method="avg")
    sample = param.draw_sample()
    samples = param.draw_samples((2, 4))
    assert sample.shape == tuple()
    assert samples.shape == (2, 4)
    assert 25 - 5 < sample < 25 + 5
    assert np.all(np.logical_or(25 - 5 < samples, samples < 25 + 5))

    param = iap.IterativeNoiseAggregator(iap.Choice([0, 50]), iterations=100, aggregation_method="max")
    sample = param.draw_sample()
    samples = param.draw_samples((2, 4))
    assert sample.shape == tuple()
    assert samples.shape == (2, 4)
    assert sample == 50
    assert np.all(samples == 50)

    param = iap.IterativeNoiseAggregator(iap.Choice([0, 50]), iterations=100, aggregation_method="min")
    sample = param.draw_sample()
    samples = param.draw_samples((2, 4))
    assert sample.shape == tuple()
    assert samples.shape == (2, 4)
    assert sample == 0
    assert np.all(samples == 0)

    seen = [0, 0, 0]
    for _ in sm.xrange(100):
        param = iap.IterativeNoiseAggregator(iap.Choice([0, 50]), iterations=100, aggregation_method=["avg", "max"])
        samples = param.draw_samples((1, 1))
        diff_0 = abs(0 - samples[0, 0])
        diff_25 = abs(25 - samples[0, 0])
        diff_50 = abs(50 - samples[0, 0])
        if diff_25 < 10.0:
            seen[0] += 1
        elif diff_50 < eps:
            seen[1] += 1
        elif diff_0 < eps:
            seen[2] += 1
        else:
            assert False
    assert seen[2] < 5
    assert 50 - 20 < seen[0] < 50 + 20
    assert 50 - 20 < seen[1] < 50 + 20

    param = iap.IterativeNoiseAggregator(iap.Choice([0, 50]), iterations=2, aggregation_method="max")
    samples = param.draw_samples((2, 1000))
    nb_0 = np.sum(samples == 0)
    nb_50 = np.sum(samples == 50)
    assert nb_0 + nb_50 == 2 * 1000
    assert 0.25 - 0.05 < nb_0 / (2 * 1000) < 0.25 + 0.05

    param = iap.IterativeNoiseAggregator(iap.Choice([0, 50]), iterations=5, aggregation_method="avg")
    samples1 = param.draw_samples((100, 10), random_state=np.random.RandomState(1234))
    samples2 = param.draw_samples((100, 10), random_state=np.random.RandomState(1234))
    assert samples1.shape == (100, 10)
    assert samples2.shape == (100, 10)
    assert np.allclose(samples1, samples2)


def test_parameters_Sigmoid():
    reseed()
    eps = np.finfo(np.float32).eps

    param = iap.Sigmoid(iap.Deterministic(5), add=0, mul=1, threshold=0.5, activated=True)
    expected = 1 / (1 + np.exp(-(5 * 1 + 0 - 0.5)))
    sample = param.draw_sample()
    samples = param.draw_samples((5, 10))
    assert sample.shape == tuple()
    assert samples.shape == (5, 10)
    assert expected - eps < sample < expected + eps
    assert np.all(np.logical_or(expected - eps < samples, samples < expected + eps))

    param = iap.Sigmoid(iap.Deterministic(5), add=0, mul=1, threshold=0.5, activated=False)
    expected = 5
    sample = param.draw_sample()
    samples = param.draw_samples((5, 10))
    assert sample.shape == tuple()
    assert samples.shape == (5, 10)
    assert expected - eps < sample < expected + eps
    assert np.all(np.logical_or(expected - eps < samples, samples < expected + eps))

    param = iap.Sigmoid(iap.Deterministic(5), add=0, mul=1, threshold=0.5, activated=0.5)
    expected_first = 5
    expected_second = 1 / (1 + np.exp(-(5 * 1 + 0 - 0.5)))
    seen = [0, 0]
    for _ in sm.xrange(1000):
        sample = param.draw_sample()
        diff_first = abs(sample - expected_first)
        diff_second = abs(sample - expected_second)
        if diff_first < eps:
            seen[0] += 1
        elif diff_second < eps:
            seen[1] += 1
        else:
            assert False
    assert 500 - 150 < seen[0] < 500 + 150
    assert 500 - 150 < seen[1] < 500 + 150

    param = iap.Sigmoid(iap.Choice([1, 10]), add=0, mul=1, threshold=0.5, activated=True)
    expected_first = 1 / (1 + np.exp(-(1 * 1 + 0 - 0.5)))
    expected_second = 1 / (1 + np.exp(-(10 * 1 + 0 - 0.5)))
    seen = [0, 0]
    for _ in sm.xrange(1000):
        sample = param.draw_sample()
        diff_first = abs(sample - expected_first)
        diff_second = abs(sample - expected_second)
        if diff_first < eps:
            seen[0] += 1
        elif diff_second < eps:
            seen[1] += 1
        else:
            assert False
    assert 500 - 150 < seen[0] < 500 + 150
    assert 500 - 150 < seen[1] < 500 + 150

    muls = [0.1, 1, 10.3]
    adds = [-5.7, -1, -0.0734, 0, 0.0734, 1, 5.7]
    vals = [-1, -0.7, 0, 0.7, 1]
    threshs = [-5.7, -1, -0.0734, 0, 0.0734, 1, 5.7]
    for mul in muls:
        for add in adds:
            for val in vals:
                for thresh in threshs:
                    param = iap.Sigmoid(iap.Deterministic(val), add=add, mul=mul, threshold=thresh)
                    sample = param.draw_sample()
                    samples = param.draw_samples((2, 3))
                    assert sample.shape == tuple()
                    assert samples.shape == (2, 3)
                    expected = 1 / (1 + np.exp(-(val * mul + add - thresh)))
                    assert expected - eps < sample < expected + eps
                    assert np.all(np.logical_or(expected - eps < samples, samples < expected + eps))

    param = iap.Sigmoid(iap.Choice([1, 10]), add=0, mul=1, threshold=0.5, activated=True)
    samples1 = param.draw_samples((100, 10), random_state=np.random.RandomState(1234))
    samples2 = param.draw_samples((100, 10), random_state=np.random.RandomState(1234))
    assert samples1.shape == (100, 10)
    assert samples2.shape == (100, 10)
    assert np.array_equal(samples1, samples2)


def test_parameters_operators():
    reseed()

    param1 = iap.Normal(0, 1)
    param2 = iap.Uniform(-1.0, 1.0)

    # Multiply
    param3 = param1 * param2
    assert isinstance(param3, iap.Multiply)
    assert param3.other_param == param1
    assert param3.val == param2

    param3 = param1 * 2
    assert isinstance(param3, iap.Multiply)
    assert param3.other_param == param1
    assert isinstance(param3.val, iap.Deterministic)
    assert param3.val.value == 2

    param3 = 2 * param1
    assert isinstance(param3, iap.Multiply)
    assert isinstance(param3.other_param, iap.Deterministic)
    assert param3.other_param.value == 2
    assert param3.val == param1

    # Divide
    param3 = param1 / param2
    assert isinstance(param3, iap.Divide)
    assert param3.other_param == param1
    assert param3.val == param2

    param3 = param1 / 2
    assert isinstance(param3, iap.Divide)
    assert param3.other_param == param1
    assert isinstance(param3.val, iap.Deterministic)
    assert param3.val.value == 2

    param3 = 2 / param1
    assert isinstance(param3, iap.Divide)
    assert isinstance(param3.other_param, iap.Deterministic)
    assert param3.other_param.value == 2
    assert param3.val == param1

    # Add
    param3 = param1 + param2
    assert isinstance(param3, iap.Add)
    assert param3.other_param == param1
    assert param3.val == param2

    param3 = param1 + 2
    assert isinstance(param3, iap.Add)
    assert param3.other_param == param1
    assert isinstance(param3.val, iap.Deterministic)
    assert param3.val.value == 2

    param3 = 2 + param1
    assert isinstance(param3, iap.Add)
    assert isinstance(param3.other_param, iap.Deterministic)
    assert param3.other_param.value == 2
    assert param3.val == param1

    # Subtract
    param3 = param1 - param2
    assert isinstance(param3, iap.Subtract)
    assert param3.other_param == param1
    assert param3.val == param2

    param3 = param1 - 2
    assert isinstance(param3, iap.Subtract)
    assert param3.other_param == param1
    assert isinstance(param3.val, iap.Deterministic)
    assert param3.val.value == 2

    param3 = 2 - param1
    assert isinstance(param3, iap.Subtract)
    assert isinstance(param3.other_param, iap.Deterministic)
    assert param3.other_param.value == 2
    assert param3.val == param1

    # Power
    param3 = param1 ** param2
    assert isinstance(param3, iap.Power)
    assert param3.other_param == param1
    assert param3.val == param2

    param3 = param1 ** 2
    assert isinstance(param3, iap.Power)
    assert param3.other_param == param1
    assert isinstance(param3.val, iap.Deterministic)
    assert param3.val.value == 2

    param3 = 2 ** param1
    assert isinstance(param3, iap.Power)
    assert isinstance(param3.other_param, iap.Deterministic)
    assert param3.other_param.value == 2
    assert param3.val == param1


def create_random_images(size):
    return np.random.uniform(0, 255, size).astype(np.uint8)


def create_random_keypoints(size_images, nb_keypoints_per_img):
    result = []
    for i in sm.xrange(size_images[0]):
        kps = []
        height, width = size_images[1], size_images[2]
        for i in sm.xrange(nb_keypoints_per_img):
            x = np.random.randint(0, width-1)
            y = np.random.randint(0, height-1)
            kps.append(ia.Keypoint(x=x, y=y))
        result.append(ia.KeypointsOnImage(kps, shape=size_images[1:]))
    return result


def array_equal_lists(list1, list2):
    assert isinstance(list1, list)
    assert isinstance(list2, list)

    if len(list1) != len(list2):
        return False

    for a, b in zip(list1, list2):
        if not np.array_equal(a, b):
            return False

    return True


def keypoints_equal(kps1, kps2, eps=0.001):
    if len(kps1) != len(kps2):
        return False

    for i in sm.xrange(len(kps1)):
        a = kps1[i].keypoints
        b = kps2[i].keypoints
        if len(a) != len(b):
            return False

        for j in sm.xrange(len(a)):
            x_equal = float(b[j].x) - eps <= float(a[j].x) <= float(b[j].x) + eps
            y_equal = float(b[j].y) - eps <= float(a[j].y) <= float(b[j].y) + eps
            if not x_equal or not y_equal:
                return False

    return True


def reseed(seed=0):
    ia.seed(seed)
    np.random.seed(seed)
    random.seed(seed)


if __name__ == "__main__":
    main()
