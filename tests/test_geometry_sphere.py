import specklepy
from bg_specklepy.Geometry.sphere import Sphere

def test_geometry_sphere():

    sphere = Sphere.create()

    assert isinstance(sphere, specklepy.objects.geometry.Mesh)
