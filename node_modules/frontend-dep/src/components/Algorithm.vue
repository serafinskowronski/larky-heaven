<template>
    <div>
    <v-btn
        @click="run();coursesStore.submitCourses()"
    >
    Stwórz plan doskonały!
    </v-btn>
    {{ errorMessage }}
    <keep-alive>
        <ejs-schedule ref='scheduleObj' height='100%' width='100%' :selectedDate='selectedDate' 
        :eventSettings='eventSettings'
        id='Schedule'>
            <e-views>
                <e-view option='Day' startHour="8:00" endHour="20:00"></e-view>
                <e-view option='Week' startHour="8:00" endHour="20:00"></e-view>
                <e-view option='WorkWeek' startHour="8:00" endHour="20:00"></e-view>
                <e-view option='Month' startHour="8:00" endHour="20:00"></e-view>
                <e-view option='Agenda' startHour="8:00" endHour="20:00"></e-view>
            </e-views>
            <e-resources>
                <e-resource field="OwnerId" title="Owner" name="Owners" :dataSource="ownerDataSource" textField="OwnerText"
                idField="Id" colorField="OwnerColor">
                </e-resource>
            </e-resources>
        </ejs-schedule>
    </keep-alive>
    </div>
</template>

<script setup>
import { useCoursesStore } from '@/store/coursesStore'
import { provide, ref, onBeforeMount } from "vue"
import {
  ScheduleComponent as EjsSchedule, ViewsDirective as EViews, ViewDirective as EView,
  ResourcesDirective as EResources, ResourceDirective as EResource,
  Day, Week, WorkWeek, Month, Agenda
} from "@syncfusion/ej2-vue-schedule"
import { registerLicense } from '@syncfusion/ej2-base'

// Registering Syncfusion license key
registerLicense('Mgo+DSMBaFt+QHJqVk1hXk5Hd0BLVGpAblJ3T2ZQdVt5ZDU7a15RRnVfRF1rSXZTdkBjWn5ZeA==;Mgo+DSMBPh8sVXJ1S0R+X1pFdEBBXHxAd1p/VWJYdVt5flBPcDwsT3RfQF5jT35bdk1jWXpec3ddTg==;ORg4AjUWIQA/Gnt2VFhiQlJPd11dXmJWd1p/THNYflR1fV9DaUwxOX1dQl9gSXhTfkVrWX9bcHdQQGg=;MjM1OTU3NUAzMjMxMmUzMDJlMzBmWW54elhhQ0FPTTZKTTh3bzZNTy81aWJvRnhCZVFQMjhWSzl0SEllTkt3PQ==;MjM1OTU3NkAzMjMxMmUzMDJlMzBVZTZOdVArbTVwUDRHRVNlc2J2b1l3YU01d3V5ZU9HMlg2TkFPK3Y4dFBvPQ==;NRAiBiAaIQQuGjN/V0d+Xk9HfV5AQmBIYVp/TGpJfl96cVxMZVVBJAtUQF1hSn5Vdk1jUX9edXRRQmhU;MjM1OTU3OEAzMjMxMmUzMDJlMzBNOUZnOTg4V1A1cXJ4bTlOVGZwNjhYdlMzWlVwRzhoUm41OW1kVUk2Z0k4PQ==;MjM1OTU3OUAzMjMxMmUzMDJlMzBTMDYydm1pOUNWYU9RemUvemluNFA2UXdwdkt1VWhQVjVHQXk1VkNMbXVnPQ==;Mgo+DSMBMAY9C3t2VFhiQlJPd11dXmJWd1p/THNYflR1fV9DaUwxOX1dQl9gSXhTfkVrWX9bcHFWQmg=;MjM1OTU4MUAzMjMxMmUzMDJlMzBaMFgzSWpyTEQ3c3h2Q0hEbm5RODdJMlRtUitGMURlZ0JSZzM0VjV5RUdVPQ==;MjM1OTU4MkAzMjMxMmUzMDJlMzBaeXF6bUJoTURUWWZJc2orbVlsbWJ5dFEyMGZ0THRHS1lSR0FNSkJJWkVRPQ==;MjM1OTU4M0AzMjMxMmUzMDJlMzBNOUZnOTg4V1A1cXJ4bTlOVGZwNjhYdlMzWlVwRzhoUm41OW1kVUk2Z0k4PQ==');

