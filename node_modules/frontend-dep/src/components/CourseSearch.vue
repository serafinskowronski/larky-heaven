<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { BACKEND_API_URL } from '@/config'

const USOS_API_URL = 'https://usosapps.uw.edu.pl/services'

// Select semester
const select_semester = ref(null)
const items_semester = ref([
  { title: 'Semestr letni 2023/2024 (2023L)', value: '2023L' },
  { title: 'Semestr zimowy 2023 (2023Z)', value: '2023Z' },
  { title: 'Semestr letni 2022/2023 (2022L)', value: '2022L' },
  { title: 'Semestr zimowy 2022 (2022Z)', value: '2022Z' },
  { title: 'Semestr letni 2021/2022 (2021L)', value: '2021L' },
  { title: 'Semestr zimowy 2021 (2021Z)', value: '2021Z' }
])

// Select course
const loading_course = ref(false)
const search_course = ref(null)
const select_course = ref(null)
const items_course = ref([])

async function query_course_search(course_name) {
  loading_course.value = true

  await axios
    .get(USOS_API_URL + '/courses/search', {
      params: {
        lang: 'pl',
        name: course_name,
        fields: 'name|course_id',
        num: 20
      }
    })
    .then(function (response) {
      //console.log(response.data.items[0])
      items_course.value = response.data.items.map((item) => {
        return { title: `${item.name.pl} (${item.course_id})`, value: item.course_id }
      })
    })
    .catch(function (error) {
      console.log(error)
    })
    .finally(function () {
      loading_course.value = false
    })
}

// Load groups
async function query_course_edition(course_id, term_id) {
  let course = null

  await axios
    .get(USOS_API_URL + '/courses/course_edition', {
      params: {
        course_id: course_id,
        term_id: term_id,
        fields: 'course_name|term_id|course_units_ids|course_id'
      }
    })
    .then(function (response) {
      course = response.data
    })
    .catch(function (error) {
      console.log(error)
      throw error
    })
    .finally(function () {})

  return course
}

async function query_course_unit(course_unit_id) {
  let unit = null

  await axios
    .get(USOS_API_URL + '/courses/course_unit', {
      params: {
        course_unit_id: course_unit_id,
        fields: 'id|class_groups'
      }
    })
    .then(function (response) {
      unit = response.data
    })
    .catch(function (error) {
      console.log(error)
      throw error
    })
    .finally(function () {})

  return unit
}

async function query_classgroup_dates(unit_id, group_number) {
  let dates = null

  await axios
    .get(USOS_API_URL + '/tt/classgroup_dates2', {
      params: {
        unit_id: unit_id,
        group_number: group_number
      }
    })
    .then(function (response) {
      dates = response.data
    })
    .catch(function (error) {
      console.log(error)
      throw error
    })
    .finally(function () {})

  return dates
}

async function get_unit(course_unit_id) {
  let unit = await query_course_unit(course_unit_id)

  /*
  // requests are sent one after another
  for (var group of unit.class_groups) {
    group.selected = true
    group.dates = await query_classgroup_dates(group.course_unit_id, group.number)
  }
  */

  // requests are sent asynchronously
  const promises = unit.class_groups.map(async (group) => {
    group.selected = true
    group.dates = await query_classgroup_dates(group.course_unit_id, group.number)
    await axios
    .get(BACKEND_API_URL + 'database_api/get_course_groups/', {
      params: {
        course_unit_id: group.course_unit_id
      }
    })
    .then(function (response) {
      for (let i = 0; i < response.data.length; ++i) {
        if (response.data[i].group_number == group.number) {
          group.submit_count = response.data[i].submit_count
        }
      }
    })
    return group
  })

  unit.class_groups = await Promise.all(promises)

  return unit
}

async function get_course(course_id, term_id) {
  let course = null

  try {
    course = await query_course_edition(course_id, term_id)
    course.units = await Promise.all(
      course.course_units_ids.map((course_unit_id) => get_unit(course_unit_id))
    )
  } catch (error) {
    course = null
    console.log(error)
  }

  return course
}

import { useCoursesStore } from '@/store/coursesStore'
const coursesStore = useCoursesStore()

async function addCourse(course_id, term_id) {
  let course = await get_course(course_id, term_id)
  coursesStore.addCourse(course)
}
</script>

<template>
  <v-list>
    <v-list-item>
      <v-select
        v-model="select_semester"
        :items="items_semester"
        item-title="title"
        item-value="value"
        label="Wybierz semestr"
      ></v-select>
    </v-list-item>

    <v-list-item>
      <v-autocomplete
        v-model="select_course"
        v-model:search="search_course"
        :loading="loading_course"
        :items="items_course"
        item-title="title"
        item-value="value"
        hide-no-data
        hide-details
        label="Wyszukaj przedmiot"
        @keyup.enter="query_course_search(search_course)"
      ></v-autocomplete>
    </v-list-item>

    <v-list-item>
      <v-btn variant="outlined" @click="addCourse(select_course, select_semester)">
        dodaj przedmiot
      </v-btn>
    </v-list-item>
  </v-list>
</template>
