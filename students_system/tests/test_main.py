import pytest

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'course_work.settings')


from model_mommy import mommy
from course_work.students_system.models import Adress


@pytest.mark.django_db
def test_address():
    obj = mommy.make(Adress)
    assert str(obj) == 'м. {}, вул. {}, {}, {}'.format(obj.city, obj.street, obj.build, obj.flat)
