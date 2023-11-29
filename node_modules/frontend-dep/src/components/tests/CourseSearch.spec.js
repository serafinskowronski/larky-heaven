import { describe, it, expect } from 'vitest'

import vuetify from '@/plugins/vuetify'
import pinia from '@/store'
import { mount } from '@vue/test-utils'
import CourseSearch from '../CourseSearch.vue'

import ResizeObserver from 'resize-observer-polyfill'
global.ResizeObserver = ResizeObserver

describe('CourseSearch', () => {
  it('renders properly', () => {
    const wrapper = mount(CourseSearch, {
      global: { plugins: [vuetify, pinia] }
    })
    expect(wrapper.text()).toContain('dodaj przedmiot')
  })
})
