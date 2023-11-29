import logging
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework import status
from .models import CourseGroup

logger = logging.getLogger(__name__)

def get_int_param(request, param_name):
    try:
        value = int(request.GET.get(param_name))
    except (TypeError, ValueError):
        value = None
        logger.warning('Failed to get integer parameter.')

    return value

@require_http_methods(["GET"])
def submit_course_group(request):
    course_unit_id = get_int_param(request, 'course_unit_id')
    group_number = get_int_param(request, 'group_number')

    if course_unit_id is None or group_number is None:
        logger.warning('Invalid or missing parameters in submit_course_group.', extra={
            'request': request,
            'course_unit_id': course_unit_id,
            'group_number': group_number
        })
        return JsonResponse({'status': 'error', 'message': 'Invalid or missing course_unit_id or group_number'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        course_group, created = CourseGroup.objects.get_or_create(
            course_unit_id=course_unit_id, group_number=group_number,
            defaults={'submit_count': 1}
        )
    except Exception as e:
        logger.error('Failed to create or get CourseGroup.', exc_info=True, extra={
            'request': request,
            'course_unit_id': course_unit_id,
            'group_number': group_number
        })
        return JsonResponse({'status': 'error', 'message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    if not created:
        course_group.submit_count += 1
        course_group.save()

    return JsonResponse({'status': 'success'})

@require_http_methods(["GET"])
def get_course_groups(request):
    course_unit_id = get_int_param(request, 'course_unit_id')

    if course_unit_id is None:
        logger.warning('Invalid or missing course_unit_id in get_course_groups.', extra={
            'request': request,
            'course_unit_id': course_unit_id
        })
        return JsonResponse({'status': 'error', 'message': 'Invalid or missing course_unit_id'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        course_groups = CourseGroup.objects.filter(course_unit_id=course_unit_id)
    except Exception as e:
        logger.error('Failed to filter CourseGroups.', exc_info=True, extra={
            'request': request,
            'course_unit_id': course_unit_id
        })
        return JsonResponse({'status': 'error', 'message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    data = [{'id': cg.id, 'course_unit_id': cg.course_unit_id, 'group_number': cg.group_number, 'submit_count': cg.submit_count} for cg in course_groups]
    return JsonResponse(data, safe=False)
