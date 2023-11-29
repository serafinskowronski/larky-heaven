import { describe, it, expect } from 'vitest'

import vuetify from '@/plugins/vuetify'
import pinia from '@/store'
import { mount } from '@vue/test-utils'
import CourseList from '../CourseList.vue'

import ResizeObserver from 'resize-observer-polyfill'
global.ResizeObserver = ResizeObserver

import { useCoursesStore } from '@/store/coursesStore'
import data from '@/tests/course_data.json'

describe('CourseList', () => {
  it('renders properly', async () => {
    const wrapper = mount(CourseList, {
      global: { plugins: [vuetify, pinia] }
    })

    const coursesStore = useCoursesStore()
    coursesStore.courses = data

    await wrapper.vm.$nextTick()

    expect(wrapper.text()).toContain('Matematyka dyskretna')
    expect(wrapper.text()).toContain('Inżynieria oprogramowania')

    const panelTitles = wrapper.findAllComponents({ name: 'v-expansion-panel-title' })
    const panelTitle = panelTitles
      .filter((title) => title.text().includes('Matematyka dyskretna'))
      .at(0)
    await panelTitle.trigger('click')

    const panelContent = wrapper.findComponent({ name: 'v-expansion-panel-text' })

    expect(panelContent.isVisible()).toBe(true)

    expect(panelContent.text()).toContain('Wykład gr. 1')
    expect(panelContent.text()).toContain('Ćwiczenia gr. 9')
  })
})
