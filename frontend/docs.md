# Documentation

### Type of data that is stored in `coursesStore`
```
courses: [
  {
    // from services/courses/course_edition
    "course_name": {
        "pl": "Matematyka dyskretna",
        "en": "Discrete mathematics"
    },
    "term_id": "2022L",
    "course_units_ids": [
        "486449",
        "486450"
    ],
    "course_id": "1000-212bMD"

    // added
    units: [
      {
        // from services/courses/course_unit
        "class_groups": [
          {
              "course_unit_id": "486450",
              "number": 1

              // from services/tt/classgroup_dates2
              dates: [
                {
                  "start_time": "2023-02-27 12:15:00",
                  "end_time": "2023-02-27 14:00:00",
                  "name": {
                      "pl": "Ćwiczenia",
                      "en": "Class"
                  }
                },
                {
                  "start_time": "2023-03-03 10:15:00",
                  "end_time": "2023-03-03 12:00:00",
                  "name": {
                      "pl": "Ćwiczenia",
                      "en": "Class"
                  }
                },
              ]

              "selected": true // added
          },
          {
              "course_unit_id": "486450",
              "number": 2
          },
          {
              "course_unit_id": "486450",
              "number": 3
          },
          {
              "course_unit_id": "486450",
              "number": 4
          },
          {
              "course_unit_id": "486450",
              "number": 5
          },
          {
              "course_unit_id": "486450",
              "number": 6
          },
          {
              "course_unit_id": "486450",
              "number": 7
          },
          {
              "course_unit_id": "486450",
              "number": 8
          },
          {
              "course_unit_id": "486450",
              "number": 9
          }
        ]

        "id": 486450 // added for redundancy
      }
    ]
  }
]
```