provide('schedule', [Day, Week, WorkWeek, Month, Agenda]);

let selectedDate = new Date() // current date

let eventSettings = {
  dataSource: [
  ]
}

const ownerDataSource = [
  { OwnerText: "", Id: 1, OwnerColor: "#ffaa00" },
  { OwnerText: "", Id: 2, OwnerColor: "#f8a398" },
  { OwnerText: "", Id: 3, OwnerColor: "#7499e1" },
  { OwnerText: "", Id: 4, OwnerColor: "#d80020" },
  { OwnerText: "", Id: 5, OwnerColor: "#cdb1fd" },
  { OwnerText: "", Id: 6, OwnerColor: "#63072a" },
  { OwnerText: "", Id: 7, OwnerColor: "#51fb36" },
  { OwnerText: "", Id: 8, OwnerColor: "#f3de74" },
  { OwnerText: "", Id: 9, OwnerColor: "#f49855" },
  { OwnerText: "", Id: 10, OwnerColor: "#09207f" }
]

const coursesStore = useCoursesStore()

let errorMessage = ref('')
let cand = ref([])
let best = ref(10000000)

async function rec(mask, len, n_valid_groups, collisions) {
    if (mask.length < len) {
        for (let j = 0; j < n_valid_groups[mask.length]; ++j) {
            mask.push(j)
            await rec(mask, len, n_valid_groups, collisions)
            mask.pop(j)
        }
    } else {
        let n_collisions = 0, j_prefix_sum = 0
        for (let j = 0; j < mask.length; ++j) {
            j_prefix_sum += mask[j]
            let k_prefix_sum = 0
            for (let k = 0; k < mask.length; ++k) {
                k_prefix_sum += mask[k]
                if (j_prefix_sum != k_prefix_sum) {
                    n_collisions += collisions[j_prefix_sum][k_prefix_sum];
                }
                k_prefix_sum -= mask[k]
                k_prefix_sum += n_valid_groups[k]
            }
            j_prefix_sum -= mask[j]
            j_prefix_sum += n_valid_groups[j]
        }
        let ok = true
        for (let j = 0; j < mask.length; ++j) {
            let ctr = 0
            for (const unit of coursesStore.courses[j].units) if (unit.class_groups[0].dates[0].name.pl != 'Wykład') {
                for (const group of unit.class_groups) {
                    if (mask[j] == ctr && group.selected == false) {
                        ok = false
                    }
                    ++ctr
                }
            }
        }
        if (!ok) {
            return;
        }
        if (n_collisions == 0) {
            let potential = 0
            const min_max = new Map()
            for (let j = 0; j < mask.length; ++j) {
                let ctr = 0
                for (const unit of coursesStore.courses[j].units) if (unit.class_groups[0].dates[0].name.pl != 'Wykład') {
                    for (const group of unit.class_groups) {
                        if (mask[j] == ctr) for (const date of group.dates) {
                            let key = date.start_time.substr(0, date.start_time.indexOf(" "))
                            if (!min_max.has(key)) {
                                min_max.set(key, {
                                    min: 10000000,
                                    max: 0
                                })
                            }
                            let current = min_max.get(key)
                            min_max.set(key, {
                                min: Math.min(current.min, (new Date(date.start_time)).getHours() * 60 + (new Date(date.start_time)).getMinutes()),
                                max: Math.max(current.max, (new Date(date.end_time)).getHours() * 60 + (new Date(date.end_time)).getMinutes())
                            })
                        }
                        ++ctr;
                    }
                }
            }
            for (const [key, value] of min_max) {
                potential += value.max - value.min;
            }
            if (potential < best.value) {
                best.value = potential
                cand.value = []
                for (let elt of mask) {
                    cand.value.push(elt)
                }
            }
        }
    }
}

