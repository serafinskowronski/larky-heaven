from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import CourseGroup

class CourseGroupTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.course_group_1 = CourseGroup.objects.create(course_unit_id=1, group_number=1, submit_count=0)
        self.course_group_2 = CourseGroup.objects.create(course_unit_id=19, group_number=1, submit_count=78)
        self.course_group_3 = CourseGroup.objects.create(course_unit_id=19, group_number=2, submit_count=4)

    
    def test_submit_course_group_ok(self):
        url = reverse('submit_course_group')
        response = self.client.get(url, {'course_unit_id': 1, 'group_number': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_course_group = CourseGroup.objects.get(course_unit_id=1, group_number=1)
        self.assertEqual(updated_course_group.submit_count, 1)

    def test_submit_course_group_create(self):
        url = reverse('submit_course_group')
        response = self.client.get(url, {'course_unit_id': 13, 'group_number': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_course_group = CourseGroup.objects.get(course_unit_id=13, group_number=1)
        self.assertEqual(updated_course_group.submit_count, 1)

    def test_submit_course_group_invalid(self):
        url = reverse('submit_course_group')
        response = self.client.get(url, {'course_unit_id': 'invalid', 'group_number': 1})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.get(url, {'course_unit_id': 1})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_course_groups_1(self):
        url = reverse('get_course_groups')
        response = self.client.get(url, {'course_unit_id': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.course_group_1.course_unit_id)
        self.assertContains(response, self.course_group_1.group_number)
        self.assertContains(response, self.course_group_1.submit_count)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['course_unit_id'], 1)
        self.assertEqual(response.json()[0]['group_number'], 1)
        self.assertEqual(response.json()[0]['submit_count'], 0)

    def test_get_course_groups_2(self):
        url = reverse('get_course_groups')
        response = self.client.get(url, {'course_unit_id': 19})
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertContains(response, self.course_group_2.course_unit_id)
        self.assertContains(response, self.course_group_2.group_number)
        self.assertContains(response, self.course_group_2.submit_count)

        self.assertContains(response, self.course_group_3.course_unit_id)
        self.assertContains(response, self.course_group_3.group_number)
        self.assertContains(response, self.course_group_3.submit_count)

    def test_get_course_groups_invalid(self):
        url = reverse('get_course_groups')
        response = self.client.get(url, {'course_unit_id': 'invalid'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.get(url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.get(url, {'course_unit_id': 13})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


