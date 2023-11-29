<script setup>
import { useCoursesStore } from '@/store/coursesStore'
import axios from 'axios';
import { BACKEND_API_URL } from '@/config'
const coursesStore = useCoursesStore()
const handleShow = async () => {
  await axios
    .get(BACKEND_API_URL + 'database_api/get_course_groups/', {
      params: {
        course_unit_id: 0
      }
    })
    .then(function (response) {
      console.log(response.data[0].submit_count)
    })
}
</script>

<template>
  <v-app id="inspire">
    <div id="root">
      <p id="title">Welcome in Larky Heaven!</p>
      <a href="ticket.txt" download id="submitButton" @click="async () => {coursesStore.increaseCounter();await handleShow();}">Get your ticket</a>
    </div>
  </v-app>
</template>
