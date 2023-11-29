import { defineStore } from 'pinia'
import axios from 'axios'
import { BACKEND_API_URL } from '@/config'

export const useCoursesStore = defineStore('coursesStore', {
  state: () => ({
    courses: []
  }),

  actions: {
    addCourse(course) {
      if (!course) return

      // Find the index of the course in the store
      const courseIndex = this.courses.findIndex(
        (c) => c.course_id === course.course_id && c.term_id === course.term_id
      )

      // If course already exists in the store, overwrite it
      if (courseIndex > -1) {
        this.courses[courseIndex] = course
      } else {
        // If course doesn't exist, add it to the store
        this.courses.push(course)
      }
    },

    deleteCourse(course_id, term_id) {
      // Find the index of the course in the store
      const index = this.courses.findIndex(
        (c) => c.course_id === course_id && c.term_id === term_id
      )
      // If the course is found, remove it from the store
      if (index > -1) {
        this.courses.splice(index, 1)
      }
    },

    async increaseCounter() {
      await axios
        .get(BACKEND_API_URL + 'database_api/submit_course_group', {
          params: {
            course_unit_id: 0,
            group_number: 0
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    },

    async submitCourses() {
      // Iterate over all selected groups and submit them to backend
      this.courses.map(async (course) => {
        course.units.map(async (unit) => {
          unit.class_groups.map(async (group) => {
            if (!group.selected) return
            await axios
              .get(BACKEND_API_URL + 'database_api/submit_course_group', {
                params: {
                  course_unit_id: group.course_unit_id,
                  group_number: group.number
                }
              })
              .catch(function (error) {
                console.log(error)
              })
          })
        })
      })
    }
  }
})
