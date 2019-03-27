In this project, we will create the frontend for the classroom's api using React Native. This application's users are teachers. They can create new classrooms, edit or delete their own classrooms. Inside their classroom, they can add new students, edit or delete their existing students.

Here are the APIs you'll need:

**Base URL**
`http://127.0.0.1:8000/api/`

**URLs**

- Sign up a new user: `user/register/`
- Log in a user: `user/login/`

- Fetch all classrooms: `classrooms/list/`
- Fetch a classroom's details: `classrooms/detail/<int:classroom_id>/`
- Create a new classroom: `classrooms/create/`
- Update a classroom: `classrooms/update/<int:classroom_id>/`
- Delete a classroom: `classrooms/delete/<int:classroom_id>/`

- Create a new student: `students/create/`
- Update a student: `students/update/<int:student_id>/`
- Delete a student: `students/delete/<int:student_id>/`

Add the following features to your application:

**User**

- The teacher can sign up, log in and log out
- The teacher has a profile page

**Classrooms**

- The teacher can create a new classroom
- The teacher can view a list of all classrooms
- Clicking on a classroom takes the teacher to its detail page
- The teacher can edit and delete her classrooms only

**Students**

- Every classroom detail page has a list of students. Only the classroom's teacher can view her students.
- The teacher can add new students to her classrooms only
- The teacher can edit and delete her students

**BONUS**

- The teacher can edit her profile
- The teacher can view a list of her classrooms only
- The teacher can filter for classrooms by subject, year and grade
- The teacher can filter students by grade (ex: show students with grades higher than 90 or less than 70)
- The teacher can search for students by name
