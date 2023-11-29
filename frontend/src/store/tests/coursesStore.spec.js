import { describe, it, expect } from 'vitest'

import ResizeObserver from 'resize-observer-polyfill'
global.ResizeObserver = ResizeObserver

import { createPinia } from 'pinia'
import { useCoursesStore } from '@/store/coursesStore'

describe('coursesStore', () => {
  let store

  beforeEach(() => {
    // Create a new store before each test
    const pinia = createPinia()
    store = useCoursesStore(pinia)
  })

  it('adds a course', () => {
    const course = { course_id: '1', term_id: '1', name: 'course' }

    store.addCourse(course)

    expect(store.courses).toHaveLength(1)
    expect(store.courses[0]).toEqual(course)
  })

  it('overwrites an existing course', () => {
    const course = { course_id: '1', term_id: '1', name: 'course' }
    const newCourse = { course_id: '1', term_id: '1', name: 'new course' }

    store.addCourse(course)
    store.addCourse(newCourse)

    expect(store.courses).toHaveLength(1)
    expect(store.courses[0]).toEqual(newCourse)
  })

  it('deletes a course', () => {
    const course = { course_id: '1', term_id: '1', name: 'course' }

    store.addCourse(course)
    store.deleteCourse(course.course_id, course.term_id)

    expect(store.courses).toHaveLength(0)
  })
})
