const API_URL = "http://localhost:8000";
const API_KEY = "gym-secret-key";


// ======================================================
// HELPER FUNCTION
// ======================================================

async function apiRequest(url, options = {}) {
    try {
        const response = await fetch(url, options);

        if (!response.ok) {
            let errorMessage = "Request failed";

            try {
                const errorData = await response.json();
                errorMessage = errorData.detail || errorMessage;
            } catch (error) {
                errorMessage =` HTTP error ${response.status}`;
            }

            throw new Error(errorMessage);
        }

        return await response.json();

    } catch (error) {
        alert(error.message);
        throw error;
    }
}


// ======================================================
// MEMBERS
// ======================================================

async function loadMembers() {
    const membersList = document.getElementById("members-list");

    try {
        const members = await apiRequest(
            `${API_URL}/members/`
        );

        membersList.innerHTML = "";

        members.forEach((member) => {
            const item = document.createElement("div");
            item.className = "item";

            item.innerHTML = `
                <strong>ID:</strong> ${member.id}<br>
                <strong>Name:</strong> ${member.name}<br>
                <strong>Email:</strong> ${member.email}
            `;

            membersList.appendChild(item);
        });

    } catch (error) {
        membersList.innerHTML =
            `<div class="error">${error.message}</div>`;
    }
}


document
    .getElementById("load-members")
    .addEventListener("click", loadMembers);


document
    .getElementById("member-form")
    .addEventListener("submit", async function (event) {
        event.preventDefault();

        const name =
            document.getElementById("member-name").value;

        const email =
            document.getElementById("member-email").value;

        const member = {
            name: name,
            email: email
        };

        try {
            await apiRequest(
                `${API_URL}/members/`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json",
                        "X-API-Key": API_KEY
                    },

                    body: JSON.stringify(member)
                }
            );

            alert("Member added successfully");

            this.reset();

            loadMembers();

        } catch (error) {
            console.error(error);
        }
    });


// ======================================================
// COURSES
// ======================================================

async function loadCourses() {
    const coursesList = document.getElementById("courses-list");

    try {
        const courses = await apiRequest(
            `${API_URL}/courses/`
        );

        coursesList.innerHTML = "";

        courses.forEach((course) => {
            const item = document.createElement("div");
            item.className = "item";

            item.innerHTML = `
                <strong>ID:</strong> ${course.id}<br>
                <strong>Name:</strong> ${course.name}<br>
                <strong>Trainer:</strong> ${course.trainer}<br>
                <strong>Schedule:</strong> ${course.schedule}
            `;

            coursesList.appendChild(item);
        });

    } catch (error) {
        coursesList.innerHTML =
            `<div class="error">${error.message}</div>`;
    }
}


document
    .getElementById("load-courses")
    .addEventListener("click", loadCourses);


document
    .getElementById("course-form")
    .addEventListener("submit", async function (event) {
        event.preventDefault();

        const name =
            document.getElementById("course-name").value;

        const trainer =
            document.getElementById("course-trainer").value;

        const schedule =
            document.getElementById("course-schedule").value;

        const course = {
            name: name,
            trainer: trainer,
            schedule: schedule
        };

        try {
            await apiRequest(
                `${API_URL}/courses/`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json",
                        "X-API-Key": API_KEY
                    },

                    body: JSON.stringify(course)
                }
            );

            alert("Course added successfully");

            this.reset();

            loadCourses();

        } catch (error) {
            console.error(error);
        }
    });


// ======================================================
// REGISTRATIONS
// ======================================================

async function loadRegistrations() {
    const registrationsList =
        document.getElementById("registrations-list");

    try {
        const registrations = await apiRequest(
            `${API_URL}/registrations/`
        );

        registrationsList.innerHTML = "";

        registrations.forEach((registration) => {
            const item = document.createElement("div");
            item.className = "item";

            item.innerHTML = `
                <strong>ID:</strong> ${registration.id}<br>
                <strong>Member ID:</strong> ${registration.member_id}<br>
                <strong>Course ID:</strong> ${registration.course_id}
            `;

            registrationsList.appendChild(item);
        });

    } catch (error) {
        registrationsList.innerHTML =

            `<div class="error">${error.message}</div>`;
    }
}


document
    .getElementById("load-registrations")
    .addEventListener("click", loadRegistrations);


document
    .getElementById("registration-form")
    .addEventListener("submit", async function (event) {
        event.preventDefault();

        const memberId =
            Number(
                document.getElementById(
                    "registration-member-id"
                ).value
            );

        const courseId =
            Number(
                document.getElementById(
                    "registration-course-id"
                ).value
            );

        const registration = {
            member_id: memberId,
            course_id: courseId
        };

        try {
            await apiRequest(
                `${API_URL}/registrations/`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json",
                        "X-API-Key": API_KEY
                    },

                    body: JSON.stringify(registration)
                }
            );

            alert("Member registered successfully");

            this.reset();

            loadRegistrations();

        } catch (error) {
            console.error(error);
        }
    });


// ======================================================
// PAYMENTS
// ======================================================

async function loadPayments() {
    const paymentsList =
        document.getElementById("payments-list");

    try {
        const payments = await apiRequest(
            `${API_URL}/payments/`
        );

        paymentsList.innerHTML = "";

        payments.forEach((payment) => {
            const item = document.createElement("div");
            item.className = "item";

            item.innerHTML = `
                <strong>ID:</strong> ${payment.id}<br>
                <strong>Member ID:</strong> ${payment.member_id}<br>
                <strong>Amount:</strong> ${payment.amount} €<br>
                <strong>Date:</strong> ${payment.payment_date}
            `;

            paymentsList.appendChild(item);
        });

    } catch (error) {
        paymentsList.innerHTML =
            `<div class="error">${error.message}</div>`;
    }
}


document
    .getElementById("load-payments")
    .addEventListener("click", loadPayments);


document
    .getElementById("payment-form")
    .addEventListener("submit", async function (event) {
        event.preventDefault();

        const memberId =
            Number(
                document.getElementById(
                    "payment-member-id"
                ).value
            );

        const amount =
            Number(
                document.getElementById(
                    "payment-amount"
                ).value
            );

        const paymentDate =
            document.getElementById(
                "payment-date"
            ).value;

        const payment = {
            member_id: memberId,
            amount: amount,
            payment_date: paymentDate
        };

        try {
            await apiRequest(
                `${API_URL}/payments/`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json",
                        "X-API-Key": API_KEY
                    },

                    body: JSON.stringify(payment)
                }
            );

            alert("Payment added successfully");

            this.reset();

            loadPayments();

        } catch (error) {
            console.error(error);
        }
    });