async function run() {
    cand.value = []
    best.value = 100000000
    errorMessage.value = ''
    let scheduleObj = document.getElementById('Schedule').ej2_instances[0]
    for (let i = 0; i < 10000; ++i) {
        scheduleObj.deleteEvent(i)
    }
    if (coursesStore.courses.length == 0) {
        errorMessage.value = 'Nie wybrano żadnego przedmiotu!'
        return
    }
    // preprocessing
    let n_groups = 0, n_valid_groups = []
    for (const course of coursesStore.courses) {
        let sum = 0
        for (const unit of course.units) {
            if (unit.class_groups[0].dates[0].name.pl != 'Wykład') {
                sum += unit.class_groups.length
            }
        }
        n_valid_groups.push(sum)
        n_groups += sum
    }
    let collisions = Array(n_groups).fill().map(() => Array(n_groups).fill(0));
    let id_1 = 0, id_2 = 0;
    for (let i_1 = 0; i_1 < coursesStore.courses.length; ++i_1) {
        for (const unit_1 of coursesStore.courses[i_1].units) if (unit_1.class_groups[0].dates[0].name.pl != 'Wykład') {
            for (const group_1 of unit_1.class_groups) {
                id_2 = 0;
                for (let i_2 = 0; i_2 < coursesStore.courses.length; ++i_2) {
                    for (const unit_2 of coursesStore.courses[i_2].units) if (unit_2.class_groups[0].dates[0].name.pl != 'Wykład') {
                        for (const group_2 of unit_2.class_groups) {
                            if (id_1 != id_2) {
                                for (const date_1 of group_1.dates) {
                                    for (const date_2 of group_2.dates) {
                                        let beg_mx = Math.max((new Date(date_1.start_time)).getTime(), (new Date(date_2.start_time)).getTime())
                                        let end_mn = Math.min((new Date(date_1.end_time)).getTime(), (new Date(date_2.end_time)).getTime())
                                        if (end_mn > beg_mx) {
                                            collisions[id_1][id_2]++;
                                        }
                                    }
                                }
                            }
                            id_2++
                        }
                    }
                }
                id_1++;
            }
        }
    }
    await rec([], n_valid_groups.length, n_valid_groups, collisions)
    if (cand.value.length > 0) {
        let ctr = 0, next_id = 0
        scheduleObj = document.getElementById('Schedule').ej2_instances[0]
        for (let j = 0; j < cand.value.length; ++j) {
            ctr = 0
            for (const unit of coursesStore.courses[j].units) {
                for (const group of unit.class_groups) {
                    if (cand.value[j] == ctr || unit.class_groups[0].dates[0].name.pl == 'Wykład') for (const date of group.dates) {
                        scheduleObj.addEvent({
                            Id: next_id++,
                            OwnerId: j,
                            EventType: unit.class_groups[0].dates[0].name.pl == 'Wykład' ? 'Common' : 'Confirmed',
                            Subject: coursesStore.courses[j].course_name.pl + " " + date.name.pl + " " + group.number,
                            StartTime: new Date(date.start_time),
                            EndTime: new Date(date.end_time)
                        })
                    }
                    if (unit.class_groups[0].dates[0].name.pl != 'Wykład') {
                        ++ctr;
                    }
                }
            }
        }
    } else {
        errorMessage.value = 'Brak planu doskonałego:('
    }
}
</script>

<style>
    @import '../../node_modules/@syncfusion/ej2-base/styles/material.css';
    @import '../../node_modules/@syncfusion/ej2-buttons/styles/material.css';
    @import '../../node_modules/@syncfusion/ej2-calendars/styles/material.css';
    @import '../../node_modules/@syncfusion/ej2-dropdowns/styles/material.css';
    @import '../../node_modules/@syncfusion/ej2-inputs/styles/material.css';
    @import '../../node_modules/@syncfusion/ej2-navigations/styles/material.css';
    @import '../../node_modules/@syncfusion/ej2-popups/styles/material.css';
    @import '../../node_modules/@syncfusion/ej2-vue-schedule/styles/material.css';
</style>