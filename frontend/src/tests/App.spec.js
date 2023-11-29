import { describe, it, expect } from 'vitest'

import vuetify from '@/plugins/vuetify'
import pinia from '@/store'
import { mount } from '@vue/test-utils'
import App from '@/App.vue'

import ResizeObserver from 'resize-observer-polyfill'
global.ResizeObserver = ResizeObserver

describe('some test', () => {
  it('initializes message_sent properly', () => {
    const wrapper = mount(App, {
      global: { plugins: [vuetify, pinia] }
    })
    expect(wrapper.text()).toContain('PlanDoskonały')
  })
})
